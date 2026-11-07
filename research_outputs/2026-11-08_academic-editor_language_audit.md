# Language and consistency audit (report only, no edits made): 2026-11-08

**Agent:** academic-editor. **Mode:** audit only. `SAR_review_master_document.md` was not modified.
**Scope:** manuscript text under TITLE AND AUTHORS, ABSTRACT, and I.–VI. (lines 307–409, 419–555, 567–605, 615–654, 666–699, 718–744), plus the Sec. 15 numbered bibliography (lines 810–904). Status and Sourcing notes were skipped.
**Target style:** IEEE (American spelling, IEEE Access abstract of 150–250 words in one paragraph with no citations).
**Line numbers** are from the file as it stood on 2026-11-08.

Severity: **[S]** serious (accuracy, overclaim, leakage, or a rule-4 methods issue), **[M]** moderate (clarity, consistency, grammar), **[m]** minor (style, polish).
Items marked **→ stats-consistency-checker** or **→ citation-verifier** involve a number, label, or source description. I have not changed these and leave them to the named agent.

---

## 0. Abstract word count

- Current abstract (line 730): **275 words**. That is **25 over** the IEEE Access limit of 250. It is one paragraph and contains no citations.
- A ≤250-word replacement is given in §8 (**238 words**). It keeps every number.

---

## 1. Working-document leakage (all [S])

1. [Line 436] "surveyed by the model reference paper's own three-mode HRI account [4]" → leaked internal label. It also contradicts line 676, which says [4] reports no per-mode distribution, so "predominantly human-supervised framings" is unsupported → "…a departure from the HRI framing in [4], which defines only human-involved modes." (Or delete the sentence: it repeats line 425.)
2. [Lines 571, 573] Fig. 7 alt text and caption: "this review's structural counterpart to the model reference paper's five-layer system architecture [4]" → leakage inside a caption → "Fig. 7. Four-way Autonomy/HRI Mode taxonomy applied to the 39 included papers."
3. [Line 605] "None of the four verified prior reviews resolve…" → "verified prior reviews" is leakage → "To our knowledge, none of the prior reviews in Table I resolves…"
4. [Line 605] "this review's structural counterpart to the model reference paper's five-layer architecture [4]" → leakage → "…plays the organizing role that the five-layer architecture plays in [4]."
5. [Line 605] "as all four verified prior reviews are" → leakage → "as the prior reviews in Table I are".
6. [Line 617] "rather than in the model reference paper's generic gap list" → leakage, and a gratuitous jab at [4] → "…grounded in that evidence."
7. [Line 623] "A further nuance the extraction table's short fields did not capture:" → describes the internal workflow → "A further result is relevant:"
8. [Line 631] "This was checked directly against the extraction data before writing this section" → process narration → "We tested this hypothesis against the extraction data; it does not hold."
9. [Line 633] "than the generic-scenario framing this section originally set out to test" → "originally set out to" is leakage → "…than the generic-versus-specific distinction."
10. [Line 641] "for the same reason the model reference paper states its own [4]" → leakage → "Several limitations of this review should be stated plainly:"
11. [Line 699] The whole italic note "*(The model reference paper's own Introduction [4] has no closing … roadmap … Left out here to match; add one later if wanted.)*" sits under heading I → an editorial note inside the manuscript → delete it. IEEE Access papers normally end the Introduction with a roadmap, so consider adding: "Section II describes the review method, Section III reports the results, Section IV presents the taxonomy, Section V discusses the findings, and Section VI concludes."
12. [Line 583] "(Its headlined validation used autonomous waypoint navigation…; a one-off manual repositioning step … does not change this primary classification.)" → internal classification reasoning → move it to the supplementary coding manual, or shorten to "[17] validated its framework under autonomous waypoint navigation."
13. [Line 694] "an explicit, logged, precedent-based classification protocol" (also lines 375, 605, 690, 730, 738) → "logged" and "precedents" are working-record terms. A reviewer will ask to see them → "an explicit rule-based classification protocol (decision rules in Supplementary Table S1)". Keep this only if the authors supply that supplement.
14. **Bibliography internal notes** [S]. Delete every italic working note from the submission bibliography:
    - [Line 814] [3] "*(Secondary news citation, not a peer-reviewed source — …)*"
    - [Line 826] [9] "*(This review's own excluded paper #4, cited in Methodology Section II.D …)*". This note also gives the wrong section: [9] is cited in Section II-E.
    - [Line 852] [22] "*(Costa-Pérez also co-authors ID 87 …)*" (internal record ID)
    - [Line 856] [24] "*(Same author team as ID 14 …)*" (internal record ID)
    - [Line 862] [27] "*(Third paper by the Kareem/Abid/Hammood trio … model reference paper …)*"
    - [Line 874] [33] "*(Page number corrected …)*"
    - [Line 904] [48] "*(Author names as given on the paper …)*"

---

## 2. Overclaims and calibration ([S] unless marked)

15. [Line 730] "which has not been reported previously in this literature" → novelty claim. The only dated scan (`research_outputs/2026-11-08_initial_novelty_scan_and_stats.md`) is a 6-search baseline, and its item 4 says to hedge → "To our knowledge, this gap has not been quantified in prior SAR reviews."
16. [Line 696] "An empirical finding, not previously reported in prior SAR robotics reviews" → same issue → "An empirical finding, to our knowledge not quantified in prior SAR reviews, …"
17. [Line 730] "compared with 60–75% for the more human-involved modes"; [Line 696] "compared with 60–75% for the more human-involved control modes" → **factually wrong scope**. Shared-Collaborative Control is human-involved but has 0/3 field-tested (Table XI). The 60–75% range covers only Teleoperation and Supervisory Control → "…compared with 60–75% for Teleoperation and Supervisory Control." (Line 740 already says this correctly.)
18. [Line 521] "The more autonomous a reported system in this corpus, the less likely it is to have been tested outside simulation." → the gradient is not monotonic (Teleop 60%, Supervisory 75%, Shared 0%, FA 7.4%) → "Fully Autonomous systems were far less often field-tested than Teleoperation or Supervisory Control systems." The same "inverse relationship" wording appears at lines 605, 690, 696, and 740. Soften it everywhere to "a validation gap between Fully Autonomous and human-supervised modes". **→ stats-consistency-checker** to confirm the wording against the crosstab.
19. [Line 730] "A review organized around any axis other than autonomy would not surface this pattern" → unprovable → delete. It is already the fifth repetition (see item 50).
20. [Line 742] "This distinction is invisible to a review organized around platform type, sensor modality, or system architecture" → overclaim → "This distinction is easy to miss in a review organized around…"
21. [Line 605] "would not surface the inverse relationship" → "is unlikely to surface the gap between…"
22. [Line 690] "none of the reviewed prior works evaluate…" and "surfaces a pattern that a review organized by … would not reveal" → hedge: "To our knowledge, none of these reviews evaluates…" and "…that is not visible when the corpus is organized by…". Note that the novelty scan found uncited 2026 reviews (Shuvo et al.; *Applied Soft Computing* path-planning SLR).
23. [Line 676] "None of these reviews organizes its corpus primarily around how much autonomy…" → the novelty scan shows that [6] does code three autonomy bands → "None of these reviews uses autonomy/HRI mode as its primary organizing axis."
24. [Line 676] and Table I [Line 686]: "Bakzadeh et al. [6] … explicitly exclude autonomy and control software from their stated scope" / "Autonomy and control software explicitly excluded from scope" → the novelty scan found this a **mischaracterization**: [6] assigns A1/A2/A3 autonomy levels → use the scan's suggested rewrite. **→ citation-verifier**
25. [Line 686] Table I: "15 platforms" for [6]. The novelty scan reports 14 platforms (12/1/1). **→ citation-verifier / stats-consistency-checker**. I have not changed it.
26. [Line 695] "the most recent and most directly comparable prior review" → Shuvo et al. (Oct 2026) is more recent, according to the novelty scan → "the most directly comparable prior systematic review [4]".
27. [Line 740] "The results demonstrate that Fully Autonomous systems dominate current SAR robotics research" → this generalizes from 39 papers found through publisher portals → "Fully Autonomous systems dominate the reviewed corpus (69.2%)".
28. [Line 740] "indicating that naming a specific hazard type does not by itself guarantee…" → the 89.7% figure does not show this. The [25] example does → "…and, as [25] illustrates, naming a hazard does not guarantee that its physical conditions were modeled." Conclusions should avoid citations, so the alternative is "…suggesting that naming a hazard…"
29. [Line 621] "is not an artifact of a few weak papers pulling down an average. It holds up at the level of individual flagship examples." → examples cannot rule out an artifact → "Two flagship examples illustrate what the 7.4% figure means in practice." Cite the Fisher test from the novelty scan (p = 0.0056) if it is added to Results.
30. [Line 625] "The gap between 'Fully Autonomous' succeeding and failing in this corpus concentrates specifically in control and decision execution, not in perception." → generalizes from one paper ([47]) → "In [47], the shortfall lies in control and decision execution rather than perception."
31. [Line 599] "a figure the authors themselves describe as inadequate for safety-critical deployment" → the quote at line 625 is "modest for safety-critical applications", so "inadequate" overstates the source → "…a figure the authors describe as 'modest for safety-critical applications'."
32. [Line 637] "is a direct, evidenced finding rather than a speculative connection" → overconfident. The novelty scan reports p = 0.031 as borderline → "…is a descriptive pattern in this corpus."
33. [Line 637] "The platform receiving the most attention from the corpus's more autonomy-forward research" → UAV and UGV are tied at 9 FA papers each (Table VII). UAV leads only when the 3 Shared papers are counted → "UAVs, which account for 12 of the 30 Fully Autonomous and Shared-Collaborative papers, …" **→ stats-consistency-checker** to confirm the 12/30.
34. [Line 583] "is the corpus's clearest evidence for what well-designed supervisory HRI delivers operationally" → it rests on a mock-up study → "offers the corpus's clearest evidence on supervisory HRI benefits, from a mock-up study".
35. [Line 631] "slightly *higher*" (95.2% vs. 83.3%, a 12-point difference) → "higher, not lower".
36. [Line 672] "is well established in the SAR and disaster-robotics literature [2]" → one arXiv preprint does not support "well established" → "is widely recognized in SAR robotics [2]". Add a peer-reviewed source.
37. [Line 672] "Estimates … range from just over 20% in some assessments to more than 90% in others" → **no citation** → add a source or delete. "Virtually all sources agree…" is also uncited → "Sources agree on the shape, if not the numbers:".
38. [Line 670] "killing an estimated 2,200 people." → the Afghanistan figure has no citation → add [1] (Sourcing notes say CRED covers both earthquakes).
39. [Line 674] "an increasingly active area … over the past decade" → uncited trend claim. It is also a one-sentence paragraph → merge it into line 672 or 676 and cite [4], [5].

---

## 3. Internal contradictions and cross-reference errors

40. [S] [Line 605] "under a logged, precedent-based protocol (Section II-F)" → the precedent protocol is described in Section II-G (Data Extraction, line 375), not II-F (Screening) → "(Section II-G)".
41. [S] [Lines 595 vs. 601] Line 595 says the single-robot cluster's real-world validation is "markedly thinner … than the corpus average", but line 601 calls it "the cluster with the most real-world testing (single-robot navigation)" → these contradict each other. **→ stats-consistency-checker** should decide which is true. Do not edit before that check.
42. [S] [Lines 593 vs. 623] Line 593: "LiDAR pipeline produced enough false positives from grass and wind to cause 3 of 10 physical collisions". Line 623: "misreading long grass as obstacles and wind-shaken foliage as false negatives" → the error type differs between the two passages, and false positives alone would not cause collisions → make both match the [25] source. **→ citation-verifier**
43. [S] [Line 593] "success rates degrade sharply as swarm size grows beyond that one validated unit" → the degradation is from the 4- to 24-agent **simulation** (line 623), not growth beyond the one physical unit → "in simulation, success fell from 95.83% (4 agents) to 69.36% (24 agents)".
44. [S] [Line 587] "share a distinguishing feature not found in the Supervisory bucket: each treats the operator's own cognitive or psychological state as a first-class design and evaluation target" → [17], a Supervisory paper, measured operator workload, reaction time, and trust (line 583) → "…a feature that is central here but secondary in the Supervisory papers: …"
45. [S] [Line 587] "detection recall … as low as 2.6–26.4% mAP" → recall and mAP are different metrics → **→ stats-consistency-checker / citation-verifier** to confirm the metric in [20].
46. [S, rule 4] [Line 397] "only findings on which all three agreed were retained … disagreements were resolved through joint discussion" → this contradicts itself (consensus versus unanimity only). Separately, the Sec. 2.2 audit note and the Sec. 16 log record single-annotator screening and Google Scholar/AI-assisted identification. That contradicts lines 325, 371, 375, and 397 ("conducted independently by the three authors"). **Flag to the authors. Do not polish this text.** Truthful wording is needed, for example: "Records were identified through publisher portals, Google Scholar, and AI-assisted search (ChatGPT, Gemini); see the AI-use statement." The screening description should match what was actually done.
47. [M] [Line 676] Tong et al. [8] "falls outside both this review's 2025–2026 window and the 2016–2024 corpus in [4]" → a 2024 paper does not fall outside 2016–2024. In any case, [4]'s corpus is primary studies, not reviews → "…since it predates this review's 2025–2026 window and is not a structurally comparable peer."
48. [M] [Line 537] "This is addressed in the Discussion alongside the platform's 17.9% overall corpus share (Section III-B)." → Section V-C does not discuss the 17.9% → "Section V-C discusses this pattern."
49. [M] [Line 555] "One further pattern concerns the Discussion:" → the underground/teleoperation contrast never appears in Section V → "One further pattern stands out:", or add it to V-C.
50. [M] [Line 654] "documented in both Section IV-D's multi-robot cluster synthesis and [25]'s specific scalability results" → IV-D's degradation evidence is [25] itself, so it is counted twice → "documented in [25] (Section IV-D)".

---

## 4. Redundancy across sections

51. [M] The claim that a non-autonomy axis "would not surface" the gap appears at lines 605, 690, 730, 742, and implicitly 627 → keep it once in Section I (hedged, line 690) and once in Section IV-E. Delete it from the Abstract and soften it in the Conclusion.
52. [M] The three-author independence statement appears at lines 325, 371, 375, and 397 → this is subject to item 46. If it survives, state it once in II-F.
53. [M] The year restriction is explained at both line 349 and line 365 → keep line 365. Shorten line 349 to "Queries were restricted to publications from 2025 onward."
54. [M] "naming a hazard does not guarantee its physical conditions were modeled" appears at lines 633, 653, and 740 → keep it at 633. Shorten 653 to "(Section V-B)".
55. [m] [Line 436] repeats line 425 ("no human in the … control loop") → delete or merge (see item 1).
56. [m] [Line 521] "Fig. 6 presents this inverse relationship across the full four-way autonomy spectrum." → repeats the paragraph's first sentence, which already cites Fig. 6 → delete.
57. [m] [Line 648] "not from a generic list" repeats line 617 → delete.

---

## 5. Terminology and acronyms

58. [M] [Line 361] "whether teleoperated, shared-autonomy, supervisory, or fully autonomous" → does not match the taxonomy label → "…teleoperated, supervisory, shared-collaborative, or fully autonomous".
59. [M] [Lines 580, 626] "drone" ("a drone and a quadruped"; "AI-enhanced rescue drone") vs. "UAV" everywhere else → "UAV". Line 579's "caged-drone designs" → "caged-UAV designs".
60. [M] [Title, line 720] "Teleoperation, Human-Robot Collaboration, and Autonomous Approaches" → does not map onto the four modes (Supervisory is missing, and "Human-Robot Collaboration" is not a category). Consider "…A Systematic Review of Teleoperation, Supervisory, Shared, and Autonomous Control". The authors decide.
61. [m] [Line 587] "the Supervisory bucket"; [Line 377] "bucketing" → informal → "the Supervisory Control category"; "classifying".
62. [m] Category labels capitalized mid-sentence, inconsistently: [Line 506] "Partial validation", "Real-world field tests"; [Line 440] "Legged platforms"; [Line 471] "Visual-sensor finding" → either capitalize all labels consistently or lowercase them in running text. "Hybrid/Multi-Platform" (tables) vs. "hybrid multi-platform" (lines 730, 740) has the same problem.
63. [m] [Line 684] Table I, this-review scope "UAV/UGV/legged/UUV" → the corpus label is "UUV/USV", and hybrid systems are also included → "UAV/UGV/legged/UUV/USV/hybrid".
64. **Acronyms defined twice:**
    - [M] SAR: Intro line 668 (first use in paper order), then Methods line 309, then Conclusion line 738. Drop the later two.
    - [M] HRI: Intro line 676, inside nested parentheses "(Human-Robot Interaction (HRI), Perception, …)" → define it earlier in line 676 ("human-robot interaction (HRI)") and remove the nested form. It is defined again at lines 313 and 738.
65. **Defined but barely used:**
    - [m] SLR (line 309, used once) → delete the acronym.
    - [m] RSAR (lines 672, 674, 730), while the rest of the paper says "SAR robotics" → drop RSAR.
66. **Undefined at first use** [M]:
    - UAV/UGV (line 676) and UUV/USV (line 440)
    - PRISMA (line 309; expand once: Preferred Reporting Items for Systematic Reviews and Meta-Analyses)
    - IoT (359), LiDAR and IMU (471), GPS (480), RF (485)
    - YOLOv8 (a model name, acceptable), mAP (579), DARPA and SubT (583, 595), LLM, EEG, and 2D (587), DRL and TAEMS (593), GNSS (593)
    - MPC, SLAM, and AMCL (595), MLLM (599; "multimodal-LLM-driven" never defines it), LoRa (599)
67. [m] [Line 625] "the reported RQ1/RQ2 experiments" → readers will confuse these with this review's RQ1–RQ4 → "the paper's reported experiments".

---

## 6. Grammar, punctuation, spelling, and sentence clarity

68. [M] [Line 309] "was conducted between 18–19 July 2026" → "between … –" is ungrammatical, and the date format clashes with "March 28, 2025" (line 670). The whole review was not done in two days. Rule 4 also applies → "Screening was conducted on July 18–19, 2026."
69. [M] [Line 371] "(18–19 July 2026)" → "(July 18–19, 2026)" (IEEE/American date format).
70. [m] Spelling (IEEE uses American): "catalogued" (lines 325, 343, 345, 365, 395), "catalogue" (line 353) → "cataloged" / "catalog". "Centre" is a proper name; keep it. "Synthesising" in [9]'s title is as published; keep it.
71. [m] [Line 315] "and how is this distributed across the corpus?" → "and how are these modes distributed across the corpus?"
72. [M] [Line 359] "as its primary stated application (…) as the paper's primary framing rather than…" → "primary" is doubled → "…as its primary stated application (…), rather than as a cited example or future-work mention."
73. [M] [Line 363] The "For example, needs-assessment studies …" sentence runs about 60 words → "For example, Rajashekhar and Prabhakar [9] was excluded: it combines a literature review, a public survey, and first-responder interviews but neither presents nor tests a robotic system."
74. [m] [Line 365] "no record was screened against and failed a publication-year test" → "no record failed a publication-year test at screening."
75. [M] [Line 369] "papers whose abstracts mention 'search and rescue' once or twice in the introduction" → abstracts do not have introductions → "papers that mention SAR once or twice in the abstract or introduction". The second sentence is about 110 words; split it after "past the abstract."
76. [M] [Line 369] "read in its entirety (methodology, results, and conclusion, not the abstract alone)" → the parenthesis lists only parts of the paper, which contradicts "in its entirety" → "read in full, not the abstract alone".
77. [m] [Line 369] "a subjective user-survey" → "a subjective user survey" (a noun phrase takes no hyphen).
78. [m] [Line 371] "avoiding re-litigating a paper that resurfaces" → informal → "avoiding reassessing a paper that reappears".
79. [M] [Line 375] the "Borderline classification decisions…" sentence is about 95 words → split it after "supervisory interface)". Put the precedents in a supplement.
80. [M] [Line 377] about 120 words in one sentence → use a list or split it per field. Also: "to avoid the great majority of machine-learning-based papers defaulting to a 'hybrid' label" → "so that offline training alone did not make a paper 'hybrid'".
81. [m] [Line 377] "eleven sensor categories" → Table VIII has 11 rows including "None (fully abstracted)", which is not a sensor category → "ten sensor categories plus a 'none' flag". **→ stats-consistency-checker**
82. [m] [Line 353] "removed prior to screening" → "removed before screening".
83. [m] [Line 395] "because 12 of the excluded records violated more than one criterion, the per-criterion counts … sum to more than 86" → 63 + 28 + 7 = 98, and 98 − 86 = 12 only if no record violated all three criteria. **→ stats-consistency-checker**
84. [m] [Line 457] "shows autonomy is not evenly distributed" → "shows that autonomy mode is not evenly distributed". Also "never appears on a bare UAV platform" → "never appears on a UAV-only platform".
85. [m] [Line 471] "A notable quarter of the corpus" → "A quarter of the corpus". "This pairs with the Visual-sensor finding:" is unclear → "Thus, alongside sensor-driven perception work, …"
86. [m] [Line 493] "A quarter of papers (10, 25.6%)" repeats line 471's "a quarter" → "Ten papers (25.6%)".
87. [m] [Line 506] "followed by Partial validation, simulation combined with limited real-world testing (10, 25.6%)" → the appositive is ambiguous → "followed by partial validation (simulation plus limited real-world testing; 10, 25.6%)".
88. [M] [Line 537] "the opposite of what their smaller sample size alone would suggest" → a small sample does not predict a direction → delete.
89. [m] [Line 541] "and Wildfire/Fire and one other single-occurrence hazard for 1 paper each (2.6%)" → awkward. A reviewer will ask what "Other" is → name the hazard (possibly volcanic, [39]; UNVERIFIED). **→ stats-consistency-checker**
90. [m] [Line 569] "elaborating the technical approaches" → "describing the technical approaches".
91. [m] [Line 579] "([14], [11], [12])" → out of numeric order → "[11], [12], [14]".
92. [m] Global: citations wrapped in parentheses, "([10])" (lines 579, 583, 593–599) → IEEE style is a bare "[10]".
93. [m] Global: sentences that open with "[17]'s", "[18]'s", "[19] has", "[25]'s", "[47] illustrates" (lines 583, 587, 593, 599, 623, 633) → IEEE style uses "Ruan et al. [17]…" or "In [17], …".
94. [M] [Line 583] the [18] sentence runs about 70 words with nested commas → "[18] responds to a real constraint of wilderness SAR: flights are often cut short by weather, battery, or terrain. Its planner searches high-probability regions first, so an interrupted flight still covers most of the high-value area."
95. [M] [Line 593] "Only one of the twelve, [25]'s curriculum-learning multi-UGV policy, which specifically replaces…, reports…, and even there…; the paper's own results note…, and its real-world LiDAR pipeline…" → overlong (about 85 words) → split it into three sentences.
96. [m] [Line 595] "simulation-only or MATLAB-only validation" → MATLAB-only is a kind of simulation-only → "simulation-only validation (including MATLAB-only)".
97. [M] [Line 599] the [47] sentence runs about 80 words → split it at "…safety-critical deployment." and "Although the authors' Discussion…".
98. [m] [Line 601] "this corpus's most explicit authors'-own admission" → the punctuation is malformed → "the corpus's most explicit admission by its own authors".
99. [m] [Line 605] "None … resolve" (plural); line 676 "None … organizes" (singular); line 690 "none … evaluate" → pick one number. Singular is preferred in IEEE style.
100. [M] [Line 623] "Read together, [25] is best described as…" → a dangling modifier ("read together" with only one paper) → "Taken together, these results show that…"
101. [m] [Line 623] The paragraph is about 230 words → split it at "A further result…".
102. [m] [Line 625] The 45-word direct quote from [20] → shorten to the key clause and paraphrase the rest (rule 5).
103. [M] [Line 627] "One plausible reading of that omission … is that a taxonomy that never isolates full autonomy as its own category also has no natural place to ask how rigorously it was validated as a category, the question this review's…" → convoluted → "Because [4] has no Fully Autonomous category, it cannot compare validation rigor by autonomy level. The four-way taxonomy makes that comparison possible."
104. [m] [Lines 633, 637] "this data" → "these data" (IEEE treats "data" as plural). Line 537's "data alone" is fine.
105. [m] [Line 637] "This is not an isolated statistic." → throat-clearing → delete.
106. [M] [Line 637] Final sentence is about 75 words → split it after "alone."
107. [m] [Line 643] "applied to their full corpus" → "their" lacks a clear plural antecedent → "which [4] applied to its full corpus".
108. [m] [Line 668] "These figures sit below the 2005–2024 annual average (…), a reduction CRED attributes to…; the cumulative burden … remained consistent…" → about 70 words → split it after the parenthesis.
109. [m] [Line 670] "a 7.7-magnitude earthquake", "a 6.0-magnitude earthquake" → standard form is "a magnitude 7.7 earthquake".
110. [m] [Line 672] "Estimates of the proportion of survivors located alive by roughly the 72-hour mark" → ambiguous → "Estimates of the share of trapped people rescued alive within about 72 hours".
111. [M] [Line 676] "a systematic review of 74 SAR robotics papers published between 2016 and 2024 in *IEEE Access*" → reads as if the 74 papers appeared in IEEE Access → "a systematic review, published in *IEEE Access*, of 74 SAR robotics papers from 2016–2024". The paragraph is about 300 words; split it per prior review.
112. [m] [Line 676] "Sinha et al. [5] reviewed … but restrict" → tense mismatch → "review … but restrict".
113. [m] [Line 676] "An earlier, narrower review by Tong et al. [8] … predating all four of the above" → "earlier" and "predating" say the same thing → drop "predating all four of the above".
114. [m] [Line 678] "Table I summarizes these differences directly." → one-sentence paragraph → append it to line 676.
115. [m] [Line 692] "In particular, the main contributions of this review can be summarized as follows:" → "The main contributions of this review are as follows:"
116. [m] [Line 695] "the period immediately following, with zero temporal overlap, the most recent and most directly comparable prior review's own 2016–2024 corpus" → the interruption makes it hard to parse → "covering 2025–2026, immediately after the 2016–2024 corpus of [4], with no temporal overlap".
117. [m] [Lines 730, 738] "screened under PRISMA 2020 guidelines" / "synthesizing … under PRISMA 2020 guidelines" → PRISMA is a reporting guideline → "reported according to PRISMA 2020".
118. [m] [Line 740] "field-tested outside simulation" → redundant → "field-tested". "This pattern recurs at the platform level" → it is a different crosstab → "A similar gap appears at the platform level".
119. [m] Number style is mixed: "three of the five" (line 579) vs. "3 of 4" (line 521) vs. "5 of 7" (line 597) → use numerals for counts with denominators throughout.
120. [m] [Line 335] "PLOS One" (also lines 325 and 336) → the official title is "PLOS ONE".
121. [m] [Lines 325, 335] "ten sources" mixes publishers (MDPI, Springer) with journals (Scientific Reports, PLOS ONE), and Springer and Scientific Reports overlap → "ten publisher or journal portals".

---

## 7. Captions and tables

122. [m] [Lines 343, 345] Fig. 1: "DOI-verified by publisher" → ambiguous (verified by whom?) → "…grouped by publisher (N = 130 cataloged records)."
123. [M] [Lines 533, 535] Fig. 6 caption: "…, this review's clearest evidenced pattern (Section V-A)." → self-promotion in a caption → "Fig. 6. Real-world field-validation rate by Autonomy/HRI mode."
124. [m] [Line 473] Table VIII caption "(multi-select; N = 39, non-exclusive)" → "multi-select" and "non-exclusive" say the same thing → "(multi-select; N = 39)".
125. [m] Table XI (line 525) column order (Sim, Real-world, Partial, Bench) differs from Table X (Sim, Partial, Real-world, Bench). Table VII (line 461) column order differs from Table VI → use the same order. This changes no values.
126. [m] [Line 571] The Fig. 7 image comes before its first text mention (line 575) → put the image after line 575.

---

## 8. Bibliography format (Sec. 15, lines 810–904)

127. [S] The entire list is in APA style ("Delforge, D., … (2026). 'Title.' *Journal*, vol, pages."). IEEE needs "D. Delforge, R. Below, …, 'Title,' *Journal*, vol. X, no. Y, pp. A–B, Mon. Year, doi: …" → convert all 48 entries when the submission file is built. This changes no content.
128. [M] Single-page numbers where IEEE needs a range: [33] "13, 2981"; [37] "26(9), 13775"; [45] "25(6), 8655"; [18] has no pages → **→ citation-verifier**
129. [M] Missing DOIs: [9] (and its author format "Rajashekhar V S, &" is malformed) and [3] (no URL or date). The novelty scan already recommends replacing [3] → **→ citation-verifier**
130. [m] Volume and year look mismatched: [29] "(2025) … *Information*, 17(1)"; [43] "(2025) … *Applied System Innovation*, 9(1)" → probably online-first papers dated December 2025. **→ citation-verifier** to confirm.
131. [m] [9]'s title capitalizes "post-Earthquake" → check against the published title. **→ citation-verifier**

---

## 9. Proposed Abstract (238 words; every number unchanged)

> Robotic search and rescue (SAR) systems can locate and assist survivors in disaster environments that are too hazardous for human responders. This systematic review, reported according to PRISMA 2020, analyzes 39 papers published in 2025–2026, selected from 130 candidate records. Prior reviews organize this literature by system architecture, platform type, or research method. This review instead classifies every included system under a four-way autonomy/human-robot interaction (HRI) taxonomy (Teleoperation, Supervisory Control, Shared-Collaborative Control, and Fully Autonomous) and resolves each paper to a single primary category with an explicit, precedent-based classification protocol. Fully Autonomous systems dominate the corpus (69.2%), followed by Teleoperation (12.8%), Supervisory Control (10.3%), and Shared-Collaborative Control (7.7%). Cross-tabulating autonomy mode against validation type reveals a validation gap: only 7.4% of Fully Autonomous systems were field-tested in real-world conditions, compared with 60–75% of Teleoperation and Supervisory Control systems. To our knowledge, this gap has not been quantified in prior SAR reviews. A related platform-level mismatch emerges: only 7.7% of unmanned aerial vehicle (UAV)-based systems were field-tested, versus 57.1% of hybrid multi-platform systems. In addition, 89.7% of the corpus reports an environmental-realism limitation, whether the tested scenario names a specific hazard or a generic disaster environment. The review covers the 2025–2026 period immediately after the most recent structurally comparable review (2016–2024 corpus) and grounds its gap analysis in the included papers' own reported limitations. These findings suggest that current Fully Autonomous SAR systems demonstrate research-stage rather than field-ready capability.

Changes: fixes the "more human-involved modes" scope error (item 17), hedges the novelty claim (item 15), removes the unprovable "any other axis" sentence (item 19), replaces "screened under PRISMA" (item 117), and drops RSAR (item 65). If "precedent-based" is retired (item 13), replace it with "rule-based".

---

## 10. Structural notes (not sentence-level; for the caller)

- Discussion V-A lacks the required **mechanism → implication** steps. It gives the finding and flagship examples but never says why FA work is under-validated (hardware cost, safety and regulatory barriers, and the ease of simulation benchmarks; V-C does this for UAVs) or what practitioners should do. Add 2–3 sentences.
- Limitations V-D has only two bullets. The missing limitations include the publisher-portal search with two terms and no Scopus/WoS, AI-assisted identification, the screening process (rule 4), no inter-rater κ, no protocol registration, and small cell sizes in Tables VII and XI. → methodology-auditor
- Table I omits Tong et al. [8] (discussed in the text) and the uncited 2026 reviews found by the novelty scan. → literature-scout
