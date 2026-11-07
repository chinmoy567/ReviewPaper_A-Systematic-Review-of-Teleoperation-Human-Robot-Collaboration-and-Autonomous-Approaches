---
name: search-update
description: Design a reproducible, PRISMA-S-compliant database search (Scopus, Web of Science, IEEE Xplore, ACM DL) for the SAR robotics review, plus an update-search and merge procedure, to fix the narrow two-term publisher-portal search. Use when strengthening the search strategy, running an update search before submission, or answering a reviewer's coverage critique.
---

# Search Strategy Upgrade

The current search ("rescue robot" / "disaster rescue robot" on publisher portals) is the manuscript's single largest Q1 rejection risk. This skill produces a search the authors can run themselves (database access is needed, so Claude drafts and the authors execute; never fabricate hit counts).

## 1. Concept blocks
- **A (application):** "search and rescue" OR "search-and-rescue" OR SAR OR USAR OR "urban search" OR "disaster response" OR "disaster robot*" OR "emergency response" OR "rescue robot*" OR "mine rescue" OR "victim detection" OR "survivor detection" OR "collapsed building*" OR earthquake OR flood OR wildfire
- **B (robot):** robot* OR UAV OR UAVs OR drone* OR "unmanned aerial" OR UGV OR "unmanned ground" OR quadruped OR "legged robot*" OR "multi-robot" OR swarm OR "unmanned surface" OR USV OR AUV
- **C (optional precision filter, test sensitivity with and without):** autonom* OR teleoperat* OR "shared control" OR "shared autonomy" OR supervisory OR "human-robot"
- Limits: 2025–2026; English; article / conference paper; exclude reviews (screened later, not filtered, so they can feed citation chasing).

## 2. Database syntax (verify field codes on each platform before running)
- **Scopus:** `TITLE-ABS-KEY((A) AND (B)) AND PUBYEAR > 2024 AND (LIMIT-TO(LANGUAGE,"English"))`
- **Web of Science Core:** `TS=((A) AND (B))` with Publication Years 2025–2026
- **IEEE Xplore:** Command Search, "All Metadata", year filter 2025–2026
- **ACM DL:** Abstract + Title fields, 2025–2026
- Keep the original publisher-portal searches as a **supplementary source** (PRISMA "other methods"), not discarded.

## 3. Validation of the search (PRISMA-S + rigor)
- Gold-set test: the 39 included papers should be retrieved — report recall = found/39. If <90%, revise blocks.
- Report per-database hits, date run, exact string (supplementary table).
- Citation chasing: backward (references of included papers) + forward (citations of Kareem et al. 2026 and of included papers).

## 4. Merge & screen
Deduplicate by DOI then normalized title; screen only new records with the same C1–C3 criteria and the same three-rater + consensus process; compute Fleiss' κ on the new batch; update PRISMA (two-column "previous studies / new search" layout of PRISMA 2020 for updated reviews).

## 5. Manuscript changes
Update Sec. II-B/C, Table II, PRISMA figure, all corpus-derived numbers (rerun `stats-consistency-checker`), and add the search strings to a supplementary file. Log in master doc Sec. 16.
