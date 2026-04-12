# RunScore — Regression Results Summary
*Analysis date: April 2026 | N = 2,477–3,143 U.S. counties*

---

## Key Finding: RunScore Predicts Home Values Beyond Income

### Model 3 — Log(Home Value) ~ Log(Income) + Controls + RunScore
| Variable | β | p |
|---|---|---|
| Log(Median Income) | 1.2361 | <0.001 *** |
| % Unemployed | 2.4527 | <0.001 *** |
| % Uninsured | 1.8430 | <0.001 *** |
| Life Expectancy | 0.0287 | <0.001 *** |
| **RunScore** | **0.0028** | **<0.001 ***** |

**R² progression:**
- Income alone: R² = 0.619
- + health/labor controls: R² = 0.659
- + RunScore: R² = **0.673** (ΔR² = +0.014)

RunScore is **statistically significant at p < 0.001** even after controlling for income, unemployment, insurance coverage, and life expectancy. It adds independent explanatory power.

---

## Dollar Value of RunScore
*Based on median county home value of $224,505*

| RunScore Increase | Home Value Change | Dollar Impact |
|---|---|---|
| +10 points | +2.9% | **+$6,444** |
| +25 points | +7.3% | **+$16,459** |
| +50 points | +15.2% | **+$34,125** |

---

## RunScore → Health Outcomes (controlling for income)
*All significant at p < 0.001*

| Outcome | β per RunScore point | ΔR² from adding RunScore |
|---|---|---|
| Obesity rate | -0.053% | +0.062 |
| Diabetes rate | -0.029% | +0.056 |
| Fair/poor health | -0.047% | +0.048 |
| Life expectancy | +0.020 years | +0.014 |

A county moving from RunScore 25→75 (25th to 75th percentile) predicts:
- 2.7 percentage points lower obesity
- 1.5 percentage points lower diabetes
- 1.0 year longer life expectancy

---

## Bivariate Correlations (Spearman)

| Variable | r | n |
|---|---|---|
| Exercise access | +0.807 | 3,097 |
| Walkability score | +0.761 | 3,132 |
| Physical inactivity | -0.755 | 2,956 |
| Fair/poor health | -0.690 | 2,956 |
| Diabetes rate | -0.676 | 2,956 |
| Median income | +0.634 | 3,142 |
| Home value (ZHVI) | +0.604 | 3,064 |
| Life expectancy | +0.582 | 3,060 |
| Obesity rate | -0.570 | 2,956 |
| Park access | +0.530 | 2,846 |
| 5-yr home appreciation | +0.214 | 3,013 |

---

## Top 20 Counties by RunScore
| Rank | County | State | RunScore |
|---|---|---|---|
| 1 | Charles City | VA | 100.0 |
| 2 | Billings | ND | 100.0 |
| 3 | Nantucket | MA | 99.9 |
| 4 | Falls Church | VA | 99.9 |
| 5 | Fairfax City | VA | 99.9 |
| 6 | Teton | WY | 99.8 |
| 7 | Irion | TX | 99.8 |
| 8 | San Juan | WA | 99.8 |
| 9 | New York (Manhattan) | NY | 99.8 |
| 10 | Arlington | VA | 99.7 |
| 11 | Armstrong | TX | 99.7 |
| 12 | Dukes (Martha's Vineyard) | MA | 99.7 |
| 13 | Charlottesville | VA | 99.6 |
| 14 | District of Columbia | DC | 99.6 |
| 15 | Missoula | MT | 99.6 |
| 16 | Gallatin (Bozeman) | MT | 99.5 |
| 17 | Alexandria | VA | 99.5 |
| 18 | King (Seattle) | WA | 99.5 |
| 19 | Bergen | NJ | 99.4 |
| 20 | Norfolk | MA | 99.4 |

---

## RunScore Components (v2)
1. **Physical activity** — CDC PLACES % physically inactive (inverted)
2. **Race event density** — RunSignUp races per 100k population
3. **Exercise infrastructure** — County Health Rankings exercise access %
4. **Fitness facility density** — USDA Atlas facilities per 1k population
5. **Walkability** — EPA National Walkability Index (pop-weighted county mean)

*Strava Metro trip-count data pending academic cohort application — will strengthen Component 1/2 significantly*

---

## Robustness Checks — RunScore Holds Across All Subgroups

Adding USDA Rural-Urban Continuum Code (RUCC 1–9) as a control, and splitting metro vs. non-metro:

| Model | N | R² | RunScore β | p |
|---|---|---|---|---|
| Full sample + RUCC control | 3,017 | 0.641 | 0.00276 | <0.001 *** |
| Metro counties only | 1,174 | 0.702 | 0.00229 | <0.001 *** |
| Non-metro counties only | 1,843 | 0.486 | 0.00374 | <0.001 *** |

**RunScore is significant in every subgroup.** The effect is actually *larger* in non-metro counties — running culture predicts home values even in rural areas, independent of urbanicity.

---

## City Deep Dive Profiles

### High RunScore Counties
| County | RunScore | Inactive % | Obese % | Life Exp. | Home Value | Income |
|---|---|---|---|---|---|---|
| Teton WY (Jackson Hole) | 99.8 | 18.3% | 24.0% | 87.6 yrs | $2,147,757 | $130,156 |
| Gallatin MT (Bozeman) | 99.5 | 13.9% | 23.0% | 82.0 yrs | $689,955 | $90,942 |
| Missoula MT | 99.5 | 16.5% | 26.2% | 78.6 yrs | $559,508 | $72,882 |
| Nantucket MA | 99.9 | 17.2% | 27.7% | 82.8 yrs | $3,029,344 | $108,671 |
| Manhattan NY | 99.8 | 20.4% | 19.2% | 83.0 yrs | $1,217,413 | $100,869 |

### Low RunScore Counties
| County | RunScore | Inactive % | Obese % | Life Exp. | Home Value | Income |
|---|---|---|---|---|---|---|
| Humphreys MS | 0.1 | 47.9% | 52.4% | 66.6 yrs | $82,469 | $31,538 |
| Greene AL | 0.0 | 44.7% | 52.7% | 70.6 yrs | $125,975 | $34,619 |
| Oglala Lakota SD | 0.2 | 40.1% | 47.0% | 56.9 yrs | N/A | $42,791 |

**The spread across the extremes:**
- Life expectancy: **+30.7 years** (56.9 → 87.6)
- Obesity rate: **−33.2 percentage points** (52.7% → 19.2% at the min)
- Home value: **26× difference** ($82K → $2.1M+)

---

## Figures Generated
- `figures/fig1_runscore_vs_homevalue.png` — Scatter plot, RunScore vs. home value (colored by income tercile)
- `figures/fig2_runscore_vs_health.png` — 2×2 panel, RunScore vs. obesity / diabetes / life expectancy / fair health
- `figures/fig3_deepdive_comparison.png` — Side-by-side bar chart of deep dive counties
- `figures/fig4_runscore_map.png` — US county choropleth map of RunScore

---

## Data Sources
| Dataset | Provider | Coverage |
|---|---|---|
| CDC PLACES 2023 | CDC | 3,143 counties |
| County Health Rankings 2025 | UW-RWJF | 3,143 counties |
| Zillow ZHVI Feb 2026 | Zillow | 3,073 counties |
| RunSignUp API 2019–2024 | RunSignUp | 17,810 races, 50 states |
| EPA National Walkability Index | EPA | 220,739 block groups |
| USDA Food Environment Atlas 2020 | USDA ERS | 3,144 counties |
