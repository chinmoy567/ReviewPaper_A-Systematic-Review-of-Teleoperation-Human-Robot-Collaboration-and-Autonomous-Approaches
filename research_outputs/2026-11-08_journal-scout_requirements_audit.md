# Journal-scout requirements audit (2026-11-08, audit mode, manuscript not edited)

Limitation: my toolset had no grep or shell. I read only Sec. 14 (lines 712-747) of the master document. I could NOT grep Secs. 9-13 for venue or quartile claims. Re-run that grep before relying on the "none found" statements below.

## A. Venue / quartile claims in the manuscript
- Sec. 14 (title, abstract, Index Terms, conclusion): no journal name, no quartile claim, and no statement that Kareem et al. 2026 is in a Q1 venue. The abstract calls it "the most recent structurally comparable prior review (2016-2024 corpus)".
- The abstract says the autonomy-axis pattern "has not been reported previously". Under CLAUDE.md rule 2 this needs a dated novelty scan in research_outputs/.
- Secs. 9-13 and 15: UNCHECKED (see limitation).
- Sec. 8 or 16 may say Kareem is "Q1". Any such claim must stay UNVERIFIED until checked below. The IEEE Access quartile is itself not clean (see B).

## B. IEEE Access (ISSN 2169-3536)
Verified from the official page https://ieeeaccess.ieee.org/authors/submission-guidelines/:
- Index terms/keywords: 3-10 chosen at submission.
- Short biographies required for all authors, placed below the references. No photo requirement is stated there.
- AI-generated text must be disclosed in the Acknowledgements, and the AI system must be cited. Source: the same page, plus the IEEE AI-text policy page https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/ (snippet only; the full page was not opened). Light editing: disclosure recommended, not required (search snippet, UNVERIFIED on the page).
- Page limit: none. Under 20 pages is recommended. Topical Reviews and Surveys are excluded from the count. Longer papers get an initial editorial check.
- APC: USD 2,160 plus taxes, according to that page. An older FAQ version gives no amount.
- Review types:
  - Topical Review: must show need and novelty against recent reviews, state research questions and scope, compare methods on defined criteria, and give evidence-based future directions.
  - Survey: the same, plus inclusion/exclusion criteria and a description of the search and screening process.
  - Both are rejected if they mainly list papers, report bibliometrics without synthesis, or are a tutorial or historical overview.
- Abstract <=250 words, no citations: NOT stated on the official page. A third-party blog (manusights.com) says 150-250 words, one paragraph. UNVERIFIED officially. The current abstract is roughly 330 words by my estimate, so it is likely over. Count it exactly.
- Funding, data availability, conflict of interest: not mentioned on the guidelines page. The PDF checklist https://ieeeaccess.ieee.org/wp-content/uploads/2025/09/IEEE-Access-Submission-Checklist.pdf could not be text-extracted. UNVERIFIED. Treat funding statement, COI and data availability as expected from the submission system and IEEE norms.
- Reference format: IEEE numbered style [n]. UNVERIFIED on the page, but standard IEEEtran.
- Quartile: UNVERIFIED. Journalmetrics.org (third party) says JCR 2025 IF 3.6, Q2. The CASRAI entry says IF 4.2. SJR 0.849 for 2024 is from IEEE's own page https://open.ieee.org/publishing-options/ieee-access/. I found no SCImago 2025 quartile page. Do NOT call IEEE Access a "Q1" journal without opening Clarivate JCR or scimagojr.com for ISSN 2169-3536 and recording category and year. SJR often puts it Q1 in some categories and Q2 in others, so check each category.

## C. Alternatives (all metrics from third-party aggregators unless noted; official pages were not retrieved)
| Journal | Quartile | Metrics | APC / model | Notes |
|---|---|---|---|---|
| Robotics and Autonomous Systems (Elsevier) | UNVERIFIED | IF 5.2 (2025) per journalmetrics.org/journal/robotics-and-autonomous-systems; CiteScore 8.1-9.9 across sources | UNVERIFIED | Official guide for authors not retrieved. Review-article policy UNVERIFIED. |
| Journal of Field Robotics (Wiley) | UNVERIFIED (Q1 per Peeref JCR 2023; Q2 per journalmetrics 2025) | IF 5.2 or 7.4 or 8.3, conflicting | Hybrid, about USD 4,430 (journalmetrics, UNVERIFIED) | Strong scope fit with field robotics. Review policy UNVERIFIED. |
| Frontiers in Robotics and AI | Q2 for SJR/AI per researcher.life; impact-factor sites say Q2 | IF about 3.0-3.7 (Frontiers page says 3; https://www.frontiersin.org/journals/robotics-and-ai/about) | Open access, APC UNVERIFIED | Likely not Q1. It also hosts the competing reviews (Shuvo, Bakzadeh), so the conflict risk is high. |
| Drones (MDPI) | Q1 for the 2024 IF in Remote Sensing per the MDPI history page, though journalmetrics says Q2 in one record. UNVERIFIED for 2025 | IF 5.2 (JCR 2025, released June 2026) per journalmetrics and the MDPI page | CHF 2,000-2,600, conflicting. UNVERIFIED | Fast, and reviews are welcomed. Scope is UAV-centric. The paper is autonomy/HRI across UGV/UAV/hybrid, so the fit is partial. |
| Artificial Intelligence Review (Springer) | Q1 per aggregators; the explicit latest-year JCR quartile was not found | IF 13.9 (2024) and median 12 days to first decision, per https://www.springer.com/10462 | Fully open access since Jan 2024, APC UNVERIFIED | Scope is AI. The paper is robotics/HRI. Expect a desk-reject risk for fit. |

The full candidate list required by the skill (at least 10 journals, scored fit, LaTeX template) is NOT done in this audit. It is a requirements audit only.

## D. Front/back matter missing from the .md (checked against Sec. 14 only)
Present: title, 3 authors, one shared affiliation, abstract, Index Terms (9), Conclusion, Sec. 15 numbered references.
MISSING (not seen in Sec. 14):
1. Corresponding author and email, ORCIDs.
2. Funding/financial support statement.
3. Conflict-of-interest/competing-interests statement.
4. Data-availability statement (PRISMA records, extraction table, classification log, and paperlinks.xlsx would back it).
5. AI-use disclosure in Acknowledgements. The audit trail records ChatGPT and Gemini used for discovery, so this is required and must match what was actually done (CLAUDE.md rule 4).
6. Acknowledgements section.
7. Author biographies for all three authors (IEEE Access requires them; photos not required per the page).
8. Author contributions (CRediT), ethics and registration statement (PROSPERO/OSF, or a statement that none exists), and a PRISMA checklist (not required by IEEE Access but expected by most journals).
9. Abstract word count against 250 words and a no-citations check.
Secs. 9-13 might contain some of these. UNCHECKED.

## E. Recommendation
Do not describe IEEE Access as Q1 or cite Kareem 2026 as Q1 until a JCR or SJR page is opened and the category and year are recorded. IEEE Access fits the existing format, though the same-reviewer conflict with Kareem remains. Journal of Field Robotics and Robotics and Autonomous Systems are the likeliest true Q1 alternatives, but their quartiles and review policies must be verified on the official Clarivate and publisher pages first.

Sources:
- https://ieeeaccess.ieee.org/authors/submission-guidelines/
- https://ieeeaccess.ieee.org/wp-content/uploads/2025/09/IEEE-Access-Submission-Checklist.pdf
- https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/
- https://open.ieee.org/publishing-options/ieee-access/
- https://www.journalmetrics.org/journal/ieee-access
- https://www.journalmetrics.org/journal/robotics-and-autonomous-systems
- https://www.journalmetrics.org/journal/journal-of-field-robotics
- https://www.frontiersin.org/journals/robotics-and-ai/about
- https://www.journalmetrics.org/journal/drones
- https://www.mdpi.com/journal/drones
- https://www.springer.com/10462
