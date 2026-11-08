# Literature-scout novelty scan v2 (2026-11-08)

- **Agent:** literature-scout, following the `/novelty-gap-search` protocol.
- **Manuscript source:** `SAR_review_master_document.md` only (Sec. 8; Sec. 13 L666–699; Sec. 14 L730/L740; Sec. 15 L810–904).
- **Earlier work this builds on:** `2026-11-08_initial_novelty_scan_and_stats.md` and `2026-11-08_full_paper_audit.md` §3 C5/C6, §4 M20–M24 and §6.
- **Scope of searching:** 22 web searches (10 in extended mode), 5 bibliographic-API queries (Crossref/Semantic Scholar, including citation chasing of Kareem [4]), and about 45 page/record opens. The full log is in §11.
- **Status:** Complete, except the items marked **UNVERIFIED** in §12. No manuscript text was edited.

---

## 1. Verdicts on the claimed contributions

| # | Claim as tested | Verdict | Key evidence |
|---|---|---|---|
| C1 | No SAR review uses a four-way autonomy/HRI taxonomy as its primary organizing axis, with one label per paper | **STANDS WITH HEDGING** | No SAR review found that does this for a research corpus. Closest work: (i) Bakzadeh et al. [6] code a 14-platform mine-rescue inventory on a three-band Sheridan–Verplank autonomy axis (A1/A2/A3 = 12/1/1). (ii) Kareem et al. [4] *discuss* three HRI modes qualitatively. (iii) Man et al. 2026 (IJHCI) review HMI for *teleoperated* rescue vehicles only. (iv) Shuvo et al. 2026 organize by learning paradigm (H2M/M2M/M2H). |
| C2 | No SAR review cross-tabulates real-world validation against autonomy/HRI mode (FA 2/27 field-tested vs human-in-mission modes) | **STANDS WITH HEDGING** | No review found that cross-tabulates validation by autonomy mode. However, validation prevalence *has* been quantified corpus-wide: Sinha et al. [5] report "only eight papers (4.2%)" on full field deployments and 35 (18.4%) simulation-based. Wu et al. 2026 (Front. Neurorobot.) define a V0/V1/V2 validation-maturity code (no autonomy cross-tab, not SAR-specific). The sim-to-real gap is named as the main barrier in Jamwal & Singh 2026 and Shuvo et al. 2026. The claim has to be the **cross-tabulation**, not "validation was never quantified". The statistics also need fixing (audit C2/C3): this is a binary contrast, not a gradient. |
| C3a | UAV platform–validation mismatch (UAV 1/13 vs Hybrid 4/7) | **STANDS WITH HEDGING** | Nothing comparable found. It is descriptive and post hoc (p = 0.031, n = 13 vs 7), and it is confounded with mode, since Hybrid holds all three Teleoperation papers (audit M15). Present it as exploratory. |
| C3b | 89.7% (35/39) environmental-realism limitation | **STANDS WITH HEDGING** (the number is new; the concept is not) | Shuvo et al. ("many reviewed approaches are primarily validated in simulation or custom experimental environments"), Jamwal & Singh 2026 and Sinha [5] all report the realism/sim-to-real gap qualitatively or as a prevalence. The 35/39 figure is a new *self-report count*, but it needs a coding rule and a Results table (audit C9). Cite these reviews as concordant evidence, not as gaps. |
| C4 | "Not previously reported/quantified in prior SAR robotics reviews"; "first review of 2025–2026" | **THREATENED** as currently worded; **STANDS** if narrowed | (a) Validation prevalence *was* quantified by [5] (4.2% field deployment). (b) 2025 is covered by Shuvo et al. (2005–2025), Sinha [5] (2020–2025), Hu et al. 2026 (bibliometric, 1992–2025) and probably Khalil et al. (years UNVERIFIED). So "first to cover 2025–26" is unsafe. "Zero temporal overlap with [4]" is still true, and "the 2025–2026 primary literature specifically" is defensible. |

**Hedged wording for each claim** (Markdown drop-in; placeholder refs `[N-x]` are defined in §3):

- **C1:** "To our knowledge, this is the first review of disaster SAR robotics to use a four-mode autonomy/HRI classification (Teleoperation, Supervisory Control, Shared-Collaborative Control, Fully Autonomous) as its primary organizing axis for a research-literature corpus, assigning every included study a single primary label. The nearest precedent, [6], applies a coarser three-band Sheridan–Verplank autonomy scale to an inventory of 14 mine-rescue platforms."
- **C2:** "Prior reviews have reported how few SAR robotics studies reach field deployment [5] and have identified sim-to-real transfer as a principal barrier [N-c], [N-a]. To our knowledge, none has cross-tabulated validation type against the level of human involvement in the mission. Doing so here shows that 2 of 27 Fully Autonomous studies (7.4%) were field-tested, compared with 6 of 12 (50.0%) studies with a human in the mission loop (Fisher's exact test, p = 0.006; exploratory)."
- **C3:** "Exploratory platform-level and limitation analyses point the same way. In this corpus, UAV studies were field-tested least often (1 of 13), and 35 of 39 studies (89.7%) self-reported an environmental-realism limitation. This is consistent with qualitative assessments in recent reviews [N-a], [N-c]."
- **C4:** "...not, to our knowledge, previously quantified *by autonomy/HRI mode* in SAR robotics reviews." Drop "first to cover 2025–2026". Keep "the period immediately following the 2016–2024 corpus of [4]".

---

## 2. Verification of the seven requested items (Task 2)

| Item | Verdict | Full citation (verified fields) | Corpus / years | Organizing axis | Codes autonomy/HRI mode? | Counts sim vs real? |
|---|---|---|---|---|---|---|
| (a) Shuvo et al. | **VERIFIED** (full text opened, offsets 0–292k) | M. I. R. Shuvo, A. A. Fime, R. Ashraf, N. Alam, J.-H. Kim, "Learning-enabled collaborative intelligence in search and rescue robotics: a survey of paradigms, models, and challenges," *Front. Robot. AI*, vol. 13, art. 1832982, publ. 14 Oct 2026, doi:10.3389/frobt.2026.1832982 | 130 studies (Fig. 3: "one hundred thirty records included in final synthesis"); 2005–2025; 9 databases (IEEE Xplore, ACM DL, Scopus, SpringerLink, Google Scholar, PubMed, NCBI, CINAHL, WoS). Labelled "Systematic Review" by the journal, but the authors call it "not intended as a fully PRISMA-compliant systematic review". | Learning paradigm: H2M / M2M / M2H | **No.** Human oversight is discussed only generically. | **No counts.** Qualitative only: "primarily validated in simulation or custom experimental environments"; "no current LLM-enabled SAR system has been validated … at operational scale". It does **not** cite Kareem [4] or Sinha [5] (checked in the alphabetical reference list). It does cite Tong [8]. |
| (b) Applied Soft Computing path-planning SLR | **Metadata VERIFIED via Crossref; content UNVERIFIED this pass** (ScienceDirect 403) | Y. Khalil, N. Jafari Navimipour, T. Arsan, M. Hosseinzadeh, "Path planning for search and rescue robots: A systematic and bibliometric review," *Applied Soft Computing*, vol. 204, art. 116380, Jan 2027 issue (online 2026), doi:10.1016/j.asoc.2026.116380 | Earlier scan read "73 articles from 850 Scopus+WoS records" (**UNVERIFIED** this pass); year range unknown. A search snippet says the review is PRISMA-guided and uses VOSviewer. | Path-planning paradigm (graph-, sampling-, swarm/metaheuristic-, learning-based, hybrid) per the search snippet | No (snippet: it does not address teleoperation/HRI) | UNVERIFIED |
| (c) arXiv:2412.20699 | **VERIFIED; peer-reviewed version exists** | Y. Zhang, H. Yan, D. Zhu, J. Wang, C.-H. Zhang, W. Ding, X. Luo, C. Hua, M. Q.-H. Meng, "Air–Ground Collaborative Robots for Fire and Rescue Missions: A Survey From the Mapping and Navigation Perspective," *IEEE Trans. Syst., Man, Cybern.: Syst.*, 2026, pp. 1–15 (early access; vol./issue not yet assigned), doi:10.1109/TSMC.2026.3736745. arXiv v3 (25 Sep 2026) is the accepted version. | Not stated | UAV mapping → UAV/UGV co-localization → UGV navigation; systems also classed by number of UAVs/UGVs | Not stated on the abstract page | Not stated |
| (d) "Autonomous Aerial Robots for Enhanced SAR Operations" | **PREPRINT ONLY. Do not cite as peer-reviewed.** | Y. Alqudsi, E. Aydemir, S. Saif, B. Kerdige, G. Olayei, "Autonomous Aerial Robots for Enhanced Search and Rescue Operations: A Critical Review of Trends, Pitfalls, and Future Methodological Directions," SSRN preprint, 2026, doi:10.2139/ssrn.6810578 (a second SSRN version, doi:10.2139/ssrn.6054114, adds A. Abdallah). Crossref type: posted-content. A related earlier preprint: Alqudsi, Aydemir, Kerdiğe, *Preprints.org* 2025, doi:10.20944/preprints202506.0330.v1. | UNVERIFIED (SSRN 403) | Search snippet: links platform constraints to autonomy-stack modules | UNVERIFIED | UNVERIFIED |
| (e) ESARBench | **VERIFIED (preprint)** | D. Zhang, P. Chen, J. Zhou, S. Yang, "ESARBench: A Benchmark for Agentic UAV Embodied Search and Rescue," arXiv:2605.01371, 2 May 2026 (no journal-ref) | 600 tasks; 4 UE5/AirSim environments built from GIS data | n/a (benchmark) | n/a | Simulation benchmark. The reported bottlenecks are "spatial memory, aerial adaptation, and the trade-off between search efficiency and flight safety". The abstract does **not** separate perception from control, so do not cite it as direct support for the perception-vs-control claim attributed to [47]. Use it only to support the call for standardized benchmarks. |
| (f) Hagenow et al. | **VERIFIED as a preprint; peer-reviewed DOI UNVERIFIED** | M. Hagenow, M. Selvaggio, X. Yu, Y. Wang, Y. Demiris, A. Bobu, Y. Du, H. Soh, D. Losey, J. Shah, "Shared Control/Autonomy in Human-Robot Interaction: Current Trends and the Role of Generative AI." The PDF is typeset for *Int. J. Robot. Res.* with "DOI: 10.1177/ToBeAssigned". The Crossref record found is TechRxiv, 19 Dec 2025, doi:10.36227/techrxiv.176617724.41163595/v1, with a slightly different title ("…: A Historical Perspective, Current Trends, and the Role of Generative AI"). | 195 papers, 2020–2024, from RA-L, ICRA and Science Robotics (search date 18 Mar 2025) | Human-centred SC/SA taxonomy: minimizing human time (31) / input (43) / improving input quality (111) / maximizing output (10) | Defines SC/SA as "an intermediate between manual robot teleoperation and full autonomy" and traces the term to Ferrell & Sheridan's supervisory control. Only 3 "Emergency Response" papers. | No sim/real count; it reports participant counts |
| (g) doi:10.3389/frobt.2025.1540476 | **VERIFIED** | C. A. Contreras, A. Rastegarpanah, M. Chiou, R. Stolkin, "A mini-review on mobile manipulators with Variable Autonomy," *Front. Robot. AI*, vol. 12, art. 1540476, publ. 14 Feb 2025 (Mini Review) | n/a | Variable autonomy (VA): autonomy-changing (mixed-initiative / human-initiative = adjustable / AI-initiative = sliding) vs autonomy-sharing (shared control: supervisory or assistive) | Theory only. It says SAR needs human-robot teams because full autonomy is unreliable under uncertainty. | No |

**How to use (f), (g) and Kim et al. 2024 in Sec. IV:** they ground "Shared-Collaborative" as distinct from Supervisory Control. Kim, Anthis & Sebo, "A Taxonomy of Robot Autonomy for Human-Robot Interaction," *Proc. HRI '24*, pp. 381–393, doi:10.1145/3610977.3634993 (verified via Crossref), is a recent systematic-review-based autonomy taxonomy. Reviewers in HRI will expect it to be cited.

---

## 3. New competitors not cited in the manuscript

| Ref | Citation (verified) | DOI | Scope | Overlap with this review | How to position | Suggested sentence (Markdown) |
|---|---|---|---|---|---|---|
| N-a | Shuvo, Fime, Ashraf, Alam & Kim, *Front. Robot. AI* 13, 2026 | 10.3389/frobt.2026.1832982 | SAR, 130 studies, 2005–2025, learning paradigms | **High** (most recent SAR review; covers 2025) | Different axis (learning paradigm); qualitative on validation; not PRISMA-compliant by its own statement | "Shuvo et al. [N-a] synthesize 130 SAR robotics studies (2005–2025) around human-to-machine, machine-to-machine and machine-to-human learning paradigms, noting that most approaches remain validated in simulation or controlled settings, but they do not classify studies by autonomy mode or quantify validation." |
| N-b | Khalil, Jafari Navimipour, Arsan & Hosseinzadeh, *Appl. Soft Comput.* 204, 116380 (2027 issue; online 2026) | 10.1016/j.asoc.2026.116380 | SAR path planning, PRISMA + bibliometric | Medium; its Scopus/WoS search will be compared with this review's search rigor | Algorithm-family axis; no HRI | "Khalil et al. [N-b] provide a systematic and bibliometric review of SAR path-planning methods, organized by algorithm family rather than by human involvement." (Verify the corpus size before adding numbers.) |
| N-c | Jamwal & Singh, "Comprehensive Survey on Autonomous Disaster Reconnaissance: A Comparative Analysis of UAVs and UGVs," *Telecom* 7(2), 31, 16 Mar 2026 | 10.3390/telecom7020031 | UAV vs UGV software (perception, navigation, coordination) for disaster reconnaissance | **High**, on platform comparison and sim-to-real | Abstract (verified) names the sim-to-real gap, missing disaster benchmarks and DRL explainability as the main deployment barriers. Whether it codes autonomy mode is **UNVERIFIED** (full text 403). It shares an author (S. Singh) with [5]. | "Jamwal and Singh [N-c] compare UAV and UGV reconnaissance software and identify sim-to-real transfer as a principal barrier to field deployment; the present review quantifies that barrier by autonomy mode." |
| N-d | Zhang et al., *IEEE Trans. SMC: Systems*, 2026, pp. 1–15 (early access) | 10.1109/TSMC.2026.3736745 | Air–ground (UAV+UGV) fire and rescue, mapping and navigation | Medium; relevant to the Hybrid/Multi-Platform discussion | Technical-pipeline axis | "Air–ground collaborative systems for fire and rescue have been surveyed from a mapping-and-navigation perspective [N-d]." |
| N-e | Chen, Rushworth & Jia, "A Review on Search and Rescue Robots in Complex Scenarios: Key Technologies of SLAM," *J. Field Robot.* 43(7), 4783–4820, 2026 | 10.1002/rob.70256 | SAR SLAM | Low–medium | Single-technology axis | Add one Table I row or one sentence: "…and SLAM for SAR robots in GNSS-denied, unstructured environments [N-e]." |
| N-f | Hu, Komagata, Kanbara, Yu & Jiang, "The Shifting Paradigms of Disaster Robotics: Three Decades of Research," *J. Field Robot.* 43(6), 3783–3793, 2026 | 10.1002/rob.70223 | Bibliometric, 2,201 WoS papers, 1992–2025 | Medium; supports the "growing body" sentence (L674, audit m7) | Bibliometric, no study-level coding | "Bibliometric analysis of 2,201 disaster-robotics papers (1992–2025) shows sustained growth and a shift from hardware toward perception and learning-enabled intelligence [N-f]." |
| N-g | Man, Jiang, Zhou, Tong & Chan, "Human-Machine Interaction in Teleoperated Rescue Vehicles: A Bibliometric Analysis and Systematic Review," *Int. J. Hum.-Comput. Interact.* 42(18), 14819–14846, 2026 | 10.1080/10447318.2026.2618584 | HMI in teleoperated rescue vehicles | **Medium–high for C1**: an HRI-focused SAR review, but for one mode (teleoperation) only | Single-mode; human-factors axis. It notes that most studies use virtual or physical setups. Corpus size not visible (UNVERIFIED). Name form: Crossref gives "Siu Shing Man", Semantic Scholar gives "Shing-Man Siu", so confirm the family name. | "Man et al. [N-g] review human-machine interaction for teleoperated rescue vehicles, but restrict attention to a single (teleoperation) mode." |
| N-h | Wu, Chow, Wong, Chuah, Kanesan & Zhang, "AI-driven quadruped robots: from fundamental locomotion to advanced biomimetic behaviors," *Front. Neurorobot.* 20, 1855550, 23 Jul 2026 | 10.3389/fnbot.2026.1855550 | Quadrupeds, 287 studies, PRISMA-style, 2000–2025/26 | **Medium for C2**: defines validation maturity V0 (simulation/theory) / V1 (controlled hardware) / V2 (field). No counts were visible and there is no autonomy cross-tab. | Methodological precedent for validation coding; not SAR | "Validation-maturity coding has been proposed for legged robotics [N-h]; we apply an analogous scheme to SAR and cross-tabulate it against autonomy mode." |
| N-i | Kim, Anthis & Sebo, *Proc. HRI '24*, 381–393 | 10.1145/3610977.3634993 | Autonomy taxonomy for HRI | Theory | Grounding for C1 | Cite in Sec. IV with Beer et al. 2014 and Parasuraman et al. 2000. |
| N-j | Contreras, Rastegarpanah, Chiou & Stolkin, *Front. Robot. AI* 12, 1540476, 2025 | 10.3389/frobt.2025.1540476 | Variable autonomy | Theory | Grounds Shared-Collaborative and variable autonomy | "Shared control (supervisory or assistive) is distinguished from autonomy-changing schemes in the variable-autonomy literature [N-j]." |
| N-k | Delmerico et al., "The current state and future outlook of rescue robotics," *J. Field Robot.* 36(7), 1171–1191, 2019 | 10.1002/rob.21887 | Rescue robotics readiness against responder needs | Pre-2025 anchor | Supports the deployment-readiness framing in Sec. V | "Earlier readiness assessments already found a gap between laboratory capability and responder requirements for robustness and ease of use [N-k]." |
| (optional) | Hagenow et al., TechRxiv 2025 (IJRR-formatted) | 10.36227/techrxiv.176617724.41163595/v1 | Shared control/autonomy, 195 papers | Theory | Cite only as a preprint unless the IJRR DOI appears | — |
| (do not cite as peer-reviewed) | Alqudsi et al., SSRN 2026 | 10.2139/ssrn.6810578 | UAV SAR | — | Preprint | — |

**Citation chasing of Kareem [4]** (Semantic Scholar, 9 citing records): no citing record is a SAR review using autonomy-mode classification. The citing set comprises primary studies, one ISCRAM paper, a multi-UAV collision-avoidance survey (*Comput. Sci. Rev.*, doi:10.1016/j.cosrev.2026.101045) and a narrative drone-applications article.

---

## 4. Re-verification of manuscript statements about [4]–[8] (Task 3) and factual errors

| # | Manuscript text (line) | What the source says | Status | Fix |
|---|---|---|---|---|
| E1 | L676: "Bakzadeh et al. [6], reviewing three decades of mine search-and-rescue robot platforms, explicitly exclude autonomy and control software from their stated scope" | The scope sentence is real, verbatim on Frontiers and PMC: "the autonomy, mapping, SLAM, path planning, and software architecture of CMRRs are not reviewed". **But** [6] still codes every classifiable platform for autonomy. Table 7 caption: "Three-axis taxonomy of reviewed CMRRs", with "Axis A follows the Sheridan–Verplank scale". Bands: "A1 teleoperated (Levels 1–4, operator retains all decision authority)", A2 semi-autonomous (5–7), A3 fully autonomous (8–10). Count: "Of the 14 reviewed platforms, 12 are classified A1, one achieves A2 (CUMT-V), and one achieves A3 (Groundhog/Cave Crawler)." Footnote: "MINBOT-II supports switchable A1 and A3 modes; no intermediate A2 behavior is reported by the developers." | **Mischaracterization (rejection-level)** | Use the rewrite in §5. "Control software" is not the source's wording; use "autonomy algorithms and software architecture". |
| E2 | Table I L686: "Mine/underground rescue robots only, 15 platforms" | **Both 14 and 15 appear, and both are correct for different things.** 15 is the scope: "a systematic description of the mechanical design and sensor suite combinations of 15 documented CMRRs"; "None of these works cover all 15 documented CMRRs"; Table 2 caption "coverage of the 15 CMRR platforms identified in the present survey". 14 is the classification: Table 7 classifies 14 because KQR48 is excluded for insufficient data ("the KQR48 CMRR is not included due to a lack of available information"). | **Open item M22 RESOLVED** | Table I: "15 documented coal-mine rescue platforms (14 classified)". Any autonomy count must use 14 (12/1/1). |
| E3 | Table I L686 "Gap" column: "Autonomy and control software explicitly excluded from scope"; Sec. 8B "Doesn't address autonomy/HRI mode at all"; Sec. 8C "explicitly excludes autonomy from its scope" | Contradicted by the Axis A coding above. The manuscript itself uses [6] at L555 for "predominantly teleoperation-oriented", which only makes sense because [6] codes autonomy. | **Error** | Replace with: "Autonomy algorithms are outside scope, but platforms are coded on a three-band Sheridan–Verplank autonomy axis (12/14 teleoperated); platform inventory, single hazard type, no validation analysis". |
| E4 | L676 and Table I: "Sinha et al. [5] reviewed 190 papers" / "190 papers" | "The analysis synthesizes findings from over 190 recent studies (2020–2025)" (PMC12986560). Note also that the Sec. 2.2 category counts in [5] sum to 180, and the text and Table 1 disagree (35 vs 36 simulation-based). | **Minor misquote** | "over 190 studies". |
| E5 | L676: "organize their corpus by research-method type (algorithm development, simulation, experimental, hardware, and comparative studies)" | [5]: "Papers were categorized based on research type (e.g., simulation, experiment, algorithm development)". Table 1 has **eight** categories: experimental, simulation-based, review, theoretical, field deployment, algorithm development, hardware platform, comparative analysis. The manuscript lists five and omits "field deployment", the category most relevant to this paper's claim. The survey body itself is organized by technical topic (hardware, algorithms, field/lab performance), so "research type" is the corpus-categorization scheme, not necessarily the primary organizing axis. | **Incomplete / slightly mis-framed** | "categorize their corpus by research type (eight categories, including simulation-based and field-deployment studies)". |
| E6 | L690: "none of the reviewed prior works evaluate the relationship between autonomy level and validation rigor" | True for the relationship. But [5] **does** quantify validation prevalence ("only eight papers (4.2%) focused on full field deployments"). The manuscript never mentions this, and a reviewer will see it as selective. | **Omission (major)** | Acknowledge [5]'s 4.2% figure explicitly and frame C2 as the cross-tabulation. |
| E7 | L676/Table I: "[5] … restrict their scope to unmanned ground vehicles" | "This survey focuses exclusively on Unmanned Ground Vehicles (UGVs)"; "the survey intentionally excludes aerial (UAV) systems", with an exception for direct comparative data. Also "multi-database screening" holds: databases are named (inconsistently across sections) and there is no PRISMA. | **Correct** | Optionally add "(UAV studies admitted only for direct comparison)". |
| E8 | L676: "Kareem et al. [4], a systematic review of 74 SAR robotics papers published between 2016 and 2024 in *IEEE Access*" | Metadata verified via Crossref: Kareem, Abid, Hammood, Al-Naji, Chahl, *IEEE Access* 14, 19157–19182, 2026. 74 papers / 2016–2024 / five-layer architecture are corroborated by an aggregator abstract (synapsesocial). The full text could **not** be opened this pass (IEEE returned 418/empty), so "3 modes, no FA bucket, no mode distribution" rests on the user-supplied PDF (Sec. 8A): **UNVERIFIED this pass**. | **Ambiguous phrasing** (it reads as if the 74 papers were published in IEEE Access) | "Kareem et al. [4] (*IEEE Access*, 2026) systematically reviewed 74 SAR robotics papers published between 2016 and 2024…". Separately: **the authors must check their [4] PDF** for whether its quality/validation score (the audit mentions a 1–6 score) or any table reports a simulation vs real-world split. If it does, C2/C4 must cite it. |
| E9 | L676: Tong [8] "falls outside both this review's 2025–2026 window and the 2016–2024 corpus in [4]" | Tong et al., *2024 IEEE IV*, pp. 953–960, 2 Jun 2024 (Crossref verified). 2024 is **inside** 2016–2024. The real point is that [4] reviewed primary studies, not reviews. The content claim ("compared UAV and UGV software approaches") was not re-verified this pass (no abstract retrieved): **UNVERIFIED this pass**, recorded as verified in Sec. 8E. | **Logical error** (audit M24 confirmed) | "…noted here as an immediate predecessor in framing rather than as a structurally comparable peer, since it is itself a review rather than a primary study of the kind analysed in [4] or here." |
| E10 | L672: "well established in the SAR and disaster-robotics literature [2]"; "range from just over 20% … to more than 90%" | [2] (Tabib et al.) uses the 72-hour framing only. The 20%–90% range has no source. | **Unsupported** | Replace with the peer-reviewed sources in §6. |
| E11 | Table I L687 [7] | Not re-opened this pass. Earlier verification (Sec. 8B, citation-verifier: OK) stands. | OK | — |

---

## 5. Recommended edits (Markdown drop-ins for the `.md`; the authors to apply and log in Sec. 16)

New references are marked `[N-a]`… as in §3. They must be renumbered by first appearance under CLAUDE.md rule 7. Inserting them in Sec. I will shift every corpus reference number.

### 5.1 Introduction: replacement for L674–L676

> RSAR has consequently become an increasingly active area of research and deployment; a bibliometric analysis of 2,201 disaster-robotics publications from 1992 to 2025 documents sustained growth and a shift from hardware development toward perception- and learning-enabled systems [N-f], accompanied by a growing number of reviews.
>
> The most directly comparable prior work is the systematic review by Kareem et al. [4] (*IEEE Access*, 2026), which covered 74 SAR robotics papers published between 2016 and 2024. That review proposes a five-layer system architecture (Human-Robot Interaction (HRI), Perception, Navigation, Control, and Robot layers) and discusses three HRI modes: teleoperation, supervisory control, and collaborative control. It does not treat full autonomy as a separate category, and it does not report how its 74 papers distribute across the three modes. Sinha et al. [5] surveyed over 190 studies (2020–2025) on ground-based reconnaissance robots for disaster management, admitting UAV work only for direct comparison, and categorized them by research type (eight categories, from algorithm development and simulation to field deployment); they found that only 4.2% of studies reported full field deployments, but did not relate validation to autonomy or HRI mode. Jamwal and Singh [N-c] compared UAV and UGV software for disaster reconnaissance and identified the sim-to-real gap as a principal barrier to field deployment. Shuvo et al. [N-a] synthesized 130 SAR studies (2005–2025) around human-to-machine, machine-to-machine, and machine-to-human learning paradigms, observing that most approaches are validated in simulation or controlled settings without quantifying this. Other recent reviews are organized around single technologies, such as path planning [N-b], SLAM [N-e], and air–ground mapping and navigation [N-d], or around a single interaction mode, such as human-machine interaction in teleoperated rescue vehicles [N-g]. For mine rescue, Bakzadeh et al. [6] describe 15 documented coal-mine rescue platforms. They place autonomy algorithms and software architecture outside their scope, yet code 14 of the platforms on a three-band autonomy scale adapted from Sheridan and Verplank; 12 of the 14 are teleoperated. An earlier paper by an overlapping author team [7] sets out interface-design guidelines for mining emergency robots without reporting a built or tested system. Tong et al. [8] reviewed UAV and UGV approaches to SAR in harsh environments in 2024; it is cited here as an immediate predecessor in framing rather than as a structurally comparable peer, because it is itself a review rather than a primary study of the kind analysed in [4] or here. To our knowledge, none of these reviews organizes a research corpus primarily by the degree of human involvement in the mission, and none cross-tabulates that involvement against validation type. These two gaps define this review's organizing axis and its central analysis.

(The Tong content clause is UNVERIFIED this pass; keep it only if the Sec. 8E verification stands.)

### 5.2 Table I: corrected and added rows

| Prior Review | Scope | Corpus / Method | Primary Organizing Axis | Gap vs. This Review |
|---|---|---|---|---|
| Kareem et al. [4] | UAV/UGV/UUV, general SAR | 74 papers, 2016–2024, PRISMA | Five-layer system architecture (HRI/Perception/Navigation/Control/Robot) | HRI is one layer of five, with 3 modes and no Fully Autonomous category; no per-paper mode distribution reported |
| Sinha et al. [5] | UGV (UAV only for comparison) | Over 190 studies, 2020–2025, multi-database, not PRISMA | Research-type categories (8, incl. simulation and field deployment) | Reports field-deployment prevalence (4.2%) but no autonomy/HRI-mode classification or cross-tabulation |
| Shuvo et al. [N-a] | General SAR, learning-enabled collaboration | 130 studies, 2005–2025, structured narrative (not fully PRISMA-compliant by its own statement) | Learning paradigm (H2M/M2M/M2H) | No autonomy-mode classification; validation discussed qualitatively only |
| Jamwal & Singh [N-c] | UAV vs UGV disaster reconnaissance | Survey (method UNVERIFIED) | Software function (perception/navigation/coordination) by platform | Names the sim-to-real gap as the main barrier; does not classify by autonomy mode (UNVERIFIED) |
| Khalil et al. [N-b] | SAR path planning | Systematic + bibliometric (corpus UNVERIFIED) | Path-planning algorithm family | No HRI/autonomy axis |
| Man et al. [N-g] | Teleoperated rescue vehicles | Bibliometric + systematic review | Human, vehicle and environmental HMI factors | Single mode (teleoperation) only |
| Bakzadeh et al. [6] | Coal-mine rescue robots | 15 documented platforms (14 classified), narrative survey | Mechanical/sensor design requirements plus a three-axis platform taxonomy | Autonomy algorithms out of scope; coarse three-band Sheridan–Verplank autonomy coding of a platform inventory (12/14 teleoperated); single hazard; no validation analysis |
| Bakzadeh et al. [7] | Mine rescue interface design | Narrative guideline synthesis | HRI/interface-design principles | No empirical corpus |
| **This review** | UAV/UGV/legged/USV, general SAR | 39 papers, 2025–2026, PRISMA 2020 | Four-way autonomy/HRI mode | — |

(Optional rows: Chen et al. [N-e], Zhang et al. [N-d]. Fill the UNVERIFIED cells only after opening the full texts.)

### 5.3 L690: replacement

> Prior reviews have documented that field deployment remains rare in SAR robotics [5] and that the sim-to-real gap is a principal obstacle [N-c], [N-a]. To our knowledge, however, none has examined whether that gap differs with the level of human involvement in the mission. Classifying all 39 included studies on a single four-way autonomy/HRI axis allows this comparison. It reveals a contrast between Fully Autonomous systems and systems with a human in the mission loop, which a review organized by platform type, sensor modality or system layer would not directly expose.

### 5.4 Abstract: replacement for the novelty sentence (L730)

Replace "A review organized around any axis other than autonomy would not surface this pattern, which has not been reported previously in this literature." with:

> Earlier reviews have reported how rarely SAR robots reach field deployment, but, to our knowledge, none has related validation to autonomy/HRI mode.

Also fix the comparator per audit C2: "…field-tested in 2 of 27 cases (7.4%), compared with 6 of 12 (50.0%) for modes with a human in the mission loop".

### 5.5 Contributions list (L695–L696)

- Item 2: "a systematic review of the 2025–2026 SAR robotics primary literature, the period immediately following the 2016–2024 corpus of [4]". Delete "with zero temporal overlap" from the contributions list; keep it in the body if wanted.
- Item 3: replace "not previously reported in prior SAR robotics reviews" with "not, to our knowledge, previously quantified by autonomy/HRI mode in SAR robotics reviews".

---

## 6. Survival-window sources to replace [2]/[3] (Task 4)

None of the verified peer-reviewed sources gives a single "X% alive at 24 h / Y% at 72 h" survival curve. The SAR-medicine literature explicitly argues **against** a universal cutoff. So the Introduction should drop the "20% to >90%" range and the precise percentages, and state the qualitative shape with these sources:

| Source (verified) | DOI / ID | Exact figures reported |
|---|---|---|
| A. G. Macintyre, J. A. Barbera, E. R. Smith, "Surviving collapsed structure entrapment after earthquakes: a 'time-to-rescue' analysis," *Prehosp. Disaster Med.*, vol. 21, no. 1, pp. 4–17, 2006 | doi:10.1017/S1049023X00003253; PMID 16602260 | 34 earthquakes (1985–2004). Of 48 medical articles with time-to-rescue data, 25 described multiple rescues after 48 h. Media reports showed rescues beyond day 2 in 18 of 34 earthquakes, with the longest reliable survival at 14 days and a mean maximum survival of 6.8 days (median 5.75). The authors caution that the data may not transfer to non-earthquake collapses. |
| A. G. Macintyre, J. A. Barbera, B. P. Petinaux, "Survival Interval in Earthquake Entrapments: Research Findings Reinforced During the 2010 Haiti Earthquake Response," *Disaster Med. Public Health Prep.*, vol. 5, no. 1, pp. 13–22, 2011 | doi:10.1001/dmp.2011.5 (verified via Crossref and the PDF) | States that "the majority of documented live rescues are accomplished within the first 5 to 6 days" (PDF p. E2). Notes that US teaching emphasized a "golden 48 hours". Argues against "a single time interval applicable to all incidents". |
| M. de Bruycker et al., "The 1980 earthquake in southern Italy: rescue of trapped victims and mortality," *Bull. World Health Organ.*, vol. 61, no. 6, pp. 1021–1025, 1983 | PMID 6609007; PMCID PMC2536241 (**no DOI**; do not invent one) | 80% of trapped people were extricated within 2 days, mostly without sophisticated equipment. Survival probability fell sharply with delay to extrication, and the authors stress the first 48 h. (The "192 of 202 deaths" figure needs re-reading in the PDF before use.) |
| H. Kaya Özdoğan et al., "Factors affecting mortality in patients undergoing surgical procedures after the 2023 Türkiye earthquake," *Ulus. Travma Acil Cerrahi Derg.*, vol. 31, no. 4, pp. 381–388, 2025 | doi:10.14744/tjtes.2025.68317; PMID 40211639 | 637 surgical patients from 4,622 admitted victims; mortality 3.9%. Extrication time predicted mortality (AUC 0.895; optimal cut-off 21 h, sensitivity 78.9%, specificity 86.4%). |

**Suggested L672 replacement:**

> Time-to-rescue strongly shapes survival after structural collapse. In the 1980 southern Italy earthquake, survival fell sharply the longer extrication was delayed, and most trapped people were reached within two days [S1]. In a 2023 Türkiye cohort, extrication time was among the strongest predictors of mortality [S2]. Live rescues beyond 48 hours are nonetheless well documented, occasionally after more than a week [S3], and disaster-medicine reviews caution against any single universal survival cutoff [S4]. The consistent message is that survival probability declines as entrapment lengthens, which places a premium on locating victims quickly while limiting responders' exposure to unstable structures.

Keep [2] (Tabib et al.) only as a robotics example of the 72-h framing. Drop [3] (NBC/Godby) or keep it only as attributed colour.

---

## 7. Sim-to-real / field-validation sources for the Discussion (Task 5)

| Source (verified) | DOI | What it supports (paraphrase) |
|---|---|---|
| E. Salvato, G. Fenu, E. Medvet, F. A. Pellegrino, "Crossing the Reality Gap: A Survey on Sim-to-Real Transferability of Robot Controllers in Reinforcement Learning," *IEEE Access*, vol. 9, pp. 153171–153187, 2021 | 10.1109/ACCESS.2021.3126658 | Simulators only approximate dynamics and interactions, so controllers trained in simulation can fail on physical robots. This is the mechanism behind the FA/simulation-heavy pattern. |
| W. Zhao, J. Peña Queralta, T. Westerlund, "Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey," *Proc. IEEE SSCI*, pp. 737–744, 2020 | 10.1109/SSCI47803.2020.9308468 | Surveys the remedies (domain randomization, domain adaptation and related methods) that FA/DRL SAR papers would need before field use. |
| A. Afzal, D. S. Katz, C. Le Goues, C. S. Timperley, "Simulation for Robotics Test Automation: Developer Perspectives," *Proc. IEEE ICST*, 2021 | 10.1109/ICST49551.2021.00036 | In a survey of 82 practitioners, 84% use simulation for testing, and the reality gap is among the top challenges. Simulation reliance is endemic, not SAR-specific. |
| J. Delmerico et al., "The current state and future outlook of rescue robotics," *J. Field Robot.*, vol. 36, no. 7, pp. 1171–1191, 2019 | 10.1002/rob.21887 | Assesses rescue-robot readiness against first-responder needs (robustness, speed, ease of use). Provides the external anchor for "capability is not field readiness". |
| (SAR-specific, recent) Jamwal & Singh 2026 [N-c] | 10.3390/telecom7020031 | Names the sim-to-real gap and the lack of disaster benchmarks as the main barriers to deployment. |
| (optional) S. Höfer et al., "Sim2Real in Robotics and Automation: Applications and Challenges," *IEEE Trans. Autom. Sci. Eng.*, 2021 | 10.1109/TASE.2021.3064065 | Title and authors verified via Semantic Scholar; abstract, volume and pages **UNVERIFIED**. Cite only after opening. |

---

## 8. Gap side (what no review addresses)

1. **Cross-tabulation of autonomy mode against validation level in SAR.** Not found anywhere. *This manuscript's data supports it.*
2. **A validation-maturity standard for autonomous SAR robots** (V0/V1/V2 exists for quadrupeds [N-h]; NIST/ASTM E54.09 test methods exist but are not used as review coding). *The data partially supports this* (the Validation Type field).
3. **Per-function autonomy profiling** (perception vs navigation vs decision), in the style of Parasuraman et al. 2000. Not done in any SAR review. *Not supported* by the single-label coding; list it as future work.
4. **Operational-scale validation of LLM/MLLM SAR agents.** Shuvo et al. state that none exists, and ESARBench is simulation-only. *Supported in part* ([47]).
5. **Responder-in-the-loop evaluation.** Man et al. [N-g] cover teleoperation only. *Supported* (Shared/Supervisory papers).

---

## 9. Searches that found nothing threatening (evidence for C1/C2)

- No 2024–2026 SAR, USAR, mine, maritime, wildfire, legged or multi-robot review was found that (i) uses autonomy/HRI mode as its primary axis with per-study labels, or (ii) cross-tabulates validation type by autonomy mode.
- Wildfire and maritime searches returned no peer-reviewed review of this kind (mostly press/vendor items, a 2026 *Drones* maritime-UAV review, and a 2026 drowning-rescue review). These were not opened beyond snippets, so they are not citable claims.

---

## 10. Earlier verdicts, revised

| Earlier scan | Now |
|---|---|
| C1 STANDS (hedge) | **Unchanged.** Add [N-g] and [N-i] to the hedge. |
| C2 STANDS | **Changed to STANDS WITH HEDGING.** [5] quantifies field-deployment prevalence (4.2%) and [N-h] defines validation maturity. |
| C3 STANDS | **Changed to STANDS WITH HEDGING** for both parts. |
| C4 THREATENED | **Unchanged.** It is now evidenced by four 2026 reviews covering 2025. |
| Bakzadeh 14 vs 15 | **Resolved:** 15 documented, 14 classified (KQR48 excluded). |

---

## 11. Search log (PRISMA-S evidence)

All searches were run on **2026-11-08** with the WebSearch tool (US index). "Ext" = extended mode, "Std" = standard mode.

| # | Query | Mode | Results opened / verified |
|---|---|---|---|
| S1 | "Safe Search and Rescue Operations Based on Autonomous Robots" systematic review general system architecture IEEE Access | Std | synapsesocial (429); doi.org → ieeexplore 11370140 (empty); stamp.jsp (418); Crossref record ✔ |
| S2 | "Path planning for search and rescue robots" systematic and bibliometric review Applied Soft Computing 2026 | Ext | sciencedirect S1568494626018284 (403, twice) |
| S3 | Kareem Abid Hammood Al-Naji Chahl 2026 search and rescue autonomous robots systematic review five-layer architecture | Std | snippets only |
| S4 | Khalil Navimipour Arsan Hosseinzadeh path planning search and rescue robots systematic bibliometric review … | Std | no hit |
| S5 | "Autonomous Aerial Robots for Enhanced Search and Rescue Operations" critical review trends pitfalls … | Std | ResearchGate (403); SSRN (403); Crossref ✔ |
| S6 | search and rescue robots systematic review 2026 levels of autonomy teleoperation human-robot interaction | Ext | Bakzadeh PMC ✔; Chen JFR (403 → Crossref ✔); SSRN Alqudsi |
| S7 | disaster response robotics review autonomy level real-world validation simulation gap field testing 2025 | Ext | Telecom 7(2):31 (403 → Crossref/S2 ✔) |
| S8 | urban search and rescue USAR robots survey 2025 human-robot teaming shared autonomy | Ext | snippets (older surveys) |
| S9 | UAV drone search and rescue systematic review 2025 2026 victim detection deep learning | Std | snippets |
| S10 | survival probability trapped victims earthquake time to extrication rescue 24 hours 72 hours study | Ext | INSARAG PDF (Macintyre 2011) ✔; scispace (empty); PubMed (cookie) → Europe PMC ✔ ×3 |
| S11 | multi-robot search and rescue survey 2025 heterogeneous UAV UGV coordination review | Std | snippets |
| S12 | large language models embodied AI disaster response robotics survey 2025 2026 | Ext | snippets |
| S13 | levels of autonomy taxonomy field robots review teleoperation supervisory shared autonomy classification 2024 2025 | Ext | Kim et al. HRI'24 → Crossref ✔ |
| S14 | maritime search and rescue unmanned surface vehicle review 2025 | Std | snippets |
| S15 | firefighting wildfire robots review 2025 autonomous UGV UAV field deployment | Std | snippets (press only) |
| S16 | arXiv 2026 survey search and rescue robotics autonomy human-in-the-loop field validation | Ext | snippets |
| S17 | rescue robot bibliometric analysis 2025 Web of Science Scopus disaster robotics trends | Std | Hu et al. JFR → Crossref ✔; cityu-dg (Man et al.) ✔; frobt.2025.1605682 (opened; irrelevant, industrial cobots) |
| S18 | legged quadruped robots disaster response search and rescue review 2025 | Std | Wu et al. Front. Neurorobot. ✔ (offsets 0–200k) |
| S19 | mine rescue robot review 2025 underground emergency robots autonomy teleoperation | Std | snippets |
| S20 | human-swarm interaction search and rescue review 2025 UAV swarm operator | Std | snippets |
| S21 | systematic review robotics proportion of studies validated in simulation only versus real world field experiments reality gap | Ext | snippets (no quantitative meta-review found) |
| S22 | deep reinforcement learning search and rescue robots review sim-to-real 2025 2026 | Std | snippets |

**Bibliographic-API queries and direct opens:**

- Crossref works: 10.1109/ACCESS.2026.3660002, 10.1109/TSMC.2026.3736745, 10.1002/rob.70256, 10.3390/telecom7020031, 10.1002/rob.70223, 10.1109/ACCESS.2021.3126658, 10.1109/SSCI47803.2020.9308468, 10.1002/rob.21887, 10.1001/dmp.2011.5, 10.1145/3610977.3634993, 10.1109/IV55156.2024.10588685; 10.1109/TASE.2021.3064065 (429).
- Crossref title queries: Khalil et al. ✔; Alqudsi et al. ✔; Hagenow et al. ✔.
- Semantic Scholar: telecom7020031 ✔; Kareem [4] citations (citation chasing) ✔; Salvato ✔; Afzal ✔; Höfer (no abstract); Man et al. ✔; asoc.2026.116380 (429); Tong (429).
- Europe PMC: Sinha [5] ✔ → PMC12986560 full text ✔; Kaya Özdoğan ✔; Macintyre 2006 ✔; de Bruycker ✔.
- Direct opens: Frontiers frobt.2026.1857704 (3 offsets) ✔; PMC13487453 (2 offsets) ✔; Frontiers frobt.2026.1832982 (3 offsets) ✔; frobt.2025.1540476 ✔; arXiv 2412.20699 ✔; arXiv 2605.01371 ✔; collab.me.vt.edu Hagenow PDF ✔ (pp. 1–2, 4–7 read); MDPI s26051659 (403); MDPI telecom PDF (403).

---

## 12. UNVERIFIED / unfinished items

1. Kareem [4] full text was not openable this pass. The "3 modes / no FA / no distribution" claims rest on the user-supplied PDF (Sec. 8A). **Authors: also check whether [4] reports a simulation/real split or a validation score.**
2. Khalil et al. [N-b]: corpus size, years and databases (ScienceDirect 403; Semantic Scholar 429).
3. Jamwal & Singh [N-c]: method, corpus and whether it codes autonomy (MDPI 403).
4. Man et al. [N-g]: corpus size and years; author family-name form.
5. Tong [8]: content claim not re-read this pass.
6. Hagenow et al.: final IJRR DOI (cite the TechRxiv DOI until it is assigned).
7. Höfer et al. 2021: volume, pages and abstract.
8. de Bruycker 1983: the "192 of 202" figure needs a direct PDF read (PMC2536241) before use.
9. Bakzadeh [6]: the identities of Axes B and C in Table 7 were not captured (a search snippet suggests one is the communication channel).
