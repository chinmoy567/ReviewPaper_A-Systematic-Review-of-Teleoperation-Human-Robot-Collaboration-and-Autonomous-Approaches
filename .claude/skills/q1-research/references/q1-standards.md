# Q1 standards for a systematic review in robotics / disaster robotics

Use this as the pass/fail bar. Each item: why reviewers care → what "good" looks like.

## A. Contribution
- [ ] **Clear gap vs. every recent review (≤3 years)**, shown in a comparison table with explicit columns (scope, years, corpus size, method, organizing axis, autonomy coding?, validation analysis?).
- [ ] Novelty claims are hedged and dated ("to our knowledge, as of <search date>") and backed by a documented novelty search.
- [ ] Contribution is more than descriptive counting: a framework/taxonomy, an evidenced explanation, and a research agenda that others can act on.
- [ ] Prior reviews are described accurately (a single mischaracterization can sink the paper).

## B. Method (PRISMA 2020 + PRISMA-S)
- [ ] Indexing databases (Scopus and/or Web of Science, plus IEEE Xplore, ACM DL) rather than only publisher portals; publisher sites as supplementary.
- [ ] Full Boolean search string per database, with synonyms (search and rescue OR USAR OR disaster response OR emergency…) AND (robot* OR UAV OR drone OR UGV…), fields searched, limits, and **date of last search per source**.
- [ ] Search is recent: last search ≤ 6–12 months before submission; if older, run an update search.
- [ ] Protocol registered (OSF/PROSPERO); if retrospective, say so honestly.
- [ ] Independent dual/triple screening **with an agreement statistic** (Cohen's/Fleiss' κ) at screening and for the key coded variable.
- [ ] Quality / risk-of-bias appraisal with a named or justified instrument, and its results used (e.g. sensitivity analysis excluding low-quality studies).
- [ ] PRISMA flow diagram consistent with text; exclusion reasons counted.
- [ ] Supplementary: PRISMA checklist, search strings, extraction sheet, exclusion log, coding manual. Data availability statement.

## C. Analysis and claims
- [ ] Every percentage reported with n/N; small cells flagged.
- [ ] Key comparisons have uncertainty (95% CI) and an appropriate test (Fisher's exact for small 2×2) — or are explicitly called descriptive.
- [ ] No causal language from cross-sectional counts ("associated with", not "causes").
- [ ] Threats to validity section: construct (taxonomy coding), internal (rater bias), external (window, databases, language), conclusion validity (small n).

## D. Theory
- [ ] Taxonomy anchored to established frameworks (Sheridan–Verplank LOA, Parasuraman et al. 2000, Beer et al. 2014 LORA, ALFUS) with a mapping table and operational decision rules.
- [ ] Classification reliability demonstrated.

## E. Writing & presentation
- [ ] Abstract within venue limit, structured logic (context → gap → method → results with numbers → implication).
- [ ] No internal/working-document language. No "model reference paper".
- [ ] Figures readable in greyscale, consistent fonts, cited in order; tables not redundant with figures.
- [ ] References: all exist, correctly formatted, majority peer-reviewed, recent (≥40–50% from last 3 years for a "recent advances" review), no news/blog sources for key facts where peer-reviewed exist.
- [ ] Practical implications for responders/standards bodies (e.g., NIST standard test methods for response robots, ASTM E54.09) — not only for researchers.

## Known open risks for THIS manuscript (from the 2026-11-08 scan — re-verify)
1. Search used only "rescue robot" / "disaster rescue robot" on publisher portals → reproducibility and coverage critique is near-certain.
2. Bakzadeh et al. 2026 [6] DOES classify platforms by autonomy band (A1/A2/A3 on Sheridan–Verplank; 12/1/1 of 14) — it excludes autonomy *software*, not autonomy *level*. Manuscript text and Table I currently overstate the exclusion.
3. Uncited 2026 competitors: Shuvo et al. 2026 (Frontiers Robot. AI, doi:10.3389/frobt.2026.1832982, H2M/M2M/M2H learning taxonomy, 2005–2025); a 2026 systematic & bibliometric review of SAR path planning (Applied Soft Computing, 73 articles, Scopus+WoS); air–ground collaborative fire & rescue survey (arXiv 2412.20699).
4. No quality appraisal, no κ, no protocol registration (the first is admitted in Limitations).
5. Headline contrasts rest on n=27 vs n=5/4/3 — need CIs/Fisher tests.
6. Abstract says the pattern "has not been reported previously" — must be hedged.
7. Ref [3] is a news quote; ref [2] is an arXiv preprint for a core framing claim.
8. Discussion contains "model reference paper" phrasing.
9. Last search July 2026; by submission, an update search may be expected.
