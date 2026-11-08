"""Recompute Results tables from data/extraction_table.csv only.

Usage:  python data/recompute_tables.py   -> writes data/recomputed_tables.md
Only rows with coding_status == 'CODED' are rebuilt data. The manuscript_* columns
are the manuscript's own labels (Sec. IV lists, Sec. 6B), shown separately for comparison.
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(HERE, 'extraction_table.csv'), encoding='utf-8')))
coded = [r for r in rows if r['coding_status'] == 'CODED']
N_all, N = len(rows), len(coded)
SENS = ['visual', 'thermal', 'depth', 'lidar', 'gps', 'imu', 'acoustic', 'gas', 'rf', 'physio', 'none']
MODES = ['Teleoperation', 'Supervisory Control', 'Shared-Collaborative Control', 'Fully Autonomous']
VALS = ['Simulation only', 'Real-world field test', 'Partial', 'Prototype bench test']
PLATS = ['UAV', 'UGV', 'Legged', 'UUV / USV', 'Hybrid / Multi-Platform', 'Abstract / Unspecified']
CLU = ['multi-robot coordination', 'single-robot navigation', 'perception-driven', 'platform-architecture']
out = []

def pct(a, b):
    return f"{a} ({100*a/b:.1f}%)" if b else f"{a} (n/a)"

def dist(title, key, order, data):
    c = Counter(r[key] for r in data)
    out.append(f"\n### {title} (n = {len(data)})\n\n| Category | n (%) |\n|---|---|")
    for k in order + sorted(set(c) - set(order)):
        if c.get(k) or k in order:
            out.append(f"| {k} | {pct(c.get(k, 0), len(data))} |")

def xtab(title, rk, ro, ck, co, data):
    out.append(f"\n### {title} (n = {len(data)})\n")
    out.append('| ' + rk + ' \\ ' + ck + ' | ' + ' | '.join(co) + ' | Total |')
    out.append('|' + '---|' * (len(co) + 2))
    for a in ro:
        sub = [r for r in data if r[rk] == a]
        if not sub:
            continue
        out.append(f"| {a} | " + ' | '.join(str(sum(1 for r in sub if r[ck] == b)) for b in co) + f" | {len(sub)} |")

out.append(f"# Recomputed tables\n\nSource: `data/extraction_table.csv`. Rows coded from PDFs: **{N} of {N_all}**. "
           "All rebuilt tables below cover only the coded rows unless marked 'manuscript labels'.")

out.append("\n## A. Manuscript labels for all 39 (not rebuilt; for reference)")
dist('Mode, manuscript labels (Table V)', 'manuscript_mode', MODES, rows)
dist('Platform, manuscript labels (Table VI)', 'manuscript_platform', PLATS, rows)
xtab('Mode x Platform, manuscript labels (Table VII)', 'manuscript_mode', MODES, 'manuscript_platform', PLATS, rows)

out.append("\n## B. Rebuilt from PDFs (coded rows only)")
dist('Table V Mode', 'mode_clean', MODES, coded)
dist('Table VI Platform', 'platform_clean', PLATS, coded)
xtab('Table VII Mode x Platform', 'mode_clean', MODES, 'platform_clean', PLATS, coded)
out.append(f"\n### Table VIII Sensor prevalence (multi-select, n = {N})\n\n| Modality | n (%) |\n|---|---|")
for s in SENS:
    out.append(f"| {s} | {pct(sum(int(r['s_'+s] or 0) for r in coded), N)} |")
dist('Table IX Architecture', 'architecture_clean', ['PC/Offline', 'Onboard/Edge', 'Hybrid', 'Cloud'], coded)
dist('Table X Validation', 'validation_clean', VALS, coded)
xtab('Table XI Mode x Validation', 'mode_clean', MODES, 'validation_clean', VALS, coded)
xtab('Platform x Validation', 'platform_clean', PLATS, 'validation_clean', VALS, coded)
dist('Table XII Scenario', 'scenario_clean', ['Generic/Unspecified', 'Underground/Mine/Tunnel/Cave', 'Earthquake/Structural Collapse',
     'Wilderness/Mountain/Forest', 'Maritime/Water', 'Wildfire/Fire', 'Other (single-occurrence hazard)'], coded)
fa = [r for r in coded if r['mode_clean'] == 'Fully Autonomous']
xtab('FA cluster x Validation', 'fa_cluster', CLU, 'validation_clean', VALS, fa)

out.append("\n### Environmental-realism limitation (author-stated)\n")
y = [r for r in coded if r['env_realism_limitation'] == 'Y']
n_ = [r for r in coded if r['env_realism_limitation'] == 'N']
out.append(f"- Coded rows: Y = {pct(len(y), N)}, N = {len(n_)}")
bord = [r['ref_N'] for r in coded if r['env_realism_confidence'].startswith('borderline')]
out.append(f"- Borderline codes (refs): {', '.join(bord) or 'none'}")
out.append(f"- N codes (refs): {', '.join(r['ref_N'] for r in n_)}")
out.append(f"- Upper bound on corpus Y if every uncoded row were Y: {len(y) + (N_all - N)}/{N_all}")
gen = [r for r in coded if r['scenario_clean'] == 'Generic/Unspecified']
spec = [r for r in coded if r['scenario_clean'] != 'Generic/Unspecified']
out.append(f"- Generic: {pct(sum(r['env_realism_limitation']=='Y' for r in gen), len(gen))}; "
           f"hazard-specific: {pct(sum(r['env_realism_limitation']=='Y' for r in spec), len(spec))}")

xtab('Human role modelled x Mode', 'mode_clean', MODES, 'human_role_modelled', ['Y', 'N'], coded)
out.append(f"\n### VDR score by mode (n = {N})\n\n| Mode | n | VDR values | mean VDR | stat = Y |\n|---|---|---|---|---|")
for m in MODES:
    sub = [r for r in coded if r['mode_clean'] == m]
    if sub:
        v = [int(r['vdr']) for r in sub]
        out.append(f"| {m} | {len(sub)} | {sorted(v)} | {sum(v)/len(v):.2f} | {sum(r['stat']=='Y' for r in sub)} |")

out.append("\n### Agreement with manuscript labels (coded rows)\n")
for k in ['mode_agrees', 'platform_agrees', 'fa_cluster_agrees']:
    c = Counter(r[k] for r in coded if r[k])
    out.append(f"- {k}: {dict(c)}")

open(os.path.join(HERE, 'recomputed_tables.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out))
