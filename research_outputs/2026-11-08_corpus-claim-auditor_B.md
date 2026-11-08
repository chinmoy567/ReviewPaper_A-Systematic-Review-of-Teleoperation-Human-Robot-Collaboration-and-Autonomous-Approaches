# Corpus-claim audit, share B: references [23] to [35]

- **Agent:** corpus-claim-auditor (instance B)
- **Date:** 2026-11-08
- **Scope:** 13 included papers, [23] to [35] (record IDs 15, 25, 30, 43, 47, 52, 56, 59, 72, 87, 114, 8, 14), using `data/id_map.csv`.
- **Coverage: all 13 papers fully audited.** Each full-text PDF in `assets/papers/` was extracted page by page (`pdftotext -layout`). Every manuscript claim citing these refs was checked against the source.
- **Manuscript source:** `SAR_review_master_document.md`, Secs. 9 to 14 (lines 300 to 745), plus Sec. 6A to 6F and the Sec. 15 bibliography. The manuscript was not edited.
- **Page numbers** are PDF page indices. For these journals they match the printed page numbers.

**Where these refs are cited in the manuscript.** I scanned lines 300 to 745 for `[23]` to `[35]` with a script, including ranges. Refs [23] to [35] appear only at lines 593 and 595 (Sec. IV-D clusters), 623 and 633 (Sec. V-A and V-B, [25] only) and 652 to 654 (Sec. V-D future work, [25] only). They do not appear in the Introduction, Methods, Results prose, Abstract or Conclusion. Sec. 6B lists the platform for each record ID. Table VII/XI cell membership per paper is not recorded anywhere in the `.md`, because the Extraction `.xlsx` is not in the project. So I could check the validation and scenario labels below only against the aggregate tables, not per cell.

**Process note (no effect on results).** Another agent wrote into the shared scratchpad `txt/` folder at the same time, which overwrote my extract of [28] with record Q1 28 (Carvalho & Aguiar, an excluded record). I caught this, re-extracted all 13 PDFs into a private folder, and checked that each first page matched its bibliography entry. [23] to [27] were byte-identical to the first extraction. Every result below comes from the verified extracts.

---

## 1. Evidence table, per paper

### [25] Mead et al. 2026, EAAI (record 30). The Discussion's flagship paper.

| Field / claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Scalability (L593) | "success rates degrade sharply as swarm size grows **beyond that one validated unit**" | The scaling test was **pure simulation** of the stage-two policy at 4/8/12/24 agents (Table 6, p9). The physical test used one UGV only (p11). No result relates degradation to the physical unit. | **WRONG** |
| LiDAR failure (L593) | "false positives **from grass and wind**" caused 3/10 collisions | Long grass close to the vehicle produced **false positives**. Slight obstacle movement caused by wind produced **false negatives** (p11). | **WRONG** (wind caused false negatives, not false positives) |
| Sim-to-real (L593) | The only one of 12 cluster papers with a successful sim-to-real transfer, single physical unit | Policy transferred to one physical "1050" UGV. The other three agents were simulated in a hybrid physical-cyber setup (p11, p12). The other papers in my share ([23], [24], [26] to [33]) report no sim-to-real transfer (see below). | OK |
| Replaces teleoperation (L593) | Platform normally operated by teleoperation | The 1050 platforms are proven operationally for firefighting "through teleoperation" (p11) | OK |
| Sim numbers (L623) | 95.83% (4), 84.50% (8), 81.11% (12), 69.36% (24); a 26.5-point drop | Table 6 (p9). The layout extraction misaligns rows, but the 95% CIs pin each value: 79.6 to 89.4 gives 84.50 at 8 agents; 76.12 to 86.10 gives 81.11 at 12; 65.24 to 73.48 gives 69.36 at 24. 95.83 − 69.36 = 26.47. | OK |
| Failure attribution (L623) | Most failures were agent-agent collisions rather than obstacle collisions | p8 to p9: stage-two failures were most often agent-agent collisions | OK |
| Physical trials (L623) | 1 physical robot, 3 simulated teammates, 10 hybrid trials, all 10 doused their fires, 3/10 had physical collisions | Table 9 (p11): all fires doused 10/10; no physical collisions 7/10; no simulation collisions 10/10. Text on p11 agrees. | OK |
| Cause of collisions (L623) | "misreading long grass as obstacles and **wind-shaken foliage** as false negatives" | False negatives came from "slight movements in the obstacles from the wind" (p11). The obstacles were two cardboard boxes and one dirt/grass mound (p11). "Foliage" is not stated. | **INCOMPLETE CONTEXT** (wording) |
| Stage 2 to stage 3 (L623) | 77.92% when the stage-two policy is applied directly to stage three, vs. 99.67% after stage-three training | Table 8 and text (p10), 2-fire scenario | OK |
| Task generalisation (L652) | "a capability proven at one curriculum stage **did not transfer** to the next without dedicated retraining" | The stage-two policy reached 77.92% on stage three, which is a partial transfer. Stage-three training is the curriculum's design, bootstrapped from stage-two weights (p9 to p10), and the authors present the gain as validating the curriculum (p10). | **OVERSTATED** |
| Scalability across the cluster (L654) | A "consistent degradation pattern … documented in both Section IV-D's multi-robot cluster synthesis and [25]" | Sec. IV-D (L593) documents degradation only for [25]. In my share, [23] also shows lower success at larger team sizes (abstract p1, Table p7). [28] says more UAVs make coordination harder (p18). Neither is cited for this point. | **INCOMPLETE CONTEXT** (the cross-reference points to text that does not contain the claim) |
| Hazard-specific scenario (L633, L653) | The grass/wind failure happened in a hazard-specific firefighting scenario | The task is collaborative firefighting. In the hybrid test the fires were simulated and the physical setting was a grassy outdoor area with 3 obstacles (p11). | OK. Consider adding that the fires were simulated. |

### [23] Tan & Zhao 2026, Complex & Intelligent Systems (record 15)

| Claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Cluster membership (L593) | Multi-robot coordination, via multi-agent RL | LADDPG: MADDPG with random-feature linear attention plus smoothed and adaptive prioritised replay, under CTDE (p1, p4, p5) | OK |
| Cluster framing (L593) | "little or no centralized control" | CTDE: centralised critic during training, decentralised execution (p4) | OK |
| Sim-to-real (L593, implicit) | Not a sim-to-real case | 2-D 100×100 abstract grid simulation only, RTX 3090 (p5). Success rates up to 90.6% and 85.2% at medium and large scale (p1). | OK |

### [24] Xue, Tan & Wong 2026, Results in Engineering (record 25)

| Claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Mechanism (L593) | "via multi-agent reinforcement learning" | CERES-Q coordinates the team with heuristic modules: phase-aware frontier clustering/allocation and dynamic task transfer. RL is used only for each robot's safe-return switch, through Safety Double Q-learning (abstract p1, p11). It is not a MARL coordination policy. | **INCOMPLETE CONTEXT** |
| Team size | (not stated) | Two robots only, a deliberate choice; scaling is left to future work (p11) | Note |
| Validation | (not stated) | MATLAB RL-toolbox grid simulation (p11). The authors state the grid abstraction, static obstacles and ideal communication as limitations (p19). | Simulation only |

### [26] Raza ur Rehman et al. 2026, Scientific Reports (record 43)

| Claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Mechanism (L593) | "decentralized reward-shaping without explicit inter-agent communication" | Independent Q-learning guided by GWO. Coordination emerges implicitly from reward shaping and duplicate-exploration penalties "without introducing communication overhead" (p5, p8, p11). However, agents coordinate through **shared environment updates in a centralized simulation framework** (p10). | OK, with a caveat: the shared map is an implicit channel |
| Not in the MARL list (L593) | Listed separately from the MARL group | The paper describes itself as MARL (IQL) (abstract p1) | Minor. Could also be listed under MARL. |

### [27] Kareem et al. 2026, Scientific Reports (record 47). **Listed but never described (confirmed).**

| Claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Cluster list (L593) | In the 12-paper list, but missing from the mechanism enumeration | Confirmed: [27] appears only in the parenthetical list | **INCOMPLETE** |
| Suggested description (paraphrased) | — | A PX4/Gazebo simulation of a small UAV swarm (Fig. 4 shows three drones, p8). Each drone picks its next grid waypoint with one of ten bio-inspired metaheuristics, using a shared thermal-confidence map (pp. 1, 4, 9). PSO scored highest on the authors' new composite Exploration Score (0.67 vs. GWO 0.62 and ACO 0.59) and covered 80% of the area in 60% of mission time (pp. 1, 12). The authors note there is no inter-drone collision avoidance (p9) and that validation is limited to a controlled virtual environment (p14). | — |

### [28] Gao et al. 2026, Discover Computing (record 52)

| Claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Mechanism (L593) | "via multi-agent reinforcement learning" | A parameter-shared DDQN under CTDE. The authors themselves say DDQN is a single-agent algorithm and list this as a limitation compared with dedicated MARL frameworks such as MADDPG or value decomposition (pp. 13 to 15). | **INCOMPLETE CONTEXT** (minor). Accurate wording: "parameter-shared deep RL (DDQN, CTDE)". |
| Setting | — | City32/City50 urban post-disaster grids, 2 to 4 UAVs (p16), Python/TensorFlow (p15). Evaluated in simulation only. Sensor noise, comms latency and static obstacles are discussed as deployment issues (pp. 19 to 20). | Simulation only |

### [29] Bedi, Zhang & Chabot 2025, Information (record 56)

| Claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Mechanism (L593) | "TAEMS-based task scheduling" | TAEMS scheduling for Police Force agents plus a voice-channel communication protocol in RoboCup Rescue Simulation (pp. 1 to 2, 12). Gains of 12% to 48% over default agents (pp. 1, 12). | OK |
| Decentralised | "little or no centralized control" | The authors describe it as decentralised coordination (p12) | OK |
| Validation | — | 2-D RCRS simulation of a post-earthquake city (p3). Moving to physical robots is listed as future work: mapping, communication robustness, fault tolerance (p12). | Simulation only |

### [30] Tao et al. 2025, Sensors (record 59)

| Claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Mechanism (L593) | "air-ground complementary mapping" | UAV plus UGV point-cloud map fusion with FAST-LIO2, improved SAC-IA and VGICP, then DDPG path planning (abstract p1) | OK |
| Cluster fit (L593) | Listed under "coordination and task allocation" | The contribution is map fusion plus single-robot DDPG navigation. Multi-agent RL task allocation between the air and ground robots is named only as **future work** (p24). | **INCOMPLETE CONTEXT** (weak fit to the cluster) |
| Validation | — | Gazebo only. The authors state that the experiment is simulation-based and that real-world rubble and landslide testing, sensor noise, extreme lighting and dynamic obstacles are future work (pp. 1, 24). | Simulation only |

### [31] Wang & Benhabib 2025, Robotics (record 72)

| Claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Mechanism (L593) | "dynamic mid-mission task reallocation for multiple concurrent missing-person searches" | Dynamic task allocation by evolving probability of success, with overlap removal (abstract p1, p5) | OK |
| Cluster framing (L593) | "with **little or no centralized control**" | The paper explicitly states "centralized control of a multi-UAV team". All UAVs stay in contact with a central controller (pp. 1, 4). | **OVERSTATED** as applied to this paper |
| Validation | — | Simulation only (abstract p1, conclusions p20). Idealised assumptions include constant speed, no effect of urban obstacles, binary detection, unlimited power and reliable links (p4). Mean detection time is 23% lower on average (p19). | Simulation only |

### [32] Romero et al. 2026, Computer Communications (record 87)

| Claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Mechanism (L593) | "GNSS/cellular-constrained fleet mission planning" | A MILP mission planner that sets minimum fleet size and paths using terrain elevation from GNSS/DEM data and communication-dependent energy profiles (abstract p1, p5) | OK |
| Cluster framing (L593) | "little or no centralized control" | Planning runs on a **centralized task planner on an edge/cloud server** (pp. 1, 3) | **OVERSTATED** as applied to this paper |
| Validation | — | Real Unitree GO1 power profiling on slopes (pp. 6 to 7). Mission planning was evaluated in analytical and Gazebo simulations (pp. 7 to 8). Weather, communication degradation and dynamic obstacles are future work (p11). | Partial (real energy measurements only; the planner was not field-run) |

### [33] Li et al. 2026, IEEE TNSE (record 114)

| Claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Mechanism (L593) | "bid-prediction-based distributed task allocation" | PDTA: a performance-impact framework with task-bid prediction during task removal, then local-search refinement (abstract p1, p5 to p7) | OK |
| Validation | — | Monte Carlo simulations on an Intel i7 PC. 4 to 6 robots, 16 to 36 tasks. Mean gap to the Gurobi optimum is 5.23% (p10). The authors list a static task set and static environment as a limitation (p9). | Simulation only |
| Sec. 6B note (working record) | "no distinct types actually differentiated" | Two rescue-team types (medicine vs. food) with a robot-task compatibility matrix (p4, p10). These are functional types, not platform classes. | The Abstract/Unspecified label stands, but the Sec. 6B wording is slightly inaccurate |

### [34] Rado, Baglioni & Jamshidnejad 2025, Scientific Reports (record 8)

| Claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Mechanism (L595) | "dynamic-obstacle-anticipating MPC" | A heuristic planner with predicted "obstacle belts" for anticipatory avoidance, plus tube-based robust MPC tracking (pp. 1 to 2, 4 to 6). Up to 42.3% better than RRT and APF (p1). | OK |
| Validation (L595) | Simulation-only, with real-world testing named as future work | MATLAB R2020b, 14 m × 14 m simulated environment (p9). Real-life experiments are named as future work (p15). | OK |

### [35] Xue, Tan & Wong 2025, Scientific Reports (record 14)

| Claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Mechanism (L595) | "energy-aware Q-learning coverage planning" | PERM-QN: Q-learning with dynamic-weight reward, prioritised replay and a memory network, energy-aware (abstract p1) | OK |
| Validation (L595) | Among the five of seven that are simulation/MATLAB-only "with real-world testing explicitly named as future work" | MATLAB grid simulation (p4). The conclusion lists only offline training time and multi-robot exploration as future work (p16). **Real-world testing is not named as future work.** | **INCOMPLETE CONTEXT.** The "named as future work" part does not hold for [35]. |

---

## 2. Label summary per paper

Platform = Sec. 6B bucket. Mode = Sec. 6A. "Human" = whether a human role is modelled in the tested setup. Env-lim = whether the paper itself reports an environmental-realism limitation.

| Ref (ID) | Platform (6B) → PDF | Mode | Validation (my reading) | Scenario (6E) | Sensors (6F flags) | Compute (6D) | Human | Env-lim |
|---|---|---|---|---|---|---|---|---|
| [23] (15) | UAV ✓ | FA ✓ | Simulation only | Generic | None | PC/Offline | N | Weak Y: future work on 3-D environments (p10); 2-D abstraction |
| [24] (25) | UGV. **Weakly typed:** generic grid "robots"; ground surface appears only in the turning-cost model (p11) | FA ✓ | Simulation only | Generic | None | PC/Offline | N | Y (p19) |
| [25] (30) | UGV ✓ | FA ✓ | Partial (sim + 1 physical UGV, hybrid) | Wildfire/Fire (firefighting) | LiDAR, GPS, IMU (wheel encoders); vision pipeline is assumed only in sim (p7) | Onboard/Edge (policy on external compute unit, p11) ✓ | N | Y (p11) |
| [26] (43) | Abstract. **Disputable:** title, abstract and keywords all frame UAVs; methods say "UAV/robot agents" (pp. 1, 5) | FA ✓ | Simulation only | Underground/Tunnel | None ("onboard sensors" not specified) | PC/Offline | N | Y (p11: centralised sim; comms delay and sensor noise future work) |
| [27] (47) | UAV ✓ | FA ✓ | Simulation only (PX4/Gazebo) | Generic | Thermal, GPS (simulated) | PC/Offline (MAVSDK-Python SITL) | N | Y (p14) |
| [28] (52) | UAV ✓ | FA ✓ | Simulation only | Generic (urban post-disaster) | None | PC/Offline | N | Y (pp. 19 to 20) |
| [29] (56) | Abstract ✓ | FA ✓ | Simulation only (RCRS) | RCRS post-earthquake city (p3). Earthquake or Generic depending on the rule; label not checkable | None | PC/Offline | N | Y (p12: physical transition challenges) |
| [30] (59) | Hybrid ✓ (UAV + UGV) | FA ✓ | Simulation only (Gazebo) | Generic | LiDAR, IMU | PC/Offline | N | Y (p24) |
| [31] (72) | UAV ✓ | FA ✓ (centralised controller) | Simulation only | Generic (urban missing persons) | None (binary sensing model) | PC/Offline | N | **N.** Idealised assumptions are stated (p4) but not framed as a limitation; the conclusion's future work does not mention realism (p20) |
| [32] (87) | Hybrid ✓ (wheeled vs. quadruped compared) | FA ✓ | Partial (real GO1 energy profiling + sim) | Generic outdoor terrain | GPS (GNSS/DEM), RF (cellular) | Hybrid/Cloud-edge planner at runtime (p3). Label not checkable | N | Y (p11) |
| [33] (114) | Abstract ✓ | FA ✓ | Simulation only | Generic | None | PC/Offline | N | Borderline Y (p9: static task set and environment) |
| [34] (8) | UGV ✓ (differential-drive ground robot, p3) | FA ✓ | Simulation only | Generic (urban collapse framing) | Visual (abstract camera perception field, p3) | PC/Offline | N | Y (p15) |
| [35] (14) | UGV. **Weakly typed:** generic "robot", no ground typing found | FA ✓ | Simulation only | Generic | None | PC/Offline | N | **N.** Only training time is stated as a limitation (p16) |

**Disagreements to resolve against the Extraction sheet (not available locally):**
1. **Environmental-realism count (35/39).** I found no self-reported environmental-realism limitation in [31] or [35], and [23] and [33] are borderline. This share holds 13 of the 39 papers, and the corpus total allows only 4 papers without a limitation. If both [31] and [35] were coded "yes", the 89.7% headline (a locked fact) would need re-checking. Ask the stats-consistency-checker to confirm the per-paper flags for IDs 72 and 14.
2. **[26] (ID 43) platform.** The paper's own framing is UAV, so Abstract/Unspecified can be challenged. Moving it to UAV would change Table VI/VII (UAV 14, Abstract 2) and the UAV validation ratios. My recommendation is to keep the current label (the agents are maze grid cells with no flight model) but **state the reason in the Methods/Sec. 6B note**, because a reviewer reading the abstract will see "UAVs".
3. **[24] and [35] (IDs 25, 14), typed UGV.** The PDFs never type their robot as a ground vehicle. Sec. 6B's basis ("explicitly typed 'ground robot'") does not hold literally. Abstract/Unspecified is at least as defensible. Changing them would shift Table VI (UGV 11, Abstract 5).
4. **[32] (ID 87) validation.** The real-hardware part is energy profiling on a bench and on slopes, not a mission. If it is coded "Partial", that is defensible but generous. Check it against Table XI.

---

## 3. WRONG / OVERSTATED items, with suggested Markdown wording (paraphrased)

**L593, [25] scalability. WRONG.** Replace "the paper's own results note success rates degrade sharply as swarm size grows beyond that one validated unit" with:
> its own simulation results show success falling from 95.83% with four agents to 69.36% with 24, while the physical test was limited to a single UGV

**L593, [25] LiDAR. WRONG.** Replace "its real-world LiDAR pipeline produced enough false positives from grass and wind to cause 3 of 10 physical collisions" with:
> in its physical trials the LiDAR pipeline read long grass as obstacles (false positives) and missed slightly wind-moved obstacles (false negatives), and these errors accounted for the 3 of 10 trials with physical collisions

**L623, [25]. INCOMPLETE CONTEXT.** Replace "and wind-shaken foliage as false negatives" with:
> and missed obstacles that the wind had shifted slightly (false negatives)

Optionally add that the physical course had only three obstacles: two cardboard boxes and one grass/dirt mound (p11).

**L593, cluster framing. OVERSTATED.** "with little or no centralized control" does not hold for [31] (central controller, pp. 1, 4) or [32] (centralized edge/cloud task planner, pp. 1, 3). Suggested wording:
> …divide search area, avoid redundant coverage, or allocate rescue tasks, through both decentralized schemes and centralized planners

**L593, [27] missing. INCOMPLETE.** Add to the enumeration:
> bio-inspired metaheuristic waypoint selection over a shared thermal-confidence map, benchmarked across ten algorithms in PX4/Gazebo ([27])

**L593, MARL list. INCOMPLETE CONTEXT** ([24], [28]). Suggested wording:
> via reinforcement learning, either multi-agent ([23], [25]), parameter-shared ([28]) or used for per-robot energy-safe return decisions alongside heuristic frontier allocation ([24])

**L593, [30] fit. INCOMPLETE CONTEXT.** Either keep it and phrase it as "air-ground map fusion feeding single-robot DDPG navigation ([30])", or note that its multi-robot coordination is limited to map fusion (task allocation is future work, p24).

**L595, [35]. INCOMPLETE CONTEXT.** Change "with real-world testing explicitly named as future work" to:
> most of them naming real-world testing as future work

(this holds for [34], p15, but not for [35], p16). The other papers in the clause, [36] to [40], are outside this share.

**L652, [25]. OVERSTATED.** Replace "a capability proven at one curriculum stage did not transfer to the next without dedicated retraining" with:
> a policy from one curriculum stage transferred only partly to the next (77.92% vs. 99.67% after stage-specific training)

**L654, cross-reference. INCOMPLETE CONTEXT.** Sec. IV-D documents swarm-size degradation only for [25]. Either cite [23]'s lower success at larger team sizes (p1) and [28]'s note that coordination gets harder with more UAVs (p18), or drop "Section IV-D's multi-robot cluster synthesis" from the sentence.

---

## 4. Re-confirmation of known issues
- **[25] degradation:** confirmed. It was in simulation, 4 to 24 agents (Table 6, p9), not beyond the physical unit. Wind caused false negatives and long grass caused false positives (p11).
- **[27]:** confirmed as listed in the multi-robot cluster (L593) but never described. A description is given in §1 and §3.

## 5. Unaudited papers
None. All 13 papers in share B ([23] to [35]) were fully audited.
