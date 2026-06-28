from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"

CASES = [f"SRD-{i:03d}" for i in range(1, 9)]
CASE_LABELS = [
    "High conflict",
    "Low conflict",
    "Hydropower",
    "Emergency",
    "Transboundary",
    "Clean build",
    "Tipping point",
    "Do not build",
]

DATA = {
    "Codex": {
        "MA_L1": np.array([28, 27, 27, 28, 28, 29, 29, 29]),
        "MA_L2": np.array([38, 33, 34, 34, 35, 34, 34, 35]),
        "MA_L3": np.array([51, 39, 42, 43, 44, 35, 43, 40]),
        "SA_L1": np.array([24, 26, 23, 26, 24, 28, 20, 27]),
        "SA_L2": np.array([30, 30, 29, 30, 30, 31, 28, 31]),
        "MCDA_L1": np.array([17, 23, 19, 20, 20, 28, 16, 25]),
        "MCDA_L2": np.array([23, 27, 24, 25, 25, 30, 23, 28]),
    },
    "Claude Code": {
        "MA_L1": np.array([26, 26, 26, 26, 26, 28, 27, 27]),
        "MA_L2": np.array([36, 34, 34, 34, 34, 36, 34, 35]),
        "MA_L3": np.array([49, 44, 43, 43, 45, 43, 45, 46]),
        "SA_L1": np.array([16, 22, 19, 21, 20, 21, 16, 22]),
        "SA_L2": np.array([22, 26, 26, 27, 27, 29, 26, 29]),
        "MCDA_L1": np.array([13, 15, 13, 13, 14, 18, 11, 15]),
        "MCDA_L2": np.array([18, 20, 18, 19, 20, 25, 18, 20]),
    },
}

COLORS = {
    "MA": "#2f8a72",
    "SA": "#2a5d8f",
    "MCDA": "#cf7f12",
    "grid": "#e5e9ef",
    "ink": "#24313f",
    "muted": "#657180",
}


def save_all(fig, stem):
    for ext in ("png", "pdf", "svg"):
        fig.savefig(REPORTS / f"{stem}.{ext}", dpi=300, bbox_inches="tight", facecolor="white")


def comparable_scores(env):
    d = DATA[env]
    return {
        "MA": d["MA_L1"] + d["MA_L2"],
        "SA": d["SA_L1"] + d["SA_L2"],
        "MCDA": d["MCDA_L1"] + d["MCDA_L2"],
    }


def draw_figure2():
    fig, axes = plt.subplots(1, 2, figsize=(16.4, 7.6), sharey=True)
    fig.patch.set_facecolor("white")
    y = np.arange(len(CASES))

    for ax, env in zip(axes, DATA):
        scores = comparable_scores(env)
        ax.set_title(env, loc="left", fontsize=13, fontweight="bold", color=COLORS["ink"])
        ax.set_xlim(25, 76)
        ax.set_ylim(-0.6, len(CASES) - 0.4)
        ax.invert_yaxis()
        ax.grid(axis="x", color=COLORS["grid"], lw=0.8)
        ax.set_axisbelow(True)

        for i in y:
            low = min(scores["MA"][i], scores["SA"][i], scores["MCDA"][i])
            high = max(scores["MA"][i], scores["SA"][i], scores["MCDA"][i])
            ax.plot([low, high], [i, i], color="#cfd7df", lw=2.2, zorder=1)

        ax.scatter(scores["MCDA"], y, s=92, marker="s", color=COLORS["MCDA"], label="MCDA", zorder=3)
        ax.scatter(scores["SA"], y, s=92, marker="^", color=COLORS["SA"], label="Single-agent", zorder=4)
        ax.scatter(scores["MA"], y, s=112, marker="o", color=COLORS["MA"], label="Multi-agent", zorder=5)

        for i in y:
            gain_sa = scores["MA"][i] - scores["SA"][i]
            gain_mcda = scores["MA"][i] - scores["MCDA"][i]
            ax.text(
                75.3,
                i,
                f"+{gain_sa:.0f}/+{gain_mcda:.0f}",
                ha="right",
                va="center",
                fontsize=8.2,
                color=COLORS["muted"],
            )

        ax.text(75.3, -0.78, "Gain\nSA/MCDA", ha="right", va="top", fontsize=8.2, color=COLORS["muted"])
        ax.set_xlabel("Comparable score: Outcome + Evidence (max 70)", fontsize=10)
        ax.spines[["top", "right"]].set_visible(False)
        ax.spines["left"].set_color("#b9c2cc")
        ax.spines["bottom"].set_color("#b9c2cc")

    axes[0].set_yticks(y)
    axes[0].set_yticklabels([f"{c}\n{l}" for c, l in zip(CASES, CASE_LABELS)], fontsize=9)
    axes[1].tick_params(axis="y", length=0)

    handles = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor=COLORS["MA"], markersize=9, label="Multi-agent"),
        Line2D([0], [0], marker="^", color="w", markerfacecolor=COLORS["SA"], markersize=9, label="Single-agent"),
        Line2D([0], [0], marker="s", color="w", markerfacecolor=COLORS["MCDA"], markersize=9, label="MCDA"),
        Line2D([0], [0], color="#cfd7df", lw=2.2, label="Within-case score range"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=4, frameon=False, fontsize=10, bbox_to_anchor=(0.52, 0.02))
    fig.text(
        0.02,
        0.985,
        "Figure 2. Multi-agent advantage over single-agent and MCDA baselines",
        ha="left",
        va="top",
        fontsize=17,
        fontweight="bold",
        color=COLORS["ink"],
    )
    fig.text(
        0.02,
        0.945,
        "Each row compares systems on the same case using only layers that all systems receive: Outcome Quality (L1) + Evidence Quality (L2). "
        "Right labels show multi-agent gain over single-agent / MCDA.",
        ha="left",
        va="top",
        fontsize=9.8,
        color=COLORS["muted"],
    )
    fig.subplots_adjust(left=0.16, right=0.985, top=0.86, bottom=0.14, wspace=0.10)
    save_all(fig, "figure2-baseline-comparison")
    plt.close(fig)


def diagnostics(env):
    d = DATA[env]
    ma = d["MA_L1"] + d["MA_L2"]
    sa = d["SA_L1"] + d["SA_L2"]
    mcda = d["MCDA_L1"] + d["MCDA_L2"]
    raw = np.column_stack(
        [
            d["MA_L1"] / 30 * 100,
            d["MA_L2"] / 40 * 100,
            d["MA_L3"] / 55 * 100,
            ma - sa,
            ma - mcda,
        ]
    )
    return raw


def draw_heatmap_panel(ax, env, show_ylabels=False):
    vals = diagnostics(env)
    pct_cols = vals[:, :3]
    delta_cols = vals[:, 3:]
    color_vals = np.column_stack([pct_cols / 100, delta_cols / 35])
    color_vals = np.clip(color_vals, 0, 1)

    im = ax.imshow(color_vals, cmap="YlGnBu", vmin=0, vmax=1, aspect="auto")
    ax.set_title(env, loc="left", fontsize=13, fontweight="bold", color=COLORS["ink"])
    columns = ["Outcome\n%", "Evidence\n%", "Process\n%", "Gain vs\nSA", "Gain vs\nMCDA"]
    ax.set_xticks(np.arange(len(columns)))
    ax.set_xticklabels(columns, fontsize=9)
    ax.set_yticks(np.arange(len(CASES)))
    if show_ylabels:
        ax.set_yticklabels([f"{c}  {l}" for c, l in zip(CASES, CASE_LABELS)], fontsize=8.5)
    else:
        ax.set_yticklabels([])
    ax.tick_params(length=0)
    ax.set_xticks(np.arange(-0.5, len(columns), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(CASES), 1), minor=True)
    ax.grid(which="minor", color="white", linestyle="-", linewidth=1.5)
    for spine in ax.spines.values():
        spine.set_visible(False)

    for i in range(vals.shape[0]):
        for j in range(vals.shape[1]):
            if j < 3:
                txt = f"{vals[i, j]:.0f}%"
            else:
                txt = f"+{vals[i, j]:.0f}"
            color = "white" if color_vals[i, j] > 0.62 else COLORS["ink"]
            ax.text(j, i, txt, ha="center", va="center", fontsize=8.2, color=color, fontweight="bold")
    return im


def draw_figure3():
    fig, axes = plt.subplots(1, 2, figsize=(16.2, 7.6), sharey=False)
    fig.patch.set_facecolor("white")
    im = draw_heatmap_panel(axes[0], "Codex", show_ylabels=True)
    draw_heatmap_panel(axes[1], "Claude Code", show_ylabels=False)

    fig.text(
        0.02,
        0.985,
        "Figure 3. Case-level diagnostic profile of multi-agent deliberation",
        ha="left",
        va="top",
        fontsize=17,
        fontweight="bold",
        color=COLORS["ink"],
    )
    fig.text(
        0.02,
        0.945,
        "Outcome, Evidence, and Process columns report normalized multi-agent layer scores. Gain columns report additional L1+L2 points over baselines. "
        "Cell color is column-normalized so high and low cases are visible within each diagnostic dimension.",
        ha="left",
        va="top",
        fontsize=9.8,
        color=COLORS["muted"],
    )
    fig.subplots_adjust(left=0.22, right=0.985, top=0.86, bottom=0.08, wspace=0.06)
    save_all(fig, "figure3-case-diagnostics")
    plt.close(fig)


def main():
    REPORTS.mkdir(parents=True, exist_ok=True)
    draw_figure2()
    draw_figure3()


if __name__ == "__main__":
    main()
