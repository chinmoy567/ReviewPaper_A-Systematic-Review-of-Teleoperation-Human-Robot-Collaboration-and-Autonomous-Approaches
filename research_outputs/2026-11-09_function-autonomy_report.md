# Per-function autonomy coding (Parasuraman, Sheridan & Wickens 2000) of the 39 included papers

**Date:** 2026-11-09 | **Coder:** one AI agent (Claude), post hoc, from full-text PDFs | **Data file:** `data/function_autonomy.csv`

> **Status: AI-assisted single coding, not human-verified.** Report it as an AI-assisted post-hoc coding exercise, never as independent human coding. Every code has a PDF page and a verbatim snippet of 20 words or fewer in the CSV `notes` column. A script matched all 195 snippets (39 papers x [4 stages + presence]) against the `pdftotext` output of the cited page, ignoring case and punctuation, and none failed. **Page numbers are physical PDF page indices** (page 1 is the first page of the PDF file), not journal pagination. For ref 46 (a journal pre-proof) the cover page counts as page 1.

## 1. Method

- Text was extracted with `pdftotext` from `assets/papers/` (paths from `data/id_map.csv`) into a private scratchpad folder. The first page of every PDF was checked against the expected title, and all 39 matched.
- **Stages:** acq = information acquisition (where sensors look and where the robot goes to gather information); ana = information analysis (detection, mapping, state estimation); dec = decision selection (goals, paths, task allocation, rescue actions); act = action implementation (executing motion or manipulation).
- **Codes:** H = human; S = shared (the human consents or vetoes, or the stage is split within the mission); M = machine. Each code describes the paper's **headline evaluated configuration**.
- **Coding conventions applied consistently:**
  - Continuous joystick or button driving counts as act = H, even when low-level stabilization is automatic. Discrete high-level commands that a controller executes (voice commands) count as act = S.
  - A goal given as part of the task (e.g. "reach a known target") with the path planned by the machine counts as dec = M. A route the experimenters fixed in advance, with no planning by the machine (refs 17 and 39), counts as dec = H.
  - Humans who steer vehicles only to collect data for offline evaluation (ref 30) are coded in the stage profile but give evaluated_human_presence = N.
  - A pilot's abort or return-to-launch veto over an autopilot (ref 18) does not make act = S.
- **designed_authority:** T, S, C or F, judged from how the paper describes its control paradigm. **evaluated_human_presence (EHP):** Y only if a real or simulated human makes or approves decisions, or controls the robot, during the evaluated mission. A human who only monitors counts as N (ref 38).
- `mode_clean` in `data/extraction_table.csv` was read **only after** all codes had been written.

## 2. Profile table (39 rows)

Profile = acq/ana/dec/act. Pages are in parentheses. Mode = existing `mode_clean` label.

| Ref | acq | ana | dec | act | Profile | Designed | EHP (p) | Mode (mode_clean) | Note |
|---|---|---|---|---|---|---|---|---|---|
| [10] | H (4) | S (3) | H (3) | S (3) | `HSHS` | T | Y (10) | Teleoperation | Machine does 3D reconstruction + face detection; operator interprets and picks locations. Discrete voice commands executed by robot controller (act=S). Person-follower sub-mode is machine-held acq/act. |
| [11] | H (11) | M (11) | H (10) | H (17) | `HMHH` | T | Y (17) | Teleoperation | Detection (YOLO) evaluated separately on images; mission motion is remote-piloted. Self-recovery posture is automatic (p18). |
| [12] | H (13) | H (13) | H (18) | H (13) | `HHHH` | T | Y (18) | Teleoperation | Low-level attitude (AMPC) and force-position control automated beneath joystick commands; no automated victim detection reported (ana=H by absence). |
| [13] | H (12) | M (11) | H (12) | H (12) | `HMHH` | T | N (11) | Teleoperation | Headline evaluation = offline YOLOv8 metrics on test images; live-feed demo does not describe a driver. Rescue team acts on cloud alerts (outside evaluation). |
| [14] | H (11) | M (1) | H (11) | H (11) | `HMHH` | T | N (23) | Teleoperation | Headline evaluation = MATLAB simulation of RescueNet detection (p18); teleoperated prototype not evaluated in a mission. Ultrasonic auto-stop is a safety interlock only. |
| [15] | S (9) | M (1) | S (3) | M (1) | `SMSM` | S | Y (9) | Supervisory Control | Operator sets target points in digital-twin UI; robot plans/avoids obstacles. EHP=Y inferred from UI design; field-test text (p20) does not state who set targets (moderate confidence). Rescuers use DT data for rescue decisions. |
| [16] | M (1) | M (1) | S (9) | M (21) | `MMSM` | S | Y (21) | Supervisory Control | DARPA SubT finals: autonomous exploration with human supervisor who could set goals/teleoperate occasionally (act mostly M). Semantic layer exists to make human goal-setting easier. |
| [17] | H (7) | M (1) | H (7) | M (7) | `HMHM` | S | N (7) | Supervisory Control | Designed for human supervisor/variable autonomy (p1) but evaluated without a human decision-maker; route pre-set by experimenters. High-radiation scenario used teleoperated positioning (p8) - borderline EHP. |
| [18] | M (1) | H (17) | S (2) | M (14) | `MHSM` | S | Y (14) | Supervisory Control | Rescuer-supplied priority map + algorithmic TSP path (dec=S). Autopilot executes; pilot holds abort/RTL veto. Imagery analysed by humans. |
| [19] | H (1) | H (7) | H (2) | H (1) | `HHHH` | C | Y (7) | Shared-Collaborative Control | Coded for the human-subject teleoperation experiment (headline). Adaptive swarm response to inferred human state evaluated only in simulation (machine-held for the other robots). |
| [20] | H (7) | M (4) | S (9) | H (9) | `HMSH` | C | N (25) | Shared-Collaborative Control | Agentic AI recommends, operator decides (designed dec=S). Headline evaluation = synthetic JSON scenarios with no human in the loop. |
| [21] | S (11) | S (11) | S (11) | M (11) | `SSSM` | S | Y (9) | Shared-Collaborative Control | MR human-swarm interface in simulator: operator allocates areas, confirms system remediation suggestions (p8, p11); swarm patrols autonomously. |
| [22] | M (1) | M (1) | M (1) | M (1) | `MMMM` | F | N (1) | Fully Autonomous |  |
| [23] | M (1) | M (1) | M (1) | M (1) | `MMMM` | F | N (1) | Fully Autonomous |  |
| [24] | M (1) | M (1) | M (1) | M (1) | `MMMM` | F | N (1) | Fully Autonomous |  |
| [25] | M (1) | M (1) | M (1) | M (1) | `MMMM` | F | N (1) | Fully Autonomous |  |
| [26] | M (1) | M (1) | M (1) | M (1) | `MMMM` | F | N (1) | Fully Autonomous |  |
| [27] | M (4) | M (4) | M (4) | M (4) | `MMMM` | F | N (14) | Fully Autonomous | Ground station is software, not a human decision-maker. |
| [28] | M (1) | M (1) | M (1) | M (1) | `MMMM` | F | N (1) | Fully Autonomous |  |
| [29] | M (1) | M (1) | M (1) | M (1) | `MMMM` | F | N (1) | Fully Autonomous | RoboCup Rescue Simulation agents only. |
| [30] | S (16) | M (1) | M (1) | S (16) | `SMMS` | F | N (1) | Fully Autonomous | Vehicles hand-steered in Gazebo only to collect mapping data (data-collection pilot -> EHP N); RL navigation stage is fully machine-held. |
| [31] | M (1) | M (1) | M (1) | M (1) | `MMMM` | F | N (1) | Fully Autonomous | Humans only file missing-person reports that trigger searches (p6). |
| [32] | M (1) | M (1) | M (1) | M (1) | `MMMM` | F | N (2) | Fully Autonomous | Framework outputs inform first responders on fleet size (p11) - pre-mission human decision, not in evaluated mission. |
| [33] | M (1) | M (1) | M (1) | M (1) | `MMMM` | F | N (1) | Fully Autonomous |  |
| [34] | M (1) | M (2) | M (1) | M (1) | `MMMM` | F | N (2) | Fully Autonomous | Target positions are given (known); machine plans and tracks. |
| [35] | M (1) | M (1) | M (1) | M (1) | `MMMM` | F | N (1) | Fully Autonomous |  |
| [36] | M (1) | M (3) | M (1) | M (1) | `MMMM` | F | N (1) | Fully Autonomous |  |
| [37] | M (2) | M (1) | M (8) | M (8) | `MMMM` | F | N (8) | Fully Autonomous | Start/end points set by experimenters; designed remote monitoring by operators (p3) not evaluated. |
| [38] | M (10) | M (1) | M (10) | M (1) | `MMMM` | F | N (11) | Fully Autonomous | Operator UI is monitoring/alerts only (no approval/control step reported) -> EHP N. |
| [39] | H (2) | M (1) | H (7) | M (7) | `HMHM` | F | N (7) | Fully Autonomous | Point-to-point: human pre-specifies the target (and thus the route); machine only estimates state and tracks bearing. No victim-detection function evaluated. |
| [40] | M (1) | M (1) | M (1) | M (1) | `MMMM` | F | N (1) | Fully Autonomous |  |
| [41] | M (6) | M (18) | M (6) | M (9) | `MMMM` | F | N (6) | Fully Autonomous | Operator input only at mission setup (Phase 1), then autonomous navigation (Phase 2). |
| [42] | M (1) | M (1) | M (1) | M (11) | `MMMM` | F | N (11) | Fully Autonomous | Person detection not addressed (p3); real-world images manually annotated for ground truth only (p9). Action implementation not evaluated online (offline evaluation). |
| [43] | M (3) | M (1) | M (15) | M (1) | `MMMM` | F | N (15) | Fully Autonomous |  |
| [44] | M (1) | M (8) | M (1) | M (1) | `MMMM` | F | N (8) | Fully Autonomous | Paper does not state whether real-world trajectories were flown by autopilot or a pilot (act=M is the designed mode; flag). |
| [45] | M (1) | M (1) | M (1) | M (6) | `MMMM` | F | N (6) | Fully Autonomous |  |
| [46] | M (2) | M (2) | M (2) | M (16) | `MMMM` | F | N (2) | Fully Autonomous |  |
| [47] | M (1) | M (1) | M (1) | M (1) | `MMMM` | C | N (5) | Fully Autonomous | Designed MUM-T: operator can intervene/adjust decisions (p4), but evaluation is offline MLLM detection and path-generation; UGV execution shown only in demo video (act weakly evidenced). |
| [48] | S (11) | M (9) | S (10) | S (10) | `SMSS` | C | Y (11) | Fully Autonomous | Traded control between Autonomous and Manual modes; both exercised in tests. |

The verbatim evidence snippets are in `data/function_autonomy.csv` (`notes` column, after `EVIDENCE:`).

## 3. Profile counts

| Profile (acq-ana-dec-act) | n | Refs |
|---|---|---|
| `MMMM` | 24 | [22], [23], [24], [25], [26], [27], [28], [29], [31], [32], [33], [34], [35], [36], [37], [38], [40], [41], [42], [43], [44], [45], [46], [47] |
| `HMHH` | 3 | [11], [13], [14] |
| `HHHH` | 2 | [12], [19] |
| `HMHM` | 2 | [17], [39] |
| `HSHS` | 1 | [10] |
| `SMSM` | 1 | [15] |
| `MMSM` | 1 | [16] |
| `MHSM` | 1 | [18] |
| `HMSH` | 1 | [20] |
| `SSSM` | 1 | [21] |
| `SMMS` | 1 | [30] |
| `SMSS` | 1 | [48] |
| **Total** | **39** | |

Stage-level totals across the corpus:

| Stage | H | S | M |
|---|---|---|---|
| Acquisition | 9 | 4 | 26 |
| Analysis | 3 | 2 | 34 |
| Decision | 8 | 6 | 25 |
| Action | 6 | 3 | 30 |

## 4. Cross-tab: profile by existing mode label (mode_clean)

| Profile | Teleoperation | Supervisory Control | Shared-Collaborative Control | Fully Autonomous | Total |
|---|---|---|---|---|---|
| `MMMM` | - | - | - | 24 | 24 |
| `HMHH` | 3 | - | - | - | 3 |
| `HHHH` | 1 | - | 1 | - | 2 |
| `HMHM` | - | 1 | - | 1 | 2 |
| `HSHS` | 1 | - | - | - | 1 |
| `SMSM` | - | 1 | - | - | 1 |
| `MMSM` | - | 1 | - | - | 1 |
| `MHSM` | - | 1 | - | - | 1 |
| `HMSH` | - | - | 1 | - | 1 |
| `SSSM` | - | - | 1 | - | 1 |
| `SMMS` | - | - | - | 1 | 1 |
| `SMSS` | - | - | - | 1 | 1 |
| **Total** | **5** | **4** | **3** | **27** | **39** |

Stage codes within each mode label (counts H/S/M):

| Mode label (n) | acq | ana | dec | act | EHP = Y |
|---|---|---|---|---|---|
| Teleoperation (5) | 5/0/0 | 1/1/3 | 5/0/0 | 4/1/0 | 3/5 |
| Supervisory Control (4) | 1/1/2 | 1/0/3 | 1/3/0 | 0/0/4 | 3/4 |
| Shared-Collaborative Control (3) | 2/1/0 | 1/1/1 | 1/2/0 | 2/0/1 | 2/3 |
| Fully Autonomous (27) | 1/2/24 | 0/0/27 | 1/1/25 | 0/2/25 | 1/27 |

Designed authority (this coding, rows) against mode_clean (columns):

| Designed | T | S | C | F |
|---|---|---|---|---|
| T | 5 | 0 | 0 | 0 |
| S | 0 | 4 | 1 | 0 |
| C | 0 | 0 | 2 | 2 |
| F | 0 | 0 | 0 | 25 |

Designed authority agrees with mode_clean in 36/39 papers. Disagreements: ref 21 (designed S vs label C), ref 47 (designed C vs label F), ref 48 (designed C vs label F). See Section 6.

## 5. Designed authority vs evaluated human presence

- 14 papers are designed for human involvement (T/S/C). Evaluated human presence = Y in 9 of them, and the human is absent from the evaluation in 5.
- Of the 25 papers designed as F, 0 have a human present in the evaluated mission.
- Over the whole corpus, a human makes, approves or executes decisions in the evaluated mission in **9/39** papers (23.1%): [10], [11], [12], [15], [16], [18], [19], [21], [48].

Mismatch cases (designed authority implies a human, but the evaluation has none):

| Ref | Designed | EHP | mode_clean | What was actually evaluated |
|---|---|---|---|---|
| [13] | T | N | Teleoperation | Offline YOLOv8 metrics on test images (p11); the robot "must be manually controlled" (p12), but no driven mission is evaluated. |
| [14] | T | N | Teleoperation | MATLAB simulation of the RescueNet detector (p18). "No physical field tests" (p23). The app-driven prototype is not evaluated in a mission. |
| [17] | S | N | Supervisory Control | Robot follows waypoints the experimenters set in advance (p7). The SA framework is aimed at a human supervisor, but no supervisor decides anything. Borderline: one scenario used teleoperated positioning (p8). |
| [20] | C | N | Shared-Collaborative Control | Decision support for an operator, evaluated only on synthetic JSON scenarios (p25). No operator receives or acts on the recommendations. |
| [47] | C | N | Fully Autonomous | MUM-T design in which the operator "can ... intervene or adjust decisions" (p4). The evaluation is offline MLLM detection and path generation (p5). |

Ref 48 is the reverse case. It is labelled FA but designed with a dual Autonomous/Manual mode, and an operator used Manual Mode during testing (EHP = Y, p11).

## 6. Observations

1. **The FA label holds at the function level, with three exceptions.** 24/27 FA-labelled studies are `MMMM` in their evaluated configuration. In **none** of the 27 does a human hold information analysis (ana = M in 27/27). In the evaluated configuration, decision selection is not machine-held in 2/27:
   - ref 39: a human sets the GPS target in advance and the robot only tracks its bearing to it (dec = H).
   - ref 48: dual-mode robot whose operator switches into Manual Mode (dec = S, EHP = Y).
   By design, 2/27 FA-labelled papers give the human a decision role: ref 47, where the operator can intervene in or adjust MLLM decisions, and ref 48. Ref 30's `SMMS` is an artefact of hand-steering in simulation to collect mapping data, not a design choice. **So by design 2/27 FA papers (7.4%) leave decision authority partly with a human, and 0/27 leave analysis to a human.** Suggest the authors re-examine refs 47 and 48 against the decision rules: both read more like Shared-Collaborative designs that were evaluated without, or partly without, a human. Per CLAUDE.md rule 3, this coding does **not** relabel them.
2. **Analysis is the most automated stage in every mode, and the Teleoperation label hides it.** Analysis is machine-held in 34/39 papers, and 3/5 Teleoperation papers (refs 11, 13, 14) pair human driving with automated victim detection (`HMHH`). Only refs 12 and 19 are pure `HHHH`. Analysis is human-held in just 3 papers: refs 12 and 19 (teleoperation) and, notably, the supervisory ref 18, where the UAV flies autonomously but humans must "manually search the imagery" (p17). The mode label is therefore mostly a statement about **acquisition, decision and action**, not about analysis.
3. **The four modes separate cleanly on the decision and action stages.**
   - Teleoperation: dec = H in 5/5 and act = H or S in 5/5.
   - Supervisory: act = M in 4/4, with dec = S or H in 4/4. This is the textbook Sheridan supervisory pattern of a human goal plus machine execution.
   - FA: dec = M and act = M in 24/27.
   - Shared-Collaborative is the least coherent label: its three papers have three different profiles (`HHHH`, `HMSH`, `SSSM`). Ref 21 looks closer to supervisory human-swarm control (operator allocates areas and confirms remediation, swarm patrols autonomously), and ref 19 is coded `HHHH` because its headline experiment is single-UAV teleoperation.
4. **Human-involving designs are often evaluated without the human.** Of 14 T/S/C designs, 5 (refs 13, 14, 17, 20, 47) were evaluated with no human deciding or controlling. Only 9/39 studies (23.1%) put a human decision-maker or operator into the evaluated mission at all, and only one FA-labelled study did (ref 48). This finding sits alongside the locked field-testing gap (FA field-tested 2/27): beyond rarely being field-tested, the human side of human-robot collaboration is also rarely tested.
5. **Where a human is in the loop, it is usually at decision level, not as a pilot.** Among the 9 EHP = Y studies, dec is H or S in 9, while act is M in 4 (ref 15, ref 16, ref 18, ref 21). This suggests that a per-function profile (e.g. `MMSM`) would describe supervisory and collaborative studies more informatively than a single mode label. It could be offered as a supplementary table or as a robustness check on the four-mode taxonomy.

## 7. Caveats and flags

- This is one AI coder's judgment. Before any number from it enters the manuscript, a human second coder should review it, at minimum on the 15 non-`MMMM` papers plus refs 44 and 47. The convention choices are a judgment call (e.g. joystick driving = H, voice commands = S, a predefined route = dec H), and they are written down in Section 1 so a second coder can apply them.
- Lower-confidence codes:
  - ref 15 EHP = Y: inferred from the target-setting user interface; the field-test section does not say who set the targets.
  - ref 17 EHP = N: one scenario used teleoperated positioning.
  - ref 44 act = M: the paper does not say whether the real-world trajectories were flown by autopilot or by a pilot.
  - ref 47 act = M: UGV execution appears only in a demonstration video.
  - ref 16 dec = S: the human supervisor's goal-setting role is described but not quantified.
- Nothing here changes a locked fact. The 27/5/4/3 mode split is untouched. The designed-authority disagreements (refs 21, 47, 48) are flagged for the authors, not applied.
- `SAR_review_master_document.md` was not opened or edited.
