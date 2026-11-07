# Initial novelty scan + statistics check — 2026-11-08

Quick baseline produced while building the `.claude` agent system. Run `/q1-research` for the full, deeper pass (the `literature-scout` agent does ≥12 searches; this baseline did 6 searches and 1 source verification).

## 1. Has this already been done? (contribution verdicts)

| Claimed contribution | Verdict | Evidence |
|---|---|---|
| C1. Four-way autonomy/HRI taxonomy as the primary organizing axis for SAR robotics, with a label for every paper | **STANDS, with a hedge needed** | No SAR review found that does this. **However**, Bakzadeh et al. 2026 [6] *does* code autonomy level (A1 teleoperated / A2 semi-autonomous / A3 fully autonomous, based on Sheridan–Verplank) as one of three axes for 14 mine-rescue platforms (12 A1, 1 A2, 1 A3). |
| C2. Real-world validation rate quantified by autonomy level (FA 7.4% field-tested) | **STANDS** | No review found that cross-tabulates autonomy level against validation type. Shuvo et al. 2026 records simulation platforms per study but reports no counts (based on the fetch tool's summary of the unread part of the page; UNVERIFIED). |
| C3. UAV platform–validation mismatch | **STANDS** | Nothing comparable found. |
| C4. First review of the 2025–2026 window after Kareem et al. 2026 | **THREATENED: reposition** | Shuvo et al. 2026 covers 2005–2025, which overlaps the manuscript's 2025 papers. A 2026 path-planning SLR also covers recent years. The "zero temporal overlap with [4]" claim is still true, but "first to cover 2025–26" is not safe. |

## 2. Factual error in the manuscript (fix before submission)
**Bakzadeh et al. 2026 [6] is mischaracterized.** The manuscript (Introduction and Table I) says it "explicitly excludes autonomy and control software from their stated scope" and "doesn't address autonomy/HRI mode at all."
The source (verified 2026-11-08) says "the autonomy, mapping, SLAM, path planning, and software architecture of CMRRs are not reviewed." In Sec. 5.1.4 it still classifies every platform by autonomy level: "Three bands are used: A1 teleoperated (Levels 1–4…); A2 semi-autonomous (Levels 5–7…); and A3 fully autonomous (Levels 8–10…)", and it reports 12/1/1.
→ Suggested rewrite: *"Bakzadeh et al. [6] exclude autonomy and control software from their scope, but do assign each of 14 mine-rescue platforms a coarse three-band autonomy level adapted from Sheridan and Verplank (12 teleoperated, one semi-autonomous, one fully autonomous). This is a platform inventory for a single hazard type, not a quantitative autonomy analysis of a research corpus."* This also helps the paper, because [6] independently supports the finding that fielded systems are overwhelmingly teleoperated.

## 3. Uncited competing / adjacent work to add
| Work | Why it matters | Positioning |
|---|---|---|
| Shuvo, Fime, Ashraf, Alam & Kim (2026), "Learning-enabled collaborative intelligence in search and rescue robotics: a survey of paradigms, models, and challenges," *Front. Robot. AI* 13, published 14 Oct 2026, doi:10.3389/frobt.2026.1832982 | The most recent SAR review. It organizes the field by H2M/M2M/M2H learning; it is a narrative review backed by a systematic search ("rather than a fully PRISMA-compliant systematic review"); it covers 2005–2025 across 9 databases. | Add to Table I. Its organizing axis is the *learning paradigm*, not *autonomy/HRI mode*, and it does not quantify validation by autonomy (UNVERIFIED for its unread sections). |
| "Path planning for search and rescue robots: A systematic and bibliometric review," *Applied Soft Computing* (2026), ScienceDirect S1568494626018284; 73 articles from 850 Scopus+WoS records | A recent PRISMA-style SAR SLR that searched Scopus and WoS. Reviewers will compare search rigor. | Add to Table I (axis: path-planning method). Verify authors and DOI before citing. |
| Air-ground collaborative robots for fire and rescue missions: a survey from the mapping and navigation perspective, arXiv:2412.20699 (revised 2026) | Multi-platform SAR survey | Cite in the Hybrid/Multi-Platform discussion. Check whether a peer-reviewed version exists. |
| "Autonomous Aerial Robots for Enhanced SAR Operations: A Critical Review…" (ResearchGate, Jan 2026) | UAV SAR review | Find the venue first. Cite only if peer-reviewed. |
| ESARBench (arXiv 2605.01371, May 2026), a benchmark for MLLM UAV agents in SAR | Supports the paper's MLLM perception-vs-control finding ([47]) and the call for standardized benchmarks | Cite in Future Directions items 1–2. |
| Hagenow et al. 2026, a review of shared control/autonomy; the Frontiers 2025 mini-review of variable autonomy (doi:10.3389/frobt.2025.1540476) | Theory grounding for the Shared-Collaborative category | Cite in Sec. IV. |

## 4. Statistics: the headline finding is statistically significant (add this to Results)
95% Wilson CIs and two-sided Fisher's exact tests, computed from Table "Autonomy Mode × Validation Type":

| Proportion field-tested | Value [95% CI] |
|---|---|
| Fully Autonomous | 2/27 = 7.4% [2.1%, 23.4%] |
| All human-involved modes (Tele + Sup + Shared) | 6/12 = 50.0% [25.4%, 74.6%] |
| Teleoperation | 3/5 = 60.0% [23.1%, 88.2%] |
| Supervisory | 3/4 = 75.0% [30.1%, 95.4%] |
| UAV | 1/13 = 7.7% [1.4%, 33.3%] |
| Hybrid/Multi-Platform | 4/7 = 57.1% [25.0%, 84.2%] |

- FA vs all human-involved: **p = 0.0056**
- FA vs Teleoperation + Supervisory: **p = 0.0010**
- UAV vs Hybrid: **p = 0.031**. This one is borderline, so report it as descriptive and use cautious wording.

The CIs for the per-mode Teleop and Supervisory rates are very wide (n = 5 and n = 4). Report the pooled "human-involved" comparison as the primary test.

## 5. Top Q1 risks (fix order)
1. Search strategy: two terms on publisher portals, no Scopus/WoS, no Boolean strings → `/search-update`
2. The Bakzadeh mischaracterization (Sec. 2 above) and the missing competitors (Sec. 3 above)
3. No inter-rater κ, no quality appraisal, no protocol registration → `/prisma-audit`
4. Hedge the abstract's "has not been reported previously"
5. Add the inferential statistics above
6. Ground the taxonomy in LOA theory and add a coding manual → `taxonomy-theorist`
7. Replace ref [3] (NBC News) and check whether ref [2] (arXiv) has a published version
8. Remove "model reference paper" wording from the Discussion
9. Confirm the target venue live. IEEE Access's quartile depends on the index and category → `journal-scout`

## Sources
- [Bakzadeh et al. 2026, Front. Robot. AI](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1857704/full)
- [Shuvo et al. 2026, Front. Robot. AI](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1832982/full)
- [Path planning for SAR robots: systematic & bibliometric review (Applied Soft Computing)](https://www.sciencedirect.com/science/article/abs/pii/S1568494626018284)
- [Air-Ground Collaborative Robots for Fire and Rescue (arXiv 2412.20699)](https://arxiv.org/abs/2412.20699)
- [Autonomous Aerial Robots for SAR: Critical Review (ResearchGate)](https://www.researchgate.net/publication/400542025_Autonomous_Aerial_Robots_for_Enhanced_Search_and_Rescue_OperationsA_Critical_Review_of_Trends_Pitfalls_and_Future_Methodological_Directions)
- [Sensors survey, Sinha et al. 2026](https://doi.org/10.3390/s26051659)
- [ESARBench](https://www.alphaxiv.org/abs/2605.01371)
- [Hagenow et al. shared control review 2026](https://collab.me.vt.edu//pdfs/hagenow_review2026.pdf)
- [Variable autonomy mini-review, Frontiers 2025](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1540476/pdf)
- [Smart earthquake rescue robot, Sci. Rep. 2025](https://www.nature.com/articles/s41598-025-16003-7)
