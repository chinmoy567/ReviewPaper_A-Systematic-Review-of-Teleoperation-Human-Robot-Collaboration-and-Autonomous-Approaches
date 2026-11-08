# Corpus-claim audit, share A: references [10]–[22]

**Agent:** corpus-claim-auditor (instance A) · **Date:** 2026-11-08
**Scope:** 13 included papers, [10]–[22] (record IDs 6, 77, 116, 5, 45, 57, 73, 106, 119, 105, 113, 126, 9), mapped with `data/id_map.csv`.
**Sources read:** full-text PDFs in `assets/papers/`, extracted with `pdftotext` and cited by PDF page. Manuscript claims come from `SAR_review_master_document.md` Secs. 9–14, plus Sec. 6A–6F rules and precedents.
**Coverage:** all 13 papers fully audited. None are unaudited.

**Limitation of this audit:** the per-paper clean labels (columns S–AH of the `Extraction` sheet) are **not in the .md**. The workbook is not in the project; the only local `.xlsx` is `assets/docs/paperlinks.xlsx`. So I can only infer each paper's validation, compute, scenario and sensor flags from the aggregate tables (V–XII) and the Sec. 6B/6D/6E notes. Wherever the manuscript does not state a label for a paper, the "manuscript says" cell reads *inferred* or *not stated*.

Status codes: `OK` · `WRONG` · `OVERSTATED` · `INCOMPLETE CONTEXT` · `NOT FOUND`.

---

## 1. Per-paper evidence tables

### [10] — ID 6, Cafolla et al. 2026 (universal SAR platform)

| Field / claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Platform (579; 6B) | Hybrid/Multi-Platform: drone + quadruped | DJI Tello drone and FREENOVE quadruped, each tested indoors and outdoors (p.4, p.7–10) | OK |
| Description (579) | Universal voice-controlled add-on controller | Modular add-on controller for any robot that accepts text commands. It does not replace the robot's own logic (p.1, p.3) | OK |
| Mode (579, 6A-Prec. A) | Teleoperation | Voice intents are atomic, magnitude-specified moves (take-off, move forward N cm, turn N deg) (p.4). Precedent A applies | OK (label) |
| "in every one of the five papers, locomotion remains entirely human-driven" (579) | Entirely human-driven | The patrol phase flies a **pre-programmed ascending spiral** autonomously (p.4–5). The quadruped was "programmed to follow" fixed rectangular and linear trajectories (p.8, p.10). The drone's **person-follower** moves the drone autonomously along x/y/z to keep a face centred (p.6), and this was tested (p.12). | **OVERSTATED** |
| Validation (inferred: one of the 3 Teleop field tests) | Not stated | Indoor tests on a lab mock-up (3D-printed ruined cottage and grain bin, IoT & Robotics Lab). Outdoor "uncontrolled" tests in 23 km/h wind, 17 °C (drone) and 22.9 km/h, 9 °C (quadruped) (p.4, p.6–7, p.9) | OK if coded field test, with the caveat that it is a small-scale campus test |
| Compute (6D) | Not listed per paper | Raspberry Pi on the drone, laptop ground station, and Google Cloud for voice NLU only. Person detection is local (p.3–4, p.11) | Hybrid fits |
| Env-realism limitation | (part of corpus 35/39) | None self-reported. The paper claims robustness in wind and noise. Its limits are NeRF speed and the quadruped's camera perspective (p.11–12) | See Sec. 2 |

### [11] — ID 77, Jia et al. 2025 (amphibious caged UAV)

| Field / claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Platform (579; 6B) | Hybrid: terrestrial–aerial UAV | Ground–air amphibious UAV that rolls on its cage and flies (p.1, p.17) | OK |
| Separation cage removes camera/LiDAR occlusion of earlier single-cage designs (579) | As stated | Earlier caged UAVs obstruct cameras and LiDAR, and the separation cage removes this (p.2, p.18) | OK, with a note: the prototype carries **no LiDAR**. Its sensors are a RealSense D435 depth camera, an IR camera and an IMU (p.10, p.14). The claim is about the design, not the sensors fitted. |
| Mode (579) | Teleoperation | Prototype "tested via remote control" on the ground and in confined-space flight (p.17). Yun Zhuo H16 remote controller (p.11) | OK. Note that an autonomous depth-camera "Vertical Operation Mode" passage-traversal decision is described (p.10, p.18) but not tested quantitatively. |
| "navigation autonomy explicitly deferred as future work in three of the five ([14], [11], [12])" (579) | [11] defers navigation autonomy | Limitations cover only onboard sensors (RF sensors possible) and budget-shortened impact and recognition testing (p.18–19). **No statement defers navigation autonomy.** | **WRONG** |
| Validation (inferred field test) | Not stated | Ground runs on Nanjing Funiu Mountain and a flight test in a forest (p.17) | OK |
| Compute | Not stated | YOLOv5s-Ghost trained on an RTX 3060 PC (p.14). Runtime location is not stated clearly ("real-time object detection", p.18) | UNVERIFIED |
| Env-realism limitation | — | Not self-reported (limits are budget and testing scope) | See Sec. 2 |

### [12] — ID 116, Liu et al. 2026 (wheeled hexapod)

| Field / claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Platform (579; 6B) | Hybrid: wheel-leg chassis | Stewart-structured wheel-legs (p.1, p.3) | OK |
| "1,200 kg-payload" (579) | 1,200 kg | Payload capacity 1200 kg, measured on the prototype (Table 5, p.21) | OK |
| "exceeding the payload capacity of comparable legged systems" (579) | Comparable legged systems in general | Compared with **three wheeled hexapods only** (BITNAZA, ASTERISK H, ATHLETE), whose figures come from their own papers (p.21) | INCOMPLETE CONTEXT (say "three comparable wheeled-hexapod platforms") |
| Hierarchical control keeps body attitude stable on uneven terrain (579) | As stated | AMPC attitude stabilisation over a force-position hybrid controller (p.13, p.16–19) | OK |
| Mode (579, Prec. C) | Teleoperation | Operator drives the chassis and the arm by joysticks from a console using live video (p.13, p.18) | OK |
| Navigation autonomy deferred as future work (579) | [12] defers it | Future work covers extreme terrain (boulder fields, deep soft ground, loose steep slopes) through **mechanical structure, terrain perception and locomotion control** (p.22). Navigation autonomy is not mentioned. | **OVERSTATED** |
| Validation | Inferred field test | Field trials on a rough gravel slope and at a firefighting and disaster-relief drill site (p.21) | OK |
| Compute | — | Onboard i9-9900K host computer and GPU, plus a remote console (p.3) | — |
| Env-realism limitation | — | Yes: not validated on more extreme terrain (p.22) | Y |

### [13] — ID 5, Raghavan et al. 2026 (YOLOv8 debris victim detection)

| Field / claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Platform (6B) | UGV | Four-wheeled robotic vehicle carrying a Jetson Nano and a Logitech C270 (p.11) | OK |
| "YOLOv8-based occluded-victim detector reaching 93.1% mAP" (579) | 93.1% mAP | mAP@0.5 = 93.1%, recall 90.5%, on a held-out custom test set (p.10–11). The detector targets partially visible faces, palms and body parts (p.2) | OK. Context worth adding: the authors say the 93.1% holds only under test-set-like conditions, and the dataset mixes web images with Gretel.AI synthetic images (p.9, p.11). |
| Mode (579) | Teleoperation | The robot "must be manually controlled to move through a debris field" (p.12) | OK |
| Navigation autonomy deferred as future work (579) | **[13] not listed** among the three | Autonomous navigation is explicitly named as a limitation and as future work: SLAM or DRL mobility "without human input" (p.12, p.15) | **WRONG by omission**: [13] belongs in this list and [11] does not |
| Validation | Inferred (bench or partial) | Controlled setting with a simulated debris environment and artificially generated images. Field trials are listed as future work (p.11, p.14–15) | Prototype bench test fits |
| Compute | — | Jetson Nano onboard, Firebase cloud for alerts, model trained in Colab (p.2, p.9) | Onboard/Edge |
| Env-realism limitation | — | Yes: dust, smoke, wet surfaces, lighting (p.11); controlled setting (p.15) | Y |

### [14] — ID 45, Khattab et al. 2025 (SERR)

| Field / claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Platform (6B) | UGV | Four-wheel-drive chassis, Arduino, RF module (p.10) | OK |
| Mode (579) | Teleoperation | Smartphone or PC movement buttons, with an automatic stop 30 cm from obstacles (p.11, p.13) | OK (the reactive stop falls under Precedent C) |
| "multi-modal visual-thermal-audio fusion system explicitly reported as untested on the physical prototype itself, validated only against synthetic data" (579) | As stated | RescueNet CNN-LSTM was validated in MATLAB on USGS-PAGER data plus simulated audio (p.1, p.18–19). "No physical field tests have been conducted" (p.23). The two-way audio is not implemented on the prototype (p.1, p.16) | OK |
| Navigation autonomy deferred (579) | [14] defers it | "limited autonomy ... will change in subsequent versions" (p.11). Future work will let the robot manoeuvre around obstacles independently (p.18) | OK |
| Compute (6D: Hybrid, perception "on a separate desktop PC at operational time") | Hybrid | Grid-Eye data goes over RF to a PC dashboard, which does the thermal display and detection (p.10, p.13). RescueNet runs only in a desktop MATLAB simulation (p.18) | Partly OK. The live PC split covers the thermal display only. RescueNet never ran live. |
| Env-realism limitation | — | Yes: dust, smoke, vibration, EMI (p.23) | Y |

### [15] — ID 57, You et al. 2026 (coal-mine rescue robot digital twin)

| Field / claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| "field-validated in genuinely hazardous underground environments" (583) | Genuinely hazardous underground site | Tests took place in a **tunnel inside CUMT's Coal Dust and Gas Explosion Laboratory**, with coal dust and debris placed to simulate an explosion scene (p.20). The paper itself says "simulated tunnel" and "simulated roadway" (p.24–27) | **OVERSTATED** |
| Direct point-cloud navigation and a digital-twin operator interface (583) | As stated | Navigation and obstacle avoidance run directly on the laser point-cloud map, with a digital-twin interface (p.2, p.9) | OK |
| Mode (583) | Supervisory | "The operator clicked waypoints on the navigation interface". Waypoint navigation "with no manual intervention" (p.25, p.27) | OK |
| Scenario | Underground/Mine | Mock coal-mine roadways (p.20) | OK |
| Sensors | — | LiDAR, IMU, binocular camera with IR, and CD10 gas, temperature and humidity sensors. UWB was not used (p.6–7, p.9, p.25) | — |
| Env-realism limitation | — | Yes: comms nodes pre-deployed; terrain model cannot handle sudden collapses or falling rocks; map degradation (p.28) | Y |

### [16] — ID 73, Ahmad & Humbert 2025 (ScanPlan, SubT)

| Field / claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| "a sampling-based semantic-navigation planner spanning legged and wheeled platforms, tested live at the DARPA Subterranean Challenge finals" (583) | The semantic-navigation planner was tested at the finals | The **ScanPlan exploration planner** ran at the finals in the Louisville Mega Cavern on 2 Spot and 2 Husky robots (p.20–23). The **semantic-navigation extension** was tested only on one Spot in CU Boulder's Engineering Center building, after an initial manual teleoperation pass (p.31–32) | **INCOMPLETE CONTEXT** (two separate tests are merged into one) |
| "though its planned aerial component was never actually deployed in the field" (583) | As stated | "quadrotor UAVs were not deployed in SubT challenge finals" (p.9) | OK |
| "field-validated in genuinely hazardous underground environments" (583) | Hazardous | A competition course built to contain dust, fog, rubble and dripping water (p.20). It is a realistic course, not a disaster site | OK, with a softening suggested |
| Mode | Supervisory | Human-supervised autonomy. Higher-level mission-management commands (p.22). In the semantic test, the human picks the goal region (p.25) | OK |
| Platform (6B) | Hybrid (legged + wheeled, both deployed) | As stated (p.20) | OK |
| Env-realism limitation | — | No environmental limitation found. Future work concerns semantic-map error correction (p.35–36) | N |

### [17] — ID 106, Ruan et al. 2025 (semantics-based SA framework)

| Field / claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Interpretable indicator layer that experts can tune and that avoids an opaque end-to-end DL design (583) | As stated | Uses heuristics and expert knowledge rather than data-driven training, and is explainable unlike black-box models (p.5, p.11) | OK |
| "a companion mock-up study associated with reduced operator reaction time and cognitive workload when switching autonomy level, and increased trust" (583) | Companion study | One Discussion sentence reports these results and cites **Ruan et al. (2025), arXiv:2507.17376**, an unrefereed preprint (p.12–13). **[17] measures no workload, trust or reaction time itself.** It has no participants, and its experiments I and II evaluate SSR scores (p.8–11) | OK as worded ("companion"). **Re-confirmation of the brief's known issue:** "[17] measures workload and trust" is **not correct for [17] itself**. The evidence sits in a different, unreviewed preprint. |
| "the corpus's clearest evidence for what well-designed supervisory HRI delivers operationally" (583) | Strong evidence claim | The HRI evidence is a one-sentence citation to an arXiv preprint. [17]'s own tests involve no operator | **OVERSTATED** |
| Headline validation used autonomous waypoint navigation to keep trajectories constant; one manual repositioning for the radiation source (583) | As stated | "Autonomous navigation was applied because we would like to keep similar trajectories" (p.7). The high-strength radiation case "needed teleoperation and positioning of the robot close to the source" (p.8) | OK |
| Mode | Supervisory | The tested pipeline has the experimenters predefine waypoints. No live operator decides anything during the trials (p.7) | Borderline. See Sec. 2 |
| Validation | Inferred, possibly one of 3 Supervisory field tests | Indoor lab arena with placed hazmat signs, uranium rock, curtains. Jackal robot (p.5, p.7–9) | If coded "Real-world field test": OVERSTATED (this is a lab test) |
| Sensors | — | RealSense D435i (RGB-D), Velodyne VLP-16, Hamamatsu gamma sensor. Onboard i5 + GTX1650Ti (p.7) | Visual + Depth + LiDAR + Gas/radiation |
| Env-realism limitation | — | Only "the vision system constrains the implementation" (p.12) | N |

### [18] — ID 119, Schomer & Adams 2026 (terrain-aware MSAR UAV planner)

| Field / claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Real constraint: flights interrupted by weather, battery or terrain before the planned area is complete (583) | As stated | Every field flight ended early: 5 of 7 from **lost line-of-sight**, 1 from a cold battery, 1 from the low-battery threshold. One UAV was lost to wind (p.13–17) | OK; INCOMPLETE CONTEXT: the main interruption was visual line-of-sight loss, which the sentence leaves out |
| Strict priority so an interrupted flight still covers the highest-value area (583) | As stated | d-relaxation = 0. "every flight covered at least 90% of the priority 1 search area" (p.17) | OK |
| Mode | Supervisory | An MSAR expert draws the priority areas. The planner and autopilot fly the viewpoints. The pilot can abort or RTL (p.12, p.14) | OK |
| Validation | Inferred UAV field test (1/13) | Simulation plus 7 field flights at Hayrick Butte with the Corvallis Mountain Rescue Unit (p.12–15) | OK (field). It could also be coded Partial. |
| Scenario | Wilderness/Mountain | Mountain SAR (p.1, p.12) | OK |
| Env-realism limitation | — | Yes: wind, snow glare, cold battery, line-of-sight (p.13, p.17–18) | Y |

### [19] — ID 105, Bhattacharya & Butail 2025 (teleoperator-state inference)

| Field / claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| "[19] has a human directly teleoperate a primary search UAV while a structurally separate autonomous swarm infers the operator's cognitive/knowledge state from movement patterns alone ... and adapts its own search strategy" (587; Prec. G) | Live coupling of human and adaptive swarm | In the **live human study** (H1–H3), participants flew a virtual UAV in Unity alongside a **quasi-static** swarm (p.5). The **adaptive swarm** (H4) was evaluated in a simulation that **replays recorded participant trajectories** (p.17). No live human was in the loop with the adaptive swarm. | **INCOMPLETE CONTEXT / OVERSTATED**, and it weakens Precedent G's statement that the live pilot is an explicit independent variable of the coupled system |
| "deliberately avoiding the need to transmit sensitive EEG or eye-tracking data" (587) | As stated | Only pose is shared, because cognitive-state information "may create security vulnerabilities" and needs bandwidth (p.4) | OK (a fair paraphrase) |
| "the authors report the underlying physiological correlations were only 'weak'" (587) | "weak" | EEG cognitive load shows "very weak" correlation with movement. Saccade frequency and alpha-SA show "weak" correlation (p.13) | OK |
| Platform / validation | UAV; simulation | Virtual quadrotor in a Grand Canyon virtual environment. EEG and eye-tracking participants (p.5, p.7) | OK |
| Env-realism limitation | — | Yes: wind, GPS loss under vegetation, comms dropouts (p.23) | Y |

### [20] — ID 113, Gaitan et al. 2025 (AI rescue drone, cognitive agentic architecture)

| Field / claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| LLM-orchestrated multi-agent filtering and prioritisation instead of raw video, with a self-correcting loop (587) | As stated | Orchestrator agent with a feedback loop that re-prompts a sub-agent when it finds an inconsistency (p.2, p.23, p.25). Reports ranked by urgency (p.32) | OK |
| "validated only in controlled lab settings against synthetic scenarios" (587) | As stated | Synthetic JSON scenario inputs (p.25). Controlled lab only (p.30) | OK |
| "detection recall for occluded or partially buried victims as low as 2.6–26.4% mAP for the hardest occlusion classes" (587) | Recall, 2.6–26.4% mAP | These are **per-class mAP@0.5** values: block50 = 0.026, block75 = 0.072, block25 = 0.264 (p.15). Recall is reported separately from the confusion matrix (stand 48%, sit 40%, walk 39%, p.15). The classes are **occlusion levels** (25/50/75% blocked), not "buried". | **WRONG** (recall and mAP are conflated) |
| Each SC paper treats operator cognitive state as a design **and evaluation** target (587) | Evaluation target | Lowering operator cognitive load is the design aim (p.2), but **no operator or human-subject evaluation** took place. "No new data involving human subjects was collected" (p.12). Metrics are hazard-identification accuracy and self-correction (p.25) | **OVERSTATED** for [20] |
| Mode (Prec. D) | Shared-Collaborative | RC-piloted (p.7). The orchestrator can issue "autonomous activation of the delivery module" (p.23). **But** p.9 says the servo is remotely controlled by the human operator, who may get recommendations | OK as a label. The paper contradicts itself, so note it in Notes. |
| Quote (625): "the current validation ... technical feasibility... in a controlled laboratory environment. The system has not yet been tested in real disaster scenarios or with the direct involvement of emergency response personnel." | Quote | Matches p.30 exactly (the ellipsis leaves out "and evaluating the performance of its components and algorithms") | OK. **Rule-5 note:** about 35 quoted words. Consider paraphrasing or shortening. |
| Compute | — | ESP32-S3 onboard handles acquisition only. YOLO11 and the LLM run at the ground station (p.10) | Hybrid |
| Env-realism limitation | — | Yes: no real sensor noise, packet loss or visual complexity; wind drift on the payload (p.31) | Y |

### [21] — ID 126, You et al. 2026 (resilient MR human-swarm interaction)

| Field / claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| "in a simulated **maritime** risk-conflict scenario" (587) | Maritime | "a mountainous wilderness area where a flash flood trapped climbers in a valley" (p.8). Sec. 6E already re-bucketed it to Wilderness | **WRONG** (stale text that conflicts with Sec. 6E and Table XII) |
| "higher usability than a **conventional 2D control interface**" (587) | Compared with a 2D interface | The control condition is the **same HSI interface without resilience attributes** in the same simulator (p.11–12). SUS was higher for the experimental interface (85.125; t(34)=4.240) (p.14). "2D" appears only in participants' qualitative remarks and one questionnaire item (p.16, p.20, p.22) | **WRONG** |
| "psychological-resilience measures (via heart-rate-variability indicators)" (587) | Resilience measured by HRV | Resilience was measured with **CD-RISC and ER89 self-report scales** (p.12, p.14). HRV (pNN50, RMSSD, SDNN) indexed cognitive load and physiological recovery (p.12–16) | **WRONG / INCOMPLETE** |
| Improved SA (587) | As stated | SART: t(34)=4.279, p<0.0001 (p.13) | OK |
| "small, largely SAR-inexperienced sample (N = 35, reduced to 27 after physiological data loss)" (587) | As stated | 35 participants, of whom 5 had UAV-assisted SAR experience. 32 had UAV experience and 30 had VR experience (p.9). Only 27 **physiological** datasets were kept (p.15, p.19). Questionnaire analyses use N=35 | INCOMPLETE CONTEXT (the 27 applies to physiological data only) |
| Mode (Prec. F) | Shared-Collaborative | "The operator decides whether to implement the solution, replace the faulty UAV" (p.12) | OK |
| Sensors (6F: Physiological = ID 105 only) | Not Physiological | ECG/GSR wristband worn by participants (p.10) | **Disagreement with Sec. 6F / Table VIII** |
| Validation | Simulation | Unity VR on an Oculus Quest (p.9–10) | OK |
| Env-realism limitation | — | Yes: VR cannot reproduce real environmental variables (p.19) | Y |

### [22] — ID 9, Maresca et al. 2026 (localization-driven multi-robot exploration)

| Field / claim (line) | Manuscript says | PDF says (page) | Status |
|---|---|---|---|
| Multi-robot coordination cluster; "RF-signal-guided exploration re-prioritization" (593) | As stated | mmWave AoA/RSSI victim localization feeds the global planner, which re-prioritises goals (p.2, p.7–8) | OK |
| Multi-robot | Multi-robot | 1, 2 and 3 Jackal robots were evaluated. The single-robot case is also reported (p.15–17) | OK |
| Mode | Fully Autonomous | Centralised global and local planners, with no operator (p.7–9) | OK |
| Validation / platform | Simulation; UGV | ROS/Gazebo with a 2D MATLAB ray-tracer (p.8–10) | OK |
| Scenario | Generic | Indoor Gazebo "factory" world (p.9) | OK |
| Env-realism limitation | — | No explicit environmental limitation. Future work covers multiple victims, predictive planning and multi-floor buildings (p.17–18). Simplifications such as the 2D ray-tracer and a single reflection bounce are justified, not stated as limitations (p.9–10) | N |

---

## 2. Per-paper label summary (auditor's reading of the PDF)

Under "Disagreement", `!` marks a mismatch with the manuscript or Sec. 6, and `?` marks a label I could not check because the workbook is missing.

| Ref | ID | Platform | Mode | Validation | Scenario | Sensors (6F flags) | Human role modelled | Env-realism limitation | Disagreement |
|---|---|---|---|---|---|---|---|---|---|
| [10] | 6 | Hybrid (UAV + quadruped) | Teleop (with a tested autonomous follower and scripted patrols) | Field (small-scale campus) | Generic | Visual, Acoustic? (microphone for voice commands) | Y | **N** | ! "entirely human-driven" |
| [11] | 77 | Hybrid (air-ground) | Teleop (RC) | Field (mountain, forest) | Generic | Visual, Thermal, Depth, IMU (no LiDAR fitted) | Y (RC pilot) | **N** | ! not a "navigation deferred" paper |
| [12] | 116 | Hybrid (wheel-leg) | Teleop (joystick) | Field (drill site) | Generic | Visual (onboard perception), IMU/encoders, force sensors | Y | Y p.22 | ! "navigation deferred" overstated |
| [13] | 5 | UGV | Teleop (manual) | Bench / controlled | Earthquake | Visual | Y | Y p.11, p.15 | ! missing from the "navigation deferred" list |
| [14] | 45 | UGV | Teleop (+ auto-stop) | Bench + MATLAB sim | Earthquake | Visual, Thermal (Grid-Eye), LiDAR (ultrasonic); audio designed but not functional | Y | Y p.23 | — |
| [15] | 57 | UGV | Supervisory (clicked waypoints) | Field (lab mock tunnel) | Underground | LiDAR, IMU, Visual (binocular/IR), Gas | Y | Y p.28 | ! "genuinely hazardous" |
| [16] | 73 | Hybrid (Spot + Husky) | Supervisory | Sim + field (SubT finals); semantic part in a campus building | Underground | LiDAR, IMU | Y (mission commands, goal selection) | **N** | ! test venues merged |
| [17] | 106 | UGV (Jackal) | Supervisory (borderline: tested runs had predefined waypoints and no live operator) | Lab test | Generic | Visual, Depth, LiDAR, Gas (radiation) | **N** in this paper (only in the companion preprint) | **N** | ! HRI evidence lives in a different preprint; ? validation label |
| [18] | 119 | UAV | Supervisory | Sim + field | Wilderness | Visual, GPS | Y | Y p.13, p.17 | — |
| [19] | 105 | UAV (virtual) | SC (adaptive swarm tested only on replayed trajectories) | Simulation (human-in-loop VR + replay) | Wilderness | Visual (sim), Physiological (EEG, eye-tracking) | Y | Y p.23 | ! live-coupling claim |
| [20] | 113 | UAV | SC (paper contradicts itself on payload authority: p.9 vs p.23) | Lab, synthetic data | Generic (mountain-trail scenarios) | Visual, LiDAR (rangefinder), GPS, IMU | N (no human-subject testing) | Y p.31 | ! recall/mAP; ! "evaluation target" |
| [21] | 126 | UAV swarm (simulated) | SC | Simulation (VR) | Wilderness | Physiological (ECG/GSR); robot sensors simulated | Y | Y p.19 | ! maritime; ! 2D control; ! HRV ≠ resilience; ! Physiological flag |
| [22] | 9 | UGV (1–3 Jackals) | FA | Simulation | Generic | LiDAR, RF | N | **N** | — |

**What this means for corpus-level numbers (flag only; I did not recompute them):**
- **Physiological prevalence (Table VIII, 1 / 2.6%):** [21] used a human-worn ECG/GSR wristband, which meets the Sec. 6F definition ("human-worn"). Under that rule the count becomes **2 (5.1%)**. The authors need to decide whether the flag means robot sensing only. If it does, the definition should say so.
- **Environmental-realism gap (35/39, 89.7%):** under this agent's definition, **5 of my 13 papers** ([10], [11], [16], [17], [22]) do not self-report an environmental-realism limitation. The manuscript allows only 4 non-reporters in the whole corpus, so the original coding must have used a looser definition, or at least one of these five was coded "Y". The 89.7% figure and the 95.2%/83.3% split in Sec. V-B cannot be reproduced from my share without the workbook's per-paper column. **This needs checking before submission**, because the number appears in the abstract and conclusion.
- **[17] validation label:** if [17] is one of the "3 of 4 Supervisory real-world field tests", it is a lab test, which would weaken the 75% figure.

---

## 3. WRONG / OVERSTATED items with suggested corrected wording (paraphrased, Markdown)

1. **[21] scenario (line 587), WRONG.** Replace "in a simulated maritime risk-conflict scenario" with:
   > "in a simulated mountain-wilderness scenario (climbers trapped in a valley by a flash flood)"

2. **[21] comparison condition (line 587), WRONG.** Replace "alongside higher usability than a conventional 2D control interface" with:
   > "alongside higher usability than the same interface with its resilience features removed (within-subject comparison)"

3. **[21] resilience measure (line 587), WRONG/INCOMPLETE.** Replace "psychological-resilience measures (via heart-rate-variability indicators)" with:
   > "self-reported psychological-resilience scores (CD-RISC, ER89), with heart-rate-variability indicators used as a physiological index of workload and recovery"

   Also change the sample clause to: "(N = 35; physiological analyses on 27 after signal loss)".

4. **[20] occlusion metric (line 587), WRONG.** Replace "with detection recall for occluded or partially buried victims as low as 2.6–26.4% mAP for the hardest occlusion classes" with:
   > "with per-class mAP@0.5 for partially occluded victims of only 0.026–0.264 across the occlusion classes"

5. **[20] "evaluation target" (line 587), OVERSTATED.** Qualify the opening sentence of IV-C, for example:
   > "each treats the operator's cognitive or psychological state as a first-class design target, and two of the three ([19], [21]) also evaluate it with human participants"

6. **Navigation-deferred list (line 579), WRONG.** Replace "navigation autonomy explicitly deferred as future work in three of the five ([14], [11], [12])" with:
   > "navigation autonomy explicitly deferred as future work in two of the five ([13], [14])"

   [11]'s future work concerns RF sensing and fuller impact and recognition testing. [12]'s concerns extreme-terrain mechanics, perception and locomotion control. If the authors want a count of three, they must find a third paper with an explicit deferral; I found none among [10]–[12].

7. **"Entirely human-driven" (line 579), OVERSTATED for [10].** Suggested:
   > "in every one of the five papers the human directs locomotion (in [10], aside from scripted patrol trajectories and an autonomous person-following mode)"

8. **[15] test site (line 583), OVERSTATED.** Replace "were field-validated in genuinely hazardous underground environments" with:
   > "were field-tested in realistic underground settings: a mock coal-mine roadway inside a university gas- and coal-dust explosion laboratory ([15]) and the DARPA SubT finals course ([16])"

9. **[16] test venues (line 583), INCOMPLETE CONTEXT.** Suggested:
   > "a sampling-based exploration planner run live on legged and wheeled robots at the DARPA SubT finals, whose semantic-navigation extension was then tested separately on a single legged robot in a university building ([16]; the planned aerial component was never fielded)"

10. **[17] evidence strength (line 583), OVERSTATED.** Suggested:
    > "[17]'s semantics-based situational-awareness framework offers an interpretable indicator layer that experts can tune, rather than an opaque end-to-end model. Its own experiments test the indicator layer on an autonomously driven robot; the operator benefits (shorter autonomy-switching reaction time, lower workload, higher trust) come from a companion study that is so far available only as a preprint [cite arXiv:2507.17376 if retained]."

    Drop "the corpus's clearest evidence". Per Rule 1, the companion preprint has not been verified for content.

11. **[19] live-coupling claim (line 587; Sec. 6A Prec. G), OVERSTATED.** Suggested:
    > "[19] records human operators flying a primary search UAV in a virtual wilderness alongside a stationary swarm, then shows in replay simulation that a swarm inferring the operator's knowledge state from movement alone could adapt its search strategy, though the physiological correlations were only weak"

    The authors should also note in Sec. 6A Precedent G that the adaptive coupling was tested on replayed, not live, trajectories. The SC label may still stand at the design level, but the classification note should state this.

12. **[12] payload comparison (line 579), INCOMPLETE CONTEXT.** Replace "exceeding the payload capacity of comparable legged systems" with:
    > "exceeding the payload of three comparable wheeled-hexapod platforms"

13. **[18] interruption causes (line 583), minor.** Add line-of-sight: "routinely cut short by line-of-sight loss, wind, battery or terrain".

14. **[20] long verbatim quote (line 625), Rule 5 risk (not wrong).** The quote is accurate (p.30) but runs about 35 words. Consider a shorter quote, for example "has not yet been tested in real disaster scenarios", with the rest paraphrased.

---

## 4. Re-confirmation of the four known issues from the brief

| Known issue | Re-confirmed? | Evidence |
|---|---|---|
| [21] scenario is a mountain-wilderness flash flood, not maritime | **Yes** | p.8 |
| [20] per-class mAP@0.5 is 0.026–0.264, not recall | **Yes**: block50 0.026, block75 0.072, block25 0.264 | p.15 |
| [10] has an autonomous person-follower sub-mode | **Yes**, and it **was tested** on the drone (not on the quadruped). Scripted patrol trajectories also exist. | p.6, p.11–12; p.4, p.8, p.10 |
| [17] measures workload and trust | **Partly.** [17] *reports* lower workload, shorter reaction time and higher trust, but cites them to a companion **arXiv preprint** (Ruan et al., 2025, arXiv:2507.17376). [17]'s own experiments have no participants and no workload or trust measures. | p.12–13 |

## 5. New issues not in the brief
- The "navigation deferred as future work" list (line 579) is wrong: it should include [13] and drop [11]. The [12] entry is overstated.
- [21] has a wrong control condition ("2D interface") and a wrong resilience measure ("via HRV").
- [21] should probably carry a Physiological sensor flag, which would put Table VIII's Physiological count at 2 rather than 1.
- [20]'s "evaluation target" claim is unsupported, because it ran no human-subject tests.
- [19]'s adaptive swarm was tested only on replayed trajectories, which bears on Precedent G.
- [15]'s "genuinely hazardous" test site is a lab mock tunnel. [16] merges two test venues into one.
- [17]'s own validation is a lab-arena test with no live operator. Its Supervisory label and its possible field-test coding are borderline.
- 5 of 13 papers in this share do not self-report an environmental-realism limitation, which is hard to square with the corpus-wide 35/39.
