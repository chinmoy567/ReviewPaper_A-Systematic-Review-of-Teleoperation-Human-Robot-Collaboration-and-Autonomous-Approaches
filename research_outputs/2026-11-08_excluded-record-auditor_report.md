# Excluded-record audit: independent second screen of 23 of 86 exclusions

**Agent:** excluded-record-auditor · **Date:** 2026-11-08 · **Status:** report only. No screening decision was changed; nothing in the master document was edited.

**Method caveat (read first):** this is a **post-hoc, AI-assisted check** run by one model on a **non-random, borderline-enriched sample** (7 mandatory borderline records + all 12 multi-criterion records + 4 random). It is not a second human screener and cannot replace one. Do not report it in the manuscript as inter-rater reliability.

---

## 1. Inputs and parsing

- Criteria C1–C3: master doc Sec. 2.1 / Sec. II-E. Checked against the original wording in `assets/docs/Paper Title and Criteria.docx`; the meaning is the same.
- Screening log: `assets/docs/Paper Selection List.docx`. I unzipped `word/document.xml`, stripped the tags and parsed the table. It gives **125 rows: 39 INCLUDED, 86 EXCLUDED**. Record IDs 12, 86, 102, 108 and 130 are absent, which matches the removed duplicate copies (04/12, 61/86, 99/102, 105/108, 110/130).
- **Written to `supplementary/screening_log.csv`** (columns: record_id, title, decision, criteria_violated, logged_reason). This is a parse only; no decision was altered. `criteria_violated` was taken from the criterion prefix of each logged reason (e.g. "C1/C2:"). All 86 exclusions carry such a prefix.
- The log's criterion counts match master doc Sec. 2.3 exactly:
  - Single-criterion exclusions: C1 alone 56, C2 alone 17, C3 alone 1.
  - Multi-criterion exclusions: C1/C2 6, C2/C3 5, C1/C3 1, i.e. **12 multi-criterion records**.
  - Totals counted under each criterion: C1 = 63, C2 = 28, C3 = 7, summing to 98 counts over 86 unique records.
- PDFs: `assets/papers/Q? <id> <title>.pdf`. Text was extracted with `pdftotext -layout` and also in reading order (plain `pdftotext`). The two-column layouts interleave under `-layout`, so all quoted snippets come from the reading-order text. **Page numbers are PDF page indices** (form-feed count), not printed journal page numbers.

## 2. Sample and how it was drawn (23 records)

| Stratum | Records | n |
|---|---|---|
| Mandatory (agent spec) | 28, 42, 64, 70, 83, 98, 117 | 7 |
| All multi-criterion exclusions (from docx) | 03, 04, 21, 48, 50, 65, 68, 75, 96, 97, 120, 127 | 12 |
| Random fill from the remaining 67 single-criterion exclusions, Python `random.seed(20261108)`, `random.sample(sorted(pool), 4)` | 29, 40, 49, 85 | 4 |

Exactly **23 records were checked**; the other 63 exclusions were not re-read. For calibration I also skimmed four **included** records (#14, #25, #72, #114) for their SAR framing and how concretely they model the robot. These four are not part of the sample or the statistics.

## 3. Per-record results

Verdict key: P = PASS, F = FAIL, B = borderline. Snippets are ≤25 words, quoted or closely trimmed from the PDF.

| # | Title (short) | Logged | C1 | C2 | C3 | Agreement |
|---|---|---|---|---|---|---|
| 28 | MARL zero-shot coverage path planning, dynamic UAV networks | C1 | **F**, p1: "applications such as precision agriculture, search-and-rescue, and wildfire monitoring"; SAR only as a "versatility" demo, p19 | P (simulated UAV team) | P, p19–20 simulations | AGREE |
| 42 | Formation scaling, heterogeneous UAV–UGV teams | C1 | **F**, p1: SAR in a generic application list; p23 conclusion: purely formation motion planning, no SAR | P | P, p23: "simulation results indicate the feasibility" | AGREE |
| 64 | DEM-based traversability maps, multirobot navigation | C1 | **B**, p1 abstract: "supports the deployment of multirobot systems for search and rescue (SAR) tasks"; p2 CESAR "victim search tasks"; p7 tests on six generic Spanish terrains; p16 conclusion has no SAR | P (Husky fleet, Gazebo/ROS2) | P | BORDERLINE |
| 70 | Improved A* for rescue robots, multi-environment maps | C2 | P, p1: "increasing application of robots in post-disaster rescue operations"; sustained rescue framing | **B/P**: abstract grid-map agent with no embodiment, but C2 text does not require embodiment (see Sec. 5) | P, 50×50 grid simulations, p28 | **DISAGREE (possible wrong exclusion)**, consistency-based |
| 83 | Hybrid ACO-GA path planning, rescue robots in mine disaster | C2 | P, p1: "multi-map path planning in mine disaster rescue scenarios" | **B/P**: same as #70; p7: "Future work could explicitly model robot-specific motion constraints" | P, p1: "validated through simulations involving both single and multiple mine disaster maps" | **DISAGREE (possible wrong exclusion)**, consistency-based |
| 98 | Data-sparse inference of operator spatial reward models (RINAO) | C2 | P, p1: "uncrewed aerial systems engaged in outdoor search and rescue"; p3 overdue-backpacker wilderness search | **B**: human–UAS tasking interface; executor is p9 "mirroring the classic Pac-Man video game"; p15: "Future work will implement… with a particular aircraft" | P, p1: "validated using 10 experts in public safety" | BORDERLINE |
| 117 | Non-perception firefighting robot, CCTV vision sharing | C1 | **F**: fire-source navigation only; "rescue" appears only in historical background (p3, Rainbow 5 in 1986); no victim search | P (two physical robots, p7) | P, p7 experiments | AGREE |
| 03 | WebRTC delays, UAV-borne IoT, urban | C1/C2 | **F**, p1: smart-city monitoring framing, no SAR | **F**: UAV as an IoT carrier/communication node | P, p1 "field experiments" | AGREE (both criteria) |
| 04 | Robot usage in post-earthquake search (needs assessment) | C2/C3 | P | **F**: no robot; literature review + survey + interviews + GenAI chatbot responses, p1 | **B**: empirical survey/interview data, but no system evaluation | AGREE on decision; the C3 label is debatable |
| 21 | NEAT rover navigation, multi-room | C1/C2 | **F**, p1: "explores their potential applications in wildfire management and search and rescue"; p34 conclusion "could be valuable" | **B/P**: simulated rover agents, as concrete as included #14 | P, p1 simulations, 100–10,000 generations | AGREE on decision (C1 alone suffices); the C2 label is inconsistent with #14 |
| 48 | Mobi2Still, human-worn mmWave radar | C1/C2 | **F**, p1: one motivating sentence ("Tracking victims in smoke-filled fire zones") among crowd analytics/security uses | **F**: radar carried by a human, no robot (p1) | P, p2 experiments | AGREE (both) |
| 50 | Earthquake demolition rescue robot design, UXM–Kano–QFD | C2/C3 | P | **F**: conceptual design only, p1 "a conceptual robot design is developed" | **B/F**: Stateflow process-level simulation + SUS (p3); not a system test | AGREE |
| 65 | Bandit heuristics, moving-target detection on a linear grid | C1/C2 | **F**, p1: SAR bundled with surveillance/defence; "we do not attempt to model a full operational system in these domains" | **F**: 1-D abstract sensor-probe POMDP | P (Monte Carlo) | AGREE (both) |
| 68 | DT-enhanced KJ-Kano design, underwater rescue robots | C2/C3 | **B**: "underwater rescue" throughout; no disaster/maritime-incident scenario found in the body | **B**: a Unity/PhysX DT robot (p20) teleoperated by 55 participants in "virtual rescue missions" (p1) | **B**: C3 explicitly lists "prototype evaluation"; but outcomes are Likert ratings only, p19: "design convergence rather than engineering-level performance optimization" | BORDERLINE |
| 75 | Ground-type classification, hexapod foot force sensors | C1/C2 | **F**, p1: "field exploration, disaster rescue, and complex terrain operations" as context only | **F**, p3: "single-leg experimental platform… as a substitute for full hexapod experiments" | P | AGREE (both) |
| 96 | Mine rescue robots, human–robot information exchange | C2/C3 | P (mine rescue) | **F**: interviews with ten mine-rescue personnel, p1; no system | **F/B**: qualitative needs study | AGREE |
| 97 | Lay perceptions of soft vs rigid assistive/rescue robots | C2/C3 | B (SAR = "socially assistive robots" here) | **F**: online vignette + Cognitive-Affective Map study, p1 | **F**: perception study, no artefact | AGREE |
| 120 | Spatiotemporal information quality, UAV-assisted ground robot networks | C1/C2 | **F**: SAR invoked once to justify model assumptions, p4 | **F**, p4: UAVs "mainly serve as high-level coordinators and communication relays" | P, p9 MATLAB queueing simulation | AGREE (both) |
| 127 | LLMs/AI agents in disaster-resilient infrastructure | C1/C3 | **F**: infrastructure resilience/damage assessment, not SAR robotics | **F**: case studies are a damage classifier and a LangGraph agent (p1); no robot | **B**: largely conceptual review, but p1 reports "Two representative case studies" | AGREE on decision; the C3 label is debatable (the C2 failure is unlogged but obvious) |
| 29 | AITL-WING-HITL drone telemanipulation | C1 | **F**: SAR only in related work (p3, p10) | P | P, p1 tested with participants | AGREE |
| 40 | Lightweight attention network, geological hazard detection, rescue robotics | C2 | P, p1: "geological hazard rescue operations" | **F**, p8: "not yet been deployed on a re[al-world rescue robot]"; 2,173-image offline dataset, p9 | P (offline benchmark) | AGREE |
| 49 | ACCMPS mapping-planning for UAVs | C1 | **F**, p1: "Potential applications include post-disaster rescue missions" alongside industrial inspection | P | P, p1 "real-world experiments" | AGREE |
| 85 | Voronoi-GRU multi-robot exploration | C1 | **B**, p10: "experimental background being set in disaster rescue scenarios, such as post-fire buildings"; maps are a corridor, a shopping mall and an art museum; abstract: SAR one of three uses | P (TurtleBot3, p10) | P | BORDERLINE |

## 4. Agreement statistics (include/exclude, n = 23)

| My classification | n | Records |
|---|---|---|
| AGREE (exclude) | 17 | 03, 04, 21, 28, 29, 40, 42, 48, 49, 50, 65, 75, 96, 97, 117, 120, 127 |
| BORDERLINE | 4 | 64, 68, 85, 98 |
| DISAGREE (would include) | 2 | 70, 83 |
| **Total** | **23** | |

- **Observed agreement:**
  - Borderlines counted as exclude: 21/23 = **91.3%**.
  - Borderlines counted as include: 17/23 = **73.9%**.
- **Cohen's κ = 0.00 in both cases, and the value is degenerate.** Every logged decision in this sample is "exclude", so the logged rater has zero variance. Expected agreement p_e therefore equals my own exclude rate, and κ = (p_o − p_e)/(1 − p_e) = 0 by construction. **κ cannot measure screening reliability on an exclusions-only sample.** A meaningful κ needs a sample stratified across both included and excluded records, double-screened blind (see the `reliability-coder` agent).
- **Criterion-label disagreements where the decision still stands:** 4 records.
  - #21: the logged C2 failure is inconsistent with the inclusion of #14.
  - #04, #127: the logged C3 failure is debatable.
  - #50: the C3 call is borderline.

  These do not change the 86, but they make the per-criterion PRISMA counts (C2 = 28, C3 = 7) softer than they look.

## 5. Possible wrong exclusions, and what they would change

### 5.1 #70 and #83: inconsistent application of C2 (the main finding)
- **Logged reason:** C2 fail, because "no robotic system… or embodiment" is modelled; it is an abstract grid path-optimisation algorithm. The log cites precedent #13.
- **Literal C2:** "present a robot, platform, or **framework** that actively performs or supports SAR operations… fully autonomous." Nothing in it requires a kinematic model, a simulator such as Gazebo, or hardware. Both papers present a path-planning framework for rescue robots, set in post-disaster scenarios (#70, p1) or mine-disaster scenarios (#83, p1), and evaluate it in simulation. C3 explicitly accepts "simulation studies".
- **The inconsistency:** included record **#14** (manuscript ref [35], Xue/Tan/Wong, *Sci. Rep.* 15:44724) is at the same level of abstraction. In its own words, p4: "This research uses Matlab and its RL toolbox… The robotic exploration scenario is emulated" on a grid map, and the robot is a grid agent. A text search of #14 found no Gazebo, ROS or kinematic model. If #14 passes C2, then #70 and #83 pass C2 on the same evidence. **Either #70 and #83 were wrongly excluded, or #14 (and possibly other abstract-simulation inclusions; #114 runs "numerical simulations" of task allocation) was wrongly included.** The criterion as written favours inclusion.
- **Contrast with #13**, the cited precedent: #13 is reasonably distinguished. Its robots perform supply delivery (the "logistics tool" exclusion), tested on the Solomon VRP benchmark. #70 and #83 are search/navigation tasks, not logistics.
- **Effect if both were included:**
  - Corpus: 39 → 41.
  - Likely mode: **Fully Autonomous**, since there is no human in the loop. FA would go from 27 → 29, i.e. 29/41 = 70.7% (from 69.2%).
  - FA field-testing: 2/29 = **6.9%** (from 7.4%). Both papers are simulation-only.
  - Platform: generic/unspecified ground robot; the UAV and Hybrid counts are unchanged.
  - Headline direction: **unchanged, and slightly strengthened** (the FA validation gap widens).
  - Environmental-realism limitation: both would likely count, giving 37/41.
  - All of this is a projection only; it would require re-extraction.

### 5.2 Borderline records (author adjudication needed; no change recommended by me alone)
- **#98 (RINAO):**
  - The case for inclusion: SAR is the sole and sustained framing, it is a genuine human–UAS teaming framework, and it was validated with 10 domain experts.
  - The case against: no aircraft is operated. The executor is a grid MDP (p9), and real-aircraft integration is deferred to future work (p15).
  - If C2 is read as "framework that supports SAR operations", it passes. The same embodiment argument as #70/#83 applies.
  - If included, the likely mode is **Supervisory** (operator sketches spatial preferences; autonomy plans and executes) and the platform is UAV. Effects:
    - Supervisory: 4 → 5.
    - UAV field-tested: 1/14 = 7.1% (from 1/13 = 7.7%).
    - Supervisory field-testing would fall, because the 60–75% Teleop/Supervisory figure would gain a non-field-tested member. The authors should recompute.
- **#68:**
  - C3 literally accepts "prototype evaluation", and a simulated DT robot was operated by 55 users in rescue tasks.
  - However, C1 is weak: underwater rescue equipment, with no disaster scenario found in the body. Only subjective ratings were reported.
  - On balance it leans toward exclusion, but the logged rationale ("no objective task-performance metric") adds a requirement that is not in C3 as written. If the review applies that rule, it should be stated in the Methods.
- **#64 and #85:** both have SAR in the abstract or experimental framing but test on generic terrain or buildings, with SAR-silent conclusions. The logged rationale (cosmetic/unrealised SAR framing) is reasonable, but it is a judgement call. C1's "primary framing" test is not operationalised in the Methods. If included, both would be **Fully Autonomous**, simulation-only multi-robot ground systems, which would again strengthen the FA validation gap.

## 6. Recommendations (for the authors; nothing applied)
1. **Resolve the #14 vs #70/#83 inconsistency** by writing an explicit C2 decision rule. Either (a) abstract grid agents count as a robotic framework (then include #70 and #83, and re-check #21, #65 and #98), or (b) embodiment of some kind is required (then re-check #14, #114 and other included grid or numerical-simulation papers). Log the rule and any changes in master doc Sec. 16, per CLAUDE.md rule 3.
2. **Add the operational rules actually used** to Sec. II-E, so a reader can reproduce the borderline calls:
   - the C1 "primary framing" test (SAR must recur in the methods, experiments and conclusion);
   - the C2 embodiment rule;
   - the C3 "objective performance metric" rule.
3. **Methods integrity (CLAUDE.md rule 4):** this check does not support the manuscript's claim of three independent screeners (Sec. II-F). The audit trail (Sec. 2.2 internal note, Sec. 16) records single-annotator screening at one point. Only the authors can confirm what happened. Any reliability statistic in the manuscript must come from a genuine, blind, two-human double-screen of a stratified sample. This AI check should be disclosed as AI-assisted verification, if it is mentioned at all.
4. Reconcile the debatable C3 labels (#04, #127, #50) before reporting per-criterion counts. #127 also fails C2, which the log does not record.

## 7. Files
- `supplementary/screening_log.csv`: the 125-row parsed screening log (parse only).
- Scratch extraction (not project files): the docx text and per-record PDF text, in the session scratchpad.
