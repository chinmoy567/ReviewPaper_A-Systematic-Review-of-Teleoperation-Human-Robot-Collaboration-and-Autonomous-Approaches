# Supplementary File: Search Protocol

**Review:** *Autonomy Modes and Validation Depth in Disaster Search-and-Rescue Robotics: A Systematic Review of the 2025–2026 Literature* (Avi, Sultana, Sarker).

**Contents**
1. The search actually run for this review (as reported in Section II-B).
2. A fully specified supplementary bibliographic-database search (Scopus, Web of Science Core Collection, IEEE Xplore) for the authors to run.
3. Deduplication against the existing 130-record catalog.
4. Screening of the new records.
5. Adding the results to the PRISMA flow diagram and the manuscript.

**Conventions.** `[[AUTHOR INPUT NEEDED]]` marks a value only the authors can supply. No result count in this file has been estimated or invented: every count shown is tabulated from `assets/docs/paperlinks.xlsx` (column "How it was found") or from `supplementary/screening_log.csv`, and every other result cell is left for the authors. Field codes and platform limits were checked against vendor documentation where noted; the person running each search must confirm that the platform accepts the string unchanged and record any change.

---

## 1. The search actually run

### 1.1 Who and when

- **Searcher:** one author, `[[AUTHOR INPUT NEEDED: initials]]`.
- **Search dates:** `[[AUTHOR INPUT NEEDED: date of each search, or at least the month and year of the last search per source]]`. (An earlier draft gave screening dates of 18–19 July 2026; the authors have not confirmed them.)
- **Year limit:** publications dated 2025 or later. Cataloged records: 61 dated 2025 and 69 dated 2026.

### 1.2 Table SP-1. Searches and other identification methods, as run

"Cataloged" is the number of records the searcher entered into the catalog from that source. It is **not** the number of hits the search returned. If the hit counts were not recorded, the manuscript must say so (see the audit report, drop-in D1).

| # | Route | Source / platform (URL) | Query as recorded in the catalog | Field(s) searched | Filters applied | Date run | Hits returned | Cataloged (n) |
|---|---|---|---|---|---|---|---|---|
| P1 | Publisher platform | MDPI (www.mdpi.com, site search) | "disaster rescue robot" | `[[AUTHOR INPUT NEEDED]]` | 2025 onward; `[[AUTHOR INPUT NEEDED: other filters]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | 34 |
| P2 | Publisher platform | Elsevier ScienceDirect (www.sciencedirect.com) | "rescue robot" | `[[AUTHOR INPUT NEEDED]]` | 2025 onward; `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | 20 (18 Elsevier; 2 Tech Science Press, *CMES*) |
| P3 | Publisher platform | Nature Portfolio, *Scientific Reports* (www.nature.com/srep) | "rescue robot" | `[[AUTHOR INPUT NEEDED]]` | 2025 onward; `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | 8 |
| P4 | Publisher platform | PLOS (journals.plos.org, *PLOS One*) | "rescue robot" | `[[AUTHOR INPUT NEEDED]]` | 2025 onward; `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | 6 |
| P5 | Publisher platform | IEEE Xplore (ieeexplore.ieee.org) | "rescue robot" | `[[AUTHOR INPUT NEEDED]]` | 2025 onward; `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | 5 |
| P6 | Publisher platform | Frontiers (www.frontiersin.org) | "rescue robot" | `[[AUTHOR INPUT NEEDED]]` | 2025 onward; `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | 4 |
| P7 | Publisher platform | Wiley Online Library (onlinelibrary.wiley.com) | "rescue robot" | `[[AUTHOR INPUT NEEDED]]` | 2025 onward; `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | 1 |
| | | | | | | | **Subtotal, publisher platforms** | **78** |
| G1 | Other method | Google Scholar (scholar.google.com) | "rescue robot" | all fields (Google Scholar default) | `[[AUTHOR INPUT NEEDED: year filter]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | 8 |
| G2 | Other method | Google Scholar | "disaster rescue robot" | all fields | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | 7 |
| A1 | Other method (AI-assisted discovery) | ChatGPT (OpenAI), model `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED: prompt wording or description]]` | not applicable | not applicable | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED: number of suggestions, if known]]` | 34 |
| A2 | Other method (AI-assisted discovery) | Gemini (Google), model `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | not applicable | not applicable | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | 3 |
| | | | | | | | **Subtotal, other methods** | **52** |
| | | | | | | | **Total cataloged** | **130** |

**Discrepancy to resolve before submission.** The authors' own write-up (`assets/docs/Paper Selection Process.docx`) names Google Scholar as "the main database" and lists seven queries: "rescue robot", "teleoperation", "search and rescue", "disaster management", "disaster search and rescue", "search and rescue robot", "disaster management robot". The catalog attributes cataloged records only to the two Google Scholar queries in rows G1 and G2, and attributes 78 records to publisher-platform searches. The authors confirmed the 78/15/34/3 split on 2026-11-08 and 2026-11-09. They should also state whether the other five queries were run and returned nothing that was cataloged `[[AUTHOR INPUT NEEDED]]`.

### 1.3 AI-assisted discovery: what must be reported

- Model names and versions, the interface (web chat or API), and the date of each session.
- The prompt wording, verbatim if the chat histories survive. If they do not survive, give a description and state that the transcripts were not kept.
- The verification rule that was applied: every suggested record was retrieved from its publisher and its bibliographic details were checked before cataloging. No record was accepted on the strength of an AI-generated description alone (as stated in Section II-B).
- How many suggestions were rejected because they did not exist or did not match (hallucinated or mis-cited references) `[[AUTHOR INPUT NEEDED: number, or "not recorded"]]`.
- AI-assisted discovery is **not reproducible**, and the manuscript says so (Sections II-B and V-D).

### 1.4 Other PRISMA-S statements for the search as run (confirm each)

- No bibliographic databases (Scopus, Web of Science) and no study registers were searched.
- No journal tables of contents, conference proceedings or websites were browsed `[[AUTHOR INPUT NEEDED: confirm]]`.
- No citation chasing (backward or forward) was done.
- No study authors or experts were contacted `[[AUTHOR INPUT NEEDED: confirm]]`.
- No published search filters were used, and no search strategy from another review was reused `[[AUTHOR INPUT NEEDED: confirm]]`.
- The search strategy was not peer reviewed.
- The searches were not updated.
- Journal quartile: every cataloged record carries a Q1 or Q2 tag (66 Q1, 64 Q2; none is Q3, Q4 or unranked). The authors must state whether quartile was used to decide which hits to catalog `[[AUTHOR INPUT NEEDED]]`. If it was, it is an eligibility restriction and must be reported in Section II-D.

---

## 2. Supplementary bibliographic-database search (to be run by the authors)

### 2.1 Purpose

1. Give the review a reproducible, Boolean, multi-database search that a reader can re-run.
2. Measure how complete the original identification was, by testing whether the database search retrieves the 39 included studies (recall test, Sec. 2.7).
3. Find eligible 2025–2026 studies that the original routes missed.

### 2.2 Eligibility applied to the new records

The same criteria C1–C3 as Section II-D, unchanged, plus:
- publication year 2025 or 2026 (record the year as the year of the final or online-first version; see Sec. 2.5);
- English language;
- document type: journal article `[[AUTHOR INPUT NEEDED: confirm that conference papers stay ineligible, as for the original corpus; if the authors decide to admit conference papers, they must re-check the original corpus rule too, and add document type "cp" / "Proceedings Paper" / IEEE "Conferences" below]]`.

Reviews are retrieved but not included. They are excluded at screening (C3), and their reference lists feed citation chasing (Sec. 2.8).

### 2.3 Concept blocks

**Block A, search-and-rescue application** (the bare acronym "SAR" is deliberately omitted, because in engineering databases it mostly retrieves synthetic aperture radar; "SAR robot" is covered by Block A phrases combined with Block B):

"search and rescue", "search-and-rescue", "urban search", USAR, "rescue robot*", "disaster robot*", "disaster response", "emergency response", "post-disaster", "post-earthquake", "earthquake rescue", "flood rescue", "mine rescue", "maritime rescue", "wilderness search", "victim detection", "victim search", "survivor detection", "survivor search", "collapsed building*", "collapsed structure*", "rescue operation*", "rescue mission*"

**Block B, robotic platform:**

robot*, UAV, UAVs, drone*, "unmanned aerial", "unmanned ground", UGV, UGVs, "unmanned surface", USV, "underwater vehicle*", AUV, quadrotor*, multirotor*, quadruped*, "legged robot*", hexapod*, "multi-robot", swarm*, uncrewed

**Block C, optional precision block (do not use in the primary search):** autonom*, teleoperat*, "shared control", "shared autonomy", supervisory, "human-robot". Block C is listed only for a documented precision check. Adding it would remove studies whose abstracts do not name the control paradigm, which is the review's main variable, so the primary search is A AND B.

### 2.4 Strings

Copy each string exactly. Record any change the platform forces (term limits, wildcard limits, syntax errors) in Table SP-2, with the string as finally run.

**S-1. Scopus** (www.scopus.com, Advanced document search):

```
TITLE-ABS-KEY(
 ( "search and rescue" OR "search-and-rescue" OR "urban search" OR usar OR "rescue robot*"
   OR "disaster robot*" OR "disaster response" OR "emergency response" OR "post-disaster"
   OR "post-earthquake" OR "earthquake rescue" OR "flood rescue" OR "mine rescue"
   OR "maritime rescue" OR "wilderness search" OR "victim detection" OR "victim search"
   OR "survivor detection" OR "survivor search" OR "collapsed building*" OR "collapsed structure*"
   OR "rescue operation*" OR "rescue mission*" )
 AND
 ( robot* OR uav OR uavs OR drone* OR "unmanned aerial" OR "unmanned ground" OR ugv OR ugvs
   OR "unmanned surface" OR usv OR "underwater vehicle*" OR auv OR quadrotor* OR multirotor*
   OR quadruped* OR "legged robot*" OR hexapod* OR "multi-robot" OR swarm* OR uncrewed )
)
AND PUBYEAR > 2024 AND PUBYEAR < 2027
AND ( LIMIT-TO ( DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "re" ) )
AND ( LIMIT-TO ( LANGUAGE , "English" ) )
```

- `TITLE-ABS-KEY` searches title, abstract and keywords (author and indexed).
- Record the hit count **before** the DOCTYPE and LANGUAGE limits and **after** them (two numbers in Table SP-2).
- Scopus treats double-quoted text as a loose phrase and allows wildcards inside it. Confirm that the platform accepts `"rescue robot*"`; if not, replace it with `"rescue robot" OR "rescue robots"` and record the change.

**S-2. Web of Science Core Collection** (www.webofscience.com, Advanced Search):

```
TS=( ( "search and rescue" OR "search-and-rescue" OR "urban search" OR USAR OR "rescue robot*"
   OR "disaster robot*" OR "disaster response" OR "emergency response" OR "post-disaster"
   OR "post-earthquake" OR "earthquake rescue" OR "flood rescue" OR "mine rescue"
   OR "maritime rescue" OR "wilderness search" OR "victim detection" OR "victim search"
   OR "survivor detection" OR "survivor search" OR "collapsed building*" OR "collapsed structure*"
   OR "rescue operation*" OR "rescue mission*" )
 AND
 ( robot* OR UAV OR UAVs OR drone* OR "unmanned aerial" OR "unmanned ground" OR UGV OR UGVs
   OR "unmanned surface" OR USV OR "underwater vehicle*" OR AUV OR quadrotor* OR multirotor*
   OR quadruped* OR "legged robot*" OR hexapod* OR "multi-robot" OR swarm* OR uncrewed ) )
AND PY=(2025-2026)
AND LA=(English)
AND DT=(Article OR Review OR Early Access)
```

- `TS=` (Topic) searches title, abstract, author keywords and Keywords Plus.
- **Record the Core Collection editions and year coverage the institution subscribes to** (e.g. SCI-EXPANDED, ESCI, CPCI-S), from the "Editions" selector. PRISMA-S item 1 requires this, and results differ by subscription. `[[AUTHOR INPUT NEEDED]]`
- If `DT=` or `LA=` is rejected in the query box, run the `TS=` and `PY=` parts and apply document type and language with the refine panel; record which method was used.

**S-3. IEEE Xplore** (ieeexplore.ieee.org, Advanced Search > Command Search):

```
("All Metadata":"search and rescue" OR "All Metadata":"search-and-rescue" OR "All Metadata":"urban search"
 OR "All Metadata":USAR OR "All Metadata":"rescue robot" OR "All Metadata":"rescue robots"
 OR "All Metadata":"disaster response" OR "All Metadata":"emergency response" OR "All Metadata":"post-disaster"
 OR "All Metadata":"post-earthquake" OR "All Metadata":"mine rescue" OR "All Metadata":"flood rescue"
 OR "All Metadata":"maritime rescue" OR "All Metadata":"wilderness search" OR "All Metadata":"victim detection"
 OR "All Metadata":"survivor detection" OR "All Metadata":"collapsed building" OR "All Metadata":"collapsed structure")
AND
("All Metadata":robot* OR "All Metadata":UAV OR "All Metadata":drone* OR "All Metadata":"unmanned aerial"
 OR "All Metadata":"unmanned ground" OR "All Metadata":UGV OR "All Metadata":"unmanned surface"
 OR "All Metadata":"underwater vehicle" OR "All Metadata":quadruped OR "All Metadata":"legged robot"
 OR "All Metadata":"multi-robot" OR "All Metadata":swarm)
```

- Filters (left panel): Year 2025–2026; Content type: Journals and Early Access Articles `[[AUTHOR INPUT NEEDED: plus Conferences only if conference papers are made eligible]]`.
- "All Metadata" covers title, abstract, index terms and author keywords, but not full text. It is broader than Scopus TITLE-ABS-KEY; note this in Table SP-2.
- The IEEE string uses only two wildcards, because IEEE Xplore caps the number of wildcards per search. Its help pages give different caps in different versions, so check the current Command Search help. If Xplore rejects the string as too long, split Block A into two halves (IEEE-1: the first nine Block A terms; IEEE-2: the remaining nine), run each with the full Block B, merge by DOI, and record both strings and both counts.

**Optional S-4. ACM Digital Library** (dl.acm.org, Advanced Search; Title and Abstract fields; publication date 2025–2026), using Blocks A and B unchanged. This is recommended only if the authors decide to admit conference papers, since most ACM robotics content is proceedings.

### 2.5 What to record for every search (Table SP-2)

| Field | S-1 Scopus | S-2 WoS CC | S-3 IEEE Xplore |
|---|---|---|---|
| Date run (YYYY-MM-DD) and time zone | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` |
| Person who ran it (initials) | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` |
| Platform / interface and access route (institutional licence) | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` (+ editions) | `[[AUTHOR INPUT NEEDED]]` |
| String as finally run (pasted from the platform's search history) | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` |
| Hits before limits | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` |
| Hits after limits (= records exported) | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` |
| Changes forced by the platform | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` |
| Export file name(s) | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` | `[[AUTHOR INPUT NEEDED]]` |

Also record:
- A screenshot or PDF of each platform's search-history page on the day of the search.
- Year boundary rule: a record counts as 2025–2026 by the year the platform assigns. Online-first 2026 articles that a platform already lists under 2027 are retrieved by none of the strings above. Note any such record found during citation chasing as "found by other methods".

### 2.6 Peer review of the strategy before running it

- Before the strings are run, a second person reviews them with the PRESS 2015 guideline elements (translation of the research question, Boolean and proximity operators, subject headings, text-word searching, spelling, syntax and line numbers, limits and filters). Ideally the reviewer is a university librarian; otherwise a co-author who did not draft them. PRESS reference: McGowan et al. (2016), *Journal of Clinical Epidemiology*, 75, 40–46 (UNVERIFIED in this project; have citation-verifier check it before citing).
- Reviewer: `[[AUTHOR INPUT NEEDED]]`. Changes made after review: `[[AUTHOR INPUT NEEDED]]`.

### 2.7 Export

- **Scopus:** export all records as **RIS** and as **CSV**, with "Citation information" and "Bibliographical information" plus "Abstract & keywords". Export in batches if the result exceeds the platform's per-export limit, and record the number of batches.
- **Web of Science:** export as **RIS** (or "Plain text file") with record content "Full Record". Also export "Full Record and Cited References" if backward citation chasing will use WoS. Export in batches within the platform's per-export limit.
- **IEEE Xplore:** export as **CSV** ("Export > Search Results"), and as RIS citations if available.
- Keep the raw export files unchanged in `data/search_update/raw/` and work on copies.

### 2.8 Recall test against the existing corpus (search validation)

- **Gold set:** the 39 included studies (DOIs in `S2_extraction_table.csv` (= `data/extraction_table.csv`), column `doi`).
- For each database, report: (i) how many of the 39 the database indexes (look each DOI up directly); (ii) how many the string retrieved; (iii) recall = retrieved / indexed.
- Report combined recall across S-1 to S-3 = (gold-set studies retrieved by at least one database) / 39.
- If combined recall is below 90%, inspect the missed studies' titles, abstracts and keywords. Add the missing synonyms to Blocks A or B, re-run, and report both versions.
- Results: `[[AUTHOR INPUT NEEDED]]` (do not estimate).

### 2.9 Citation chasing (recommended, PRISMA "other methods")

- **Backward:** reference lists of the 39 included studies and of Kareem et al. (2026a).
- **Forward:** studies citing the 39 included studies and Kareem et al. (2026a), in Scopus or WoS "Cited by", limited to 2025–2026.
- A tool such as citationchaser (Haddaway et al., 2022, *Research Synthesis Methods*; UNVERIFIED in this project, so check before citing) can make this reproducible.
- Record the date and the number of records found. Screen them with the same procedure as Sec. 4, and report them in the "other methods" column of the flow diagram.

---

## 3. Deduplication against the existing 130-record catalog

**Inputs:** the merged exports from S-1 to S-3 (and citation chasing, if done), and `assets/docs/paperlinks.xlsx` (130 records, including the five duplicates removed earlier).

**Step 1, within the new search.** Remove duplicates across the databases.

**Step 2, against the catalog.**
1. **DOI match.** Normalize each DOI: lower-case it; strip `https://doi.org/`, `http://doi.org/`, `http://dx.doi.org/` and `doi:`; trim whitespace and any trailing `.` `,` `;`. Exact match on the normalized DOI.
2. **Title match** for records without a DOI, or with no DOI match. Normalize the title: lower-case; Unicode NFKD with diacritics removed; replace every character that is not a letter or digit with a space; collapse runs of spaces. Exact match on the normalized title first. Then flag pairs with a token-set similarity of at least 0.90 for **manual** comparison of authors, year and venue. Never merge a flagged pair automatically.
3. **Online-first versus final versions:** the same DOI counts as the same record. Different DOIs (e.g. a preprint and the article) are compared manually, and the journal version is kept.

**Step 3, outputs.**
- `data/search_update/dedup_log.csv`, with columns: `new_record_id, source_db, doi_norm, title_norm, match_type (doi / title_exact / title_fuzzy_confirmed / none), matched_catalog_no, decision, checked_by`.
- Counts for the flow diagram: duplicates within the new search `[[AUTHOR INPUT NEEDED]]`; records already in the catalog `[[AUTHOR INPUT NEEDED]]` (split into already-included `[[AUTHOR INPUT NEEDED]]` and already-excluded `[[AUTHOR INPUT NEEDED]]`); new unique records to screen `[[AUTHOR INPUT NEEDED]]`.
- The already-included count from Step 2 is the recall numerator in Sec. 2.8.

Reference implementation, Python standard library only (run on a copy of the exports):

```python
import csv, re, unicodedata
from difflib import SequenceMatcher

def norm_doi(d):
    d = (d or "").strip().lower()
    d = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", d)
    return d.rstrip(".,; ")

def norm_title(t):
    t = unicodedata.normalize("NFKD", t or "")
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", t)).strip()

def token_set_ratio(a, b):
    sa, sb = set(a.split()), set(b.split())
    inter = " ".join(sorted(sa & sb))
    ra = " ".join(sorted(sa - sb)); rb = " ".join(sorted(sb - sa))
    s1, s2 = (inter + " " + ra).strip(), (inter + " " + rb).strip()
    return max(SequenceMatcher(None, inter, s1).ratio(),
               SequenceMatcher(None, inter, s2).ratio(),
               SequenceMatcher(None, s1, s2).ratio())
# 1) build dicts {norm_doi: catalog_no} and {norm_title: catalog_no} from the catalog
# 2) for each new record: DOI match -> exact title match -> fuzzy (>= 0.90) flagged for manual check
```

---

## 4. Screening the new records

### 4.1 Reviewers and independence
- Two reviewers, `[[AUTHOR INPUT NEEDED: initials]]` and `[[AUTHOR INPUT NEEDED: initials]]`, screen every new record independently.
- Each reviewer records decisions in **their own copy** of the screening sheet (or blind mode in a screening tool such as Rayyan) before seeing the other's decisions.
- Both per-reviewer files are **kept** and released with the data package. The original screening lost per-screener records, so this is the single most important process change.
- A third author, `[[AUTHOR INPUT NEEDED]]`, resolves disagreements that discussion does not settle. The reason for each final decision is logged.
- AI tools are not used to make screening decisions. If an AI check is used, it is reported separately as a post hoc audit, as in Section II-E.

### 4.2 Stages
1. **Calibration.** Both reviewers screen the same 30 randomly chosen new records, compare, and refine their shared reading of C1–C3 (the criteria text itself is not changed). Calibration records are re-screened blind in the main pass.
2. **Title and abstract.** Include/exclude/unsure. "Unsure" from either reviewer goes to full text.
3. **Full text.** Include, or exclude with **every** criterion failed (C1, C2, C3, plus "ineligible publication type", "ineligible year" or "not English" if they arise), as in the original log. Also record a **primary reason** using the hierarchy C1 > C2 > C3, so that the flow diagram can give mutually exclusive counts.

### 4.3 Screening sheet columns
`new_record_id, source_db, doi, title, year, doc_type, reviewer, stage (TA/FT), decision (include/exclude/unsure), criteria_failed (C1;C2;C3;other), primary_reason, note, date`, with one file per reviewer, plus `screening_consensus.csv` holding the final decision and how it was reached (agreement / discussion / third reviewer).

### 4.4 Agreement statistics (report for each stage)
- The 2×2 table of reviewer A vs. reviewer B (include/exclude), with percent agreement.
- **Cohen's κ** with 95% CI (Cohen, 1960). Interpret it with Landis and Koch (1977), cited as a convention, not a quality threshold.
- Because inclusion prevalence is low, κ is depressed even when agreement is high. Report **Gwet's AC1** (Gwet, 2008), or PABAK, alongside it.
- Report κ separately for title/abstract and full-text decisions, and for C1, C2 and C3 at full text.
- Results: `[[AUTHOR INPUT NEEDED]]`.

### 4.5 Optional retrospective agreement check on the original 125 records
The original screeners' separate decisions were not kept, so the original agreement cannot be recovered. A truthful substitute: two authors re-screen, blind to the logged decisions and to each other, a random sample of about 30% of the 125 records, stratified by logged decision (12 of the 39 included, 26 of the 86 excluded; fixed random seed reported). Report κ between the two re-screeners and between each re-screener and the logged decision. Label it in the manuscript as a **post hoc** reliability check, not as the original screening agreement.

### 4.6 Extraction and coding for any newly included study
- Same 18 fields and coding manual (`supplementary/coding_manual.md`).
- Two coders code the autonomy/HRI mode and validation type independently; report Cohen's κ.
- Page references for every coded cell, as in `data/extraction_table.csv`.

---

## 5. Adding the results to the PRISMA flow diagram and the manuscript

### 5.1 Flow diagram (recommended layout, because the review is not yet published)
Use the PRISMA 2020 two-column template:
- **Left column, "Identification of studies via databases":** records identified from Scopus (n = `[[AUTHOR INPUT NEEDED]]`), Web of Science Core Collection (n = `[[AUTHOR INPUT NEEDED]]`) and IEEE Xplore (n = `[[AUTHOR INPUT NEEDED]]`). Records removed before screening: duplicates across databases (n = `[[AUTHOR INPUT NEEDED]]`); records already in the original catalog (n = `[[AUTHOR INPUT NEEDED]]`). Records screened by title and abstract (n = `[[AUTHOR INPUT NEEDED]]`) → excluded (n = `[[AUTHOR INPUT NEEDED]]`). Reports sought (n = `[[AUTHOR INPUT NEEDED]]`) → not retrieved (n = `[[AUTHOR INPUT NEEDED]]`). Reports assessed (n = `[[AUTHOR INPUT NEEDED]]`) → excluded, by primary reason C1/C2/C3/other (n = `[[AUTHOR INPUT NEEDED]]` each).
- **Right column, "Identification of studies via other methods":** the existing streams (publisher platforms, 78; Google Scholar, 15; AI-assisted discovery, 37), with their existing counts (5 duplicates; 125 assessed; 86 excluded), plus citation chasing if done (n = `[[AUTHOR INPUT NEEDED]]`).
- **Included box:** studies included = 39 + new studies (n = `[[AUTHOR INPUT NEEDED]]`). Also report how many of the 39 were also retrieved by the databases (recall numerator, Sec. 2.8).

Alternative: the PRISMA 2020 template for **updated reviews** has a "Studies included in previous version of review (n = 39)" box. It suits a published update, but this would be the first publication, so the two-column layout above is preferred.

The diagram script (`data/make_prisma_v2.py`) should read the counts from a CSV filled in by the authors, so that no number is typed by hand.

### 5.2 Manuscript changes (record each change in the revision log)
- **Section II-B:** add the database search as a third identification route: strings (pointing to this file), dates, editions, limits, PRESS review, and recall result. Revise the sentence "The search did not cover bibliographic databases such as Scopus and Web of Science".
- **Table II:** add a "Bibliographic databases" column. **Fig. 1 and Fig. 2:** regenerate.
- **Sections II-E and II-K:** new-record screening, κ, and counts.
- **If any new study is included:** every corpus-derived number in Sections III–VI, the Abstract, and Tables VI–XVIII changes. Re-run `data/analysis.py` and `data/make_figures.py`, then re-run the stats-consistency check.
- **Section V-D:** soften the "narrow search" limitation according to the recall result, without deleting it, because the AI-assisted route remains non-reproducible.
- **If the authors run the search only as a coverage check and do not screen its new records:** this must be stated explicitly, with the number of unscreened new records. This is a weaker option, and reviewers are likely to ask why eligible studies were left out.

---

*Prepared 2026-11-09 by the methodology audit. No search in Sec. 2 has been run; every result cell is for the authors to fill in.*
