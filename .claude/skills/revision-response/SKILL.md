---
name: revision-response
description: Turn real (or simulated) reviewer comments into a point-by-point response letter and tracked manuscript changes. Use when the user pastes reviewer/editor comments, receives a major/minor revision decision, or asks to respond to the q1-reviewer report.
---

# Revision & Response Letter

## Steps
1. Split the comments into atomic numbered items (R1.1, R1.2, R2.1 …). Keep the reviewer's wording verbatim in the letter.
2. Classify each: **Agree-fix** / **Partially agree** / **Respectfully disagree (with evidence)** / **Requires author-only work** (new search, re-coding, quality scoring).
3. For each, decide the manuscript change. Make edits in `SAR_review_manuscript.tex` (or via `academic-editor`), wrapping changed text in `\textcolor{blue}{...}` in a separate `_revised_marked.tex` copy if the journal wants highlighted changes (add `\usepackage{xcolor}`).
4. Write the letter: `research_outputs/YYYY-MM-DD_response_to_reviewers.md` (and `.tex` if requested):
   ```
   Comment R1.3: "<verbatim>"
   Response: We thank the reviewer… <what we did / why>.
   Change: Section II-C, p. X, lines Y–Z: "<new text>"
   ```
5. Tone: grateful, specific, never defensive; disagreements backed by citations or data.
6. Never claim work that was not done. Items needing author action get `[AUTHORS: complete — e.g. report κ = __]` placeholders and are listed at the top for the user.
7. Log all changes in master doc Sec. 16, recompile, rerun `stats-consistency-checker` if any number changed.
