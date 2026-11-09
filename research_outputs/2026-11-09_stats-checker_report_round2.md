# Stats-consistency check, round 2: revised manuscript (Secs. 9-14), 2026-11-09

Scope: Title/Abstract/Conclusion, Sections I-V, Tables I-XX, Figs. 1-7. Independent recomputation from `data/extraction_table.csv` (39 rows, incl. 2026-11-09 recodes of refs 14, 17, 20, 42 and the `identification_route` column), `data/function_autonomy.csv` (39 rows), `data/reliability_blind_codes.csv`, `supplementary/screening_log.csv` (125 rows). Nothing in the manuscript or data was edited.

Scripts (run from any directory with `python`, not `-I`, because pandas is in the user site):
- `research_outputs/2026-11-09_stats-checker_scripts/check_stats.py` (round 1, re-run unchanged on the new CSV)
- `research_outputs/2026-11-09_stats-checker_scripts/check_round2.py` (new: Table XX, XIX, Table V first-criterion, sensitivity (d)(e), Holm)
- `check_prisma.py` unchanged; PRISMA/Table II inputs (paperlinks.xlsx, screening log) were not modified, and the log's route counts (publisher 18 + 59, GS 10 + 4, ChatGPT 9 + 22, Gemini 2 + 1) still reproduce Sec. II-K and Fig. 2.

## 1. Verdict

All arithmetic reproduces: every count, percentage, Wilson CI, OR, OR CI, Fisher p, Holm p, Freeman-Halton p, Mann-Whitney p, sensitivity cell (a)-(e), Table XIX row, Table XX cell and Table V column. Two real discrepancies remain (N1, N2) plus four wording points (N3-N6). All four items I raised as M1-M4 are resolved.

| # | Severity | Issue |
|---|---|---|
| N1 | Low (easy fix) | Sec. II-I says "**Four** sensitivity analyses test the primary contrast" and then lists five, (a)-(e). Table XVII and Sec. III-G also have five. |
| N2 | **Medium** | `function_autonomy.csv` codes ref 48 (Vani et al., Fully Autonomous) `evaluated_human_presence = Y` (p. 11: "both modes exercised in tests", operator remote control), whereas `extraction_table.csv` has `human_role_modelled = N`. The manuscript uses N and states "none of the 27 FA studies" in Abstract, I (contribution 2), III-A, V-B, Conclusion, Fig. 7 and Table XII (0/27). The two supplementary files therefore disagree (9 vs 8 humans in evaluated mission overall; 1/27 vs 0/27 in FA). Sec. IV-D says its tests "do not state which mode was used", which fits N but not the S7 note. Decide one coding for ref 48 and make S2 and S7 agree. If it is changed to Y, "none of 27" becomes "26 of 27" in about six places, Table XII FA row becomes 1/27 and all-row 9/39, III-A "8 of 12" is unchanged (ref 48 is FA). The primary contrast does not use this variable, so no p-value changes. |
| N3 | Low | Sec. V-A bullet 2: "No difference in reproducibility ... This suggests the difference lies in where studies are tested rather than in how carefully they are reported." A non-significant MW test (n = 27 vs 12, RP 33 of 39 at level 2) is not evidence of equivalence. Soften (see Sec. 5). |
| N4 | Low | Sec. III-G (a) and V-A: "The gap is therefore concentrated in abstract and sensor-free simulation studies" is stated as a finding, although the paragraph itself says the filter removes only sim-only FA studies, so attenuation is by construction (FA physical count stays 11). "Concentrated" is a restatement of the filter, not a result. |
| N5 | Low | Table XVII has nominal p < 0.05 cells in (d) any-physical (0.043) and (e) lenient (0.044, 2/14 vs 3/4, OR 0.07, 95% CI 0.001-1.33, n = 4 in one arm) that are not mentioned in the text. Add one sentence that sensitivity p-values are unadjusted and (e) is not interpretable. |
| N6 | Low | Holm family is the five rows of Table XIII (includes the overlapping secondary contrast FA vs Tele + Sup, and excludes the MW VD test quoted in III-D). Say so. Adding MW (six tests) leaves all adjusted p > 0.05 (0.085, 0.122, 0.171, 0.180, 0.180, 0.180), so the claim "no contrast survives" is robust to the choice. |

## 2. Mismatch list (location -> found -> expected)

| Location | Found | Expected |
|---|---|---|
| Sec. II-I, sensitivity intro | "Four sensitivity analyses" | "Five sensitivity analyses" (a)-(e) |
| Abstract, I.2, III-A, III-D (Table XII), V-B, VI, Fig. 7 caption text | FA human in evaluated mission 0/27 | Consistent with S2 (ref 48 = N) but contradicted by S7 (ref 48 = Y); resolve (N2) |
| Sec. V-A, RP bullet | "suggests the difference lies in where studies are tested" | "No detectable difference ... this does not show equivalence" (N3) |
| Sec. III-G (a) last sentence | "therefore concentrated in abstract and sensor-free simulation studies" | state it is a property of the filter (N4) |

No other mismatch. In particular the following were rechecked against the new CSV and agree: Abstract (130/78/15/37/125/39, 69.2%, 5/4/3, 16 sim-only, 7.4% [2.1-23.4], 33.3%, p = 0.060, 11.1%/50.0% p = 0.014, two thirds, 5 of 39); Table VI-X; Table XI (19/12/6/2 strict, 19/10/9/1 lenient); Table XII all cells (HIE 3/5, 3/4, 2/3, 0/27, 8/39; any physical 80/100/33.3/40.7/51.3; mean VD 2.40/2.75/1.33/1.70/1.87); Table XIV, XV, XVI, XVIII.

## 3. Recomputed inference (all two-sided; OR = conditional MLE with exact CI)

| Contrast | Groups | OR (95% CI) | p | Holm p (Table XIII) | Manuscript |
|---|---|---|---|---|---|
| Field strict, FA vs HIL | 2/27 vs 4/12 | 0.169 (0.0130-1.431) | 0.0601 | 0.128 | OK |
| Field lenient | 3/27 vs 6/12 | 0.134 (0.0165-0.837) | 0.0141 | 0.071 | OK |
| Any physical | 11/27 vs 9/12 | 0.238 (0.0337-1.242) | 0.0824 | 0.128 | OK |
| VD = 3 | 4/27 vs 6/12 | 0.184 (0.0276-1.054) | 0.0427 | 0.128 | OK |
| Strict, FA vs Tele + Sup | 2/27 vs 4/9 | 0.109 (0.0078-0.992) | 0.0245 | 0.098 | OK |
| UAV vs Hybrid strict | 3/13 vs 3/7 | 0.420 (0.037-4.54) | 0.613 | n/a | OK (0.61) |
| UAV vs Hybrid lenient | 3/13 vs 4/7 | 0.245 (0.021-2.35) | 0.174 | n/a | not cited |
| Realism, generic vs hazard-specific | 14/24 vs 12/15 | 0.359 (0.052-1.85) | 0.295 | n/a | OK (0.30) |

- Holm uses unrounded p (0.0601, 0.0141, 0.0824, 0.0427, 0.0245): adjusted 0.1281, 0.0706, 0.1281, 0.1281, 0.0980. Matches the table and the text range "0.071-0.128".
- Mann-Whitney VD: U = 103.5, p = 0.0600 (means 1.70 vs 2.25). RP: U = 167.0, p = 0.827 (2.11 vs 2.08). Both match.
- Freeman-Halton exact (full enumeration, probability ordering): strict 0.0291 (table [[3,2],[1,3],[0,3],[2,25]]), lenient 0.0058. Matches "0.029" and "0.006".
- Reliability: 35/39 (89.7%), kappa 0.789, analytic CI 0.61-0.97, AC1 0.878, binary 37/39 kappa 0.880. Matches Sec. II-G. The four disagreements are refs 18, 20, 21, 48 and are described correctly.

Sensitivity analyses (Fisher, strict / lenient / any physical), all recomputed:

| Analysis | n FA/HIL | Strict | Lenient | Any physical | Manuscript |
|---|---|---|---|---|---|
| Primary | 27/12 | 2/27 v 4/12 p 0.060 | 3/27 v 6/12 p 0.014 | 11/27 v 9/12 p 0.082 | OK |
| (a) physical platform only | 17/12 | p 0.198 (OR 0.28, 0.02-2.45) | p 0.106 | p 0.694 (OR 0.62, 0.08-4.0) | OK |
| (b) RP >= 2 | 26/12 | 2/26 p 0.066 | 3/26 p 0.016 | 10/26 v 9/12 p 0.079 | OK |
| (c) blind codes | 27/12 | 3/27 v 3/12 p 0.348 (OR 0.39, 0.04-3.4) | 4/27 v 5/12 p 0.102 | 11/27 v 9/12 p 0.082 | OK |
| (d) +2 FA sim-only (projection) | 29/12 | 2/29 p 0.0500 (0.05001) | 3/29 p 0.0106 | 11/29 p 0.0431 | OK |
| (e) publisher-only | 14/4 | 2/14 v 1/4 p 1.000 | 2/14 v 3/4 p 0.0441 | 6/14 v 3/4 p 0.577 | OK; route counts 18 publisher + 21 other confirmed |

(a): the filter removes 10 FA and 0 HIL studies, all 10 simulation-only (FA physical stays 11), as stated.

## 4. Other tables

- **Table XX vs `function_autonomy.csv`**: all 20 mode x function cells and the All row match exactly (T 0/0/5, 3/1/1, 0/0/5, 0/1/4; S 2/1/1, 3/0/1, 0/3/1, 4/0/0; C 0/1/2, 1/1/1, 0/2/1, 1/0/2; F 24/2/1, 27/0/0, 25/1/1, 25/2/0; All 26/4/9, 34/2/3, 25/6/8, 30/3/6). Text: analysis machine-held 34/39 (3 of 5 Tele) OK; Tele decision human 5/5 OK; Supervisory action machine 4/4 OK; FA all four functions machine-held 24/27 OK (24 studies overall, all FA). "Matched the mode labels for 36 of 39": confirmed; exceptions are refs 21 (C coded, designed S), 47 and 48 (FA coded, designed C), which are discussed in IV-C and IV-D. "Three studies have three different profiles" (SC): true (acq 0/1/2, 1/1/1 etc.; refs 19, 20, 21 differ).
- **Table XIX vs CSV**: nine lenient field studies = refs 10, 11, 12 (Tele, Hybrid), 15, 16, 18 (Sup; UGV, Hybrid, UAV), 36, 39, 44 (FA; UAV, UGV, UAV). Strict codes in the "Site and scope" column match (field: 10, 11, 12, 18, 36, 44; partial: 15, 16, 39). Mode and platform columns match. Strict field = 3 + 1 + 2 = 6 OK.
- **Table V first-criterion column vs `screening_log.csv`**: first-failed criterion C1 63, C2 22, C3 1 (total 86) OK; non-exclusive 63/28/7 (98) OK; combinations C1 56, C2 17, C3 1, C1/C2 6, C2/C3 5, C1/C3 1 OK.
- **Figures** (all four regenerated 2026-11-09 viewed): `fig_sensor_prevalence.png` (17, 14, 13, 10, 7, 5, 5, 3, 3, 2, 2 with rounded percentages), `fig_validation_type.png` (19/19, 12/10, 2/1, 6/9), `fig_autonomy_validation.png` (labels 3/5, 3/5, 1/4, 3/4, 0/3, 0/3, 2/27, 3/27; whiskers 23-88, 5-70, 0-56, 2-23, 4-28, 30-95), `fig_taxonomy.png` (5/12.8, 3/7.7, 4/10.3, 27/69.2; LOA 1-2, 3-5, 5-7, 8-10) all match the CSV and tables. Cosmetic only: Fig. 7 order is Tele, Shared, Supervisory, FA, whereas Tables VI, VIII, XII and Fig. 6 use Tele, Supervisory, Shared, FA; Fig. 4 uses integer percentages while Table IX uses one decimal.

## 5. Status of round-1 issues

| Round-1 item | Status |
|---|---|
| M1 sensitivity list mismatch | Resolved, except the "Four" vs five count (N1). |
| M2 "Freeman-Halton" vs MC p | Resolved: text now reports exact 0.029 / 0.006. |
| M3 sensitivity (a) cannot support "research genre" | Mostly resolved: by-construction caveat added in III-G and V-A, "largely disappears" removed, intro contribution 2 hedged, Conclusion "If real, we read it, cautiously". Residual: N4 wording. |
| M4 "statistically clear" vs no multiplicity correction | Resolved: Holm column added, "clear" removed, Conclusion and V-D say no contrast survives. |
| (d) p = 0.050 | Reported as 0.050, not called significant: resolved. |
| V-C "somewhat more frequent" | Resolved ("not more common ... no difference was detected"). |
| RP "do not differ" | Partly resolved ("no difference ... detected"), but the inference sentence remains (N3). |
| Hit-count / Google Scholar placeholder | Still an AUTHOR INPUT placeholder (two logged GS queries vs seven in notes); not a stats issue, authors must confirm. |
| Abstract: add HM interval, exploratory flag | Done (HM interval is not in the abstract, but 33.3% with p and the multiplicity sentence are). Optional: add "(13.8-60.9)". |
| Cosmetic mode order, Fig. 4 rounding | Unchanged (cosmetic). |
| Not traceable to data (AI re-check of 23 excluded; Cho "4 of 10"; external figures) | Unchanged; flag to authors / citation-verifier. |

## 6. Recommended replacement sentences

1. **II-I:** "Five sensitivity analyses test the primary contrast:" (replace "Four"). Add after the list: "Sensitivity p-values are unadjusted and are reported to show direction, not to confer significance."
2. **III-D, after the Holm sentence:** "The Holm family is the five rows of Table XIII; adding the Mann-Whitney test on validation depth (p = 0.060) does not change this conclusion."
3. **III-G (a), last sentence:** replace "The gap is therefore concentrated in abstract and sensor-free simulation studies." with "Because every excluded Fully Autonomous study is simulation-only, this attenuation is expected from the filter alone and cannot show that the gap is confined to those studies."
4. **V-A, bullet 1:** "The contrast is weaker (strict field testing OR 0.28, 95% CI 0.02-2.45, p = 0.20) when only studies with a physical platform are compared, although that filter removes only simulation-only Fully Autonomous studies."
5. **V-A, bullet 2:** "No difference in reproducibility scores was detected (mean RP 2.11 vs 2.08, p = 0.83). With 39 studies and most scoring 2, this is weak evidence of similarity, not evidence of equivalence."
6. **V-D Conclusion validity, bullet 2:** "The headline contrast is nominally significant under some codings and outcomes (p = 0.014 lenient field testing; p = 0.043 mission-representative site) but not others, and none survives Holm adjustment."
7. **N2 (authors' decision):** either recode ref 48 to N in S7 (the paper says its tests do not state which mode was used) or recode to Y in S2 and update all "none of 27" statements. Do not release S2 and S7 in disagreement.
8. **Optional Table XVII footnote:** "Two-sided Fisher exact tests, unadjusted. (d) is a projection, with the two added records assumed Fully Autonomous and simulation-only. (e) has n = 4 in the human-in-the-loop arm and cannot support inference."

## 7. Wilson CIs for headline cells (unchanged by the recodes except human-in-loop any-physical)

| Quantity | Estimate (95% Wilson CI) |
|---|---|
| FA field, strict | 2/27 = 7.4% (2.1-23.4) |
| HIL field, strict | 4/12 = 33.3% (13.8-60.9) |
| FA / HIL field, lenient | 3/27 = 11.1% (3.9-28.1); 6/12 = 50.0% (25.4-74.6) |
| FA / HIL any physical | 11/27 = 40.7% (24.5-59.3); 9/12 = 75.0% (46.8-91.1) |
| FA / HIL VD = 3 | 4/27 = 14.8% (5.9-32.5); 6/12 = 50.0% (25.4-74.6) |
| UAV / Hybrid field strict | 3/13 = 23.1% (8.2-50.3); 3/7 = 42.9% (15.8-75.0) |
| Realism limitation | 26/39 = 66.7% (51.0-79.4) |
| Public code/data | 5/39 = 12.8% (5.6-26.7) |
