---
name: novelty-gap-search
description: Web-search protocol for answering "has this already been done?" for the SAR robotics review — finds competing reviews, taxonomies, and primary studies, verifies them at source, and rates each claimed contribution as STANDS / HEDGE / THREATENED / PRE-EMPTED. Use before writing any novelty claim, before submission, or when the user asks what existing work has been done or what is missing.
---

# Novelty & Gap Search

## 1. Define what you are testing
List the manuscript's claimed contributions as falsifiable statements, e.g.:
- C1 "No SAR review uses a four-way autonomy/HRI taxonomy as its primary organizing axis with per-paper labels."
- C2 "No SAR review quantifies real-world validation rate by autonomy level."
- C3 "No review reports the UAV platform–validation mismatch."
- C4 "This is the first review covering 2025–2026 after Kareem et al. 2026."

## 2. Search matrix (run all; log each query)
Combine one term from each column; use `mode: "extended"` for the C1/C2 queries.

| Domain | Topic | Type |
|---|---|---|
| search and rescue / USAR / disaster response / emergency response / mine rescue / maritime SAR / wildfire | autonomy levels / levels of automation / shared autonomy / supervisory control / teleoperation / human-robot teaming / sim-to-real / field validation / benchmark | systematic review / survey / scoping review / bibliometric / taxonomy |
| UAV / drone / UGV / legged / multi-robot / swarm | LLM / embodied AI / foundation models | 2025 / 2026 / arXiv |

Minimum: 12 queries. Also search specific venues: Frontiers in Robotics and AI, Drones, Sensors, IEEE Access, Robotics and Autonomous Systems, Journal of Field Robotics, Artificial Intelligence Review, IJDRR, arXiv cs.RO.
Also do **citation chasing**: who cites Kareem et al. 2026 (DOI 10.1109/ACCESS.2026.3660002)? Search the DOI and title.

## 3. Verify at source
For each plausible competitor, open the page (WebFetch or the `web-fetch` agent). Record: full citation, DOI, date, review type (PRISMA?), databases, years covered, N papers, organizing axis, codes autonomy? (how), reports simulation vs real validation? (numbers). If you can only see a snippet, mark UNVERIFIED.

## 4. Rate each contribution
- **STANDS** — nothing comparable found.
- **HEDGE** — adjacent work exists; keep claim with qualifier + cite it.
- **THREATENED** — a work partially does it; reposition the claim (narrower or differently framed).
- **PRE-EMPTED** — already done; drop or reframe as replication/extension.

## 5. Also report the *gap* side (what is missing in the field)
From what you found, list research gaps no review addresses (e.g. per-function autonomy profiling, validation standards for autonomous SAR, LLM-agent SAR deployment evidence, responder-in-the-loop evaluations). Mark which ones this manuscript's data can support.

## 6. Output
`research_outputs/YYYY-MM-DD_literature-scout_novelty-scan.md` — verdict table, competitor table, factual-error list, recommended Introduction/Table I/abstract edits, full search log (query, date, mode, opened URLs). Provide sources as markdown links.
