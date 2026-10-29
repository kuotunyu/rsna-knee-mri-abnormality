# --- cell: leaderboard ---
def _leaderboard_figure():
    # Displayed private scores around our rank, read from the final private leaderboard (6,299 teams).
    import matplotlib.pyplot as plt
    BG, INK, MUTED, LINE, GREY, ORANGE = "#fcfcfb", "#1b1b1a", "#6b6a66", "#d9d8d0", "#c9c7bf", "#d9622b"
    blocks = [("0.944", 204, 296), ("0.943", 297, 583), ("0.942", 584, 1880), ("0.941", 1881, 2098), ("0.940", 2099, 2205)]
    fig, ax = plt.subplots(figsize=(13, 3.6), facecolor=BG); ax.set_facecolor(BG)
    for i, (s, a, b) in enumerate(blocks):
        ax.barh(0, b - a + 1, left=a, height=0.5, color=GREY if s != "0.943" else "#f2c3a8", edgecolor=BG, lw=2)
        if s == "0.942":
            ax.text((a + b) / 2, 0, f"private {s}\n{b - a + 1:,} teams, ranks {a:,}–{b:,}", ha="center", va="center",
                    fontsize=11, color=INK)
        else:
            ax.text((a + b) / 2, -0.36, f"{s}\n{b - a + 1:,} teams", ha="center", va="top", fontsize=9, color=MUTED)
    ax.plot([478, 478], [-0.42, 0.42], color=ORANGE, lw=2.5)
    ax.annotate("this notebook: 478th, 0.943", (478, 0.42), (330, 0.85), color=ORANGE, fontsize=11, weight="bold",
                ha="left", arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1.2))
    ax.annotate("our unchanged copy of the\n0.958 notebook scored 0.942", (1232, 0.27), (1232, 0.8), color=MUTED,
                fontsize=10, ha="center", arrowprops=dict(arrowstyle="-", color=MUTED, lw=1))
    ax.set_xlim(180, 2240); ax.set_ylim(-0.85, 1.15); ax.set_yticks([])
    ax.set_xlabel("private leaderboard rank", color=MUTED)
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(LINE); ax.tick_params(colors=MUTED)
    ax.set_title("The 0.942 block: 1,297 teams with the same displayed private score", loc="left", fontsize=14,
                 color=INK, weight="bold", pad=12)
    plt.tight_layout(); plt.show()


_leaderboard_figure()


# --- cell: public_vs_private ---
def _public_private_figure():
    # Our last 20 submissions: displayed public vs private score (Kaggle submission list after the deadline).
    import matplotlib.pyplot as plt
    from collections import Counter
    BG, INK, MUTED, LINE, GREY, ORANGE = "#fcfcfb", "#1b1b1a", "#6b6a66", "#d9d8d0", "#9d9b93", "#d9622b"
    subs = [(0.957, 0.943)] * 3 + [(0.957, 0.942)] * 6 + [(0.958, 0.942)] + [(0.956, 0.942)] * 2 + \
           [(0.956, 0.941)] * 4 + [(0.956, 0.940)] + [(0.954, 0.939)] + [(0.950, 0.938)] + [(0.950, 0.937)]
    cnt = Counter(subs)
    fig, ax = plt.subplots(figsize=(9.5, 5.2), facecolor=BG); ax.set_facecolor(BG)
    for (pu, pr), n in cnt.items():
        col = ORANGE if (pu, pr) == (0.957, 0.943) else (INK if (pu, pr) == (0.958, 0.942) else GREY)
        ax.scatter(pu, pr, s=90 + 70 * n, color=col, alpha=0.85, zorder=3)
        ax.text(pu + 0.00035, pr, f"{n}", va="center", fontsize=10, color=col)
    ax.annotate("0.958 notebook, unchanged", (0.958, 0.942), (0.9555, 0.9447), fontsize=10, color=INK,
                arrowprops=dict(arrowstyle="-", color=INK, lw=1))
    ax.annotate("selected variant (and two\nsiblings with the same scores)", (0.957, 0.943), (0.9505, 0.9433),
                fontsize=10, color=ORANGE, arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1))
    ax.set_xlabel("displayed public score", color=MUTED); ax.set_ylabel("displayed private score", color=MUTED)
    ax.set_xlim(0.949, 0.9595); ax.set_ylim(0.9362, 0.9458)
    ax.grid(color=LINE, lw=0.6, zorder=0)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    for s in ("left", "bottom"): ax.spines[s].set_color(LINE)
    ax.tick_params(colors=MUTED)
    ax.set_title("Our last 20 submissions: the highest public score was not the highest private score",
                 loc="left", fontsize=12.5, color=INK, weight="bold", pad=10)
    ax.text(0.949, 0.9365, "number = how many submissions share that point", fontsize=9, color=MUTED)
    plt.tight_layout(); plt.show()


_public_private_figure()


# --- cell: gold_per_finding ---
def _gold_figure():
    # gold-58 AUC per finding, full deployed chain: 0.958 notebook unchanged vs this notebook.
    import matplotlib.pyplot as plt
    BG, INK, MUTED, LINE, GREY, ORANGE = "#fcfcfb", "#1b1b1a", "#6b6a66", "#d9d8d0", "#c9c7bf", "#d9622b"
    auc = {"ACL": (0.9877, 0.9877), "MCL": (0.9637, 0.9660), "Medial Meniscus": (0.9784, 0.9772),
           "Lateral Meniscus": (0.9143, 0.9149), "Medial OA": (0.9907, 0.9907), "Lateral OA": (0.8472, 0.8491),
           "PF OA": (0.8867, 0.9048), "Effusion": (0.9801, 0.9826), "Synovitis": (0.8363, 0.8542),
           "Baker's": (0.9783, 0.9783), "Contusion": (0.9609, 0.9609), "Fracture": (0.9361, 0.9361)}
    names = sorted(auc, key=lambda k: auc[k][1] - auc[k][0])
    d = [auc[k][1] - auc[k][0] for k in names]
    fig, ax = plt.subplots(figsize=(9.5, 5.4), facecolor=BG); ax.set_facecolor(BG)
    ax.barh(names, d, color=[ORANGE if v > 0.005 else GREY for v in d], height=0.62)
    for i, (k, v) in enumerate(zip(names, d)):
        ax.text(max(v, 0) + 0.0004, i, f"{v:+.4f}   ({auc[k][0]:.3f} → {auc[k][1]:.3f})",
                va="center", ha="left", fontsize=9, color=INK if v > 0.005 else MUTED)
    ax.axvline(0, color=INK, lw=0.8)
    ax.set_xlim(-0.006, 0.03); ax.set_xlabel("gold-58 AUC, this notebook minus the 0.958 notebook", color=MUTED)
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(LINE); ax.tick_params(colors=MUTED, length=0)
    ax.set_title("Where the gold-58 gain comes from: PF OA and Synovitis (mean 0.9384 → 0.9419)",
                 loc="left", fontsize=12.5, color=INK, weight="bold", pad=10)
    fig.text(0.01, 0.01, "58 studies, so each finding has only 9 to 35 positives: read this as direction, not size.",
             fontsize=9, color=MUTED)
    plt.tight_layout(rect=(0, 0.04, 1, 1)); plt.show()


_gold_figure()
