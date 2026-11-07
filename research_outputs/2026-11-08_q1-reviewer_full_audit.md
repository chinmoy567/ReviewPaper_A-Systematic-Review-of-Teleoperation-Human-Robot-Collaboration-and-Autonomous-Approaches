# Simulated Reviewer-2 Report: Full Logic and Argument Audit

**Manuscript:** "Recent Advances in Robotic Systems for Disaster Search and Rescue: A Systematic Review of Teleoperation, Human-Robot Collaboration, and Autonomous Approaches" (Avi, Sultana, Sarker)
**Target venue simulated:** IEEE Access / Q1 robotics journal (RAS, JFR, IEEE THMS)
**Date:** 2026-11-08
**Source read:** `SAR_review_master_document.md`, manuscript blocks only: Title/Abstract/Index Terms (L718–732), I (L666–699), II (L307–409), III (L419–555), IV (L567–605), V (L615–654), VI (L736–744), bibliography (L810–904), and all 7 figures in `assets/figures/`. Status notes, sourcing notes and the italic working notes were not reviewed as prose, except where noted that they could leak into a submission.
**Line numbers** refer to `SAR_review_master_document.md` as of 2026-11-08.

---

## 1. Summary (as the editor sees it)

The submission is a PRISMA-labelled review of 39 papers from 2025–2026 on disaster SAR robotics. The 39 papers were drawn from 130 records found with two search phrases on publisher portals. Each paper is coded into one of four autonomy/HRI modes. The headline claim is an "inverse relationship" between autonomy level and real-world validation: 2/27 Fully Autonomous papers were field-tested, against 60–75% for Teleoperation and Supervisory papers. A related UAV-versus-Hybrid contrast and an 89.7% rate of self-reported environmental-realism limitations are also reported. The central contrast is interesting and, on my recomputation, statistically detectable. However, the paper overstates it, partly builds it in through the classification rule, and calls it a monotonic "spectrum" effect that its own Fig. 6 contradicts. Around it sits a search, appraisal and validity apparatus well below Q1 standard.

## 2. Decision

**Reject and resubmit.** Confidence: **high** (4/5).

The core idea is publishable. The current argument is not. Several conclusions are contradicted by the authors' own tables, figures and sections (M1, M2, M5, M8). Key results first appear in the Discussion (M6). The method cannot be reproduced (M9).

## 3. Rubric scores

| # | Dimension | Score | Justification |
|---|---|---|---|
| 1 | Novelty & positioning | 2 | The FA × validation cross-tab looks new as a quantified result. "Not reported previously" (L730) and "would not surface" (L605, L730) overclaim, though. The qualitative pattern (fielded rescue robots are teleoperated; autonomy stays in the lab) is long established (Murphy, *Disaster Robotics*, 2014; Delmerico et al., JFR 2019). [6] is mischaracterized (M10). Recent competitors are missing (Shuvo et al. 2026; the 2026 *Applied Soft Computing* path-planning SLR). |
| 2 | Search & selection rigor | **1** | Two phrases (L349), a different term for MDPI, publisher portals instead of Scopus/WoS, no Boolean string, no search date per source. "Sources" are publishers classified by DOI (L343), not information sources. No κ. |
| 3 | Quality appraisal | **1** | None (L643). The authors admit this themselves, and then draw validation-rigor conclusions anyway. |
| 4 | Data extraction & coding | 2 | 18 fields, but no coding manual. The "seven explicit classification precedents" (L375) are not provided. No per-study table. No reliability statistic. The core outcome "Real-world field test" is never defined. |
| 5 | Analysis & statistics | 2 | Percentages on n = 3, 4, 5 cells with no CIs or tests. A spurious statistical claim at L537. Post-hoc hypothesis checks with no tests (L631). |
| 6 | Theoretical contribution | 2 | The four modes are never defined in the prose (only one-liners in Fig. 7). No LOA theory is cited (Sheridan–Verplank, Parasuraman et al. 2000, Beer et al. 2014). The ordering of Supervisory versus Shared is asserted, not argued, yet the "spectrum" claim depends on it (M2). |
| 7 | Insight & implications | 2 | Mechanisms for the FA gap are barely discussed. Two of five future directions rest on a single paper each. The authors' own HRI axis gets no direction. Existing NIST/ASTM E54.09 response-robot test methods are ignored. |
| 8 | Threats to validity | **1** | Two bullets (L643–644). No construct, internal, external or conclusion validity discussion. |
| 9 | Writing & structure | 2 | Working-document language leaks throughout ("model reference paper" ×7, "verified prior reviews", "bucket", "flagship", "originally set out to test", "extraction table"). Process narration. IV-D and V-A repeat each other. |
| 10 | References & presentation | 2 | Key framing rests on arXiv [2] and an NBC News quote [3]. An uncited death toll (L670). Evaluative captions. Fig. 6 contradicts the text it illustrates. |

**Mean = 1.7, with 1s on dimensions 2, 3 and 8.** Under the rubric's mapping this is a Reject (resubmit).

Recomputed statistics, used below (Wilson 95% CI; two-sided Fisher exact; computed from Table XI and text counts):
- FA field-tested 2/27 = 7.4% [2.1, 23.4] vs. all human-involved modes 6/12 = 50.0% [25.4, 74.6]; p = 0.0056.
- Shared-Collaborative 0/3 = 0% [0, 56.1]. Teleoperation 3/5 [23.1, 88.2]. Supervisory 3/4 [30.1, 95.4].
- **Any non-simulation testing** (field + partial + bench): FA 11/27 = 40.7% [24.5, 59.3] vs. non-FA 10/12 = 83.3%; p = 0.018.
- UAV vs. Hybrid field-tested: 1/13 vs. 4/7; p = 0.031.
- Environmental-realism limitation, Generic vs. hazard-specific: 20/21 vs. 15/18; **p = 0.32 (no difference)**.

---

## 4. Major comments

**M1. [L740, L690, L521] The headline is misstated as "tested outside simulation," which the authors' own Table XI contradicts.**
- *Quotes:* L740: "Fully Autonomous systems … are field-tested outside simulation in only 7.4% of cases". L690: "whether the more autonomous a reported system, the more or less likely it is to have been tested outside simulation". L521: "The more autonomous a reported system in this corpus, the less likely it is to have been tested outside simulation."
- *Problem:* 7.4% is the *Real-world field test* category only. Table XI (L530) shows FA papers in Partial (sim + limited real-world, 7) and Prototype bench (2), so 11/27 FA papers (40.7%) were tested outside simulation.
- *Why it matters:* The Conclusion's main sentence is factually wrong by a factor of 5.5, and it is the sentence readers will quote.
- *Fix:* Use "real-world field-tested" consistently everywhere (Abstract, I, III-D, VI). Report both contrasts: field-tested (7.4% vs 50.0%, p = 0.006) and any non-simulation testing (40.7% vs 83.3%, p = 0.018).

**M2. [L521, L535 Fig. 6 caption, L690, L696] The "inverse relationship across the full four-way spectrum" is contradicted by Fig. 6.**
- *Quotes:* L535: "Real-world field-validation rate by Autonomy/HRI mode, spanning the full taxonomy spectrum from Teleoperation to Fully Autonomous". L521: "Fig. 6 presents this inverse relationship across the full four-way autonomy spectrum." L696: "autonomy level and real-world validation rate are inversely related".
- *Problem:* Fig. 6, in the authors' own ordering (Fig. 7: Tele → Sup → Shared → FA), reads 60% → 75% → **0%** → 7.4%. That is not monotonic: it rises, collapses and then rises again. Shared-Collaborative (0/3) is the *least* field-tested mode, below FA. The ordering of Supervisory versus Shared is also contestable. In much LOA literature, supervisory control sits at higher autonomy than shared/blended control. Swap them and the series is 60 → 0 → 75 → 7.4, still not monotonic.
- *Why it matters:* The evidence supports a binary FA-versus-human-involved contrast, not an ordinal dose-response "spectrum." Calling it "inverse" across four levels is a claim the data refute.
- *Fix:* Reframe throughout as "FA versus human-in-the-loop modes." Drop "spectrum," "inverse relationship" and "the more autonomous … the less likely." Report the pooled test with CIs. State explicitly that per-mode cells (n = 3–5) cannot support ordinal claims. Re-caption Fig. 6 neutrally and add CIs as error bars.

**M3. [L425, L599, L369] The FA–validation association is partly built in by the classification rule (circularity).**
- *Quotes:* L425: FA = "operating with no human in the control loop during the mission itself". L599: "a Fully Autonomous label describes what was tested, not necessarily what a paper's own authors believe is ready for real deployment". L449/L481: 3 "Abstract/Unspecified simulation studies" and 10 papers with "no physical sensor at all."
- *Problem:* Papers are classified by the *tested pipeline*. A pure simulation of software agents has no operator by construction, so it is coded FA. A physical field test almost always involves a safety pilot, operator or goal-setter, which pushes it toward Teleop or Supervisory. The coding rule therefore mechanically associates "simulation-only" with "FA." Contribution type (algorithm paper vs. system paper) is a further confounder: algorithmic multi-agent RL papers are both FA and simulation-only for reasons unrelated to autonomy.
- *Why it matters:* The paper's central finding may partly be a measurement artifact, and the manuscript never considers this.
- *Fix:* (a) Stratify by contribution type (algorithm-only vs. embodied-system papers), or restrict the cross-tab to papers with a physical platform. Report whether the FA gap survives. (b) Code "designed autonomy level" separately from "tested autonomy level" and cross-tab both. (c) Add this as an explicit construct/internal-validity threat.

**M4. [L730, L605, L627, L742] Logical overreach: "only an autonomy-organized review could see this."**
- *Quotes:* L730: "A review organized around any axis other than autonomy would not surface this pattern, which has not been reported previously in this literature." L605: "a review organized by platform type, sensor modality, or system layer, as all four verified prior reviews are, would not surface the inverse relationship". L627: "a taxonomy that never isolates full autonomy as its own category also has no natural place to ask how rigorously it was validated". L742: "This distinction is invisible to a review organized around platform type, sensor modality, or system architecture".
- *Problem:* A cross-tab needs autonomy as a *coded variable*, not as the *organizing axis*. Any review that coded both variables could produce it. L627 is self-justifying: the omission in [4] is "read" as support for the authors' own design. "Not reported previously" is backed only by a 6-search baseline scan. The qualitative pattern is old: Murphy (2014) documents that deployed rescue robots are overwhelmingly teleoperated, and Delmerico et al. (JFR 2019, doi:10.1002/rob.21887) report limited adoption of state-of-the-art autonomy. Even [6], cited by the authors, codes 12 of 14 mine-rescue platforms as teleoperated (A1).
- *Fix:* Delete the counterfactual claims. Scope novelty to: "To our knowledge, no prior systematic review has quantified field-validation rates by autonomy mode; the qualitative observation that fielded SAR robots are predominantly teleoperated is long-standing [Murphy 2014; Delmerico et al. 2019; 6]." Delete L627 or rewrite it as a limitation of [4]'s scope without the inference.

**M5. [L595 vs L601] Direct internal contradiction within Sec. IV-D.**
- *Quotes:* L595, on the single-robot navigation cluster: "Real-world validation is markedly thinner in this cluster than the corpus average: five of the seven report simulation-only". L601: "the cluster with the most real-world testing (single-robot navigation) is still majority-simulation".
- *Problem:* The same cluster is described as the thinnest-validated and as the best-validated within one subsection. L601 also says the multi-robot cluster "has essentially one validated sim-to-real transfer," which conflicts with L593's description of [25]'s "3 of 10 physical collisions."
- *Fix:* Report a cluster × validation table (12/7/5/3 rows) and rewrite L601 from it. Name the two FA papers counted as field-tested (Table XI); they are never identified anywhere in the paper.

**M6. [L625, L631–633, L537] New results appear first in the Discussion and Abstract, with no Results table behind them.**
- *Quotes:* L631: "self-report environmental or terrain-realism limitations … at a rate of 95.2% (20 of 21) … than the 83.3% (15 of 18)". L633: "89.7% of the entire corpus (35 of 39)". L625: "a rare pattern (2 of 39, 5.1%)". L537: "UAV papers … (1 of 13, 7.7% …; 8 of 13, 61.5% simulation only) … Hybrid … (4 of 7, 57.1% …)".
- *Problem:* 89.7% is an Abstract and Contribution-4 headline (L697, L730, L740), but it is computed only in Sec. V-B. There is no extraction field, no coding rule, no definition and no table for "environmental-realism limitation." The Platform × Validation cross-tab behind the 7.7%/57.1% Abstract figures is not tabulated anywhere (Table VII is Platform × Mode). The "2 of 39 self-declared not ready" figure appears only in the Discussion.
- *Fix:* Add to Sec. III (i) a Platform × Validation table; (ii) an "environmental-realism limitation" variable with an operational definition, a coding rule, a second coder and a Scenario × Limitation table; (iii) the "explicit not-deployment-ready" variable, if it is kept. The Discussion should then only interpret these.

**M7. [L631–633, L697] The 89.7% figure measures author self-reporting, not a validation gap. The test that motivated V-B is also null.**
- *Quotes:* L697: "a near-universal (89.7%) environmental-realism validation gap". L631: "slightly *higher*, not lower". L633: "the generic-scenario framing this section originally set out to test".
- *Problem:* (a) Construct validity. A paper that lists "unmodeled weather, lighting, vegetation, dust, smoke, or similar" as a limitation may be *more* rigorous, not less. The category is so broad that almost any limitations section qualifies. (b) 20/21 vs 15/18 gives p = 0.32. Nothing "does not hold in the expected direction"; there is simply no detectable difference. (c) The section openly narrates a post-hoc hypothesis swap, then promotes the replacement to a headline contribution.
- *Fix:* Rename it "self-reported environmental-realism limitation." Remove "validation gap" and "near-universal." Report the null with the test. Give the coding rule and κ. Present the generic-vs-specific comparison as an exploratory analysis, without the narrative of what the authors "set out to test."

**M8. [L637, L697, L740] The platform "mismatch" is presented as an independent second finding, but is probably the autonomy finding restated (confounding / double counting).**
- *Quotes:* L637: "compounds rather than merely adds to Section V-A's concern" and "is a direct, evidenced finding rather than a speculative connection". L740: "This pattern recurs at the platform level".
- *Problem:* 9/13 UAV papers are FA and 0 are Teleop. 3/7 Hybrid papers are Teleop (Table VII), and Teleop has 3 field tests. The UAV-vs-Hybrid contrast is therefore heavily confounded with mode. "Recurs" implies independent replication on the same 39 papers. L637 also claims UAV is "the platform receiving the most attention from the corpus's more autonomy-forward research," but UGV ties UAV at 9 FA papers (L466). Shared-Collaborative papers are also not "autonomy-forward" by the authors' own definitions. UAV vs Hybrid p = 0.031 on n = 13 and 7 is fragile.
- *Fix:* Present field-test rate by platform *within* FA (UAV vs UGV within the 27 FA papers). If the UAV deficit disappears within FA, demote it to a corollary. Delete "compounds," "recurs" and "direct, evidenced finding." Remove it as a separate Abstract and Contribution-4 claim unless the stratified analysis supports it.

**M9. [L325, L343, L349, L371, L397] Search and screening are neither reproducible nor credible as described.**
- *Quotes:* L349: "The search terms "rescue robot" and "disaster rescue robot" were applied … with "disaster rescue robot" used as the primary term for MDPI and "rescue robot" for the remaining sources." L343: "DOI-verified by publisher". L371: "Screening was performed independently by the three authors … completed over two days (18–19 July 2026)". L397: "only findings on which all three agreed were retained and written up in this review; disagreements were resolved through joint discussion".
- *Problem:* (a) Two phrases miss "search and rescue" + UAV/drone/UGV/legged/swarm, "disaster robotics," "USAR," and "victim detection." Using a different term per source breaks comparability. (b) Table II/Fig. 1 classify records by the DOI's publisher. That is not the information source searched (PRISMA 2020 item 6; PRISMA-S items 1–8). "Scientific Reports (Springer Nature)" and "Springer" overlap. There are no Scopus, WoS or IEEE Xplore Boolean strings and no search dates. (c) 63/86 exclusions (L407) were off-domain, a 50% off-topic rate among retrieved full texts, which signals an imprecise search. (d) Three independent full-text readings of 125 papers in two days, with no κ, no disagreement counts and no pilot calibration, will not be believed. (e) L397 says both that only unanimous findings were retained and that disagreements were resolved by discussion. If non-unanimous data were *dropped*, that is selection bias.
- *Fix:* Re-run the search in Scopus + WoS + IEEE Xplore (+ ACM DL) with a full Boolean string. Report per-source dates. Merge and deduplicate, then update PRISMA. Report Cohen's/Fleiss' κ for screening and for the mode and validation codes. Rewrite L397 to say exactly what happened. Register a protocol (OSF) and supply the PRISMA 2020 checklist plus a data-availability statement with the extraction sheet.

**M10. [L676, L686, L555] Prior work is mischaracterized, and [6] is used in contradictory ways.**
- *Quotes:* L676: "Bakzadeh et al. [6] … explicitly exclude autonomy and control software from their stated scope". L686 (Table I): "Autonomy and control software explicitly excluded from scope". L555: "mine-rescue robotics literature outside this corpus [6] is predominantly teleoperation-oriented."
- *Problem:* The authors cite [6] for an autonomy claim while stating that [6] excludes autonomy. In fact, [6] (Sec. 5.1.4) assigns all 14 platforms to Sheridan–Verplank-derived bands (A1 teleoperated 12, A2 1, A3 1). Its review covers 14 platforms, while Table I says 15. Also, L676 says Tong et al. [8] (2024) "falls outside both this review's 2025–2026 window and the 2016–2024 corpus in [4]", but 2024 lies inside 2016–2024. Sinha et al. [5] (2020–2025) overlaps this review's 2025 papers, which undercuts the "zero temporal overlap" positioning (L695, L730).
- *Fix:* Correct the [6] description and the 14/15 count, and use [6]'s 12/14 teleoperated figure as external corroboration. Fix the Tong sentence. Add Shuvo et al. 2026 (Front. Robot. AI, doi:10.3389/frobt.2026.1832982), the 2026 *Applied Soft Computing* path-planning SLR, Delmerico et al. 2019 and Murphy 2014 to Table I or Sec. I. Drop "zero temporal overlap" as a *contribution* (L695). It describes the time window; it is not a finding.

**M11. [L313–321, L571–575, bibliography] The taxonomy is not defined operationally or grounded in theory.**
- *Quotes:* L375: "resolved against seven explicit classification precedents established and logged during extraction". L605: "applied consistently across all 39 papers under a logged, precedent-based protocol (Section II-F)".
- *Problem:* The four modes are defined nowhere in the manuscript prose. The only definitions are the Fig. 7 one-liners. The precedents are not supplied. The cross-reference points to II-F (Screening), but the precedents are described in II-G. None of the 48 references is an LOA or HRI theory source. "Consistently" is asserted with no reliability evidence.
- *Fix:* Add a definitions table: mode, decision authority per action vs. per goal, mapping to Sheridan–Verplank/Parasuraman levels and to Beer et al. (2014), and inclusion/exclusion cues. Publish the seven precedents as a supplementary coding manual. Report κ on a double-coded subset. Justify the Supervisory/Shared ordering or drop the ordinal claim (see M2). Fix "Section II-F" to "Section II-G".

**M12. [L363–369 vs L449, L471] Eligibility criteria are applied inconsistently.**
- *Quotes:* L369 lists as an exclusion pattern "an abstract path-planning algorithm with no robot embodiment". L361 C2: "The robot must be the operational agent". L440: "Abstract/Unspecified simulation studies at 3". L471: "10 papers, 25.6% … models no physical sensor at all, relying on fully abstracted simulation environments".
- *Problem:* The authors exclude disembodied algorithms but include three papers with no named platform and ten with no sensor model. These papers are almost all FA and simulation-only, so the inconsistency feeds directly into the headline (M3).
- *Fix:* Define the embodiment threshold for C2. Re-adjudicate the 3 Abstract/Unspecified papers. Run a sensitivity analysis of the FA × validation contrast with and without them.

**M13. [L311–321, L469–503] RQ1–RQ4 are not fully answered, and the HRI dimension in the title is barely analyzed.**
- *Problem:* RQ3 asks about "perception/sensor configurations, computational architectures, and validation approaches". Fields 10 (perception algorithm) and 11 (navigation method) were extracted (Table III) but never reported. Computational architecture (Table IX) is reported and then never discussed or cross-tabbed. Field 8 (HRI interface/modality) and field 6 (single- vs multi-robot) are extracted but never analyzed, in a review whose title and axis are HRI. RQ2 is answered only with n ≤ 3 cell observations (L457). The title promises "Human-Robot Collaboration," but that category has n = 3, and "Recent Advances" is not synthesized: there is no performance comparison across systems.
- *Fix:* Report fields 6, 8, 10 and 11 (a table each), or drop them from Table III and the RQs. Add Architecture × Validation; onboard compute is plausibly linked to field testing. Retitle to match the content, e.g. "Autonomy Level and Real-World Validation in Disaster SAR Robotics, 2025–2026: A Systematic Review".

**M14. [L639–644] The Limitations section is inadequate. It has two bullets and is partly defensive.**
- *Quotes:* L644: "This is a considered scope choice rather than an oversight: it is precisely what allows this review to pick up immediately where the 2016–2024 corpus in [4] ends." L644: "trend claims across a longer time span rely on the prior-reviews comparison (Section I)".
- *Problem:* Missing threats to validity:
  - *Construct:* mode coded from the tested pipeline (M3); "field test" undefined; self-reported limitations used as a proxy (M7).
  - *Internal:* no κ; the precedent-based coding drifts toward early decisions; post-hoc analyses.
  - *External:* two search phrases, publisher portals, an MDPI-heavy pool (41/130), English only, an 18-month window, and 2026 truncated at July. Publication bias: field failures are rarely published.
  - *Conclusion:* n = 3–5 cells, multiple comparisons, no tests.
  - The L644 "trend claims" sentence is unsupported, because [4] reports no mode distribution (L676), so there is no baseline to compare against.
- *Fix:* Replace this with a structured "Threats to Validity" subsection, one paragraph per validity type, each with a mitigation. Add a sensitivity analysis (M12) and the pooled test (M2).

**M15. [L436, L674, L742, L740] Trend and causal language is drawn from a cross-sectional 39-paper snapshot.**
- *Quotes:* L436: "a departure from the predominantly human-supervised framings surveyed by the model reference paper's own three-mode HRI account [4]". L742: "the current literature's apparent shift toward full autonomy". L674: "increasingly active area … over the past decade". L740: "The results demonstrate that Fully Autonomous systems dominate current SAR robotics research". L579: "where autonomy is deliberately withheld, research investment shifts toward mechanical capability".
- *Problem:* There is no temporal baseline. The authors themselves state that [4] does not quantify its mode distribution (L676), so neither a "departure" nor a "shift" can be measured. "Dominate current SAR robotics research" generalizes from a two-phrase search to the field. L579 infers intent ("deliberately") and causation from n = 5.
- *Fix:* Replace these with "In this corpus, 27/39 papers…", and delete "departure," "shift," "demonstrate" and "deliberately withheld." If a trend claim is wanted, re-code a sample of [4]'s 74 papers with the same instrument.

**M16. [L619–627, L648–654] The Discussion argues from hand-picked "flagship" anecdotes, slips across categories, and future directions are partly circular.**
- *Quotes:* L621: "is not an artifact of a few weak papers pulling down an average. It holds up at the level of individual flagship examples." L625: "The gap between "Fully Autonomous" succeeding and failing in this corpus concentrates specifically in control and decision execution, not in perception." L654: "documented in both Section IV-D's multi-robot cluster synthesis and [25]'s specific scalability results".
- *Problem:*
  - Anecdotes cannot show that a rate is not an artifact. Only a sensitivity or leave-one-out analysis can.
  - The perception-versus-control generalization rests on one paper ([47]).
  - V-A, on the FA validation gap, uses [20] as evidence, but [20] is classified Shared-Collaborative (L587), not FA.
  - Future direction 5 cites IV-D and [25] as two sources, but IV-D's evidence *is* [25] (L593). Directions 2 and 3 each derive from a single paper.
  - No direction addresses the review's own HRI axis (operator workload, trust, supervisory interfaces, responder involvement).
  - "Standardized real-world validation benchmarks" (L650) ignores the existing NIST/ASTM E54.09 standard test methods for response robots (50+ ground/aerial/aquatic methods), DARPA SubT, and RoboCup Rescue arenas.
  - Mechanisms for the FA gap (cost, airspace regulation, safety-pilot requirements, sim-to-real, venue incentives) get one sentence (L637), and it has no citations.
- *Fix:* Replace the "flagship" rhetoric with a leave-one-out or sensitivity analysis. Restrict V-A evidence to FA papers. Frame directions 2–3 as "illustrated by" rather than "drawn from patterns". Add an HRI-specific direction and a standards/practice direction that engages with ASTM E54.09. Write one paragraph on mechanisms, with citations.

---

## 5. Minor comments

1. **[L436, L571, L573, L605, L617, L641] Working-document language leaks.** "model reference paper" appears six times in manuscript prose, e.g. L617 "rather than in the model reference paper's generic gap list", L641 "for the same reason the model reference paper states its own [4]", and the Fig. 7 caption at L571/573 "this review's structural counterpart to the model reference paper's five-layer system architecture [4]". *Fix:* Replace with "Kareem et al. [4]" or delete. L617's "generic gap list" is also disparaging and unsupported.
2. **[L605] "None of the four verified prior reviews"** and **"as all four verified prior reviews are"** are working-record terms. *Fix:* "the reviews in Table I".
3. **[L633] "than the generic-scenario framing this section originally set out to test"**, and **[L631] "This was checked directly against the extraction data before writing this section"**, narrate the drafting process. *Fix:* Delete both and report the comparison as an exploratory analysis.
4. **[L623] "A further nuance the extraction table's short fields did not capture"**, and **[L591] "a grouping devised for this synthesis rather than a category drawn from the extraction table itself"**, are process notes. *Fix:* Delete the first. Replace the second with "The FA papers were grouped inductively by primary contribution (first author coded, second verified; κ = …)".
5. **[L587, L377] "bucket"** ("not found in the Supervisory bucket"; "an explicit rule bucketing") is jargon. *Fix:* "category".
6. **[L621] "flagship examples"** is rhetoric that implies selection. *Fix:* "illustrative cases, selected because …".
7. **[L371] "for avoiding re-litigating a paper that resurfaces under a different search query"** is jargon and process narration. *Fix:* Delete.
8. **[L365] "An initial fourth criterion … was considered but not retained"** narrates a decision. A 2025+ restriction is an eligibility criterion (PRISMA item 5) wherever it is applied. *Fix:* List it as a criterion and say it was applied at query level. State the upper bound and the search end date.
9. **[L583] Classification justification leaks into synthesis prose:** "(Its headlined validation used autonomous waypoint navigation … does not change this primary classification.)" *Fix:* Move it to the supplementary coding manual.
10. **[L587 vs L583] Contradiction.** SC papers are said to "share a distinguishing feature not found in the Supervisory bucket: each treats the operator's own cognitive or psychological state as a first-class design and evaluation target". But [17] (Supervisory, L583) evaluated "operator reaction time and cognitive workload … and increased trust". *Fix:* Drop "not found in the Supervisory" or qualify it.
11. **[L587] Metric confusion:** "detection recall … as low as 2.6–26.4% mAP". Recall and mAP are different metrics. *Fix:* Check [20] and report one metric correctly.
12. **[L593 vs L623] [25] is described inconsistently.** L593 says "false positives from grass and wind" and degradation "as swarm size grows beyond that one validated unit". L623 says "long grass as obstacles and wind-shaken foliage as false negatives", with degradation measured in pure simulation from 4 to 24 agents. *Fix:* Make the two descriptions agree with the source, and do not imply that the hardware scale was varied.
13. **[L593, L623] [25] is called a "successful sim-to-real transfer" and "the corpus's one genuine sim-to-real success story"** despite "3 of 10 physical collisions" with one physical unit. *Fix:* "partial sim-to-real transfer (one physical unit, 3/10 collisions)".
14. **[L537] Statistical non-sequitur:** "the opposite of what their smaller sample size alone would suggest". Sample size does not predict the direction of a proportion. *Fix:* Delete. Report CIs (Hybrid 57.1% [25.0, 84.2]).
15. **[L457, L555] Absolute statements on tiny cells:** "Teleoperation, conversely, never appears on a bare UAV platform" (n = 5); "All three Shared-Collaborative Control papers use UAV platforms exclusively" (n = 3); "indicating a corpus-wide characteristic … rather than an artifact" (Supervisory 1/4 and SC 1/3 generic, vs FA 16/27). *Fix:* Add "(n = 3)"-style caveats and drop "indicating."
16. **[L471] Non-sequitur:** "This pairs with the Visual-sensor finding". Also, "None (fully abstracted)" is counted as a *modality* in Table VIII/Fig. 4, which is a category error. *Fix:* Report "no sensor modeled" as a separate row below the table, and delete the "pairs with" sentence.
17. **[L506, Table X] The core outcome categories are undefined.** What counts as a "Real-world field test" (outdoor? a disaster-representative site? the DARPA course? an indoor pool, as in [43] at L597; a lab mock-up, as in [17])? *Fix:* Add operational definitions to II-G and list each paper's code in a supplementary table.
18. **[L541, L587, L597] Scenario coding is unclear.** Table XII has Maritime/Water n = 1, but the text describes both [21] ("simulated maritime risk-conflict scenario") and [43] (drowning buoy) as water/maritime. *Fix:* State the coding rule (terrain/setting vs. hazard) and say which paper is which.
19. **[L493] "PC/Offline" is undefined.** It apparently absorbs pure-simulation papers, which conflates compute location with whether a robot exists. *Fix:* Split off "N/A (simulation only)".
20. **[L421] "bibliometric findings"** is a misnomer. There is no bibliometric analysis (years, venues, countries, citations). *Fix:* "coded study characteristics", or add a genuine bibliometric subsection (venue distribution is relevant given MDPI 41/130).
21. **[L309] "conducted between 18–19 July 2026"** implies the entire review took two days. *Fix:* Give separate dates for the search (per source), screening, extraction and analysis.
22. **[L395/Table IV] "12 of the excluded records violated more than one criterion".** 86 + 12 = 98 holds only if none violated all three. *Fix:* State this, or give the full overlap (a Venn diagram or a six-row table).
23. **[L605] Wrong cross-reference:** "precedent-based protocol (Section II-F)". The precedents are described in II-G. *Fix:* "Section II-G".
24. **[L670] Uncited figure:** "killing an estimated 2,200 people" (Afghanistan). *Fix:* Cite CRED [1] if it reports this, or an authoritative source.
25. **[L672] Uncited, implausible range:** "range from just over 20% in some assessments to more than 90% in others", with the only support being a news quote [3] and an arXiv paper [2] for "well established". *Fix:* Replace with peer-reviewed sources (e.g. Macintyre et al. 2006 on the 72-hour survival curve; Murphy 2014), or delete the numbers.
26. **[L674] "increasingly active area … over the past decade"** has no citation or data. *Fix:* Cite a bibliometric source or delete.
27. **[L686, Table I] "15 platforms"** for [6]. The source analyzes 14 (see M10). Table I also omits Tong [8], which the text does discuss, and Shuvo et al. 2026. *Fix:* Correct the count and add rows.
28. **[L730, Abstract] PRISMA abstract items are missing:** information sources, search dates, limitations, registration and funding. "screened under PRISMA 2020 guidelines" is wrong, because PRISMA is a reporting guideline. The Abstract also spends a sentence on positioning ("This review positions itself…") instead of on methods. *Fix:* Restructure using the PRISMA 2020 for Abstracts checklist.
29. **[L744 vs L650–654] The Conclusion's future-work paragraph restates V-E almost item for item, and the Conclusion has no limitations sentence.** *Fix:* Compress it to one sentence and add a sentence on limitations.
30. **[L599 vs L625] [47] (IMPACT-Agent) is narrated twice at length**: the 40% success rate, the untested human-supervision recommendation and the quotes. *Fix:* Keep the detailed account in one place (V-A) and give IV-D a one-line pointer.
31. **[L533–535, L571–573] Captions are evaluative.** "this review's clearest evidenced pattern (Section V-A)" (Fig. 6) and "structural counterpart to the model reference paper's…" (Fig. 7). *Fix:* Use descriptive captions with n and definitions. Add error bars (CIs) to Fig. 6.
32. **[Figs. 3, 5 vs Tables VI, X] The bar charts duplicate their tables exactly.** IEEE Access allows this, but RAS/JFR referees will ask that one be cut. *Fix:* Keep the tables and drop Figs. 3 and 5. Or replace them with a mode × validation stacked bar and a platform × validation chart, which would add information.
33. **[Fig. 2, PRISMA] The box reads "Databases (n = 130)" and then lists publishers.** "Records screened (n = 125) → Records excluded (n = 0)" signals that title/abstract screening was skipped. That is acceptable, but explain it in the caption. *Fix:* Relabel "Publisher platforms," add the search dates, and add an "other methods" column if any records came from citation chasing or other tools (see the author-only note below).
34. **[L699, italic note] The roadmap paragraph is missing**, and the italic note justifying its absence by reference to "the model reference paper" must not reach the submission file. *Fix:* Add a three-line "The rest of this paper is organized as follows" paragraph.
35. **[L695] Contribution 2 is a scope statement, not a contribution:** "the period immediately following, with zero temporal overlap, the most recent and most directly comparable prior review's own 2016–2024 corpus". *Fix:* Merge it into the scope sentence. With [5] covering 2020–2025, it is also not unique.
36. **[Bibliography] Incomplete entries:** [3] has no URL or date; [9] has no DOI; [44] and [46] have no volume or pages; [18] has no pages. [2] is an arXiv preprint; check for a published version. *Fix:* Complete every entry to IEEE style.

---

## 6. What would move this to Accept (ranked by impact ÷ effort)

1. **Fix the headline wording and statistics (low effort, very high impact).** Use "real-world field-tested," not "outside simulation" (M1). Present a binary FA vs human-involved contrast with CIs and Fisher p = 0.006 (M2). Drop "spectrum," "inverse relationship," "recurs" and "would not surface" (M4, M8, M15).
2. **Purge leaked working language and process narration (low effort, high impact).** Minor 1–9, 34. A Q1 editor desk-rejects on "model reference paper" alone.
3. **Move every Discussion-only number into Results (low–medium effort, high impact).** Add Platform × Validation and environmental-limitation tables, each with a definition (M6, M7).
4. **Fix the contradictions (low effort, high impact).** L595/L601 (M5); [6] (M10); [20] used as FA evidence (M16); SC vs Supervisory "distinguishing feature" (Minor 10); [25] descriptions (Minor 12); Tong's window (M10).
5. **Add a supplementary per-study table plus a coding manual (medium effort, high impact).** 39 rows × mode/validation/platform/scenario codes, the seven precedents as rules, mode definitions mapped to LOA theory (M11, Minor 17).
6. **Run the circularity and confounding checks (medium effort, high impact).** Stratify by embodied vs algorithm-only papers, give platform within FA, run a sensitivity analysis without the 3 Abstract/Unspecified papers, and do a leave-one-out (M3, M8, M12).
7. **Double-code and report κ (medium effort).** Mode, validation type and the environmental-limitation variable, on at least a 30% subset (M9, M11).
8. **Write a structured Threats-to-Validity subsection (low–medium effort).** Construct, internal, external and conclusion validity (M14).
9. **Re-run the search in Scopus/WoS/IEEE Xplore with a Boolean string and dates, then update PRISMA (high effort, decisive for rubric dimension 2).** Register an OSF protocol retroactively and add the PRISMA checklist and data availability (M9).
10. **Add a quality appraisal (medium–high effort).** For example, an adapted validation-depth/reproducibility score like [4]'s, or MMAT-style items, and use it in the synthesis (rubric dimension 3).
11. **Rebuild Discussion V-E (medium effort).** Mechanisms paragraph, HRI direction, ASTM E54.09 engagement, and future directions not resting on single papers (M16). Answer RQ3 fully or trim it (M13).

Items 1–8 are achievable in about two weeks and would move the paper to Major Revision. Items 9–10 are needed for a Q1 robotics journal. IEEE Access might accept a tightly scoped version without item 9 if the limitations are frank.

---

## 7. Confidential comments to the editor

The paper contains one genuinely useful, quantifiable observation: field validation is far rarer for FA systems than for human-in-the-loop systems in recent SAR robotics. On my recomputation it is statistically detectable (p ≈ 0.006 pooled). The manuscript around it is not yet a Q1 systematic review. The search is two phrases on publisher portals. There is no appraisal and no reliability statistic. Several headline claims are contradicted by the authors' own tables and figures: the "outside simulation" figure is wrong, and the "spectrum" is non-monotonic in Fig. 6. A plausible circularity, coding by tested pipeline, may inflate the central effect. The prose still carries drafting-stage language that reveals the paper was modeled section by section on a single prior review. I also find the methods description of three fully independent full-text screenings of 125 papers in two days, with no agreement statistic, hard to credit. I would ask for the raw screening logs and per-coder decisions if the paper returns. I recommend reject-and-resubmit rather than outright reject, because the fix path is clear and the core finding would be a worthwhile short review once honestly scoped.

---

## 8. Author-only integrity note (not part of the simulated review; per project CLAUDE.md rule 4)

The manuscript states that identification was "conducted independently by the three authors" (L325), that screening was "performed independently by the three authors" (L371), and that "only findings on which all three agreed were retained" (L397). The project's own audit trail contradicts or does not support these statements:
- Master doc Sec. 2.2 "Internal audit note" (L61) records that records were found via Google Scholar and AI-assisted prompts (ChatGPT, Gemini).
- The Sec. 16 entry at L990 records that Springer (0/14) and Tech Science Press (0/3) had *no* records found by querying those publishers directly.
- L936 records an earlier Limitations draft listing "single-annotator screening, no inter-rater reliability statistic … partial AI-assisted record discovery". The L998 entry deleted those bullets rather than verifying them.

I have not strengthened or defended these Methods claims anywhere in this report, and the authors must not submit them unless they are true. Only the authors can confirm what they actually did. Suggested truthful wording, to be confirmed by the authors:
- *"Records were identified through publisher platforms (MDPI, ScienceDirect, IEEE Xplore, …), Google Scholar, and AI-assisted discovery tools (ChatGPT, Gemini) used to suggest candidate records; every record was then retrieved and verified at its publisher source. Table II reports records by publisher of record."*
- Plus a journal-compliant AI-use disclosure.
- Plus an accurate description of who screened what. If screening was single-annotator, say so, and report a post-hoc double-coded subset with κ.

This also resolves reviewer concern M9(d).

---

**Sources consulted for spot-checks**
- [Delmerico et al. 2019, "The current state and future outlook of rescue robotics," JFR (EPFL record)](https://infoscience.epfl.ch/record/269149?ln=en); [NCCR summary](https://robohub.org/the-future-of-rescue-robotics/)
- [ASTM Subcommittee E54.09 on Response Robots](https://www.astm.org/jurisdiction-e5409); [NIST response robot test methods](https://www.nist.gov/node/1118471)
- [Reality gap survey, arXiv 2510.20808](https://arxiv.org/abs/2510.20808v1) (adjacent work; no SAR-specific quantification found)
- Prior baseline: `research_outputs/2026-11-08_initial_novelty_scan_and_stats.md` (Bakzadeh [6] autonomy coding, Shuvo et al. 2026, *Applied Soft Computing* 2026 SLR)
- Murphy, R. R. (2014), *Disaster Robotics*, MIT Press: cited from reviewer knowledge; the page-level claim is UNVERIFIED in this session.
