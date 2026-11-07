---
name: citation-check
description: Verify every reference in the manuscript exists and is correctly described, every claim attributed to a source is supported, citations are sequential and complete, and formatting matches the target journal. Use before submission, after adding references, or when the user asks to check references.
---

# Citation Check

Delegate to the `citation-verifier` agent for the full bibliography; do it inline for 1–3 new references.

## Steps
0. **Source**: the manuscript exists only in `SAR_review_master_document.md`. The references are the Sec. 15 "### Final numbered bibliography" and the in-text citations are in Secs. 9–14. Never read `SAR_review_manuscript.tex` or any PDF of the paper, which are retired.
1. **Inventory**: extract all numbered entries from the Sec. 15 bibliography and all in-text `[N]` uses in the manuscript text (Grep). Report uncited entries and citations without entries.
2. **Existence**: for each entry, search DOI first (`https://doi.org/<doi>`), else exact title in quotes. Status: EXISTS / MISMATCH / NOT-FOUND / UNVERIFIED.
3. **Claim support** (priority claims): prior-review characterizations in Introduction & Table I; disaster statistics (CRED report); golden-window survival figures; every "first/only/not previously reported" statement. Quote the supporting phrase from the source.
4. **Source quality**: flag news, blogs, Wikipedia, unreviewed preprints used for key facts; suggest verified peer-reviewed replacements only.
5. **Recency profile**: % of references from the last 3 years (a "recent advances" review should be high).
6. **Format**: IEEE style → `A. B. Author, C. Author, and D. Author, "Title," *Abbrev. J.*, vol. X, no. Y, pp. Z–W, Mon. Year, doi: …`. Currently the Sec. 15 entries use APA-like author-year order. Flag them for conversion to the target journal's style; the conversion is done in the `.md` and carried into whatever submission file is later built from it.

## Known items to re-check (2026-11-08)
- [3] NBC News quote — replace or supplement with a peer-reviewed source.
- [2] arXiv preprint for golden-window framing — check for a published version.
- [6] Bakzadeh 2026 — manuscript says autonomy is excluded from scope; source excludes autonomy *software* but classifies autonomy *level* (A1/A2/A3).

Output: `research_outputs/YYYY-MM-DD_citation-verifier_report.md`.
