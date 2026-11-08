# Extraction rebuild report (extraction-rebuilder), 2026-11-08

## LOCKED-NUMBER STATUS: CHANGED, so the run stopped

**Locked fact affected:** "35/39 (89.7%) report environmental-realism limitations" (and the Sec. V-B split: Generic 20/21, hazard-specific 15/18).

I applied the agent's rule literally. A paper is coded Y only if **the paper itself** says that its test environment left out or idealized physical conditions of the target disaster, or that validation stayed in simulation or the lab with real-environment testing left to future work. Under that rule, 5 of the first 15 papers coded are N. So the corpus total can be **at most 34/39**, even if all 24 uncoded papers turned out Y. Following the binding STOP rule, I stopped coding at that point (ref [22]). I also coded [23] and [24], whose evidence I had already read. Nothing in the manuscript was edited.

Evidence for each N (PDF page = physical page of the file in `assets/papers/`):

| Ref (record) | Scenario | Why N | Pages checked |
|---|---|---|---|
| [10] (6) | Generic | Tested indoors and outdoors in 22.9 km/h wind and 65–100 dB noise. Its future work covers other robots and SAR contexts, faster NeRF and new sensors. It never says the test conditions were idealized. | p9–p12 |
| [11] (77) | Generic | Its Limitations section (p18) lists only onboard-sensor scope, budget, and shortened impact and recognition tests. No environmental caveat. The outdoor tests were on a mountain in Beaufort-5 wind (p17). | p17–p18 |
| [16] (73) | Underground | Fielded at the DARPA SubT final (p20), and the semantic navigation was also tested in a university building (p29, p31). Its stated limitations are algorithmic (map-origin error correction, simple semantic mapping; p35). | p20–p35 |
| [17] (106) | Generic | **Borderline.** It says the vision system limits the framework and that the semantic examples were "relatively simple" (p12). That is about semantic complexity, not left-out physical conditions. | p11–p12 |
| [22] (9) | Generic | Gazebo simulation only. Its future work is multiple victims and multiple floors (p17–p18). It never says real-environment testing is pending, and it claims its ray tracer models non-ideal conditions (p11). | p9–p18 |

Even without the borderline [17], 4 papers are clear N, so the most the corpus can reach is 35/39. That holds only if every remaining paper is Y, including ones I have not read. Three borderline Y codes ([15], [18], [23]) could also turn into N on review. Four of the five N papers are Generic-scenario papers. That alone contradicts the manuscript's Generic 20/21 (which allows only one Generic N).

**Likely cause (inference, not verified):** the manuscript's 35/39 probably came from the old field-17 "Reported limitation" text with a looser reading, e.g. counting any limitation about terrain, sensors or scope. The original coding rule was never written down, so I cannot reproduce it. The authors need to decide which rule they meant. Then either (a) re-run the coding with that rule written into the Methods, or (b) keep this rule and revise the 89.7% claim in the Abstract, Sec. V-B, Conclusion and any figure. Until then, treat 35/39 as **UNVERIFIED**.

## What was completed

- **Fully coded: 15 of 39 papers** (refs [10]–[24]: all 12 Teleoperation, Supervisory and Shared papers, plus the first 3 FA multi-robot papers).
- **Not coded: 24 papers** (refs [25]–[48]). These rows carry `coding_status = NOT CODED…` and contain only metadata (citation, venue and DOI from Sec. 15) and the manuscript's own labels in `manuscript_mode`, `manuscript_platform` and `manuscript_fa_cluster`. These labels are copied from the manuscript (Sec. IV lists and Sec. 6B), not rebuilt from the PDFs. No other cells were filled for these rows.
- Text was extracted with `pdftotext -enc UTF-8` into my own scratchpad folder (`…/scratchpad/xr/t/`), not the shared `txt/`. All 39 extracted first pages were checked against the titles in `data/id_map.csv`: 0 mismatches. None of my coding used the shared `txt/` folder that other agents overwrote.

## Coding rules used

- **Mode, platform, architecture, scenario, sensors:** Sec. 6A precedents A–G, 6B (per-ID table), 6D (location at runtime), 6E (terrain/setting, not hazard), and 6F (RGB-D sets both Visual and Depth).
- **Validation (6C buckets):** *Real-world field test* = a physical system tested in an outdoor or mission-representative real site. *Partial* = a physical system or embedded deployment tested in a controlled lab/arena, or on synthetic inputs. *Prototype bench test* = a prototype was built but performance was evaluated off-mission. *Simulation only* = no physical test.
- **human_role_modelled:** Y if a real or simulated human operator, supervisor or participant acts during the tested mission. Y was **not** given just because the design includes an operator when the tested pipeline had none ([13]: images fed offline to a Jetson; [14]: MATLAB simulation).
- **env_realism_limitation:** the agent rule above, author-stated only. `env_realism_confidence` records clear or borderline.
- **VDR:** `vd` 1 = abstract simulation, 2 = physics-based simulation or physical lab/bench, 3 = mission-representative outdoor or real site. `rp` 1 = high-level only, 2 = enough parameters and setup to re-implement, 3 = also a public code or data link (author "on request" offers do not count). `stat` = Y for repeated trials with variance/CI, **or** a comparison against a baseline.
- Every coded cell has a `_page` column. "not reported" is used where the paper is silent (for example, the compute hardware of [12]).

## Agreement with existing labels (15 coded papers)

- **Mode:** 15/15 agree with the manuscript.
- **Platform:** 15/15 agree with Sec. 6B.
- **FA cluster:** 3/3 agree.
- **Validation:** the Teleoperation (3 field / 1 partial / 1 bench), Supervisory (3/1/0/0) and Shared (2 sim / 1 partial) rows of Table XI **reproduce exactly**: field tests [10], [11], [12], [15], [16], [18]; partial [13], [17], [20]; bench [14]; simulation only [19], [21]. So the locked "60–75% for Teleop/Supervisory" holds for these rows. The FA rate (2/27) and UAV 1/13 vs Hybrid 4/7 **could not be checked**, because the run stopped first. In the coded subset, Hybrid is 4/4 field-tested and UAV 1/5, which so far fits the manuscript.
- **Disagreements with manuscript or working-record conventions (not locked numbers):**
  1. **[21] (rec 126), Physiological flag.** Sec. 6F says only record 105 has a Physiological sensor. But [21] measures participants' heart-rate variability (HRV) (p15). By the same rule it should be flagged, giving at least 2 Physiological papers, not 1. Table VIII would change.
  2. **[15] (rec 57), RF flag.** Sec. 6F lists RF for record 57. I found only a Wi-Fi antenna and a 5G mention in related work (p3, p5). That is communication, not RF sensing. I left RF = 0 and recorded both readings here. Gas = 1 is supported by the gas-concentration display (p9).
  3. **[16] (rec 73), validation.** I kept it as Real-world field test (planner fielded at the DARPA SubT final, p20). Note that the semantic-navigation contribution itself was tested in a university building (p29–p33), as the coordinator also reported. If the authors classify by the headline contribution, it could be Partial. That would change Table XI's Supervisory row and the locked "75%".
  4. **[15] (rec 57).** Its "field" test was in a university coal-dust/gas explosion laboratory tunnel with placed debris (p20). I coded it as a field test (mission-representative site). A stricter reading would make it Partial and change the locked Supervisory 75%. This needs an author decision.
  5. **Architecture** for [11] and [18] has low confidence (the runtime location of inference is not stated). The marginals cannot be compared with Table IX on 15 rows.

## Recomputed tables (15 coded rows; full output in `data/recomputed_tables.md`)

- Mode: Teleop 5, Supervisory 4, Shared 3, FA 3 (partial by design). The manuscript-label marginals for all 39 reproduce Table V (27/5/4/3) and Table VII.
- Validation: Sim 5, Field 6, Partial 3, Bench 1.
- Environmental realism: Y 10/15, N 5/15. Generic 4/8 Y; hazard-specific 6/7 Y.
- Human role modelled: Teleop 3/5, Supervisory 4/4, Shared 3/3, FA 0/3.
- VDR mean: Teleop 4.60, Supervisory 5.00, Shared 3.33, FA 3.33 (FA n = 3 only).
- Public code or data link (rp = 3) among coded rows: [16] only. Among the uncoded papers, the data-availability scan found links in [32], [34], [35] and [46] (to be confirmed when coded).

## Comparison with manuscript numbers

| Manuscript number | Rebuilt status |
|---|---|
| Table V modes 27/5/4/3 | Labels consistent; 15/15 coded agree |
| Table XI Teleop, Sup, Shared rows | Reproduced exactly (subject to points 3–4 above) |
| FA 2/27 field-tested | Not checked (stopped) |
| UAV 1/13, Hybrid 4/7 | Not checked; subset consistent |
| **35/39 env-realism (89.7%); Generic 20/21; specific 15/18** | **Not reproducible under the stated rule: ≥5 N already (≤34/39); Generic already has 4 N** |
| Table VIII Physiological = 1 | At least 2 under the 6F rule ([21] HRV) |

## Files

- `C:\Users\chinmoy\Downloads\review paper\data\extraction_table.csv` (39 rows; 15 CODED, 24 NOT CODED)
- `C:\Users\chinmoy\Downloads\review paper\data\recompute_tables.py` (reads only the CSV)
- `C:\Users\chinmoy\Downloads\review paper\data\recomputed_tables.md`
- Row source scripts (scratchpad): `C:\Users\chinmoy\AppData\Local\Temp\claude\a400f87f3796922f\8677c719-5be6-4116-a066-c744e4214cb8\scratchpad\xr\rows_a.py`, `rows_b.py`, `rows_c.py`, `build.py`

## To resume

Once the authors confirm the env-realism rule (or tell me to carry on and report the full-corpus count), code refs [25]–[48]. The coordinator's audit notes for those papers need checking against page evidence when they are coded: [36] and [39] real-world; [38] Partial; [37] and [40] sim-only; [43] calm indoor pool. If [36] and [39] are both field tests, they would account for FA's 2 field tests, which would make [25]'s single-UGV hardware trial and [42]'s forest NBV data non-field (Partial). That needs checking.
