"""Post-hoc AI-assisted reliability check (NOT human inter-rater agreement).

Compares the blind AI second coding of Autonomy/HRI mode
(data/reliability_blind_codes.csv) with the original labels taken from the
manuscript's Sec. IV-A..IV-D per-mode citation lists in
SAR_review_master_document.md (cross-checked against Table VII/XI totals).

Run from the project root:  python data/reliability_stats.py
"""
import csv
import math
import random
from collections import Counter

CATS = ["T", "S", "C", "F"]
NAMES = {"T": "Teleoperation", "S": "Supervisory", "C": "Shared-Collaborative", "F": "Fully Autonomous"}

# Original labels: master doc Sec. IV-A (Teleop [10]-[14]), IV-B (Supervisory [15]-[18]),
# IV-C (Shared [19]-[21]), IV-D (FA [22]-[48]); totals match Table VII/XI (5/4/3/27).
ORIGINAL = {}
for n in range(10, 15): ORIGINAL[n] = "T"
for n in range(15, 19): ORIGINAL[n] = "S"
for n in range(19, 22): ORIGINAL[n] = "C"
for n in range(22, 49): ORIGINAL[n] = "F"
assert Counter(ORIGINAL.values()) == Counter({"F": 27, "T": 5, "S": 4, "C": 3})


def load_blind(path="data/reliability_blind_codes.csv"):
    with open(path, encoding="utf-8") as f:
        return {int(r["ref_N"]): r for r in csv.DictReader(f)}


def cohen_kappa(a, b, cats):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pa, pb = Counter(a), Counter(b)
    pe = sum(pa[c] / n * pb[c] / n for c in cats)
    return po, pe, (po - pe) / (1 - pe) if pe < 1 else float("nan")


def cohen_kappa_se(a, b, cats):
    """Large-sample SE of kappa (Fleiss, Cohen & Everitt 1969)."""
    n = len(a)
    p = {(i, j): sum(1 for x, y in zip(a, b) if x == i and y == j) / n for i in cats for j in cats}
    r = {i: sum(p[(i, j)] for j in cats) for i in cats}
    c = {j: sum(p[(i, j)] for i in cats) for j in cats}
    po = sum(p[(i, i)] for i in cats)
    pe = sum(r[i] * c[i] for i in cats)
    k = (po - pe) / (1 - pe)
    t1 = sum(p[(i, i)] * (1 - (r[i] + c[i]) * (1 - k)) ** 2 for i in cats)
    t2 = (1 - k) ** 2 * sum(p[(i, j)] * (c[i] + r[j]) ** 2 for i in cats for j in cats if i != j)
    t3 = (k - pe * (1 - k)) ** 2
    var = (t1 + t2 - t3) / (n * (1 - pe) ** 2)
    return math.sqrt(max(var, 0.0))


def scott_pi(a, b, cats):
    """Two-rater Fleiss' kappa == Scott's pi."""
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pool = Counter(a) + Counter(b)
    pe = sum((pool[c] / (2 * n)) ** 2 for c in cats)
    return (po - pe) / (1 - pe)


def gwet_ac1(a, b, cats):
    n, q = len(a), len(cats)
    po = sum(x == y for x, y in zip(a, b)) / n
    pool = Counter(a) + Counter(b)
    pe = sum((pool[c] / (2 * n)) * (1 - pool[c] / (2 * n)) for c in cats) / (q - 1)
    return (po - pe) / (1 - pe)


def bootstrap_ci(a, b, cats, stat, reps=2000, seed=1):
    rng = random.Random(seed)
    n = len(a)
    vals = []
    for _ in range(reps):
        idx = [rng.randrange(n) for _ in range(n)]
        aa, bb = [a[i] for i in idx], [b[i] for i in idx]
        v = stat(aa, bb, cats)
        if not math.isnan(v):
            vals.append(v)
    vals.sort()
    lo = vals[int(0.025 * len(vals))]
    hi = vals[min(int(0.975 * len(vals)), len(vals) - 1)]
    return lo, hi, len(vals)


def report(a, b, cats, label):
    po, pe, k = cohen_kappa(a, b, cats)
    se = cohen_kappa_se(a, b, cats)
    blo, bhi, nb = bootstrap_ci(a, b, cats, lambda x, y, c: cohen_kappa(x, y, c)[2])
    ac1 = gwet_ac1(a, b, cats)
    alo, ahi, _ = bootstrap_ci(a, b, cats, gwet_ac1)
    pi = scott_pi(a, b, cats)
    print(f"\n=== {label} (N = {len(a)}) ===")
    print(f"Percent agreement      : {po*100:.1f}% ({sum(x == y for x, y in zip(a, b))}/{len(a)})")
    print(f"Cohen's kappa          : {k:.3f}  (chance agreement pe = {pe:.3f})")
    print(f"  95% CI analytic      : [{max(-1, k-1.96*se):.3f}, {min(1, k+1.96*se):.3f}]  (SE = {se:.3f})")
    print(f"  95% CI bootstrap     : [{blo:.3f}, {bhi:.3f}]  (percentile, 2000 reps, seed 1, {nb} valid)")
    print(f"Gwet's AC1             : {ac1:.3f}  bootstrap 95% CI [{alo:.3f}, {ahi:.3f}]")
    print(f"Scott's pi (= two-rater Fleiss' kappa): {pi:.3f}")
    return dict(po=po, k=k, se=se, blo=blo, bhi=bhi, ac1=ac1, pi=pi)


def confusion(a, b, cats, la="Original", lb="Blind AI"):
    print(f"\nConfusion matrix (rows = {la}, columns = {lb})")
    print("        " + "".join(f"{c:>7}" for c in cats) + "  total")
    for i in cats:
        row = [sum(1 for x, y in zip(a, b) if x == i and y == j) for j in cats]
        print(f"{i:>6}  " + "".join(f"{v:>7}" for v in row) + f"  {sum(row):>5}")
    print("total   " + "".join(f"{sum(1 for y in b if y == j):>7}" for j in cats) + f"  {len(b):>5}")


def main():
    blind = load_blind()
    refs = sorted(ORIGINAL)
    assert sorted(blind) == refs, "ref_N sets differ"
    a = [ORIGINAL[n] for n in refs]
    b = [blind[n]["blind_mode"] for n in refs]

    report(a, b, CATS, "4-category Autonomy/HRI mode")
    confusion(a, b, CATS)

    a2 = ["FA" if x == "F" else "HUMAN" for x in a]
    b2 = ["FA" if x == "F" else "HUMAN" for x in b]
    report(a2, b2, ["FA", "HUMAN"], "Binary: Fully Autonomous vs human-in-mission (T/S/C)")
    confusion(a2, b2, ["FA", "HUMAN"])

    # Blind human_role_modelled flag vs original non-FA membership (consistency check)
    h = ["HUMAN" if blind[n]["human_role_modelled"] == "Y" else "FA" for n in refs]
    report(a2, h, ["FA", "HUMAN"], "Original non-FA vs blind human_role_modelled = Y")

    print("\nDisagreements (ref, original -> blind, blind confidence):")
    for n in refs:
        if ORIGINAL[n] != blind[n]["blind_mode"]:
            print(f"  [{n}] {NAMES[ORIGINAL[n]]} -> {NAMES[blind[n]['blind_mode']]} ({blind[n]['confidence']})")

    print("\nAgreement by blind confidence:")
    for conf in ["high", "medium", "low"]:
        sub = [n for n in refs if blind[n]["confidence"] == conf]
        agree = sum(ORIGINAL[n] == blind[n]["blind_mode"] for n in sub)
        print(f"  {conf:<6}: {agree}/{len(sub)}")

    print("\nMarginals: original", dict(Counter(a)), " blind", dict(Counter(b)))


if __name__ == "__main__":
    main()
