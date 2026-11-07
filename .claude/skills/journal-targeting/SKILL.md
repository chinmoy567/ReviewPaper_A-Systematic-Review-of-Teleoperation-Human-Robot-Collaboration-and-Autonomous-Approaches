---
name: journal-targeting
description: Select and verify a Q1 target journal for the SAR robotics systematic review — live-check quartile (JCR/SJR, category, year), scope fit for review articles, limits, APC, template — and produce the reformatting checklist. Use when the user asks which journal to submit to, whether a journal is Q1, or to reformat for a venue.
---

# Journal Targeting

Delegate to `journal-scout`. Rules:
1. **Quartiles must be verified live** (Scimago `scimagojr.com` page for SJR; Clarivate JCR via journal homepage/"Journal Citation Reports" statements). State source + year + subject category. Different categories can give different quartiles — report the best *and* the relevant one.
2. Confirm the journal publishes unsolicited review articles (some journals' reviews are invitation-only).
3. Capture: word/page limits for reviews, abstract limit, reference style, LaTeX template, APC, OA options, median time to first decision, special issues on disaster/field robotics (a fitting special issue raises acceptance odds).
4. Fit scoring for this paper: field robotics ✔, HRI/autonomy ✔, disaster management ✔, systematic-review method ✔.
5. Strategy: list a primary, a secondary, and a safety Q1 option; note the reference-style conversion each needs. The manuscript exists only as `SAR_review_master_document.md` (the old `.tex`/PDF are retired). The submission file, whether IEEEtran, Elsevier `elsarticle` or Springer `sn-jnl`, will be built fresh from the `.md` once the venue is chosen.

Output: `research_outputs/YYYY-MM-DD_journal-scout_shortlist.md`, then ask the user to choose before reformatting.
