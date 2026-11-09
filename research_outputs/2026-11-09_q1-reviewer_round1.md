# Simulated Q1 peer review, Round 1 (Reviewer 2)

**Manuscript:** "Who Holds the Decisions? A Systematic Review of Autonomy Modes and Validation Depth in Disaster Search-and-Rescue Robotics, 2025–2026" (Avi, Sultana, Sarker)
**Target venue:** *Journal of Field Robotics* (Wiley), review article
**Date of review:** 2026-11-09
**Material reviewed:** the manuscript sections of `SAR_review_master_document.md` only (title and authors, Abstract, Secs. I–VI, back matter, Tables I–XVIII, Figs. 1–7 as image files, APA reference list), plus the supporting information in `supplementary/` and `data/extraction_table.csv` and `data/analysis_output.md`. I did not read the working-record sections or earlier agent reports, so this review reflects what an external referee would see.
**Spot checks done:** recomputed table marginals and crosstab totals against S2/S5; cross-checked the PRISMA diagram against Tables II and V; checked mode and human-role codes against the S3 rationale and the S6 blind codes; ran web searches for competing prior work (sources listed at the end).

---

## 1. Summary of the submission (as the editor would see it)

The authors classify 39 disaster search-and-rescue (SAR) robotics journal articles from 2025–2026 into four autonomy/HRI modes (Teleoperation, Supervisory, Shared-Collaborative, Fully Autonomous). They cross-tabulate the modes against validation depth (simulation, partial or lab, bench, field). The headline claim is that Fully Autonomous (FA) studies, 69% of the corpus, were physically or field-tested less often than studies with a human in the mission. Sensitivity analyses then attribute the gap mainly to the "algorithm-first" genre of FA papers, not to autonomy itself. The manuscript is unusually candid about its limitations: a single-phrase publisher-portal search, 37 of 130 records found through ChatGPT/Gemini, unretained screener decisions, AI-performed extraction, and a reliability check that is AI against original labels. Those limitations go to the core of what a systematic review must deliver, and the main inferential result does not survive the authors' own sensitivity analyses.

## 2. Decision and confidence

**Decision: Reject, with encouragement to resubmit** (rubric mean 2.6; Search & Selection scored 1, which maps to Reject under the rubric).
**Confidence: High** (4/5).

The honesty of the Methods and the threats-to-validity section counts in the authors' favour, and the data package (page-referenced extraction table, analysis scripts, coding manual) is better than most submissions I see. But candour does not cure a non-systematic search. More than half of the included studies (21/39) came through non-reproducible routes, there is no human inter-rater agreement at any stage, and the primary pre-specified contrast is p = 0.060 and collapses (p = 0.35) under the alternative mode codes. A resubmission built on a reproducible database search and human double-coding could be publishable, because the question is a good one for JFR. In its current form it is not a systematic review in the PRISMA sense.

## 3. Rubric scores

| # | Dimension | Score (1–5) | Justification |
|---|---|---|---|
| 1 | Novelty & positioning | **2** | The cross-tabulation is plausibly new (my spot check found no review that tabulates autonomy mode against validation depth). But the qualitative finding is long established: deployed rescue robots are overwhelmingly teleoperated, autonomous multi-robot SAR has rarely left simulation, and there is a lab-to-field gap. Key prior work is uncited (Liu & Nejat 2013; Queralta et al. 2020; Drew 2021; Murphy 2014). By the authors' own sensitivity analysis the main finding reduces to "algorithm papers are evaluated in simulation", which is unsurprising. |
| 2 | Search & selection rigor | **1** | The search used one phrase ("rescue robot"; "disaster rescue robot" on MDPI) on publisher portals. There was no Scopus/WoS search, no Boolean string, and no search dates. 28% of records (37/130) and a majority of the included studies (21/39) came via Google Scholar or LLM prompts. Screener decisions were not kept, so there is no κ, and there was no protocol. |
| 3 | Quality appraisal | **2** | The bespoke VDR score is not a risk-of-bias instrument. Its VD component is nearly the outcome variable, its RP component is a reporting indicator, it was AI-scored with no reliability check, and it is not used to weight or stratify beyond one sensitivity row. |
| 4 | Data extraction & coding | **2** | Positives: page-level provenance and a released coding manual. Negatives: extraction was done by an AI, the original workbook was lost, and reliability is AI against the "original" labels, whose own provenance is unclear. There are also several internal contradictions in the human-role and mode codes (M4). |
| 5 | Analysis & statistics | **3** | Good practice includes Wilson CIs, exact tests, conditional-MLE ORs, an explicit "exploratory" label and sensitivity analyses. The problems: the abstract leads with an outcome other than the pre-declared primary one, a mechanism is inferred from loss of significance in a 29-study subset, the confound is not modelled, and the Methods list of sensitivity analyses does not match Table XVII. |
| 6 | Theoretical contribution | **3** | Table IV maps the modes to Sheridan–Verplank, Parasuraman and Beer. But the single-label scheme contradicts the per-function model it cites, the bands overlap at LOA 5, the S/C ordering is asserted rather than argued, and "FA" is operationalized by the test setup, not by system authority. |
| 7 | Insight & implications | **3** | The "research genre" explanation is a real attempt at mechanism. The reporting recommendations are sensible but generic, are not tied to existing standard test methods (NIST/ASTM E54) or responder requirements, and Sec. IV is an annotated bibliography. |
| 8 | Threats to validity | **4** | Construct, internal, external and conclusion validity are all addressed, specifically and honestly. This is the strongest part of the paper. |
| 9 | Writing & structure | **3** | The prose is clean, but the manuscript still contains [[AUTHOR INPUT NEEDED]] placeholders. There are also out-of-order table citations, a confusing Tong et al. bullet, references to "an earlier draft of this review", and internal file paths in the supplementary files. |
| 10 | References & presentation | **3** | Nine reference entries still carry UNVERIFIED fields. Four of the seven figures duplicate tables, figure styling is inconsistent, and key prior work is missing. |
| | **Mean** | **2.6** | Below 3.3 and a 1 on dimension 2, so **Reject (resubmit)**. |

---

## 4. Major comments

**M1. [Sec. II-B, Table II, Fig. 2: Search strategy] The search is not systematic, and the identification counts are not raw hit counts.**
*Problem.* The search used one two-word phrase ("rescue robot"; "disaster rescue robot" on MDPI) on seven publisher portals, with a lower date bound but no end date and no search date. No bibliographic database (Scopus, Web of Science, Compendex), no ACM DL and no citation chasing was used. 52 of 130 records (40%) came from Google Scholar (15) or ChatGPT/Gemini (37), and **21 of the 39 included studies (54%)** came through these non-reproducible routes. The inclusion yield also differs sharply by route: 18/77 (23%) for publisher searches against 21/48 (44%) for other methods. That shows the non-systematic routes shaped the corpus. Finally, the "records identified" figures (for example IEEE Xplore n = 5 for "rescue robot" from 2025 onward) cannot be raw hit counts. A query like that returns hundreds of IEEE records, conference papers included. This implies an unreported title-level selection step between hits and "cataloged" records.
*Why it matters.* This affects PRISMA 2020 items 6–7 and 16 and PRISMA-S items 1, 3, 8 and 13. It also bears directly on the headline outcome. Papers that say "drone" or "UAV" rather than "robot", and papers framed as "search and rescue" rather than "rescue robot", are missed, and that bias plausibly differs by platform and mode. LLM suggestions favour highly visible papers. The 69% FA prevalence and the mode × validation contrast therefore cannot be generalized even to the 2025–2026 literature.
*Fix.*
1. Run and report a full search in Scopus, Web of Science Core Collection and IEEE Xplore (optionally ACM DL and Compendex), with exact strings, field tags, limits, platform and date of search for each source. A starting Scopus string:
   `TITLE-ABS-KEY(("search and rescue" OR "search-and-rescue" OR USAR OR "disaster response" OR "disaster robot*" OR "collapsed building" OR earthquake OR "mine rescue" OR "wilderness search" OR wildfire OR flood) AND (robot* OR UAV OR UAS OR drone* OR UGV OR "unmanned aerial" OR "unmanned ground" OR quadruped OR legged OR "surface vehicle" OR swarm)) AND PUBYEAR > 2024 AND (LIMIT-TO(DOCTYPE,"ar"))`
2. Report raw hits per source, then records after deduplication, then title/abstract screening, then full text.
3. Keep the Google Scholar and LLM routes, but only as supplementary "other methods", with prompts, model versions and dates.
4. Add a sensitivity analysis restricted to database-identified studies, and report the mode distribution and the FA contrast by identification route.
5. Add the identification route (and, for AI routes, model and date) as a column in the screening log and extraction table.

**M2. [Sec. II-B and II-D: Eligibility] Undisclosed or unconfirmed selection filters.**
*Problem.* Three eligibility rules are left as author-input placeholders: journal-only, English-only, and the end of the publication window. The Methods also carry a placeholder asking whether journal ranking was used. In the supporting information, every PDF filename in `S6_reliability_blind_codes.csv` begins with a quartile tag (for example "Q1 06 …" and "Q2 77 …"), and all 39 included studies are tagged Q1 or Q2. A referee will read that as an undisclosed venue-quartile filter.
*Why it matters.* An undisclosed inclusion criterion breaches PRISMA item 5 and is a selection bias. Quartile tagging also correlates with venue type, which plausibly correlates with validation depth.
*Fix.* State every eligibility rule as it was actually applied: document type, language, publication window with an explicit end date, and whether quartile was recorded and whether it was used. If quartile was used at any stage, declare it as a criterion, justify it, and report how many records it removed. Strip quartile prefixes from the filenames in the supporting information, or explain them.

**M3. [Sec. II-E, Abstract: Screening] The claim of two independent screeners cannot be verified, and the post hoc check implies misclassification.**
*Problem.* The abstract states "two reviewers screened 125 full texts". The Methods say the separate decisions were not kept. A placeholder further discloses that the screening record describes the decisions as "averaged out", which has no meaning for include/exclude judgements. Who screened, and how disagreements were resolved, is still unstated. The post hoc AI check on 23 excluded records flagged 2 as possibly eligible and 4 as borderline. That is 26% non-agreement in a sample deliberately enriched for borderline cases. The authors also concede that the C2 rule for abstract agents "was not applied uniformly" (records #70 and #83 against Xue et al., 2025).
*Why it matters.* PRISMA item 8 requires the number of reviewers and the process for resolving disagreement. Without per-screener decisions the abstract's "two reviewers" is unverifiable. Inconsistent application of C2 bears directly on the FA cell, which is where abstract agents land.
*Fix.*
1. Have two authors re-screen independently, either all 125 full texts or at minimum a stratified random 30% sample plus all records that fail C2, and report Cohen's κ with a 95% CI and the resolution procedure.
2. Settle #70 and #83 under one written C2 rule and apply it to Xue et al. (2025) as well.
3. Until this is done, the abstract should say "screened by two authors whose individual decisions were not retained", or similar.
4. Name the screeners by initials in the CRediT statement.

**M4. [Secs. II-F, II-G, III-A, IV-A–C; S2, S3, S6: Extraction and classification] Coding provenance is unclear, there is no human reliability evidence, and several codes contradict the text.**
*Problem.*
(a) Extraction was "carried out by an AI assistant", and "the original classification had a single coding stream". The manuscript never states whether that stream was a human author or the same AI. If it was the AI, the reported κ = 0.79 is AI against AI and says nothing about human-reproducible classification.
(b) The original extraction workbook was not retained.
(c) I found these internal contradictions in the mode and human-role codes:
- **Raghavan et al. (2026) and Khattab et al. (2025)** are coded Teleoperation, yet `human_role_modelled = N` in S2/S3, while the AI blind coder (S6) codes both as Y. Teleoperation by definition requires a human deciding each motion. Sec. III-A then counts these two studies in the "human-in-mission" group, in which "a human acts in 10 of 12".
- **Khattab et al. (2025)** is described in Sec. IV-A as "validated on synthetic data, not on the physical prototype". It is nonetheless coded "Prototype bench test" (a physical category), and Sec. III-D says "Teleoperation: all five studies included physical testing."
- **Ruan et al. (2025)** is described in Sec. IV-B as run "along predefined waypoints, without a live operator". It is coded Supervisory with human role = Y. Clarification 2 of the authors' own coding manual (goals set once before the mission, then launch only) codes this F.
- **Bhattacharya & Butail (2025)**: the adaptive swarm was evaluated "in simulation on replayed participant trajectories" while "during the live user study the swarm stayed stationary". The coding rule says pre-recorded data are not evidence of mode, so the closed-loop headline evaluation contained no live human.
- **He et al. (2026)** ("flown outdoors … with human subjects") is coded human role = N, but **Strand et al. (2026)** (offline scoring of recorded images) is coded Y. The human-role variable is therefore not applied consistently.
- **Vani et al. (2026)**: per the paper, it is not stated which mode was used in testing. It is coded FA; the blind coder says S.
- Sec. II-G says "All four disagreements involved the Supervisory/Shared-Collaborative boundary or papers that report both manual and autonomous modes." In S6 the disagreements are Schomer & Adams (S→F), Gaitan et al. (C→T), F. You et al. (C→S) and Vani et al. (F→S). Schomer & Adams fits neither description.
(d) The decision rule ("control paradigm as executed in its headline closed-loop evaluation") does not say what to do with studies whose headline evaluation is open-loop perception on a dataset (Raghavan, Khattab, partly Strand). Those studies are forced into a mode their evaluation never exercised.
*Why it matters.* The primary contrast rests on a 12-study human-in-mission group. Moving two or three of these studies changes the result. Sensitivity (c) already shows strict field testing going from p = 0.060 to p = 0.35 when only the four AI-disputed codes change.
*Fix.*
1. State exactly who (human or AI) produced the original mode, validation, human-role, VD and RP codes.
2. Have a co-author who did not assign the original labels complete the blind sheet already provided (`human_second_coder_sheet.csv`) for **mode, human role, validation (strict/lenient) and VD/RP**. Report κ, AC1 and the confusion matrix for each.
3. Adjudicate each case listed above with page-cited evidence, publish the adjudication log, and re-run every table.
4. Add a "not applicable: open-loop/component-level evaluation" mode code, or an explicit rule for such studies.
5. Report the AI check separately, labelled as such (the coding manual's own §6 already says this).

**M5. [Abstract, Secs. III-D, III-G, V-A, VI: Statistics] Outcome switching, fragility, and a mechanism inferred from non-significance.**
*Problem.*
(a) Sec. II-I pre-declares the primary contrast as **strict field testing**, which gives p = 0.060 (OR 0.17, 95% CI 0.013–1.43). The abstract instead leads with **any physical testing** (p = 0.018), and the conclusion calls the result "statistically clear for physical testing and validation depth". Both outcomes were chosen after tabulation. About eight tests are run on the same contrast (strict, lenient, any-physical, VD = 3, Mann–Whitney on VD, two Freeman–Halton tests, the secondary contrast), with no multiplicity control.
(b) **No outcome survives both key sensitivity analyses.** Any-physical fails under (a) (p = 0.41). Strict and lenient field testing fail under (a) and (c) (p = 0.20/0.11 and 0.35/0.10). The abstract reports the attenuation under (a) but omits the collapse under (c).
(c) The "algorithm-first genre" mechanism is inferred because p rises when 10 FA studies are removed. But 2/17 (11.8%) against 4/12 (33.3%) still gives an OR of about 0.27, with a power problem rather than a null. Absence of significance in a 29-study subset is not evidence that the effect "largely disappears" (Sec. V-A). Contribution type, the proposed confounder, was never coded for the 12 non-FA studies, so the mechanism is asserted, not tested.
(d) The Methods list sensitivity (a) as "excluding papers whose evaluated setup models no human role". Table XVII (a) is instead "physical platform only". The human-role version appears only in S5 as (a′) and has n = 1/10.
(e) Sec. II-I calls the four-mode test "Freeman–Halton". S5 shows a Monte Carlo permutation estimate (200,000 draws, seed 1). The Mann–Whitney test is run on a 3-level ordinal variable with medians of 2 against 2, and no effect size is reported.
*Why it matters.* As written, the abstract and conclusion overstate the inferential support. For a review whose central message is "do not over-read prevalence", over-reading p-values is a credibility problem.
*Fix.*
1. In the abstract and conclusion, report the pre-declared primary outcome first, with its OR and CI, and state that the contrast was not robust to the alternative mode codes (sensitivity c).
2. Code **contribution type** (algorithm / system-platform / interface-HRI / integrated system) independently for all 39 studies. Present mode × contribution type × validation, and estimate the mode effect adjusted for contribution type with exact or Firth logistic regression or a Mantel–Haenszel stratified OR. Report effect sizes and CIs for every row of Table XVII, not just p-values.
3. Recast the "genre" explanation as a hypothesis unless the stratified analysis supports it.
4. Make Sec. II-I and Table XVII list the same sensitivity analyses, in the same order.
5. Describe the Monte Carlo approximation precisely, add rank-biserial or Cliff's δ for VD, and apply Holm correction across the family of contrasts, or explicitly name a single primary test.

**M6. [Secs. II-G, IV, V-B; Table IV, Fig. 7: Construct validity of the taxonomy] The "Fully Autonomous" category measures the experiment, not decision authority, and this undercuts the title question.**
*Problem.* FA is defined as "no human makes or approves decisions during the evaluated mission". In 26 of 27 FA studies no human was modelled at all (Sec. III-A). The authors themselves conclude that "the Fully Autonomous label describes the experiment, not the system" (Sec. IV-E). The comparison "FA vs human-in-mission" is then partly circular. A study with an operator in the loop must build an interface and usually hardware, so it is more likely to be physically tested by construction. This is the circularity M5 cannot fix statistically.
The theoretical mapping has further problems:
- Table IV assigns Shared-Collaborative to LOA 3–5 and Supervisory to 5–7, so the bands overlap at 5.
- Placing C below S is asserted from a single argument (real-time authority over a task class). Beer et al. (2014) and Parasuraman et al. (2000) would place a split-by-function system at different levels for different functions.
- The single-label design contradicts the per-function model the paper itself invokes and recommends (Sec. V-B, V-E item 3).
- The title "Who Holds the Decisions?" promises an analysis of decision authority that the coding does not deliver for 26/27 FA studies.
*Why it matters.* For a JFR/HRI readership, a taxonomy paper is judged on whether its categories are valid and reliably applicable. The weakest boundary, C/S (2 of 3 C studies recoded), and the circular FA definition sit exactly where the inference is made.
*Fix.*
1. Code per-function autonomy (Parasuraman's four stages, at least for perception/analysis, decision and action) for all 39 studies now. With 39 papers this is feasible, and it turns the recommendation into a contribution.
2. Separate two axes explicitly: (i) the *intended* decision authority of the system as designed, and (ii) the *human presence in the evaluation*. Cross-tabulate both against validation.
3. Make the LOA bands non-overlapping or justify the overlap. Justify the C/S ordering with a citation, or drop the ordinal claim and treat the modes as nominal (the data show no monotonic gradient anyway, Sec. III-D).
4. Revise the title, or deliver what it asks.

**M7. [Sec. I, Table I, contributions 1–2, Sec. IV-E: Novelty and positioning] Prior work on the same axis and the same finding is missing, and one trend claim is unsupported.**
*Problem.*
(a) The claim that "none organizes a research corpus primarily by how much decision authority the human retains" overlooks earlier work:
- **Liu & Nejat (2013)**, "Robotic urban search and rescue: A survey from the control perspective" (*J. Intell. Robot. Syst.* 72(2), 147–165, doi:10.1007/s10846-013-9822-x), which surveys USAR robotics along teleoperated, semi-autonomous and autonomous control.
- **Queralta et al. (2020)**, "Collaborative multi-robot search and rescue" (*IEEE Access*), which discusses autonomy levels and human–swarm interaction.
- **Drew (2021)**, "Multi-agent systems for search and rescue applications" (*Current Robotics Reports*), which concludes that multi-agent SAR is not deployment-ready and calls for realistic evaluation. This is the same observation as Table XVIII.
- **Murphy (2014)**, *Disaster Robotics* (MIT Press), which documents that fielded systems are overwhelmingly teleoperated.
- **Yanco & Drury (2004)** on HRI taxonomy.
Bakzadeh et al. (2026), which the paper cites, also already codes SAR platforms on an autonomy band.
(b) The characterization of Kareem et al. (2026a), that it "does not report how its studies are distributed across modes", is the crux of the gap claim but has no page citation.
(c) "The field's apparent shift toward autonomous systems" (Sec. I) is a trend claim that a two-year cross-sectional corpus cannot support. Hu et al. (2026) reports a shift toward perception- and learning-enabled systems, which is not the same thing.
*Why it matters.* "First" and "to our knowledge, none" claims draw scrutiny. As written, the contribution looks larger than it is.
*Fix.* Cite and discuss the works above. Re-state the contribution as the *first quantitative cross-tabulation for the 2025–2026 journal literature*, which corroborates and quantifies a long-standing qualitative observation. Add a page reference for the Kareem characterization. Either support the "shift" with longitudinal data (e.g., Hu et al.'s bibliometric series) or delete it.

**M8. [Back matter, Data availability, supporting information: Reporting completeness and AI disclosure] Claimed supplements are missing, and the supplementary files expose internal working material.**
*Problem.*
(a) Sec. II states that completed PRISMA 2020 and PRISMA-S checklists are supplied, and the supporting-information README lists `PRISMA_2020_checklist.md`, `PRISMA-S_checklist.md` and `search_protocol.md`. **None of the three is in `supplementary/`.**
(b) The screening log has no identification route, source, query, retrieval date or screener per record, so the PRISMA route split (18/21) cannot be verified.
(c) The supporting files contain internal working references: the coding manual tells coders not to open "`SAR_review_master_document.md`" or "`research_outputs/`" and to log disagreements in "master document Sec. 16"; S2's `bib_page` column reads "master doc Sec. 15"; S2 carries `manuscript_mode`/`mode_agrees` audit columns; and the S6 filenames carry quartile prefixes (M2).
(d) The AI-use statement has placeholders for model versions and, crucially, for **how the authors verified AI-generated content**. The statement discloses that an AI drafted and revised the manuscript text, extracted the data, carried out the reliability check and wrote the scripts. Wiley's policy requires human verification and accountability to be stated.
(e) The data repository DOI is a placeholder.
*Why it matters.* PRISMA items 24–27, reproducibility, and publisher AI policy. A referee who finds a file listed in the README missing will doubt the rest of the package.
*Fix.*
1. Supply both checklists with page/section locators, plus the search protocol.
2. Add route, source, query, date and screener columns to the screening log.
3. Remove internal paths and audit columns from the supplementary files, or explain them in a data dictionary.
4. Complete the AI statement: models, versions, dates, the tasks done by AI, and which named author checked which outputs against the PDFs, and how (all cells or a sample, with the error rate found).
5. Deposit the package (OSF or Zenodo) and give a reviewer-access link at resubmission.

**M9. [Sec. II-H, III-F: Quality appraisal] VDR is not a quality or risk-of-bias appraisal.**
*Problem.* VD (validation depth) is almost the outcome variable of the review. RP is a reporting-completeness indicator, and RP = 3 simply means code or data were released. Neither assesses the internal validity of the primary studies' claims: baselines, number of trials, variance, blinding of test conditions, independent test environments, cherry-picked runs, or author-built simulators. The scores were apparently assigned by the AI, with no reliability check. The adaptation from Kareem et al. (2026a) is not described.
*Why it matters.* PRISMA item 11 and AMSTAR-2 items 9, 12 and 13. Readers cannot tell whether "field-tested" studies are also *credible* field tests. One trial on one day is coded the same as a multi-site campaign.
*Fix.* Replace VDR with, or add, an explicit appraisal of experimental rigour. Items could include: baseline comparison; ≥ N repeated trials; dispersion reported; test environment independent of the training environment; failure cases reported; statistical test used; physical trials count and duration; and conflicts with platform vendors. Double-code it, report κ, and use it to stratify the validation analyses. Relabel the current VDR as "reporting indicators".

**M10. [Sec. IV, V-E, V-F: Depth of synthesis for a JFR readership] The synthesis is a catalogue and contains no field lessons.**
*Problem.* Sec. IV gives one or two lines per paper. There is no comparative table of the physical and field tests: environment, duration, trial counts, success metrics, failure causes, operator count, and communication setup. Field failure modes that the corpus does contain are scattered and not synthesized. Examples are Schomer & Adams (every flight ended early through line-of-sight loss, wind and battery), Mead et al. (long grass read as obstacles, wind-moved obstacles), and Cho et al. (4/10 planning success). The recommendations do not engage with existing standard test methods for response robots (NIST/ASTM E54 standard test methods), DARPA SubT evaluation practice, or responder requirements beyond Delmerico et al. (2019).
*Why it matters.* JFR readers want to know what breaks in the field and how to test for it. A counting exercise over 39 papers, most of them simulation-only, gives them little of that.
*Fix.*
1. Add a table of the 21 studies with any physical test, giving test environment, scale, number of trials, metrics, reported failure modes and human roles.
2. Add a short synthesis of field failure modes by mode and platform.
3. Map recommendations V-E 1–5 onto existing standard test methods and evaluation frameworks, citing them, and state what is new.

---

## 5. Minor comments

1. **[Title, Abstract, Sec. II]** "2025–2026" has no end date, and the search and screening dates are placeholders. State the cut-off (day, month, year) in the abstract and Methods. 2026 is a partial year.
2. **[Sec. III-A]** Table XII is cited before Tables VII–XI. Cite "Section III-D" instead, or reorder.
3. **[Sec. I, Tong et al. bullet]** "…not as a structurally comparable peer, because it is itself a review rather than a primary study of the kind analyzed…" makes no sense, because every comparator is a review. Rewrite (e.g., "a narrative conference review without a systematic method") or drop it, and decide whether it belongs in Table I.
4. **[Sec. IV-A]** "…compared with Liu et al. (2026)" should be a parenthetical citation: "(Liu et al., 2026)".
5. **[Secs. IV-C, IV-E item 2]** The text says a mode is "the least reproducible" or that "modes are not equally reproducible" when it means *reliably coded*. This clashes with the RP (reproducibility) variable. Use "reliably classified".
6. **[Sec. III-G row c, Table XVII]** "Independent blind codes" overstates independence, because the re-coder is an AI of the same family that did the extraction. Write "AI re-coding (blind to original labels)".
7. **[Sec. II-G]** Report the 4 × 4 confusion matrix in the paper, not only κ/AC1, and give κ for human role and validation as well as mode.
8. **[Secs. III-F, V-C]** The generic vs hazard-specific realism comparison (p = 0.30) is not motivated by any RQ and reads as a residual hypothesis. Motivate it under RQ4 or drop it. "Naming a specific hazard did not make the acknowledgment less likely" is a double negative; rephrase.
9. **[Sec. V-D, internal validity]** "…changed several validation, sensor, architecture, and scenario codes relative to an earlier draft of this review" refers to a document the reader has never seen. Quantify the changes (k of N cells per field) in a supplementary diff, or delete the clause.
10. **[Figs. 1, 3, 4, 5]** These duplicate Tables II, VII, IX and XI. Keep one form for each. Harmonize style: Figs. 1 and 3 have embedded titles and off-white backgrounds, unlike the others, and Fig. 1 says "catalogued" while the text says "cataloged". Use one order for "USV/UUV" (text) and "UUV/USV" (figure).
11. **[Fig. 1, Table II]** Grouping by DOI prefix splits Springer Nature into "Springer" and "Scientific Reports". Explain or merge. Also explain how two Tech Science Press records were retrieved "through the ScienceDirect search interface".
12. **[Fig. 2]** The right-hand column has no "records screened" box, unlike the left. Add the search dates per source. If the M1 database search is added, regenerate the diagram from the PRISMA2020 Shiny template with the raw hit counts.
13. **[Table IV, Fig. 7]** The LOA bands overlap at level 5 (3–5 and 5–7). Make them non-overlapping, or annotate the overlap in the figure and caption.
14. **[Tables VII, IX, X, XV]** Give Wilson CIs, or at least n/N, consistently. They are available in S5.
15. **[Sec. III-D, Table XIII]** The OR CIs span two orders of magnitude (e.g., 0.013–1.43). Add one sentence on what this imprecision means for interpretation.
16. **[Sec. V-A]** "A system can hardly be evaluated without being built, and once built it is easier to take into the field" is speculation. Mark it as such or support it with a citation.
17. **[Sec. V-A]** The comparison with Sinha et al.'s 4.2% notes the definitional difference but then draws a conclusion anyway. Either harmonize definitions (re-code with Sinha's eight research-type categories) or drop the numerical comparison.
18. **[Reference list]** Nine entries still carry UNVERIFIED fields: Chen, Rushworth & Jia (2026); de Bruycker et al. (1983); Delmerico et al. (2019); Hu et al. (2026); Jamwal & Singh (2026); Kaya Özdoğan et al. (2025); Man et al. (2026); Afzal et al. (2021) pages; Cruz Ulloa et al. (2026) volume. Gowry Sailaja et al.'s name form is also unconfirmed. Several entries give one page number where a range is expected (e.g., Chen, Sun et al. 2026, "13775"; Gowry Sailaja et al. 2026, "8655"; Li et al. 2026, "2981").
19. **[Sec. III / S2]** Report venue type for the included studies and run a venue-quality sensitivity check. The corpus mixes established venues with newer titles (*Discover Computing*, *Discover Applied Sciences*, *Int. J. Robotics and Control Systems*), and a referee will ask whether validation depth tracks venue.
20. **[Abstract]** "Coded with page-level provenance" is jargon; write "with page references". The abstract is near the usual 250-word limit; check JFR's limit.
21. **[Terminology]** "Uncrewed" (Sec. III-B, "uncrewed surface or underwater vehicles") and "unmanned" (UAV/UGV) are mixed. Pick one convention.
22. **[Sec. II-F]** The two coded items "human role modeled" and "environmental-realism limitation" are central to the results but are not in Table III's 18 fields. Add them, with VD, RP and FA cluster, to Table III or to a "derived variables" table.
23. **[Sec. IV-D]** Mead et al.'s hybrid trials took place outdoors (long grass, wind). Justify why this is "Partial" rather than a field test under the lenient rule.
24. **[Sec. II-B]** "Every AI-suggested record was retrieved from its publisher…" is good practice. Also report how many LLM-suggested items were hallucinated or non-existent and discarded. Readers will want that denominator.

---

## 6. Status of the [[AUTHOR INPUT NEEDED]] placeholders: which would block acceptance on their own

| Placeholder (location) | Blocks acceptance by itself? | Reason |
|---|---|---|
| Search and screening dates (Sec. II intro) | **Yes** | PRISMA item 7 and PRISMA-S item 9. A review without search dates cannot be assessed. |
| Google Scholar queries actually run; LLM prompts, model versions, dates (II-B) | **Yes** | The route that produced 21 of 39 included studies must be described. |
| Supplementary database search: date, strings, yield (II-B) | **Yes, for this referee** | See M1. Without it the dimension-2 score stays at 1. |
| Journal-ranking use (II-B) | **Yes** | A potential undisclosed criterion (M2). |
| Conference/non-English eligibility (II-D) | **Yes** | PRISMA item 5. External validity also relies on it (Sec. V-D). |
| Screener identities and disagreement resolution, given "averaged out" (II-E) | **Yes** | The abstract's two-screener claim depends on it (M3). |
| Which author verified AI-extracted values, and how (II-F) | **Yes** | Wiley AI policy and data integrity (M4, M8). |
| Blind human second coder κ (II-G) | **Yes, for this referee** | There is currently no human reliability evidence at any stage. |
| AI model versions and human-verification sentence (AI-use statement) | **Yes** | Publisher policy. |
| Repository DOI (Data availability) | **Yes, at acceptance** | The package is promised as "will be deposited". |
| Protocol registration confirmation (II-J) | No | Already disclosed as unregistered. A retrospective OSF record is optional but helpful. |
| Corresponding author, ORCID, funding, COI, CRediT, acknowledgments | No (administrative) | Needed at submission and production, not a scientific barrier. CRediT should record who searched and who screened. |

---

## 7. What would move this to Accept: shortest path, ranked by impact per unit of effort

1. **Fix the internal contradictions and the abstract framing.** *Very high impact, about 1 day.* Resolve the M4(c) cases, align the sensitivity lists (M5d), lead the abstract and conclusion with the primary outcome and report sensitivity (c) (M5a–b), and recast "genre" as a hypothesis. This removes the most visible credibility problems at almost no cost.
2. **Complete the supporting information and the disclosures.** *High impact, 1–2 days.* Add the PRISMA and PRISMA-S checklists and the search protocol, add route/source/date columns to the screening log, strip internal paths and quartile prefixes, complete the AI-use verification statement, disclose any quartile or language filter, and deposit on OSF/Zenodo (M2, M8).
3. **Human double-coding of mode, human role, validation and VD/RP for the 39 studies, with κ.** *Very high impact, 2–4 days.* The blind sheet and manual already exist.
4. **Code contribution type and per-function autonomy for all 39 studies; run the stratified or exact-logistic analysis.** *High impact, 3–5 days.* This turns the "genre" story into a tested claim and the per-function recommendation into a contribution (M5c, M6).
5. **Reproducible database search (Scopus + WoS + IEEE Xplore) with a full Boolean string, raw hit counts and dates; title/abstract plus full-text screening by two humans with κ; integrate the new studies; redraw PRISMA.** *Highest impact, 2–4 weeks.* This is the only way to lift dimension 2 above 1, and it will probably also enlarge the corpus enough to make the mode contrast estimable within strata.
6. **Add the prior work and re-scope the novelty claim.** *Medium impact, 1 day.* Cite Liu & Nejat 2013, Queralta et al. 2020, Drew 2021, Murphy 2014 and Yanco & Drury 2004, add a page-cited characterization of Kareem et al., and drop the "shift" claim (M7).
7. **Add a field-test synthesis table and a failure-mode synthesis mapped to NIST/ASTM standard test methods.** *Medium–high impact for JFR fit, 3–4 days* (M10).
8. **Replace or extend VDR with a double-coded rigour appraisal** (M9). *Medium impact, 2–3 days* (can run alongside item 3).
9. **Minor comments, figure de-duplication, and reference completion.** *Low–medium impact, 1–2 days.*

Items 1–4 and 6 alone would bring this to roughly a Major Revision. Item 5 is what makes it publishable as a systematic review in a Q1 venue.

---

## 8. Confidential comments to the editor

This is an honest submission. The authors disclose AI-assisted identification, AI extraction, unretained screener decisions and the absence of registration, which is more transparency than I usually see. Their supplementary package (page-referenced extraction, scripts, coding manual) is genuinely useful. My recommendation rests on substance, not on the disclosures. The search is a single phrase on publisher portals, a majority of the included studies were found through ChatGPT/Gemini or Google Scholar, there is no human agreement statistic at any stage, and the central contrast is not robust to the authors' own alternative codes. I also note three things the editor may want to check before any further round. First, the supporting information lists three files that are absent (both PRISMA checklists and the search protocol). Second, the PDF filenames carry journal-quartile tags that suggest an undisclosed venue filter. Third, the AI-use statement says an AI drafted and revised the manuscript and performed the reliability check, with the human-verification sentence still a placeholder. I would welcome a resubmission built on a reproducible database search and human double-coding. The research question, whether autonomy prevalence is mistaken for field readiness, is relevant to JFR and worth answering properly.

---

### Sources consulted for novelty spot-checks (web, 2026-11-09)
- [Liu & Nejat (2013), Robotic urban search and rescue: A survey from the control perspective (bibbase)](https://bibbase.org/network/publication/liu-nejat-roboticurbansearchandrescueasurveyfromthecontrolperspective-2013)
- [dblp record, Liu & Nejat 2013, J. Intell. Robot. Syst.](https://dblp.org/rec/journals/jirs/LiuN13)
- [Queralta et al. (2020), Collaborative Multi-Robot Search and Rescue, IEEE Access (Tampere repository PDF)](https://trepo.tuni.fi/bitstream/10024/127921/1/09220149_Collaborative_Multi_Robot_Search_and_Rescue.pdf)
- [Drew (2021), Multi-agent systems for search and rescue applications, Current Robotics Reports](https://link.springer.com/content/pdf/10.1007/s43154-021-00048-3.pdf)
- [Delmerico et al. (2019), The current state and future outlook of rescue robotics, JFR (EPFL Infoscience)](https://infoscience.epfl.ch/record/269149/files/JFR18-Final-The_Current_State_and_Future_Outlook_of_Rescue_Robotics.pdf)
- [A review on search and rescue robots in complex scenarios: key technologies of SLAM (JFR 2026; Nottingham Ningbo listing)](https://research.nottingham.edu.cn/en/publications/a-review-on-search-and-rescue-robots-in-complex-scenarios-key-tec/)
- [Synapse Social listing for the 74-paper 2016–2024 SAR systematic review (Kareem et al.)](https://synapsesocial.com/papers/69a76049c6e9836116a2ce35)

UNVERIFIED in this review: the Kareem et al. (2026a) details (IEEE Access, five-layer architecture, no per-study mode distribution) could not be confirmed from web snippets alone. The Sinha et al. (2026) 4.2% figure was not independently checked.
