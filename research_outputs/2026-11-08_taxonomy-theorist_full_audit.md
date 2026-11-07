# Taxonomy-theorist full audit: grounding, decision rules, boundary consistency, construct validity, reliability

Date: 2026-11-08. Mode: AUDIT ONLY. The manuscript was not edited.
Source read: `SAR_review_master_document.md` only (Secs. 3, 6A, 9–16) and `assets/figures/fig_taxonomy.png`. One corpus PDF (ID 119 = [18]) was opened to check a boundary case. The retired `.tex`/PDF were not opened.
Line numbers refer to `SAR_review_master_document.md` as of today.

---

## 0. Verdict in one paragraph

The four-mode taxonomy is the paper's main contribution (Abstract l.730, Contribution 1 l.694, Sec. IV-E l.605), yet **the manuscript cites no autonomy or HRI theory at all**. A search of the whole file for Sheridan, Parasuraman, Beer, ALFUS, J3016, Endsley, Fong, Murphy, "levels of automation/autonomy" and kappa/agreement returns zero hits in manuscript prose. The four modes are never defined in the manuscript text: the definitions appear only in the internal field spec (l.87) and in the Fig. 7 box labels. The seven decision rules (Sec. 6A) exist only in the working record. The manuscript asserts an "explicit, precedent-based classification protocol" five times but never reports it. No reliability statistic is reported. The Methods wording on independent three-author extraction conflicts with the audit trail (CLAUDE.md rule 4).

On theory, three problems stand out:
- (i) The Fig. 7 ordering puts Shared-Collaborative *above* Supervisory on the autonomy axis. Beer et al. (2014) order these the other way.
- (ii) Precedent F labels "human approves or rejects a system-proposed action" as Shared-Collaborative. In Sheridan–Verplank this is exactly the consent-based level of supervisory control.
- (iii) The "Fully Autonomous" label partly codes an *experimental condition* (no human modelled in a simulation) rather than a *system design*. This partly builds in the headline autonomy-to-validation finding.

There is also a factual problem in the Introduction. The paper's own prior-review comparator [6] *does* propose a Sheridan–Verplank-based autonomy axis (A1/A2/A3), and the manuscript does not mention it. A reviewer who knows [6] will catch this.

Severity count: 6 Major, 7 Moderate, 4 Minor.

---

## 1. Verified theory sources (web-checked 2026-11-08)

| Source | Status | What it contributes |
|---|---|---|
| Sheridan, T.B., & Verplank, W.L. (1978). *Human and Computer Control of Undersea Teleoperators*. MIT Man-Machine Systems Lab tech. report, NTIS ADA057655 (ONR contract N00014-77-C-0256). No DOI. | VERIFIED (NTRL catalogue record) | The original 10-level LOA scale. Level 5 = computer executes its suggestion if the human approves. Level 6 = the human has limited time to veto. Level 10 = the computer decides everything and ignores the human. The level wording is taken via its reproduction in Parasuraman et al. 2000, Table 1. The original report's full text was not opened. |
| Parasuraman, R., Sheridan, T.B., & Wickens, C.D. (2000). A model for types and levels of human interaction with automation. *IEEE Trans. SMC-A*, 30(3), 286–297. doi:10.1109/3468.844354 | VERIFIED (DOI and pages match across several records) | Four function stages: information acquisition, information analysis, decision/action selection, and action implementation. Each stage can be automated to a different level. This is the direct basis for a per-function profile. |
| Beer, J.M., Fisk, A.D., & Rogers, W.A. (2014). Toward a framework for levels of robot autonomy in human-robot interaction. *J. Human-Robot Interaction*, 3(2), 74–99. doi:10.5898/JHRI.3.2.Beer | VERIFIED (DOI). Level names and content PARTIALLY VERIFIED from search snippets of Table 4; exact numbers 1–10 UNVERIFIED (PMC page blocked by reCAPTCHA) | 10 LORA levels defined by who senses, plans and acts: Manual, Teleoperation, Assisted Teleoperation, Batch Processing, Decision Support, Shared Control (human initiative / robot initiative), Supervisory Control, Executive Control, Full Autonomy. The snippets confirm that Supervisory and Executive Control (robot senses, plans and acts while the human monitors or gives an abstract goal) sit *above* Shared Control. Whether Supervisory is level 8 and Executive level 9, or the reverse, is unconfirmed. Check Table 4 before printing level numbers. |
| Endsley, M.R., & Kaber, D.B. (1999). Level of automation effects on performance, situation awareness and workload in a dynamic control task. *Ergonomics*, 42(3), 462–492. doi:10.1080/001401399185595 | VERIFIED (PubMed). One aggregator misprints the DOI as "001400399…"; use the PubMed string. | A 10-level LOA scale that separates monitoring, generating, selecting and implementing. It includes "shared control" and "supervisory control" as distinct levels. |
| Huang, H.-M. (ed.). *Autonomy Levels for Unmanned Systems (ALFUS) Framework, Vol. I: Terminology*, NIST SP 1011-I-2.0 (2008). doi:10.6028/NIST.SP.1011-I-2.0. Earlier v1.1 is NIST SP 1011 (2004). | VERIFIED (NIST records). Version labels are inconsistent on NIST pages (2.0 vs 2.1). The PDF was not opened, so definitions are UNVERIFIED. | Contextual autonomy rated on three axes: human independence, mission complexity and environmental complexity. This is the standard reply to "autonomy is not one-dimensional". |
| Fong, T., Thorpe, C., & Baur, C. (2003). Robot, asker of questions. *Robotics and Autonomous Systems*, 42(3–4), 235–243. Also Fong, Thorpe & Baur, "Collaboration, dialogue, and human-robot interaction," ISRR 2001 (Springer STAR vol. 6, 2003). | VERIFIED (CMU/EPFL records). RAS DOI UNVERIFIED (not confirmed in this pass). | *Collaborative control*: robot and human as dialogue peers, where the robot can ask the human for help. This is the origin of Kareem et al.'s third mode and differs from *shared control* (continuous blending of human and robot inputs). |
| SAE J3016_202104, *Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles*. doi:10.4271/J3016_202104 | VERIFIED (SAE Mobilus) | Analogy only. Levels describe the *engaged feature in a given instance of operation*, not the vehicle. The 2021 revision treats "remote driving" as not automated driving. Both points support coding by the *tested* operating mode. |
| Murphy, R.R. (2004). Human–robot interaction in rescue robotics. *IEEE Trans. SMC-C*, 34(2), 138–153. doi:10.1109/TSMCC.2004.826267 | VERIFIED (DBLP) | The canonical SAR-specific HRI reference. Its absence is conspicuous in a SAR HRI review. |
| Bakzadeh et al. (2026) [6], *Front. Robot. AI* 13:1857704 | VERIFIED (full text fetched) | Table 7 "Axis A follows the Sheridan–Verplank scale": **A1 teleoperated = LOA 1–4; A2 semi-autonomous = LOA 5–7; A3 fully autonomous = LOA 8–10**. 12 of 15 platforms are A1. MINBOT-II is coded "A1/A3" (switchable). The paper also states that autonomy, mapping, SLAM, path planning and software architecture "are not reviewed", and that most mine rescue robots are teleoperated. |

---

## 2. Findings

### M1 (Major): The taxonomy has no theoretical grounding in the manuscript
- **Where:** l.313 (RQ1), l.375 (II-G), l.569–575 (IV intro and Fig. 7), l.605 (IV-E), l.676 (Intro), l.694 (Contribution 1), l.730 (Abstract), l.738 (Conclusion).
- **Quote (l.605):** "This four-way resolution, applied consistently across all 39 papers under a logged, precedent-based protocol … is this review's structural counterpart to the model reference paper's five-layer architecture [4]."
- **Problem:** No LOA or HRI framework is cited anywhere. The four modes are presented as self-evident. The only lineage given is Kareem et al.'s three HRI modes plus a fourth bucket. A Q1 HRI or human-factors reviewer will ask why these four bins, and how they relate to Sheridan–Verplank, Parasuraman, Beer, ALFUS or J3016. As the draft stands, the paper has no answer.
- **Fix:** Add a short subsection "IV-A Theoretical basis" (or II-G-1) that:
  - cites [Sheridan & Verplank 1978], [Parasuraman et al. 2000], [Beer et al. 2014], [Huang ALFUS], [Fong et al. 2003] and [Murphy 2004];
  - gives the mapping table in Sec. 3 below;
  - states that the four modes are *coarse bands* over the LOA continuum. This is the same move [6] makes with A1–A3.

  Add these sources to Sec. 15 and renumber per CLAUDE.md rule 7. Drop-in text is in Sec. 5.

### M2 (Major): The decision rules and mode definitions are reported only in the internal working record
- **Where:** definitions at l.87 (internal field spec) and in Fig. 7 box text only. Precedents A–G at l.152–173 (internal Sec. 6A). The manuscript refers to them at l.375, l.605, l.690, l.694, l.730 and l.738.
- **Quote (l.375):** "…were resolved against seven explicit classification precedents established and logged during extraction…"
- **Problem:**
  - The precedents are asserted but not reported, so a reader cannot reproduce any label.
  - The revision log (l.964) records that pointers to the precedent audit trail were *deliberately removed* from the manuscript as "working-doc scaffolding".
  - Apart from Fig. 7's one-liners and III-A's "no human in the control loop during the mission itself" (l.425), the manuscript never states the four definitions in prose.
  - "Explicit" and "logged" cannot be checked by a reader, which fails PRISMA 2020 item 10a/b (data items and the rules for them).
- **Fix:**
  - Put the four operational definitions in II-G.
  - Put the coding manual and decision tree (Sec. 4 below) in a Supplementary File S1, with a figure version.
  - Add a per-paper label table (ID, mode, precedent applied, one-line rationale) as Supplementary Table S2. Sec. 6A and the extraction Notes field (field 18) already hold the content.

### M3 (Major): The Fig. 7 ordinal axis contradicts the LOA literature and the paper's own Shared-Collaborative cases
- **Where:** `fig_taxonomy.png` (arrow labelled "Increasing autonomy", ordered Teleop, Supervisory, Shared-Collaborative, FA); l.575 "their position along the underlying autonomy spectrum"; l.521 "The more autonomous a reported system in this corpus, the less likely…"; l.521/535 "the full four-way autonomy spectrum"; l.623–627.
- **Problem:**
  - In Beer et al. (2014), Shared Control sits *below* Supervisory and Executive Control.
  - In Sheridan–Verplank, supervisory control spans the consent and veto levels (5–6) and up.
  - In [6]'s own A-bands, "shared authority" is A2 (LOA 5–7), below A3.
  - The paper's own Shared-Collaborative cases contain *more* direct human control than its Supervisory cases. [20] is RC-piloted (Precedent D, l.164). [19] has a directly teleoperated primary UAV (Precedent G, l.172).
  - So placing Shared-Collaborative third on an "increasing autonomy" arrow is not defensible. The inverse-relationship sentence also does not hold monotonically even on the paper's own ordering: field-test rates are Teleop 60%, Supervisory 75%, Shared-Collaborative 0%, FA 7.4%.
- **Fix:**
  - **Option A (preferred):** Redraw Fig. 7 as an ordered axis Teleoperation < Shared-Collaborative < Supervisory < FA. This matches Beer et al. and Sheridan–Verplank, and the field-test rates become 60 / 0 / 75 / 7.4.
  - **Option B:** Treat the four modes as *nominal* HRI structures, drop the arrow, and replace "the more autonomous…, the less likely…" with a contrast of "human-in-mission modes (Teleop + Supervisory + Shared-Collaborative, 6/12 = 50% field-tested) vs FA (2/27 = 7.4%)". The binary contrast is the defensible claim.

  Either way, do not call the four modes a monotone spectrum without the reordering. (Hand the binary contrast to stats-consistency-checker for a Fisher exact test and CIs.)

### M4 (Major): Precedent F conflicts with the definition of supervisory control
- **Where:** l.169–170 (Precedent F). Applied to [21] (ID 126), l.587.
- **Quote (l.170):** "distinguish 'human sets initial goal, then system executes autonomously' (Supervisory) from 'autonomous baseline runs, but a specific class of in-mission decision is dynamically retained by the human' (Shared-Collaborative)…"
- **Problem:**
  - In Sheridan's framework, the human approving or rejecting a system-proposed action during the mission (management by consent, LOA 5) is the core of supervisory control, not a separate mode.
  - Beer's Supervisory Control level likewise includes the human's override authority during the mission.
  - Precedent F thus redefines "supervisory" more narrowly than the field does ("set goal, then walk away"). That is closer to Beer's Executive Control.
  - As written, a reviewer could argue [21] belongs in Supervisory. That would change the counts to Supervisory 5 / Shared-Collaborative 2.
- **Fix:** Either reclassify (a labelling change: evidence plus a Sec. 16 entry; not done here per rule 3) or keep the label and justify it explicitly in II-G. A defensible justification: the human's authority covers a *specific function class* (fault recovery), allocated by design. That is function-level shared authority in the Parasuraman sense, not mission-level monitoring.

  Also define Shared-Collaborative so that it covers two subtypes:
  - **SC-a, function-partitioned authority:** Precedents D, F, G.
  - **SC-b, dialogue or peer collaboration:** Fong-style.

  State that no input-blending shared-control paper occurred in the corpus. The current one-line definition ("decision-making dynamically split", l.87) does not tell the reader any of this.

### M5 (Major): "Fully Autonomous" mixes system design with experimental condition
- **Where:** l.87 (definition "no human in the control loop during the mission"); l.425; l.521; l.591–601; Precedents B (l.155–156) and E (l.166–167); l.916 (ID 100).
- **Quote (l.425):** "27 of 39 papers (69.2%) present robotic SAR systems operating with no human in the control loop during the mission itself."
- **Problem:**
  - 16 of the 27 FA papers are simulation-only (Table XI). 10 of the 39 papers model no sensor at all (Table VIII).
  - In a simulation with no operator modelled, "no human in the loop" is a property of the *test bench*, not evidence of a *designed* fully autonomous system. Many such papers (MARL coverage, task allocation) never address the human role at all.
  - Conversely, Teleoperation and most Supervisory systems *cannot* be meaningfully evaluated without a human and usually a physical robot.
  - So part of the autonomy-to-validation association is structural, and partly circular: the way a paper was validated partly fixes its label.
  - Precedent E (code by what was tested) and Precedent B (code by designed closed-loop behaviour, *not* by the human-piloted real-world flight) also pull in opposite directions. E codes the test; B codes the design.
  - Two specific cases:
    - [42] (ID 17) is FA while its real-world phase was a human-piloted data-collection flight scored offline. Yet IV-D (l.597) says it "recovered 5 of 7 fully canopy-occluded targets in real forest trials", which reads as autonomous field performance.
    - [44] (ID 100): the source never names the real-world drone's flight-execution mechanism (l.916).
- **Quote (l.597):** "next-best-view camera planning that recovered 5 of 7 fully canopy-occluded targets in real forest trials ([42])".
- **Fix:**
  - (a) Split the definition. Code mode by the *architecture as evaluated in the headline experiment* (state this rule once; it subsumes B and E). Separately record a binary flag **Human-role-modelled (Y/N)**: was any operator role specified or evaluated?
  - (b) Rename the construct in the text to "Fully Autonomous (as tested)". Add one sentence in III-D acknowledging that operator-free simulation makes the FA label easier to reach, so the 7.4% figure partly reflects evaluation practice.
  - (c) Sensitivity analysis: recompute Table XI after (i) excluding FA papers with Human-role-modelled = N, and (ii) recoding [42] and [44] as "autonomy not field-exercised". Report whether the human-in-mission vs FA gap survives.
  - (d) Reword l.597 to say the real-forest data were collected on a human-piloted flight and scored offline.
  - (e) List the two FA "real-world field test" papers by citation in III-D, and confirm that autonomy was actually active in the field for both. The workbook was not readable in this audit, so their identity is UNVERIFIED here.

### M6 (Major): No classification reliability is reported, and the Methods wording conflicts with the audit trail
- **Where:** l.375, l.397 (Methods). l.643–644 (Limitations: no reliability item). Revision log l.936 and l.998.
- **Quote (l.375):** "Extraction was carried out independently by the three authors of this review, and the resulting field values were cross-checked against one another…"
- **Quote (l.998):** "'Single-annotator screening and extraction' and 'Partial reliance on AI-assisted record discovery' are both now false under the new framing … so both were deleted…"
- **Problems:**
  - (a) No κ, percent agreement or confusion matrix appears anywhere. The l.936 log shows the original Discussion listed "no inter-rater reliability statistic" as a limitation, and that bullet was then deleted.
  - (b) Sec. 2.2 (l.61) and the l.936 entry record single-annotator work at one point. The current wording states independent triple coding (CLAUDE.md rule 4).
  - (c) Internal inconsistency in the method itself. Precedents "established and logged during extraction" so that "later, structurally similar papers were classified consistently with earlier ones" (l.375), and IDs 53 and 126 were relabelled after a "deeper text-verification pass" (l.914). Both describe *sequential, precedent-driven* coding, which cannot also be three blind, independent codings.
  - (d) l.397 says "only findings on which all three agreed were retained" and then "disagreements were resolved through joint discussion". The first clause implies non-unanimous items were dropped. They were not; every paper has a label.
- **Fix:**
  - The authors must confirm what was actually done; this audit cannot. Do not strengthen the current claim.
  - Truthful option: "Autonomy/HRI mode was coded by [one author / the first author], with borderline cases referred to the co-authors and resolved against seven written precedents (Supplementary File S1). To estimate reliability, two co-authors blind-recoded [all 39 / a stratified 30% sample] after extraction; agreement is reported in Table S3."
  - Run the protocol in Sec. 6 below and restore a Limitations bullet on reliability.
  - Fix l.397 to "…compared, and disagreements were resolved by joint discussion until consensus."

### m1 (Moderate): The description of comparator [6] is incomplete and undercuts the novelty framing
- **Where:** l.676, l.686 (Table I), l.280–283 (internal 8C).
- **Quote (l.676):** "Bakzadeh et al. [6] … explicitly exclude autonomy and control software from their stated scope…" Table I gap cell: "Autonomy and control software explicitly excluded from scope".
- **Problem:** [6] does exclude autonomy *software* from review. But it also builds an explicit **autonomy-level axis grounded in Sheridan–Verplank (A1 = LOA 1–4, A2 = 5–7, A3 = 8–10)** and classifies all 15 platforms on it (12 are A1, and one is switchable A1/A3). It is therefore a prior SAR review that *does* classify by autonomy level, albeit for a narrow mine-only, platform-level corpus. The paper's claim that "None of these reviews organizes its corpus primarily around how much autonomy…" (l.676) survives only on the word "primarily".
- **Fix:**
  - Reword: "[6] excludes autonomy and navigation software from its review, but classifies its 15 mine rescue platforms on a three-band autonomy axis derived from Sheridan–Verplank (teleoperated / semi-autonomous / fully autonomous), finding most to be teleoperated."
  - Present this review's four modes as a refinement of the same Sheridan–Verplank banding: A2 is split into Shared-Collaborative and Supervisory. That is a strength, not a threat.
  - Update the Table I gap cell. Route the novelty sentences (l.676, l.696, l.730) to literature-scout for re-scan.

### m2 (Moderate): The text for Shared-Collaborative papers omits the facts that justify the label
- **Where:** l.587.
- **Quote:** "[20] uses an LLM-orchestrated multi-agent architecture to filter and prioritize what reaches the operator rather than presenting raw video…"; "[21] uses a mixed-reality swarm interface in a simulated maritime risk-conflict scenario…"
- **Problem:**
  - Read from the manuscript alone, [20] is a *decision-support / information-analysis* system (Beer "Decision Support", Parasuraman stage 2). The fact that makes it Shared-Collaborative (Precedent D: RC piloting plus an agent with independent authority to trigger payload deployment, l.164) is missing.
  - Likewise, [21]'s Shared-Collaborative basis (the human's mid-mission approve/reject authority over fault recovery, Precedent F) is missing.
  - The IV-C intro also claims the distinguishing feature is treating "the operator's cognitive or psychological state as a first-class design target". That is a thematic observation, not the classification criterion.
- **Fix:** Add one clause per paper stating who holds which decision:
  - [20]: "the airframe is pilot-flown, while the agentic layer can independently trigger payload release";
  - [19]: "the operator teleoperates the lead UAV while the swarm's coverage behaviour adapts to inferred operator state";
  - [21]: "UAVs search autonomously, but the operator approves or rejects fault-recovery countermeasures mid-mission".

### m3 (Moderate): [21]'s scenario is described as "maritime", contradicting Table XII and the logged correction
- **Where:** l.587 vs l.224 and l.978.
- **Problem:** ID 126 (= [21]) was reclassified from Maritime/Water to Wilderness/Mountain/Forest ("climbers trapped in a valley by a flash flood"). IV-C still says "simulated maritime risk-conflict scenario". Table XII's single Maritime/Water paper is therefore not [21].
- **Fix:** Change to "a simulated mountain-valley flash-flood rescue scenario" (verify the wording against the PDF `assets/papers/Q1 126 …pdf`). Log in Sec. 16.

### m4 (Moderate): The Supervisory/FA boundary has no written rule, and [18] is a test case
- **Where:** l.583 ([18]); FA single-robot and multi-robot coverage planners at l.593–595.
- **Problem:**
  - [18] (Schomer & Adams; PDF checked) is an autonomous UAV coverage path planner. The human role is to supply the search-probability map and area before flight; the field experiments evaluate the planner.
  - Many FA coverage and task-allocation papers ([23], [24], [28], [35], [31]) also start from a human- or scenario-assigned area.
  - Precedent A's heuristic ("human specifies a goal/waypoint/region … robot sequences actions" means Supervisory) would make *all* of them Supervisory. Yet only [18] is.
  - None of A–G covers "human input only at mission initialisation". The label for [18] may be defensible: MSAR teams supply the probability map as an operational input, and the paper frames the tool for rescuer use. But the rule is unwritten.
- **Fix:**
  - Add a written rule, **Precedent H**: "Supervisory requires that the paper specifies or evaluates a human goal-setting, monitoring, or re-tasking role *during or between mission phases*. A system whose only human input is a pre-mission area or parameter set, with no operator role in the evaluated pipeline, is FA."
  - Re-check [18], [16] and [15] against it, and log the outcome either way.

### m5 (Moderate): Mode switching and adjustable autonomy are hidden by the single-label rule
- **Where:** l.87 ("Always resolve to one firm primary label"); l.153 ([10]'s autonomous person-follower sub-mode); l.583 ([17] studies operators "switching autonomy level"); l.579 "in every one of the five papers, locomotion remains entirely human-driven".
- **Problem:**
  - A reviewer will ask "systems switch modes; what about variable autonomy?" [17] is explicitly a variable-autonomy study, and [10] has a secondary autonomous mode, yet the manuscript never says how many papers are multi-mode.
  - l.579's "entirely human-driven" overstates the case for [10], which has an autonomous follower sub-mode, and for [12], whose onboard controllers keep it balanced and tracking (Precedent C).
- **Fix:**
  - Using the Notes field, count papers with a secondary or switchable mode and report it, for example "k of 39 papers offer a secondary mode; Table S2 lists it". Note that J3016 likewise rates the *engaged feature in a given instance*, which is the analogue of the "primary tested mode" rule.
  - Soften l.579 to "locomotion decisions remain human-driven in the tested configuration".

### m6 (Moderate): The interpretation of [4]'s three-mode account goes beyond its data
- **Where:** l.436, l.627.
- **Quote (l.436):** "…a departure from the predominantly human-supervised framings surveyed by the model reference paper's own three-mode HRI account [4]."
- **Problem:** Sec. 8A (l.262) records that [4] reports *no* distribution across its modes. A "departure" from it cannot be measured, and the comparison is across different category schemes.
- **Fix:** "…whereas [4] discusses HRI only through three human-involved modes and reports no per-paper distribution, so the two corpora cannot be compared directly on this axis."

### m7 (Moderate): The size of the categories limits the inferential weight of the taxonomy
- **Where:** l.521, l.696, l.730.
- **Problem:** Supervisory n = 4 and Shared-Collaborative n = 3. "60–75%" is 3/5 and 3/4, and no CIs or tests are given. Reviewers will treat the four-way comparison as descriptive only.
- **Fix:** Report the binary human-in-mission vs FA contrast with an exact test and Wilson CIs, and call the four-way rates descriptive (refer to stats-consistency-checker).

### n1 (Minor): Wrong cross-reference
- **Where:** l.605 "(Section II-F)".
- **Problem:** The precedent-based protocol is described in II-G (Data Extraction), not II-F (Screening).
- **Fix:** Change to "Section II-G".

### n2 (Minor): The Fig. 7 end-labels misuse loop terminology
- **Where:** Fig. 7 ("Human-in-the-loop" … "No human in the loop").
- **Problem:** Supervisory control is conventionally described as human-*on*-the-loop.
- **Fix:** Use the labels "human in the loop / on the loop / out of the loop", or drop them.

### n3 (Minor): The Fig. 7 Teleoperation definition is too literal
- **Where:** Fig. 7 Teleoperation box ("Human directly drives every robot action").
- **Problem:** Precedent C keeps onboard stabilisation inside Teleoperation, so "every action" is literally false for [12].
- **Fix:** "Human selects every motion command; onboard control only stabilises or executes it" (equivalent to Beer Teleoperation / Assisted Teleoperation).

### n4 (Minor): The unverified novelty phrase is outside the scope of this audit
- **Where:** Abstract l.730 "which has not been reported previously in this literature".
- **Problem:** Under CLAUDE.md rule 2 this requires a dated novelty scan in `research_outputs/`.
- **Fix:** Confirm such a scan exists. With m1 in view, the safer claim is "not reported in the prior SAR robotics reviews compared in Table I".

---

## 3. Mapping table (proposed for Sec. IV / Supplementary S1)

Sheridan–Verplank (S–V) levels follow Parasuraman et al. (2000), Table 1. Beer level names are partially verified; check exact numbers against Beer 2014, Table 4 before printing them. P-stages: 1 = information acquisition, 2 = information analysis, 3 = decision/action selection, 4 = action implementation.

| This review | S–V LOA (approx.) | Who holds stage 3 (decide) / stage 4 (act) | Beer et al. LORA | [6] A-band | Corpus n | Precedents |
|---|---|---|---|---|---|---|
| Teleoperation | 1–2 (onboard reflexes allowed) | Human / human (robot may stabilise or execute) | Teleoperation; Assisted Teleoperation | A1 (LOA 1–4) | 5 | A, C |
| Shared-Collaborative | 3–5, function-partitioned | Split *by function*: human retains some stage-3 decisions, robot or agent owns others with real authority | Decision Support; Shared Control (human or robot initiative) | A2 (5–7) | 3 | D, F, G |
| Supervisory | 5–7 at mission level | Robot (with human goal-setting, consent or veto, re-tasking) / robot | Batch Processing (lower end); Supervisory Control | A2–A3 boundary (6–8) | 4 | A (goal-level), H (proposed) |
| Fully Autonomous (as tested) | 8–10 | Robot / robot; no human role in the evaluated pipeline | Executive Control; Full Autonomy | A3 (8–10) | 27 | B, E, H |

Note on order: this table uses the theory-consistent order (Shared-Collaborative below Supervisory). Under the current Precedent F, [21] sits at the S–V 5 (consent) boundary. See M4.

**Operational decision rules (apply in order; first "yes" wins):**
1. **R1:** Does the evaluated pipeline contain *any* human role during or between mission phases (goal-setting, monitoring with override, approval, piloting)? If no, the paper is **FA (as tested)**. Record the Human-role-modelled flag. (Covers Precedents B, E and H.)
2. **R2:** Does a human select each motion or action command (any interface modality), with onboard control only stabilising or executing it? If yes, and no independent machine decision layer has authority over task-relevant actions, the paper is **Teleoperation**. (Precedents A, C.)
3. **R3:** Is authority over task-relevant *decisions* partitioned by function or by asset, so that a machine layer independently decides some actions while a human pilots or decides others? If yes, the paper is **Shared-Collaborative**. (Precedents D, G; F as currently written.)
4. **R4:** Otherwise (the robot senses, plans and acts, and the human sets goals, monitors, re-tasks or vetoes), the paper is **Supervisory**.
5. **R5 (tie-break):** When the paper's design philosophy and its tested pipeline differ, code the tested pipeline and record the design in Notes (Precedent E). For data collected under one mode and scored offline under another, code the mode of the closed-loop headline experiment and set the flag "autonomy not field-exercised" (Precedent B).

---

## 4. Coding manual / decision tree (Supplementary S1 and figure)

```
START: identify the headline (quantitatively reported) experiment
 |
 Q1 Is any human role present in the evaluated pipeline during/between mission phases?
 |-- NO  -> FULLY AUTONOMOUS (as tested)         [B, E, H]
 |          flag: human-role-modelled? Y/N ; autonomy field-exercised? Y/N
 |-- YES
     Q2 Does the human choose every motion/action command (voice/GUI/joystick alike)?
     |-- YES -> Q2a Is there a separate machine decision layer with authority over
     |           a task-relevant action (not a servo/stabiliser loop)?
     |           |-- NO  -> TELEOPERATION                 [A, C]
     |           |-- YES -> SHARED-COLLABORATIVE          [D, G]
     |-- NO
         Q3 Is a specific class of in-mission decision retained by the human while
            the machine decides the rest (function- or asset-partitioned authority)?
         |-- YES -> SHARED-COLLABORATIVE                  [F]  (see M4)
         |-- NO  -> SUPERVISORY CONTROL (goal-level tasking, monitoring, override)  [A]
 Record: primary label, secondary/switchable mode (if any), precedent used, 1-line rationale.
```

Worked anchors (one per precedent; cite in S1): A = [10]; B = [42]; C = [12]; D = [20]; E = [47]; F = [21]; G = [19]; proposed H = [18].

---

## 5. Drop-in Markdown for the manuscript (for the authors to adapt; not inserted)

**For II-G (after the first sentence):**

> The four modes are coarse bands over the levels-of-automation continuum introduced by Sheridan and Verplank [S–V] and extended to information-processing stages by Parasuraman et al. [PSW] and to human-robot interaction by Beer et al. [Beer]. Bakzadeh et al. [6] used the same banding approach for mine rescue platforms. *Teleoperation* covers systems in which the human selects every motion or action command and onboard control only stabilises or executes it. *Shared-Collaborative Control* covers systems in which authority over task-relevant decisions is split by function or by asset between the human and an independent machine decision layer. *Supervisory Control* covers systems in which the robot senses, plans and acts while the human sets goals, monitors, re-tasks or vetoes. *Fully Autonomous* covers systems whose evaluated pipeline contains no human role during the mission. Each paper was coded by the mode of its headline experiment rather than its stated design philosophy, and a separate flag recorded whether any operator role was modelled at all. The full decision rules, seven worked precedents and per-paper rationales are given in Supplementary File S1 and Table S2.

**For the start of Sec. IV:**

> Fig. 7 orders the four modes by how much decision authority is held by the robot: Teleoperation, Shared-Collaborative, Supervisory, Fully Autonomous, consistent with [Beer] and [6]. Because the modes are bands rather than points, a paper can sit near a boundary, and a system can expose more than one mode. We therefore report the mode exercised in each paper's headline experiment and list secondary modes in Table S2.

(Placeholders [S–V], [PSW] and [Beer] must become numbered references in Sec. 15 with renumbering per rule 7.)

---

## 6. Reliability study the authors can still run

1. **Codebook freeze:** Sec. 3 rules plus Sec. 4 tree plus anchors, written up as S1 *before* re-coding.
2. **Sample:** all 39 papers (feasible), or at least a 30% stratified sample (12 papers: all 3 Shared-Collaborative, all 4 Supervisory, 2 Teleoperation, and 3 FA including [42] and [44]). Oversampling the boundary cases is deliberate.
3. **Blinding:** each of the three authors codes independently from full texts in `assets/papers/`, without access to columns G/S or Notes. Order is randomised and the precedent anchors are excluded from the scored set (or scored separately).
4. **Statistics:**
   - Fleiss' κ (3 raters × 4 categories) with a bootstrap 95% CI.
   - Because FA prevalence is 69%, κ will be deflated (the prevalence paradox), so also report Gwet's AC1 and raw percent agreement.
   - Report pairwise Cohen's κ and per-category agreement.
   - If the reordered ordinal axis (M3, Option A) is adopted, report Krippendorff's α (ordinal).
   - Report κ for the binary human-in-mission vs FA contrast separately. It carries the headline finding.
5. **Confusion matrix:** each rater vs the published consensus label (4×4), plus a 2×2 for the binary contrast.
6. **Reporting:**
   - State honestly that this was a **post-hoc reliability check** run after the original extraction, not part of the original process (CLAUDE.md rule 4).
   - Put κ, AC1 and the CIs in II-G with Table S3. Give the number of labels that would change, and say whether any change alters Table XI.
   - Benchmarks: κ ≥ 0.61 substantial; ≥ 0.81 almost perfect (Landis & Koch 1977, *Biometrics* 33:159–174; DOI not verified in this pass).
7. **Sensitivity:** recompute Table XI under each rater's labels and under the M5 exclusions.

---

## 7. Theoretical extension that the existing data supports

**A second axis, "autonomy as tested vs autonomy as claimed or designed".** The extraction already contains the inputs: field 7 (tested mode), field 18 Notes (stated design, as in Precedent E for [47] and B for [42]), field 8 (interface: "N/A" when no operator interface is described) and field 14 (validation). Code the axis per paper as follows:
- **Claimed mode:** from the abstract and discussion.
- **Tested mode:** the current label.
- **Human-role-modelled:** Y/N.
- **Autonomy field-exercised:** Y/N.

The Sec. III-D finding can then be restated without circularity as a 2×2 of tested autonomy × field exercise. [47] and [20] become instances of the claimed > tested gap, with no new extraction required. A per-function Parasuraman profile (perception / navigation / decision) is attractive, but Discussion item 2 (l.651) shows the corpus rarely reports these separately, so it is **not** recommended without new extraction.

---

## Sources
- [Parasuraman et al. 2000 (DOI record)](https://bibbase.org/network/publication/parasuraman-sheridan-wickens-amodelfortypesandlevelsofhumaninteractionwithautomation-2000)
- [Beer et al. 2014, PMC author manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC5656240) and [Table 4](https://pmc.ncbi.nlm.nih.gov/articles/PMC5656240/table/T4)
- [Endsley & Kaber 1999, PubMed](https://pubmed.ncbi.nlm.nih.gov/10048306/)
- [NIST SP 1011-I-2.0 ALFUS](https://www.nist.gov/document/nistsp1011-i-2-0pdf)
- [Fong et al., Robot, asker of questions (CMU)](https://www.ri.cmu.edu/?p=16867); [Collaboration, dialogue, and HRI (CMU)](https://www.ri.cmu.edu/publications/collaboration-dialogue-and-human-robot-interaction)
- [SAE J3016_202104](https://saemobilus.sae.org/content/j3016_202104)
- [Murphy 2004, DBLP](https://dblp.uni-trier.de/rec/bibtex/journals/tsmc/Murphy04)
- [Sheridan & Verplank 1978, NTRL](https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/ADA057655.xhtml)
- [Bakzadeh et al. 2026 [6], Frontiers full text](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1857704/full)
