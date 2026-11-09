# Q1 readiness report: SAR robotics systematic review (2026-11-09)

**Target venue:** *Journal of Field Robotics* (Wiley), review-paper category. Confirmed by the authors on 2026-11-08.
- **Quartile:** SJR 2025 Q1 in both Computer Science Applications and Control and Systems Engineering (SJR 1.141), verified on scimagojr.com in the user's own browser. JCR quartile is UNVERIFIED (requires a login).
- **Evidence:** `2026-11-08_venue_verification_chrome.md`

**Final simulated decision (Reviewer 2, round 2):** Reject, with encouragement to resubmit. The rubric mean rose from 2.6 to 2.7, and round-3 fixes were applied after that review. The reviewer's stated path is:
- the text and data fixes (now done) plus the author confirmations reach **Major Revision**;
- **Minor Revision or acceptance requires the reproducible database search**, which only the authors can run.

**Status: NOT ready to submit.** 23 `[[AUTHOR INPUT NEEDED]]` markers remain, and integrity items I-1, I-2, I-4, I-8, I-11 and I-12 are blocked on the authors.

## 1. Before/after metrics

| Metric | Before (2026-11-08 audit) | After (2026-11-09) |
|---|---|---|
| Methods describe what was done | No (claimed three-author portal search and screening) | Yes, to the extent the authors have confirmed; gaps marked |
| AI use disclosed | No | Yes (identification, extraction, analysis, drafting), with an AUTHOR INPUT for the verification sentence |
| Reproducible data | Extraction workbook lost | Page-referenced CSV (39 × ~80 columns), analysis and figure scripts, screening log |
| Numbers reproducible from data | Not possible | All reproduce (stats checker, rounds 1–2: no arithmetic mismatches) |
| Inferential statistics | None | Wilson CIs, Fisher and ORs, exact Freeman–Halton, Mann–Whitney, Holm, five sensitivity analyses |
| Headline claims | "Inverse relationship", 89.7% realism gap, UAV mismatch, "not reported previously" | Descriptive findings; FA difference stated as consistent in direction but not established; claims hedged and backed by dated scans |
| Theory grounding | None | Sheridan–Verplank, Parasuraman et al., Endsley & Kaber, Beer et al., ALFUS, Murphy, Yanco & Drury, Kim et al.; mapping table; per-function coding (Table XX) |
| Reliability | None | Post hoc AI blind recoding (κ = 0.79, labelled as AI-only); human second-coder sheet prepared |
| Quality appraisal | None | VDR score (stated as not a risk-of-bias tool) |
| PRISMA 2020 checklist | Absent | Completed (supplement); audit tally 14 R / 20 P / 6 M / 2 N/A before rounds 2–3 fixes |
| PRISMA-S | 4/16 reported | Checklist completed, plus one-line statements for items 3–6, 10–12 and 14; dates and hit counts are AUTHOR INPUT |
| References | 48 numbered, mostly APA, gaps | 79 APA author-date (JFR); all verified against Crossref or PubMed; 3 name forms for the authors to confirm |
| Tables / figures | 12 / 7 | 20 / 7; Figs. 2, 4–7 regenerated from data; greyscale-safe |
| Abstract | 275 words, unhedged | 243 words, structured, primary outcome first |

## 2. Locked facts that changed (evidence: Sec. 16 entries 5–8; `data/analysis_output.md`)

The authors' original extraction workbook was lost. Re-extraction from the PDFs, followed by three audit rounds, changed the following:

| Fact | Before | After |
|---|---|---|
| Teleoperation / Supervisory field testing | "60–75%" | 3/5 and 1/4 (strict) |
| UAV vs Hybrid field testing | 1/13 vs 4/7 | 3/13 vs 3/7 (p = 0.61) |
| Environmental-realism limitation | 35/39 | 26/39 (author-stated rule) |
| Validation (Simulation / Partial / Field / Bench) | 18 / 10 / 8 / 3 | 19 / 12 / 6 / 2 strict |
| FA vs human-in-the-loop field testing | (not tested) | 2/27 vs 4/12 (p = 0.060); no contrast survives Holm |

Unchanged:
- record flow (130 / 125 / 39 / 86);
- mode split (27 / 5 / 4 / 3);
- platform split;
- all 39 mode and platform labels.

## 3. Status of every audit ID (from `2026-11-08_full_paper_audit.md`)

**Integrity items (I):**

| ID | Status |
|---|---|
| I-1 | FIXED in text (Google Scholar reported). BLOCKED-ON-AUTHORS: which of the 7 queries were run |
| I-2 | FIXED (78 / 15 / 34 / 3 by route, two-column PRISMA) |
| I-3 | FIXED (one searcher) |
| I-4 | FIXED in text (two screeners). BLOCKED-ON-AUTHORS: identities, and what "averaged out" meant |
| I-5 | FIXED (limitations restored, expanded into threats to validity) |
| I-6 | FIXED (AI and Google Scholar disclosed; Sec. 2.2 superseded) |
| I-7 | FIXED (contradictory sentence removed) |
| I-8 | BLOCKED-ON-AUTHORS (dates and batches unconfirmed; the date was removed and marked) |
| I-9 | FIXED (AI-assisted extraction stated) |
| I-10 | FIXED in text (AI-use statement). BLOCKED-ON-AUTHORS: versions and the verification sentence |
| I-11 | PARTLY FIXED (year limit for the AI route stated as checked per record). BLOCKED: confirmation |
| I-12 | BLOCKED-ON-AUTHORS (all 130 records are Q1 or Q2; was quartile a filter?) |
| I-13 | FIXED (the docx "20 real / 19 sim" scheme is superseded by the page-referenced strict and lenient coding) |

**Critical items (C):**

| ID | Status |
|---|---|
| C1 | FIXED / BLOCKED (as I-1 to I-12) |
| C2 | FIXED |
| C3 | FIXED (gradient claim removed) |
| C4 | FIXED |
| C5 | FIXED ([6] corrected: 15 platforms, 14 classified, autonomy coded) |
| C6 | FIXED (hedged; dated scans 2026-11-08 v2 and 2026-11-09) |
| C7 | FIXED (CSV rebuilt from PDFs) |
| C8 | FIXED |
| C9 | FIXED (rule plus Table XVI; value now 26/39) |
| C10 | FIXED (full threats-to-validity section) |

**Major items (M):**
- **M1 (search):** BLOCKED-ON-AUTHORS. The protocol and Boolean strings are in `supplementary/search_protocol.md`.
- **M2:** FIXED.
- **M3:** FIXED (definitions, rules, coding manual, S3).
- **M4:** FIXED.
- **M5:** FIXED (bands, no ordinal axis claim).
- **M6:** FIXED (human-in-evaluation flag, per-function coding, circularity discussed).
- **M7:** FIXED as AI-only. BLOCKED: human κ.
- **M8:** FIXED (VDR).
- **M9:** FIXED in text ("not registered"). AUTHOR choice: retrospective OSF record.
- **M10:** FIXED.
- **M11–M14:** FIXED.
- **M15, M16:** FIXED (descriptive, confounded).
- **M17:** FIXED (trend claims removed).
- **M18, M19:** FIXED.
- **M20, M21:** FIXED ([2] and [3] replaced by peer-reviewed sources).
- **M22–M25:** FIXED.
- **M26, M27:** FIXED (abstract, title).
- **M28:** PARTLY. Statements drafted; BLOCKED: emails, ORCID, funding, COI, CRediT, repository DOI. Biographies are not required by JFR.
- **M29:** FIXED (JFR, SJR Q1).
- **M30:** FIXED.

**Minor items (m1–m26):** all FIXED. Leaked language was removed (grep-verified). Bibliography notes, APA format, DOIs and pages, name forms, citations, acronyms, American spelling, terminology and figures were all addressed.
- Remaining for the authors: name forms for refs [9], [45] and [48].
- Remaining for the authors: the year convention for Khalil (2026 or 2027).

## 4. Remaining author actions (checklist)

- [ ] **Run the supplementary database search** (Scopus, Web of Science, IEEE Xplore; strings in `supplementary/search_protocol.md`). Screen new records with two people and keep each person's decisions. This is the single largest remaining rejection risk.
- [ ] Search dates per source; screening dates; hit counts if recorded (the first PRISMA box currently counts cataloged records).
- [ ] Was journal quartile used to decide what to catalog? (All 130 records are Q1 or Q2.)
- [ ] Which Google Scholar queries were run; the ChatGPT and Gemini prompts, versions and dates; how many AI suggestions were hallucinated or mis-cited.
- [ ] Screener identities; what "averaged out" meant; were per-screener sheets kept?
- [ ] Who checked the AI extraction, the quality scores and the citations, and how. Wiley requires this to be stated.
- [ ] Human second coder: complete `supplementary/human_second_coder_sheet.csv` blind, using `coding_manual.md`, and report κ. Check the borderline codes listed in S3, including [44], [48], [20] and [21].
- [ ] Document-type and language eligibility rules.
- [ ] Registration: state "not registered", or deposit a retrospective OSF record.
- [ ] Repository DOI (OSF or Zenodo) for the supplementary package.
- [ ] Corresponding author, emails, ORCIDs, funding, COI, CRediT, acknowledgments, AI-system versions.
- [ ] Confirm the name forms for [9] Rajashekhar V S, [45] Gowry Sailaja V and [48] Vani et al., and the year label for Khalil et al.
- [ ] Read the whole manuscript yourselves. Wiley's AI policy requires human oversight and the authors' own verification of all AI-generated content.

## 5. Deliverables

- **`SAR_review_master_document.md`:** manuscript Secs. 9–14 rewritten; APA list added to Sec. 15; Sec. 16 entries 1–8.
- **`data/`**
  - `extraction_table.csv`, `function_autonomy.csv`, `reliability_blind_codes.csv`
  - `analysis.py` → `analysis_output.md`
  - `make_figures.py`, `make_prisma_v2.py`, `references.py`, `rebuild_reflist.py`, `check_xrefs.py`, `build_docx.py`
- **`supplementary/`:** S1 screening log, S2 to S7, coding manual, PRISMA 2020 and PRISMA-S checklists, search protocol, scripts, README. Zipped as `submission/supplementary_data.zip`.
- **`assets/figures/`:** `prisma_diagram_v2.png`; regenerated `fig_sensor_prevalence.png`, `fig_validation_type.png`, `fig_autonomy_validation.png` and `fig_taxonomy.png`. The old versions are backed up in the session scratchpad.
- **`submission/`:** `JFR_submission_manuscript.docx` (Wiley free format; 44-page PDF preview checked visually) and `cover_letter.md`. JFR requires no highlights and no suggested reviewers, so none are produced.
- **`research_outputs/2026-11-08_*` and `2026-11-09_*`:** all agent reports.
- **`.claude/agents/`:** four new agents (corpus-claim-auditor, extraction-rebuilder, excluded-record-auditor, reliability-coder).
