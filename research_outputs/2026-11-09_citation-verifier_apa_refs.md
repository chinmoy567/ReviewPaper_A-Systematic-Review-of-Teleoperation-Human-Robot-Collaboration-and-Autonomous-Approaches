# Citation verification of the 72 APA reference entries (2026-11-09)

*The citation-verifier agent was not permitted to write report files. The main session saved this file from the agent's final message, condensed but unaltered in substance. The agent edited only `data/references.py`.*

## Method
Every DOI was checked against the Crossref API (authors, title, journal, volume, issue, pages or article number, dates). PubMed was used for de Bruycker 1983, Kaya Özdoğan 2025 and both Macintyre papers. The CRED PDF itself was read for [1]. Wiley, MDPI, ScienceDirect and Taylor & Francis pages returned 403, so those entries were checked through Crossref only.

## In-text change needed
- [43] Srijiranon et al.: the year changes from 2025 to 2026. The paper is in *Applied System Innovation* 9(1), the January 2026 issue (online 28 Dec 2025). This follows the volume-year convention already used for Bedi [29] and Yeoh [39].

## Corrections made in `data/references.py`
- **de Bruycker 1983:** full author list (8) taken from PubMed 6609007; PMC URL added (the paper has no DOI).
- **Kaya Özdoğan 2025:** full author list (7) taken from PubMed 40211639. Journal name changed to the Crossref English title, *Turkish Journal of Trauma and Emergency Surgery*.
- **Hu 2026:** Hu, Q., Komagata, T., Kanbara, S., Yu, T., & Jiang, Y. The Japanese surname-first reading was inferred, because Crossref swaps given and family names. The title colon is UNVERIFIED.
- **Jamwal & Singh 2026:** Jamwal, H. D. S., & Singh, S.
- **Chen, Rushworth & Jia 2026:** Chen, T., Rushworth, A., & Jia, F. "SLAM" is spelled out in the title, as Crossref gives it.
- **Man et al. 2026:** Man, S. S., Jiang, X., Zhou, S., Tong, M., & Chan, A. H. S. The family name is "Man", per the publisher metadata.
- **Delmerico 2019:** full list of 13 authors.
- **Afzal 2021:** pages 263–274.
- **Cruz Ulloa 2026:** volume 6 inferred from other articles in the same issue (Crossref lists no volume).
- **[45]:** pages 8655–8666. **[37]:** pages 13775–13784. **[33]:** pages 2981–2997.
- **Issue numbers added:** [7], [16], [31] 14(11); [20] 6(10); [36] 9(8); [19] 11(10); [23] 12(1); [48] 8(4).

## Still UNVERIFIED (authors to confirm)
- [9]: Crossref gives family name "V S", given name "Rajashekhar".
- [45]: Crossref and IEEE give family name "V", given name "Gowry Sailaja".
- [48]: Crossref lists "R, Vani", "K, Lalitha" and "Venkatesh, Prasanna".
- Year conventions: Khalil (volume 204 is dated Jan 2027) and Yeoh (online Dec 2025).

## Status
- **Verified with no change:** [1], 4, 5, 6, 8, 10–15, 17, 18, 21, 22, 24–30, 32, 34, 35, 38–42, 44, 47; Page, Rethlefsen, Cohen, Gwet, Wilson, Parasuraman, Endsley & Kaber, Beer, Huang (ALFUS), Murphy, Macintyre 2006 and 2011, Shuvo, Khalil, Zhang, Salvato, Zhao.
- **Catalogue-level only:** Sheridan & Verplank 1978.
- **Not found:** none.

## Claim spot-check
- **Supported:** CRED figures; de Bruycker; Kaya Özdoğan; Macintyre 2006 and 2011; Hu; Jamwal & Singh; Man; Zhang; Chen; Delmerico; Zhao; Salvato.
- **CRED wording:** "not to any decline in underlying risk" is an inference, not CRED's wording. Soften it.
- **Shuvo:** the paper says many studies are "heavily dependent on controlled experimental settings", not "most validated in simulation". Soften the manuscript wording.
- **Sinha [5]:** reports "experimental field studies" at 14.7% (28) and "full field deployments" at 4.2% (8). The manuscript's 15.4%/23.1% vs 4.2% comparison should name the matching category.
- **Bakzadeh [6]:** platform details checked against the abstract only in this pass; the full-text check was done earlier.
- **Not checked:** Khalil and Afzal (no abstract retrievable).
