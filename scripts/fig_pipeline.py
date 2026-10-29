def _figure():
    # How this notebook works (scores: public / private leaderboard as displayed; gold-58 AUC of the deployed chain)
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

    BG, INK, MUTED, LINE = "#fcfcfb", "#1b1b1a", "#6b6a66", "#d9d8d0"
    GREY, GREY2, BLUE, BLUE_T, ORANGE, ORANGE_T = "#efeee9", "#e2e1db", "#2a78d6", "#dbe9fb", "#d9622b", "#fbe3d6"

    fig = plt.figure(figsize=(15, 8.6), facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.text(0.03, 0.95, "A variant of the public 0.958 notebook, chosen on the 58 fully labelled training studies",
            fontsize=18, color=INK, weight="bold", va="center")
    ax.text(0.03, 0.905, "Grey: public work used unchanged.   Orange: the two things this notebook changes.",
            fontsize=11.5, color=MUTED, va="center")

    def box(x, y, w, h, title, sub, fill, edge, tc=INK):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.004,rounding_size=0.012",
                                    fc=fill, ec=edge, lw=1.4))
        ax.text(x + 0.012, y + h - 0.033, title, fontsize=11.5, color=tc, weight="bold", va="center")
        ax.text(x + 0.012, y + h - 0.075, sub, fontsize=9.6, color=MUTED, va="top", linespacing=1.35)

    def arrow(x0, y0, x1, y1, c=MUTED):
        ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=13, color=c, lw=1.3))

    # stage 1-2: public models
    box(0.03, 0.66, 0.25, 0.17, "Raptor CoAtNet, 384 px", "nartaa · knee + mirror\nweight 0.65 in the Raptor slot", GREY, LINE)
    box(0.03, 0.46, 0.25, 0.17, "Raptor CoAtNet, 224 px", "nartaa · varshithakolupuri\nweight 0.35 in the Raptor slot", GREY, LINE)
    box(0.03, 0.22, 0.25, 0.19, "Compact model R6", "heliosli · ConvNeXt-small\n4 folds, flip TTA", GREY, LINE)

    # stage 3: blend (changed)
    box(0.36, 0.40, 0.25, 0.30, "Part A3: rank blend", "per finding:\nw · rank(Raptor) + (1 − w) · rank(R6)\n\n"
        "changed w:\nMedial OA 0.5 → 0.3\nPF OA 0.6 → 0.3\nSynovitis 0.8 → 0.5", ORANGE_T, ORANGE, ORANGE)
    for y in (0.745, 0.545):
        arrow(0.28, y, 0.36, 0.60)
    arrow(0.28, 0.315, 0.36, 0.47)

    # part B: goodpjw reader
    box(0.69, 0.60, 0.27, 0.17, "Part B: goodpjw's 2.5D reader", "3 public folds · sujanmajhisuzan's weights\n"
        "weight 0.003 to 0.035 per finding", GREY, LINE)
    arrow(0.61, 0.62, 0.69, 0.665)

    # part C: our reader (added)
    box(0.69, 0.34, 0.27, 0.20, "Part C: our reader, weight 0.1", "goodpjw's code, retrained by us\nConvNeXt-small 256 px, 4 folds × 2 seeds\n"
        "nartaa's LLM soft labels, no gold-58", ORANGE_T, ORANGE, ORANGE)
    arrow(0.825, 0.60, 0.825, 0.54)
    box(0.69, 0.13, 0.27, 0.15, "submission.csv", "per finding:\nrank(0.9 · rank(Part B) + 0.1 · rank(reader))", GREY2, LINE)
    arrow(0.825, 0.34, 0.825, 0.28, ORANGE)

    # results
    rows = [("", "gold-58", "public", "private"), ("0.958 notebook, unchanged", "0.9384", "0.958", "0.942"),
            ("this notebook", "0.9419", "0.957", "0.943")]
    x0, y0 = 0.36, 0.30
    for i, r in enumerate(rows):
        for j, t in enumerate(r):
            ax.text(x0 + [0, 0.165, 0.22, 0.275][j], y0 - i * 0.04, t, fontsize=10.5 if i else 9.5,
                    color=(ORANGE if i == 2 else INK) if i else MUTED, weight="bold" if i == 2 and j == 3 else "normal",
                    va="center", ha="left" if j == 0 else "center")
    ax.plot([x0, x0 + 0.295], [y0 - 0.02, y0 - 0.02], color=LINE, lw=1)
    ax.text(0.03, 0.06, "Private: 478th of 6,299 (bronze; 507th at the deadline). Ranks 584 to 1,880 all display 0.942, like our unchanged copy. "
            "gold-58 was reused many times, so it is a selection signal, not an independent test.",
            fontsize=9.6, color=MUTED, va="center")
    plt.show()


_figure()
