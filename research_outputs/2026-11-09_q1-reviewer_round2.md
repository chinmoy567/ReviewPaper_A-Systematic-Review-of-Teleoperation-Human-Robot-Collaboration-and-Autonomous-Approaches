# Simulated Q1 peer review, Round 2 (Reviewer 2)

**Manuscript (revised):** "Autonomy Modes and Validation Depth in Disaster Search-and-Rescue Robotics: A Systematic Review of the 2025–2026 Literature" (Avi, Sultana, Sarker)
**Target venue:** *Journal of Field Robotics* (Wiley), review article
**Date:** 2026-11-09
**Material reviewed:**
- my round-1 report (`research_outputs/2026-11-09_q1-reviewer_round1.md`);
- the revised manuscript in `SAR_review_master_document.md`: Sec. 14 (title, Abstract, Conclusion, back matter), Secs. 9–13 (Sections I–V), and the APA reference list in Sec. 15;
- Sec. 16 entry 7, read as the authors' response to reviewers;
- `supplementary/` (all files) and `data/` (extraction table, analysis output, function-autonomy codes).

I did not read any other `research_outputs/` files.

**Spot checks done:**
- recomputed the route × decision split from `screening_log.csv`;
- cross-checked S2, S3, S6 and S7 codes study by study;
- recomputed Fisher tests for field testing against evaluated human presence (exact hypergeometric, by hand in Python);
- checked the Drew (2021) characterization against the source PDF;
- viewed Figs. 1, 2 and 7;
- ran one web search for competing reviews.

---

## 1. Summary of the submission (as the editor would see it)

The revision classifies 39 disaster-SAR robotics journal articles (2025–2026) into four autonomy/HRI modes and cross-tabulates mode against validation depth. The headline is now descriptive:
- Fully Autonomous (FA) studies dominate (27/39);
- none of the FA studies puts a human in the evaluated mission;
- most FA studies are evaluated only in simulation;
- the FA vs human-in-the-loop difference in field testing is "consistent in direction but not statistically established" (strict p = 0.060; none of the contrasts survives Holm adjustment).

The authors have made a serious, honest effort. They added Holm adjustment, an exact Freeman–Halton test, a publisher-only sensitivity analysis, a post hoc per-function coding (Table XX), a field-test table (Table XIX), the prior surveys I asked for, and both PRISMA checklists and a search protocol. However, every element that makes this a *systematic* review is still either missing or an `[[AUTHOR INPUT NEEDED]]` placeholder:
- a reproducible database search;
- search dates;
- the eligibility rules as actually applied;
- screener identities;
- any human reliability statistic.

Several coding contradictions I raised also survive, now in a different form.

## 2. Decision and confidence

**Decision: Reject, with encouragement to resubmit** (unchanged in category; rubric mean 2.7, and Search & Selection is still 1).
**Confidence: High (4/5).**

The text has improved materially. Statistics and framing went from overclaiming to appropriately cautious, and the threats-to-validity section is now exemplary. If this were judged on writing and candour alone, it would be at Major Revision. But a JFR editor cannot send out a "systematic review" with these features:
- no search dates;
- an unconfirmed journal-quartile filter, while every one of the 130 cataloged records is Q1/Q2;
- a majority of included studies found through Google Scholar or LLM prompts;
- no human agreement statistic at any stage.

Two new findings make the substantive problem sharper, not smaller:
- **Route composition.** 8 of the 12 human-in-the-loop comparison studies came through non-reproducible routes (S5, "Identification route" table: publisher route 18 studies, 14 FA, so 4 human-in-the-loop; other routes 21 studies, 13 FA, so 8 human-in-the-loop).
- **Lenient contrast.** The lenient-coding contrast (p = 0.014, the only nominally significant field-testing result) depends on two validation codes that contradict the paper's own lenient definition (new comment N1).

Most of the remaining blockers are author-supplied facts (Section 7). The rest are textual and could be fixed in a day or two.

## 3. Rubric scores (round 2, with round-1 score in brackets)

| # | Dimension | R2 score | R1 | Justification |
|---|---|---|---|---|
| 1 | Novelty & positioning | **2** | 2 | Prior surveys are now cited and Contribution 2 is narrowed to "first cross-tabulation". However: (i) the abstract's "autonomy and validation have not been reviewed together" and Sec. IV-E's "no prior SAR robotics review has made these observations" still overreach; (ii) the Sec. I claim that "none organizes a research corpus primarily by how much decision authority the human retains" sits awkwardly next to Liu & Nejat (2013), which the paper now cites as organizing by control level; (iii) **Drew (2021) is mis-cited** (N7); (iv) there is still no page-located evidence for the Kareem et al. (2026a) characterization, and the "apparent shift toward autonomous systems" sentence is still there. |
| 2 | Search & selection rigor | **1** | 1 | **Better reported:** hit counts are admitted as unrecorded, selection before cataloging is disclosed, the route is now in the screening log, and sensitivity (e) is added. **Substance unchanged:** two short phrases on publisher portals; no Scopus/WoS; no dates; quartile question open; screeners unnamed; no κ. The supplementary search protocol now discloses that the authors' own write-up calls Google Scholar "the main database", with seven queries (N6). |
| 3 | Quality appraisal | **2** | 2 | VDR is now honestly labelled "not a risk-of-bias tool", which is good. But no rigour appraisal was added, the scorer is a placeholder, and "repeated trials *or* baseline" (35/39) is too coarse to discriminate. |
| 4 | Data extraction & coding | **2** | 2 | Provenance is now stated (AI against AI), and He, Strand and Khattab were fixed. Still: no human coder; no rule for open-loop evaluations; Teleoperation and Supervisory labels on studies with no human in the evaluated mission; IV-A text contradicts Table XII; S3 contradicts S2 on Gaitan; S7 contradicts the FA definition (N2–N4). |
| 5 | Analysis & statistics | **3** | 3 | Big improvement in framing: primary outcome first, Holm, exact Freeman–Halton, (c) reported in the abstract. Not done: contribution-type coding and stratified analysis; effect sizes for Table XVII and for the Mann–Whitney test; the lenient result rests on two questionable codes (N1); "Four sensitivity analyses" lists five (N9); a lenient FA vs Tele+Sup contrast in S5 (p = 0.0027) is not reported or justified as excluded. |
| 6 | Theoretical contribution | **3** | 3 | Table XX (per-function coding) is a real addition and partly answers M6. But it is AI-coded, post hoc, and contradicts the mode definitions in at least three studies. The LOA overlap at 5 and the C-below-S ordering remain. The designed-mode and evaluated-presence axes are reported but **not cross-tabulated against validation**. When I did that cross-tabulation, it suggests the circularity I warned about (N3). |
| 7 | Insight & implications | **3** | 3 | Table XIX and the failure-mode bullets move in the right direction. The table still lacks trial counts, metrics, operator count and communications. The recommendations are not mapped to standards beyond one ASTM stepfield citation. Sec. IV is still largely a catalogue. |
| 8 | Threats to validity | **4** | 4 | Now with route-specific inclusion yields, the quartile pattern, reporting bias and qualitative confidence ratings. Strong. The only gap is that it does not mention that two thirds of the comparison group came from non-reproducible routes. |
| 9 | Writing & structure | **3** | 3 | Cleaner, but 20+ `[[AUTHOR INPUT NEEDED]]` placeholders remain in the manuscript (more in the supplement), and most of my round-1 wording minors were not touched (Section 5 below). |
| 10 | References & presentation | **3** | 3 | Seven verified references were added and only three name-form UNVERIFIED flags remain. Problems remaining: the Drew misquote; figure duplication and styling unchanged; Fig. 7 still shows overlapping LOA bands. |
| | **Mean** | **2.7** | 2.6 | A 1 on dimension 2 means **Reject (resubmit)** under the rubric. |

---

## 4. Status of round-1 MAJOR comments

| # | Topic | Status | Evidence |
|---|---|---|---|
| M1 | Search not systematic; counts not raw hits | **NOT RESOLVED** (reporting improved) | II-B now states that cataloged records are a title/abstract selection and that hit counts were not recorded. Sensitivity (e) has been added (Table XVII), and `screening_log.csv` has an `identification_route` column. But there is still no database search, no Boolean string and no dates. Sec. II-B carries a placeholder for the supplementary search. Sensitivity (e) leaves 14 vs 4 studies, "too few for inference" (III-G). See also new N5 and N6. |
| M2 | Undisclosed selection filters | **PARTLY RESOLVED** | II-B now discloses "every cataloged record appeared in a journal ranked Q1 or Q2 (66 Q1, 64 Q2)" and V-D discusses it. Quartile prefixes have been removed from S6 and the coder sheet. Whether quartile was used, journal-only/English-only, and the window end date are all still `[[AUTHOR INPUT NEEDED]]` (II-B, II-D). A 130/130 Q1–Q2 pattern from portal searches that include MDPI, Springer and Tech Science Press is extremely unlikely by chance. Until it is explained, an editor will assume a filter. |
| M3 | Two-screener claim unverifiable | **PARTLY RESOLVED** | II-E and V-D state that the decisions were not kept. The abstract lists "unrecorded screener agreement" as a limitation. But the abstract still asserts "two reviewers screened 125 full texts" as fact. The screener identities and the "averaged out" placeholder are still in II-E. There was no re-screen and no κ. #70/#83 were handled by sensitivity (d), not by adjudicating a single C2 rule. |
| M4 | Coding provenance, reliability, contradictions | **PARTLY RESOLVED** | **Resolved:** provenance stated (II-G: both codings AI-assisted); the description of the four disagreements corrected; He et al. and Strand et al. human-role coding made consistent; Khattab recoded to simulation-only (Sec. 16 entry 7). **Not resolved:** (i) Raghavan and Khattab are still Teleoperation with no human in the evaluated mission (S2 `human_role_modelled = N`; S7 `evaluated_human_presence = N`), so their "headline closed-loop evaluation" is open-loop perception, and no rule covers that case (coding manual §3 unchanged); (ii) Ruan is still Supervisory although S2 now says no operator was present, which is exactly coding-manual Clarification 2 ("goals set once ... code F"); (iii) Bhattacharya is still C, while S7 codes all four functions as human-held; (iv) Vani is still FA with "mode not stated", and S7 gives "designed authority C"; (v) no human second coder; (vi) the coder sheet still covers mode and human role only, not validation or VD/RP. New contradictions: N2, N4, N8. |
| M5 | Outcome switching, fragility, mechanism from non-significance | **LARGELY RESOLVED** (text); **PARTLY RESOLVED** (analysis) | The abstract and Conclusion now lead with strict field testing (p = 0.060), report Holm and the attenuation under (a) and (c), and call the result "not statistically established". Genre is recast as a conditional interpretation (V-A: "If the difference is real ... cautiously"). Freeman–Halton is now exact, with Monte Carlo as a check (S5). II-I and Table XVII list the same analyses. **Still missing:** contribution type was not coded for all 39 (Table XVIII covers FA only), so the genre explanation is still untested; no Mantel–Haenszel or exact-logistic adjustment; no ORs or CIs for the Table XVII rows; no effect size for the Mann–Whitney test (medians 2 vs 2, S5). V-B now says "a review cannot separate them". With 39 studies and a 4-level contribution variable it can at least be *stratified*, so that sentence is a cop-out. |
| M6 | FA measures the experiment; taxonomy construct validity | **PARTLY RESOLVED** | The title was changed and no longer promises "who holds the decisions". Designed mode and human presence are reported separately (Table XII, last columns; II-F). Per-function coding was added (II-G, V-B, Table XX, S7). **Not done:** (i) evaluated human presence is not cross-tabulated against validation (see N3; it is the stronger predictor); (ii) the LOA bands still overlap at 5 (Table IV, Fig. 7). II-G now acknowledges that this boundary is "least sharp", but the ordinal claim and the arrow in Fig. 7 remain; (iii) the C-below-S ordering is still argued from one sentence without a citation, even though the data show no gradient (III-D); (iv) Table XX contradicts the mode definitions (N2). |
| M7 | Prior work missing; novelty and trend claims | **PARTLY RESOLVED** | Liu & Nejat 2013, Queralta 2020, Drew 2021, Murphy 2014 and Yanco & Drury 2004 have been added (Sec. I, II-G; reference list), and Contribution 2 is narrowed. **Not done:** (i) no page reference for "Kareem et al. (2026a) ... does not report how its studies are distributed across modes" (Sec. I and Table I); (ii) "the field's apparent shift toward autonomous systems" (Sec. I, last paragraph before contributions) is unchanged; (iii) the abstract opener "their autonomy and validation have not been reviewed together" and IV-E's "no prior SAR robotics review has made these observations" are unchanged overclaims; (iv) Drew is mis-cited (N7). |
| M8 | Missing supplements; internal material; AI disclosure | **PARTLY RESOLVED** | **Done:** `PRISMA_2020_checklist.md`, `PRISMA-S_checklist.md` and `search_protocol.md` are now present; route column added; S6 filenames removed; `manuscript_mode`/`mode_agrees` dropped. **Remaining leaks:** `screening_log.csv` record 61 says "per Section 7.1 of the master prompt"; S3 contains "[2026-11-09 recode: ...]" working notes and refers to "boundary rule A–G", which are not defined in the public coding manual (that manual has Clarifications 1–5); S2 keeps the audit column `fa_cluster_agrees`; the coding manual tells coders to use a `pdf_filename` column that does not exist and a local folder `assets/papers/`; `search_protocol.md` cites internal files (`assets/docs/paperlinks.xlsx`, `Paper Selection Process.docx`) and says "the authors confirmed ... on 2026-11-08 and 2026-11-09"; S5 headers still say "human-in-mission" while the manuscript says "human-in-the-loop". **Still placeholders:** the AI-use human-verification sentence, model versions, repository DOI. The screening log has no screener or date columns. |
| M9 | VDR is not a quality appraisal | **NOT RESOLVED** (honestly relabelled) | II-H now says that VDR "does not assess bias" and "is not" a risk-of-bias instrument. That is truthful, but the PRISMA item 11 / AMSTAR-2 gap stays open. No rigour items were added (number of trials, dispersion, train/test environment independence, failure reporting), and the scorer is a placeholder. |
| M10 | Synthesis is a catalogue; no field lessons | **PARTLY RESOLVED** | New Table XIX lists 9 studies with site, scope and reported limitation. V-A synthesizes four failure patterns and cites ASTM E54.09. **Not done:** trial counts, metrics, operator count and communications setup in Table XIX; mapping of the V-E recommendations to specific standard test methods (only the E2828 stepfield standard is cited, and it covers mobility only); Sec. IV is still one line per paper. Table XIX also includes a study that does not meet its own heading (N1). |

## 5. Status of round-1 MINOR comments

| # | Topic | Status | Evidence |
|---|---|---|---|
| 1 | End date; search and screening dates | NOT RESOLVED (author input) | Sec. II intro placeholder; title and abstract still say "2025–2026" with no cut-off. |
| 2 | Table XII cited before VII–XI | NOT RESOLVED | III-A, second paragraph: "(Table XII)". |
| 3 | Tong et al. bullet | NOT RESOLVED | Sec. I bullet unchanged ("because it is itself a review rather than a primary study"). |
| 4 | "compared with Liu et al. (2026)" | NOT RESOLVED | IV-A, third bullet. |
| 5 | "least reproducible" / "not equally reproducible" | NOT RESOLVED | IV-C, last paragraph; IV-E item 2. |
| 6 | "independent blind codes" | NOT RESOLVED | III-G bullet (c). The Table XVII row says "blind codes" without "AI". Contribution 1 also calls an AI–AI check "a reliability check". |
| 7 | Confusion matrix; κ for human role and validation | PARTLY RESOLVED | The four disagreements are now listed in II-G. There is still no 4 × 4 matrix and no κ for the other coded variables. |
| 8 | Unmotivated generic vs hazard test; double negative | NOT RESOLVED | III-F and V-C; "Naming a hazard therefore did not make acknowledgment ... less likely" is still in V-C. It is now listed in II-I, but not tied to an RQ. |
| 9 | "earlier draft of this review" | NOT RESOLVED | V-D, internal validity, bullet 8. |
| 10 | Figures duplicate tables; styling | NOT RESOLVED | Figs. 3, 4 and 5 still duplicate Tables VII, IX and XI. Fig. 1 still has an embedded title, an off-white background, "catalogued" and the subtitle "DOI-verified by publisher". |
| 11 | Springer split; TSP via ScienceDirect | NOT RESOLVED | Table II, Fig. 1. The footnote "*Retrieved through the ScienceDirect search interface" is still unexplained. |
| 12 | PRISMA right column; dates | PARTLY RESOLVED | Fig. 2 is redrawn with per-route exclusions, but the right column still has no "records screened" box and there are no search dates. |
| 13 | LOA overlap in Table IV / Fig. 7 | PARTLY RESOLVED | Acknowledged in II-G text. Table IV and Fig. 7 still show 3–5 and 5–7 unannotated. |
| 14 | CIs in Tables VII, IX, X, XV | NOT RESOLVED | Still n and % only (the CIs exist in S5). |
| 15 | OR imprecision sentence | RESOLVED | III-D: "the evidence is weak ... too small to establish it statistically". |
| 16 | "A system can hardly be evaluated without being built" | NOT RESOLVED | V-A, second paragraph; still unmarked speculation. |
| 17 | Sinha comparison | PARTLY RESOLVED | Now compared against Sinha's 14.7% "experimental field" category, with the caveat that the categories differ. It still concludes "the order of magnitude agrees". Acceptable if hedged once more. |
| 18 | UNVERIFIED references; page ranges | LARGELY RESOLVED | Only three name-form flags remain (Gowry Sailaja, Rajashekhar, Vani). Page ranges are fixed (e.g. Gowry Sailaja 8655–8666). |
| 19 | Venue-type sensitivity | NOT RESOLVED | Not reported. Now more pressing given the Q1/Q2 disclosure. |
| 20 | "page-level provenance" jargon | NOT RESOLVED | Abstract, sentence 5. The abstract is 241 words, which is fine. |
| 21 | Uncrewed / unmanned | NOT RESOLVED | III-B list. |
| 22 | Derived variables missing from Table III | PARTLY RESOLVED | Human role and realism are now defined in II-F prose. VD, RP and FA cluster are not in a derived-variables table. |
| 23 | Mead et al. Partial vs field (lenient) | NOT RESOLVED | Still Partial under both codings (S3: "hybrid physical-simulated outdoor test"). See N1. |
| 24 | Count of hallucinated LLM suggestions | NOT RESOLVED (author input) | `search_protocol.md` §1.3 placeholder; nothing in the manuscript. |

---

## 6. New comments (round 2)

**N1. [Sec. III-D, Table XI, Table XIII row 2, Table XIX; S2/S3: lenient coding] The only nominally significant field-testing contrast depends on two codes that break the paper's own lenient rule.**
*Problem.* III-D defines lenient field testing as also counting "constructed outdoor courses and competition venues". Two codes break this rule:
- **S. You et al. (2026)** (Supervisory) is lenient-coded as a field test, but its site is "a mock coal-mine tunnel inside a university explosion laboratory" (IV-B; S3: "explosion-lab tunnel"). That is an indoor laboratory mock-up, not an outdoor course or a competition venue. Table XIX's own heading ("real site or competition venue") does not fit it either.
- **Mead et al. (2026)** (FA) ran a physical UGV outdoors in long grass and wind (IV-D). It stays Partial under lenient coding, while Yeoh et al.'s constructed outdoor volcanic course is upgraded.

Both calls go in the direction that favours the hypothesis. With S. You at Partial and Mead at field, the lenient contrast becomes FA 4/27 against HITL 5/12. That is exactly the row (c) lenient cell, p = 0.102, not 0.014. Cho et al.'s strict "bench" → lenient "Partial" switch is also unexplained.
*Why it matters.* The abstract reports p = 0.014 and Table XIII's smallest Holm p (0.071) comes from this row. The "consistent in direction" message survives, but the paper's best p-value is a coding artefact.
*Fix.*
1. Write the lenient rule as a decision list (indoor mock facility, outdoor constructed course, competition venue, real non-disaster site, real disaster site) and code every study against it.
2. Publish the per-study lenient rationale.
3. Recompute Tables XI, XII, XIII, XVII and XIX, and the abstract.

**N2. [Sec. II-G, V-B, Table XX; S7: per-function codes contradict the mode definitions] Table XX is presented as validating the modes, but it contains cases that the mode definitions forbid.**
*Problem.*
- **FA cases with human-held functions.** FA is defined as "no human makes or approves decisions during the evaluated mission". Yet Table XX's FA row shows decision held by a human in 1 study and shared in 1 (25/1/1). In S7 these are Yeoh et al. (acq = H, dec = H) and Vani et al. (designed authority C).
- **Teleoperation cases with no human present.** Table XX shows the human holding acquisition and decision in all 5 Teleoperation studies. II-G says the function codes describe "the evaluated configuration", but S7 codes Raghavan and Khattab as human-held while also coding `evaluated_human_presence = N`. The function codes therefore describe the *designed* allocation, not the evaluated one.
- **A Shared-Collaborative study coded as all-human.** Bhattacharya & Butail is coded H/H/H/H, which is a Teleoperation profile, yet it is counted as matching C.
- **Unnamed exceptions.** II-G reports a 36/39 match and says the three exceptions "are discussed in Section IV", but Section IV never identifies them as exceptions.

*Why it matters.* This is the paper's main theoretical addition since round 1. If it contradicts the definitions it is meant to support, a referee will discount both.
*Fix.*
1. State whether S7 codes the designed or the evaluated configuration, and recode to match II-G.
2. Name the exceptions in II-G.
3. Resolve Yeoh (FA with a human-held decision?) and Bhattacharya (C with an all-human profile?) with page evidence. Either change the mode or explain why the function codes differ.
4. Label Table XX as an AI-assisted, single-coder output in the caption. The caption says "post hoc AI-assisted coding", which is good; keep it.

**N3. [Secs. III-D, V-B: the circularity is now visible in the authors' own data] Field testing tracks evaluated human presence far more strongly than it tracks designed mode.**
*Problem.* Using S2 `human_role_modelled`, I cross-tabulated field testing against whether a human was present in the evaluated mission:
- **Strict coding:** 4/8 studies with a human present were field-tested, against 2/31 without (Fisher p ≈ 0.011).
- **Lenient coding:** 6/8 against 3/31 (p ≈ 0.0006).
- **Within the 12 human-in-the-loop-mode studies:** 4/8 against 0/4.

The four human-in-the-loop studies with *no* human in the evaluation (Raghavan, Khattab, Ruan, Gaitan) were never field-tested. This is what M6 predicted. A field test with an operator puts a human in the mission almost by construction, so "human present" and "field-tested" partly measure the same event.
*Why it matters.* The designed-mode contrast is partly a proxy for whether the authors ran a live, operator-in-the-loop trial. The genre explanation and the circularity explanation make different predictions, and the authors have the data to start separating them.
*Fix.*
1. Report this cross-tabulation (as a table and as a sensitivity row).
2. State plainly in V-B that evaluated human presence and field testing are partly co-determined.
3. Treat the designed-mode contrast as descriptive. Do not run more p-values on it.

**N4. [Sec. IV-A vs. Table XII: direct internal contradiction] Sec. IV-A says of the Teleoperation studies: "In all five, the human drives locomotion in the headline experiment."** Table XII reports a human in the evaluated mission for 3/5. S2 and S7 code Raghavan and Khattab as having no human in the evaluated mission, and IV-A itself says Khattab was validated only on synthetic data.
*Fix.* Rewrite IV-A to say that two of the five evaluate perception offline. Then either (i) add the "open-loop / component-level evaluation" rule I asked for in round-1 M4(d) and apply it, or (ii) justify, with page evidence, coding these two as Teleoperation from the *designed* control interface. Option (ii) contradicts the "as executed in its headline closed-loop evaluation" rule in II-G.

**N5. [Secs. II-B, III-G, V-D; S5 route table: the comparison group comes mainly from non-reproducible routes] Two thirds of the human-in-the-loop group came from Google Scholar or LLM prompts.**
*Problem.* S5 shows the publisher route yielded 18 included studies (14 FA, so 4 human-in-the-loop) and other routes yielded 21 (13 FA, so 8 human-in-the-loop). The screening log also shows very different inclusion yields by route: Google Scholar 10/14 (71%), Gemini 2/3, ChatGPT 9/31 (29%), and publisher platforms 18/77 (23%). A 71% yield from Google Scholar implies the searcher catalogued Scholar results with prior knowledge of their relevance. V-D reports the pooled 21/48 against 18/77 but not this breakdown or the composition of the comparison group.
*Why it matters.* The comparator in the primary contrast is drawn mostly from the non-reproducible routes. Sensitivity (e) leaves only 4 comparator studies.
*Fix.*
1. Add both facts to III-G and V-D.
2. Report the inclusion yield per route (four routes, not two).
3. This strengthens the case for the database search in M1.

**N6. [Supplement `search_protocol.md` §1.2 vs. Methods II-B: undisclosed discrepancy about the main search route]** The supplement states that the authors' own process write-up "names Google Scholar as 'the main database' and lists seven queries". The Methods present publisher-platform searching as the primary route (78 records) and Google Scholar as an "other method" with two logged queries (II-B placeholder). A referee who opens the supplement will see that the Methods and the authors' own record disagree about what the main search was.
*Fix.* The authors must settle this before resubmission. Report in II-B every query actually run on every source, including those that yielded no cataloged records. Then delete the internal-document references from the supplement.

**N7. [Sec. I, paragraph 3: mis-cited source] "Drew (2021) notes, citing field reports, that only two of at least 40 documented deployments involved any autonomous operation."** That is not what Drew says. Drew (2021, *Current Robotics Reports* 2:189–200, Introduction) reports at least 40 documented robot-assisted responses, of which "only four of them involved three or more robots deployed at once, and only two of those (both marine robots) involved a degree of autonomous operation". The "two" is a subset of the four *multi-robot* deployments, not of all 40.
*Fix.* Rewrite, for example: "Drew (2021) notes that of at least 40 documented robot-assisted responses since 2001, only four used three or more robots at once, and only two of those (both marine) involved any autonomous operation." Then check every other secondary characterization against its source PDF.

**N8. [S3 vs. S2: Gaitan et al. (2025)]** S3 codes "Human in evaluated mission: Y (p. p28)". S2 and S7 code N, Table XII (2/3 for Shared-Collaborative) uses N, and IV-C says validation was "without human participants". S3 is stale.
*Fix.* Regenerate S3 from S2, and add an automated consistency check to `analysis.py`.

**N9. [Sec. II-I] "Four sensitivity analyses test the primary contrast" is followed by five items, (a)–(e).** Also:
- S5 computes a lenient FA vs Teleoperation+Supervisory contrast (p = 0.0027) that does not appear in Table XIII. Either report it or state why it is outside the Holm family.
- The Mann–Whitney (p = 0.060) and Freeman–Halton tests are also outside the Holm family of five. Say so explicitly.

**N10. [Sec. II-G, II-H, II-F: who did what is still undeclared]** Three placeholders together mean that, as submitted, the reader cannot tell whether any human checked any coded value: who verified the extraction (II-F), who assigned VDR (II-H), and the AI-use verification sentence. The AI-use statement also says the assistant "drafted and revised the manuscript text". Wiley will accept that only with an explicit human-accountability statement.
*Fix.* Author input (see Section 7).

**N11. [Abstract and Sec. I, Contribution 1] "with explicit decision rules, a released coding manual, and a reliability check".** The only reliability check is AI against AI. Write "an AI-assisted consistency check (human inter-rater agreement pending)", or replace this with the human κ.

**N12. [Response to reviewers: Sec. 16 entry 7]** The locked-fact table in entry 7 says human-in-evaluated-mission "all studies 11/39 → 9/39". The manuscript (Table XII) and S5 give 8/39. The response letter should match the paper.

---

## 7. Remaining blockers, separated by type

### 7A. Purely author-supplied facts or actions (`[[AUTHOR INPUT NEEDED]]`). The text cannot fix these.

| Blocker | Location | Blocks acceptance on its own? |
|---|---|---|
| Reproducible Scopus + WoS + IEEE Xplore search, run with dates, raw hits and screening (protocol already in `search_protocol.md` §2) | II-B; Fig. 2 | **Yes.** It is the only route off a score of 1 on dimension 2. |
| Search and screening dates per source; corpus end date | II intro; II-D; title/abstract | **Yes** (PRISMA 7; PRISMA-S 9) |
| Whether journal quartile was used to select records | II-B, II-D | **Yes** (130/130 Q1–Q2) |
| Google Scholar queries actually run (2 or 7?); LLM prompts, model versions, dates; number of hallucinated suggestions | II-B; search protocol §1.2–1.3; N6 | **Yes** |
| Journal-only and English-only confirmation | II-D | **Yes** (PRISMA 5) |
| Screener identities; meaning of "averaged out"; disagreement resolution; ideally a re-screen with κ | II-E; abstract | **Yes** |
| Human blind second coder for mode, human role and validation (sheet exists); κ, AC1 and confusion matrix | II-G | **Yes, for this referee** |
| Who verified the AI extraction and who scored VDR; AI-use human-verification sentence; model versions | II-F, II-H, back matter | **Yes** (Wiley AI policy) |
| Repository DOI (OSF/Zenodo) | Data availability | Yes, at acceptance |
| Protocol registration confirmation (or a retrospective OSF record) | II-J | No |
| Corresponding author, ORCID, funding, COI, CRediT (who searched and who screened), acknowledgments | Front and back matter | No (administrative) |

### 7B. Problems the text, data and supplement still have (fixable without new author facts)

1. **Lenient-coding inconsistency** (S. You, Mead, Cho) and the knock-on p = 0.014 (N1). *Must fix.*
2. **Teleoperation and Supervisory labels on studies with no human in the evaluated mission** (Raghavan, Khattab, Ruan), and the missing open-loop rule. IV-A contradicts Table XII (N4, M4). *Must fix.*
3. **Table XX / S7 contradictions with the mode definitions** (Yeoh, Vani, Bhattacharya, Teleoperation rows); exceptions not named (N2). *Must fix.*
4. **Evaluated-human-presence × validation cross-tabulation**, and an explicit circularity statement (N3). *Must fix.*
5. **Route composition of the comparison group** and per-route yields (N5). *Must fix.*
6. **Drew (2021) misquote** (N7); missing Kareem page locator; "apparent shift" sentence; abstract and IV-E novelty overclaims (M7). *Must fix.*
7. **Contribution-type coding for all 39 studies, with a stratified or exact analysis** (M5), or drop the genre interpretation from the Contributions and the Conclusion. *Must fix one way or the other.*
8. **Rigour appraisal** (M9): add a small set of double-codable items (trial count, dispersion, baseline, independence of train and test environments, failure reporting). *Strongly recommended.* It needs human coders to count as double-coded, but the AI-assisted first pass could be done now.
9. **Table XIX enrichment and standards mapping** (M10). *Recommended for JFR fit.*
10. **Supplement hygiene** (M8 residue, N6, N8): "master prompt" in screening-log #61; S3 working notes and undefined "boundary rule A–G"; `fa_cluster_agrees`; `pdf_filename` and `assets/papers/` in the coding manual; internal `.docx`/`.xlsx` paths and session dates in `search_protocol.md`; "human-in-mission" in S5. *Must fix.*
11. **N9, N11, N12** and the unresolved minors (2–6, 8–11, 13, 14, 16, 19–23). *Must fix (quick).*

---

## 8. What would move this to Accept: shortest path, ranked by impact per unit of effort

1. **Fix the coding contradictions and the lenient rule (7B items 1–5).** *Very high impact, 1–2 days.* Recompute everything. This removes the remaining credibility problems in the data the referee can check.
2. **Answer the factual placeholders that cost nothing to answer.** *Very high impact, hours.* The items are dates, the quartile question, the Google Scholar queries, the LLM prompts and versions, journal/English-only, screener identities, who verified the AI output, the AI-use sentence and CRediT. Several are binary confirmations. If the quartile answer is "yes", declare it as a criterion and keep the corpus.
3. **Human blind second coder on mode, human role and validation (strict and lenient), using the existing sheet.** *Very high impact, 2–3 days.* Report κ, AC1 and the confusion matrix. Replace the AI check in the abstract with this.
4. **Text fixes: N7, M7 residue, novelty wording, minors, supplement hygiene.** *Medium–high impact, 1 day.*
5. **Contribution-type coding plus the stratified analysis; evaluated-presence cross-tabulation (N3).** *High impact, 2–3 days.* Either supports the genre hypothesis or retires it.
6. **Database search (Scopus, WoS, IEEE Xplore) with two human screeners and κ, integrated into Fig. 2 and every table.** *Highest impact, 2–4 weeks.* Without it, dimension 2 stays at 1 and the paper is a structured narrative review with PRISMA reporting, not a systematic review. If the authors cannot run it, they should consider retitling the paper honestly (e.g. "a structured review") and targeting a venue where that is acceptable.
7. **Rigour appraisal and Table XIX enrichment mapped to ASTM E54 test methods.** *Medium impact, 2–3 days.*

Items 1–5 would bring this to **Major Revision**. Item 6 is the condition for Minor Revision or Accept at JFR.

---

## 9. Confidential comments to the editor

The authors responded to round 1 in good faith and, on the analysis and framing side, well. The abstract and conclusion no longer oversell, the threats-to-validity section is among the most candid I have reviewed, and the data package is reproducible down to page references. My recommendation is still reject-and-resubmit, for reasons that are mostly in the authors' hands rather than the text's:
- there is no reproducible database search and no search dates;
- every one of 130 cataloged records is from a Q1/Q2 journal, with no statement on whether that was a filter;
- the authors' own supplementary search record describes Google Scholar as "the main database", unlike the Methods;
- there is no human reliability statistic at any stage;
- the AI-use statement still lacks the human-verification sentence, although an AI drafted the text, extracted the data and ran the reliability check.

On the textual side, I found one mis-cited source (Drew 2021: "two of 40" is actually "two of the four multi-robot deployments"). I also found that the only nominally significant field-testing result depends on two validation codes that contradict the paper's own lenient definition. The editor may wish to ask for a point-by-point adjudication log with page evidence at resubmission. The research question is a good fit for JFR, and a resubmission with a real database search and a human second coder would be worth sending out again.

---

### Sources consulted (web and PDF, 2026-11-09)
- [Drew (2021), Multi-agent systems for search and rescue applications, Current Robotics Reports (Utah DRL author copy)](https://drl.ece.utah.edu/wp-content/uploads/sites/155/2021/07/drew-reports2021.pdf). Introduction text checked for the "40 deployments" sentence.
- [Drew (2021), Springer PDF](https://link.springer.com/content/pdf/10.1007/s43154-021-00048-3.pdf)
- [A review on search and rescue robots in complex scenarios: key technologies of SLAM (JFR, 2026; Nottingham Ningbo listing)](https://research.nottingham.edu.cn/en/publications/a-review-on-search-and-rescue-robots-in-complex-scenarios-key-tec/)
- [CiteDrive record, doi:10.1002/rob.70256](https://www.citedrive.com/en/discovery/a-review-on-search-and-rescue-robots-in-complex-scenarios-key-technologies-of-simultaneous-localisation-and-mapping/)
- [Synapse Social listing for the 74-paper 2016–2024 SAR systematic review (Kareem et al.)](https://synapsesocial.com/papers/69a76049c6e9836116a2ce35)

UNVERIFIED in this review: the Kareem et al. (2026a) characterization ("no per-study mode distribution") is still not confirmed from the source by me or by any page reference in the manuscript. My web search (2026-11-09) found no 2025–2026 review that cross-tabulates autonomy mode against validation depth. That is a single standard search, not a full novelty scan.
