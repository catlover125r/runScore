import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy import stats

# ── Style ──────────────────────────────────────────────────────────────────
mpl.rcParams.update({
    'font.family':       'sans-serif',
    'font.sans-serif':   ['Helvetica Neue', 'Arial', 'DejaVu Sans'],
    'axes.spines.top':   False,
    'axes.spines.right': False,
    'axes.spines.left':  True,
    'axes.spines.bottom':True,
    'axes.grid':         True,
    'grid.color':        '#f0f0f0',
    'grid.linewidth':    0.8,
    'axes.facecolor':    'white',
    'figure.facecolor':  'white',
    'axes.edgecolor':    '#cccccc',
    'xtick.color':       '#888888',
    'ytick.color':       '#888888',
    'xtick.labelsize':   11,
    'ytick.labelsize':   11,
})

# ── Data ───────────────────────────────────────────────────────────────────
df = pd.read_csv('data/processed/master_county.csv')

# Income tertiles for coloring
df['income_tertile'] = pd.qcut(df['median_household_income'], 3,
                                labels=['Low Income', 'Mid Income', 'High Income'])

COLORS = {
    'Low Income':  '#e05a4e',
    'Mid Income':  '#f0a040',
    'High Income': '#4caf72',
}

# ── Figures config ─────────────────────────────────────────────────────────
CHARTS = [
    dict(
        col='pct_obese',
        ylabel='Obesity Rate (%)',
        title='RunScore vs. Obesity Rate',
        r_label='r = −0.570',
        filename='fig_health_obesity.png',
        invert=True,       # lower is better → slope goes down
    ),
    dict(
        col='pct_diabetes',
        ylabel='Diabetes Rate (%)',
        title='RunScore vs. Diabetes Rate',
        r_label='r = −0.676',
        filename='fig_health_diabetes.png',
        invert=True,
    ),
    dict(
        col='life_expectancy',
        ylabel='Life Expectancy (years)',
        title='RunScore vs. Life Expectancy',
        r_label='r = +0.582',
        filename='fig_health_lifeexp.png',
        invert=False,
    ),
    dict(
        col='pct_fair_poor_health',
        ylabel='Fair / Poor Health (%)',
        title='RunScore vs. Fair / Poor Health',
        r_label='r = −0.673',
        filename='fig_health_fairpoor.png',
        invert=True,
    ),
]

for cfg in CHARTS:
    sub = df[['runscore', cfg['col'], 'income_tertile']].dropna()
    x = sub['runscore'].values
    y = sub[cfg['col']].values

    fig, ax = plt.subplots(figsize=(8, 5.6))

    # Scatter — income tertile colors
    for tertile, color in COLORS.items():
        mask = sub['income_tertile'] == tertile
        ax.scatter(x[mask], y[mask],
                   c=color, alpha=0.35, s=14, linewidths=0,
                   label=tertile, rasterized=True)

    # OLS trend line
    slope, intercept, r, p, _ = stats.linregress(x, y)
    x_line = np.linspace(0, 100, 300)
    ax.plot(x_line, intercept + slope * x_line,
            color='#1a1a1a', linewidth=1.8, zorder=5)

    # Labels
    ax.set_xlabel('RunScore (0 – 100)', fontsize=12, color='#444', labelpad=8)
    ax.set_ylabel(cfg['ylabel'], fontsize=12, color='#444', labelpad=8)

    ax.set_title(
        f"{cfg['title']}  —  3,143 U.S. Counties\n"
        f"Spearman {cfg['r_label']},  p < 0.001",
        fontsize=12.5, color='#222', pad=14, linespacing=1.5,
    )

    ax.set_xlim(-1, 101)
    ax.tick_params(length=0)

    # Legend
    ax.legend(
        frameon=False, fontsize=10,
        loc='upper right' if not cfg['invert'] else 'upper left',
        labelcolor='#555',
    )

    fig.tight_layout(pad=1.5)
    out = f"figures/{cfg['filename']}"
    fig.savefig(out, dpi=220, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"Saved {out}")

print("Done.")
