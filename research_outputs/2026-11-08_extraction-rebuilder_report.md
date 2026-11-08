# Extraction rebuild report (extraction-rebuilder), 2026-11-08 (final, full corpus)

**Scope:** all 39 included papers were coded from their full-text PDFs. Every cell has a `_page` column (the PDF page = the physical page of the file in `assets/papers/`). The master document was **not** edited.

**History:** the first run stopped at ref [22], because the environmental-realism count could no longer reach 35/39 (the stop rule). The coordinator confirmed that the discrepancy had been reported to the authors and asked for the full corpus. The authors then decided that the **literal (author-stated) env-realism rule** and **strict validation coding** are primary. The **broad** env-realism rule and **lenient** validation coding are sensitivity checks.

**Text extraction:** all text was extracted into my own folder (`scratchpad/xr/t/`, `pdftotext -enc UTF-8`). It was never read from the shared `txt/` folder that other agents overwrote. All 39 first pages matched their `id_map.csv` titles (0 mismatches).

## LOCKED-NUMBER STATUS (primary codings, with sensitivity check in brackets)

| Locked fact | Rebuilt value | Status |
|---|---|---|
| Modes: FA 27 / Teleop 5 / Sup 4 / Shared 3 | 27 / 5 / 4 / 3. All 39 mode labels agree with the manuscript. | **UNCHANGED** |
| FA field-tested 2/27 (7.4%) | Strict: **2/27 (7.4%)**, refs [36], [44]. [Lenient: **3/27 (11.1%)**, refs [36], [39], [44].] | Number **UNCHANGED under the primary coding**, but rests on different papers (see note A). **CHANGED under lenient coding.** |
| "60–75% for Teleop/Supervisory" | Strict: Teleop 3/5 (60%), **Supervisory 1/4 (25%)**. [Lenient: 3/5 (60%) and 3/4 (75%).] | **CHANGED under the primary coding.** Unchanged under lenient. |
| UAV field-tested 1/13 (7.7%) vs Hybrid 4/7 (57.1%) | **UAV 3/13 (23.1%)** under both codings (refs [18], [36], [44]). Hybrid: strict **3/7 (42.9%)** [lenient 4/7 (57.1%)]. | **CHANGED.** The UAV figure changes under both codings. |
| 35/39 (89.7%) report environmental-realism limitations | Literal: **26/39 (66.7%)**. [Broad: **33/39 (84.6%)**.] | **CHANGED under both rules.** |
| Sec. V-B: Generic 20/21 (95.2%) vs hazard-specific 15/18 (83.3%) | Literal: Generic **14/24 (58.3%)**, hazard-specific **12/15 (80.0%)**. [Broad: 19/24 (79.2%), 14/15 (93.3%).] | **CHANGED.** The direction reverses under both rules: hazard-specific papers report the gap more often, the opposite of the claim. |
| 130 → 5 → 125 → 39 / 86; Kareem et al. facts | Not tested by this agent. | Out of scope |

**What still holds:** the qualitative inverse pattern. Under strict coding, FA papers are field-tested 2/27 (7.4%), against 4/12 (33.3%) for the human-in-mission modes (Fisher exact two-sided p = 0.060). Under lenient coding it is 3/27 (11.1%) against 6/12 (50.0%), p = 0.014. A human acts in the tested setup in 1/27 FA papers, against 10/12 papers in the other modes. The "60–75%" wording and the size of the gap in Fig. 6 depend on whether mock facilities count as field tests.

**Note A (FA field tests):**
- **[44] (record 100).** It flew a DJI Mini 3 Pro outdoors over a playground, bushland and a forest, with 10 human subjects and 10 decoys (p8). That is a real outdoor site, so it is a field test under both codings.
- **[39] (record 55).** It is outdoors, but on a constructed "simulated volcanic terrain" course under clear sky (p7, p9). Lenient = field; strict = Partial.
- **[36] (record 20).** One flight in a real underground car park (p12). I coded it as a field test under both codings, but this is borderline: it is a real GNSS-denied site, not a mock facility, yet it is not a disaster site.
- **[42] (record 17).** Its real forest data were collected and then scored offline (p9, p11), so it is Partial under both codings (Precedent B).

So the manuscript's "2" probably meant [36] and [39], which is the coordinator's audit reading. My strict "2" is [36] and [44].

## Coding rules

- **Clean categories:** Sec. 6A precedents A–G (mode), 6B (platform), 6D (architecture at runtime), 6E (terrain/setting), 6F (sensor flags; RGB-D = Visual + Depth). Where the PDF does not state the architecture, it is coded "Not reported" rather than forced into a bucket ([12], [46]).
- **validation_strict (primary; = `validation_clean`):**
  - *Real-world field test* = a physical system tested in a real, non-mock outdoor site or a real disaster-like site.
  - *Partial* = a physical system in a mock or lab facility (university lab, indoor arena, pool, explosion-lab tunnel, constructed competition or terrain course, real-data-then-offline), or simulation plus a limited physical test.
  - *Prototype bench test* = a prototype or tabletop mock evaluated off-mission.
  - *Simulation only* = no physical test.
- **validation_lenient (sensitivity):** the same rules, except that a physical test in an outdoor constructed course or a competition venue counts as a field test.
- **env_realism_limitation (primary, literal):** Y only if the paper itself says that its test environment omitted or idealized physical conditions of the target disaster, or that validation was limited to simulation or the lab with real-environment testing left to future work. Each code is marked clear or borderline in `env_realism_confidence`.
- **env_realism_broad (sensitivity):** Y if the stated limitations mention any real-world-condition gap, including sensor or communication limits, or the absence of field testing.
- **human_role_modelled:** Y if a real or simulated human operator, supervisor or participant acts during the tested mission. A design-only operator does not count.
- **VDR score:**
  - `vd`: 1 = abstract simulation; 2 = physics-based simulation or physical lab/bench test; 3 = mission-representative outdoor or real site.
  - `rp`: 1 = method described at a high level only; 2 = enough parameters and setup to re-implement; 3 = also a public code or data link from the authors (third-party benchmark datasets and "on request" offers do not count).
  - `stat` = Y for repeated trials with variance/CI, or a comparison against a baseline.

## Borderline calls (all recorded in the CSV `*_note` / `env_realism_confidence` columns)

- **Literal env-realism, borderline:**
  - [15]: method limitation under dynamic collapse.
  - [17] (coded N): "simple" semantic examples.
  - [18]: field terrain simpler than other sites.
  - [23]: only "3D future work".
  - [25] (coded N): real grass/wind LiDAR failures, but no claim that the test omitted conditions.
  - [28]: static-obstacle assumption.
  - [31]: idealizing assumptions stated in the setup.
  - [32]: terrain-friction simplification.
  - [36]: SAR-scenario testing left to future work.
  - [42] (coded N): offline evaluation and battery assumption.
  - [45]: static-survivor assumption.
- **Clear literal N (13 papers):** [10], [11], [16], [17], [22], [25], [33], [35], [42], [44], [46], [47], [48]. Of these, [17], [25] and [42] are borderline; the other 10 are clear. Even if all 3 borderline N papers became Y, the total would be 29/39, still well short of 35.
- **Validation:** [16] (strict Partial: the SubT final is a constructed competition course, and the semantic navigation was tested in a university building, p29–p33); [15] (explosion-lab tunnel, Partial); [39] (constructed volcanic course, Partial); [36] (real car park, field); [47] (tabletop mock: strict Bench, lenient Partial).
- **Scenario:**
  - [29]: RCRS is an earthquake-derived simulator, but the paper frames the scenario generically; coded Generic.
  - [38]: "collapsed or underground", tested on mock rubble; coded Earthquake/Structural Collapse.
  - [41]: Byland outdoor trails; coded Generic.
  - [46]: NIST-style rubble; coded Generic.
- **Human role:** [42] coded Y (the real data-collection flight was human-piloted, per Precedent B).

## Differences from other manuscript tables (not locked; the manuscript's marginals come from the lost workbook)

| Table | Manuscript | Rebuilt | Main reasons (refs) |
|---|---|---|---|
| VI Platform, VII Mode×Platform | as printed | identical (39/39 platform labels agree) | — |
| VIII Sensors | Visual 20, IMU 13, LiDAR 12, GPS 10, None 10, Thermal 7, Depth 5, Gas 3, RF 3, Acoustic 2, Physio 1 | Visual 17, IMU 13, LiDAR 14, GPS 7, None 10, Thermal 5, Depth 5, Gas 3, RF 2, Acoustic 3, Physio 2 | Physio: [21] records participants' heart-rate variability (p15). RF: I found no RF sensing in [15], only Wi-Fi communication. The others are judgment calls on which simulated or related-work sensors count. |
| IX Architecture | PC 15, Onboard 13, Hybrid 10, Cloud 1 | PC 21, Onboard 7, Hybrid 8, Cloud 1, Not reported 2 | Sec. 6D calls [37] (record 46) Onboard/Edge, but its PDF shows simulation only (Gazebo/MATLAB, p6–p9). Simulation-only papers are coded PC/Offline per Sec. 6D. |
| X Validation | Sim 18, Partial 10, Field 8, Bench 3 | Strict: Sim 18, Partial 12, Field 6, Bench 3. [Lenient: 18 / 10 / 9 / 2.] | See the locked-number table above. |
| XII Scenario | Generic 21, Underground 6, Earthquake 5, Wilderness 4, other categories 1 each | Generic 24, Underground 5, Earthquake 3, Wilderness 4, other categories 1 each | Borderline scenario calls listed above. |

## Other recomputed results (full tables in `data/recomputed_tables.md`)

- **FA cluster × validation (strict):**
  - multi-robot coordination: 12 papers, 0 field (10 sim, 2 Partial);
  - single-robot navigation: 7 papers, 1 field ([36]);
  - perception-driven: 5 papers, 1 field ([44]);
  - platform-architecture: 3 papers, 0 field.

  This supports the Sec. IV-D statement that the multi-robot cluster has almost no physical validation: only [25]'s hybrid single-UGV trial and [32]'s energy profiling, both Partial.
- **VDR, mean (vd / rp):** Teleop 4.60 (2.60 / 2.00); Supervisory 5.00 (2.75 / 2.25); Shared 3.33 (1.33 / 2.00); FA 3.81 (1.70 / 2.11). 35/39 papers report a baseline comparison or variance. 5 papers have a public code or data link from the authors ([16], [32], [34], [35], [46]).
- **Agreement with manuscript labels:** mode 39/39, platform 39/39, FA cluster 27/27.

## Recommendations for the authors (the manuscript is not edited here)

1. Replace "35/39 (89.7%)" with the rule-based figure (literal 26/39, 66.7%), state the rule in the Methods, and report the broad reading (33/39) as a sensitivity check. Rewrite Sec. V-B: the Generic-vs-specific comparison now runs in the other direction.
2. Report the autonomy–validation contrast under strict coding (FA 7.4% vs human-in-mission 33.3%), with the lenient coding as sensitivity. Revise "60–75%": under strict coding, Supervisory is 25%.
3. Revise "UAV 1/13" to 3/13, and give Hybrid as 3/7 (strict) or 4/7 (lenient).
4. Update Tables VIII, IX, X and XII, or explain the differences. A human second coder should check the borderline calls listed above.

## Files

- `C:\Users\chinmoy\Downloads\review paper\data\extraction_table.csv`: 39 rows, all CODED. It includes `validation_strict`, `validation_lenient`, `env_realism_limitation`, `env_realism_broad`, the confidence/note columns, and the manuscript_* comparison columns.
- `C:\Users\chinmoy\Downloads\review paper\data\recompute_tables.py`: reads only the CSV. It uses scipy for the Fisher tests.
- `C:\Users\chinmoy\Downloads\review paper\data\recomputed_tables.md`
- Row sources in the scratchpad: `C:\Users\chinmoy\AppData\Local\Temp\claude\a400f87f3796922f\8677c719-5be6-4116-a066-c744e4214cb8\scratchpad\xr\rows_a.py` to `rows_g.py`, and `build.py`.
