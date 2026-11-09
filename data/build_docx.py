"""Build the Journal of Field Robotics free-format submission (.docx) fresh from the master document.

Reading order (JFR main-text order): title, authors, affiliations, [acknowledgments/statements],
abstract + keywords, I-VI, references, then back-matter statements.
Run: python data/build_docx.py  -> submission/JFR_submission_manuscript.docx
"""
import re, os
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

SRC = "SAR_review_master_document.md"
OUT = "submission/JFR_submission_manuscript.docx"
s = open(SRC, encoding="utf-8").read()


def section(a, b):
    i = s.index(a); return s[i:s.index(b, i)]


front = section("### TITLE AND AUTHORS", "## 15.")
title_block, rest = front.split("### ABSTRACT", 1)
abstract_block, rest = rest.split("### VI. CONCLUSION", 1)
conclusion_block, back_block = rest.split("### BACK MATTER", 1)
body = [section("### I. INTRODUCTION", "### Sourcing notes"), section("### II. METHODOLOGY", "## 10."),
        section("### III. RESULTS", "## 11."), section("### IV. TAXONOMY", "## 12."), section("### V. DISCUSSION", "## 13."),
        "### VI. CONCLUSION" + conclusion_block]
refs = section("### Reference list for the manuscript", "\n## 16.")
refs = refs.split("\n\n", 2)[2]  # drop heading + note paragraph

doc = Document()
st = doc.styles["Normal"]; st.font.name = "Times New Roman"; st.font.size = Pt(11)
INLINE = re.compile(r"(\*\*\*[^*]+\*\*\*|\*\*[^*]+\*\*|\*[^*\s][^*]*\*)")


def add_runs(p, text):
    text = text.replace("\\*", "*").replace("US\\$", "US$")
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("***"):
            r = p.add_run(part[3:-3]); r.bold = r.italic = True
        elif part.startswith("**"):
            r = p.add_run(part[2:-2]); r.bold = True
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            r = p.add_run(part[1:-1]); r.italic = True
        else:
            p.add_run(part)


def render(md):
    lines = md.strip("\n").split("\n"); i = 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip() or ln.strip() == "---":
            i += 1; continue
        if ln.startswith("### "):
            doc.add_heading(ln[4:].strip(), level=1); i += 1; continue
        if ln.startswith("#### "):
            doc.add_heading(ln[5:].strip(), level=2); i += 1; continue
        m = re.match(r"!\[(.*?)\]\((.*?)\)", ln)
        if m:
            if os.path.exists(m.group(2)):
                doc.add_picture(m.group(2), width=Inches(6.0))
                doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
            i += 1
            if i < len(lines) and not lines[i].strip():
                i += 1
            if i < len(lines) and lines[i].startswith("*Fig."):
                p = doc.add_paragraph(); add_runs(p, lines[i].strip().strip("*")); p.runs[0].bold = False
                i += 1
            continue
        if ln.startswith("|"):
            tbl = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[-| :]+\|$", lines[i].strip()):
                    tbl.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            ncol = max(len(r) for r in tbl)
            t = doc.add_table(rows=len(tbl), cols=ncol); t.style = "Table Grid"
            for r, row in enumerate(tbl):
                for c in range(ncol):
                    cell = t.cell(r, c); cell.text = ""
                    add_runs(cell.paragraphs[0], row[c] if c < len(row) else "")
                    for run in cell.paragraphs[0].runs:
                        run.font.size = Pt(9)
                        if r == 0:
                            run.bold = True
            doc.add_paragraph()
            continue
        m = re.match(r"^(\s*)(- |\d+\. )(.*)", ln)
        if m:
            style = "List Bullet" if m.group(2) == "- " else "List Number"
            if len(m.group(1)) >= 2:
                style += " 2"
            p = doc.add_paragraph(style=style); add_runs(p, m.group(3)); i += 1; continue
        para = [ln.strip()]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||!\[|\s*- |\s*\d+\. |---)", lines[i]):
            para.append(lines[i].strip()); i += 1
        p = doc.add_paragraph(); add_runs(p, " ".join(para))


# Title page
tb = title_block.replace("### TITLE AND AUTHORS", "").strip().split("\n")
tb = [l for l in tb if l.strip() and l.strip() != "---"]
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(tb[0].strip("* ")); r.bold = True; r.font.size = Pt(16)
for l in tb[1:]:
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; add_runs(p, l.strip())
doc.add_heading("Abstract", level=1)
render(abstract_block)
for b in body:
    render(b)
doc.add_heading("References", level=1)
for e in [x for x in refs.strip().split("\n\n") if x.strip()]:
    p = doc.add_paragraph(); p.paragraph_format.left_indent = Inches(0.4); p.paragraph_format.first_line_indent = Inches(-0.4)
    add_runs(p, e.strip())
doc.add_heading("Statements", level=1)
render(back_block.replace("**Acknowledgments.**", "**Acknowledgments.**"))
os.makedirs("submission", exist_ok=True)
doc.save(OUT)
print("saved", OUT)
