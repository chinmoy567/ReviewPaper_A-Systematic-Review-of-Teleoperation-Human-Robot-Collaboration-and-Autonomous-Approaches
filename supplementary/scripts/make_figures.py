"""Regenerate Figs. 4-7 from data/extraction_table.csv (run: python data/make_figures.py).
Palette: validated categorical slots blue #2a78d6 (strict / primary) and orange #eb6834 (lenient),
lenient bars also hatched so the figure survives greyscale printing.
"""
import csv, collections, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

rows = list(csv.DictReader(open("data/extraction_table.csv", encoding="utf-8")))
BLUE, ORANGE, INK, MUTED, GRID = "#2a78d6", "#eb6834", "#0b0b0b", "#52514e", "#e4e3df"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED})
FIELD = "Real-world field test"


def wilson(k, n, z=1.959964):
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0, c - h) * 100, min(1, c + h) * 100


def clean(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="x", color=GRID, lw=0.8); ax.set_axisbelow(True)


# Fig. 4 sensor prevalence (horizontal bars, single series)
labels = [("s_visual", "Visual"), ("s_lidar", "LiDAR/range"), ("s_imu", "IMU/proprioceptive"), ("s_none", "None (idealized simulation)"),
          ("s_gps", "GNSS/GPS"), ("s_thermal", "Thermal"), ("s_depth", "Depth"), ("s_gas", "Gas/chemical"),
          ("s_acoustic", "Acoustic"), ("s_rf", "RF/radar"), ("s_physio", "Physiological (human-worn)")]
vals = [(lab, sum(r[k] == "1" for r in rows)) for k, lab in labels]
vals.sort(key=lambda x: x[1])
fig, ax = plt.subplots(figsize=(8, 5.2))
ax.barh([v[0] for v in vals], [v[1] for v in vals], color=BLUE, height=0.62)
for i, (_, n) in enumerate(vals):
    ax.text(n + 0.3, i, f"{n} ({100*n/39:.0f}%)", va="center", fontsize=10, color=INK)
ax.set_xlabel("Number of studies (N = 39; non-exclusive)"); ax.set_xlim(0, 21); clean(ax)
fig.tight_layout(); fig.savefig("assets/figures/fig_sensor_prevalence.png", dpi=200, facecolor="white"); plt.close(fig)

# Fig. 5 validation type, strict vs lenient
cats = ["Simulation only", "Partial", "Prototype bench test", FIELD]
names = ["Simulation only", "Partial (sim + limited\nphysical / lab or mock site)", "Prototype bench test", "Real-world field test"]
s = [sum(r["validation_strict"] == c for r in rows) for c in cats]
l = [sum(r["validation_lenient"] == c for r in rows) for c in cats]
fig, ax = plt.subplots(figsize=(8, 4.6))
y = range(len(cats)); h = 0.36
ax.barh([i + h / 2 for i in y], s, height=h, color=BLUE, label="Strict coding (primary)")
ax.barh([i - h / 2 for i in y], l, height=h, color=ORANGE, hatch="///", edgecolor="white", label="Lenient coding (sensitivity)")
for i in y:
    ax.text(s[i] + 0.3, i + h / 2, str(s[i]), va="center", fontsize=10)
    ax.text(l[i] + 0.3, i - h / 2, str(l[i]), va="center", fontsize=10)
ax.set_yticks(list(y)); ax.set_yticklabels(names); ax.invert_yaxis()
ax.set_xlabel("Number of studies (N = 39)"); ax.set_xlim(0, 21); clean(ax)
ax.legend(frameon=False, loc="lower right")
fig.tight_layout(); fig.savefig("assets/figures/fig_validation_type.png", dpi=200, facecolor="white"); plt.close(fig)

# Fig. 6 field-testing rate by mode, strict vs lenient, Wilson CIs, n labels
modes = ["Teleoperation", "Supervisory Control", "Shared-Collaborative Control", "Fully Autonomous"]
short = ["Teleoperation", "Supervisory\nControl", "Shared-\nCollaborative", "Fully\nAutonomous"]
fig, ax = plt.subplots(figsize=(8.4, 4.8))
w = 0.36
for j, (col, colr, lab, hatch) in enumerate([("validation_strict", BLUE, "Strict coding (primary)", None),
                                              ("validation_lenient", ORANGE, "Lenient coding (sensitivity)", "///")]):
    for i, m in enumerate(modes):
        sub = [r for r in rows if r["mode_clean"] == m]; n = len(sub); k = sum(r[col] == FIELD for r in sub)
        lo, hi = wilson(k, n); x = i + (j - 0.5) * w
        ax.bar(x, 100 * k / n, width=w * 0.92, color=colr, hatch=hatch, edgecolor="white",
               label=lab if i == 0 else None)
        ax.errorbar(x, 100 * k / n, yerr=[[100 * k / n - lo], [hi - 100 * k / n]], fmt="none", ecolor=INK, capsize=3, lw=1)
        ax.text(x, hi + 2, f"{k}/{n}", ha="center", fontsize=9, color=INK)
ax.set_xticks(range(4)); ax.set_xticklabels([f"{s_}\n(n = {sum(r['mode_clean']==m for r in rows)})" for s_, m in zip(short, modes)])
ax.set_ylabel("Studies with a real-world field test (%)"); ax.set_ylim(0, 105)
for sp in ("top", "right"):
    ax.spines[sp].set_visible(False)
ax.grid(axis="y", color=GRID, lw=0.8); ax.set_axisbelow(True)
ax.legend(frameon=False, loc="upper right")
fig.tight_layout(); fig.savefig("assets/figures/fig_autonomy_validation.png", dpi=200, facecolor="white"); plt.close(fig)

# Fig. 7 taxonomy bands (ordered by robot decision authority; no equal-interval axis)
order = [("Teleoperation", "Human decides each action;\nrobot executes or stabilizes", "LOA ~1–2"),
         ("Shared-Collaborative Control", "Task decisions split between\nhuman and machine layer", "LOA ~3–5"),
         ("Supervisory Control", "Human sets goals and\nmonitors; robot plans and acts", "LOA ~5–7"),
         ("Fully Autonomous", "No human decision role in the\nevaluated mission", "LOA ~8–10")]
fig, ax = plt.subplots(figsize=(11, 3.9)); ax.set_xlim(0, 100); ax.set_ylim(0, 40); ax.axis("off")
shades = ["#cde2fb", "#9ec5f4", "#5598e7", "#256abf"]
for i, (nm, desc, loa) in enumerate(order):
    n = sum(r["mode_clean"] == nm for r in rows); x = 1 + i * 24.7
    ax.add_patch(FancyBboxPatch((x, 12), 23, 25, boxstyle="round,pad=0.2,rounding_size=1.2", fc=shades[i], ec=MUTED, lw=1))
    tc = "white" if i >= 2 else INK
    ax.text(x + 11.5, 32.5, nm.replace("Shared-Collaborative Control", "Shared-Collaborative\nControl"), ha="center", va="center", fontsize=11.5, fontweight="bold", color=tc)
    ax.text(x + 11.5, 24.5, f"n = {n} ({100*n/39:.1f}%)", ha="center", va="center", fontsize=11, color=tc)
    ax.text(x + 11.5, 17, desc, ha="center", va="center", fontsize=9, color=tc)
    ax.text(x + 11.5, 9.5, loa, ha="center", va="center", fontsize=9, color=MUTED)
ax.annotate("", xy=(99, 4), xytext=(1, 4), arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.3))
ax.text(50, 0.6, "Ordered bands of decision authority held by the robot (Sheridan–Verplank; Beer et al.) — not equally spaced",
        ha="center", fontsize=9.5, color=MUTED)
fig.savefig("assets/figures/fig_taxonomy.png", dpi=200, facecolor="white", bbox_inches="tight"); plt.close(fig)
print("figures written")
