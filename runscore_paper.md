# RunScore: Running Activity as a Predictive Signal for Community Quality of Life and Real Estate Desirability

**Luke Popler**
Sequoia High School, Redwood City, California
lukepopler@gmail.com | 818038@seq.org

*April 2026*

---

## Abstract

This study introduces RunScore, a novel composite index measuring the running activity level and supporting infrastructure of U.S. counties. Using publicly available data across five domains — physical inactivity rates, organized race event density, exercise infrastructure access, fitness facility density, and neighborhood walkability — RunScore was computed for all 3,143 U.S. counties and validated against a broad set of quality-of-life outcomes. Bivariate analysis reveals strong correlations between RunScore and home values (Spearman r = +0.604), life expectancy (r = +0.582), obesity rates (r = −0.570), and diabetes prevalence (r = −0.676), all significant at p < 0.001. Multivariate OLS regression demonstrates that RunScore predicts county-level home values independently of median household income, unemployment, insurance coverage, and life expectancy (β = 0.0035, p < 0.001, ΔR² = +0.022). Each 10-point increase in RunScore is associated with a 3.5% increase in median home value — approximately $7,885 on a median county home. Critically, RunScore also predicts forward-looking home value appreciation: each 10-point increase is associated with 0.9 additional percentage points of five-year appreciation, controlling for income, employment, and urbanicity (β = 0.087, p < 0.001). These findings hold across metro and non-metro subgroups and after controlling for urbanicity. RunScore represents a replicable, low-cost lifestyle signal with direct applications for residential real estate platforms, urban planners, and public health agencies.

**Keywords:** running activity, quality of life, real estate, county health, composite index, physical activity, home values

---

## 1. Introduction

### 1.1 The Problem with Lifestyle Data in Real Estate

When someone decides where to live, they are not just buying a house — they are buying into a community. Buyers increasingly filter not just on price and square footage, but on walkability, outdoor access, school quality, safety, and the lifestyle culture of a neighborhood. Real estate platforms have responded by embedding third-party signals like Walk Score and school ratings directly into listings. Yet these signals are siloed: walkability tells you nothing about health culture, and school ratings say nothing about whether people in the community actually exercise.

There is currently no single, observable, publicly replicable signal that captures whether a community is physically active — whether the infrastructure, culture, and behavior around fitness actually exist on the ground. This gap matters because physical activity culture is among the most powerful predictors of the lifestyle outcomes buyers care about: health, safety, community cohesion, and long-term property value.

Running — more than any other form of exercise — is a uniquely observable community behavior. It requires public space, infrastructure, and cultural buy-in. Communities that run produce measurable signals: they register for races, they build trails, they invest in walkability, they support fitness facilities. These signals are public, consistent, and computable at geographic scale.

### 1.2 The RunScore Proposal

This paper develops and validates RunScore: a county-level composite index of running activity, infrastructure, and community engagement, computed for all 3,143 U.S. counties. RunScore is not a measure of individual behavior — it is a measure of community running culture. We then test whether RunScore predicts:

1. Health outcomes: obesity, diabetes, life expectancy, self-rated health
2. Residential real estate values: Zillow Home Value Index (ZHVI)
3. Broader quality-of-life indicators: walkability, park access, social capital

The central hypothesis is that RunScore captures something real about a community that income alone does not — and that this residual signal has independent predictive power for where people want to live and how healthy they are.

### 1.3 Motivation and Intended Audience

This research has two intended audiences. First, academic: it contributes to a literature on physical activity, community health, and residential location that has so far lacked a running-specific county-level index. Second, applied: real estate platforms, relocation agencies, and urban planners increasingly need richer lifestyle signals. RunScore is designed to be replicable at scale, updated annually, and embeddable in existing platforms as a neighborhood-level feature.

### 1.4 Research Questions

1. Does county-level running activity (RunScore) correlate with health outcomes net of income?
2. Does RunScore predict residential home values beyond what income and urbanicity explain?
3. Does RunScore predict *future* home value appreciation, functioning as a leading indicator for real estate markets?
4. Is the RunScore–home value relationship consistent across metro and non-metro counties?
5. What do extreme-case communities (high and low RunScore) reveal about the qualitative texture of running culture?

---

## 2. Background and Related Work

### 2.1 Physical Activity and Community Health

The relationship between physical activity and individual health is among the most replicated findings in epidemiology. Adults who meet recommended physical activity guidelines have substantially lower risk of cardiovascular disease, type 2 diabetes, depression, and premature death (Physical Activity Guidelines Advisory Committee, 2018). What is less studied is how *community-level* physical activity rates — aggregated across individuals — correlate with population health outcomes at geographic scale.

Joh et al. (2015) provide the most direct precedent for this study. Using CDC Behavioral Risk Factor Surveillance System (BRFSS) data for approximately 500 U.S. counties, they found that county-level physical activity rates were associated with lower obesity, lower diabetes prevalence, and longer life expectancy, with effects that persisted after controlling for socioeconomic factors. Their analysis was limited by BRFSS sample sizes in smaller counties and did not decompose physical activity by type.

The CDC PLACES dataset — a model-based extension of BRFSS using multilevel regression and poststratification (MRP) — has since extended county-level physical inactivity estimates to all 3,143 U.S. counties, enabling analyses at full national scale (Centers for Disease Control and Prevention, 2023).

### 2.2 Running Participation and Its Community Correlates

Running is the most common form of aerobic exercise in the United States, with an estimated 50 million participants in 2024 (Sports & Fitness Industry Association, 2024). Unlike gym-based exercise, running is inherently public: it requires outdoor space, infrastructure investment, and community engagement through race events and running clubs.

Prior research has found that walkable neighborhoods are associated with higher physical activity rates (Sallis et al., 2016), and that access to parks and trails is independently associated with recreational physical activity (Brownson et al., 2009). However, most of this literature operates at the individual level or focuses on specific cities rather than producing nationally comparable county-level indices.

The American College of Sports Medicine (ACSM) American Fitness Index provides the closest existing analog to RunScore, rating 100 large U.S. cities across 35 fitness and health metrics annually. The current study extends the concept to all 3,143 U.S. counties, uses a running-specific activity lens, and explicitly tests the connection to real estate outcomes — a link the ACSM index does not address.

### 2.3 Physical Activity and Residential Property Values

The relationship between fitness infrastructure and home values has been studied primarily through the lens of park access and walkability. Crompton (2001) reviewed evidence that parks increase adjacent property values by 8–20%, while Walk Score, the commercial walkability index, estimates that each one-point Walk Score increase is associated with a $3,000 increase in home value in urban areas (Leinberger & Alfonzo, 2012).

However, these studies focus on infrastructure proximity, not behavioral outcomes. A community could be highly walkable but sedentary; a rural trail community could have modest Walk Scores but vibrant running culture. Importantly, no prior study has examined whether a behaviorally-grounded measure of running community strength predicts home values at the county level across the full United States — or whether such a measure functions as a leading indicator of future home price appreciation, a question with direct commercial implications for residential real estate platforms.

### 2.4 Gap in the Literature

Taken together, existing research establishes that (1) physical activity is strongly associated with health outcomes, (2) fitness infrastructure is associated with higher home values, and (3) community-level behavioral norms shape individual outcomes. What is missing is an integrated, nationally comparable county-level index that captures running activity as a community behavior and validates it against both health and real estate outcomes simultaneously. RunScore fills this gap.

---

## 3. Data and Methods

### 3.1 Geographic Unit of Analysis

The county is the primary unit of analysis (n = 3,143 U.S. counties and county-equivalents). Counties are the smallest geographic unit for which a comprehensive suite of health, economic, and real estate data is publicly available. All datasets were joined using 5-digit Federal Information Processing Series (FIPS) codes as a universal geographic identifier.

### 3.2 RunScore Construction

RunScore is a composite index combining five standardized components. Each component captures a distinct dimension of running activity and infrastructure. All components were standardized to z-scores before combining, and RunScore is expressed as a percentile rank (0–100) across all counties.

**Component 1 — Physical Activity Level**
Source: CDC PLACES 2023. Variable: percentage of adults with no leisure-time physical activity (LPA), model-based estimates for all 3,143 counties using multilevel regression and poststratification from BRFSS. The LPA rate was inverted so that higher scores indicate more active communities.

**Component 2 — Race Event Density**
Source: RunSignUp public API, queried for all 50 states for race events from 2019–2024. Event types included running races, trail races, ultramarathons, and running-only events. 17,810 unique races were identified and geocoded using a ZIP code–to–FIPS crosswalk (Census Bureau ZCTA-to-county relationship file, 2020). Race counts were normalized per 100,000 county population.

**Component 3 — Exercise Infrastructure Access**
Source: County Health Rankings 2025 (University of Wisconsin Population Health Institute / Robert Wood Johnson Foundation). Variable: percentage of county residents with adequate access to exercise opportunities (v132), derived from physical activity facility databases.

**Component 4 — Fitness Facility Density**
Source: USDA Food Environment Atlas 2020. Variable: recreational facilities and fitness centers per 1,000 population (NAICS code 713940), derived from the Census County Business Patterns. Counties with missing values (n = 1,849, predominantly very rural) were assigned zero, consistent with the interpretation that no tracked facilities exist.

**Component 5 — Neighborhood Walkability**
Source: EPA National Walkability Index (Smart Location Database, June 2021). Block group–level walkability scores (1–20) were aggregated to the county level using population-weighted means across 220,739 census block groups covering 3,233 U.S. counties.

**Composite Score**
The five standardized components were averaged with equal weights to produce a raw composite. Counties were then ranked by percentile to produce RunScore (0–100), where 100 represents the county at the highest percentile of running activity and infrastructure nationally. Sensitivity analyses with alternative weighting schemes produced substantively similar results (not shown; available upon request).

### 3.3 Outcome Variables

**Health outcomes** were drawn from CDC PLACES 2023 (obesity, diabetes, hypertension, depression, fair/poor health, physical inactivity) and the Institute for Health Metrics and Evaluation Global Burden of Disease study via the County Health Rankings 2025 dataset (life expectancy, premature death rate).

**Real estate outcomes** were drawn from Zillow Research (Zillow Home Value Index, ZHVI, as of February 2026, covering 3,073 counties). ZHVI is a model-based estimate of the median home value at the 35th–65th percentile tier. One-year and five-year appreciation rates were computed from the same series. Five-year appreciation serves as the dependent variable in a separate forward-looking analysis testing whether RunScore functions as a leading indicator of home price growth.

**Socioeconomic controls** included median household income, unemployment rate, and percentage uninsured from the County Health Rankings 2025 dataset (derived from Census ACS, BLS, and BRFSS respectively).

**Urbanicity** was measured using the USDA Rural-Urban Continuum Code (RUCC, 2023), a 9-category scale ranging from 1 (counties in metro areas with populations over 1 million) to 9 (completely rural counties not adjacent to a metro area).

### 3.4 Statistical Analysis

**Bivariate analysis:** Spearman rank correlation coefficients were computed between RunScore and each outcome variable. Spearman correlation was chosen over Pearson given the non-normal distribution of home values and the ordinal nature of some variables.

**Multivariate regression:** Ordinary least squares (OLS) regression was used to model the log-transformed Zillow ZHVI as a function of log median household income, unemployment rate, percentage uninsured, life expectancy, RUCC urbanicity score, and RunScore. Heteroskedasticity-consistent (HC3) standard errors were used throughout. Home values were log-transformed to address right skew; the RunScore coefficient is interpreted as: a one-unit increase in RunScore is associated with a [exp(β) − 1] × 100 percent increase in home value, holding all other variables constant.

Health outcome regressions used OLS with the raw rate (not log-transformed) as the dependent variable, controlling for log median household income. Incremental R² was computed to assess RunScore's contribution beyond income alone.

**Robustness checks:** The primary regression was re-estimated (1) with RUCC urbanicity as an additional control, (2) restricted to metro counties only (RUCC 1–3, n = 1,174), and (3) restricted to non-metro counties only (RUCC 4–9, n = 1,843).

**Community profiles:** Eight counties were selected as deep-dive case studies representing the extremes of the RunScore distribution, spanning a range of income levels, population sizes, and urbanicity classifications.

---

## 4. Results

### 4.1 RunScore Distribution

RunScore ranges from 0.03 to 100 across 3,143 U.S. counties (mean = 50.0, SD = 28.9 by construction). The distribution is approximately uniform — a consequence of the percentile-rank transformation — with modest geographic clustering. High-RunScore counties are concentrated in the Northeast corridor (Virginia suburbs, Massachusetts coastal communities), the Mountain West (Montana, Wyoming, Colorado, Utah), the Pacific Northwest (Washington), and dense coastal metros (Manhattan, the San Francisco Bay Area).

Low-RunScore counties are concentrated in the rural Deep South (Mississippi, Alabama, Louisiana, Arkansas), the Texas Panhandle, and the Northern Great Plains. The lowest-scoring counties are characterized by very high physical inactivity rates (often 40–50%), zero organized race events, minimal exercise infrastructure, and near-zero walkability.

**Table 1: Top 10 and Bottom 10 Counties by RunScore**

| Rank | County | State | RunScore | Inactive % | Races/100k | Home Value |
|---|---|---|---|---|---|---|
| 1 | Nantucket | MA | 99.9 | 17.2% | 41.5 | $3,029,344 |
| 2 | Falls Church | VA | 99.9 | 15.8% | 0.0 | — |
| 3 | Teton | WY | 99.8 | 18.3% | 21.5 | $2,147,757 |
| 4 | San Juan | WA | 99.8 | 15.8% | 48.5 | — |
| 5 | New York | NY | 99.8 | 20.4% | 3.9 | $1,217,413 |
| 6 | Arlington | VA | 99.7 | 14.8% | 7.7 | — |
| 7 | Gallatin (Bozeman) | MT | 99.5 | 13.9% | 19.0 | $689,955 |
| 8 | Missoula | MT | 99.5 | 16.5% | 18.9 | $559,508 |
| 9 | King (Seattle) | WA | 99.5 | 13.9% | 6.5 | — |
| 10 | District of Columbia | DC | 99.6 | 14.9% | 0.2 | — |
| ... | | | | | | |
| 3134 | Tensas | LA | 0.5 | 56.9% | 0.0 | — |
| 3135 | Stewart | GA | 0.5 | 60.8% | — | — |
| 3136 | Issaquena | MS | 0.4 | 59.0% | 0.0 | — |
| 3137 | Wilkinson | MS | 0.4 | 58.2% | 0.0 | — |
| 3138 | Zapata | TX | 0.4 | 52.9% | 0.0 | — |
| 3139 | Oglala Lakota | SD | 0.3 | 40.1% | 0.0 | — |
| 3140 | Hancock | GA | 0.3 | 60.0% | 0.0 | — |
| 3141 | Kenedy | TX | 0.3 | 59.8% | 0.0 | — |
| 3142 | Humphreys | MS | 0.1 | 47.9% | 0.0 | $82,469 |
| 3143 | Greene | AL | 0.0 | 44.7% | 0.0 | $125,975 |

*Note: Home values not available for all counties in Zillow dataset (predominantly very rural counties).*

### 4.2 Bivariate Correlations

**Table 2: Spearman Rank Correlations Between RunScore and Key Outcomes**

| Outcome | Spearman r | n | Significance |
|---|---|---|---|
| Exercise access | +0.807 | 3,097 | p < 0.001 |
| EPA Walkability Index | +0.761 | 3,132 | p < 0.001 |
| Physical inactivity | −0.733 | 2,956 | p < 0.001 |
| Smoking rate | −0.710 | 2,956 | p < 0.001 |
| Fair/poor health | −0.673 | 2,956 | p < 0.001 |
| Diabetes rate | −0.676 | 2,956 | p < 0.001 |
| Hypertension rate | −0.648 | 2,956 | p < 0.001 |
| Heart disease rate | −0.645 | 2,956 | p < 0.001 |
| Median household income | +0.634 | 3,142 | p < 0.001 |
| Home value (ZHVI) | +0.604 | 3,064 | p < 0.001 |
| Life expectancy | +0.582 | 3,060 | p < 0.001 |
| Obesity rate | −0.570 | 2,956 | p < 0.001 |
| Premature death (YPLL) | −0.560 | 3,080 | p < 0.001 |
| Park access | +0.554 | 2,846 | p < 0.001 |
| 5-year home appreciation | +0.186 | 3,013 | p < 0.001 |
| 1-year home appreciation | +0.142 | 3,064 | p < 0.001 |
| Social associations per 10k | −0.013 | 3,143 | n.s. |

The strongest bivariate correlations are with exercise access (r = +0.807) and walkability (r = +0.761), which are partial inputs to RunScore and serve as validation checks. The correlation with physical inactivity (r = −0.733) further validates internal consistency. Among outcome variables, the correlations with smoking (r = −0.710), diabetes (r = −0.676), fair/poor health (r = −0.673), and home values (r = +0.604) are all substantively large and statistically significant across more than 2,900 counties. The strong negative correlations with cardiovascular risk factors — hypertension (r = −0.648), heart disease (r = −0.645) — underscore that RunScore captures health dimensions well beyond obesity.

Both measures of home value appreciation are positively correlated with RunScore (five-year: r = +0.186; one-year: r = +0.142; both p < 0.001), providing initial evidence that RunScore may function as a leading indicator of real estate market growth.

Notably, social associations per 10,000 residents — a measure of civic and community organization density — does not correlate with RunScore (r = −0.013, n.s.), suggesting RunScore captures behavioral and infrastructural dimensions of community fitness rather than generalized social capital.

### 4.3 RunScore and Home Values

**Table 3: OLS Regression — Log(Home Value) as Dependent Variable**

| | Model 1 | Model 2 | Model 3 |
|---|---|---|---|
| | Income only | + Controls | + RunScore |
| **Constant** | −5.539*** | −6.475*** | −3.935*** |
| **Log(Median Income)** | 1.617*** | 1.488*** | 1.279*** |
| **% Unemployed** | | 5.000*** | 4.356*** |
| **% Uninsured** | | 1.237*** | 1.505*** |
| **Life Expectancy** | | 0.027*** | 0.022*** |
| **RunScore** | | | **0.0035***\*** |
| **N** | 3,017 | 3,017 | 3,017 |
| **R²** | 0.578 | 0.611 | **0.633** |
| **Adj. R²** | 0.578 | 0.610 | 0.632 |

*Standard errors HC3-robust. \* p < 0.05; ** p < 0.01; \*\*\* p < 0.001*

Income alone explains 57.8% of the variance in county-level home values (Model 1). Adding unemployment, insurance coverage, and life expectancy increases explained variance to 61.1% (Model 2). Adding RunScore increases R² to 63.3% — a statistically significant increment of +2.2 percentage points (F-test for ΔR², p < 0.001). The RunScore coefficient (β = 0.0035) is significant at p < 0.001 and remains stable across specifications, indicating that it captures independent signal not already accounted for by income or health controls.

**Interpretation of the RunScore coefficient in dollar terms:**

Each 10-point increase in RunScore is associated with a 3.5% increase in median home value, holding income, unemployment, insurance, and life expectancy constant. Evaluated at the sample median home value of $223,928:

- **+10 RunScore points → +3.5% → +$7,885** in home value
- **+25 RunScore points → +9.0% → +$20,237** in home value
- **+50 RunScore points → +18.9% → +$42,304** in home value

### 4.4 RunScore and Health Outcomes

**Table 4: RunScore Coefficient in Health Outcome Regressions (Controlling for Log Income)**

| Outcome | β (per RunScore point) | SE | t | p | ΔR² |
|---|---|---|---|---|---|
| Smoking rate (%) | −0.0477 | 0.0019 | −24.64 | <0.001 | +0.093 |
| Hypertension (%) | −0.0640 | 0.0032 | −20.13 | <0.001 | +0.069 |
| Obesity rate (%) | −0.0532 | 0.0030 | −17.68 | <0.001 | +0.062 |
| Heart disease (%) | −0.0161 | 0.0009 | −17.60 | <0.001 | +0.057 |
| Diabetes rate (%) | −0.0294 | 0.0015 | −19.74 | <0.001 | +0.056 |
| Fair/poor health (%) | −0.0472 | 0.0023 | −20.20 | <0.001 | +0.048 |
| Poor sleep (%) | −0.0262 | 0.0030 | −8.76 | <0.001 | +0.020 |
| Life expectancy (yrs) | +0.0196 | 0.0021 | +9.29 | <0.001 | +0.014 |
| Premature death (YPLL) | −19.75 | 2.40 | −8.23 | <0.001 | +0.013 |

*All regressions control for log median household income. n = 2,955–3,142.*

RunScore adds significant explanatory power beyond income for every health outcome tested. The strongest incremental contribution is for smoking (ΔR² = +0.093), suggesting that running culture captures a dimension of health behavior that income alone does not. A county moving from the 25th to the 75th percentile of RunScore (a 50-point increase) is associated with:
- **3.2 percentage points lower hypertension**
- **2.7 percentage points lower obesity rate**
- **2.4 percentage points lower smoking rate**
- **1.5 percentage points lower diabetes rate**
- **2.4 percentage points lower fair/poor health rate**
- **+1.0 year of life expectancy**

These effect sizes are clinically and policy-relevant. A 2.7 percentage point reduction in obesity, applied to the median county population of ~25,000 adults, corresponds to approximately 675 fewer adults with obesity.

### 4.5 Robustness Checks

**Table 5: RunScore Coefficient Across Robustness Specifications**

| Model | N | R² | RunScore β | SE | p |
|---|---|---|---|---|---|
| Base (no RUCC) | 3,017 | 0.633 | 0.00346 | 0.00025 | <0.001 |
| + RUCC urbanicity control | 3,017 | 0.641 | 0.00276 | 0.00027 | <0.001 |
| Metro counties only (RUCC 1–3) | 1,174 | 0.702 | 0.00229 | 0.00033 | <0.001 |
| Non-metro counties only (RUCC 4–9) | 1,843 | 0.486 | 0.00374 | 0.00038 | <0.001 |

RunScore remains significant at p < 0.001 in all specifications. Adding the RUCC urbanicity score as a control — which is itself significantly negative (β = −0.020, p < 0.001, indicating that more rural counties have lower home values) — attenuates the RunScore effect only slightly (from 0.00346 to 0.00276), confirming that RunScore captures signal beyond urbanicity alone.

The non-metro finding is particularly noteworthy: among rural counties alone, RunScore is a stronger predictor (β = +0.00374) than among metro counties (β = +0.00229). This suggests that running culture adds disproportionate value in rural communities — outdoor recreation towns like Bozeman, MT and Missoula, MT outperform their income levels on both health and real estate. For real estate platforms, this implies that RunScore provides the most incremental information precisely where existing signals (Walk Score, transit data) have the thinnest coverage.

### 4.6 RunScore and Home Value Appreciation

The preceding analysis establishes that RunScore is associated with *current* home values. A more commercially relevant question for real estate platforms is whether RunScore predicts *future* home value growth — that is, whether it functions as a leading indicator.

**Table 6: OLS Regression — 5-Year Home Value Appreciation (%) as Dependent Variable**

| Variable | β | SE | p |
|---|---|---|---|
| **Constant** | −25.69 | 23.53 | 0.275 |
| **Log(Median Income)** | 3.29 | 2.55 | 0.197 |
| **% Unemployed** | −186.82*** | 33.53 | <0.001 |
| **% Uninsured** | −22.65** | 8.33 | 0.007 |
| **Life Expectancy** | 0.30 | 0.17 | 0.076 |
| **RunScore** | **0.087***\*** | **0.015** | **<0.001** |
| **RUCC** | 0.06 | 0.14 | 0.680 |
| **N** | 2,983 | | |
| **R²** | 0.093 | | |

*HC3 robust standard errors. \* p < 0.05; ** p < 0.01; \*\*\* p < 0.001*

RunScore is a significant predictor of five-year home value appreciation (β = 0.087, p < 0.001), even after controlling for income, employment, insurance, life expectancy, and urbanicity. Notably, income itself is *not* significant in this model — appreciation is driven by factors beyond current wealth. RunScore stands out as one of the strongest individual predictors.

**Interpretation:**
- **+10 RunScore points → +0.9 percentage points** of 5-year appreciation
- **+25 RunScore points → +2.2 percentage points** of 5-year appreciation
- **+50 RunScore points → +4.3 percentage points** of 5-year appreciation

For a $300,000 home, a 25-point RunScore advantage implies approximately $6,600 of additional five-year price growth — above and beyond what income and demographics predict. This finding directly supports the use of RunScore as a forward-looking signal for real estate investment and relocation decisions.

### 4.7 Community Deep Dives

To ground the quantitative findings, eight counties were selected for qualitative and quantitative profiling across the RunScore spectrum.

**Table 7: Community Deep Dive Profiles**

| Community | RunScore | Inactive % | Obese % | Diabetic % | Life Exp. | Home Value | 5yr Appr. | Income |
|---|---|---|---|---|---|---|---|---|
| Teton County, WY (Jackson Hole) | 99.8 | 18.3% | 24.0% | 8.4% | 87.6 yrs | $2,147,757 | +67.5% | $130,156 |
| Gallatin County, MT (Bozeman) | 99.5 | 13.9% | 23.0% | 6.7% | 82.0 yrs | $689,955 | +31.8% | $90,942 |
| Missoula County, MT | 99.5 | 16.5% | 26.2% | 8.3% | 78.6 yrs | $559,508 | +44.5% | $72,882 |
| Nantucket County, MA | 99.9 | 17.2% | 27.7% | 8.6% | 82.8 yrs | $3,029,344 | +48.7% | $108,671 |
| New York County, NY (Manhattan) | 99.8 | 20.4% | 19.2% | 8.9% | 83.0 yrs | $1,217,413 | −9.3% | $100,869 |
| Humphreys County, MS | 0.1 | 47.9% | 52.4% | 24.7% | 66.6 yrs | $82,469 | +7.0% | $31,538 |
| Greene County, AL | 0.0 | 44.7% | 52.7% | 27.1% | 70.6 yrs | $125,975 | −2.9% | $34,619 |
| Oglala Lakota County, SD | 0.2 | 40.1% | 47.0% | 21.1% | 56.9 yrs | N/A | N/A | $42,791 |

*Home value = Zillow ZHVI Feb 2026. Greene County, AL has RUCC 2 (metro-adjacent) despite very rural character — a known classification artifact.*

The range across extremes is stark. Teton County, Wyoming — home to Jackson Hole — has a life expectancy of 87.6 years, the longest of any county in this study. Obesity stands at 24.0% and diabetes at 8.4%. Median home values exceed $2.1 million and have appreciated 67.5% over the past five years — the highest appreciation rate among the profiled counties.

Oglala Lakota County, South Dakota — home to the Pine Ridge Indian Reservation — has a life expectancy of 56.9 years, among the shortest in the United States and comparable to some developing nations. Obesity affects 47.0% of adults. There are no organized running races. Exercise access stands at 1.9%. Median household income is $42,791 — modest, but not the lowest in this comparison.

The case of Missoula County, MT is instructive. With a median household income of $72,882 — well below Nantucket's $108,671 — Missoula achieves a nearly identical RunScore (99.5 vs. 99.9) and comparable health outcomes (life expectancy 78.6 years, obesity 26.2%). Home values of $559,508 and 44.5% five-year appreciation reflect strong demand for a community that has built running culture through a university presence, trail networks, and race event density — not primarily through wealth.

The appreciation data reinforces the leading-indicator finding from Section 4.6. Among the high-RunScore counties, four of five show five-year appreciation rates exceeding 30% — with Teton at 67.5% and Nantucket at 48.7%. Among the low-RunScore counties, appreciation is near zero or negative. The exception — Manhattan's −9.3% decline — reflects COVID-era urban-to-suburban migration patterns specific to ultra-dense metros, not a failure of the RunScore signal.

This pattern — outdoor recreation communities achieving health and real estate outcomes that exceed what income would predict — recurs throughout the high-RunScore tier and is consistent with both the regression finding that RunScore's home value effect is larger in non-metro counties and the appreciation regression showing RunScore as a forward-looking predictor.

---

## 5. Discussion

### 5.1 What RunScore Actually Measures

RunScore is not purely a measure of how much people run. It is a measure of whether a community has built the conditions — infrastructure, culture, events, facilities, walkable streets — that make running a normal, accessible part of daily life. These conditions are correlated with each other and with running behavior, but they also independently predict outcomes.

A community with high RunScore is one where the sidewalks are there, the trails are there, the gym is nearby, and the local race calendar gives people a reason to train. These conditions make running easy. They also make it normal — which matters for behavior change in ways that simply having one element (a walkable downtown, or one local race) does not.

This is why RunScore predicts home values even after controlling for income. High-RunScore communities have made specific, observable investments in the built environment and community programming that buyers want to live in — and they reveal this preference through the prices they pay.

### 5.2 The Real Estate Implication

The finding that each 10-point increase in RunScore is associated with a 3.5% increase in home values, holding income constant, has direct practical implications. But the more commercially significant finding is the appreciation result: RunScore predicts *future* home value growth (β = 0.087 per point, p < 0.001) even when income does not. This transforms RunScore from a descriptive label into a predictive signal.

For real estate platforms, RunScore is a feature that belongs alongside Walk Score and school ratings in listing data. It captures a dimension of neighborhood desirability — active lifestyle infrastructure — that none of the existing signals fully address. Walk Score measures pedestrian convenience. School ratings measure educational outcomes. Crime statistics measure safety. RunScore measures whether a community has built the conditions for a physically active lifestyle — a preference that has grown consistently since the early 2000s and accelerated through the COVID-19 pandemic's reshaping of residential priorities.

The appreciation regression (Section 4.6) provides the strongest commercial argument: each 10-point RunScore increase predicts 0.9 additional percentage points of five-year appreciation, controlling for income, employment, and urbanicity. Communities building the conditions for high RunScore are attracting buyers whose revealed preferences drive price growth — and this effect is measurable, predictive, and updatable annually from public data.

### 5.3 Practical Implementation for Real Estate Platforms

RunScore is designed for direct integration into residential real estate platforms. The implementation path is straightforward:

**Listing-level display.** RunScore can be displayed as a 0–100 badge on individual property listings, analogous to Walk Score. A county-level score is available for all 3,143 U.S. counties today; ZIP code– and census tract–level resolution (see Section 5.6, Future Work) would enable within-county variation for metro areas.

**Search and filter.** Buyers searching for active-lifestyle communities could filter by minimum RunScore, or sort listings by RunScore within a price range. This addresses a gap in current platform search: no existing filter captures "communities where people actually exercise."

**Relocation and lifestyle matching.** For buyers relocating across metro areas, RunScore provides a single comparable number across the full United States. A buyer leaving a RunScore-85 community can identify comparable communities in their target region — a use case no current platform signal supports.

**Investment and valuation.** The appreciation regression suggests RunScore as a forward-looking signal for home value growth. Counties with rising RunScore components (new trail construction, increasing race event density, fitness facility openings) may represent investment opportunities — analogous to how Walk Score improvements have been shown to predict price growth.

**Data pipeline.** All five RunScore components are derived from publicly available, annually updated datasets. The computational pipeline requires no proprietary data, no API licensing fees, and no survey infrastructure. A platform could compute and publish RunScore nationally for negligible marginal cost.

### 5.4 The Public Health Implication

The independent association between RunScore and nine health outcomes — including smoking (ΔR² = +0.093), hypertension (+0.069), obesity (+0.062), and diabetes (+0.056) — after controlling for income supports the interpretation that running infrastructure and culture have their own health effects, beyond the health effects of income itself. The breadth of health outcomes predicted by RunScore — spanning behavioral (smoking), metabolic (obesity, diabetes), cardiovascular (hypertension, heart disease), and longevity (life expectancy, premature death) domains — suggests it captures a generalizable dimension of community health culture, not just running behavior.

This does not establish causality. High-RunScore communities may attract healthier residents rather than making existing residents healthier. Wealthier, younger, and more health-conscious movers may select into places with better running infrastructure, generating the correlation without direct causal impact. Establishing causality would require quasi-experimental designs exploiting natural variation in infrastructure investment — a direction for future work.

What can be said is that the RunScore–health correlation is large, robust, and present even within income strata. Counties that are poor but have relatively high RunScore are healthier than poor counties with low RunScore. Counties that are affluent but have low RunScore are less healthy than their income level would predict. These patterns are consistent with a causal interpretation but do not prove it.

### 5.5 Limitations

Several limitations constrain interpretation of these findings.

**Small-county artifacts in rankings.** The race event density component (Component 2) is normalized per 100,000 population. In very small counties (population under 5,000), a single race event produces an outsized per-capita rate. For example, the highest-ranked county by raw RunScore — Charles City, VA (population 6,610) — achieves 348 races per 100,000 due to a small number of events in a small population. This does not invalidate the regression analysis, where these counties have negligible leverage, but it affects the interpretability of the top-ranked counties list. Future versions should consider a population floor or Bayesian shrinkage estimator for the race density component.

**Data coverage.** Zillow ZHVI data is unavailable for the most rural counties — predominantly those with very thin real estate markets. Fitness facility data from the USDA Atlas is missing for 1,849 counties, replaced with zero. Missing data is not random; it is concentrated in less-populated, lower-income, more rural counties that tend toward low RunScore — potentially attenuating the true effect sizes.

**RunSignUp representativeness.** The RunSignUp API captures 17,810 running events from 2019–2024, but not all organized races in the United States are listed on RunSignUp. Platform penetration varies by region and event size, which may systematically undercount races in areas where other registration platforms (e.g., ACTIVE.com) dominate.

**Strava data absence.** The optimal Component 2 of RunScore would be actual running trip counts from Strava Metro — aggregate GPS-track data reflecting all running activity, not just organized racing. A Strava Metro academic cohort application is pending. Strava data would capture recreational running that produces no race registrations, likely strengthening the measure substantially.

**Reverse causality.** High home values may attract wealthier, healthier, more active populations — generating the correlation without RunScore causing higher values. The appreciation regression (Section 4.6) provides partial mitigation: RunScore predicts *future* price growth, not just current levels. However, a fully causal design would require quasi-experimental variation in infrastructure investment.

**Selection bias.** People who prioritize running culture select into high-RunScore communities. Observed health differences between high- and low-RunScore communities may reflect selection of healthier individuals rather than health effects of the environment itself.

### 5.6 Future Work

Priority extensions of this research include:

1. **Strava Metro integration.** Incorporating actual GPS trip counts (pending cohort application) to replace modeled physical inactivity proxies with observed running behavior. This would strengthen the measure substantially and enable time-series analysis of running activity trends.
2. **Sub-county resolution.** Applying RunScore methodology at the ZIP code or census tract level — the resolution most relevant for individual listing-level real estate applications. CDC PLACES and the EPA Walkability Index already provide tract-level data; RunSignUp events can be geocoded to ZIP codes. A tract-level RunScore could be embedded directly in property listings.
3. **Longitudinal panel design.** Testing whether *changes* in RunScore components (e.g., new trail construction, fitness facility openings, race event growth) predict subsequent home price appreciation, controlling for baseline values. This design would provide stronger causal evidence and directly operationalize RunScore as an investment signal.
4. **Causal identification.** Using natural experiments — trail construction bond measures, rail-trail conversions, parkrun establishment — to estimate causal effects of running infrastructure on health and property values. The parkrun quasi-experimental literature (Morris & Weed, 2023) provides a methodological template.
5. **Platform integration pilot.** Partnering with a residential real estate platform to display RunScore alongside existing neighborhood signals and measuring user engagement, search behavior changes, and buyer satisfaction with community lifestyle fit.

---

## 6. Conclusion

This study introduces RunScore, a five-component composite index of county-level running activity and infrastructure, computed for all 3,143 U.S. counties. RunScore demonstrates strong bivariate correlations with home values (r = +0.604), life expectancy (r = +0.582), obesity (r = −0.570), and diabetes (r = −0.676). In multivariate regression, RunScore predicts county-level home values independently of median household income, unemployment, insurance coverage, life expectancy, and urbanicity. Each 10-point increase in RunScore is associated with a 3.5% increase in median home value — approximately $7,885 on a median county home. This effect holds across metro and non-metro subgroups and is robust to a range of control specifications.

Critically, RunScore also predicts future home value growth: each 10-point increase is associated with 0.9 additional percentage points of five-year appreciation, controlling for income, employment, and urbanicity. This forward-looking predictive power — present even when income itself is not a significant predictor of appreciation — transforms RunScore from a descriptive community label into an actionable market signal.

RunScore fills a gap in the existing landscape of community metrics: it is the first nationally comparable, county-level index to capture running activity as a community behavior and validate it against both health and real estate outcomes simultaneously. It is replicable from public data, updatable annually, and directly embeddable in residential real estate platforms as a lifestyle desirability signal. The methodology is open, the data pipeline requires no proprietary inputs, and the computational cost is negligible at scale.

The 30-year gap in life expectancy between Oglala Lakota County, SD (56.9 years) and Teton County, WY (87.6 years) — two counties in the same country — is not explained by running. But running culture, and the infrastructure and investment decisions that produce it, is one measurable dimension of what makes some communities places where people live long, healthy lives and others places where they do not. RunScore is a way to see and compare that dimension at scale.

---

## References

Morris, P., & Weed, M. (2023). parkrun: Much more than just a run in the park. *British Journal of Sports Medicine*, 57(9), 517–518.

Brownson, R. C., Boehmer, T. K., & Luke, D. A. (2005). Declining rates of physical activity in the United States: What are the contributors? *Annual Review of Public Health*, 26, 421–443.

Brownson, R. C., Hoehner, C. M., Day, K., Forsyth, A., & Sallis, J. F. (2009). Measuring the built environment for physical activity: State of the science. *American Journal of Preventive Medicine*, 36(4), S99–S123.

Centers for Disease Control and Prevention. (2023). *PLACES: Local data for better health, county data 2023 release*. CDC. https://www.cdc.gov/places

Crompton, J. L. (2001). The impact of parks on property values: A review of the empirical evidence. *Journal of Leisure Research*, 33(1), 1–31.

Joh, K., Nguyen, M. T., & Boarnet, M. G. (2015). Rate of physical activity and community health: Evidence from U.S. counties. *Journal of Planning Education and Research*, 35(1), 5–17.

Leinberger, C. B., & Alfonzo, M. (2012). *Walk this way: The economic promise of walkable places in metropolitan Washington, DC*. Brookings Institution.

Physical Activity Guidelines Advisory Committee. (2018). *2018 physical activity guidelines advisory committee scientific report*. U.S. Department of Health and Human Services.

Robert Wood Johnson Foundation / University of Wisconsin Population Health Institute. (2025). *County Health Rankings & Roadmaps: 2025 national data*. https://www.countyhealthrankings.org

Sallis, J. F., Bull, F., Guthold, R., Heath, G. W., Inoue, S., Kelly, P., … & Hallal, P. C. (2016). Progress in physical activity over the Olympic quadrennium. *The Lancet*, 388(10051), 1325–1336.

Sports & Fitness Industry Association. (2024). *2024 SFIA topline participation report*. SFIA.

U.S. Environmental Protection Agency. (2021). *National Walkability Index: Methodology and user guide*. Office of Sustainable Communities, Smart Growth Program.

U.S. Department of Agriculture, Economic Research Service. (2020). *Food environment atlas*. https://www.ers.usda.gov/data-products/food-environment-atlas

Zillow Research. (2026). *Zillow Home Value Index (ZHVI): Data methodology and downloads*. https://www.zillow.com/research/data

---

## Appendix A — RunScore Data Table (Sample)

*Full county-level RunScore data for all 3,143 U.S. counties is available in the accompanying dataset file `master_county.csv`.*

| FIPS | County | State | RunScore | Inactive % | Races/100k | Exercise Access | Walkability | Facilities/1k |
|---|---|---|---|---|---|---|---|---|
| 56039 | Teton | WY | 99.8 | 18.3% | 21.5 | 99.2% | 7.28 | 0.596 |
| 30031 | Gallatin | MT | 99.5 | 13.9% | 19.0 | 86.8% | 10.88 | 0.257 |
| 30063 | Missoula | MT | 99.5 | 16.5% | 18.9 | 90.9% | 11.71 | 0.271 |
| 25019 | Nantucket | MA | 99.9 | 17.2% | 41.5 | 94.5% | 13.90 | 0.527 |
| 36061 | New York | NY | 99.8 | 20.4% | 3.9 | 100.0% | 13.75 | 0.368 |
| 28053 | Humphreys | MS | 0.1 | 47.9% | 0.0 | 1.0% | 5.77 | — |
| 01063 | Greene | AL | 0.0 | 44.7% | 0.0 | 4.0% | 3.86 | — |
| 46102 | Oglala Lakota | SD | 0.2 | 40.1% | 0.0 | 1.9% | 3.82 | — |

---

## Appendix B — Regression Output Tables

*Full regression coefficient tables with all control variables are reported in Section 4.3 and 4.5 of the main text. Additional model specifications available upon request.*

---

## Appendix C — Data Sources and Access

| Dataset | Provider | Year | N | Access |
|---|---|---|---|---|
| CDC PLACES — Physical Inactivity (LPA) | Centers for Disease Control | 2023 | 3,143 counties | Free download: data.cdc.gov |
| County Health Rankings | UW-RWJF | 2025 | 3,143 counties | Free download: countyhealthrankings.org |
| Zillow Home Value Index (ZHVI) | Zillow Research | Feb 2026 | 3,073 counties | Free download: zillow.com/research/data |
| RunSignUp Race Events | RunSignUp | 2019–2024 | 17,810 events, 50 states | Free open API: runsignup.com/rest |
| EPA National Walkability Index | U.S. EPA | 2021 | 220,739 block groups | Free download: epa.gov/smartgrowth |
| USDA Food Environment Atlas | USDA ERS | 2020 | 3,144 counties | Free download: ers.usda.gov |
| USDA Rural-Urban Continuum Codes | USDA ERS | 2023 | 3,233 counties | Free download: ers.usda.gov |
| Census ZCTA-County Crosswalk | U.S. Census Bureau | 2020 | All ZCTAs | Free download: census.gov |
