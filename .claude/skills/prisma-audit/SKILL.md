---
name: prisma-audit
description: Audit the review's methodology against the PRISMA 2020 27-item checklist, PRISMA-S search-reporting items, and Q1 rigor criteria (protocol, inter-rater agreement, quality appraisal), producing an item-by-item table and concrete fixes with drop-in text. Use when checking or strengthening the Methodology section or preparing the PRISMA checklist supplement.
---

# PRISMA Audit

Delegate full audits to the `methodology-auditor` agent. Verify item wording against the official PRISMA 2020 statement (Page et al., BMJ 2021;372:n71) and PRISMA-S (Rethlefsen et al., Syst Rev 2021;10:39) via web if unsure — do not paraphrase from memory into the supplement.

## PRISMA 2020 items to check (abridged labels)
1 Title identifies as systematic review · 2 Abstract (PRISMA-Abstracts) · 3 Rationale · 4 Objectives · 5 Eligibility criteria · 6 Information sources + dates · 7 Full search strategy · 8 Selection process (who, independent, tools) · 9 Data collection process · 10a/b Data items · 11 Risk-of-bias/quality method · 12 Effect measures (state N/A or proportions) · 13a–f Synthesis methods · 14 Reporting-bias assessment · 15 Certainty assessment · 16a/b Study selection + flow diagram + excluded-with-reasons · 17 Study characteristics · 18 Risk of bias in studies · 19 Results of individual studies · 20a–d Synthesis results · 21 Reporting biases · 22 Certainty · 23a–d Discussion incl. limitations of evidence and of review · 24a–c Registration & protocol · 25 Support/funding · 26 Competing interests · 27 Availability of data, code, materials.

## PRISMA-S essentials
Databases & platforms named · multi-database search · registries/grey lit · online resources/browsing · citation searching · contacts · other methods · full strings for each · limits & restrictions · search filters · prior work reused · updates · dates of searches · peer review of search (PRESS) · total records per source · deduplication method.

## Robotics-SLR rigor add-ons
- Kitchenham & Charters-style quality questions (aim clear? method described? validation adequate? results reproducible? limitations stated?) scored 0/0.5/1.
- Fleiss' κ for 3 raters (screening + Autonomy/HRI label); interpretation per Landis & Koch.
- Sensitivity analysis: do headline findings hold excluding low-quality studies?

## Output format
Table: Item | Status (✅ / ◐ / ❌ / N/A) | Where in manuscript | Fix. Then ranked fixes and Markdown drop-ins. "Where in manuscript" means the location in `SAR_review_master_document.md` Secs. 9–14, the only manuscript source; never use `SAR_review_manuscript.tex` or any PDF of the paper. Never write that a step was done if the authors did not do it — draft wording as a template with `[AUTHORS: fill]` markers.
