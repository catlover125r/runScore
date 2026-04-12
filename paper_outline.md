# RunScore Research Paper — Outline
*Audience: Real estate platforms (Zillow, Redfin), relocation agencies, urban planners, developers*
*Core claim: A community's running activity level (RunScore) is a strong, measurable predictor of the quality-of-life features home buyers actually value.*

---

## Title (working)
**"RunScore: Running Activity as a Predictive Signal for Community Quality of Life and Real Estate Desirability"**

---

## Abstract (500 words)
- Introduce RunScore as a novel composite index of running activity frequency at the U.S. county level
- State the problem: buyers want walkable, healthy, safe, high-opportunity communities — but no single signal captures all of this
- State the finding: running activity correlates strongly with home values, school quality, health outcomes, and walkability
- Implication: RunScore is a low-cost, observable leading indicator for the features that drive real estate demand

---

## 1. Introduction
### 1.1 Motivation
- Home buyers increasingly prioritize lifestyle fit: walkability, outdoor access, safety, good schools, health-conscious neighbors
- Existing signals (school ratings, crime stats) are lagged, siloed, and hard to synthesize
- Running activity is a measurable, public-domain behavior signal that reflects community investment in health infrastructure, safety, and outdoor culture

### 1.2 Research Questions
1. Does county-level running activity correlate with health outcomes (obesity, chronic disease)?
2. Does RunScore predict real estate values and rent levels beyond what income alone explains?
3. Does RunScore align with school quality, walkability, and low crime rates?
4. Can RunScore serve as a single-number lifestyle proxy for home buyers and real estate platforms?

### 1.3 Contribution
- First study to quantize running activity at the U.S. county level and validate it against a broad QoL variable set
- Provides a replicable methodology that platforms like Zillow could operationalize at scale
- Fills the gap between individual fitness data (Strava) and community-level decision-making

---

## 2. Background & Related Work
### 2.1 Physical Activity and Community Health
- PMID 26595939: "Rate of Physical Activity and Community Health: Evidence From U.S. Counties" (2015) — most direct precedent
- CDC PLACES data on leisure-time physical inactivity as a community health marker
- County Health Rankings methodology (UW-RWJF) — 80+ measures rolled into composite scores

### 2.2 Walkability and Real Estate Value
- Literature on Walk Score / EPA Walkability Index as home price predictor
- Active transportation infrastructure and property premiums
- Trust for Public Land ParkScore and urban livability

### 2.3 Existing Composite QoL Indices
- ACSM American Fitness Index (100 cities, 35 metrics) — closest analog; our study extends to all 3,144 counties
- County Health Rankings, Social Vulnerability Index, Child Opportunity Index
- Gap: none of these use running-specific activity as an input

### 2.4 Data Limitations & Prior Approaches
- Self-report bias in BRFSS / CDC PLACES (MRP-modeled)
- Strava selection bias (wealthier, younger, urban users)
- RunSignUp as an objective behavioral proxy for running community engagement

---

## 3. Data & Methods
### 3.1 Geographic Unit of Analysis
- U.S. county (n ≈ 3,144); FIPS codes as universal join key
- City-level deep dives for qualitative profiles (Section 7)

### 3.2 RunScore Construction
**Component 1 — Physical Inactivity Proxy (inverted)**
- Source: CDC PLACES LPA (% adults with no leisure-time physical activity)
- Transformation: invert so higher score = more active community

**Component 2 — Running Community Engagement**
- Source: RunSignUp API → race events and finisher counts per county (normalized per 100k population)
- Rationale: objective behavioral signal — people register and show up to run races

**Component 3 — Running Infrastructure**
- Sources: EPA National Walkability Index (aggregated to county); OSM trail/path network density (km per sq mi); USDA Food Environment Atlas fitness facility density (NAICS 713940)

**Component 4 — Strava Activity Density** *(pending academic cohort approval)*
- Source: Strava Metro running trip counts per county
- Fallback: Strava heatmap pixel density (methodology TBD; noted as limitation)

**Composite RunScore**
- Weighted sum of standardized (z-score) components
- Weights: initially equal; sensitivity analysis to test alternative weightings
- Output: RunScore 0–100 percentile rank for all U.S. counties

### 3.3 Quality-of-Life Outcome Variables
| Domain | Variables | Source |
|---|---|---|
| Health | Obesity rate, diabetes prevalence, life expectancy, physical inactivity rate | CDC PLACES, IHME GBD, County Health Rankings |
| Real Estate | Zillow Home Value Index (ZHVI), median sale price, ZORI rent index | Zillow Research, Redfin |
| Education | Stanford SEDA test scores, HS graduation rate, % bachelor's degree | SEDA, EdFacts, ACS |
| Safety | Violent crime rate, pedestrian fatality rate | FBI NIBRS (ICPSR), NHTSA FARS |
| Environment | EPA Walkability Index, tree canopy %, park access, AQI | EPA, NLCD, TPL ParkServe, EPA AQI |
| Social Capital | Economic connectedness index | Harvard Social Capital Atlas |

### 3.4 Control Variables (Confounders)
- Median household income (ACS)
- Population density (Census)
- % population age 25–44 (ACS — core running demographic)
- Urban/rural classification (USDA ERS Rural-Urban Continuum Code)
- Climate: mean temperature, precipitation (NOAA)
- USDA Natural Amenities Scale (terrain, climate desirability)

### 3.5 Statistical Analysis
1. **Descriptive statistics** — distribution of RunScore across counties; top/bottom decile profiles
2. **Bivariate correlations** — Pearson/Spearman between RunScore and each outcome variable
3. **Multivariate OLS regression** — RunScore as predictor of ZHVI and health outcomes, controlling for income, density, urbanicity, age
4. **Spatial autocorrelation** — Moran's I to test whether high-RunScore counties cluster geographically
5. **Cluster analysis** — K-means or hierarchical clustering to identify RunScore archetypes (e.g., affluent suburban runners vs. outdoor recreation towns)
6. **Sensitivity analysis** — reweight RunScore components; test robustness of findings

---

## 4. Results — RunScore Distribution
- Map: RunScore choropleth for all 3,144 U.S. counties
- Top 10 and bottom 10 counties by RunScore
- Regional patterns (Sun Belt, Mountain West, Rust Belt, Deep South)
- Urban vs. rural RunScore comparison

---

## 5. Results — Health Correlations
- RunScore vs. obesity rate: expected strong negative correlation
- RunScore vs. diabetes prevalence, hypertension, life expectancy
- RunScore vs. CDC PLACES physical inactivity (validation check — should be very high correlation since LPA is a component)
- Partial correlations controlling for income: does RunScore have independent health signal beyond wealth?

---

## 6. Results — Real Estate & Community Desirability
### 6.1 Home Values
- RunScore vs. Zillow ZHVI: correlation, scatterplot, regression coefficient
- RunScore as predictor of ZHVI controlling for income, density, urbanicity
- Interpretation: $X increase in median home value per 10-point RunScore increase (holding income constant)

### 6.2 Lifestyle Indicators
- RunScore vs. EPA Walkability Index
- RunScore vs. park access (ParkServe)
- RunScore vs. economic connectedness (Harvard Social Capital Atlas)
- RunScore vs. violent crime rate
- RunScore vs. school quality (SEDA test scores)

### 6.3 The Composite Picture
- Multiple regression: RunScore as predictor of a composite QoL index (weighted average of health, education, safety, environment)
- R² contribution of RunScore beyond traditional predictors

---

## 7. City Deep Dives — Extreme Case Profiles
*Qualitative + quantitative profiles of 6–8 cities representing RunScore extremes*

### 7.1 Selection Methodology
- Top RunScore counties: identify anchor city in each
- Bottom RunScore counties: identify anchor city in each
- Include high-income/high-RunScore, high-income/low-RunScore (test wealth vs. running culture independently), and low-income/high-RunScore (outdoor recreation towns) cases

### 7.2 Profile Template (per city)
- RunScore breakdown (component-by-component)
- Zillow ZHVI and trend
- Obesity rate, life expectancy
- School quality (SEDA scores)
- Walkability, park access, trail network
- Key qualitative narrative: what makes this city a runner's community or not?

### 7.3 Candidate Cities (preliminary)
| Category | Candidate Cities |
|---|---|
| High RunScore, high income | Boulder CO, Marin County CA, Teton County WY |
| High RunScore, moderate income | Missoula MT, Flagstaff AZ, Asheville NC |
| Low RunScore, low income | Deep South rural counties (MS, AL, LA) |
| Low RunScore, high income | Car-dependent affluent suburbs (Las Vegas NV metro) |

---

## 8. Discussion
### 8.1 What RunScore Captures
- Running as a proxy for infrastructure investment, community culture, outdoor access, and health norms
- Why it works as a real estate signal: it reflects revealed preferences, not stated preferences

### 8.2 Implications for Real Estate Platforms
- RunScore as a neighborhood-level feature in listing platforms (analogous to Walk Score)
- Predictive value for home price appreciation: high-RunScore counties as growth markets
- Application for relocation tools: buyers filtering by lifestyle preferences
- Use case for Zillow: RunScore layer on Zestimate map; lifestyle-fit matching in search

### 8.3 Limitations
- Strava data selection bias: skews toward wealthier, younger users
- CDC PLACES LPA is model-based (MRP), not directly measured at county level
- RunSignUp captures organized racing culture, not casual recreational running
- Heatmap pixel density is not raw count data (normalization issue)
- Reverse causality: does high RunScore attract wealthy buyers, or do wealthy counties become running communities? (address with time-lagged analysis if data permits)

### 8.4 Future Work
- Strava Metro academic cohort: next cycle application for trip-count data
- ZIP code and census tract resolution (below county)
- Longitudinal RunScore: does change in RunScore predict future home price appreciation?
- Employer and corporate relocation use case

---

## 9. Conclusion
- RunScore is a measurable, replicable, county-level index that captures running community strength
- It correlates significantly with home values, health outcomes, school quality, and walkability — the exact variables that drive residential location decisions
- Real estate platforms can operationalize RunScore as a lifestyle signal with predictive power beyond traditional price drivers
- Invitation for partnership: the methodology is open; the data pipeline is replicable at scale

---

## Appendices
- **A:** RunScore methodology detail — variable sources, standardization, weighting sensitivity
- **B:** Full correlation table (RunScore vs. all 30+ outcome/control variables)
- **C:** County-level RunScore data table (all 3,144 counties)
- **D:** City deep dive data tables
- **E:** Regression output tables (full OLS results with controls)
- **F:** Data sources and access instructions

---

## Target Journals / Venues *(for academic credibility before industry pitch)*
- *Journal of Urban Economics*
- *Real Estate Economics*
- *American Journal of Preventive Medicine*
- *Health & Place*
- ACSM Annual Meeting abstract (American Fitness Index community)

---

## Industry Pitch Strategy
*After academic publication (or preprint on SSRN):*
1. **Zillow Research** — pitch RunScore as an additive neighborhood feature layer
2. **Redfin** — lifestyle-matching tool integration
3. **Walk Score / Redfin partnership** — RunScore as companion to Walk Score
4. **National Association of Realtors** — white paper on lifestyle data in residential search
5. **ACSM / Running USA** — co-publish RunScore national rankings as annual report
