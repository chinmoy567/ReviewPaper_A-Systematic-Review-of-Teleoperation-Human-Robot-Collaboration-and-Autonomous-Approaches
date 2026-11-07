---
name: q1-research
description: Master pipeline for taking the SAR robotics systematic review to Q1-journal standard. Runs novelty search, methodology audit, statistics check, citation verification, taxonomy grounding, simulated peer review, and journal targeting, then compiles one prioritized Q1-readiness report and fix plan. Use when the user asks to "make this Q1", "check if ready to submit", "run the full review", or "/q1-research".
---

# Q1 Research Pipeline

Goal: a manuscript that survives Q1 peer review. Q1 reviewers of systematic reviews judge, in order: **(1) is the contribution genuinely new, (2) is the method reproducible and rigorous, (3) are the claims proportionate to the evidence, (4) is it useful/insightful beyond description, (5) is it well written and correctly referenced.** The pipeline checks exactly these.

Read `.claude/CLAUDE.md` first. All outputs go to `research_outputs/` (create it if missing) with prefix `YYYY-MM-DD_`.

**Manuscript source:** `SAR_review_master_document.md` only. The manuscript is Secs. 9–14, the bibliography is Sec. 15 and the figures are in `assets/figures/`. `SAR_review_manuscript.tex` and `review_paper_v34_final.pdf` are retired, so no stage may read or edit them. Tell every agent this when spawning it.

## Stages

Run stages 1–5 in parallel (they are independent), then 6, then 7.

| # | Stage | Agent (`subagent_type`) | Skill it follows | Output |
|---|---|---|---|---|
| 1 | Novelty & competing work (web) | `literature-scout` | `novelty-gap-search` | `_literature-scout_novelty-scan.md` |
| 2 | PRISMA / method rigor | `methodology-auditor` | `prisma-audit` | `_methodology-auditor_prisma-audit.md` |
| 3 | Numbers & statistics | `stats-consistency-checker` | — | `_stats-checker_report.md` |
| 4 | References | `citation-verifier` | `citation-check` | `_citation-verifier_report.md` |
| 5 | Taxonomy theory & reliability | `taxonomy-theorist` | — | `_taxonomy-theorist_report.md` |
| 6 | Simulated Q1 peer review (reads 1–5) | `q1-reviewer` | `q1-peer-review` | `_q1-reviewer_report.md` |
| 7 | Venue (can run anytime) | `journal-scout` | `journal-targeting` | `_journal-scout_shortlist.md` |

When spawning, give each agent: the project path, today's date, its output filename, and "follow `.claude/agents/<name>.md` and the named skill".

## Stage 8 — Compile the readiness report (you, the main session)
Read all stage outputs and write `research_outputs/YYYY-MM-DD_Q1_readiness_report.md`:

1. **Verdict:** Ready / Needs minor work / Needs major work / Not yet viable — with the simulated reviewer's decision.
2. **Novelty status** per contribution (STANDS / HEDGE / THREATENED / PRE-EMPTED).
3. **Fix plan** — one table, de-duplicated across agents, ranked by (rejection risk × ease). Columns: #, issue, evidence/source agent, fix, effort (S/M/L), who (authors-only vs. Claude-can-do).
   - Mark items **only the authors can do** (re-run database searches, blind re-coding for κ, OSF registration, quality scoring of papers they hold) — never simulate those results.
4. **Drop-in text** for the top fixes Claude can do now (Markdown, ready to paste into the `.md`).
5. **Submission checklist** for the chosen venue.

Then show the user the verdict + top 10 fixes and ask which to apply. Apply edits to the `.md` with `academic-editor` (or directly), run the CLAUDE.md rule 7 consistency checks, and log every manuscript change in master doc Sec. 16.

## Q1 bar — the checklist the pipeline must clear
See `references/q1-standards.md`.
