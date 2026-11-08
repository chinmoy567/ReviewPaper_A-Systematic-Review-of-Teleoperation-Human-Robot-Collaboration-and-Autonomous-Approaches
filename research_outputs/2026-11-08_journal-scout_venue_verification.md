# Journal-scout venue verification (2026-11-08) - INCOMPLETE, quartiles NOT verified

## Outcome
No JCR or SJR quartile could be verified for any journal. Every direct fetch of scimagojr.com (journalsearch.php by ISSN and by sid), mdpi.com/journal/drones, sciencedirect.com (RAS) and onlinelibrary.wiley.com (JFR) returned HTTP 403. Springer (link.springer.com/journal/10462) redirects to an auth handshake. Clarivate JCR needs a login. WebSearch cannot open scimagojr.com. All quartiles below are therefore UNVERIFIED. A person with a browser must open the SCImago pages and JCR (via a library login) and record category + year.

## Per-journal status
| Journal | Quartile (JCR/SJR, category, year) | Other facts obtained | Source |
|---|---|---|---|
| IEEE Access 2169-3536 | UNVERIFIED. Aggregator says JCR 2025 Q2, IF 3.6 (third party); IEEE page gives SJR 0.849 (2024) with no quartile | Official guidelines (see prior audit): Topical Review and Survey accepted, no page limit, APC USD 2,160, AI disclosure in Acknowledgements, biographies required | https://ieeeaccess.ieee.org/authors/submission-guidelines/ ; https://open.ieee.org/publishing-options/ieee-access/ |
| Journal of Field Robotics 1556-4959 | UNVERIFIED. Aggregators conflict: SJR Q1 (Computer Science Applications, Control and Systems Engineering; resurchify, paperguide) vs JCR Q2 with IF 5.2 (journalmetrics, 2025) | Wiley page blocked (403); review policy, APC, template UNVERIFIED | https://www.journalmetrics.org/journal/journal-of-field-robotics ; https://www.resurchify.com/impact/details/21100301602 |
| Robotics and Autonomous Systems 0921-8890 | UNVERIFIED | ScienceDirect blocked (403). IF 5.2 (2025) and CiteScore 8.1-9.9 are aggregator-only | https://www.journalmetrics.org/journal/robotics-and-autonomous-systems |
| IEEE Transactions on Field Robotics | UNVERIFIED; no JCR IF or quartile found anywhere (may be too new to be indexed) | RAS scope page says experimental validation limited to simulation or controlled lab work is not published. That is hostile to a review of simulation-heavy literature only if the paper contributes no field evidence; it is a scope hint, not a review policy. Whether T-FR takes surveys is UNVERIFIED | https://www.ieee-ras.org/publications/t-fr/ |
| Drones 2504-446X | UNVERIFIED (mdpi.com 403) | none new | - |
| Artificial Intelligence Review 0269-2821 | UNVERIFIED | Springer page blocked. Earlier audit: IF 13.9 (2024), median 12 days to first decision, per springer.com/10462 (from search snippet, not re-opened) | https://www.springer.com/10462 |
| Frontiers in Robotics and AI 2296-9144 | UNVERIFIED. | Official About page (opened): IF 3.7, CiteScore 7, quartile not stated; "Systematic Review" is an accepted article type; APC amount not on page (links to publishing-fees page, not opened); first-decision time not stated | https://www.frontiersin.org/journals/robotics-and-ai/about |
| Int. J. Disaster Risk Reduction (Elsevier) | UNVERIFIED | Search found no current IF, quartile or review policy. A 6.5 IF aggregator figure is undated, treat as unusable | - |
| IEEE RAM, Autonomous Robots, Annual Reviews in Control, ACM Computing Surveys, IEEE THMS, Robotics (MDPI), Intelligent Service Robotics | NOT CHECKED (blocked by time and fetch limits) | - | - |

Not obtained for any journal: AI-use policy text (except IEEE Access, from the prior audit), data-availability policy, CRediT/highlights/graphical-abstract/suggested-reviewer requirements, word and reference limits, LaTeX templates, turnaround. All UNVERIFIED.

## Provisional recommendation (reasoning only, not a verified-Q1 claim)
- Do not pick any venue as "Q1" on this report. None is verified.
- Leading candidate to verify first: Journal of Field Robotics (best topical fit with field robotics; SJR Q1 per two aggregators, JCR Q2 per one). Verify review-article acceptance on Wiley's author guidelines before committing. The paper's headline finding (field-test gap) matches the journal's field-validation ethos.
- Backup to verify: Robotics and Autonomous Systems (Elsevier, robotics scope, accepts surveys in practice but policy UNVERIFIED).
- IEEE Access: a fit for the current IEEEtran format and an explicit Survey article type, but the quartile is disputed (Q2 per aggregator) and Kareem et al. 2026 appeared there, so same-reviewer overlap risk is real. Do not default to it.
- Frontiers in Robotics and AI: accepts Systematic Reviews officially, but IF 3.7 is probably not Q1 in JCR Robotics, and Shuvo et al. 2026 and Bakzadeh et al. 2026 were published there. High conflict risk.
- Drones and AI Review: scope fit partial (UAV-centric; AI-centric) so desk-reject risk.

## Next steps for the authors
1. Open https://www.scimagojr.com and search each ISSN; record the quartile table (category x year) for the latest year shown, plus the URL.
2. Check JCR through an institutional login (BAIUST may lack one; if so, rely on SJR and say so).
3. Open each publisher's author guidelines for article types, AI policy and templates, then re-run this scout.

Sources:
- https://www.frontiersin.org/journals/robotics-and-ai/about
- https://www.journalmetrics.org/journal/journal-of-field-robotics
- https://www.resurchify.com/impact/details/21100301602
- https://www.journalmetrics.org/journal/robotics-and-autonomous-systems
- https://www.ieee-ras.org/publications/t-fr/
- https://ieeeaccess.ieee.org/authors/submission-guidelines/
- https://open.ieee.org/publishing-options/ieee-access/
