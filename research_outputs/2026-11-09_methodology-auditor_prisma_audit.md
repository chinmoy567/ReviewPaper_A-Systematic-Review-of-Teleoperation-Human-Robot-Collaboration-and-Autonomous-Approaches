# Methodology audit: PRISMA 2020, PRISMA-S, PRISMA-Abstracts, and AMSTAR-2-style appraisal

- **Date:** 2026-11-09
- **Agent:** methodology-auditor
- **Manuscript source:** `SAR_review_master_document.md`, Secs. 9–14 (manuscript Sections I–VI, Abstract, back matter), as rewritten on 2026-11-08/09. The retired `.tex` and PDF were not opened.
- **Target venue:** *Journal of Field Robotics* (Wiley).
- **Process facts (confirmed by the authors, relayed by the caller):** one searcher; publisher platforms 78, Google Scholar 15, ChatGPT 34, Gemini 3; two screeners with no per-screener records; AI-assisted extraction and drafting.
- **Evidence also used:**
  - `assets/docs/paperlinks.xlsx` (column "How it was found", the quartile column);
  - `supplementary/screening_log.csv`;
  - `assets/docs/Paper Screening Process.docx`, `Paper Selection Process.docx`;
  - `data/extraction_table.csv`, `data/analysis.py`;
  - `assets/figures/prisma_diagram_v2.png`;
  - the PRISMA 2020 checklist, read from PMC8005924 (Page et al., 2021), and the PRISMA-S checklist, read from PMC7839230 (Rethlefsen et al., 2021).
- **Files produced:**
  - `supplementary/PRISMA_2020_checklist.md` (27 items with sub-items, plus the 12 abstract items);
  - `supplementary/PRISMA-S_checklist.md` (16 items);
  - `supplementary/search_protocol.md` (the search as run, plus a specified Scopus/WoS/IEEE supplementary search, deduplication, screening, κ, and PRISMA integration);
  - this report.
- **Master document:** not edited.

---

## 0. Bottom line

The rewritten Methods section is now **honest**. It no longer claims three independent searchers or screeners, it reports Google Scholar and AI-assisted discovery as identification routes, and it reports registration, screener records and AI extraction as limitations. That removes the integrity risk. What remains is **completeness and rigor**:

1. **No search dates** anywhere. This is required by PRISMA 2020 items 6 and 2 (abstract) and PRISMA-S item 13.
2. **The flow diagram's "records identified" are records the searcher chose to catalog, not search hits.** For example, the Wiley "rescue robot" 2025+ search is recorded as yielding 1 record, and MDPI as 34. Behind those numbers is an unreported title-level selection step, done by one person. It must either be quantified or declared.
3. **All 130 cataloged records are Q1/Q2** (66 Q1, 64 Q2; no Q3, Q4 or unranked). This is strong circumstantial evidence of an unreported quartile filter. II-B currently says quartile was "not used to decide inclusion" `[[AUTHOR INPUT NEEDED]]`. The authors must answer this truthfully before submission.
4. **Methods and Results disagree on the sensitivity analyses** (II-I lists three; Table XVII reports four, and its (a) is a different analysis). Mann–Whitney and two further Fisher tests are used in Results but not declared in II-I.
5. **Items 14/21 (reporting bias) and 15/22 (certainty) are missing.** Funding and competing interests are placeholders.
6. **AMSTAR-2-style confidence: critically low**, because of two critical-domain flaws (no a priori protocol; non-comprehensive, partly non-reproducible search). This is typical of engineering SLRs and is fully disclosed. JFR reviewers will judge it on transparency. Running the supplementary database search (search protocol, Sec. 2) is the single change that would move the rating most.

---

## 1. PRISMA 2020 item table

Key:
- **R** = reported; **P** = partial; **M** = missing; **N/A** = not applicable.
- "Where" gives the manuscript section, with the master-document section in brackets.
- The submission-ready version is `supplementary/PRISMA_2020_checklist.md`.

| # | Item | Status | Where | Minimal fix |
|---|---|---|---|---|
| 1 | Title identifies SR | R | Title [§14] | — |
| 2 | Abstract per PRISMA-A | P | Abstract [§14] | See Sec. 3; drop-in D9 |
| 3 | Rationale | R | I, Table I [§13] | — |
| 4 | Objectives | R | II-A RQ1–RQ4 [§9]; I contributions | — |
| 5 | Eligibility criteria, grouping | P | II-D, II-G, II-I [§9] | Confirm document type and language; answer the quartile question; D2 |
| 6 | Information sources and dates | P | II-B, Table II, Fig. 1 [§9]; search protocol Table SP-1 | **Add search dates**; D1 |
| 7 | Full search strategy | P | II-B; search protocol Table SP-1 | Fields, filters, GS queries, AI prompts; D1 |
| 8 | Selection process | P | II-E [§9] | Screener identities; disagreement resolution ("averaged out" must be explained); D3 |
| 9 | Data collection process | P | II-F; AI-use statement [§9, §14] | Who verified AI extraction and how; "study authors not contacted"; D4 |
| 10a | Outcomes defined | R | II-F, II-I; strict/lenient only in III-D | Move strict/lenient definitions into II-F; D4 |
| 10b | Other variables; missing-data assumptions | P | II-F, Table III | Add the "not reported" rule; D4 |
| 11 | RoB method (tool, assessors, independence, automation) | P | II-H [§9] | State assessor (AI single stream plus a human check?); say VDR is not a RoB tool; D5 |
| 12 | Effect measures | R | II-I | Add Mann–Whitney; D6 |
| 13a | Studies per synthesis | R | II-I | One sentence: all 39 studies in every synthesis |
| 13b | Data preparation | P | II-F; III-D | Strict/lenient rule in Methods; D4 |
| 13c | Tabulation and visualization | P | Tables VI–XVIII, Figs. 3–7 | One sentence in II-I; D6 |
| 13d | Synthesis methods, software | P | II-I | Name Python/SciPy versions; declare all tests; D6 |
| 13e | Heterogeneity methods | N/A | — | State "no pooled effect; cross-tabulations descriptive"; D6 |
| 13f | Sensitivity analyses | P (**inconsistent**) | II-I (a–c) vs. Table XVII (a–d) | Align; D6 |
| 14 | Reporting-bias methods | M | — | D7 |
| 15 | Certainty methods | M | — | D7 |
| 16a | Flow and diagram | P | II-K, Fig. 2, Table V | Raw hits not given; relabel the identification boxes; D1, D3 |
| 16b | Near-miss exclusions cited | P | II-D (Rajashekhar & Prabhakar); V-D (#70, #83 by number) | Cite #70 and #83 as references with reasons; D3 |
| 17 | Characteristics of each study | P | IV (all cited); S2 per-study CSV | Cite S2 (`S2_extraction_table.csv`) in III as the per-study table |
| 18 | RoB per study | P | III-F (means only); S2 columns `vd`, `rp` | Cite S2 for per-study VDR in III-F |
| 19 | Individual study results | P | IV narrative; CSV | Reference the CSV from III |
| 20a | Characteristics/RoB of contributing studies | R | Table XII; III-F | — |
| 20b | Synthesis results with precision | R | III-A–F; Tables VI, XII, XIII; Fig. 6 | — |
| 20c | Heterogeneity results | N/A | Tables VIII, XIV (descriptive) | — |
| 20d | Sensitivity results | R | III-G, Table XVII | Align with II-I |
| 21 | Reporting biases | M | — | D7 (Results/Discussion sentence) |
| 22 | Certainty of evidence | M | — | D7 (Supplementary Table S7, confidence ratings) |
| 23a | Interpretation | R | V-A, V-B, IV-E | — |
| 23b | Limitations of evidence | R | V-C, V-D | — |
| 23c | Limitations of the review | R | V-D; Abstract; VI | — |
| 23d | Implications | R | V-E, V-F, VI | — |
| 24a | Registration | R | II-J; Abstract | Confirm; optional retrospective OSF record; D8 |
| 24b | Protocol access | P | II-J | State whether a protocol was prepared at all; D8 |
| 24c | Amendments | P | II-J (general) | List them; D8 |
| 25 | Support | M (placeholder) | Back matter | Author input |
| 26 | Competing interests | M (placeholder) | Back matter | Author input |
| 27 | Data, code, materials | P | Data availability statement | Repository DOI; list exact files; D10 |

**Tally (42 rows):** R 14 (1, 3, 4, 10a, 12, 13a, 20a, 20b, 20d, 23a–d, 24a); P 20 (2, 5, 6, 7, 8, 9, 10b, 11, 13b, 13c, 13d, 13f, 16a, 16b, 17, 18, 19, 24b, 24c, 27); M 6 (14, 15, 21, 22, 25, 26); N/A 2 (13e, 20c).

---

## 2. PRISMA-S item table

The submission-ready version is `supplementary/PRISMA-S_checklist.md`.

| # | Item | Status | Where | Minimal fix |
|---|---|---|---|---|
| 1 | Database / platform names | R | II-B item 1 | URLs given in Table SP-1 |
| 2 | Multi-database platforms | N/A | — | — |
| 3 | Registries | R (none) | II-B | — |
| 4 | Online resources / browsing | P | — | One sentence "none browsed" (confirm) |
| 5 | Citation searching | R (none) | II-B | — |
| 6 | Contacts | M | — | One sentence "none contacted" (confirm) |
| 7 | Other methods | P | II-B item 2; AI-use statement | Prompts, model versions, dates; count of rejected/hallucinated suggestions |
| 8 | Full strategies, exactly as run | P | II-B; Table SP-1 | Field searched, filters; GS queries (the catalog shows "rescue robot", 8, and "disaster rescue robot", 7); prompts |
| 9 | Limits and restrictions | P | II-B, II-D | Language, document type, **quartile**; justify the 2025 start in II-B |
| 10 | Search filters | M | — | "No published filters used" |
| 11 | Prior work | M | — | "No strategy reused" |
| 12 | Updates | M | — | "Not updated", or run search-protocol Sec. 2 |
| 13 | Dates of searches | **M (critical)** | — | Dates per source |
| 14 | Peer review of search | M | — | "Not peer reviewed"; PRESS for the new search |
| 15 | Total records per source | P | Table II, Figs. 1–2 | Counts are **cataloged**, not **retrieved**; give hits or say they were not recorded |
| 16 | Deduplication | R | II-C | Say whether manual or scripted |

**Tally (16 items):** R 4 (1, 3, 5, 16); N/A 1 (2); P 5 (4, 7, 8, 9, 15); M 6 (6, 10, 11, 12, 13, 14). Items 6, 10, 11, 12 and 14 can each be fixed with one truthful sentence (drop-in D1).

---

## 3. PRISMA 2020 for Abstracts

| # | Item | Status | Fix |
|---|---|---|---|
| 1 | Title | R | — |
| 2 | Objectives | P | Explicit objective sentence |
| 3 | Eligibility | P | Name C1–C3 briefly |
| 4 | Sources and dates | P | Add date of last search |
| 5 | Risk of bias | P | Name the VDR appraisal |
| 6 | Synthesis methods | P | "Wilson CIs; exploratory Fisher tests" |
| 7 | Included studies | R | — |
| 8 | Synthesis results | R | — |
| 9 | Limitations of evidence | P | Already partly covered; acceptable once item 6 is added |
| 10 | Interpretation | R | — |
| 11 | Funding | M | Add |
| 12 | Registration | R | — |

Drop-in D9 is a revised abstract of about 250 words (the current one is 249) that fixes items 2–6 and 11. JFR's abstract word limit is **UNVERIFIED**: the journal-scout notes found no official limit, and a third-party source says 150–250.

---

## 4. Internal inconsistencies and audit-trail discrepancies

Each was checked against the files named.

| # | Finding | Evidence | Severity | Action |
|---|---|---|---|---|
| X1 | **Sensitivity analyses: Methods ≠ Results.** II-I promises (a) "excluding papers whose evaluated setup models no human role", (b) RP ≥ 2, (c) boundary re-coding. Table XVII reports (a) "physical platform only (excludes abstract agents and sensor-free simulations)", (b), (c), and an unannounced (d) "two possibly misexcluded records". III-G says II-I's (a) could not be estimated (1/27 FA studies models a human). | §9 II-I vs. §10 III-G | Major (a reviewer will notice) | D6 rewrites II-I to list the four analyses actually run, and states that the planned human-role subgroup analysis could not be estimated |
| X2 | Tests used in Results but not declared in Methods: Mann–Whitney (VD p = 0.024; RP p = 0.83); Fisher for generic vs. hazard-specific realism (p = 0.30); the VD = 3 outcome row in Table XIII. | §10 III-D, III-F; `data/analysis.py` imports `mannwhitneyu` | Moderate | D6 |
| X3 | **Cataloged ≠ identified.** Fig. 2 and Table II give 78 "records identified from publisher platforms". The catalog shows single queries yielding small counts (Wiley 1, Frontiers 4, IEEE Xplore 5), which cannot be the platforms' full result counts for "rescue robot", 2025+. An unreported title-level selection by one person sits before Fig. 2's first box. | `paperlinks.xlsx` col. D | **Major** (PRISMA 16a; PRISMA-S 15) | D1 discloses it; relabel the Fig. 2 boxes "records cataloged from…", with a footnote "total hits not recorded" if they were not |
| X4 | **Quartile.** Every cataloged record is tagged Q1 (66) or Q2 (64). II-B says ranking was not used `[[AUTHOR INPUT NEEDED: confirm]]`. A Gate-1 statement "quartile used as a filter" went unticked by the authors (Sec. 16 entry 1), which does not confirm it was *not* used. | `paperlinks.xlsx` col. B; §16 | **Major if a filter was used and not reported** (an undisclosed eligibility restriction) | The authors must answer. If quartile guided cataloging, add it to II-D as a restriction, and to V-D (bias toward high-visibility venues). If not, say how an all-Q1/Q2 catalog arose |
| X5 | **Google Scholar queries.** The authors' `Paper Selection Process.docx` calls Google Scholar "the main database" and lists 7 queries. The catalog attributes only 15 records to Google Scholar, under 2 queries ("rescue robot", 8; "disaster rescue robot", 7). The authors' confirmed split (78/15/34/3) matches the catalog. | docx vs. xlsx | Moderate | II-B: report the 2 queries that yielded cataloged records, and state whether the other 5 were run (`[[AUTHOR INPUT NEEDED]]`) |
| X6 | "Averaged out" (screening docx) is not a valid way to reconcile include/exclude decisions. II-E already flags it as `[[AUTHOR INPUT NEEDED]]`. | `Paper Screening Process.docx` | Moderate | D3 template |
| X7 | II-F says "Five fields were reduced to single clean categories", but one of the five (Sensor Suite) is multi-hot flags, not a single category. | §9 II-F | Minor | "Four fields were reduced to single categories and one to flags" |
| X8 | II-H attributes the VDR score's origin to "the 1–6 quality score of Kareem et al. (2026a)". No project file verifies that Kareem et al. report a 1–6 quality score: §8A, the verified summary, does not mention one, and the idea first appears as a suggestion in `2026-11-08_full_paper_audit.md`. **UNVERIFIED.** | §8A; research_outputs | Moderate (citation accuracy) | citation-verifier to check against the Kareem PDF; otherwise reword as "purpose-built for this review" (D5 does this) |
| X9 | Exclusion counts by route (Fig. 2) vs. totals (Table V): **consistent.** Platforms: C1 42 / C2 21 / C3 3, 7 multi → 59. Other methods: 21 / 7 / 4, 5 multi → 27. Total 63 / 28 / 7, 12 multi → 86. Recomputed from `screening_log.csv` (125 rows; 39 included, 86 excluded; pairs C1+C2 6, C2+C3 5, C1+C3 1). | CSV, recomputed | OK | Suggest also giving **mutually exclusive primary reasons** (hierarchy C1 > C2 > C3, which matches the "ordered by importance" in the screening docx): C1 63, C2 22, C3 1 (= 86). Platforms 42/17/0; other methods 21/5/1 |
| X10 | Table II row and column sums, the Fig. 2 per-platform list (ScienceDirect 20 = 18 + 2 Tech Science Press), duplicates (1 + 4), and inclusions by route (18 + 21) all reconcile. | Table II, Fig. 2, xlsx | OK | — |
| X11 | II-E notes "Rajashekhar & Prabhakar (2026)" as excluded; its duplicate (#12 of #4) was removed at deduplication. | docx duplicate table | OK | — |
| X12 | Inclusion yield differs by route: other methods 21/48 (43.8%) vs. publisher platforms 18/77 (23.4%). AI and Google Scholar suggestions were more "on target", which is consistent with a visibility-biased route. | recomputed | Interpretive | Worth one clause in V-D (internal validity); supports the coverage concern |
| X13 | CLAUDE.md "Locked facts" (screening 18–19 July 2026; FA 2/27 vs 60–75%; UAV 1/13 vs Hybrid 4/7; 35/39) are superseded in the manuscript by Sec. 16 entry 6 (the realism figure is now 26/39; UAV 3/13 vs Hybrid 3/7). The manuscript is internally consistent with entry 6. | §16 | Housekeeping | The authors or caller should update CLAUDE.md's locked-facts block; I did not edit it |
| X14 | The Data availability statement lists "the search record", but none existed in `supplementary/` before today. `search_protocol.md` now covers it. The extraction table and scripts are in `data/`, not `supplementary/`. | file listing | Minor | D10 lists the actual file names |
| X15 | Landis & Koch (1977) and the PRESS guideline are needed if D3 and the search protocol are adopted, but are not in the reference list. | §15 | Minor | Add after citation-verifier checks them |

---

## 5. Rigor criteria rating

| Criterion | Rating | Basis |
|---|---|---|
| Protocol registration | **Absent** (disclosed) | II-J: not registered, no protocol published. A retrospective OSF record would improve transparency, not rigor; it must be labelled retrospective (D8) |
| Comprehensive, reproducible search | **Weak** | 2 phrases on 7 publisher platforms; no Scopus or WoS; no citation chasing; 37/130 records (and an unknown share of the 21 other-route inclusions) came from non-reproducible LLM suggestions; no dates; hits not recorded |
| Dual independent screening | **Claimed but unverifiable** | Two screeners, but per-screener decisions were not kept and the reconciliation method is unclear ("averaged out") |
| Inter-rater agreement statistic | **Partial, AI only** | Screening: none. Mode coding: AI vs. original κ = 0.79 (Gwet AC1 0.88), honestly labelled as not human–human. The blind human second-coder sheet (`supplementary/human_second_coder_sheet.csv`) is ready but not yet completed |
| Quality / risk-of-bias appraisal | **Partial** | VDR (validation depth plus reproducibility) is a sensible, field-appropriate appraisal and is used in a sensitivity analysis. It is not a risk-of-bias tool, it is not validated, and it was coded by a single AI stream |
| Sensitivity analysis | **Good** | Four analyses, plus strict/lenient coding and the boundary re-coding; results reported honestly, including attenuation. Needs alignment with Methods (X1) |
| Data and code availability | **Good, pending deposit** | Screening log, page-referenced extraction CSV, coding manual and scripts exist. Repository DOI pending. Per-screener and per-extractor raw data do not exist |
| Statistical reporting | **Good** | Wilson CIs, exact ORs, explicit exploratory label, no multiplicity claims. Needs software versions and full test declaration |

---

## 6. AMSTAR-2-style appraisal

AMSTAR 2 (Shea et al., 2017, *BMJ*, 358, j4008) was designed for reviews of healthcare interventions. It is applied here only as a structured heuristic for the review's main weaknesses; items 11, 12 and 15 assume a meta-analysis. Critical domains are marked ★.

| AMSTAR 2 item | Rating | Reason |
|---|---|---|
| 1. Research questions and inclusion criteria include the components of the question | Yes | RQ1–RQ4 and C1–C3 define population (SAR robotic systems), "intervention" (autonomy mode), and outcomes (validation depth) |
| 2★. Methods established before the review; deviations justified | **No** | No protocol and no registration; criteria and coding rules refined during the review; strict/lenient coding and tests chosen after tabulation (disclosed) |
| 3. Selection of study designs explained | Yes | C3 (empirical evaluation) is justified |
| 4★. Comprehensive literature search | **No** | Fewer than 2 bibliographic databases; 2 short phrases; no citation chasing; no grey literature; AI-assisted discovery is non-reproducible; no dates. ("Partial yes" needs at least 2 databases with keywords and a justified restriction) |
| 5. Study selection in duplicate | **Partial / unverifiable** | Two screeners are reported, but there is no record of independent decisions or of a consensus method |
| 6. Data extraction in duplicate | **No** | Single AI extraction stream; human verification is `[[AUTHOR INPUT NEEDED]]`; the original workbook was lost and the table rebuilt |
| 7★. List of excluded studies with justification | **Yes** | `screening_log.csv`: all 86 exclusions with reasons, provided the file is released as stated |
| 8. Included studies described in adequate detail | Partial yes | Aggregate tables plus a per-study CSV; no per-study table referenced in the article |
| 9★. Satisfactory technique for assessing RoB in individual studies | **Partial** | VDR addresses validation depth and reproducibility, the main bias concerns for engineering evaluations, but it is unvalidated, single-coded, and does not cover selective outcome reporting or comparator fairness |
| 10. Funding sources of included studies reported | No | Not extracted |
| 11★. Appropriate statistical combination | N/A | No meta-analysis. The exploratory tests are appropriate for the counts (Fisher exact, Wilson) |
| 12. Impact of RoB on synthesis assessed | Yes | Sensitivity (b) RP ≥ 2; (a) physical-platform restriction |
| 13★. RoB accounted for when interpreting results | Yes | V-A and V-D interpret the attenuation and the confounding; claims are downgraded to "exploratory" |
| 14. Heterogeneity explained | Yes | Research-genre explanation, supported by sensitivity (a) and the FA cluster table |
| 15★. Publication bias investigated | **No** (N/A in the strict sense) | No discussion of the bias toward successful, simulation-only demonstrations, or of unpublished field failures (item 14/21 gap) |
| 16. Conflicts of interest of the review reported | Pending | Placeholder |

**Overall confidence (AMSTAR 2 rule: more than one critical flaw gives "critically low"): CRITICALLY LOW**, driven by items 2★ and 4★, with 9★ and 15★ weak.

**What moves the rating** (each item is achievable before submission):
- Item 4★ moves to Partial yes once the search-protocol Sec. 2 database search is run, deduplicated and screened, with dates and strings, a recall test and citation chasing. This is the only change that would lift the overall rating out of "critically low", together with item 2★, which cannot be fixed after the fact.
- Item 2★ cannot become "Yes" retrospectively. A retrospective OSF record plus an explicit list of post hoc decisions (D8) is the honest maximum.
- Item 5 moves to "Yes" for the new records if dual blind screening with kept records is used, and the D3 retrospective 30% blind re-screen gives a measured κ for the original corpus.
- Item 6 / reliability: the human blind second coder on mode (sheet ready) plus a human check of a random 20–30% sample of the extracted cells (validation type, VD, RP, realism) with κ.
- Item 15★: add D7.

---

## 7. Ranked fix list (impact × effort)

Impact: H/M/L = effect on a JFR reviewer's assessment. Effort: L = minutes (one sentence), M = hours, H = days.

| Rank | Fix | Impact | Effort | Owner | Drop-in |
|---|---|---|---|---|---|
| 1 | Supply **search dates** (per source, or at least the month and year of the last search) | H | L | Authors | D1 |
| 2 | **Answer the quartile question** truthfully and report it as a restriction if it applied | H | L | Authors | D2 |
| 3 | **Disclose that Fig. 2 counts are cataloged records**, selected by one searcher from result lists; give hit counts or say they were not recorded; relabel the Fig. 2 boxes | H | L–M | Authors, then figure script | D1 |
| 4 | Align the **sensitivity-analysis list** and declare all tests and software (X1, X2) | H | L | Agent (on request) | D6 |
| 5 | Add **reporting-bias and certainty** statements (items 14, 15, 21, 22) and Supplementary Table S7 | M–H | L–M | Agent drafts, authors confirm ratings | D7 |
| 6 | One-sentence PRISMA-S closers: no browsing, no contacts, no filters, no prior strategy, not updated, not peer reviewed | M | L | Authors confirm | D1 |
| 7 | Screener identities and the real reconciliation method; primary-reason exclusion counts; cite #70 and #83 | M | L | Authors | D3 |
| 8 | Who verified the AI extraction, the missing-data rule, no author contact; VDR assessor | M | L | Authors | D4, D5 |
| 9 | Funding, COI, CRediT, repository DOI, file list | M | L | Authors | D10 |
| 10 | Revised abstract (dates, eligibility, appraisal, funding) | M | L | Agent plus authors | D9 |
| 11 | Registration wording plus an amendments list; optional retrospective OSF deposit | M | L–M | Authors | D8 |
| 12 | **Human blind second coder** on mode (sheet ready); report κ with CI, alongside or instead of the AI κ | H | M | One co-author not involved in the original coding | II-G marker |
| 13 | **Retrospective blind 30% re-screen** (12 included + 26 excluded, fixed seed) by two authors; κ with CI and Gwet AC1 | M–H | M | Two authors | D3 option |
| 14 | Human check of a random 30% of extracted cells (validation_strict, vd, rp, env_realism, human_role) with κ | M–H | M | One author | D4 option |
| 15 | **Run the supplementary database search** (Scopus, WoS CC, IEEE Xplore), PRESS review, recall test against the 39, dual screening with kept records, citation chasing; integrate into Fig. 2 and re-run all analyses | **Highest** | H | Authors (database access) | `supplementary/search_protocol.md` |
| 16 | Verify or remove the "Kareem et al. (2026a) 1–6 quality score" attribution (X8) | M | L | citation-verifier | D5 |
| 17 | Cite S2 (`S2_extraction_table.csv`, per-study characteristics and VD/RP) and S3 from III and III-F | M | L | Agent | — |
| 18 | Update the CLAUDE.md locked-facts block (X13) | L (internal) | L | User | — |

Suggested order: 1–11 this week (text only); 12–14 in parallel (human effort, 1–2 days); 15 decides the review's standing and should be done before submission if any author has Scopus or WoS access.

---

## 8. Drop-in Markdown for Section II (and the Abstract)

These are templates. Every `[[AUTHOR INPUT NEEDED]]` must be resolved by the authors, and no sentence below may be kept if the authors cannot confirm it. They are for the master document's §9 and §14. I have not inserted them; log each insertion in §16.

### D1. II-B, new paragraph after the numbered list (search details and PRISMA-S closers)

> The searches were run between [[AUTHOR INPUT NEEDED: date]] and [[AUTHOR INPUT NEEDED: date]]; the last search of each source is dated in Table SP-1 of the supplementary search protocol. On each publisher platform the phrase was searched in [[AUTHOR INPUT NEEDED: all fields / title, abstract and keywords]], with the publication-year filter set to 2025 onward [[AUTHOR INPUT NEEDED: any other filter, e.g. article type]]. The number of results each search returned [[AUTHOR INPUT NEEDED: is given in Table SP-1 / was not recorded]]. The searcher selected records for cataloging from the result lists on the basis of [[AUTHOR INPUT NEEDED: title / title and abstract]] relevance to disaster SAR robotics [[AUTHOR INPUT NEEDED: state any other rule applied at this step, including journal quartile]]. This selection was made by one person and was not checked independently, so Fig. 2 counts records cataloged, not all records retrieved. The Google Scholar queries that yielded cataloged records were "rescue robot" (8 records) and "disaster rescue robot" (7 records) [[AUTHOR INPUT NEEDED: confirm, and state whether the other queries in the authors' search record were run]]. No published search filters were used, no search strategy from another review was reused, and the strategy was not peer reviewed. No journal tables of contents, conference proceedings, or websites were browsed, no study authors or experts were contacted, and the searches were not updated [[AUTHOR INPUT NEEDED: confirm each clause]].

Also relabel Fig. 2's identification boxes "Records cataloged from publisher-platform searches (n = 78)" and "Records cataloged from other methods (n = 52)". If hit counts were not recorded, add a footnote saying so.

### D2. II-D, replace the last sentence ("Peer-reviewed journal articles in English were eligible […]")

Option A, if quartile was **not** used:

> Only peer-reviewed journal articles in English were eligible [[AUTHOR INPUT NEEDED: confirm]]. Journal ranking was not used at any stage. All cataloged records happen to appear in journals ranked Q1 or Q2 [[AUTHOR INPUT NEEDED: by SJR/JCR, year]], which reflects the sources searched rather than a selection rule [[AUTHOR INPUT NEEDED: only if true]].

Option B, if quartile **was** used:

> Only peer-reviewed journal articles in English, in journals ranked Q1 or Q2 in [[AUTHOR INPUT NEEDED: SJR or JCR, year]], were cataloged. The quartile restriction was applied by the searcher when selecting records from search results. It is not a quality criterion and may exclude eligible studies published in lower-ranked or unranked venues (Section V-D).

If Option B applies, add to V-D (internal validity): "Restricting cataloging to Q1/Q2 journals may bias the corpus toward high-visibility venues."

### D3. II-E, replace the `[[AUTHOR INPUT NEEDED]]` marker and extend Table V

> The two screeners were [[AUTHOR INPUT NEEDED: initials]] and [[AUTHOR INPUT NEEDED: initials]]. Disagreements were resolved by [[AUTHOR INPUT NEEDED: discussion until consensus / decision by a third author, initials]]. Only the consensus decision was recorded.

Then add a "Primary reason" column to Table V, with the caption sentence: "Primary reason assigns each excluded record to its first failed criterion in the order C1, C2, C3, so the column sums to 86."

| Criterion violated | n (non-exclusive) | n (primary reason) |
|---|---|---|
| C1, not disaster SAR domain | 63 | 63 |
| C2, no active robotic SAR role | 28 | 22 |
| C3, no empirical evaluation | 7 | 1 |
| Total | 98 | 86 |

These values were recomputed from `supplementary/screening_log.csv`. By route: publisher platforms 42/17/0; other methods 21/5/1.

16b: in V-D, replace "two exclusions (#70 and #83)" with the two papers' author–year citations and add them to the reference list `[[AUTHOR INPUT NEEDED: bibliographic details of catalog records 70 and 83 from paperlinks.xlsx]]`.

Optional, if rank-13 fix is done:

> As a post hoc check of screening reliability, two authors ([[initials]], [[initials]]) independently re-screened a random sample of 38 of the 125 records (12 included and 26 excluded; random seed [[n]]), blind to the logged decisions and to each other. Agreement between them was [[x]]% (Cohen's κ = [[x]], 95% CI [[x–x]]; Gwet's AC1 = [[x]]), and agreement with the logged decisions was [[x]]%. This check estimates the reproducibility of the criteria; it does not recover the original screeners' agreement.

### D4. II-F, after "[[AUTHOR INPUT NEEDED: which author(s) checked…]]"

> [[AUTHOR INPUT NEEDED: initials]] checked [[every coded cell / a random sample of n cells, stratified by field]] against the full texts. [[If a sample: The checker agreed with the extracted value for x of n cells (κ = x for validation type).]] Study authors were not contacted for missing or unclear information. Information that a paper did not report was coded "not reported" and never inferred. For the validation outcome, a *strict* coding counts as a field test only a physical test at a non-mock outdoor or real site, while a *lenient* coding also counts constructed outdoor courses and competition venues. The strict coding is primary.

Also fix X7: "Four fields were reduced to single categories, and the fifth (Sensor Suite) to independent flags, for counting:"

### D5. II-H, replace the first sentence and append a sentence

> No established risk-of-bias instrument exists for primary studies in robotics engineering. Each included paper was therefore appraised with a two-dimension validation-depth and reproducibility (VDR) score developed for this review. [[Delete "adapted from the 1–6 quality score of Kareem et al. (2026a)" unless citation-verifier confirms that Kareem et al. report such a score.]]

Append:

> VDR addresses how far, and how reproducibly, a system was evaluated. It does not assess other sources of bias, such as selective reporting of outcomes or comparison against weak baselines, and it has not been validated. Scores were assigned by [[AUTHOR INPUT NEEDED: the AI assistant during re-extraction, with page references, and checked by initials / two authors independently]]. Per-study scores are given in Supplementary File S2.

### D6. II-I, replace the paragraph from "All tests were chosen…" to the end of the sensitivity list

> All tests were chosen after the data had been tabulated. They are therefore exploratory, and no correction for multiplicity was applied. Binary outcomes (field test under the strict and lenient codings; any physical test; testing at a mission-representative site) were compared with two-sided Fisher's exact tests. Ordinal scores (validation depth and reproducibility, each 1–3) were compared with two-sided Mann–Whitney U tests. The same Fisher test compared realism acknowledgment between generic and hazard-specific scenarios. All 39 studies contribute to every synthesis. Results are tabulated as cross-tabulations by autonomy mode and shown as proportions with Wilson intervals (Fig. 6). No effect was pooled, so heterogeneity was not modeled statistically, and the platform and scenario cross-tabulations are descriptive.
>
> Four sensitivity analyses test the primary contrast:
> - (a) restricting to studies with a physical platform, which excludes abstract agents and sensor-free simulations;
> - (b) restricting to studies with RP ≥ 2;
> - (c) re-coding the boundary cases identified by the reliability check;
> - (d) adding, as Fully Autonomous simulation-only studies, the two excluded records whose exclusion the post hoc check questioned (Section II-E).
>
> An analysis restricted to studies that model a human role was planned but could not be estimated, because only 1 of 27 Fully Autonomous studies models one. Analyses used Python [[version]] with SciPy [[version]] (`data/analysis.py`).

The versions can be read from the environment that produced `data/analysis_output.md`. UNVERIFIED here.

### D7. New subsection II-L "Reporting Bias and Certainty of Evidence" (Methods), plus a Results sentence and Supplementary Table S7

Methods:

> Risk of bias due to missing results was not assessed formally. Funnel-plot and related methods do not apply to proportions of study characteristics, and unpublished SAR robotics evaluations are not registered anywhere. We judged its likely direction qualitatively: studies with failed or disappointing field trials may go unpublished, which would make the published field-testing rate an overestimate for every mode. No formal certainty framework such as GRADE was applied, because it is designed for intervention effects. Instead, each headline finding received a confidence rating (high, moderate, low, or very low). The ratings were based on the precision of the estimate, its robustness across the sensitivity analyses, the reliability of the coding behind it, and the completeness of the search (Supplementary Table S7).

Results (end of III-G):

> Confidence ratings for the headline findings are given in Supplementary Table S7.

Draft Supplementary Table S7 (ratings are the auditor's proposal; **the authors must confirm or change them**):

| Finding | Precision | Robustness | Coding reliability | Search completeness | Proposed confidence |
|---|---|---|---|---|---|
| FA is the most common mode (27/39, 69.2%, CI 53.6–81.4) | Moderate | n/a | FA vs. other κ = 0.88 (AI vs. original) | Downgrade: non-reproducible, narrow search | Moderate |
| FA studies less often reach any physical test (40.7% vs 83.3%) | Low (OR CI 0.013–0.87) | Holds in (b), (c), (d); attenuates in (a), p = 0.41 | Validation coded by a single AI stream | Downgrade | Low |
| FA studies less often field-tested, strict (7.4% vs 33.3%) | Low (p = 0.060; OR CI crosses 1) | Not robust to (a) and (c) | Strict/lenient boundary depends on judgment | Downgrade | Very low |
| 5/39 release code or data | Moderate | n/a | Objective (link present) | Downgrade | Moderate |
| Two thirds acknowledge idealized conditions (26/39) | Moderate | 33/39 under the broad reading | Author-statement rule, single AI stream | Downgrade | Low |

### D8. II-J, replace the paragraph

> The review protocol was not registered, and no protocol was [[AUTHOR INPUT NEEDED: prepared / published]] before the review began. [[Optional, only if done: "After the analyses were complete, a record describing the methods as conducted was deposited on the Open Science Framework (registered retrospectively on [date]; [DOI]). It is not a prospective protocol."]] The following decisions were made or changed during the review:
> - A fourth criterion, publication in 2025 or later, was dropped as a screening criterion because the search was already limited to those years.
> - The eligibility criteria were operationalized during screening (Section II-D).
> - The autonomy/HRI decision rules were refined during coding (Section II-G).
> - The strict/lenient field-test codings, the VDR appraisal, all statistical tests and the sensitivity analyses were chosen after tabulation.
> - The extraction table was rebuilt from the full texts after the original workbook was lost (Section II-F).

### D9. Abstract, revised (about 250 words; the current abstract is 249; JFR limit UNVERIFIED)

> Robots are increasingly proposed for disaster search and rescue (SAR). We reviewed how autonomy/human-robot interaction modes are distributed in recent SAR robotics and whether validation depth differs by mode. Following PRISMA 2020, one author cataloged 130 records published in 2025–2026 from publisher-platform searches (78), Google Scholar (15), and AI-assisted discovery (37), last searched in [[AUTHOR INPUT NEEDED: month year]]. Two reviewers screened 125 full texts for a primary disaster-SAR application, an operational robotic role, and an empirical evaluation, and 39 studies were included. Each was assigned one of four autonomy modes under explicit decision rules; validation depth and reproducibility were appraised with a purpose-built score. Proportions are reported with Wilson 95% CIs and exploratory Fisher tests. Fully Autonomous systems made up 69.2% of studies (27/39); the rest were Teleoperation (5), Supervisory Control (4), and Shared-Collaborative Control (3). Fully Autonomous studies reached physical testing less often than studies with a human in the mission (40.7% vs. 83.3%; p = 0.018). Their field-testing rate was 7.4% (95% CI 2.1–23.4) vs. 33.3% under strict coding (p = 0.060), and 11.1% vs. 50.0% under lenient coding (p = 0.014). The difference attenuated when abstract-agent and sensor-free simulations were excluded, suggesting an algorithm-first research genre rather than an effect of autonomy itself. Two thirds of studies acknowledged idealized test conditions; 5 of 39 released code or data. Limitations include non-reproducible AI-assisted discovery, a narrow search, unrecorded screener agreement, and AI-assisted extraction. The review was not registered and received [[AUTHOR INPUT NEEDED: no specific funding / funder]]. Autonomy's prevalence should not be read as deployment readiness.

Every number in it was checked against Tables VI, XII, XIII and XVI and III-F. No new numbers were introduced.

### D10. Data availability statement, replace the bullet list (file names follow `supplementary/README.md`)

> The following are available at [[AUTHOR INPUT NEEDED: OSF/Zenodo DOI]] and as supporting information:
> - S1, the screening log for all 125 screened records, with consensus decisions and reasons (`screening_log.csv`; per-screener decisions were not kept);
> - S2, the page-referenced extraction table, including per-study VD and RP scores (`S2_extraction_table.csv`);
> - S3, the per-study classification rationale (`S3_classification_rationale.md`);
> - S4, the coding manual, and a blank second-coder sheet (`coding_manual.md`, `human_second_coder_sheet.csv`);
> - S5, the analysis output (`S5_analysis_output.md`);
> - S6, the AI blind-recoding data (`S6_reliability_blind_codes.csv`);
> - the PRISMA 2020 and PRISMA-S checklists (`PRISMA_2020_checklist.md`, `PRISMA-S_checklist.md`);
> - the search protocol, with the search record (Table SP-1) and the supplementary database strategy (`search_protocol.md`);
> - S7, the confidence ratings for the headline findings (to be created if D7 is adopted);
> - the analysis and figure scripts (`scripts/`).

---

## 9. Questions only the authors can answer (blocking items)

1. The date of each search, or at least the month and year of the last search per source.
2. Were search hit counts recorded? Which field was searched on each platform, and which filters were applied?
3. How were records chosen from result lists for cataloging (title? abstract?), and **was journal quartile used**? All 130 are Q1/Q2.
4. Which Google Scholar queries were actually run? The catalog shows 2; the selection document lists 7.
5. ChatGPT and Gemini: model versions, dates, prompts (or a description), and whether the transcripts survive. How many suggestions were rejected as non-existent or mis-cited?
6. Screener initials, and what "averaged out" meant in practice.
7. Who checked the AI extraction, and how much of it?
8. Who assigned the VDR scores?
9. Document type and language rules (journal-only? English-only?).
10. Funding, COI, CRediT, repository.
11. Whether to run the database search (strongly recommended), and who will act as human second coder and as second re-screener.

---

## Sources

- Page et al. (2021), PRISMA 2020 statement, item and abstract checklists: https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/
- Rethlefsen et al. (2021), PRISMA-S: https://pmc.ncbi.nlm.nih.gov/articles/PMC7839230/
- IEEE Xplore Command Search help: https://ieeexplore.ieee.org/Xplorehelp/searching-ieee-xplore/command-search
- IEEE Xplore search tips (wildcard limits; help versions disagree, so verify at run time): https://ieeexplore.ieee.org/Xplorehelp/searching-ieee-xplore/search-tips
- Library guide to IEEE Xplore command search: https://libguides.ittralee.ie/using-ieee-xplore/command-search
- A web search for a 1–6 quality score in Kareem et al. (2026) returned nothing relevant, so X8 remains UNVERIFIED.
- Not web-verified in this session (send to citation-verifier before citing): Shea et al. (2017) AMSTAR 2; McGowan et al. (2016) PRESS 2015; Haddaway et al. (2022) citationchaser; Landis & Koch (1977).
