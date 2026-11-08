# Corpus-claim audit, share C: references [36]–[48]

**Agent:** corpus-claim-auditor (instance C) · **Date:** 2026-11-08
**Scope:** 13 included papers, [36]–[48] (record IDs 20, 46, 51, 55, 82, 11, 17, 66, 100, 124, 22, 53, 54), per `data/id_map.csv`.
**Coverage:** **13/13 papers fully audited** against the full-text PDFs in `assets/papers/`. All 13 PDFs open and match their catalogued titles. (Manifest note: the Drive manifest also lists a different paper, "Q1 40 A lightweight and cross-scale attention network…", and its record number 40 shares its digits with ref [40]. That file is not part of this share. The id_map path for [40] points to the correct Symmetry 2025 paper.)
**Manuscript source:** `SAR_review_master_document.md` only. The claims about these refs appear at lines 595, 597, 599, 601, 611, 625 and 651, plus Sec. 6A Precedents B and E, Sec. 6B, Tables VII/XI and Sec. 16.
**Page convention:** "p" = PDF page index from `pdftotext`. This equals the printed article page for every paper except [38] (Sensors), where PDF p.N is journal page N−7 from p.20 onward. Example: PDF p.40 = journal p.33. Both are given for [38].
**Limits:** the per-paper extraction table (`SAR_review_data_extraction_table.xlsx`, columns S–AH) is not in the project. So per-paper Validation, Scenario, Architecture and Sensor flags cannot be compared cell by cell. Where a manuscript aggregate depends on them, the dependency is flagged and not asserted.

---

## 0. Headline findings

1. **The "five of the seven are simulation-only" claim is not supported (line 595).** Of the five single-robot-navigation papers in this share, only **2 are simulation-only**: [37] (Gazebo + MATLAB) and [40] (MATLAB 2D grid). [38] is Partial: simulation and benchmark data, plus pilot indoor corridor and mock-rubble logs from a lab-built ground robot. [36] and [39] are **real-world hardware tests with no simulation component**: [36] made an autonomous flight in an underground parkade, and [39] ran 30 outdoor trials on emulated volcanic terrain. Even if both [34] and [35] (share B) are simulation-only, the cluster is at most **4/7**, not 5/7. The add-on "with real-world testing explicitly named as future work" also fails for [37], which names only "more application scenarios".
2. **Line 601 contradicts line 595.** Line 595 says real-world validation in the single-robot cluster is "markedly thinner … than the corpus average". Line 601 calls the same cluster "the cluster with the most real-world testing". Both cannot be true. On the share-C evidence ([36] and [39] real-world, [38] partial), the cluster is not thin. Both sentences need rewriting once [34]/[35] are confirmed.
3. **[42] (known issue, re-confirmed in part).** Offline, post-hoc scoring is **confirmed**. The real-world NBV views were chosen by brute force from a pre-recorded set of 1,032 images, scored in post-processing, and no closed loop was flown (p9, p11). However, **"human-piloted" is NOT stated in the PDF.** The paper says only that a DJI Mavic 3 Pro "was used to acquire" the images (p9). Sec. 6A Precedent B's "human-piloted data-collection flight" is therefore an inference, not a source fact. The manuscript's "fully canopy-occluded targets in real forest trials" is also overstated (see the table).
4. **[47] (known issue, re-confirmed).** The source says the 40% success rate "remains modest for safety-critical applications" (p6). Line 599's "describe as inadequate for safety-critical deployment" is **OVERSTATED**. Line 625 quotes it correctly. A second, related overstatement: line 625 says [47] "explicitly state[s]… that their tested system is not ready for real deployment". The paper never says that.
5. **[43] is misdescribed.** Line 597 calls Robobuoy "a low-cost drowning-detection buoy". It is a **shore-based monitoring station plus a radio-controlled surface vessel (FT009 RC boat)**. The buoys were the *targets*: stationary buoys stood in for victims, and no humans took part in the hardware trials (p3–p5, p14).
6. **[48]'s Fully Autonomous label is contestable.** The paper explicitly "combines manual and autonomous operational modes" (p1). An operator can take over through an Electron GUI (p9–p11), and the reported tests do not separate which mode produced the results. This affects Table VII's Legged/FA cell (2), which needs both [46] and [48] to be FA. Flagged for the authors; not re-labelled (CLAUDE.md rule 3).
7. **A risk to the 35/39 environmental-realism figure.** For **4 papers in this share alone**, no self-reported environmental-realism limitation was found: [37], [44], [47], [48]. [42] and [45] are borderline: [42] only notes that its real-world experiment was "less comprehensive", and [45] only assumes "fair weather". The corpus claim allows only 4 papers without one *in the whole corpus*. Unless share A/B have zero such papers, and the extraction coded the borderline cases as Y, 35/39 (89.7%) may be overstated. **Status: UNVERIFIED pending the extraction column and shares A/B.**

---

## 1. Per-paper evidence tables

Status codes: OK · WRONG · OVERSTATED · INCOMPLETE CONTEXT · NOT FOUND

### [36] Allan & Barczyk 2025, *Drones*, record 20

| field / claim (line) | manuscript says | PDF says (page) | status |
|---|---|---|---|
| Description (595) | "a low-cost SubT-Challenge-style exploration quadcopter" | Custom low-cost quadcopter (ZED 2 stereo, Jetson Xavier NX) running the FUEL frontier explorer. The SubT Challenge is cited as motivation (p1–p3). | OK |
| Cluster validation (595) | counted within "five of the seven… simulation-only or MATLAB-only" | "successfully validated through a hardware autonomous flight experiment performed in an underground environment" (p1). Single flight in an underground car parkade, 3 min 39 s, 93 m path (p12, p14). No simulation study. | **WRONG** (if counted as sim-only). It is a real hardware test, though only one proof-of-concept flight. |
| Future work | "real-world testing explicitly named as future work" | Further tests in simulated SAR scenarios and with ground truth are left to future work (p12). More trials are needed for statistical significance (p15). | OK as a caveat, but the paper *already has* a real-world test |
| Platform (6B) | UAV | quadcopter (p1, p5) | OK |
| Mode (cluster: FA) | Fully Autonomous | "Fully autonomous drone flight… demonstrated… in a single proof-of-concept flight" (p15) | OK |

### [37] Chen et al. 2026, *IEEE Sensors J.*, record 46

| field / claim (line) | manuscript says | PDF says (page) | status |
|---|---|---|---|
| Description (595) | "improved-AMCL localization for Ackermann-steered ground vehicles" | UKF-fused odometry/IMU improving AMCL (±0.036 m) **plus** the DAC-A* planner (about 40% less time to reach the destination) (p1, p8) | INCOMPLETE CONTEXT (the planning half is omitted) |
| Validation (595) | sim-only / MATLAB-only | Localization tested in Gazebo corridor and hospital worlds (p6–p7). Planning simulated in MATLAB R2022b (p7–p8). "validated through multiple simulation experiments" (p8). | OK (simulation only) |
| Future work (595) | real-world testing named as future work | The abstract says only "further algorithm optimization and exploration of more application scenarios" (p1). Real-world testing is not named. | **NOT FOUND** |
| Platform (6B) | UGV | Ackermann mobile robot, 23 × 19 cm (p5) | OK |

### [38] Almalkawi et al. 2026, *Sensors*, record 51

| field / claim (line) | manuscript says | PDF says (page) | status |
|---|---|---|---|
| Description (595) | "GPS-denied thermal-visual-inertial SLAM on commodity embedded hardware" | TV-VO + ZUPT odometry, occupancy mapping and loop-closure return-to-base, RescueGraph detection, PPO planner (p1). All modules ran on a quad-core ARM SBC with 4 GB RAM (PDF p16 / jnl p16). The authors state they do not claim a new SLAM algorithm (p2). | OK (the "SLAM" shorthand is acceptable) |
| Validation (595) | in the 5/7 sim-only group? | Synthetic/bench data plus "Pilot-Run Datasets… indoor corridor and mock-rubble logs", described as "proof-of-concept validation" (p16). Lab-built prototype shown in Fig. 24 (PDF p41). | **WRONG** if counted as simulation-only; it is **Partial** |
| Future work | real-world named | "controlled real-robot validation in physically cluttered SAR-like environments" is the next step (PDF p40 / jnl p33) | OK |
| Platform (6B) | UGV | differential-drive ground robot (p13, p15) | OK |

### [39] Yeoh, Sumaryo & Susanto 2026, *IJRCS*, record 55

| field / claim (line) | manuscript says | PDF says (page) | status |
|---|---|---|---|
| Description (595) | "volcanic-terrain heading estimation" | Hybrid GPS–INS with tilt-compensated magnetometer heading and PID heading control on an Arduino Mega (p1) | OK |
| Validation (595) | in the 5/7 sim-only group? | "Field experiments were conducted in simulated volcanic terrain" with rocky surfaces, slopes up to 30° and ash-like gravel. 30 physical trials of 20–100 m, outdoors (p1, p5, p7). | **WRONG** if counted as simulation-only. It is a physical outdoor test on an emulated terrain. |
| Scenario (6E) | Other (volcanic) | volcanic SAR framing (p1) | OK |
| Note | — | Despite the title, no victim detection is implemented or tested (p1–p9). Return runs need a manual "heading lock" reset (p7–p8). | — |

### [40] Kozhubaev et al. 2025, *Symmetry*, record 82

| field / claim (line) | manuscript says | PDF says (page) | status |
|---|---|---|---|
| Description (595) | "dynamic symmetrical path planning for coal-mine environments" | Enhanced A* + DWA + RRT with path symmetry as a criterion, for coal-mine robots (p1–p2) | OK |
| Validation (595) | sim/MATLAB-only | "simulation experiments conducted within the MATLAB environment" (p1). A 2D grid; 3D simulation is planned (p10). | OK |
| Future work (595) | real-world named | Lab test results will be used to plan "a field test in a real coal mine environment" (p15) | OK |
| Platform (6B) | UGV | abstract mobile robot/"car" on a grid; sensor models are assumed only (p10) | OK (borderline; no physical platform) |

### [41] Kareem et al. 2026, *JESTECH*, record 11

| field / claim (line) | manuscript says | PDF says (page) | status |
|---|---|---|---|
| Description (597) | "dual-altitude thermal-then-visual UAV victim confirmation" | High-altitude thermal coarse scan, then low-altitude YOLO visual confirmation, with PSO swarm planning (p1, p6) | OK |
| Validation | (FA cluster; not stated) | "The current evaluations are limited to simulation" (p25). Gazebo + PX4 SITL replica of Sunnyvale Baylands Park (p13, p19, p23). The hardware architecture is described (p21) but not flown. | Simulation only (consistent) |
| Note | — | The lead author is the same as for the closest prior review, Kareem et al. 2026 (IEEE Access), already logged in Sec. 16. An operator initializes the mission and monitors through QGroundControl (p6, p20); no human decision step was tested. | — |

### [42] Strand et al. 2026, *IEEE JSTARS*, record 17

| field / claim (line) | manuscript says | PDF says (page) | status |
|---|---|---|---|
| Number (597) | "recovered 5 of 7 … targets" | "the NBV selection process successfully captured five of the seven targets that were occluded from top-down imagery" (p10) | OK |
| Target description (597) | "fully canopy-occluded targets" | Seven tripod markers in hi-vis vests, "partially concealed within bushes or behind tree trunks", placed so that none was visible from any top-down viewpoint (p9) | **OVERSTATED** ("hidden from all top-down views", not "fully canopy-occluded") |
| Test framing (597) | "in real forest trials" | One real-world dataset: 1,032 images from a DJI Mavic 3 Pro, each manually annotated. The EA was not run; fitness was computed by brute force over the pre-recorded images "in postprocessing" (p9). "real-world experiments… relied on offline evaluation" (p11). The real experiment is "less comprehensive but act[s] as a proof of concept" (p7). | **INCOMPLETE CONTEXT.** One offline-scored dataset, not closed-loop trials. |
| Sec. 6A Precedent B | "human-piloted data-collection flight" | The PDF says only that the UAV "was used to acquire a dense dataset" (p9). How it was flown is not stated. | **NOT FOUND** ("human-piloted" is an inference) |
| Sim number (abstract of [42]) | — | ">90% of hidden objects in simulated forests" (p1) | (not used in the manuscript) |

### [43] Srijiranon et al. 2025, *Appl. Syst. Innov.*, record 66

| field / claim (line) | manuscript says | PDF says (page) | status |
|---|---|---|---|
| System description (597) | "a low-cost drowning-detection buoy" | A shore monitoring station (Raspberry Pi 5, webcam, YOLO12m drowning detector + YOLOv5m USV tracker) commands an FT009 RC speedboat by radio (p1, p3–p5). "Robobuoy" is the system name; buoys were the targets (p14). | **WRONG** |
| Test setting (597) | "validated only in a calm indoor pool" | "still or near-still water… negligible wind and no measurable current, corresponding to an indoor pool environment" (p4). A 6.0 × 4.0 m still-water pool (p14). Outdoor or larger settings were not evaluated (p14). | OK |
| n (597) | "n = 9 trials" | 3 targets × 3 trials = nine runs, all successful, within 1 m, 11–23 s (p1, p14–p15) | OK |
| Missing context | — | "stationary buoys were used as repeatable victim surrogates. No hardware trials were conducted with human subjects" (p14). The drowning detector was validated only on datasets (mAP@0.5 0.9284). | INCOMPLETE CONTEXT |

### [44] He et al. 2026, *J. Field Robotics*, record 100

| field / claim (line) | manuscript says | PDF says (page) | status |
|---|---|---|---|
| Description (597) | "flight-trajectory optimization that improves detection confidence without modifying the underlying detector" | V-circular trajectory with a pretrained YOLOv11m. The paper emphasizes trajectory rather than detector improvement (p1, p4, p6). | OK |
| Validation | (FA; not stated) | Numerical simulations (p6–p8) plus real-world DJI Mini 3 Pro experiments in a playground, a bushy area and a forested region (p8–p9) | Partial (consistent with Sec. 16 note) |

### [45] Gowry Sailaja et al. 2026, *IEEE TMC*, record 124

| field / claim (line) | manuscript says | PDF says (page) | status |
|---|---|---|---|
| Description (597) | "lightweight survivor-location-prediction-plus-path-planning framework" | PSL prediction + PB-PAPP + weight synthesis (p1–p2) | OK |
| Limitation (597) | "its own authors note performs best only in low-density rural settings" | "PB-PAPP works best in rural or sparsely populated areas with low population density"; in dense urban areas exhaustive search is more beneficial. It may also not scale to larger grids (p10). | **OVERSTATED (minor).** The source has no "only", and the grid-size limitation is omitted. |
| Validation | (FA) | Pygame grid simulation; ground truth from xBD satellite imagery (p6–p7); assumes "fair weather conditions" (p2) | Simulation only |

### [46] Cruz Ulloa et al. 2026, *Biomimetic Intell. Robot.* (pre-proof), record 22

| field / claim (line) | manuscript says | PDF says (page) | status |
|---|---|---|---|
| Description (599) | "bio-inspired quadruped using material-aware semantic risk-mapping to cut slippage on unstable rubble" | CNN semantic + depth risk maps. Against a geometric baseline, average slip fell from 0.18 to 0.05 m/m (about 72%) and success rose from 65% to 95%, over 20 trials on surfaces of varying friction (e.g., varnished wood, loose debris) with localized smoke (p28–p29). | INCOMPLETE CONTEXT. The test environment is an indoor NIST-style arena / Isaac Sim (p17–p18), not "rubble" as such, and the PDF does not state whether the 20-trial comparison was physical or simulated. |
| Validation | (FA; not stated) | Isaac Sim campaign plus physical trials with Unitree Aliengo and Go2 in the CAR-Robotics-Arena (p24–p27) | Partial |
| Platform (6B) | Legged | two quadruped models, one class (p24) | OK |

### [47] Cho, You & Choi 2026, *IEEE Access*, record 53

| field / claim (line) | manuscript says | PDF says (page) | status |
|---|---|---|---|
| 40% figure (599, 625, 651) | "only a 40% path-planning success rate even with chain-of-thought" | CoT raised success "from 20% to 40%" (p1, p6). Without CoT, both models managed 2 of 10 trials (p5). n = 10 trials. | OK (add n = 10) |
| Author characterization (599) | "a figure the authors themselves describe as **inadequate** for safety-critical deployment" | "the overall success rate remains **modest** for safety-critical applications" (p6) | **OVERSTATED** |
| Author characterization (625) | "modest for safety-critical applications" | same (p6) | OK |
| Readiness claim (625) | "explicitly state, in their own words, that their tested system is not ready for real deployment" | No such statement. Closest: success rate "modest for safety-critical applications" (p6), and "Rather than tasking an MLLM with end-to-end control, a more robust approach is to leverage it as a high-level commander" (p7). | **OVERSTATED** |
| Quote (599) | "supervising high-level goals, validating critical decisions, and intervening when necessary" | verbatim (p7) | OK. Context: the authors present this as a property of *their proposed framework* (Fig. 2 includes a human operator, p3), not just as a recommendation. |
| MHC (625) | high-level reasoner under human "Meaningful Human Control," rather than for direct control | "ensuring Meaningful Human Control (MHC) is imperative" plus the high-level-commander passage (p7) | OK |
| Untested safeguard (599, 625) | never implemented or tested in RQ1/RQ2 | RQ2 "evaluated whether the MLLM could independently control the UGV using only aerial imagery" (p5); no human step is reported | OK |
| 86% mAP (625, 651) | perception "reached 86% mAP" via 5-shot ICL | "up to 86%" (p1), at IoU threshold 0.3 (p5) | INCOMPLETE CONTEXT (lenient IoU 0.3; "up to") |
| Validation | (FA) | "lab-scale disaster response environment" with toy figures and markers, imagery from a quadcopter (p3–p5) | Prototype/lab-scale (consistent with "never field-tested") |
| Line 611 claim | verbatim "independently control the UGV" | p5 | OK |

### [48] Vani et al. 2026, *Discover Appl. Sci.*, record 54

| field / claim (line) | manuscript says | PDF says (page) | status |
|---|---|---|---|
| Description (599) | "a modular, dual-LoRa/Wi-Fi hexapod with swappable terrain-specific legs" | A "dual communication system namely LoRa and Wi-Fi" (p1). Leg components "can be switched easily": buoyant legs for water, pointy legs for mud, grippy legs for rock (p4). | OK (wording: "dual-LoRa" can be misread as two LoRa links) |
| Mode (cluster "novel autonomous platform"; Table VII Legged/FA) | Fully Autonomous | "The hexapod robot combines manual and autonomous operational modes" (p1). Operators can "take over and guide the robot remotely" (p9). Manual mode needs an operator over Wi-Fi (p10). The results describe both modes and mode switching (p11). | **INCOMPLETE CONTEXT / label contestable.** See §2. |
| Validation | (FA) | Python leg-IK simulation, prototype build, LoRa at 500 m, a two-position sensor reading table (p11–p15). Mission-representative testing is not described. | Prototype bench test |

---

## 2. Per-paper label summary (share C)

The manuscript/Sec. 6 columns use only what the `.md` exposes: Sec. 6B platform, and FA mode from the IV-D cluster membership. Validation/scenario/sensor cells are my reading of the source and **cannot be diffed against the extraction table, which is absent**.

| Ref | Rec | Platform (6B → PDF) | Mode (ms → PDF reading) | Validation (PDF) | Scenario (PDF) | Sensors (6F flags, PDF) | Compute at runtime (6D) | Human role modelled in test | Env-realism limitation self-reported |
|---|---|---|---|---|---|---|---|---|---|
| [36] | 20 | UAV → UAV ✓ | FA → FA ✓ | **Real-world** (1 autonomous flight, underground parkade) | Underground/GNSS-denied (parkade as proxy) | Visual, Depth (ZED 2), LiDAR (LiDAR-Lite altimeter), IMU | Onboard/Edge (Jetson Xavier NX) | N | Y: SAR-scenario testing deferred (p12); low-texture depth degradation (p13) |
| [37] | 46 | UGV → UGV ✓ | FA → FA ✓ | Simulation only | Generic post-disaster (Gazebo corridor/hospital) | LiDAR, IMU (+odometry) | PC/Offline | N | **N (NOT FOUND)** |
| [38] | 51 | UGV → UGV ✓ | FA → FA ✓ | **Partial** (sim/bench + pilot indoor robot logs) | Collapsed/underground, generic | Visual, Thermal, IMU, Acoustic | Onboard/Edge (ARM SBC) | N | Y: smoke/heat, indoor-only field scope (PDF p40 / jnl p33) |
| [39] | 55 | UGV → UGV ✓ | FA → FA ✓ | **Real-world** (30 outdoor trials, emulated volcanic terrain) | Other (volcanic) ✓ | GPS, IMU (+magnetometer) | Onboard/Edge (Arduino) | Partial (manual heading-lock reset) | Y: no airborne ash, thermal gradients or magnetic anomalies (p8) |
| [40] | 82 | UGV → abstract robot (borderline) | FA → FA ✓ | Simulation only | Underground/Mine | modelled LiDAR/ultrasonic assumptions only (no real sensor) | PC/Offline | N | Y: environmental uncertainty not modelled; dust/LiDAR to be modelled later (p10, p14) |
| [41] | 11 | UAV → UAV ✓ | FA → FA ✓ (operator initializes and monitors only) | Simulation only | Generic/park terrain (Gazebo Baylands) | Thermal, Visual, GPS, (TOF range) | PC/Offline (SITL) | N (monitoring only) | Y: simulation only; smoke/rain future (p25) |
| [42] | 17 | UAV → UAV ✓ | FA → FA ✓ (Precedent B) | Partial (sim + one offline-scored real dataset) | Wilderness/Forest | Visual, GPS (geotags) | PC/Offline | N (flight method unstated) | Borderline: real experiment "less comprehensive" (p7) |
| [43] | 66 | USV → USV ✓ | FA → FA ✓ ("fully autonomously without human interference", p15) | Prototype/hardware pool test | Maritime/Water (pool) | Visual (station webcam) | Hybrid (shore RPi 5 + RC boat) | N | Y: still water, stable lighting, no outdoor tests (p4, p14) |
| [44] | 100 | UAV → UAV ✓ | FA → FA ✓ | Partial (sim + real DJI flights) | Generic (playground, bush, forest) | Visual | not determinable | N | Borderline: lighting/weather cited only as fit noise (p11) |
| [45] | 124 | UAV → UAV (abstract agents) | FA → FA ✓ | Simulation only (Pygame) | Generic (xBD imagery) | None/abstract (camera assumed) | PC/Offline | N | Borderline: "fair weather" is an *assumption* (p2) |
| [46] | 22 | Legged → Legged ✓ | FA → FA ✓ | Partial (Isaac Sim + arena trials) | Generic/collapse-like indoor arena | Visual + Depth (RGB-D) ✓ (per 6F correction) | not determinable from the text read | N | Y: smoke/unstable-debris misclassification (p21) |
| [47] | 53 | Hybrid → Hybrid ✓ (UAV imagery + UGV) | FA → FA ✓ (Precedent E) | Prototype/lab-scale | Generic (toy-scale flood/earthquake framing) | Visual | Cloud ✓ (Gemini 1.5 Pro / GPT-4o) | N in test (operator only in the architecture) | **N (NOT FOUND)** |
| [48] | 54 | Legged → Legged ✓ | FA → **contestable (manual + autonomous modes)** | Prototype bench test | Generic (collapsed/underground framing) | LiDAR, Thermal (IR), Gas (MQ-135), IMU (gyro), + temp/humidity/pressure | Onboard/Edge (RPi Zero W + STM32), with telemetry to a PC | **Y** (manual mode/GUI) | **N (NOT FOUND)** |

**Effects on aggregates (for the stats checker; not asserted as errors):**
- **FA real-world field tests = 2/27.** In this share alone, [36] and [39] are both physical real-world tests with no simulation part. If the extraction coded them as "Real-world field test", they may be the corpus's only two FA field tests. If either was coded "Partial" or "Prototype", that coding contradicts the source. Check columns T and S for records 20 and 55.
- **UAV field-tested 1/13.** [36] is the only UAV paper in this share with a real hardware-only test. [42] and [44] have partial real-world components.
- **Table VII Legged/FA = 2** requires [48] to be FA (see §0 item 6).
- **35/39 environmental-realism figure:** see §0 item 7.

---

## 3. WRONG / OVERSTATED items, with suggested Markdown (paraphrased; for the authors to apply and log in Sec. 16)

1. **Line 595: single-robot cluster validation (WRONG for [36], [38], [39]; NOT FOUND for [37]'s future-work clause).** Replace the last sentence once [34]/[35] are confirmed by share B. A draft for the case where both are simulation-only:
   > Real-world evidence in this cluster is mixed: four of the seven are validated in simulation only ([34], [35], [37], [40]), one combines simulation with pilot indoor runs on a laboratory prototype ([38]), and two report physical tests without a simulation stage, a single autonomous flight in an underground car park ([36]) and 30 outdoor trials on emulated volcanic terrain ([39]).

   Then fix line 601 so that it does not contradict this sentence. For example, drop "the cluster with the most real-world testing (single-robot navigation) is still majority-simulation", or replace it with: "even the single-robot navigation cluster, which holds two of the corpus's physical-only tests, is majority-simulation".
2. **Line 597: [42] (OVERSTATED / INCOMPLETE CONTEXT).**
   > …next-best-view camera planning that, scored offline on images from a single real forest survey, selected views capturing 5 of 7 targets hidden from every top-down viewpoint ([42])…

   Also amend Sec. 6A Precedent B. Replace "human-piloted data-collection flight" with "a separate data-collection flight (flight method not stated in the source), scored offline". Log the change in Sec. 16.
3. **Line 597: [43] (WRONG).**
   > …a low-cost shore-station drowning detector that guides a radio-controlled surface vessel, with the vessel's navigation validated only in a still-water pool against stationary buoy targets ([43], n = 9 runs)…
4. **Line 597: [45] (minor OVERSTATED).** Drop "only": "…that its own authors note works best in sparsely populated rural areas and may not scale to larger search grids ([45])."
5. **Line 599: [47] (OVERSTATED).** Replace "a figure the authors themselves describe as inadequate for safety-critical deployment" with "a level the authors themselves call modest for safety-critical applications (4 of 10 trials)".
6. **Line 625: [47] (OVERSTATED).** Replace "explicitly state, in their own words, that their tested system is not ready for real deployment" with "explicitly flag, in their own words, that their tested system falls short of what real deployment would require". Also check that [20] (share A) still fits the reworded framing. Optionally qualify "86% mAP" as "up to 86% mAP at an IoU threshold of 0.3".
7. **Line 599: [48] (wording, plus a label to flag).** Replace "dual-LoRa/Wi-Fi" with "dual-link (LoRa and Wi-Fi)". Flag to the authors that [48] reports switchable manual and autonomous modes. Under Sec. 6A's "classify by what was tested" heuristic, the FA label needs a documented basis in the Notes. Otherwise it is a candidate for re-classification, which would change Tables V, VII and XI. Do not change it without author review (CLAUDE.md rule 3).
8. **Line 599: [46] (INCOMPLETE CONTEXT, optional).** "…to cut slippage (about 72% lower than a geometry-only planner) on mixed-friction surfaces in an indoor test arena ([46])".
9. **Line 595: [37] (INCOMPLETE CONTEXT, optional).** "improved-AMCL localization and smoothed A* planning for Ackermann-steered ground vehicles ([37])".

---

## 4. Audit completeness
- Fully audited: [36], [37], [38], [39], [40], [41], [42], [43], [44], [45], [46], [47], [48] (13/13).
- Not audited: none in this share. [34] and [35] were excluded as share B, so the 7-paper cluster count above is partial by design.
- Not possible: a cell-by-cell comparison with the extraction table (xlsx not in the project). The validation/scenario/sensor/architecture labels in §2 are source-based readings to cross-check against columns S–AH.
