# Supplementary File: PRISMA 2020 Checklist

**Review:** *Who Holds the Decisions? A Systematic Review of Autonomy Modes and Validation Depth in Disaster Search-and-Rescue Robotics, 2025–2026* (Avi, Sultana, Sarker).

**Reporting guideline:** Page, M. J., et al. (2021). The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ*, 372, n71. https://doi.org/10.1136/bmj.n71

**How to read this file.**
- Checklist item text is **paraphrased** from PRISMA 2020 Table 1 (item checklist) and Table 2 (abstract checklist). For the authoritative wording, see the official checklist at https://www.prisma-statement.org.
- "Location" points to the manuscript by section, table and figure (Section II = Methods, III = Results, IV = Taxonomy, V = Discussion, VI = Conclusion).
- "Not reported – reason" is given wherever an item is not addressed.
- The column **"Audit note (delete before submission)"** records the status as of the methodology audit of 2026-11-09 (`research_outputs/2026-11-09_methodology-auditor_prisma_audit.md`). R = reported; P = partially reported; M = missing; N/A = not applicable. Remove that column, and resolve every `[[AUTHOR INPUT NEEDED]]` marker, before upload.

---

## Part A. PRISMA 2020 item checklist

| Section / topic | # | Checklist item (paraphrased) | Location in manuscript | Audit note (delete before submission) |
|---|---|---|---|---|
| **TITLE** | | | | |
| Title | 1 | Identify the report as a systematic review. | Title page ("…A Systematic Review of Autonomy Modes and Validation Depth…") | R |
| **ABSTRACT** | | | | |
| Abstract | 2 | Report the abstract according to the PRISMA 2020 for Abstracts checklist. | Abstract; see Part B below | P: no search dates, no funding statement, eligibility criteria and appraisal method not named (Part B items 3, 4, 5, 11) |
| **INTRODUCTION** | | | | |
| Rationale | 3 | Explain why the review is needed, given what is already known. | Section I, paragraphs 1–6; Table I | R |
| Objectives | 4 | State the objective(s) or question(s) explicitly. | Section II-A (RQ1–RQ4); Section I (contributions list) | R |
| **METHODS** | | | | |
| Eligibility criteria | 5 | Give the inclusion and exclusion criteria and how studies were grouped for the syntheses. | Section II-D (C1–C3, publication years); Section II-G (grouping by autonomy/HRI mode); Section II-I (contrast groups) | P: document type and language rule is `[[AUTHOR INPUT NEEDED]]`; journal-quartile question is `[[AUTHOR INPUT NEEDED]]` (all 130 cataloged records carry a Q1/Q2 tag) |
| Information sources | 6 | List every database, register, website, organisation, reference list and other source searched or consulted, with the date each was last searched or consulted. | Section II-B (publisher platforms, Google Scholar, ChatGPT, Gemini); Table II; Fig. 1; Supplementary search protocol, Sec. 1 | P: search dates are `[[AUTHOR INPUT NEEDED]]`. Not reported: dates of searching |
| Search strategy | 7 | Present the full search strategies for every database, register and website, including filters and limits. | Section II-B (query phrases and year limit); Supplementary search protocol, Sec. 1, Table S1 | P: searched fields, platform filters, Google Scholar queries and AI prompts are `[[AUTHOR INPUT NEEDED]]` |
| Selection process | 8 | Describe the methods used to decide eligibility: how many reviewers screened each record and report, whether they worked independently, and any automation tools used. | Section II-E | P: screener identities and disagreement-resolution method are `[[AUTHOR INPUT NEEDED]]`; per-screener decisions not retained (stated); AI post hoc check described |
| Data collection process | 9 | Describe how data were collected from reports: how many collectors, whether independently, any process for obtaining or confirming data from study investigators, and any automation tools used. | Section II-F; AI-use statement | P: who verified the AI-extracted values, and how, is `[[AUTHOR INPUT NEEDED]]`. Not reported: whether study authors were contacted (they were not; add the sentence) |
| Data items | 10a | List and define all outcomes for which data were sought, whether all compatible results were sought, and how results were selected if not. | Section II-F (Table III; validation type; human role; environmental-realism item); Section II-I (primary contrast); Section III-D (strict and lenient field-test codings) | R. Recommended: move the strict/lenient field-test definitions from III-D into II-F |
| Data items | 10b | List and define all other variables sought, and any assumptions made about missing or unclear information. | Section II-F (Table III; clean-category rules); Section II-G | P: no rule stated for missing or unclear information ("not reported" coding, Table X) |
| Study risk of bias assessment | 11 | Specify the methods used to assess risk of bias in included studies: the tool(s), how many reviewers assessed each study, whether independently, and any automation tools. | Section II-H (validation-depth and reproducibility score, VDR) | P: number of assessors, independence and AI involvement not stated. VDR is a validation-depth and reporting-quality appraisal, not a risk-of-bias tool; say so |
| Effect measures | 12 | Specify the effect measure(s) used for each outcome. | Section II-I (proportions with Wilson 95% CIs; odds ratios with exact 95% CIs) | R. Mann–Whitney comparison of VD and RP (Section III-D, III-F) is not declared in II-I |
| Synthesis methods | 13a | Describe how studies were chosen for each synthesis. | Section II-I (all 39 studies; FA vs. human-in-mission grouping); Section II-G | R (recommended: state explicitly that all 39 studies enter every synthesis) |
| Synthesis methods | 13b | Describe any methods used to prepare the data for presentation or synthesis. | Section II-F (clean categories; sensor flags); Section III-D (strict vs. lenient coding) | P: strict/lenient coding defined only in Results |
| Synthesis methods | 13c | Describe any methods used to tabulate or visually display results. | Tables VI–XVIII; Figs. 3–7 | P: the tabulation approach (cross-tabulation by mode; Wilson intervals in Fig. 6) is not described in II-I |
| Synthesis methods | 13d | Describe the synthesis methods and the rationale for them; for meta-analysis, the model, heterogeneity methods and software. | Section II-I (descriptive synthesis; Fisher's exact; Freeman–Halton; exploratory status) | P: software and version (Python, SciPy) not named; Mann–Whitney and the Fisher tests in III-F not declared |
| Synthesis methods | 13e | Describe any methods used to explore possible causes of heterogeneity. | Not reported – no meta-analysis or pooled effect was estimated; platform and scenario cross-tabulations (Section III-B, III-D, III-E) are descriptive | N/A, but state it in II-I |
| Synthesis methods | 13f | Describe any sensitivity analyses used to assess the robustness of the synthesized results. | Section II-I (a)–(c); Section III-G, Table XVII | P: **inconsistent**. II-I lists three analyses, and its (a) is "excluding papers that model no human role"; Table XVII reports four, and its (a) is "physical platform only", with (d) "two possibly misexcluded records" not pre-announced |
| Reporting bias assessment | 14 | Describe any methods used to assess risk of bias due to missing results in a synthesis (reporting biases). | Not reported – not assessed | M: add a statement (see audit report, drop-in D7) |
| Certainty assessment | 15 | Describe any methods used to assess certainty (or confidence) in the body of evidence for an outcome. | Not reported – no formal certainty framework was applied | M: add a statement (see audit report, drop-in D7) |
| **RESULTS** | | | | |
| Study selection | 16a | Describe the results of the search and selection process, from records identified to studies included, ideally with a flow diagram. | Section II-K; Fig. 2 (PRISMA flow diagram); Table V | P: Fig. 2 "records identified" are the records the searcher chose to catalog, not the number of hits each search returned; raw hit counts are `[[AUTHOR INPUT NEEDED]]` or must be declared as not recorded |
| Study selection | 16b | Cite studies that might appear to meet the inclusion criteria but were excluded, and explain why. | Section II-D (Rajashekhar & Prabhakar, 2026); Section V-D (records #70 and #83, by catalog number only); Supplementary screening log (all 86 exclusions with reasons) | P: cite #70 and #83 by reference, not by catalog number |
| Study characteristics | 17 | Cite each included study and present its characteristics. | Section IV (every included study cited); Tables VI–XVI (aggregate); Supplementary extraction table (`extraction_table.csv`, per-study, page-referenced) | P: no per-study characteristics table in the article or in a named supplementary table |
| Risk of bias in studies | 18 | Present assessments of risk of bias for each included study. | Section III-F (VDR means by mode); per-study VD, RP and VDR scores are in the supplementary extraction table (columns `vd`, `rp`, `vdr`) | P: name the per-study table in the text (proposed Supplementary Table S3) |
| Results of individual studies | 19 | For all outcomes, present for each study the summary statistics and an effect estimate with its precision. | Section IV (narrative per-study results); Supplementary extraction table (per-study codes, key metric) | P: per-study outcome codes are only in the supplementary CSV; reference it from Section III |
| Results of syntheses | 20a | For each synthesis, briefly summarise the characteristics and risk of bias of the contributing studies. | Section III-D (Table XII: human role, mean VD per mode); Section III-F (VDR and RP by mode) | R |
| Results of syntheses | 20b | Present results of all statistical syntheses, with precision and the direction of effect. | Section III-A–III-F; Tables VI, XII, XIII; Fig. 6 | R |
| Results of syntheses | 20c | Present results of all investigations of possible causes of heterogeneity. | Section III-B and III-D (Tables VIII and XIV, descriptive); Section III-E | N/A (no pooled effect); descriptive cross-tabulations reported |
| Results of syntheses | 20d | Present results of all sensitivity analyses. | Section III-G; Table XVII; Section III-D (lenient coding) | R (but see 13f inconsistency) |
| Reporting biases | 21 | Present assessments of risk of bias due to missing results for each synthesis. | Not reported – not assessed | M |
| Certainty of evidence | 22 | Present assessments of certainty (or confidence) in the body of evidence for each outcome. | Not reported – not assessed | M |
| **DISCUSSION** | | | | |
| Discussion | 23a | Give a general interpretation of the results in the context of other evidence. | Section V-A, V-B; Section IV-E | R |
| Discussion | 23b | Discuss limitations of the evidence included in the review. | Section V-C; Section V-D (construct and external validity) | R |
| Discussion | 23c | Discuss limitations of the review processes used. | Section V-D (internal and conclusion validity); Abstract; Section VI | R |
| Discussion | 23d | Discuss implications for practice, policy and future research. | Section V-E, V-F; Section VI | R |
| **OTHER INFORMATION** | | | | |
| Registration and protocol | 24a | Give registration information, including register name and number, or state that the review was not registered. | Section II-J; Abstract | R (confirmation is `[[AUTHOR INPUT NEEDED]]`). If a retrospective OSF record is created, cite it as retrospective |
| Registration and protocol | 24b | Indicate where the protocol can be accessed, or state that a protocol was not prepared. | Section II-J ("no protocol was published in advance") | P: state whether a protocol was prepared at all |
| Registration and protocol | 24c | Describe and explain any amendments to information provided at registration or in the protocol. | Section II-J (criteria and coding rules refined during screening and extraction) | P: list the specific amendments (dropped year criterion; strict/lenient coding chosen after tabulation; VDR appraisal and sensitivity analyses added post hoc; extraction table rebuilt) |
| Support | 25 | Describe sources of financial or non-financial support for the review and the role of funders. | Back matter, Funding | M: placeholder `[[AUTHOR INPUT NEEDED]]` |
| Competing interests | 26 | Declare any competing interests of review authors. | Back matter, Conflict of interest | M: placeholder `[[AUTHOR INPUT NEEDED]]` |
| Availability of data, code and other materials | 27 | Report which of the following are publicly available and where: template data collection forms, extracted data, data used for all analyses, analytic code, any other materials. | Back matter, Data availability statement (screening log, extraction table, coding manual, search record, second-coder sheet, scripts) | P: repository DOI is `[[AUTHOR INPUT NEEDED]]`; name each file; the screening log holds only final (consensus) decisions |

---

## Part B. PRISMA 2020 for Abstracts checklist

| Section / topic | # | Checklist item (paraphrased) | Reported in abstract? | Audit note (delete before submission) |
|---|---|---|---|---|
| Title | 1 | Identify the report as a systematic review. | Yes (title) | R |
| Objectives | 2 | State the main objective(s) or question(s) the review addresses. | Partly: "their autonomy and validation have not been reviewed together" implies the objective | P: add one explicit objective sentence |
| Eligibility criteria | 3 | Specify the inclusion and exclusion criteria. | Partly: "three eligibility criteria" and years 2025–2026, criteria not named | P |
| Information sources | 4 | Specify the information sources (e.g. databases, registers) and the date each was last searched. | Partly: routes named (publisher platforms, Google Scholar, AI-assisted discovery); no dates | P: dates `[[AUTHOR INPUT NEEDED]]` |
| Risk of bias | 5 | Specify the methods used to assess risk of bias in included studies. | Partly: "validation depth … and reproducibility were coded" | P: name the VDR appraisal |
| Synthesis of results | 6 | Specify the methods used to present and synthesise results. | Partly: "exploratory Fisher" tests | P: add "descriptive synthesis with Wilson 95% CIs; exploratory Fisher's exact tests" |
| Included studies | 7 | Give the total number of included studies and participants and summarise relevant characteristics. | Yes: 39 studies; mode distribution (participants not applicable) | R |
| Synthesis of results | 8 | Present results for main outcomes, with the number of studies, summary estimates, confidence intervals and direction of effect. | Yes: 40.7% vs 83.3%; 7.4% (95% CI 2.1–23.4) vs 33.3%; 11.1% vs 50.0%; p-values | R |
| Limitations of evidence | 9 | Summarise the main limitations of the evidence (e.g. risk of bias, inconsistency, imprecision). | Partly: review-process limitations listed; evidence limitations (small cells, idealized test conditions) only implicit | P |
| Interpretation | 10 | Give a general interpretation of the results and important implications. | Yes (final sentence) | R |
| Funding | 11 | Specify the primary source of funding for the review. | No | M: add "Funding: none" or the funder `[[AUTHOR INPUT NEEDED]]` |
| Registration | 12 | Give the register name and registration number. | Yes: "The review was not registered." | R (if a retrospective OSF record is created, add "registered retrospectively, OSF [DOI]") |

---

*Prepared 2026-11-09 from `SAR_review_master_document.md` Secs. 9–14 (the only manuscript source). No manuscript text was edited.*
