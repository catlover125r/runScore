# RunScore Research Paper — Master Data Inventory
*Compiled April 2026 from 7 parallel research agents*

---

## DOMAIN 1: RUNNING & FITNESS ACTIVITY DATA

| Dataset | Provider | Geography | Access | Key Variables | Notes |
|---|---|---|---|---|---|
| **CDC PLACES — Physical Inactivity (LPA)** | CDC | County, Tract, ZCTA | Free CSV | % adults with no leisure-time physical activity | Best available free county-level exercise proxy; all 3,144 counties; model-based from BRFSS |
| **Strava Metro** | Strava | County / road segment | Free for cities; competitive academic program | Running trip counts by segment; time-of-day; activity type | Most accurate running data but requires academic program application; apply for next cohort |
| **Strava Global Heatmap** | Strava | Tile-based raster (any) | Login required; ToS risks for scraping | Pixel density = relative running frequency; filterable to "run" only | Normalized (not raw counts); cross-geography comparison unreliable; unofficial access only |
| **RunSignUp API** | RunSignUp | City / ZIP per race | Free open API | Race event counts, finisher counts, distance, location | Best free proxy for running community engagement; aggregate to county by ZIP crosswalk |
| **Athlinks Race Results API** | Athlinks | Race/state level | API key (free registration) | Finisher counts, race events, results | Most comprehensive endurance results database; less geographic detail than RunSignUp |
| **ATUS — Running (TRCODE 130101)** | BLS | National / state (some years) | Free download | Time spent running per day; participation rate | Running coded specifically; state-level only in public files; county not available |
| **BRFSS / County Health Rankings** | CDC / UW-RWJF | County (CHR all counties) | Free | Physical inactivity %; exercise access % | CHR republishes BRFSS-derived inactivity for all counties annually |
| **NHTS** | FHWA / ORNL | National (county: restricted) | Free public CSV | Walk/jog/run trips; trip purpose, distance, duration | County IDs only in restricted files; state-level for public use |
| **USATF Certified Courses** | USATF | City / state | Free web search | Certified road race courses by location | No bulk download; web scraping required for systematic use |
| **Running USA Reports** | Running USA | State-level | $299/report non-member | Race finisher counts; participation trends; demographics | Top 100 races report; state-level only |
| **SFIA Participation Data** | SFIA | Census region | $300/report non-member | Running/jogging participants (50M+ in 2024); frequency; demographics | Census region only; no county or state detail |

---

## DOMAIN 2: HEALTH OUTCOMES

| Dataset | Provider | Geography | Access | Key Variables | Notes |
|---|---|---|---|---|---|
| **CDC PLACES** | CDC / RWJF | County, Place, Tract, ZCTA | Free CSV / API | Obesity, diabetes, hypertension, heart disease, COPD, depression, physical inactivity, sleep, disability, social needs (40 measures) | Gold standard for county-level health; model-based MRP estimates from BRFSS + ACS |
| **County Health Rankings** | UW-RWJF | County (all ~3,000) | Free Excel/CSV | 80+ measures: premature death, life expectancy, YPLL, poor health days, obesity, physical inactivity, access to care, crime, income, education, environment | Most comprehensive county health index; annual since 2010; raw component data downloadable |
| **CDC WONDER** | CDC / NCHS | County (web UI only) | Free web tool | Mortality rates by ICD-10 cause, age, sex, race; cancer; natality | County-level requires web UI; API is national only; suppression for small counts |
| **IHME Global Burden of Disease — US County** | IHME / UW | County by race/ethnicity | Free (account required) | Life expectancy, HALE, disease burden (DALYs), 292 causes, 88 risk factors — 2000–2019 | Most granular US county life expectancy by race; non-commercial use only |
| **USALEEP (CDC/NCHS)** | CDC / NCHS / RWJF | Census tract | Free download | Life expectancy at birth by tract and sex (2010–2015 only) | Must aggregate to county; only one release (2010–2015) |
| **BRFSS SMART** | CDC | MMSA / metro counties | Free SAS XPT | Direct survey health behaviors; smoking, obesity, exercise, mental health | Only covers metro areas with 500+ respondents; rural gaps |
| **CMS Medicare Chronic Conditions** | CMS | County | Free dashboard / CSV | 19 chronic conditions prevalence (diabetes, heart failure, COPD, depression, etc.) among Medicare beneficiaries | Medicare population only (65+); not representative of full county |
| **Provisional Drug Overdose Deaths** | CDC / NCHS | County | Free CSV | Drug overdose deaths by county and 12-month period | Suppressed for small counties; provisional data lags |
| **State Cancer Profiles** | NCI + CDC | County | Free web tool | Age-adjusted cancer incidence and mortality by site, county, sex, race | Suppressed if <16 cases; registry coverage varies |
| **SAMHSA NSDUH** | SAMHSA | State only | Free download | Mental illness, depression, substance use disorders | State-level SAE only; no county estimates published |
| **HRSA Area Health Resources Files (AHRF)** | HRSA | County | Free download | 6,000+ variables: hospitals, physicians, nurses, shortage areas, health status indicators | Gold standard for county health workforce and facilities |

---

## DOMAIN 3: SOCIOECONOMIC DATA

| Dataset | Provider | Geography | Access | Key Variables | Notes |
|---|---|---|---|---|---|
| **Census ACS 5-Year Estimates** | Census Bureau | County, Tract, ZCTA, Block Group | Free API / FTP | Median income, poverty rate, Gini coefficient, housing costs, employment, commute, education, household structure | 2020–2024 most recent; the core socioeconomic dataset for any county study |
| **Zillow Research Data** | Zillow | County, ZIP, City | Free CSV | Home Value Index (ZHVI), Rent Index (ZORI), median list/sale price | Model-based index; rural counties may have sparse coverage; updated monthly |
| **Redfin Data Center** | Redfin | County, ZIP, Metro | Free CSV | Median sale price, days on market, inventory, price cuts | Transaction-based; thinner rural coverage; 2012–present |
| **FRED (Federal Reserve)** | St. Louis Fed | County, Metro, State | Free API | Income, unemployment, home prices, population — aggregated from BLS/BEA/Census | Convenience API; always verify original source |
| **BLS Local Area Unemployment (LAUS)** | BLS | County | Free download / API | Unemployment rate, labor force, employed, unemployed (monthly and annual) | Model-based for counties; not seasonally adjusted at county level |
| **USDA ERS County Data Sets** | USDA ERS | County | Free XLSX/CSV | Poverty rate, median income, unemployment, education attainment, rural-urban codes | Convenient precompiled file; updated annually |
| **Census SAIPE** | Census Bureau | County, School District | Free API / CSV | Poverty rate, child poverty, median household income (annual single-year estimates) | Best annual county poverty estimate; model-based |
| **Opportunity Insights — Opportunity Atlas** | Harvard / Census | County, Tract | Free CSV | Economic mobility by parental income, race, sex; college attendance; incarceration rates | Birth cohorts 1978–1992; historical outcomes, not current conditions |
| **Opportunity Insights — Social Capital Atlas** | Harvard / Meta | County, ZIP | Free CSV | Economic connectedness, cohesiveness, civic engagement (from Facebook friendship data) | Snapshot 2020–2022; Facebook data has demographic gaps |
| **IRS Statistics of Income — County** | IRS | County | Free CSV | AGI, wages, capital gains, number of returns by AGI class | Tax filers only; excludes non-filers; 2022 most recent |
| **HUD Fair Market Rents** | HUD | County / FMR Area | Free XLSX | FMR by bedroom size (0–4BR); historical back to FY1983 | 40th percentile of gross rents; not median market rent |
| **USDA Food Environment Atlas** | USDA ERS | County | Free XLSX/CSV | Store access, restaurant density, food assistance, food prices, obesity, fitness facility counts | Includes fitness facilities per 100,000 (NAICS 713940) by county |
| **CDC / ATSDR Social Vulnerability Index** | CDC / ATSDR | County, Tract | Free CSV / Shapefile | 16 ACS-derived variables; 4 theme scores; overall SVI (0–1 scale) | Designed for emergency preparedness; useful as socioeconomic covariate |
| **EPI Family Budget Calculator** | EPI | County, Metro | Free CSV (non-commercial) | Cost of living by family type; component costs (housing, food, childcare, transport, healthcare) | Not a price index; living wage threshold by family configuration |

---

## DOMAIN 4: EDUCATION QUALITY

| Dataset | Provider | Geography | Access | Key Variables | Notes |
|---|---|---|---|---|---|
| **Stanford SEDA** | Stanford / Ed Opportunity Project | County, District, School | Free CSV | Standardized test scores in math and ELA; achievement gaps by race, gender; 2008–2019 and 2022–2024 (district) | Best free county-level test score data; uses state assessments linked to common scale |
| **NCES Common Core of Data (CCD)** | NCES / Dept. of Education | School, District (→ County) | Free download | Enrollment, per-pupil expenditure, FRPL eligibility, staff FTE, Title I status | Must aggregate district → county using FIPS codes; fiscal data lags 2 years |
| **EdFacts / ED Data Express** | Dept. of Education | School, District (→ County) | Free CSV | Graduation rates (ACGR), proficiency rates, chronic absenteeism | Grad rates available 2009–present; absenteeism 2017–present |
| **Census ACS — Educational Attainment** | Census Bureau | County | Free API | % with bachelor's degree or higher; school enrollment rates by age | Ongoing; 5-year estimates for all counties |
| **Census SAIPE — School District Poverty** | Census Bureau | County, School District | Free API / CSV | Child poverty rate and median income by school district AND county; annual | Critical for controlling for school poverty; only annual single-year district poverty estimate |
| **Child Opportunity Index (COI) 3.0** | diversitydatakids / Brandeis | County, Tract, ZIP | Free CSV | Education domain: school quality, preschool access, AP enrollment, college proximity, school poverty | County-level pre-built download; 2012–2023 annual; composite + 44 raw indicators |
| **Urban Institute Education Data Portal** | Urban Institute | School, District, County | Free API | CCD + CRDC + SAIPE + IPEDS integrated; county-level summary endpoints | Convenient API wrapper; no new data beyond source datasets |
| **AEI Return to Learn Tracker** | AEI | District (14,700+) | Free CSV | Chronic absenteeism rates 2016–2025; district-level | Best coverage of pandemic-era absenteeism trends |
| **KIDS COUNT Data Center** | Annie E. Casey Foundation | County, State | Free download | School readiness, 4th grade reading, 8th grade math, high school graduation, Head Start enrollment | Convenient county-level precompiled education + child welfare indicators |
| **GreatSchools** | GreatSchools.org | School (→ County) | Free API (limited); bulk = paid | School ratings 1–10 (academics, growth, equity) | Bulk data requires enterprise license; free API rate-limited |

---

## DOMAIN 5: INFRASTRUCTURE & ENVIRONMENT

| Dataset | Provider | Geography | Access | Key Variables | Notes |
|---|---|---|---|---|---|
| **EPA National Walkability Index** | EPA Office of Smart Growth | Census Block Group | Free CSV / GeoJSON | Walkability score (1–20); intersection density, transit proximity, employment mix | Fully free alternative to Walk Score; aggregable to county by population weighting |
| **Trust for Public Land ParkScore / ParkServe** | Trust for Public Land | City (100 largest) / Urban areas | Free Shapefile / CSV | Park acreage per capita, % residents within 10-min walk, park equity scores, trail polygons | ParkScore = 100 largest cities; ParkServe = all urban areas |
| **Walk Score** | Walk Score / Redfin | Address → City | Free API (limited); research request | Walk Score, Transit Score, Bike Score (0–100) | Academic bulk access requires formal request; EPA Walkability Index is better for research |
| **EPA AQI Annual Summary** | EPA | County | Free CSV | Days in each AQI category; max/median AQI; PM2.5, ozone days | Not all counties have monitors; rural gaps |
| **NOAA Climate at a Glance — County** | NOAA NCEI | County | Free CSV / API | Mean temperature, precipitation, extreme heat days; 1895–present | Best climate data at county level; derived from weather station interpolation |
| **OpenStreetMap — Trails & Paths** | OSM Community | Feature level → County | Free (Geofabrik bulk or Overpass API) | Footways, paths, tracks, cycleways; filter by highway=footway, path, track | Crowd-sourced; urban areas well-mapped; rural gaps; use R `osmextract` or Python `osmnx` |
| **USGS 3DEP (Elevation)** | USGS | 30m raster → County | Free download | Digital elevation model; derive TRI, slope, elevation variance | Must compute county-level terrain statistics yourself via zonal stats |
| **USGS PAD-US 4.1 (Protected Areas)** | USGS Gap Analysis | County (summary stats) | Free CSV / Geodatabase | Protected acres by county, GAP status, designation type, managing agency | County-level pre-built summary table downloadable from Statistics Dashboard |
| **FBI UCR / NIBRS (ICPSR)** | FBI / ICPSR | County (via ICPSR archive) | Free (ICPSR registration) | Violent crime rate, property crime rate, assault, robbery, homicide | Coverage gaps especially 2021 (transition year); ICPSR county-level files most research-ready |
| **FHWA National Bicycle Network** | FHWA / DOT | Route/segment → County | Free Shapefile / GeoJSON | Bicycle route location, length, type (protected, shared, off-road) | Based on voluntary state submissions; variable quality |
| **NPS / USGS National Digital Trails** | NPS / USGS | Trail/segment → County | Free Shapefile / Feature Service | Trail length, permitted uses (running, hiking), surface, NPS unit | NPS lands only for NPS dataset; USGS version broader (multi-agency) |
| **USDA Food Environment Atlas** | USDA ERS | County | Free XLSX/CSV | Fitness & recreational sports centers per 100,000 (NAICS 713940 from CBP) | Pre-computed fitness facility density; most convenient county-level fitness infrastructure metric |
| **Census County Business Patterns (NAICS 713940)** | Census Bureau | County | Free CSV / API | Fitness center establishments count, employment, payroll | NAICS 713940 = fitness & recreational sports centers; counts establishments with paid employees only |
| **NHTSA FARS** | NHTSA | Individual crash → County | Free CSV | Pedestrian/cyclist fatalities; crash location, time, conditions | Fatalities only (not non-fatal); county-level aggregation from lat/lon |
| **NASA Black Marble (Light Pollution)** | NASA / NOAA | ~500m raster → County | Free (NASA Earthdata account) | Nighttime light radiance; annual composites 2012–present | R package `blackmarbler` handles county-level extraction automatically |
| **NLCD Tree Canopy / EPA EnviroAtlas** | USGS / EPA | 30m raster / County CSV | Free | % tree canopy, % green space, % impervious surface by county | EPA EnviroAtlas has pre-computed county-level land cover proportions as CSV |

---

## DOMAIN 6: DEMOGRAPHICS & POPULATION

| Dataset | Provider | Geography | Access | Key Variables | Notes |
|---|---|---|---|---|---|
| **Census ACS 5-Year (Demographics)** | Census Bureau | County, Tract, Block Group | Free API / FTP | Age distribution (B01001), race/ethnicity, foreign-born, disability, veterans, vehicles, WFH, broadband, household size | Primary source for all demographic variables at county level; 2020–2024 most recent |
| **Census Population Estimates (PEP)** | Census Bureau | County | Free CSV | Annual population, births, deaths, net migration, population change by year 2020–2024 | Vintage 2024 is current; download only (no API for current vintage) |
| **Census TIGER/Line — Urban/Rural** | Census Bureau | County / Block | Free Shapefile | Urban area boundaries, % urban/rural by county; 2020 definitions | 2020 definition changed (min 5,000 pop); discontinuity with 2010 |
| **NCHS Urban-Rural Classification** | CDC / NCHS | County | Free CSV | 6-category urban-rural classification (large central metro → noncore) | Direct download; 2023 scheme; use alongside USDA RUCC for robustness |
| **USDA ERS Rural-Urban Continuum Codes (RUCC)** | USDA ERS | County | Free XLSX/CSV | 9-category metro/nonmetro classification; 2023 codes | Standard for rural research; updated decennially |
| **USDA ERS Rural-Urban Commuting Area (RUCA)** | USDA ERS | Census Tract, ZIP | Free Excel | 10-category classification at tract/ZIP level — sub-county rural/urban detail | More granular than RUCC; useful if working below county level |
| **JEC Social Capital Index** | U.S. Senate JEC | County (2,971) | Free XLSX | Family unity, community health, institutional health, collective efficacy subindices | Published 2018; 2012–2016 data; somewhat dated but comprehensive and free |
| **Rupasingha-Goetz Social Capital Index** | NERCRD / Penn State | County | Free Excel | Factor score: civic orgs, voter turnout, census response, nonprofits per capita | 5 time points 1990–2014; useful for longitudinal social capital analysis |
| **ASARB U.S. Religion Census 2020** | ASARB / ARDA | County | Free CSV (via ARDA) | Congregation counts by denomination; adherent counts; 2020 | Gold standard for congregation density; decennial; 372 religious bodies |
| **MIT Election Lab — County Returns** | MIT Election Lab | County | Free CSV (GitHub) | Presidential election results 2000–2024; vote counts by party | Good civic engagement proxy; complements social capital indices |
| **AmeriCorps CEV — Volunteer Rates** | AmeriCorps / CNCS | State only | Free CSV | Volunteer rate, volunteer hours per resident, informal helping | State-level only; no county estimates available from direct surveys |
| **FCC National Broadband Map** | FCC | Address → County | Free CSV | % locations with broadband by speed tier; mobile coverage | Address-level accuracy; ISP self-reported (optimistic); biannual updates |
| **IRS SOI County-to-County Migration** | IRS | County pairs | Free CSV | Return counts (households), personal exemptions, AGI for migrants; 2022–2023 | Best annual county migration data; filer-based (excludes non-filers) |

---

## DOMAIN 7: EXISTING QUALITY OF LIFE INDICES

| Index | Provider | Geography | Access | Dimensions | Relevance | Raw Data? |
|---|---|---|---|---|---|---|
| **County Health Rankings** | UW / RWJF | County (all US) | Free annual download | Health behaviors, clinical care, social/economic, physical environment | Primary benchmark; physical inactivity variable is key validation target | YES — full raw data |
| **CDC PLACES** | CDC | County, Tract, ZCTA | Free CSV / API | 40 health measures via MRP from BRFSS | Physical inactivity + obesity + chronic disease at county level | YES |
| **Child Opportunity Index 3.0** | diversitydatakids / Brandeis | County, Tract, ZIP | Free CSV | Education, Health & Environment, Social & Economic (44 indicators) | Excellent outcome variable for child-focused QoL | YES — all 44 indicators |
| **Social Vulnerability Index (SVI)** | CDC / ATSDR | County, Tract | Free CSV / Shapefile | Socioeconomic, Household Characteristics, Minority Status, Housing/Transport | Best free covariate for controlling socioeconomic vulnerability | YES |
| **USDA Natural Amenities Scale** | USDA ERS | County (48 states) | Free CSV | Temperature, sun, humidity, topography, water area | Critical terrain/climate control variable; static (1999) | YES |
| **Harvard Social Capital Atlas** | Opportunity Insights / Meta | County, ZIP | Free CSV | Economic connectedness, cohesiveness, civic engagement | Key covariate; 2022 snapshot from Facebook data | YES |
| **American HDI (Measure of America)** | SSRC | County, Tract | Tool only | Life expectancy, education, median earnings | Simple 3-dimension HDI adapted for US | Tool only (reconstruct from public data) |
| **Sharecare Community Well-Being Index** | Sharecare / BU | County (99.9%) | Licensed — not free | Career, Social, Financial, Physical, Community WB + 600 SDOH variables | Richest wellbeing data; requires partnership or license | Licensed |
| **ACSM American Fitness Index** | ACSM / Elevance | 100 largest cities | Free PDF report | Health behaviors, outcomes, built environment, community infrastructure, local policy | Closest methodological precedent to RunScore; city-level only | Report PDF only |
| **US News Healthiest Communities** | US News | County (~3,000) | Web only (no download) | Community Vitality, Economy, Education, Environment, Equity, Food, Health, Housing, Infrastructure, Safety | 10-category composite; 92 metrics; excludes counties <2,000 pop | NO |
| **AARP Livability Index** | AARP | ZIP / City / County | Tool only | Housing, Neighborhood, Transportation, Environment, Health, Engagement, Opportunity | 61 indicators; designed for older adults; no running-specific variable | NO |
| **JEC Social Capital Index** | U.S. Senate JEC | County (2,971) | Free XLSX | Family unity, community health, institutional health, collective efficacy | County social capital composite; 2016 data | YES |
| **Gallup / Sharecare WBI** | Gallup | State / partial county | Subscription | Career, Social, Financial, Physical, Community well-being (survey-based) | Best subjective wellbeing data; county-level requires license | Subscription |
| **Opportunity Atlas** | Harvard / Census | County, Tract | Free CSV | Economic mobility by parental income, race, sex | Long-run outcome variable (historical cohorts) | YES |

---

## CURATED SHORTLIST: RECOMMENDED DATASETS

### For the RunScore Itself
| Priority | Dataset | Why |
|---|---|---|
| **1** | CDC PLACES (LPA variable) | Only free county-level exercise inactivity covering all 3,144 counties; immediate validation baseline |
| **2** | Strava Metro (academic program) | Actual running trip counts by road segment; apply for next cohort |
| **3** | RunSignUp API | Free; build race event density and finisher counts per county as running community engagement proxy |
| **4** | County Health Rankings — Exercise Access | % population near park or fitness facility; complements PLACES |
| **5** | ATUS (TRCODE 130101) | Running-specific time-use data for national/state validation |

### For the QoL Outcome Variables
| Dataset | Variables |
|---|---|
| County Health Rankings | Premature death, life expectancy, poor mental/physical health days |
| CDC PLACES | Obesity, diabetes, hypertension, depression, sleep, all chronic conditions |
| IHME GBD US County | Life expectancy by race/ethnicity 2000–2019 |
| Opportunity Atlas | Economic mobility, college attendance rates |
| Child Opportunity Index | County-level opportunity composite |

### For Health Confounders / Controls
| Dataset | Variables |
|---|---|
| CDC / ATSDR SVI | Socioeconomic vulnerability |
| USDA Natural Amenities Scale | Terrain, climate (running-relevant environment) |
| EPA AQI Annual Summary | Air quality |
| NOAA Climate at a Glance | Temperature, precipitation |
| NCHS Urban-Rural Classification | Urban/rural control |

### For Socioeconomic Confounders
| Dataset | Variables |
|---|---|
| Census ACS 5-Year | Median income, poverty, Gini, age distribution, education |
| Zillow ZHVI | Home value by county |
| Census SAIPE | Annual county poverty rate |
| Harvard Social Capital Atlas | Economic connectedness |

### For Education Variables
| Dataset | Variables |
|---|---|
| Stanford SEDA | Test scores by county |
| NCES CCD / SAIPE | Per-pupil spending, graduation rates, school poverty |
| Child Opportunity Index — Education Domain | Composite education score + 6 raw indicators |

### For Infrastructure Variables
| Dataset | Variables |
|---|---|
| USDA Food Environment Atlas | Fitness facilities per 100,000 by county |
| EPA National Walkability Index | Block-group walkability → county aggregate |
| OSM via Geofabrik | Trail/path miles by county (footway + track + path) |
| USGS PAD-US | Protected land acres by county |
| Trust for Public Land ParkServe | Park access for urban counties |

### For City Deep Dives (Extreme Cases)
| Dataset | Variables |
|---|---|
| ACSM American Fitness Index | 35 fitness metrics for 100 largest cities; best city-level fitness data |
| CDC PLACES (Place level) | 29,923 US cities; same 40 health measures |
| County Health Rankings | County-level for all extreme counties |
| Opportunity Insights Social Capital | City-level economic connectedness |

---

## KEY ACADEMIC LITERATURE

| Paper | Relevance |
|---|---|
| "Rate of Physical Activity and Community Health: Evidence From U.S. Counties" (PubMed 26595939, 2015) | Most directly relevant prior work; county-level physical activity → health outcomes using BRFSS + CHR |
| Chetty et al. (2022) — Social Capital I & II (Nature) | Economic connectedness as predictor of mobility; key covariate methodology |
| Parkrun BMC Public Health (2021) — 2.3M participants | Running community → wellbeing; strongest effects in most deprived populations |
| Frontiers in Psychology (2025) — SES and endurance sports | SES gradients in long-distance running; critical for addressing selection bias in RunScore |

---

## DATA ACCESS NOTES

- **All county-level datasets use 5-digit FIPS codes** as the universal key for merging
- **ZIP-to-county crosswalk:** HUD USPS Crosswalk Files — https://www.huduser.gov/portal/datasets/usps_crosswalk.html
- **Census API key:** Free registration at api.census.gov/data/key_signup.html
- **Strava Metro academic cohort:** Next application cycle TBA; monitor metro.strava.com/academics
- **IHME GBD:** Free account required at ghdx.healthdata.org (non-commercial use)

---

*Generated April 2026 | 7 research agents | ~300 datasets surveyed | ~80 datasets catalogued*
