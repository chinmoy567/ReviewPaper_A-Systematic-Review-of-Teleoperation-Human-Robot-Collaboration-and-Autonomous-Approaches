"""Cross-reference checks for the manuscript sections of the master document (CLAUDE.md rule 7)."""
import re, os
s = open('SAR_review_master_document.md', encoding='utf-8').read()
regs = {'T': ('### TITLE AND AUTHORS', '## 15.'), 'I': ('### I. INTRODUCTION', '### Sourcing notes'), 'II': ('### II. METHODOLOGY', '## 10.'),
        'III': ('### III. RESULTS', '## 11.'), 'IV': ('### IV. TAXONOMY', '## 12.'), 'V': ('### V. DISCUSSION', '## 13.')}
seg = {k: s[s.index(a):s.index(b, s.index(a))] for k, (a, b) in regs.items()}
head, concl = seg['T'].split('### VI. CONCLUSION')
full = head + seg['I'] + seg['II'] + seg['III'] + seg['IV'] + seg['V'] + '### VI. CONCLUSION' + concl
R = {r: i + 1 for i, r in enumerate('I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI XVII XVIII XIX XX XXI XXII'.split())}
defs = [(R[m.group(1)], m.start()) for m in re.finditer(r'\*\*TABLE ([IVX]+)\.\*\*', full)]
print('tables', [d[0] for d in defs], 'sequential:', [d[0] for d in defs] == list(range(1, len(defs) + 1)))
for n, pos in defs:
    cites = [m.start() for m in re.finditer(r'Tables? ([IVX]+)\b', full) if R.get(m.group(1)) == n]
    if not cites or min(cites) > pos: print('  table', n, 'not cited before it appears')
refs = {R[x] for x in re.findall(r'Tables? ([IVX]+)\b', full) if x in R}
print('  refs to undefined tables:', sorted(refs - {d[0] for d in defs}))
figs = [(int(m.group(1)), m.start()) for m in re.finditer(r'!\[Fig\. (\d+)\.', full)]
print('figs', [f[0] for f in figs])
for n, pos in figs:
    c = [m.start() for m in re.finditer(r'Figs?\. %d\b' % n, full)]
    if not any(x < pos for x in c): print('  fig', n, 'not cited before embed')
for p_ in re.findall(r'\]\((assets/figures/[^)]+)\)', full):
    if not os.path.exists(p_): print('  MISSING image', p_)
heads, cur = {}, None
for line in full.split('\n'):
    m = re.match(r'### (I|II|III|IV|V|VI)\. ', line)
    if m: cur = m.group(1); heads.setdefault(cur, set())
    m2 = re.match(r'#### ([A-K])\. ', line)
    if m2 and cur: heads[cur].add(m2.group(1))
bad = sorted({f'{a}-{b}' for a, b in re.findall(r'Sections? (I|II|III|IV|V|VI)-([A-K])', full) if b not in heads.get(a, set())})
print('bad section refs:', bad)
print('abstract words:', len(seg['T'].split('### ABSTRACT')[1].split('**Keywords')[0].split()))
print('AUTHOR INPUT markers:', full.count('[[AUTHOR INPUT NEEDED'), '| UNVERIFIED:', full.count('UNVERIFIED'))
