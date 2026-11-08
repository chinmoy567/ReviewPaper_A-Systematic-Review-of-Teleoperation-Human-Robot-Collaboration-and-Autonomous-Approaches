# POST-HOC AI-ASSISTED RELIABILITY CHECK — NOT HUMAN INTER-RATER AGREEMENT

**Agent:** reliability-coder (Claude, AI) · **Date:** 2026-11-08 · **Scope:** Autonomy/HRI mode of the 39 included studies.

An AI model coded all 39 papers a second time, blind to the original labels, using only the written decision rules in `.claude/agents/reliability-coder.md`. **No human coded anything in this check.** The statistics below measure agreement between the original labels and one AI coder. They are **not** human inter-rater agreement and must not be reported as such, for example in the Methods section as "two reviewers independently coded…".

## 1. Files produced
| File | Content |
|---|---|
| `data/reliability_blind_codes.csv` | Blind codes for 39 papers: mode, human_role_modelled, confidence, PDF page and an evidence snippet of 25 words or fewer. Saved before Phase 2 (sha256 `e77d8903ea784ecda852f22497a9d19cbf3442b6372c81298033a4923fa876be`, 2026-11-08T07:16+06:00) and not changed afterwards. |
| `data/reliability_stats.py` | Reproducible statistics. Run `python data/reliability_stats.py` from the project root. |
| `supplementary/human_second_coder_sheet.csv` | Blank sheet for a human coder, rows shuffled (seed 1), with no original labels. |
| `supplementary/coding_manual.md` | Decision rules written for a human coder, hard-case clarifications, and the procedure for computing κ. |

## 2. Protocol actually followed
- **Phase 1 (blind):** the only inputs were the agent file, `data/id_map.csv` and the 39 PDFs (extracted with `pdftotext -layout` and split by page). I did not open the master document, `data/extraction_table.csv`, `research_outputs/` or `assets/docs/` before the codes were saved.
- **Phase 2:** the original labels came from master doc Sec. IV-A to IV-D: Teleop [10]–[14], Supervisory [15]–[18], Shared [19]–[21], FA [22]–[48]. These match the Table VII/XI totals of 5/4/3/27.
- **Blinding limitations (disclose these):**
  1. In `id_map.csv`, `ref_N` runs contiguously and the manuscript's reference numbers are grouped by mode. I noticed during coding that the grouping might carry information. Every code rests on PDF evidence, but the blinding is imperfect. The human sheet is shuffled to reduce this cue, although `ref_N` is still visible there.
  2. The decision rules were written after the original labelling, possibly with the original labels in view. That can raise agreement.
  3. I read only text extracted from the PDFs, not figures or videos.
  4. **Process incident:** the session scratchpad is shared with another agent running at the same time, which writes text files named by `record_id`. One of my files (ref 21) was overwritten with record 21's text, a different paper. I caught this before saving any code, re-extracted all 39 PDFs into an isolated folder and confirmed that each file's title matches `id_map`. The papers I had read before the collision (refs 10–20) had already been checked against their titles.

## 3. Statistics (N = 39)
| Measure | 4-category mode | Binary FA vs human-in-mission |
|---|---|---|
| Percent agreement | **89.7% (35/39)** | 94.9% (37/39) |
| Cohen's κ | **0.789** | 0.880 |
| 95% CI, analytic (Fleiss–Cohen–Everitt SE) | 0.606–0.972 | 0.717–1.000 |
| 95% CI, bootstrap (2000 reps, seed 1, percentile) | 0.575–0.950 | 0.687–1.000 |
| Gwet's AC1 (bootstrap 95% CI) | 0.878 (0.753–0.971) | 0.911 (0.773–1.000) |
| Scott's π (= two-rater Fleiss' κ) | 0.788 | 0.880 |

Chance agreement for the 4-category κ is p_e = 0.514, inflated by the 27/39 FA prevalence. That is why AC1 is higher than κ. Agreement by blind confidence was 27/27 (high), 6/9 (medium) and 2/3 (low), so every disagreement fell in a case I had already marked uncertain. The blind `human_role_modelled = Y` flag matched the original non-FA membership in 37/39 papers (κ 0.880).

### Confusion matrix (rows = original, columns = blind AI)
|  | T | S | C | F | total |
|---|---|---|---|---|---|
| **T** | 5 | 0 | 0 | 0 | 5 |
| **S** | 0 | 3 | 0 | 1 | 4 |
| **C** | 1 | 1 | 1 | 0 | 3 |
| **F** | 0 | 1 | 0 | 26 | 27 |
| total | 6 | 5 | 1 | 27 | 39 |

Shared-Collaborative is the weak category: only 1 of 3 papers was reproduced (only [19]).

## 4. Disagreement analysis
| Ref | Original | Blind | Evidence (PDF) | Which rule each label follows | Rule ambiguity? |
|---|---|---|---|---|---|
| [18] terrain-aware UAV search planner | S | F (medium) | p12: field experiments flew CPP paths planned in situ; p6: MSAR personnel *may* place viewpoints **before** the search; p14: a safety pilot terminated the autopilot / commanded RTL when line-of-sight was lost | The S label rests on "human specifies regions/mission parameters" (rescuers' probability map, search area). The F label rests on "no human decides during the mission; humans at most launch", treating parameters set before the mission as part of the launch. | **Yes.** The rules do not say whether goals or parameters set *before* the mission count as supervision. Clarification 2 of the coding manual resolves this. Note that Sec. IV-B's own description of [18] cites no in-mission human role. |
| [20] LLM cognitive-agentic rescue drone | C | T (medium) | p7: "the drone is controlled via a radio controller and receiver"; p9: the operator controls the payload release remotely, based on recommendations from the cognitive architecture | The C label treats the LLM layer's filtering, prioritisation and self-correction as autonomous authority over a task action. The T label treats the LLM as **advisory** only: the human flies, and the human triggers the one physical task action (release). | **Yes.** It is unclear whether autonomous information filtering counts as authority over a "task-relevant action". Clarification 1 makes advisory-only AI T or S. The authors should check whether any action in [20] is executed without a human trigger. |
| [21] MR human-swarm interface | C | S (medium) | p12: the system proposes solutions and "the operator decides whether to implement the solution, replace the faulty UAV"; p17: experienced operators preferred manual control supported by system suggestions | The C label fits "autonomous baseline but a specific class of in-mission decision retained by the human" (fault response). The S label fits "human monitors, may re-task; does not drive individual actions". | **Yes, a genuine overlap between the rules.** The S rule's "re-task" and the C rule's "class of decision retained by the human" both describe accepting or rejecting proposed swarm actions. The authors need a sharper boundary, for example: C only when human and machine each hold *concurrent real-time* authority over different action classes. |
| [48] dual-mode hexapod | F | S (low) | p10: "two distinct modes: Autonomous Mode and Manual Mode"; p9: operators can take over; p12–13: dashboard with direction controls. The PDF does not state which mode was used in the reported tests. | The F label follows the autonomous mode as headline. The S label follows "human may switch autonomy level". | **Yes.** Dual-mode systems whose evaluation mode is not reported. Clarification 4: code the mode actually evaluated, otherwise use low confidence. The original F is defensible if the authors confirm that the tests ran in Autonomous Mode. |

Other uncertain cases where we agreed: [16] (an F reading is possible from the planner-only simulation; I chose S because of the SubT supervisor interventions on p21), [17] (S at low confidence: waypoints set before the mission plus one teleoperated positioning, p7–8), and [47] (F at low confidence: the human oversight the paper describes was not tested, matching Sec. IV-D's own caveat).

## 5. Implications for the manuscript
1. **Headline robustness.** The blind labels give FA = 27, the same total, because [18] moves in and [48] moves out. The FA share of 69.2% is therefore unchanged. However, Shared-Collaborative would fall to 1, and the field-test cross-tab may shift: [18] reports real field experiments (p12), and Table XI gives Supervisory 3 field tests. If [18] were FA, FA field-tested could rise from 2/27 to 3/27 (11.1%), depending on [48]'s validation code. I have **not** recomputed this. It needs a sensitivity run by `stats-consistency-checker` against `data/extraction_table.csv`.
2. **Possible factual error (verify):** Sec. IV-C says [21] uses "a simulated maritime risk-conflict scenario". The PDF (p8) says "The experimental scenario was set in a mountainous wilderness area where a flash fl[ood]…", and "maritime" does not appear in the extracted text. This is a likely error that should be corrected after the authors check it.
3. **Methods wording.** Under CLAUDE.md rule 4, this check must not be presented as independent dual coding. If the authors want to mention it, suggested truthful Markdown wording is: *"As a post-hoc, AI-assisted consistency check, a large language model re-coded the Autonomy/HRI mode of all 39 studies blind to the original labels, using written decision rules (Supplementary coding manual); agreement with the original coding was 89.7% (Cohen's κ = 0.79, 95% CI 0.58–0.95; Gwet's AC1 = 0.88). This check does not substitute for human inter-rater reliability [see Sec. X for the human second-coder results]."* The journal's AI-use disclosure statement must also cover this check.

## 6. Recommendation
**Have an independent human second-coder pass done before submission.** A co-author who did not assign the original labels, or an external coder, should fill in `supplementary/human_second_coder_sheet.csv` blind, following `supplementary/coding_manual.md`. Then compute κ, AC1 and the confusion matrix with `data/reliability_stats.py`, resolve disagreements by discussion, and log each resolution in master doc Sec. 16. Settle the C-vs-S boundary first ([20], [21]), because the Shared-Collaborative category (n = 3) is the least reproducible part of the taxonomy and would draw a Q1 reviewer's attention.
