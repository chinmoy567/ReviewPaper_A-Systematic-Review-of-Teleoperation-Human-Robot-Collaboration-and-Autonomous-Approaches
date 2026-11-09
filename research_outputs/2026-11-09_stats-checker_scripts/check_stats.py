import pandas as pd, numpy as np, os, math, itertools
from scipy.stats import fisher_exact, mannwhitneyu
from scipy.stats.contingency import odds_ratio
from scipy.special import gammaln

def pc(k,n,method='wilson'):
    from scipy.stats import norm
    z=norm.ppf(.975);p=k/n;dd=1+z*z/n;c=(p+z*z/(2*n))/dd;h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/dd
    return max(0,c-h),min(1,c+h)
def cohen_kappa_score(a,b):
    a=np.asarray(a);b=np.asarray(b);po=np.mean(a==b);cs=set(a)|set(b)
    pe=sum(np.mean(a==c)*np.mean(b==c) for c in cs);return (po-pe)/(1-pe)

os.chdir(r"C:\Users\chinmoy\Downloads\review paper")
d = pd.read_csv('data/extraction_table.csv', dtype=str)
assert len(d) == 39


def W(k, n):
    lo, hi = pc(k, n, method='wilson')
    return f"{k}/{n} {100*k/n:.1f}% [{100*lo:.1f}-{100*hi:.1f}]"


for c in ['mode_clean', 'platform_clean', 'validation_strict', 'validation_lenient', 'architecture_clean',
          'scenario_clean', 'fa_cluster', 'vd', 'rp', 'vdr', 'human_role_modelled', 'env_realism_limitation',
          'env_realism_broad', 'stat']:
    print('\n==', c)
    print(d[c].value_counts(dropna=False).to_string())
print('\nWilson mode')
for m, k in d.mode_clean.value_counts().items():
    print(m, W(k, 39))
print('sensors')
for s in [c for c in d.columns if c.startswith('s_')]:
    print(s, W((d[s] == '1').sum(), 39))
print(pd.crosstab(d.mode_clean, d.validation_strict, margins=True))
print(pd.crosstab(d.platform_clean, d.validation_strict, margins=True))
print(pd.crosstab(d.validation_lenient, d.validation_strict, margins=True))
print(pd.crosstab(d.mode_clean, d.platform_clean, margins=True))
print(pd.crosstab(d.mode_clean, d.validation_lenient, margins=True))
print(pd.crosstab(d.fa_cluster, d.validation_strict, margins=True))
FA = d.mode_clean == 'Fully Autonomous'
HM = ~FA
TS = d.mode_clean.isin(['Teleoperation', 'Supervisory Control'])
fs = d.validation_strict == 'Real-world field test'
fl = d.validation_lenient == 'Real-world field test'
ph = d.validation_strict != 'Simulation only'
vd3 = d.vd == '3'


def C(lab, a, b):
    A = a.sum(); nA = len(a); B = b.sum(); nB = len(b)
    t = [[A, nA - A], [B, nB - B]]
    p = fisher_exact(t)[1]
    o = odds_ratio(t, kind='conditional'); ci = o.confidence_interval(0.95)
    print(f"{lab}: {A}/{nA} vs {B}/{nB}  OR {o.statistic:.3f} [{ci.low:.4f}-{ci.high:.3f}] p={p:.4f}")


C('field strict FA v HM', fs[FA], fs[HM]); C('field lenient', fl[FA], fl[HM]); C('any phys', ph[FA], ph[HM]); C('VD3', vd3[FA], vd3[HM])
C('strict FA v T+S', fs[FA], fs[TS]); C('lenient FA v T+S', fl[FA], fl[TS])
uav = d.platform_clean == 'UAV'; hyb = d.platform_clean.str.startswith('Hybrid')
C('UAV v Hybrid strict', fs[uav], fs[hyb]); C('UAV v Hybrid lenient', fl[uav], fl[hyb])
print('UGV lenient field', fl[d.platform_clean == 'UGV'].sum(), 'UAV lenient', fl[uav].sum(), 'hyb lenient', fl[hyb].sum())
gen = d.scenario_clean.str.startswith('Generic'); lim = d.env_realism_limitation == 'Y'; br = d.env_realism_broad == 'Y'
C('realism generic v spec', lim[gen], lim[~gen])
print(W(lim.sum(), 39), W(br.sum(), 39), lim[gen].sum(), gen.sum(), lim[~gen].sum(), (~gen).sum(), br[gen].sum(), br[~gen].sum())
rp3 = d.rp == '3'
print('RP3', W(rp3.sum(), 39), 'stat Y', (d.stat == 'Y').sum())
v = d.vd.astype(int); r = d.rp.astype(int); vr = d.vdr.astype(int)
print('MW VD', mannwhitneyu(v[FA], v[HM], alternative='two-sided'), v[FA].mean(), v[HM].mean())
print('MW RP', mannwhitneyu(r[FA], r[HM], alternative='two-sided'), r[FA].mean(), r[HM].mean())
print(d.assign(v=v, r=r, vr=vr).groupby('mode_clean')[['v', 'r', 'vr']].mean().round(3)); print(v.mean(), vr.mean())
print('VDR = VD+RP check', (vr == v + r).all())
print(pd.crosstab(d.mode_clean, d.human_role_modelled))
print('any phys by mode'); print(ph.groupby(d.mode_clean).agg(['sum', 'count'])); print(ph.sum())
print('lenient field by mode', fl.groupby(d.mode_clean).sum().to_dict())
for lab, fld in [('strict', fs), ('lenient', fl)]:
    print(lab, 'Wilson per mode')
    for m in d.mode_clean.unique():
        mk = d.mode_clean == m; print(' ', m, W(fld[mk].sum(), mk.sum()))
    print(' HM', W(fld[HM].sum(), 12), ' all', W(fld.sum(), 39), ' FA', W(fld[FA].sum(), 27))
for lab, o in [('phys', ph), ('vd3', vd3)]:
    print(lab, 'FA', W(o[FA].sum(), 27), 'HM', W(o[HM].sum(), 12))
ok = (d.platform_clean != 'Abstract / Unspecified') & (d.s_none != '1')
print('phys platform subset', ok.sum(), (FA & ok).sum(), (HM & ok).sum(), 'removed FA', (FA & ~ok).sum(), 'removed HM', (HM & ~ok).sum())


def S(lab, mask, fa=FA):
    f = mask & fa; h = mask & ~fa; out = []
    for o in [fs, fl, ph]:
        a = o[f].sum(); b = o[h].sum()
        out.append(f"{a}/{f.sum()} v {b}/{h.sum()} p={fisher_exact([[a, f.sum()-a], [b, h.sum()-b]])[1]:.3f}")
    print(lab, f.sum(), h.sum(), out)


S('primary', pd.Series(True, index=d.index)); S('a', ok); S('b RP>=2', r >= 2)
b = pd.read_csv('data/reliability_blind_codes.csv', dtype=str)
print(b.columns.tolist())
m = {'T': 'Teleoperation', 'S': 'Supervisory Control', 'C': 'Shared-Collaborative Control', 'F': 'Fully Autonomous'}
bm = d.ref_N.map(dict(zip(b.ref_N, b.blind_mode))).map(m)
FAb = bm == 'Fully Autonomous'
S('c blind', pd.Series(True, index=d.index), FAb)
print('agree 4-mode', (bm == d.mode_clean).sum(), 'binary', (FAb == FA).sum())
print(pd.DataFrame({'ref': d.ref_N, 'orig': d.mode_clean, 'blind': bm})[bm != d.mode_clean])
print('kappa4', cohen_kappa_score(d.mode_clean, bm), 'kappa bin', cohen_kappa_score(FA, FAb))


def ac1(a, b):
    cats = sorted(set(a) | set(b)); n = len(a); pa = np.mean(np.array(a) == np.array(b))
    pi = [(sum(x == c for x in a) + sum(x == c for x in b)) / (2 * n) for c in cats]
    pe = sum(p * (1 - p) for p in pi) / (len(cats) - 1)
    return (pa - pe) / (1 - pe)


print('AC1', ac1(list(d.mode_clean), list(bm)))
po = np.mean(d.mode_clean == bm); cats = d.mode_clean.unique()
pe = sum((d.mode_clean == c).mean() * (bm == c).mean() for c in cats); k = (po - pe) / (1 - pe)
se = math.sqrt(po * (1 - po) / (39 * (1 - pe) ** 2)); print('kappa simple CI', k, k - 1.96 * se, k + 1.96 * se)
# Fleiss-Cohen analytic SE (large sample)
n = 39
pm = [((d.mode_clean == c).mean(), (bm == c).mean()) for c in cats]
A = sum((d.mode_clean == c).mean() * 0 for c in cats)
rng = np.random.default_rng(0); ks = []
for _ in range(5000):
    i = rng.integers(0, 39, 39)
    a_ = d.mode_clean.values[i]; b_ = bm.values[i]
    if len(set(a_)) < 2 and len(set(b_)) < 2: continue
    ks.append(cohen_kappa_score(a_, b_))
print('kappa boot', np.nanpercentile(ks, [2.5, 97.5]))
modes = ['Teleoperation', 'Supervisory Control', 'Shared-Collaborative Control', 'Fully Autonomous']


def fh(fld):
    t = np.array([[(fld[d.mode_clean == mm]).sum(), (~fld[d.mode_clean == mm]).sum()] for mm in modes])
    rows = t.sum(1); K = t[:, 0].sum()
    lg = lambda x: gammaln(np.array(x) + 1).sum()
    lp = lambda x: -lg(x) - lg(rows - np.array(x))
    l0 = lp(t[:, 0]); ps = []
    for x in itertools.product(*[range(rr + 1) for rr in rows]):
        if sum(x) == K: ps.append(lp(x))
    ps = np.array(ps); w = np.exp(ps - ps.max()); w /= w.sum()
    return t.tolist(), w[ps <= l0 + 1e-9].sum()


print('FH exact strict', fh(fs)); print('FH exact lenient', fh(fl))
print(pd.crosstab(d.scenario_clean, d.mode_clean))
print('sim-only HM', d[(~ph) & HM].mode_clean.tolist())
print('FA sim only', (~ph & FA).sum(), 'FA phys', (ph & FA).sum())
print('sensor none FA/HM', ((d.s_none == '1') & FA).sum(), ((d.s_none == '1') & HM).sum())
print('VD3 FA/HM', vd3[FA].sum(), vd3[HM].sum())
print('arch pct'); print((d.architecture_clean.value_counts() / 39 * 100).round(1))
# 2 Underground studies modes
print(d[d.scenario_clean.str.startswith('Underground')][['mode_clean']].value_counts())
print(d[hyb & fs][['mode_clean']].value_counts(), d[uav & fs][['mode_clean']].value_counts())
print('UAV by mode', d[uav].mode_clean.value_counts().to_dict())
