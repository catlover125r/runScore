# RunScore

**A county-level running activity index for all 3,143 U.S. counties.**

RunScore is a composite index that quantifies the strength of a community's running culture using public-domain data sources. The index correlates with home values, health outcomes, walkability, and school quality — making it a measurable lifestyle signal for home buyers, real estate platforms, and urban planners.

**Site:** [runscore.org](https://runscore.org)

---

## What is RunScore?

RunScore (0–100) is built from four components:

| Component | Source |
|---|---|
| Physical inactivity rate (inverted) | CDC PLACES |
| Running race participation per 100k residents | RunSignUp |
| Walkability & trail infrastructure | EPA National Walkability Index, USDA |
| Fitness facility density | USDA Food Environment Atlas |

---

## Key Findings

- **Home values:** Spearman r = +0.606, p < 0.001 — each 10-point RunScore increase corresponds to ~$58,000 higher median home value
- **Obesity:** r = −0.570, p < 0.001
- **Diabetes:** r = −0.676, p < 0.001
- **Life expectancy:** r = +0.582, p < 0.001
- **Fair/Poor health:** r = −0.673, p < 0.001

---

## Repository Structure

```
runscore/
├── index.html                        # Main website (GitHub Pages)
├── RunScore_Paper_Popler_2026.pdf    # Full research paper
├── figures/                          # All charts and maps
│   ├── fig4_runscore_map.png
│   ├── fig1_runscore_vs_homevalue.png
│   ├── fig_health_obesity.png
│   ├── fig_health_diabetes.png
│   ├── fig_health_lifeexp.png
│   └── fig_health_fairpoor.png
├── data/processed/                   # Cleaned county-level datasets
│   └── master_county.csv             # Master dataset (3,143 counties)
├── build_health_figs.py              # Script to regenerate health charts
└── CNAME                             # runscore.org custom domain
```

---

## Data Sources

- [CDC PLACES](https://www.cdc.gov/places) — county-level health estimates
- [RunSignUp](https://runsignup.com) — race event and finisher counts
- [EPA National Walkability Index](https://www.epa.gov/smartgrowth/smart-location-mapping)
- [USDA Food Environment Atlas](https://www.ers.usda.gov/data-products/food-environment-atlas/)
- [Zillow Research](https://www.zillow.com/research/data/) — ZHVI home value index
- [County Health Rankings](https://www.countyhealthrankings.org) — life expectancy, health outcomes

---

## Author

Luke Popler — Sequoia High School, 2026
