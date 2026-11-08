# Full paper audit — SAR Robotics Systematic Review (manuscript in `SAR_review_master_document.md`)

**Date:** 2026-11-08 · **Mode:** find-and-prove only; no manuscript text was changed.
**Line numbers** refer to `SAR_review_master_document.md` as of this audit (1,085 lines).

**Agent reports this audit builds on (all in `research_outputs/`):**
- `2026-11-08_citation-verifier_full_audit.md`
- `2026-11-08_academic-editor_language_audit.md` (131 language items)
- `2026-11-08_taxonomy-theorist_full_audit.md`
- `2026-11-08_journal-scout_requirements_audit.md`
- The stats-consistency-checker's report is merged into §9 here (it was not allowed to write a file).

**Coverage gap:** five agents stopped early on the account's 5-hour usage limit (resets 06:00 Asia/Dhaka): literature-scout, methodology-auditor, the two corpus-claim agents and q1-reviewer. Their checks are covered here by my own pass, and every item I could not finish is marked **STILL OPEN** or **NOT AUDITED**. Nothing is reported as checked unless it was.

---

## 1. Verdict

**Today: desk-reject or reject at a Q1 journal. If the methods are rewritten truthfully and items C1–C10 are fixed, it is a credible major-revision candidate.**

1. **The Methods section describes a process the authors' own records contradict.** It says three authors searched each publisher database with two terms and screened independently to consensus. The authors' own files say otherwise:
   - `Paper Selection Process.docx` says Google Scholar was the main database and lists 7 queries.
   - `Paper Screening Process.docx` says two researchers screened and their results were "averaged out".
   - `paperlinks.xlsx` shows 52 of 130 records (40%) came from ChatGPT, Gemini or Google Scholar.

   That is a publication-ethics problem, not a style problem.
2. **The search is not reproducible and would fail PRISMA-S.** There is no Scopus or WoS search, no Boolean strings, and no per-source dates.
3. **The headline claim is misstated.** The abstract says "60–75% for the more human-involved modes", but Shared-Collaborative, also human-involved, is 0/3.
4. **The "inverse relationship" is not monotone.** The rates are 60, 75, 0 and 7.4%.
5. **No uncertainty or tests are reported anywhere,** even though the contrast is significant (p = 0.0056) when reported properly.
6. **The taxonomy has no theoretical grounding, no reported decision rules and no reliability statistic.**
7. **The closest comparator (Bakzadeh et al. [6]) is mischaracterized.**

The data analysis itself is arithmetically clean. Every table and percentage recomputes. That gives the authors something solid to rebuild on.

---

## 2. Research-integrity / methods-truthfulness issues (Section I): HIGHEST PRIORITY

Per CLAUDE.md rule 4, this section does **not** decide what happened. It shows the conflicting records and the questions only the authors can answer.

### Evidence table

| # | Manuscript says (line) | Authors' own record says | Source |
|---|---|---|---|
| I-1 | L349: "The search terms "rescue robot" and "disaster rescue robot" were applied across the sources listed in Table II" (MDPI with "disaster rescue robot", the rest with "rescue robot") | "The main database used to source the papers were **Google Scholar**." Seven queries: *rescue robot, teleoperation, search and rescue, disaster management, disaster search and rescue, search and rescue robot, disaster management robot*. | `Paper Selection Process.docx` |
| I-2 | L325: "Candidate records were identified from ten sources…", and Fig. 2 puts all 130 under "Databases" | "How it was found" column: **78/130 publisher-portal search; 34 ChatGPT; 15 Google Scholar; 3 Gemini** (52 = 40% non-database) | `paperlinks.xlsx` (recount below) |
| I-3 | L325: "This identification process, **conducted independently by the three authors**" | Per-record discovery tool logged; no per-author record. Sec. 2.2 (L61): records "originally located via Google Scholar and AI-assisted search prompts (ChatGPT, Gemini)" | master doc L61 |
| I-4 | L371: "Screening was performed independently by **the three authors**… The three independent sets of decisions were then compared record by record… consensus" | "**Two researchers** independently carried out the process, which then was **averaged out** for a neutral result." | `Paper Screening Process.docx` |
| I-5 | L371, L397: three-author independent screening and extraction | The revision log (L936) records an earlier Limitations section that listed "**single-annotator screening, no inter-rater reliability statistic**… partial AI-assisted record discovery". L998 records those two bullets being **deleted** because "both are now false under the new framing". | master doc L936, L998 |
| I-6 | Whole manuscript: no mention of AI or Google Scholar | L59: "do not mention AI tools, Google Scholar, or any single-annotator framing anywhere in manuscript prose". L986–L990: the user instructed the removal of "all mention of automatic/AI-assisted extraction or discovery", and the assistant flagged that "Tech Science Press (0/3) and Springer (0/14) have zero records found via a direct query". | master doc L59, L986–990 |
| I-7 | L397: "only findings on which all three agreed were retained… disagreements were resolved through joint discussion" | Self-contradictory: findings cannot be both unanimous-only and consensus-after-discussion. It also conflicts with I-4 ("averaged"). | L397 |
| I-8 | L309: "conducted between 18–19 July 2026" (the *whole* review); L371: 125 full texts "read in its entirety" by each of three authors in 2 days, in 12 batches | No docx records batches or dates. The source file `review_process_and_findings.md` cited at L928 is not in the project. | — |
| I-9 | L375: "Extraction was carried out independently by the three authors… cross-checked" | Sec. 1, 5 and 16 describe extraction done in "handoffs" by an AI assistant from a workbook, with PDFs supplied by the user in batches (L944–L950, L976). The precedents were "established and logged during extraction", which is a sequential, single-stream process. | master doc L5, L36, L976 |
| I-10 | No AI-use statement | The working document shows the **manuscript prose itself** was drafted by an AI assistant: L5 ("Paste this document into a new conversation… the assistant should pick up"), L128–L135 ("Done this handoff"), L940 ("Drafted the full Introduction"). IEEE requires AI-generated text to be disclosed in the Acknowledgments, naming the system and the sections ([IEEE Access submission guidelines](https://ieeeaccess.ieee.org/authors/submission-guidelines/); [IEEE Author Guidelines for AI-Generated Text](https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/)). | master doc + IEEE |
| I-11 | L365: query-level 2025+ restriction "already restricted every catalogued record" | ChatGPT and Gemini "queries" have no reproducible date filter. The xlsx gives no date filter per query. | `paperlinks.xlsx` |
| I-12 | Methods never mention journal quartile | Every record is tagged Q1/Q2 (66/64), and the PDF filenames are prefixed with the quartile. `Paper Selection Process.docx` says records were catalogued by "quartile". If quartile was used to select records, it is an **unreported eligibility criterion**. | `paperlinks.xlsx`, `assets/papers/` |
| I-13 | Results: 18 sim-only, 8 field, 10 partial, 3 bench | `Paper Project Type Analysis.docx`: "20 (51%) real-life… 19 (49%) simulation". This is a different, unreconciled classification of the same 39 papers. | docx |

### Per-publisher discovery method (recomputed from `paperlinks.xlsx`, DOI-prefix publisher)

| Publisher (DOI prefix) | Total | Publisher-portal query | ChatGPT | Gemini | Google Scholar |
|---|---|---|---|---|---|
| MDPI (10.3390) | 41 | 34 | 2 | 0 | 5 |
| Elsevier ScienceDirect (10.1016) | 31 | 18 | 10 | 0 | 3 |
| IEEE Xplore (10.1109) | 15 | 5 | 7 | 1 | 2 |
| Springer (10.1007) | 14 | **0** | 10 | 1 | 3 |
| Scientific Reports (10.1038) | 12 | 8 | 2 | 1 | 1 |
| PLOS One (10.1371) | 6 | 6 | 0 | 0 | 0 |
| Frontiers (10.3389) | 6 | 4 | 2 | 0 | 0 |
| Tech Science Press (10.32604) | 3 | 2* | 1 | 0 | 0 |
| Wiley (10.1002) | 1 | 1 | 0 | 0 | 0 |
| ASCEE (10.31763) | 1 | **0** | 0 | 0 | 1 |
| **Total** | **130** | **78 (60%)** | **34** | **3** | **15** |

\*Both Tech Science Press "portal" records are logged as "via elsevier search query", which is not a Tech Science Press interface. This is probably why the old PRISMA miscounted 33/1.

Query strings actually logged: "rescue robot" 52, "disaster rescue robot" 41, and no query string for 37 (the AI-assisted records).

### Risk

- **COPE "misrepresentation of methods".** A Methods section that describes a process the authors did not follow is grounds for retraction if discovered after publication. IEEE's author-ethics policy treats it as misconduct.
- **Discovery risk is high.** The search cannot be reproduced from the paper, so a reviewer who reruns "rescue robot" on Springer Link will not recover these 14 records.
- **AI non-disclosure** breaches IEEE policy on its own, separately from the methods issue.
- **The fix costs little scientifically.** Honest reporting plus a supplementary database search (`/search-update`) strengthens the paper.

### Questions the authors must answer before any rewrite

1. Who searched? Was it one author or three? Was Google Scholar the primary tool (as the docx says) or were the publisher portals primary?
2. Which queries were actually run: the 2 in the manuscript or the 7 in `Paper Selection Process.docx`? On which dates, with which year filters?
3. For the 37 ChatGPT/Gemini records: what prompts were used, and was each record then retrieved and checked at the publisher?
4. How many people screened: one, two or three? What does "averaged out" mean for include/exclude decisions? Is there any per-screener decision file, so that κ can be computed?
5. Was screening really done on 18–19 July 2026, in 12 batches? Where is `review_process_and_findings.md`?
6. Was journal quartile (Q1/Q2) used to admit records?
7. Was extraction done by humans, an AI assistant, or both? Who checked the AI output?
8. Which manuscript sections were drafted by an AI system, and which system was used?

### Truthful replacement wording (draft, for the authors to adapt once Q1–Q8 are answered)

> **B. Information Sources and Search Strategy.** Records were identified between [dates] through (i) the native search interfaces of MDPI, ScienceDirect, IEEE Xplore, Nature Portfolio (*Scientific Reports*), PLOS, Frontiers and Wiley using the terms "rescue robot" and "disaster rescue robot" (n = 78); (ii) Google Scholar using [list queries] (n = 15); and (iii) AI-assisted discovery, in which candidate papers suggested by ChatGPT ([version]) and Gemini ([version]) in response to [prompt description] were each retrieved and verified at the publisher's site before cataloguing (n = 37). All searches were limited to publications dated 2025 or later. Because AI-assisted discovery is not reproducible, we report it separately in the PRISMA diagram as "identification via other methods" and treat it as a limitation (Section V-D). [Optional, strongest fix: a reproducible supplementary search of Scopus and Web of Science on [date], string in Appendix A, retrieved N additional records.]
>
> **F. Screening.** Full texts were screened by [one author / two authors] ([initials]); [a second author] independently re-screened [all / a random X%] of records, giving Cohen's κ = [value] … Disagreements were resolved by discussion with the third author.
>
> **Acknowledgments (AI-use disclosure).** ChatGPT ([version], OpenAI) and Gemini ([version], Google) were used to suggest candidate records during identification (Section II-B). [An AI assistant ([system]) was used to draft and edit the text of Sections [list]; all content was checked by the authors, who take full responsibility.]
>
> **V-D Limitations (restore).** Partial reliance on non-reproducible discovery (Google Scholar, AI-assisted); [single-annotator / two-annotator] screening without [full] reliability statistics; …

---

## 3. Critical problems (rejection-level or factual errors)

`[ID] [Severity] [Line / Section] "quote" → Problem → Evidence → Fix`

- **[C1] [Critical] [L349, L325, L371, L375, L397 / II-B, C, F, G, H]** "applied across the sources listed in Table II" / "conducted independently by the three authors" / "only findings on which all three agreed were retained"
  - Problem: the Methods contradict the authors' own records (see §2).
  - Evidence: `Paper Selection Process.docx`, `Paper Screening Process.docx`, `paperlinks.xlsx`, L59, L61, L936, L998.
  - Fix: rewrite truthfully after the authors answer Q1–Q8, and restore the deleted Limitations.
- **[C2] [Critical] [L696, L730]** "compared with 60–75% for the more human-involved modes"
  - Problem: Shared-Collaborative is a human-involved mode with 0/3 field-tested, so the pooled human-involved rate is 6/12 = 50%. As worded, the abstract's headline is false.
  - Evidence: Table XI (L529) and Fig. 6.
  - Fix: "versus 6 of 9 (66.7%) for Teleoperation and Supervisory Control combined (50% for all human-involved modes)".
- **[C3] [Critical] [L521, L605, L690, L696, L740; Fig. 6 caption L533]** "The more autonomous a reported system in this corpus, the less likely it is to have been tested outside simulation"; "inverse relationship… across the full four-way autonomy spectrum"
  - Problem: the rates along the paper's own Fig. 7 ordering are 60 → 75 → 0 → 7.4%, which is not monotone. Theory also places Shared-Collaborative *below* Supervisory, so the ordering itself is contestable.
  - Evidence: `fig_autonomy_validation.png`, `fig_taxonomy.png`, Beer et al. 2014 (doi:10.5898/JHRI.3.2.Beer).
  - Fix: claim a binary contrast (FA vs human-in-mission), not a gradient.
- **[C4] [Critical] [Whole Results / Abstract]** No confidence interval, test or effect size appears anywhere (grep confirms).
  - Problem: claims rest on cells of n = 3–5 (Teleoperation 3/5, 95% CI 23–88%).
  - Evidence: recomputed in §9 (FA 2/27 vs human-involved 6/12, Fisher p = 0.0056, OR 0.08 [0.01–0.50]; FA vs Tele+Sup p = 0.0010; Freeman-Halton 4×2 p = 0.0017).
  - Fix: add Wilson CIs and Fisher tests, labelled exploratory/post hoc.
- **[C5] [Critical] [L676, Table I L686]** "Bakzadeh et al. [6]… explicitly exclude autonomy and control software from their stated scope"; Table I: "Autonomy and control software explicitly excluded from scope"
  - Problem: [6] classifies every platform on a Sheridan–Verplank-based autonomy axis (A1 levels 1–4, A2 5–7, A3 8–10; mostly teleoperated). The manuscript itself relies on [6] at L555 for "predominantly teleoperation-oriented", which contradicts L676 internally.
  - Evidence: Frontiers full text (verified by the taxonomy-theorist agent and the earlier scan, Sec. 5.1.4 of [6]): <https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1857704/full>.
  - Fix: use the rewrite in the scan §2.
- **[C6] [Critical] [L730, L696, L690, L605]** "which has not been reported previously in this literature"; "not previously reported"; "none of the reviewed prior works evaluate…"; "would not surface"
  - Problem: the novelty claim rests on one 6-search baseline scan. The full literature scan did not complete (rate limit), and CLAUDE.md rule 2 requires a dated, adequate scan.
  - Evidence: the earlier scan's §1 rated C4 "THREATENED".
  - Fix: hedge to "to our knowledge, not quantified in prior SAR robotics reviews" until a complete scan exists.
- **[C7] [Critical] [Whole / Data availability]** The Results claim to be computed from `SAR_review_data_extraction_table.xlsx` (L17, L415), but **that file is not in the project.**
  - Problem: no per-paper data exist locally to reproduce Tables V–XII, the clusters or the 35/39 realism coding. `review_process_and_findings.md` (exclusion log, batches) is also missing.
  - Evidence: `find` over the project.
  - Fix: recover both files and publish the extraction table as supplementary data.
- **[C8] [Critical] [L587]** "[21] uses a mixed-reality swarm interface in a **simulated maritime** risk-conflict scenario"
  - Problem: this is a factual error. The scenario is mountain wilderness, and it contradicts the logged reclassification (L224, L978) and Table XII.
  - Evidence: `Q1 126 …pdf`, extracted line 169: "set in a mountainous wilderness area where a flash flood trapped climbers in a valley".
  - Fix: "a simulated mountain-wilderness flash-flood scenario".
- **[C9] [Critical] [L631–L633, L697, L730, L740]** "89.7% of the entire corpus (35 of 39)… self-reports some form of environmental-realism gap"
  - Problem: this result first appears in the Discussion. "Environmental-realism limitation" is not an extraction field in Table III, there is no coding rule, and no Results table supports it. It is nonetheless a headline abstract number (CLAUDE.md rule 6).
  - Fix: define the coding rule in II-G, add a Results table (per paper), and report the CI (76.4–95.9%).
- **[C10] [Critical] [L641–L644 / V-D]** The Limitations section has two bullets only (no quality scoring; narrow window).
  - Problem: it omits search restrictions (2 terms, no Scopus/WoS), non-reproducible AI/Scholar discovery, screener count and the lack of κ, classification subjectivity, tiny cells, English-only (if applicable), publication bias, and the single 2-day screen. Two truthful bullets were deleted (L998).
  - Fix: write a full validity-threats section (construct, internal, external, conclusion).

## 4. Major problems

- **[M1] [Major] [L349 / II-C]** "search terms "rescue robot" and "disaster rescue robot""
  - Problem: there is no Boolean string, no fields (title/abstract/keywords), no per-source dates, no Scopus/WoS/ACM, and no citation chasing. PRISMA-S items 1–3, 8, 9 and 13 are missing. The terms also miss UAV, drone, "search and rescue", USAR, teleoperation, autonomy and so on. With "rescue robot" only, records titled "UAV … search and rescue" are found only by chance.
  - Fix: `/search-update` with a documented Scopus/WoS supplementary search.
- **[M2] [Major] [L395, Fig. 2]** All 130 records sit under "Identification via databases and registers".
  - Problem: Google Scholar and ChatGPT/Gemini records belong in PRISMA 2020's "Identification via other methods" column.
  - Evidence: `prisma_diagram.png`, xlsx counts.
  - Fix: redraw the diagram with two columns (78 / 52, or as the authors confirm).
- **[M3] [Major] [L375, L605 / II-G]** "resolved against seven explicit classification precedents"
  - Problem: the precedents (Sec. 6A) and even the four mode definitions never appear in the manuscript, so the "explicit, precedent-based protocol" claimed at L375, L605, L690, L694 and L730 cannot be checked. The revision log (L964) shows the pointers were removed deliberately.
  - Fix: add the definitions and decision rules to II-G and put the precedents and per-paper table in a supplement.
- **[M4] [Major] [Taxonomy grounding]**
  - Problem: no citation of Sheridan & Verplank 1978, Parasuraman et al. 2000 (doi:10.1109/3468.844354), Beer et al. 2014 (doi:10.5898/JHRI.3.2.Beer), Endsley & Kaber 1999, ALFUS, Fong et al. 2003 or Murphy 2004.
  - Evidence: `2026-11-08_taxonomy-theorist_full_audit.md` M1.
  - Fix: add a theory subsection with a mapping table.
- **[M5] [Major] [Fig. 7 / L575]** "their position along the underlying autonomy spectrum"
  - Problem: Fig. 7 places Shared-Collaborative to the right of (more autonomous than) Supervisory. This is contrary to Sheridan–Verplank and Beer et al., and two of the three Shared cases have a human flying the UAV ([19], [20]).
  - Fix: reorder, or drop the ordinal arrow.
- **[M6] [Major] [Construct validity, FA label]**
  - Problem: 16/27 FA papers are simulation-only with no operator modelled, so "no human in the loop" is partly a property of the test setup. That partly builds in the 7.4% finding. Precedent B (code the design) and Precedent E (code what was tested) conflict.
  - Evidence: Sec. 6A L156, L166; taxonomy audit M5.
  - Fix: adopt one rule, add a "human role modelled" flag, and run a sensitivity analysis.
- **[M7] [Major] [Inter-rater reliability]**
  - Problem: no κ for screening or for the autonomy labels. PRISMA 2020 items 8 and 9 are partial at best.
  - Fix: blind re-code of all 39 (or a stratified 30%) and report Fleiss' κ / AC1, honestly framed as post hoc.
- **[M8] [Major] [Quality / risk of bias]**
  - Problem: there is no appraisal instrument (L643 admits this). Q1 reviews expect one (PRISMA item 11, AMSTAR-2).
  - Fix: apply a simple validation-depth/reproducibility score (e.g. adapt [4]'s 1–6 score).
- **[M9] [Major] [Protocol / registration]**
  - Problem: no protocol and no registration (PRISMA 24a–c), and no data/code availability (item 27).
  - Fix: state "not registered", and deposit the extraction table and the screening log (e.g. OSF/Zenodo).
- **[M10] [Major] [L595 vs L601]**
  - L595: "Real-world validation is markedly thinner in this cluster than the corpus average"
  - L601: "the cluster with the most real-world testing (single-robot navigation) is still majority-simulation"
  - Problem: the two sentences contradict each other. Moreover, the perception cluster has [42] (real forest) and [43] (physical pool). There is no cluster × validation table.
  - Fix: add the table and correct L601.
- **[M11] [Major] [L593]** "the paper's own results note success rates degrade sharply as swarm size grows beyond that one validated unit, and its real-world LiDAR pipeline produced enough false positives from grass and wind"
  - Problem: the degradation is simulation-only (4→24 agents), not beyond the physical unit. Wind caused **false negatives**, not false positives; L623 is closer.
  - Evidence: `Q1 30 …pdf`: "long grass… false positives as well as slight movements in the obstacles from the wind causing false negatives".
  - Fix: reword to match the PDF.
- **[M12] [Major] [L599]** "a figure the authors themselves describe as inadequate for safety-critical deployment"
  - Problem: this overstates the source. The PDF says "the overall success rate remains **modest** for safety-critical applications" (L625 quotes it correctly).
  - Fix: use "modest".
- **[M13] [Major] [L587]** "detection recall for occluded or partially buried victims as low as 2.6–26.4% mAP"
  - Problem: recall and mAP are conflated. The source gives per-class mAP@0.5 of 0.026–0.264; overall recall is 40.25% and aggregate mAP@0.5 is 0.613.
  - Evidence: `Q1 113 …pdf`, §4.4.
  - Fix: "per-class mAP@0.5 of 0.026–0.264 for the hardest occlusion classes".
- **[M14] [Major] [L587]** "each treats the operator's own cognitive or psychological state as a first-class design and evaluation target… not found in the Supervisory bucket"
  - Problem: [20] is a filtering/decision-support architecture, not an operator-state study, and [17] (Supervisory) does measure workload and trust.
  - Fix: drop the generalization.
- **[M15] [Major] [L537, L637, L697, L730, L740]** "UAV papers show the weakest real-world validation rate of any platform category"; "the platform most associated with Fully Autonomous… research"
  - Problems:
    - There is no Platform × Validation table in the manuscript.
    - Abstract/Unspecified (3, all simulation by definition) is likely 0/3, below UAV.
    - UAV ties UGV for FA (9 each).
    - UAV vs the rest gives p = 0.23. UAV vs Hybrid gives p = 0.031, but that comparison is post hoc (2 of 15 possible pairs) and confounded with mode, since Hybrid holds all 3 Teleoperation papers.
  - Fix: add the table and present the contrast as descriptive only.
- **[M16] [Major] [L537]** "the opposite of what their smaller sample size alone would suggest"
  - Problem: sample size predicts imprecision, not direction, so the phrase is meaningless.
  - Fix: delete it.
- **[M17] [Major] [L436, L742, L644]** "a departure from the predominantly human-supervised framings surveyed by the model reference paper"; "the current literature's apparent shift toward full autonomy"
  - Problem: these are trend claims with no longitudinal data. [4] reports no mode distribution (as the manuscript itself says at L676), so there is no baseline to "depart" from.
  - Fix: remove or reframe the trend language.
- **[M18] [Major] [L625, L651]** "The gap between 'Fully Autonomous' succeeding and failing in this corpus concentrates specifically in control and decision execution, not in perception."
  - Problem: this generalizes from one paper ([47]) to the corpus.
  - Fix: limit it to [47].
- **[M19] [Major] [L654]** "the consistent degradation pattern with increasing agent count documented in both Section IV-D… and [25]"
  - Problem: IV-D documents only [25], so the "consistent pattern" is circular and rests on a single source.
  - Fix: cite the evidence or soften to "in [25]".
- **[M20] [Major] [L672]** "Estimates… by roughly the 72-hour mark range from just over 20% in some assessments to more than 90% in others"; "Virtually all sources agree"
  - Problem: no citation is given for the range. The only cited source, [2], actually says ~90% survival **within 24 h** falling to 5–10% after 72 h, so ">90% at 72 h" looks like a misreading. "Well established… [2]" rests on an arXiv preprint whose content does not support the sentence.
  - Evidence: citation-verifier audit, [2].
  - Fix: cite peer-reviewed SAR-medicine sources (e.g. on earthquake rescue survival curves) and correct the numbers.
- **[M21] [Major] [L672, ref [3]]** The survival figures rest on an NBC News quote.
  - Problem: it is a weak source for a quantitative claim, and the entry has no URL or date.
  - Fix: replace it with peer-reviewed data, or keep it only as colour, with a full citation.
- **[M22] [Major] [Table I, L686]** "15 platforms"
  - Problem: the sources conflict. The earlier scan read 14 platforms (12/1/1, KQR48 excluded), while the taxonomy-theorist agent read "all 15".
  - Status: **STILL OPEN.** Re-read [6] Sec. 5.1.4 and its platform table.
- **[M23] [Major] [Table I, L680–L688]**
  - Problem: Table I omits recent competitors (Shuvo et al. 2026, the *Applied Soft Computing* 2026 SAR path-planning SLR, the arXiv:2412.20699 air–ground survey) and Tong [8]. A reviewer will find them.
  - Status: verification **STILL OPEN** (§6).
- **[M24] [Major] [L676]** "it falls outside both this review's 2025–2026 window and the 2016–2024 corpus in [4]"
  - Problem: Tong et al. is dated 2024, which is *inside* 2016–2024. The intended point is that Kareem reviewed primary studies, not reviews.
  - Fix: reword.
- **[M25] [Major] [L605]** "under a logged, precedent-based protocol (Section II-F)"
  - Problem: the protocol is described in II-G.
  - Fix: change "II-F" to "II-G".
- **[M26] [Major] [Abstract L730]**
  - Problems:
    - 275 words; the target is ≤250.
    - It omits the PRISMA-abstract items (sources, search dates, eligibility, synthesis methods, limitations, funding, registration).
    - It contains the unhedged novelty claim.
    - It says "screened under PRISMA 2020 guidelines", but PRISMA is a reporting guideline, not a screening method.
  - Fix: rewrite (the academic-editor report §9 has a 238-word draft, which still needs the C2 fix).
- **[M27] [Major] [Title L720]** "A Systematic Review of Teleoperation, Human-Robot Collaboration, and Autonomous Approaches"
  - Problem: the title omits Supervisory Control, one of the four modes.
  - Fix: align the title with the taxonomy.
- **[M28] [Major] [Front/back matter]**
  - Problem: the `.md` is missing:
    - corresponding author, emails and ORCIDs;
    - author biographies (required by IEEE Access);
    - funding statement;
    - conflict of interest;
    - data availability;
    - author contributions (CRediT);
    - AI-use disclosure (Acknowledgments);
    - PRISMA 2020 checklist supplement;
    - registration statement;
    - the IEEE-style organization paragraph (L699 is an internal note in its place).
  - Evidence: [IEEE Access guidelines](https://ieeeaccess.ieee.org/authors/submission-guidelines/).
- **[M29] [Major] [Venue]**
  - Problem: the IEEE Access quartile is **UNVERIFIED**, possibly Q2 by JCR (journal-scout, aggregator). The project goal is Q1.
  - Fix: verify in JCR/SJR by category before targeting.
- **[M30] [Major] [Discussion V-A–C]**
  - Problem: the Discussion gives no mechanism analysis ("why") beyond V-C, and there is no comparison with external evidence on sim-to-real gaps in robotics.
  - Fix: add literature-grounded interpretation.

## 5. Minor problems

- **[m1] [L436, L571/573, L605, L617, L641] Leaked working language.**
  - Quotes: "model reference paper"; "verified prior reviews" (L605 ×2); "this section originally set out to test" (L633); L699, which is an italic internal note inside Section I.
  - Fix: delete or neutralize.
- **[m2] [Bibliography L814, L826, L852, L856, L862, L874, L904] Italic working notes inside reference entries** ("This review's own excluded paper #4… Section II.D", "Costa-Pérez also co-authors ID 87", "Same author team as ID 14", page-correction notes, naming notes).
  - Fix: strip all of them. The [9] note also cites the wrong section (II.D → II-E).
- **[m3] [All refs] Format.** The references are APA-style; IEEE requires initials-first, abbreviated venue, vol./no./pp. or Art. no., and month.
  - Missing data: [9] DOI (10.1016/j.rcns.2026.01.001); pages for [18] (40–58), [22] (421–441), [44] (vol. 43, no. 5, pp. 3264–3275), [46] (Art. no. 100330) and [47] (50575–50583), all per Crossref via citation-verifier.
- **[m4] [Refs] Name forms.**
  - [26]: the family name is "ur Rehman".
  - [13]: Crossref gives "V, Berlin Hency".
  - [45]: the PDF prints "Gowry Sailaja V".
  - Years to check: [39] (online 24 Dec 2025) and [29] (online 22 Dec 2025, vol. 2026).
- **[m5] [L676]** "Sinha et al. [5] reviewed 190 papers": the source abstract says "over 190".
- **[m6] [L670]** The Afghanistan earthquake sentence ("killing an estimated 2,200 people") has no citation; [1] supports it, so add [1].
- **[m7] [L674]** "an increasingly active area… with a correspondingly growing body of systematic reviews" has no citation.
- **[m8] [Fig. 5]** Fig. 5 is never cited in the text (only in its own embed and caption). Cite it at L506.
- **[m9] [L353]** "byte-level full-text comparison applied as a secondary confirmation in two cases": 4 of the 5 duplicate pairs are byte-identical (MD5) per the stats agent, and 04/12 has identical text but different bytes. Correct the count.
- **[m10] [L593]** "(12 papers: [22]…[33])": [27] is listed but never described.
- **[m11] [L579]** "in every one of the five papers, locomotion remains entirely human-driven": [10] has an autonomous person-follower sub-mode (Precedent A note, L153). Qualify the sentence.
- **[m12] [L579]** "([14], [11], [12])": citations out of numeric order.
- **[m13] [L377]** "eleven sensor categories": one of the eleven is "None". Say "ten modalities plus a 'none' flag".
- **[m14] [Table IV, L403]** The table gives no pair breakdown. From the screening list: C1+C2 = 6, C2+C3 = 5, C1+C3 = 1, all two-criterion (`Paper Selection List.docx`). Add it as a footnote.
- **[m15] [L541, Table XII]** "one other single-occurrence hazard": name it (volcanic eruption, [39]).
- **[m16] [L537]** "addressed in the Discussion alongside the platform's 17.9% overall corpus share": V-C never mentions 17.9%.
- **[m17] [Acronyms]**
  - SAR and HRI are each defined three times; SLR and RSAR are defined but barely used.
  - About 25 terms are undefined: UAV, UGV, UUV, USV, PRISMA, LiDAR, IMU, GPS, LLM, MLLM, SLAM, DRL, MPC, AMCL, mAP, NBV, MR and others.
- **[m18] [Spelling] [L325, L343, L395…]** "catalogued" ×6 should be "cataloged" (IEEE American spelling). Date formats are also mixed ("18–19 July 2026" vs "March 28, 2025").
- **[m19] [Terminology]**
  - "shared-autonomy" (L361) vs "Shared-Collaborative"; "drone" (L579, L625) vs "UAV"; "Hybrid/Multi-Platform" vs "hybrid multi-platform" (L730, L740).
  - "(the 2023 Turkey–Syria earthquakes)" (L672) needs a comma construction.
- **[m20] [L621]** "is not an artifact of a few weak papers pulling down an average": this is a count, not an average. Reword.
- **[m21] [L697, L730] Overconfident wording.** "near-universal (89.7%)" (CI 76–96%); "The results demonstrate" (L740). Hedge both.
- **[m22] [L309]** "The review… was conducted between 18–19 July 2026": that is the screening dates, not the whole review. Clarify.
- **[m23] [Fig. 6, Fig. 7]** The subtitles duplicate the captions, there are no error bars or n labels on Fig. 6, and the Fig. 7 subtitle uses an em dash. Greyscale is legible because of the direct labels; the Fig. 7 Supervisory and Shared blues are close in luminance.
- **[m24] [L583]** "(Its headlined validation used autonomous waypoint navigation… does not change this primary classification.)": internal classification reasoning has leaked into the prose.
- **[m25] Repetition.** The claim that "a review organized by any other axis would not surface this" appears five times (L605, L690, L730, L742, plus L627). Keep it once and hedge it.
- **[m26]** Full list of 131 language items: `2026-11-08_academic-editor_language_audit.md`.

## 6. Missing literature

| Work | Status this session | Action |
|---|---|---|
| Shuvo et al. 2026, *Front. Robot. AI*, doi:10.3389/frobt.2026.1832982 (per the earlier scan) | **STILL OPEN.** The earlier scan fetched it. My 2026-11-08 web search did **not** return it, and literature-scout stopped before verifying. | Open the DOI before citing. If it exists, add it to Table I (axis: learning paradigm; covers 2005–2025, which overlaps 2025). |
| "Path planning for search and rescue robots: a systematic and bibliometric review", *Applied Soft Computing* 2026 (ScienceDirect PII S1568494626018284 per the earlier scan) | **STILL OPEN.** My search did not find it; authors and DOI are unverified. | Verify on ScienceDirect, then add it to Table I. |
| arXiv:2412.20699 (air–ground fire & rescue survey) | **STILL OPEN** (peer-reviewed version not checked) | Check for a journal version before citing. |
| "Autonomous Aerial Robots for Enhanced SAR Operations" (Jan 2026) | **STILL OPEN** (venue unknown) | Cite only if peer-reviewed. |
| ESARBench, arXiv 2605.01371 | **STILL OPEN** | Optional, for Future Directions 1–2. |
| Hagenow et al. 2026 (shared control review); Frontiers 2025 variable-autonomy mini-review, doi:10.3389/frobt.2025.1540476 | **STILL OPEN** | Theory support for Shared-Collaborative. |
| LOA theory, **verified by the taxonomy-theorist agent**: Sheridan & Verplank 1978 (NTIS ADA057655); Parasuraman, Sheridan & Wickens 2000, doi:10.1109/3468.844354; Beer, Fisk & Rogers 2014, doi:10.5898/JHRI.3.2.Beer; Endsley & Kaber 1999, doi:10.1080/001401399185595; NIST ALFUS SP 1011-I-2.0, doi:10.6028/NIST.SP.1011-I-2.0; Murphy 2004, doi:10.1109/TSMCC.2004.826267 | VERIFIED (DOIs) | Add a theory subsection (M4). |
| Peer-reviewed survival-window source to replace [2]/[3] | Not yet identified | Needed for M20. |

Searches made this session (my own): (1) the *Applied Soft Computing* SAR path-planning SLR, no hit; (2) the Shuvo 2026 title, no hit; (3) the IEEE Access AI-disclosure policy, verified. Literature-scout's ≥15-query run did not complete, so **re-run `/novelty-gap-search` after the limit resets.** The earlier scan's §1 verdicts (C1 hedge, C2 stands, C3 stands, C4 threatened) remain **STILL OPEN** until then.

## 7. Reference audit table (48)

The source is the citation-verifier (Crossref DOI check for every entry); details and IEEE-format rewrites are in `2026-11-08_citation-verifier_full_audit.md`. "Format" problems (APA style) apply to **all 48** and are not repeated per row.

| [N] | Short cite | Status | Issue |
|---|---|---|---|
| 1 | CRED 2025 Disasters in Numbers | OK | Statistics match the report. The Myanmar US$11 B figure is unchecked. Add [1] to the Afghanistan sentence. |
| 2 | Tabib et al. arXiv:2410.08507 | **Mismatch (claim)** | The paper exists but does not support the "golden window… well established" sentence. It is a preprint (accepted at ISER 2025). |
| 3 | Godby / NBC News 2023 | Weak source | The quote exists. The entry has no URL or date and contains an internal note. |
| 4 | Kareem et al. 2026 IEEE Access | Metadata OK; claims **UNVERIFIED** this pass | Paywalled. The "no FA category" and "no mode distribution" claims rest on an earlier user-supplied PDF (Sec. 8A). |
| 5 | Sinha et al. 2026 Sensors | Minor mismatch | "over 190" vs "190". The organizing axis is UNVERIFIED. |
| 6 | Bakzadeh et al. 2026 Front. Robot. AI | **Mismatch (claim)** | Autonomy is coded (C5). The platform count, 14 vs 15, is STILL OPEN. |
| 7 | Bakzadeh et al. 2025 Robotics | OK | — |
| 8 | Tong et al. 2024 IEEE IV | Metadata OK; claim UNVERIFIED | The "outside 2016–2024" logic is wrong (M24). |
| 9 | Rajashekhar & Prabhakar 2026 | Incomplete | DOI missing (10.1016/j.rcns.2026.01.001), the issue (1) is missing, and the internal note cites the wrong section. |
| 10 | Cafolla et al. 2026 RAS | OK | — |
| 11 | Jia et al. 2025 Appl. Sci. | OK | — |
| 12 | Liu et al. 2026 MMT | OK | 1,200 kg payload verified in the PDF. |
| 13 | Raghavan et al. 2026 Results Eng. | Name form | "V, Berlin Hency". 93.1% mAP verified. |
| 14 | Khattab et al. 2025 Sci. Rep. | OK | — |
| 15 | You S. et al. 2026 Sensors | OK | — |
| 16 | Ahmad & Humbert 2025 Robotics | OK | — |
| 17 | Ruan et al. 2025 Front. Robot. AI | OK | — |
| 18 | Schomer & Adams 2026 IEEE T-FR | Incomplete | pp. 40–58 missing. |
| 19 | Bhattacharya & Butail 2025 CAIS | OK | — |
| 20 | Gaitan et al. 2025 AI | OK | Quote verified. See M13 for recall vs mAP. |
| 21 | You F. et al. 2026 IJHCS | OK (metadata) | The in-text scenario is wrong (C8). |
| 22 | Maresca et al. 2026 IEEE OJ-COMS | Incomplete | pp. 421–441 missing; internal note in the entry. |
| 23 | Tan & Zhao 2026 CAIS | OK | — |
| 24 | Xue et al. 2026 Results Eng. | OK | Internal note in the entry. |
| 25 | Mead et al. 2026 EAAI | OK | All numbers verified. Text errors in M11. |
| 26 | ur Rehman et al. 2026 Sci. Rep. | Name form | The surname is "ur Rehman". |
| 27 | Kareem et al. 2026 Sci. Rep. | OK | Internal note in the entry. Never described in the text (m10). |
| 28 | Gao et al. 2026 Discover Computing | OK | — |
| 29 | Bedi et al. 2025 Information | Year check | Online Dec 2025, vol. 17 (2026). |
| 30 | Tao et al. 2025 Sensors | OK | — |
| 31 | Wang & Benhabib 2025 Robotics | OK | — |
| 32 | Romero et al. 2026 Comput. Commun. | OK | — |
| 33 | Li et al. 2026 IEEE TNSE | OK | Internal note in the entry. Page 2981 (docx says 2986). |
| 34 | Rado et al. 2025 Sci. Rep. | OK | — |
| 35 | Xue et al. 2025 Sci. Rep. | OK | — |
| 36 | Allan & Barczyk 2025 Drones | OK | — |
| 37 | Chen et al. 2026 IEEE Sens. J. | OK | — |
| 38 | Almalkawi et al. 2026 Sensors | OK | — |
| 39 | Yeoh et al. 2026 IJRCS | Year check | Online 24 Dec 2025. |
| 40 | Kozhubaev et al. 2025 Symmetry | OK | — |
| 41 | Kareem et al. 2026 JESTCH | OK | — |
| 42 | Strand et al. 2026 IEEE JSTARS | OK | "5 of 7" verified. Real flight was human-piloted and scored offline, so L597 should say so. |
| 43 | Srijiranon et al. 2025 ASI | OK | 9 pool trials verified. |
| 44 | He et al. 2026 J. Field Robot. | Incomplete | vol. 43, no. 5, pp. 3264–3275 missing. |
| 45 | Gowry Sailaja V et al. 2026 IEEE TMC | Name form | — |
| 46 | Cruz Ulloa et al. 2026 BIROB | Incomplete | Art. no. 100330 missing. |
| 47 | Cho et al. 2026 IEEE Access | Incomplete | pp. 50575–50583 missing. 40% / 86% / quotes verified. Wording issue in M12. |
| 48 | Vani et al. 2026 Discover Appl. Sci. | OK | Internal note in the entry. |

Order of first appearance (I → II → III → IV → V) is [1]…[48] sequential: verified by script. Every reference is cited, and no citation falls outside 1–48.

## 8. Corpus-claim audit table (39 papers)

**Partial.** The two corpus-claim agents stopped on the rate limit before finishing. The rows below were verified against the PDFs this session (by me, the stats agent or the citation agent). The rest are **NOT AUDITED**, to resume after 06:00 Asia/Dhaka.

| [N] | Record | Manuscript claim (line) | PDF says | Status |
|---|---|---|---|---|
| 10 | 6 | Voice-controlled add-on, drone + quadruped (L579) | Voice control confirmed | OK (sub-mode caveat, m11) |
| 12 | 116 | 1,200 kg payload; hierarchical attitude control (L579) | "payload capacity of 1200 kg"; AMPC attitude control | OK |
| 13 | 5 | YOLOv8, 93.1% mAP (L579) | 93.1% mAP | OK |
| 20 | 113 | Lab-only validation quote (L625) | "controlled laboratory environment. The system has not yet been tested in real disaster scenarios…" | OK |
| 20 | 113 | "detection recall… 2.6–26.4% mAP" (L587) | Per-class mAP@0.5 0.026–0.264; overall recall 40.25% | **WRONG (terminology)** |
| 21 | 126 | "simulated maritime risk-conflict scenario" (L587) | Mountainous wilderness flash flood (p. ~4) | **WRONG** |
| 21 | 126 | N = 35 → 27 after physiological loss (L587) | 35 participants; 27 valid physiological samples | OK |
| 25 | 30 | 95.83 / 84.50 / 81.11 / 69.36%; 77.92 vs 99.67%; 3/10 collisions (L623) | All present (Table 9: 7/10 collision-free) | OK |
| 25 | 30 | Degradation "beyond that one validated unit"; "false positives from grass and wind" (L593) | Degradation is in simulation; wind caused false negatives | **WRONG** |
| 42 | 17 | "recovered 5 of 7… in real forest trials" (L597) | "five of the seven"; real flight human-piloted and scored offline (Precedent B) | OK number / **incomplete context** |
| 43 | 66 | Calm indoor pool, n = 9 trials (L597) | "controlled water pool… all nine trials"; "no measurable current… indoor pool" | OK |
| 47 | 53 | 40% path success; 86% mAP (L599, L625) | "doubled… from 20% to 40%"; "up to 86% mAP" | OK |
| 47 | 53 | "supervising high-level goals, validating critical decisions, and intervening when necessary" (L599) | Verbatim present | OK |
| 47 | 53 | "describe as inadequate for safety-critical deployment" (L599) | "remains modest for safety-critical applications" | **OVERSTATED** |
| 47 | 53 | "modest for safety-critical applications" (L625) | Verbatim | OK |
| All others | — | Platform, mode, validation, scenario and sensor labels | — | **NOT AUDITED** (agents rate-limited) |

Labels cannot be audited against the extraction sheet because `SAR_review_data_extraction_table.xlsx` is missing (C7). The ≥15 excluded-record spot-check (methodology-auditor) was also **NOT COMPLETED**. From the screening list's reasons, the borderline exclusions most likely to draw reviewer challenge are these, which should be resampled first:
- #28, #42, #64 and #98 (flagged "Borderline call" in the docx);
- #70 and #83 (genuine sustained rescue framing, excluded under C2);
- #117 (firefighting-robot autonomous navigation, excluded under C1).

## 9. Number consistency table

Merged from the stats-consistency-checker. All counts were recomputed from n/N.

| Number | Locations | Recomputed | Status |
|---|---|---|---|
| 130 / 5 / 125 / 39 / 86 | L325, L353, L395, L730, Fig. 2, Sec. 2.3 | 130−5 = 125; 125−86 = 39 | OK |
| Source split 41/31/15/14/12/6/6/3/1/1 | Table II, Fig. 1, Fig. 2 | Sum 130; xlsx DOI prefixes agree | OK (no 33/1 leak) |
| C1 63 / C2 28 / C3 7; 12 multi | Table IV, L395, Fig. 2 | 98 − 12 = 86; pairs C1C2 6, C2C3 5, C1C3 1 (from docx) | OK; pair breakdown missing (m14) |
| 5 duplicate pairs | L353 | 04/12, 61/86, 99/102, 105/108, 110/130 all present; 4 byte-identical | OK; "two cases" wrong (m9) |
| FA 27 (69.2%), Tele 5 (12.8%), Sup 4 (10.3%), Shared 3 (7.7%) | Table V, L425, L591, L696, L730, L740, Fig. 7 | OK | OK. FA 95% CI 53.6–81.4 |
| Platforms 13/13/7/3/2/1 | Table VI, L440, L740, Fig. 3 | OK | OK |
| Table VII crosstab | L459–L467, L457, L637 | All rows and columns sum | OK |
| Sensors 20/13/12/10/10/7/5/3/3/2/1 | Table VIII, L471, Fig. 4 | OK | OK |
| Architecture 15/13/10/1 | Table IX, L493 | OK | OK |
| Validation 18/10/8/3 | Table X, L506, Fig. 5 | OK | OK. **Conflicts with docx 20/19** (I-13). Also sim-only 18 > PC/Offline 15, despite the Sec. 6D rule placing sim-only papers in PC/Offline; needs a check against the xlsx. |
| FA field 2/27 = 7.4% | L521, L621, L650, L696, L730, L740, Fig. 6 | 7.4% [2.1–23.4] | OK value; no CI |
| "60–75%" | L621, L696, L730, L740 | Tele 3/5 = 60 [23–88]; Sup 3/4 = 75 [30–95]; Shared 0/3 = 0 [0–56] | **Misleading at L696 and L730 (C2)** |
| FA vs human-involved | — | 2/27 vs 6/12, Fisher p = 0.0056, OR 0.08 [0.013–0.50] | **Not reported (C4)** |
| FA vs Tele+Sup | — | 2/27 vs 6/9, p = 0.0010 | Not reported |
| 4×2 autonomy × field | — | Freeman-Halton p = 0.0017 | Not reported |
| UAV 1/13 = 7.7%; Hybrid 4/7 = 57.1% | L537, L637, L730, L740 | UAV vs Hybrid p = 0.031 (post hoc, confounded); UAV vs the rest p = 0.23 | Values OK; **"weakest of any" unsupported (M15)** |
| UAV sim 8/13 = 61.5%; Hybrid sim 1/7 = 14.3% | L537 | OK | OK |
| FA sim 16/27 = 59.3%; Shared sim 2/3 = 66.7% | L521 | OK | OK |
| Scenarios 21/6/5/4/1/1/1 | Table XII, L541 | OK | OK |
| Generic by mode 16/3/1/1 = 21; Underground 4 FA + 2 Sup | L555 | OK | OK |
| Realism 20/21 = 95.2% vs 15/18 = 83.3%; 35/39 = 89.7% | L631, L633, L653, L697, L730, L740 | p = 0.32 (n.s.); 89.7% [76.4–95.9] | Values OK; **no source table (C9)** |
| 2/39 = 5.1% self-declared not ready | L625 | OK | OK |
| Clusters 12+7+5+3 = 27 | L593–L599 | OK | OK |
| "five of the seven" sim-only (single-robot cluster) | L595 | No table | **Unverifiable (M10)** |
| [25]: 26.5-point drop | L623 | 95.83 − 69.36 = 26.47 | OK |
| CRED: 358 / 16,607 / 110.2 M / US$169.7 B; averages 377 / 57,429 / 169.0 M / US$215.0 B; 72.8%; Myanmar 3,820 | L668–L670 | Verified against the CRED report by citation-verifier; Myanmar US$11 B unchecked | OK |
| Afghanistan 2,200 deaths | L670 | No citation | m6 |
| 74% at 24 h → 22% at 72 h | L672 | Verified in NBC quote | OK (weak source) |
| ">90%" at 72 h | L672 | [2] says ~90% at **24 h** | **Likely wrong (M20)** |
| Abstract length | L730 | 275 words | **Over 250 (M26)** |

## 10. PRISMA 2020 checklist (and PRISMA-S)

R = reported, P = partial, M = missing. The methodology-auditor's full PRISMA-S pass did not complete; this table is my own.

| Item | Status | Line / note |
|---|---|---|
| 1 Title identifies SR | R | L720 (but omits Supervisory, M27) |
| 2 Abstract (PRISMA-A) | P | L730: no sources, dates, risk of bias, limitations, funding or registration |
| 3 Rationale | R | L668–L690 |
| 4 Objectives | R | L313–L321 (RQ1–RQ4) |
| 5 Eligibility criteria | P | L357–L365; no language or document-type criteria; possible quartile filter (I-12) |
| 6 Information sources + dates | **M/P** | L325; no search dates per source; Google Scholar and AI not reported (I-1, I-2) |
| 7 Search strategy (full strings) | **M** | L349; two terms only; no Boolean or fields |
| 8 Selection process (reviewers, independence, automation) | **P, contradicted** | L371; conflicts with the docx (I-4); automation/AI not disclosed |
| 9 Data collection process | P, contradicted | L375 (I-9) |
| 10a/b Data items | P | Table III lists fields, but the "environmental-realism" item is not defined (C9) |
| 11 Risk of bias / quality | **M** | L643 admits none |
| 12 Effect measures | M (N/A-ish) | Proportions only; no stated measure or CI |
| 13a–f Synthesis methods | P | Descriptive counts; no stated methods for crosstabs, tests or sensitivity |
| 14 Reporting-bias assessment | M | — |
| 15 Certainty assessment | M | — |
| 16a Study selection flow | R/P | Fig. 2; needs the "other methods" column (M2) |
| 16b Excluded-but-near-miss studies cited with reasons | P | Only [9] is given; borderline exclusions should be tabulated |
| 17 Study characteristics | P | No per-study characteristics table in the manuscript (supplement needed) |
| 18 Risk of bias in studies | M | — |
| 19 Results of individual studies | P | Only flagship papers described |
| 20a–d Results of syntheses | P | Counts and crosstabs; no uncertainty (C4) |
| 21 Reporting biases | M | — |
| 22 Certainty of evidence | M | — |
| 23a–d Discussion and limitations | P | L615–L654; Limitations thin (C10) |
| 24a–c Registration / protocol / amendments | **M** | — |
| 25 Support / funding | **M** | — |
| 26 Competing interests | **M** | — |
| 27 Data, code, materials availability | **M** | Extraction xlsx missing (C7) |

**PRISMA-S:** item 1 (databases named) P; 2 (multi-database platforms) M; 3 (registers) M; 4 (online resources/browsing) M; 5 (citation searching) M; 6 (contacts) M; 7 (other methods, incl. Google Scholar and AI) **M, and concealed**; 8 (full search strings) **M**; 9 (limits and filters) P (year only); 10 (search filters) M; 11 (prior work) M; 12 (updates) M; 13 (dates of searches) **M**; 14 (peer review of search) M; 15 (total records per source) R (Table II); 16 (deduplication method) R (L353).

## 11. Coverage proof

**Manuscript lines read, in full:**
- Title and authors: L718–L724
- Abstract and Index Terms: L728–L732
- I: L666–L699
- II: L307–L409
- III: L419–L555
- IV: L567–L605
- V: L615–L654
- VI: L736–L744
- Bibliography: L802–L908, plus the corpus list L756–L798

**Working records read in full:** L1–L299 (Secs. 1–8), L912–L1084 (Sec. 16 revision log and Sec. 17).

**Authors' records read:**
- `paperlinks.xlsx`: all 130 rows, programmatically tabulated.
- All 8 `.docx` files, full text including the 125-row screening table.
- `assets/prisma/prisma.csv`, to confirm the old 33/1 split is confined there.

**PDFs opened (pdftotext, by me):** record 126 ([21]), 116 ([12]), 30 ([25]), 53 ([47]), 113 ([20]), 66 ([43]).
- The stats agent additionally opened 17, 30, 53, 66, 116 and 126 and checked the duplicate-pair MD5s.
- The citation agent spot-checked [10], [13], [25], [42] and [47].

**Figures opened:** prisma_diagram, fig_taxonomy and fig_autonomy_validation (by me); all 7 (by the stats agent).

**Agents run:**

| Agent | Status |
|---|---|
| stats-consistency-checker | Completed |
| citation-verifier | Completed |
| academic-editor | Completed |
| taxonomy-theorist | Completed |
| journal-scout | Completed |
| literature-scout | Stopped (rate limit) |
| methodology-auditor | Stopped (rate limit) |
| corpus-claims A and B | Stopped (rate limit) |
| q1-reviewer | Stopped (rate limit) |

**Web queries (mine):**
1. *Applied Soft Computing* SAR path-planning SLR
2. Shuvo 2026 Frontiers
3. IEEE Access AI disclosure

Agents' queries are listed in their own files.

**URLs used:**
- <https://ieeeaccess.ieee.org/authors/submission-guidelines/>
- <https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/>
- <https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1857704/full> (via the taxonomy agent and the earlier scan)
- The agent files list the rest, e.g. Crossref records for all 48 DOIs.

**Status of the earlier scan's Top-9 risk list:**

| # | Risk | Status |
|---|---|---|
| 1 | Search strategy | CONFIRMED, and worse: the records show Google Scholar, ChatGPT and Gemini as discovery sources |
| 2 | Bakzadeh mischaracterization | CONFIRMED (platform count STILL OPEN). Missing competitors: STILL OPEN |
| 3 | No κ / quality appraisal / protocol | CONFIRMED |
| 4 | "has not been reported previously" | CONFIRMED still unhedged |
| 5 | Inferential statistics | CONFIRMED values, still absent from the manuscript |
| 6 | LOA grounding and coding manual | CONFIRMED absent |
| 7 | Refs [3] NBC and [2] arXiv | CONFIRMED weak; [2] also does not support its sentence |
| 8 | "model reference paper" wording | CONFIRMED, in 5 manuscript places plus captions |
| 9 | Venue quartile | CONFIRMED unverified; IEEE Access may be Q2 |

**To finish after the limit resets (06:00 Asia/Dhaka):**
1. Resume literature-scout (full novelty scan; verify Shuvo and the ASC SLR).
2. Resume both corpus-claim agents (remaining ~28 papers).
3. Resume methodology-auditor (≥15 excluded-record spot checks; IEEE / RAS / JFR AI policies).
4. Resume q1-reviewer.
