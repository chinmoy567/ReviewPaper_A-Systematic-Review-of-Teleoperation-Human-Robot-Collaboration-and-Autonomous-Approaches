"""PRISMA 2020 flow diagram (two identification routes) for the SAR review.

Counts come from assets/docs/paperlinks.xlsx ("How it was found") and
supplementary/screening_log.csv; see master doc Sec. 16, 2026-11-08 entry.
Never use the numbers in assets/prisma/ (old, uncorrected split).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = "assets/figures/prisma_diagram_v2.png"

fig, ax = plt.subplots(figsize=(16, 14.5))
ax.set_xlim(0, 160)
ax.set_ylim(0, 145)
ax.axis("off")

EDGE = "#333333"


def box(x, y, w, h, text, fs=11.5, fc="white", ec=EDGE, bold=False, ha="center", rot=0, lw=1.8):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=1.2",
                                fc=fc, ec=ec, lw=lw))
    tx = x + w / 2 if ha == "center" else x + 1.8
    ax.text(tx, y + h / 2, text, ha=ha, va="center", fontsize=fs, rotation=rot,
            fontweight="bold" if bold else "normal", linespacing=1.35)


def arrow(x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", lw=1.8, color=EDGE, mutation_scale=16))


# headers
box(14, 136, 84, 7, "Identification of studies via publisher-platform searches", fs=13, fc="#F3A93E", ec="#F3A93E", bold=True)
box(104, 136, 54, 7, "Identification via other methods", fs=13, fc="#C9C9C9", ec="#C9C9C9", bold=True)

# phase labels
for y, h, t in [(104, 30, "Identification"), (22, 79, "Screening"), (2, 17, "Included")]:
    box(1, y, 9, h, t, fs=13, fc="#DCE6F2", ec="#7EA1C9", bold=True, rot=90)

# --- left column: publisher platforms
box(14, 106, 40, 27,
    "Records identified from publisher\nplatforms (n = 78):\n"
    "   MDPI (n = 34)\n   Elsevier ScienceDirect (n = 20)*\n   Scientific Reports (n = 8)\n"
    "   PLOS One (n = 6)\n   IEEE Xplore (n = 5)\n   Frontiers (n = 4)\n   Wiley (n = 1)",
    fs=10.5, ha="left")
box(60, 113, 38, 13, "Records removed before screening:\n   Duplicate records (n = 1)", fs=10.5, ha="left")
arrow(54, 119.5, 60, 119.5)

box(14, 88, 40, 10, "Records screened\n(n = 77)")
box(60, 88, 38, 10, "Records excluded before\nfull-text review (n = 0)", fs=10.5)
arrow(34, 106, 34, 98)
arrow(54, 93, 60, 93)

box(14, 72, 40, 10, "Reports sought for retrieval\n(n = 77)")
box(60, 72, 38, 10, "Reports not retrieved\n(n = 0)", fs=10.5)
arrow(34, 88, 34, 82)
arrow(54, 77, 60, 77)

box(14, 50, 40, 10, "Reports assessed for eligibility\n(n = 77)")
box(58, 42, 42, 25,
    "Reports excluded (n = 59);\ncriteria non-exclusive:\n   Not disaster SAR domain (C1, n = 42)\n"
    "   No active robotic SAR role (C2, n = 21)\n   No empirical evaluation (C3, n = 3)\n"
    "   (7 records violate two criteria)", fs=10, ha="left")
arrow(34, 72, 34, 60)
arrow(54, 55, 58, 55)

# --- right column: other methods
box(104, 106, 54, 27,
    "Records identified from:\n   Google Scholar (n = 15)\n   AI-assisted discovery (n = 37):\n"
    "      ChatGPT (n = 34)\n      Gemini (n = 3)\n\nEach AI-suggested record was\nretrieved and checked at the publisher",
    fs=10.5, ha="left")
box(104, 92, 54, 9, "Duplicate records removed (n = 4)", fs=10.5)
arrow(116.5, 106, 116.5, 101)

box(104, 72, 25, 14, "Reports sought\nfor retrieval\n(n = 48)", fs=10.5)
box(133, 72, 25, 14, "Reports not\nretrieved\n(n = 0)", fs=10.5)
arrow(116.5, 92, 116.5, 86)
arrow(129, 79, 133, 79)

box(104, 50, 25, 12, "Reports assessed\nfor eligibility\n(n = 48)", fs=10.5)
box(133, 42, 25, 25,
    "Reports excluded\n(n = 27); non-\nexclusive:\n C1 (n = 21)\n C2 (n = 7)\n C3 (n = 4)\n(5 records violate\ntwo criteria)", fs=10, ha="left")
arrow(116.5, 72, 116.5, 62)
arrow(129, 56, 133, 56)

# included
box(14, 4, 84, 12, "Studies included in review (n = 39)\n18 via publisher platforms; 21 via other methods", fs=12)
arrow(34, 50, 34, 16)
arrow(116.5, 50, 98, 12)

ax.text(14, 0.2, "*Includes 2 Tech Science Press records retrieved through the ScienceDirect interface. "
        "Total records identified: 130; unique records after deduplication: 125.",
        fontsize=9.5, style="italic")

fig.savefig(OUT, dpi=150, bbox_inches="tight", facecolor="white")
print("saved", OUT)
