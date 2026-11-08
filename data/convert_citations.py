"""Convert numbered [n] and [@key] citations in the manuscript sections of the master document
to APA author-date, and write the APA reference list into Sec. 15. One-off; run once.
"""
import re, sys
sys.path.insert(0, "data")
from references import REFS, cite_paren, cite_narr, sort_key

P = "SAR_review_master_document.md"
s = open(P, encoding="utf-8").read()
REG = [("### II. METHODOLOGY", "## 10."), ("### III. RESULTS", "## 11."), ("### IV. TAXONOMY", "## 12."),
       ("### V. DISCUSSION", "## 13."), ("### I. INTRODUCTION", "### Sourcing notes"), ("### TITLE AND AUTHORS", "## 15.")]

PRE = [
 ("Sheridan and Verplank introduced that continuum as a ten-level scale running from full human control to full computer autonomy [@sheridan1978].",
  "Sheridan and Verplank (1978) introduced that continuum as a ten-level scale running from full human control to full computer autonomy."),
 ("Parasuraman, Sheridan, and Wickens separated automation", "Parasuraman et al. (2000) separated automation"),
 ("each of which can be automated to a different degree [@parasuraman2000].", "each of which can be automated to a different degree."),
 ("Endsley and Kaber showed", "Endsley and Kaber (1999) showed"), ("situation awareness, and workload [@endsley1999].", "situation awareness, and workload."),
 ("Beer, Fisk, and Rogers carried", "Beer et al. (2014) carried"), ("which agent senses, plans, and acts [@beer2014].", "which agent senses, plans, and acts."),
 ("In rescue robotics specifically, Murphy identified", "In rescue robotics specifically, Murphy (2004) identified"),
 ("team structure as the central HRI problems [@murphy2004].", "team structure as the central HRI problems."),
 ("Bakzadeh et al. grouped mine-rescue platforms into three autonomy bands derived from the Sheridan–Verplank scale [6].",
  "Bakzadeh et al. (2026) grouped mine-rescue platforms into three autonomy bands derived from the Sheridan–Verplank scale."),
 ("Cohen's κ = 0.79, 95% CI 0.61–0.97 [@cohen1960kappa]; Gwet's AC1 = 0.88 [@gwet2008ac1])",
  "Cohen's κ = 0.79, 95% CI 0.61–0.97 [Cohen, 1960]; Gwet's AC1 = 0.88 [Gwet, 2008])"),
 ("**Jamwal and Singh** compared", "**Jamwal and Singh (2026)** compared"),
 ("a principal barrier to field deployment [@jamwal2026].", "a principal barrier to field deployment."),
 ("**Shuvo et al.** synthesized", "**Shuvo et al. (2026)** synthesized"),
 ("validated in simulation or controlled settings [@shuvo2026].", "validated in simulation or controlled settings."),
 ("**Man et al.** reviewed", "**Man et al. (2026)** reviewed"), ("a single interaction mode [@man2026].", "a single interaction mode."),
 ("Two of the five, [13] and [14], explicitly", "Two of the five [13], [14] explicitly"),
 ("For example, [25] reached", "For example, Mead et al. (2026) reached"),
 ("(12 studies: [22]–[33])", "(12 studies)"), ("(7 studies: [34]–[40])", "(7 studies)"),
 ("(5 studies: [41]–[45])", "(5 studies)"), ("(3 studies: [46]–[48])", "(3 studies)"),
]

TOK = r"\[(?:\d+|@[A-Za-z0-9_]+)\]"
SEQ = re.compile(r"(\()?(" + TOK + r"(?:(?:, | and )" + TOK + r")*)(\))?")
NARR_BEFORE = re.compile(r"(^|\n|\*\*|- |\. |\bIn |\bin |\bof |\bby |\band |\bis |\bthan |\bfrom |\bwith |\bfollowing )$")


def key(t):
    t = t.strip("[]")
    return t[1:] if t.startswith("@") else int(t)


def convert(txt):
    out, i = [], 0
    for m in SEQ.finditer(txt):
        out.append(txt[i:m.start()]); i = m.end()
        lp, body, rp = m.group(1), m.group(2), m.group(3)
        keys = [key(t) for t in re.findall(TOK, body)]
        before = "".join(out)[-40:]
        if len(keys) == 1 and not lp:
            k = keys[0]; a = REFS[k][0]
            if before.rstrip().endswith(a) or before.rstrip().endswith(a.replace(" and ", " & ")):
                out.append(f"({REFS[k][1]})"); out.append(rp or ""); continue
            if NARR_BEFORE.search(before):
                out.append(cite_narr(k)); out.append(rp or ""); continue
        keys = sorted(dict.fromkeys(keys), key=lambda k: (REFS[k][0].lower().replace("s. you", "you s").replace("f. you", "you f"), REFS[k][1]))
        grp = "; ".join(cite_paren(k) for k in keys)
        if lp and rp:
            out.append(f"({grp})")
        else:
            out.append((lp or "") + f"({grp})" + (rp or ""))
    out.append(txt[i:])
    return "".join(out)


used = set()
for a, b in REG:
    x = s.index(a); y = s.index(b, x); seg = s[x:y]
    for o, n in PRE:
        seg = seg.replace(o, n)
    used |= {key(t) for t in re.findall(TOK, seg)}
    used |= {k for k, v in REFS.items() if f"{v[0]} ({v[1]})" in seg}
    seg = convert(seg)
    s = s[:x] + seg + s[y:]

# also count narrative-only cites introduced by PRE
for k in ["sheridan1978", "parasuraman2000", "endsley1999", "beer2014", "murphy2004", "cohen1960kappa", "gwet2008ac1", "jamwal2026", "shuvo2026", "man2026", 6, 25, 13, 14]:
    used.add(k)
bib = "\n\n".join(REFS[k][2] for k in sorted(used, key=sort_key))
block = ("\n### Reference list for the manuscript (APA author-date, *Journal of Field Robotics*), 2026-11-08\n\n"
         "Supersedes the numbered list above for the manuscript (the numbered list is kept as the working record). "
         "In-text citations in Secs. 9–14 use these author-date forms. Entries marked UNVERIFIED must be completed from the DOI/PubMed record before submission.\n\n"
         + bib + "\n")
z = s.index("\n## 16. Revision log")
s = s[:z] + block + s[z:]
open(P, "w", encoding="utf-8").write(s)
print(len(used), "references in list")
