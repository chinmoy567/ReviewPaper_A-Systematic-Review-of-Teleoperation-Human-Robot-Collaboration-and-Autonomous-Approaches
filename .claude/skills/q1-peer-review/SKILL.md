---
name: q1-peer-review
description: Rubric and report format for a simulated Q1-journal peer review of the SAR robotics systematic review (or any section of it). Use when the user asks for a review, a "Reviewer 2" critique, a mock decision, or to check whether the paper would be accepted.
---

# Q1 Peer Review

Delegate to the `q1-reviewer` agent for a full-paper review. For a single section, you may apply the rubric directly.

## Rubric (score 1–5 each; 5 = Q1-excellent)

| Dimension | 5 looks like | 1–2 looks like |
|---|---|---|
| 1. Novelty & positioning | Clear, verified gap vs. all reviews ≤3 yrs; accurate prior-work characterization | Overclaims "first"; missing recent competitors; mischaracterized prior work |
| 2. Search & selection rigor | Scopus/WoS + IEEE/ACM, full strings, dates, κ, protocol | Few terms, portals only, no strings, no agreement stats |
| 3. Quality appraisal | Named instrument, scores reported and used | None |
| 4. Data extraction & coding | Coding manual, reliability shown, supplementary data | Ad hoc, unreproducible |
| 5. Analysis & statistics | n/N everywhere, CIs, appropriate tests, small-cell caveats | Percentages on tiny cells as if robust |
| 6. Theoretical contribution | Taxonomy grounded in LOA theory, operational rules | Categories asserted without grounding |
| 7. Insight & implications | Explains mechanisms; actionable agenda for research + practice/standards | Restates results; generic future work |
| 8. Threats to validity | Construct/internal/external/conclusion addressed | Two bullet points |
| 9. Writing & structure | Tight, consistent, venue-compliant | Internal jargon, repetition |
| 10. References & presentation | All verified, current, good figures | Weak sources, errors |

**Decision mapping:** mean ≥4.3 and no dimension <3 → Minor; mean 3.3–4.3 or any 2 → Major; any dimension 1 on 1/2/5 or mean <3.3 → Reject (resubmit).

## Comment format
```
M3. [Sec. II-C, Search Criteria] Problem: only two search terms on publisher portals.
Why it matters: coverage and reproducibility (PRISMA 2020 item 7, PRISMA-S item 8).
Fix: re-run in Scopus + WoS + IEEE Xplore with full Boolean string (provide), report date, merge and dedupe, update PRISMA.
```

## Report sections
Summary · Decision + confidence · Rubric table · Major comments · Minor comments · Shortest path to Accept (ranked) · Confidential note to editor.

Save to `research_outputs/YYYY-MM-DD_q1-reviewer_report.md`.
