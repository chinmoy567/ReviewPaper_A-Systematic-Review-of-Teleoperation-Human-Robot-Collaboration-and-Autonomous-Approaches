"""Round-2 checks: Table XX vs function_autonomy.csv, Table XIX, Table V first criterion, sensitivity (a)-(e), Holm."""
import pandas as pd, numpy as np, csv, collections, os
from scipy.stats import fisher_exact
os.chdir(r"C:\Users\chinmoy\Downloads\review paper")
d=pd.read_csv('data/extraction_table.csv',dtype=str); f=pd.read_csv('data/function_autonomy.csv',dtype=str)
m=d.merge(f,on='ref_N',suffixes=('','_f'))
assert len(m)==39
short={'Teleoperation':'T','Supervisory Control':'S','Shared-Collaborative Control':'C','Fully Autonomous':'F'}
m['mc']=m.mode_clean.map(short)
print('--- Table XX (M/S/H counts)')
for mo in ['T','S','C','F',None]:
    s=m if mo is None else m[m.mc==mo]
    print(mo,len(s),[ '/'.join(str((s[c]==k).sum()) for k in 'MSH') for c in ['acq','ana','dec','act']])
print('designed_authority vs mode crosstab'); print(pd.crosstab(m.mc,m.designed_authority))
print('mismatched refs',m[m.mc!=m.designed_authority][['ref_N','mc','designed_authority']].values.tolist())
allM=m[(m.acq=='M')&(m.ana=='M')&(m.dec=='M')&(m.act=='M')]
print('FA all four M',(allM.mc=='F').sum(),'of',(m.mc=='F').sum(), 'any mode all four M',len(allM))
print('evaluated_human_presence vs human_role_modelled'); print(pd.crosstab(m.evaluated_human_presence,m.human_role_modelled))
print(m[m.evaluated_human_presence!=m.human_role_modelled][['ref_N','mc','human_role_modelled','evaluated_human_presence']].values.tolist())
print(pd.crosstab(m.mc,m.evaluated_human_presence))
print('--- Table XIX (lenient field)')
fl=m.validation_lenient=='Real-world field test'
print(m[fl][['ref_N','mc','platform_clean','validation_strict','citation']].assign(citation=lambda x:x.citation.str[:40]).to_string())
print('--- Table V first criterion')
log=pd.read_csv('supplementary/screening_log.csv',dtype=str)
ex=log[log.decision=='EXCLUDED']
print(ex.criteria_violated.map(lambda s:s.split('/')[0]).value_counts().to_dict(), len(ex))
print(collections.Counter(k for s in ex.criteria_violated for k in s.split('/')))
print(ex.criteria_violated.value_counts().to_dict())
print(log.groupby(['identification_route','decision']).size())
print('--- sensitivity (e)')
print(d.identification_route.value_counts().to_dict())
FA=d.mode_clean=='Fully Autonomous'; fs=d.validation_strict=='Real-world field test'; fls=d.validation_lenient=='Real-world field test'; ph=d.validation_strict!='Simulation only'
pub=d.identification_route=='publisher'
for lab,o in [('strict',fs),('lenient',fls),('phys',ph)]:
    a=o[FA&pub].sum();na=(FA&pub).sum();b=o[~FA&pub].sum();nb=(~FA&pub).sum()
    print('(e)',lab,f'{a}/{na} vs {b}/{nb} p={fisher_exact([[a,na-a],[b,nb-b]])[1]:.4f}')
# (d): add 2 FA sim-only
for lab,o in [('strict',fs),('lenient',fls),('phys',ph)]:
    a=o[FA].sum();b=o[~FA].sum()
    print('(d)',lab,f'{a}/29 vs {b}/12 p={fisher_exact([[a,29-a],[b,12-b]])[1]:.5f}')
print('--- Holm over Table XIII rows')
p=np.array([0.0601,0.0141,0.0824,0.0427,0.0245])
from itertools import count
def holm(p):
    o=np.argsort(p);n=len(p);adj=np.empty(n);run=0
    for i,j in enumerate(o):
        run=max(run,(n-i)*p[j]);adj[j]=min(1,run)
    return adj
print(holm(p).round(3))
