# Coding Manual: Autonomy/HRI Mode (Second-Coder Reliability Pass)

Use this manual to code the 39 included studies independently. The result lets the authors report a genuine human inter-rater agreement statistic for the review's four-way Autonomy/HRI taxonomy.

## 1. Blinding: read this first
- Code **only** from the full-text PDFs in `assets/papers/` (the filename is in `pdf_filename` in the sheet) and this manual.
- **Do not** open the manuscript, `SAR_review_master_document.md`, `data/extraction_table.csv`, `data/reliability_blind_codes.csv`, anything in `research_outputs/`, or `assets/docs/` until you have finished and saved your sheet. Do not discuss individual papers with the first coder either.
- The rows in `supplementary/human_second_coder_sheet.csv` are in shuffled order. Work in `sheet_order`. The `ref_N` column is only an identifier: in the manuscript the reference numbers are grouped by mode, so do not draw conclusions from them.
- Once a code is saved, do not change it after you see the original labels. Any later correction goes in a separate column, with a reason.

## 2. What to code
For each paper, fill in:

| Column | Values | Meaning |
|---|---|---|
| `mode` | T / S / C / F | Control paradigm in the paper's headline evaluation (Section 3) |
| `human_role_modelled` | Y / N | Does the evaluated setup include a human, real or simulated, acting during the mission? (A safety pilot who only aborts for safety counts as N; note it.) |
| `confidence` | high / medium / low | How clearly the paper supports your code |
| `page` | integer | PDF page holding the decisive evidence |
| `evidence_snippet` | ≤ 25 words | Short quote supporting the code |
| `notes` | free text | Alternative readings, mixed modes, uncertainty |

## 3. Decision rules (the only basis for coding)
Code the control paradigm **as executed in the paper's headline closed-loop evaluation**, whether simulated or physical. Ignore how pre-collected datasets were gathered, and ignore designs the authors recommend but did not test.

- **Teleoperation (T):** a human decides each individual motion or action in real time (joystick, RC transmitter, VR, or voice/GUI commands that each map to one atomic motion). Onboard stabilization, balance, compliance or obstacle-stop loops that only carry out the human's command do not change this.
- **Supervisory Control (S):** a human specifies goals, waypoints, regions or mission parameters and monitors, while the robot's own planner sequences the actions that achieve them. The human may switch the autonomy level or re-task the robot, but does not drive individual actions.
- **Shared-Collaborative Control (C):** decision authority is split *during* the mission. An autonomous decision layer (not a servo loop) has genuine authority over some task-relevant actions, while the human keeps real-time authority over others. Examples: a human pilots while an AI layer independently triggers a task action; the baseline is autonomous but one class of in-mission decision stays with the human; one human-teleoperated asset works alongside an autonomous team whose behaviour is driven by the human's state.
- **Fully Autonomous (F):** no human makes or approves decisions during the evaluated mission; at most, humans launch the system.
- **Tie-break:** decide by whether the human chooses each action or only the goal, in the headline experiment. Always pick exactly one label.

### Clarifications for recurring hard cases
These follow from the rules above. Record your reasoning in `notes` whenever one applies.
1. **Advisory AI (decision support) vs. C.** If the AI only recommends and the human still triggers every action, code T or S according to how the human controls motion. Code C only if the AI layer *acts* on its own authority for some task action.
2. **Goals set before the mission vs. during it.** If the experimenter sets a goal or region once and then only launches the robot, code F. If a human issues or changes goals while the mission runs (clicking waypoints, re-tasking, accepting or rejecting proposed solutions), code S.
3. **Safety pilot / optional override.** A safety pilot or an override that exists but is not part of the evaluated protocol does not make a paper S. Code F and add a note.
4. **Dual-mode systems (manual + autonomous).** Code the mode used in the headline evaluation. If the paper does not say which mode was used, choose the best-supported mode, set confidence to low and describe both readings in `notes`.
5. **Mixed evaluations** (for example, a planner-only simulation plus a field deployment with a human supervisor). Code the evaluation the paper presents as its main validation (abstract and conclusions), and note the other one.

## 4. Procedure
1. For each PDF, read the abstract, the system overview, and the experiments/results sections.
2. Find who decides actions and goals during the evaluated mission. Apply Section 3.
3. Fill in every column and save the sheet as `supplementary/human_second_coder_sheet_<initials>.csv`.
4. Send the file to the corresponding author. Only after that, compare it with the original labels.

## 5. Computing agreement afterwards
1. Copy your `mode` column into `data/reliability_blind_codes.csv` format (columns `ref_N`, `blind_mode`, `human_role_modelled`, `confidence`), or adapt `data/reliability_stats.py` so that its `load_blind()` reads your file.
2. Run `python data/reliability_stats.py` from the project root. It reports:
   - percent agreement;
   - Cohen's κ, with an analytic 95% CI (Fleiss–Cohen–Everitt large-sample SE) and a percentile bootstrap 95% CI (2,000 resamples, seed 1);
   - Gwet's AC1 (robust to the skewed marginals here: 27 of 39 papers are Fully Autonomous);
   - Scott's π, which equals Fleiss' κ when there are two raters;
   - the 4 × 4 confusion matrix;
   - the binary κ for Fully Autonomous vs. human-in-mission (T/S/C).
3. Interpretation (Landis & Koch 1977, as a convention only): 0.61–0.80 substantial, 0.81–1.00 almost perfect. Report κ and AC1 together, because κ is depressed by prevalence imbalance.
4. Resolve disagreements by discussion and record each one, with its resolution, in the revision log (master document Sec. 16). Report both the pre-discussion agreement and the final consensus labels in the paper.
5. If three or more coders take part, use Fleiss' κ across all of them, or Krippendorff's α (nominal).

## 6. Reporting
State plainly who coded, whether the coders were independent and blinded, and when the coding was done. Report any earlier AI-assisted check separately, labelled as a post-hoc AI-assisted check and not as inter-rater agreement.
