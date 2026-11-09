# Stats-consistency check: rewritten manuscript (Secs. 9-14), 2026-11-09

Scope: every number in the ABSTRACT, I-VI, Tables I-XVIII, Figs. 1-7 captions, checked by independent recomputation from `data/extraction_table.csv` (39 rows), `data/reliability_blind_codes.csv`, `assets/docs/paperlinks.xlsx` (130 rows) and `supplementary/screening_log.csv` (125 rows). Nothing in the manuscript or data was edited.

Scripts (reproducible; run from the project root with `python`):
- `research_outputs/2026-11-09_stats-checker_scripts/check_stats.py` (all CSV-derived numbers, Wilson CIs, Fisher/OR, Mann-Whitney, exact Freeman-Halton by full enumeration, sensitivity, kappa/AC1)
- `research_outputs/2026-11-09_stats-checker_scripts/check_prisma.py` (paperlinks.xlsx and screening_log.csv: PRISMA flow, Table II, duplicates, exclusions)

## 1. Verdict

No arithmetic mismatches in any table, percentage, Wilson CI, Fisher p, OR, OR CI, Mann-Whitney p, sensitivity cell, PRISMA count, or Table II cell. Four substantive issues remain, all about method description or inferential wording, not arithmetic:

| # | Severity | Issue |
|---|---|---|
| M1 | Medium | Sec. II-I lists three sensitivity analyses (a)(b)(c) and defines (a) as "excluding papers that model no human role". Table XVII / Sec. III-G report four analyses, and its (a) is "physical platform only"; the human-role subset (old a') is "not estimable" and is not reported; (d) (two misexcluded records) is not in Methods. |
| M2 | Medium | Sec. II-I calls the 4-mode test a "Freeman-Halton test". The reported p = 0.027 (strict) comes from `analysis.py`'s Monte Carlo permutation using Pearson chi-square ordering. The true Freeman-Halton exact p (probability ordering, full enumeration) is 0.0291 strict and 0.0058 lenient. Lenient agrees (0.006); strict differs (0.027 vs 0.029). |
| M3 | Medium | Sensitivity (a) cannot support the "research genre" reading as written. All 10 FA studies removed by the filter are simulation-only (verified: FA physical 11 before and after). The filter therefore removes only FA studies with the "no physical test" outcome, so attenuation is guaranteed by construction. The OR moves 0.17 -> 0.28 (CI 0.02-2.45), with wide overlap. "Contrast largely disappears" and Intro contribution 2 ("Sensitivity analyses show that this gap reflects...") overstate. |
| M4 | Medium | "Statistically clear" (Conclusion) / "clear for any physical testing and validation depth" (Sec. III-D, V-A) conflicts with Sec. II-I / V-D ("no multiplicity correction"). Holm over the five contrasts of Sec. III-D (strict, lenient, any physical, VD=3, MW VD): adjusted p = 0.085, 0.070, 0.072, 0.085, 0.073. None is < 0.05. |

## 2. Mismatch list (location -> found -> expected)

Arithmetic mismatches: **none** (see per-section statements in Sec. 3).

Non-arithmetic discrepancies:

| Location | Found | Expected / recommendation |
|---|---|---|
| Sec. II-I, sensitivity list (a)-(c) | (a) = exclude papers with no human role; only three analyses | Match Table XVII: (a) physical platform only; (b) RP >= 2; (c) boundary cases re-coded with blind codes; (d) add the two possibly misexcluded records. Report human-role subset as "not estimable (1 of 27 FA models a human)". |
| Sec. II-I "Freeman-Halton test" vs Sec. III-D "exact test ... p = 0.027" | 0.027 (MC, chi-square order) | Either report Freeman-Halton exact p = 0.029 (strict) and 0.006 (lenient), or call it "permutation test (200,000 permutations), p = 0.027 / 0.006". |
| Sec. II-B item 2, AUTHOR INPUT placeholder | Lists seven Google Scholar queries as candidates | paperlinks.xlsx "How it was found" records only two Google Scholar queries: "rescue robot" (8 records) and "disaster rescue robot" (7 records). Only those two are evidenced. |
| Sec. III-G (d) strict | p = 0.050 | Exact p = 0.05001, i.e. just above 0.05. Report as 0.050 and do not describe it as "significant" or "below 0.05" anywhere. |
| Table XVII (d) label | "Two possibly misexcluded records added as FA, simulation only" | Fine, but state it is a projection (assumed outcome), not data. |
| Sec. V-C | "somewhat more frequent among hazard-specific studies (80.0% vs 58.3%, p = 0.30)" | p = 0.295; OR 0.36 (0.05-1.85). Write "no detectable difference (p = 0.30)" and drop "somewhat more frequent". |
| Sec. V-A "Reproducibility scores do not differ ... The difference therefore lies in where studies are tested" | RP 2.11 vs 2.08, p = 0.83 | n = 27 vs 12, 3-level ordinal, mostly 2s (33 of 39). "No detectable difference" is the supportable reading; this is not evidence of equivalence. |
| Order of modes | Fig. 7 / Sec. II-G order: Tele, Shared, Supervisory, FA; Tables VI, VIII, XII: Tele, Supervisory, Shared, FA | Cosmetic. Add a note or reorder one for consistency. |
| Fig. 4 labels | Integer percentages (44, 36, ...) vs one decimal in Table IX | Consistent rounding; cosmetic only. |

Not traceable to the CSV or logs (cannot be checked from the data package; flag for the authors, not as errors): Sec. II-E post hoc AI check on 23 excluded records (17 agreed / 4 borderline / 2 flagged; 17 + 4 + 2 = 23, arithmetic OK, but no file in the package records it); "4 of 10" Cho et al. trials (the PDF states 40%, 86% mAP and "modest"; "4 of 10" is not literal text; 40% is verified); external figures in the Introduction and Table I (CRED, Kareem 74, Sinha >190 and 4.2%, Shuvo 130, Bakzadeh 15/14/12, Hu 2,201) belong to citation-verifier. Verified against the source PDFs by text search: Mead et al. 95.83%, 69.36%, 77.92%, 99.67% and collisions (ref 25); Gaitan 0.026 and 0.264 (ref 20); F. You 35 participants / 27 (ref 21); Raghavan 93.1% (ref 13); Cho 86% (ref 47). The 1,200 kg payload is in the CSV (ref 12).

## 3. Per-section statements

**PRISMA flow and Table II (paperlinks.xlsx + screening_log.csv): no mismatches.**
- 130 records: 78 publisher-platform + 15 Google Scholar + 37 AI (ChatGPT 34, Gemini 3) = 130; other methods 52. OK.
- DOI-based duplicates: five pairs (110/130, 105/108, 4/12, 99/102, 61/86). The five records absent from the screening log are 12, 86, 102, 108, 130 (the later-cataloged copy of each pair). Routes of removed: 86 = publisher; 12 = Google Scholar; 102, 108, 130 = AI. So 1 publisher + 4 other. 78 - 1 = 77; 52 - 4 = 48; 77 + 48 = 125. OK.
- MD5 of the PDFs (assets/papers): four pairs byte-identical (110/130, 105/108, 99/102, 61/86); pair 4/12 differs. Matches Sec. II-C wording.
- Screening log: 125 rows = 39 INCLUDED + 86 EXCLUDED. Included by route: 18 publisher + 21 other (10 Google Scholar + 11 AI). Excluded by route: 59 + 27 = 86. OK.
- Exclusions by criterion (screening log): C1 only 56, C2 only 17, C3 only 1, C1/C2 6, C2/C3 5, C1/C3 1. Totals C1 = 63, C2 = 28, C3 = 7 (Table V OK). 12 dual-criterion records, sum 98 (86 + 12). OK. Per-route in Fig. 2: publisher C1 42 / C2 21 / C3 3 with 7 dual (4 C1+C2, 3 C2+C3); other C1 21 / C2 7 / C3 4 with 5 dual (2, 2, 1). All match the figure text.
- Table II (DOI prefix, route): all 30 cells and all row/column totals match (MDPI 34/5/2; Elsevier 18/3/10; IEEE 5/2/8; Springer 0/3/11; Sci. Rep. 8/1/3; PLOS 6/0/0; Frontiers 4/0/2; TSP 2*/0/1; Wiley 1/0/0; ASCEE 0/1/0). The Elsevier search returned 20 DOI-prefix 10.1016 + 10.32604 records (18 + 2 TSP), matching the footnote and Fig. 2 "Elsevier ScienceDirect (n = 20)*". Fig. 1 counts and percentages (31.5, 23.8, 11.5, 10.8, 9.2, 4.6, 4.6, 2.3, 0.8, 0.8) correct.
- Sec. II-F: 18 fields, 5 clean-category fields, 10 sensor flags + none: matches the CSV columns.

**Abstract: no mismatches.** 130/78/15/37/125/39; 69.2% (27/39); 5/4/3; 40.7% vs 83.3% p = 0.018; 7.4% (2.1-23.4) vs 33.3% p = 0.060; 11.1% vs 50.0% p = 0.014; two thirds (66.7%); 5 of 39. Every one traces to Tables VI, XII, XIII and XVI.

**Sec. III-A, Table VI: no mismatches.** 27/5/4/3 and 69.2 (53.6-81.4), 12.8 (5.6-26.7), 10.3 (4.1-23.6), 7.7 (2.7-20.3). "26 of 27 no human; 10 of 12 human acts": CSV human_role 26 N / 1 Y for FA; 3 + 4 + 3 = 10 of 12. OK.

**Sec. III-B, Tables VII, VIII: no mismatches.** Platform 13/13/7/3/2/1 and 33.3/33.3/17.9/7.7/5.1/2.6. Table VIII matches the CSV cell for cell (Tele 0/2/0/0/3/0; Sup 1/2/0/0/1/0; SC 3/0/0/0/0/0; FA 9/9/2/1/3/3). Text bullets correct.

**Sec. III-C, Tables IX, X, Fig. 4: no mismatches.** All 11 sensor counts and percentages; architecture 21/8/7/1/2 (53.8/20.5/17.9/2.6/5.1); Fig. 4 bar labels match (17, 14, 13, 10, 7, 5, 5, 3, 3, 2, 2). "One in four" = 25.6%.

**Sec. III-D, Tables XI, XII, XIV, XVIII, Figs. 5, 6: no mismatches.** Strict 18/12/6/3, lenient 18/10/9/2; Table XII all cells, row totals, all Wilson CIs (60.0 23.1-88.2; 25.0 4.6-69.9; 0.0 0.0-56.1; 7.4 2.1-23.4; all 15.4 7.2-29.7; HM 33.3 13.8-60.9), lenient %, any-physical % (100, 100, 33.3, 40.7, 53.8), human role, mean VD 2.60/2.75/1.33/1.70/1.90 (exact 1.704, overall 1.897). Table XIV and XVIII cell for cell. Fig. 5 bars (18/18, 12/10, 3/2, 6/9) and Fig. 6 bars, labels (3/5, 3/5, 1/4, 3/4, 0/3, 0/3, 2/27, 3/27) and CI whiskers all match. Fig. 6 does not display the pooled human-in-mission group, which is fine because Table XIII has it.

**Sec. III-D inference, Table XIII: no mismatches.** Independent recomputation (two-sided Fisher; conditional MLE OR with exact CI):

| Contrast | Groups | OR (95% CI) | p |
|---|---|---|---|
| Field strict, FA vs HM | 2/27 vs 4/12 | 0.169 (0.013-1.431) | 0.0601 |
| Field lenient | 3/27 vs 6/12 | 0.134 (0.0165-0.837) | 0.0141 |
| Any physical | 11/27 vs 10/12 | 0.145 (0.0130-0.873) | 0.0180 |
| VD = 3 | 4/27 vs 6/12 | 0.184 (0.0276-1.054) | 0.0427 |
| Field strict, FA vs Tele + Sup | 2/27 vs 4/9 | 0.109 (0.0078-0.992) | 0.0245 |
| UAV vs Hybrid strict | 3/13 vs 3/7 | 0.420 (0.037-4.54) | 0.613 |

Mann-Whitney VD: U = 92.0, p = 0.0242 (means 1.70 vs 2.33). RP: p = 0.827 (2.11 vs 2.08). Exact Freeman-Halton (enumeration): strict 0.0291 (table [[3,2],[1,3],[0,3],[2,25]]), lenient 0.0058; the manuscript's 0.027/0.006 come from the MC (see M2). "Not ordered along the autonomy scale" (60 / 25 / 0 / 7.4) correct. "UAV and Hybrid do not differ (p = 0.61)" correct (lenient 3/13 vs 4/7, p = 0.17, not cited). Platform text: UAV 3/13 (23.1%), Hybrid 3/7 (42.9%; 4/7 lenient), UGV 0/13 (2/13 lenient); all three Hybrid field tests are Teleoperation (verified).

**Sec. III-E, Table XV: no mismatches.** 24/5/4/3/1/1/1 and percentages; Underground 3 FA + 2 Supervisory, 0 Teleoperation (verified).

**Sec. III-F, Table XVI: no mismatches.** 26/39 (66.7; Wilson 51.0-79.4); broad 33/39 (84.6; 70.3-92.8); generic 14/24 = 58.3%, hazard-specific 12/15 = 80.0%, p = 0.295 (OR 0.36, 0.05-1.85); broad 19/24 = 79.2%, 14/15 = 93.3%; 35/39 = 89.7%; 5/39 = 12.8 (5.6-26.7). VDR means 4.60/5.00/3.33/3.81 (3.815 rounds to 3.81); VDR = VD + RP holds for every row.

**Sec. III-G, Table XVII: no mismatches.** Recomputed: (a) 17/12: 2/17 v 4/12 p = 0.198; 3/17 v 6/12 p = 0.106; 11/17 v 10/12 p = 0.408. (b) 26/12: 0.066, 0.016, 0.015. (c) 27/12: 3/27 v 3/12 0.348; 4/27 v 5/12 0.102; 11/27 v 10/12 0.018. (d) 29/12: 0.0500, 0.0106 (0.011), 0.0148 (0.015). Primary row 0.060/0.014/0.018. "Removes 10 FA and no HM" verified (10 sim-only FA, 0 HM). Blind-code reclassification reproduces: 4 disagreements (refs 18 S->F, 20 C->T, 21 C->S, 48 F->S).

**Sec. II-G reliability: no mismatches.** 35/39 = 89.7%; kappa 0.789; analytic 95% CI 0.606-0.972 (reported 0.61-0.97); AC1 0.878 (0.88); binary 37/39, kappa 0.880 (0.88). Sec. V-D "disagreed on two of the three Shared-Collaborative" (refs 20 and 21): correct. Sec. IV-C: Gaitan = ref 20 read as Teleoperation; F. You = ref 21 read as Supervisory: correct.

**Sec. IV and V other numbers: no mismatches.** Cluster sizes 12/7/5/3 (sum 27); "ten of twelve simulation-only, none field"; "four of seven sim-only, two partial, one field"; Cho 40%/4 of 10/86%; Mead 95.83 -> 69.36, 77.92 vs 99.67, 3 of 10 collisions; 15.4%/23.1%/69.2%/66.7%/84.6%/5 of 39/2 of 27/26 of 27; "about half as often" = 40.7/83.3 = 0.49; Sec. V-D "52 ... 21 of the 39" correct (52 other-route records; 21 included).

**Conclusion: no mismatches** (69.2%, two thirds, 5 of 39, 39 studies); wording issues only (M4).

**Fig. 7 (fig_taxonomy.png): no mismatches.** n = 5 (12.8%), 3 (7.7%), 4 (10.3%), 27 (69.2%); LOA bands 1-2, 3-5, 5-7, 8-10 match Table IV.

**Four regenerated figures vs CSV: all match.** `fig_sensor_prevalence.png`, `fig_validation_type.png`, `fig_autonomy_validation.png`, `fig_taxonomy.png` (details in the sections above). I also viewed `prisma_diagram_v2.png` and `fig_records_by_source.png`: all numbers match.

## 4. Wilson CIs and inferential table for the headline claims (for the manuscript)

| Quantity | Estimate (95% Wilson CI) |
|---|---|
| FA field-tested, strict | 2/27 = 7.4% (2.1-23.4) |
| Human-in-mission field-tested, strict | 4/12 = 33.3% (13.8-60.9) |
| FA field-tested, lenient | 3/27 = 11.1% (3.9-28.1) |
| Human-in-mission, lenient | 6/12 = 50.0% (25.4-74.6) |
| FA any physical test | 11/27 = 40.7% (24.5-59.3) |
| Human-in-mission any physical | 10/12 = 83.3% (55.2-95.3) |
| FA VD = 3 | 4/27 = 14.8% (5.9-32.5) |
| UAV field-tested, strict | 3/13 = 23.1% (8.2-50.3) |
| Hybrid field-tested, strict | 3/7 = 42.9% (15.8-75.0) |
| Hybrid, lenient | 4/7 = 57.1% (25.0-84.2) |
| UGV field-tested, strict | 0/13 = 0% (0-22.8) |
| Multi-robot coordination cluster, field | 0/12 = 0% (0-24.2) |
| Realism limitation, author-stated | 26/39 = 66.7% (51.0-79.4) |
| Public code/data | 5/39 = 12.8% (5.6-26.7) |
| Repeated trials / baseline | 35/39 = 89.7% (Wilson 76.4-95.9, not currently reported) |

Not significant: FA vs human-in-mission field testing under strict coding (p = 0.060, OR CI includes 1); UAV vs Hybrid (p = 0.61 strict, 0.17 lenient); generic vs hazard-specific realism acknowledgment (p = 0.30); RP difference (p = 0.83); all sensitivity (a), (c) strict, (c) lenient field outcomes. Nominally significant but not multiplicity-robust: lenient field (0.014), any physical (0.018), MW VD (0.024), VD = 3 (0.043), FA vs Tele + Sup strict (0.025).

## 5. Recommended replacement wording

1. **Sec. II-I.** Replace the final two sentences with: "Four sensitivity analyses were run on the primary contrast: (a) restricting to studies with a physical platform and at least one physical sensor, which excludes abstract agents and sensor-free simulations; (b) restricting to RP >= 2; (c) re-coding the boundary cases with the independent blind codes; and (d) adding the two possibly misexcluded records as simulation-only Fully Autonomous studies. A fifth, restricting to studies that model a human role, is not estimable because only one Fully Autonomous study does." And replace "a Freeman-Halton test" with "a Freeman-Halton exact test (p = 0.029 strict, 0.006 lenient)" or, if the MC value is kept, "a permutation test (200,000 permutations)".
2. **Sec. III-D, Four modes together.** "An exact Freeman-Halton test of mode against field testing gave p = 0.029 (strict) and p = 0.006 (lenient)." (Sec. III-D list item, Sec. II-I.)
3. **Sec. III-D opening of the inference paragraph.** "Fully Autonomous studies had lower point-estimate odds on every validation indicator. These tests are exploratory and uncorrected for multiplicity; after Holm adjustment over the five tests in this paragraph none remains below 0.05 (adjusted p 0.07-0.09). The consistency of direction, not any single p-value, is the finding."
4. **Sec. III-D bullet "Clearest".** "Largest and most consistent: any physical testing (OR 0.14, 95% CI 0.013-0.87, uncorrected p = 0.018) and validation depth (Mann-Whitney uncorrected p = 0.024)."
5. **Sec. III-G first sentence and bullet 1.** "The direction never reverses, but the evidence is weak once abstract and sensor-free studies are removed. Those 10 Fully Autonomous studies are all simulation-only by construction, so this attenuation is partly mechanical: the OR rises from 0.17 to 0.28 (95% CI 0.02-2.45) for strict field testing, and the intervals overlap almost completely."
6. **Sec. V-A, "Two observations support this reading".** Replace with "Two observations are consistent with this reading: the contrast is weaker when only studies with a physical platform are compared (although that filter removes only simulation-only Fully Autonomous studies, so it cannot discriminate between explanations), and reproducibility scores show no detectable difference between the groups (mean 2.11 vs 2.08, p = 0.83)." Also change "largely disappears" to "attenuates".
7. **Sec. I contribution 2.** Replace "Sensitivity analyses show that this gap reflects ... more than autonomy as such" with "Sensitivity analyses are consistent with the gap reflecting the algorithm-first, simulation-based character of most Fully Autonomous research rather than autonomy as such, although the corpus cannot separate the two."
8. **Conclusion.** Replace "It was statistically clear for physical testing and validation depth, and borderline for strict field testing." with "It was nominally significant, without multiplicity correction, for physical testing and validation depth, and borderline for strict field testing (p = 0.060)."
9. **Sec. V-A.** Replace "it was clear for any physical testing and for validation depth" with "it was nominally significant (uncorrected) for any physical testing and for validation depth".
10. **Sec. V-C.** "Naming a specific hazard did not make the acknowledgment less likely: 80.0% of hazard-specific and 58.3% of generic studies acknowledged it, a difference that is not statistically distinguishable (p = 0.30)."
11. **Abstract.** Add the HM interval and flag exploratory status: "Their field-testing rate was 7.4% (95% CI 2.1-23.4) vs. 33.3% (13.8-60.9) with strict coding (exploratory p = 0.060) and 11.1% vs. 50.0% with lenient coding (p = 0.014)." Replace "(40.7% vs. 83.3%; exploratory Fisher p = 0.018)" by "(40.7% vs. 83.3%; OR 0.14, 95% CI 0.01-0.87; exploratory Fisher p = 0.018; not corrected for multiplicity)".

Suggested compact footnote under Table XIII: "Two-sided Fisher exact test; OR = conditional maximum-likelihood estimate with exact 95% CI; all tests post hoc and unadjusted. Holm-adjusted p across the five contrasts discussed in Sec. III-D: 0.085 (strict field), 0.070 (lenient field), 0.072 (any physical), 0.085 (VD = 3), 0.073 (Mann-Whitney VD)."

## 6. Notes on method

- Wilson formula in `check_stats.py` matches `analysis.py`; OR from `scipy.stats.contingency.odds_ratio(kind="conditional")`.
- Freeman-Halton exact: enumeration over all 4 x 2 tables with the observed margins, summing hypergeometric probabilities <= the observed table's probability.
- Holm adjustment computed over the five tests listed in the footnote (choice of family is mine; with the three most favourable tests only, Bonferroni gives 0.042, 0.054, 0.073).
- The Wilson CIs for 0/12 and 0/13 are given because "none of the 12 multi-robot studies reached a field test" is a strong statement on a small cell; the upper bound is 24%.
