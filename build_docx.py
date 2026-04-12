"""
Convert runscore_paper.md to a formatted .docx file.
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import re
import os

doc = Document()

# ── Page margins ─────────────────────────────────────────────────────────────
for section in doc.sections:
    section.top_margin    = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin   = Inches(1.25)
    section.right_margin  = Inches(1.25)

# ── Style helpers ─────────────────────────────────────────────────────────────
def set_font(run, name="Times New Roman", size=12, bold=False, italic=False, color=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = RGBColor(*color)

def add_paragraph(text="", style="Normal", align=None):
    p = doc.add_paragraph(style=style)
    if align:
        p.alignment = align
    if text:
        run = p.add_run(text)
        set_font(run)
    return p

def shade_row(row, hex_color="D9E1F2"):
    for cell in row.cells:
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), hex_color)
        tcPr.append(shd)

def add_table(headers, rows, col_widths=None):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Header row
    hdr = t.rows[0]
    shade_row(hdr, "1B4F8A")
    for i, h in enumerate(headers):
        cell = hdr.cells[i]
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(9)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    # Data rows
    for ri, row_data in enumerate(rows):
        row = t.rows[ri + 1]
        if ri % 2 == 0:
            shade_row(row, "EBF3FB")
        for ci, val in enumerate(row_data):
            cell = row.cells[ci]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(str(val))
            run.font.name = "Times New Roman"
            run.font.size = Pt(9)

    # Column widths
    if col_widths:
        for i, w in enumerate(col_widths):
            for row in t.rows:
                row.cells[i].width = Inches(w)
    doc.add_paragraph()
    return t

# ═══════════════════════════════════════════════════════════════════════════════
# TITLE PAGE
# ═══════════════════════════════════════════════════════════════════════════════
doc.add_paragraph()
doc.add_paragraph()

title_p = doc.add_paragraph()
title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title_p.add_run("RunScore: Running Activity as a Predictive Signal\nfor Community Quality of Life and Real Estate Desirability")
run.font.name = "Times New Roman"
run.font.size = Pt(18)
run.font.bold = True
run.font.color.rgb = RGBColor(27, 79, 138)

doc.add_paragraph()

author_p = doc.add_paragraph()
author_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = author_p.add_run("Luke Popler")
run.font.name = "Times New Roman"; run.font.size = Pt(13); run.font.bold = True

for line in ["Sequoia High School, Redwood City, California",
             "lukepopler@gmail.com  |  818038@seq.org",
             "April 2026"]:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(line)
    run.font.name = "Times New Roman"; run.font.size = Pt(11)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════════
# ABSTRACT
# ═══════════════════════════════════════════════════════════════════════════════
h = doc.add_heading("Abstract", level=1)
h.runs[0].font.name = "Times New Roman"
h.runs[0].font.size = Pt(14)
h.runs[0].font.color.rgb = RGBColor(27, 79, 138)

abstract_text = (
    "This study introduces RunScore, a novel composite index measuring the running activity level "
    "and supporting infrastructure of U.S. counties. Using publicly available data across five "
    "domains — physical inactivity rates, organized race event density, exercise infrastructure "
    "access, fitness facility density, and neighborhood walkability — RunScore was computed for "
    "all 3,143 U.S. counties and validated against a broad set of quality-of-life outcomes. "
    "Bivariate analysis reveals strong correlations between RunScore and home values "
    "(Spearman r = +0.604), life expectancy (r = +0.582), obesity rates (r = −0.570), and "
    "diabetes prevalence (r = −0.676), all significant at p < 0.001. Multivariate OLS regression "
    "demonstrates that RunScore predicts county-level home values independently of median "
    "household income, unemployment, insurance coverage, and life expectancy "
    "(β = 0.0035, p < 0.001, ΔR² = +0.022). Each 10-point increase in RunScore is associated "
    "with a 3.5% increase in median home value — approximately $7,885 on a median county home. "
    "Critically, RunScore also predicts forward-looking home value appreciation: each 10-point "
    "increase is associated with 0.9 additional percentage points of five-year appreciation, "
    "controlling for income, employment, and urbanicity (β = 0.087, p < 0.001). "
    "These findings hold across metro and non-metro subgroups and after controlling for urbanicity. "
    "RunScore represents a replicable, low-cost lifestyle signal with direct applications for "
    "residential real estate platforms, urban planners, and public health agencies."
)
p = doc.add_paragraph()
run = p.add_run(abstract_text)
run.font.name = "Times New Roman"; run.font.size = Pt(11); run.font.italic = True
p.paragraph_format.left_indent  = Inches(0.4)
p.paragraph_format.right_indent = Inches(0.4)
p.paragraph_format.space_after  = Pt(6)

kw = doc.add_paragraph()
kw.paragraph_format.left_indent = Inches(0.4)
krun = kw.add_run("Keywords: ")
krun.font.name = "Times New Roman"; krun.font.size = Pt(11); krun.font.bold = True
krun2 = kw.add_run("running activity, quality of life, real estate, county health, composite index, physical activity, home values")
krun2.font.name = "Times New Roman"; krun2.font.size = Pt(11)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════════
# HELPER: section heading
# ═══════════════════════════════════════════════════════════════════════════════
def section_heading(text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.name = "Times New Roman"
        run.font.color.rgb = RGBColor(27, 79, 138) if level == 1 else RGBColor(44, 62, 80)
        run.font.size = Pt(14) if level == 1 else Pt(12)

def body(text, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    return p

def italic_note(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = "Times New Roman"; run.font.size = Pt(10); run.font.italic = True

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — INTRODUCTION
# ═══════════════════════════════════════════════════════════════════════════════
section_heading("1. Introduction")
section_heading("1.1  The Problem with Lifestyle Data in Real Estate", level=2)
body(
    "When someone decides where to live, they are not just buying a house — they are buying into "
    "a community. Buyers increasingly filter not just on price and square footage, but on "
    "walkability, outdoor access, school quality, safety, and the lifestyle culture of a "
    "neighborhood. Real estate platforms have responded by embedding third-party signals like "
    "Walk Score and school ratings directly into listings. Yet these signals are siloed: "
    "walkability tells you nothing about health culture, and school ratings say nothing about "
    "whether people in the community actually exercise."
)
body(
    "There is currently no single, observable, publicly replicable signal that captures whether "
    "a community is physically active — whether the infrastructure, culture, and behavior around "
    "fitness actually exist on the ground. Running — more than any other form of exercise — is "
    "a uniquely observable community behavior. Communities that run produce measurable signals: "
    "they register for races, they build trails, they invest in walkability, they support fitness "
    "facilities. These signals are public, consistent, and computable at geographic scale."
)

section_heading("1.2  The RunScore Proposal", level=2)
body(
    "This paper develops and validates RunScore: a county-level composite index of running "
    "activity, infrastructure, and community engagement, computed for all 3,143 U.S. counties. "
    "RunScore is not a measure of individual behavior — it is a measure of community running "
    "culture. We test whether RunScore predicts: (1) health outcomes including obesity, diabetes, "
    "life expectancy, and self-rated health; (2) residential real estate values via the Zillow "
    "Home Value Index; and (3) broader quality-of-life indicators including walkability, park "
    "access, and social capital."
)
body(
    "The central hypothesis is that RunScore captures something real about a community that income "
    "alone does not — and that this residual signal has independent predictive power for where "
    "people want to live and how healthy they are."
)

section_heading("1.3  Research Questions", level=2)
for q in [
    "Does county-level running activity (RunScore) correlate with health outcomes net of income?",
    "Does RunScore predict residential home values beyond what income and urbanicity explain?",
    "Does RunScore predict future home value appreciation, functioning as a leading indicator for real estate markets?",
    "Is the RunScore–home value relationship consistent across metro and non-metro counties?",
    "What do extreme-case communities reveal about the qualitative texture of running culture?",
]:
    p = doc.add_paragraph(style="List Number")
    run = p.add_run(q)
    run.font.name = "Times New Roman"; run.font.size = Pt(12)

doc.add_paragraph()

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — BACKGROUND
# ═══════════════════════════════════════════════════════════════════════════════
section_heading("2. Background and Related Work")
section_heading("2.1  Physical Activity and Community Health", level=2)
body(
    "The relationship between physical activity and individual health is among the most replicated "
    "findings in epidemiology. Adults who meet recommended physical activity guidelines have "
    "substantially lower risk of cardiovascular disease, type 2 diabetes, depression, and "
    "premature death (Physical Activity Guidelines Advisory Committee, 2018). Joh et al. (2015) "
    "provide the most direct precedent for this study: using CDC BRFSS data for approximately "
    "500 U.S. counties, they found that county-level physical activity rates were associated with "
    "lower obesity, lower diabetes prevalence, and longer life expectancy, with effects persisting "
    "after controlling for socioeconomic factors. The CDC PLACES dataset — using multilevel "
    "regression and poststratification (MRP) — has since extended county-level physical inactivity "
    "estimates to all 3,143 U.S. counties (CDC, 2023)."
)

section_heading("2.2  Running Participation and Its Community Correlates", level=2)
body(
    "Running is the most common form of aerobic exercise in the United States, with an estimated "
    "50 million participants in 2024 (SFIA, 2024). Unlike gym-based exercise, running is "
    "inherently public: it requires outdoor space, infrastructure investment, and community "
    "engagement through race events and running clubs. The American College of Sports Medicine "
    "(ACSM) American Fitness Index provides the closest existing analog to RunScore, rating 100 "
    "large U.S. cities across 35 fitness and health metrics annually. The current study extends "
    "this concept to all 3,143 U.S. counties, applies a running-specific lens, and explicitly "
    "tests the connection to real estate outcomes — a link the ACSM index does not address."
)

section_heading("2.3  Physical Activity, Infrastructure, and Property Values", level=2)
body(
    "Research has established that parks increase adjacent property values by 8–20% (Crompton, "
    "2001), and that Walk Score is associated with approximately $3,000 higher home values per "
    "index point in urban areas (Leinberger & Alfonzo, 2012). However, these studies focus on "
    "infrastructure proximity rather than behavioral outcomes. A community could be highly "
    "walkable yet sedentary; an outdoor recreation town could have modest Walk Scores but "
    "vibrant running culture. To our knowledge, no prior study has examined whether a "
    "behaviorally-grounded measure of running community strength predicts home values at the "
    "county level across the full United States."
)

section_heading("2.4  Gap in the Literature", level=2)
body(
    "Existing research establishes that physical activity strongly predicts health outcomes, "
    "fitness infrastructure predicts home values, and community behavioral norms shape individual "
    "outcomes. What is missing is an integrated, nationally comparable county-level index that "
    "captures running activity as a community behavior and validates it against both health and "
    "real estate outcomes simultaneously. RunScore fills this gap."
)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3 — DATA & METHODS
# ═══════════════════════════════════════════════════════════════════════════════
section_heading("3. Data and Methods")
section_heading("3.1  Geographic Unit of Analysis", level=2)
body(
    "The county is the primary unit of analysis (n = 3,143 U.S. counties and county-equivalents). "
    "All datasets were joined using 5-digit Federal Information Processing Series (FIPS) codes."
)

section_heading("3.2  RunScore Construction", level=2)
body(
    "RunScore is a composite index combining five standardized components. Each component was "
    "standardized to a z-score before combining, and RunScore is expressed as a percentile rank "
    "(0–100) across all counties."
)
for comp in [
    ("Component 1 — Physical Activity Level",
     "CDC PLACES 2023. Percentage of adults with no leisure-time physical activity (LPA), "
     "model-based estimates for all 3,143 counties. Inverted so higher scores indicate more active communities."),
    ("Component 2 — Race Event Density",
     "RunSignUp public API, queried for all 50 states (2019–2024). 17,810 unique races identified "
     "and geocoded using a Census ZCTA-to-county crosswalk. Normalized per 100,000 population."),
    ("Component 3 — Exercise Infrastructure Access",
     "County Health Rankings 2025 (UW-RWJF). Percentage of residents with adequate access to "
     "exercise opportunities (v132)."),
    ("Component 4 — Fitness Facility Density",
     "USDA Food Environment Atlas 2020. Recreational facilities per 1,000 population (NAICS 713940). "
     "Counties with missing values (n = 1,849) assigned zero."),
    ("Component 5 — Neighborhood Walkability",
     "EPA National Walkability Index (Smart Location Database, 2021). Block group–level scores "
     "aggregated to county level using population-weighted means across 220,739 block groups."),
]:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.3)
    p.paragraph_format.space_after = Pt(4)
    r1 = p.add_run(comp[0] + ": ")
    r1.font.name = "Times New Roman"; r1.font.size = Pt(12); r1.font.bold = True
    r2 = p.add_run(comp[1])
    r2.font.name = "Times New Roman"; r2.font.size = Pt(12)

doc.add_paragraph()

section_heading("3.3  Outcome Variables", level=2)
body(
    "Health outcomes were drawn from CDC PLACES 2023 and County Health Rankings 2025 (life "
    "expectancy, premature death). Real estate outcomes used the Zillow Home Value Index (ZHVI, "
    "February 2026, covering 3,073 counties). Socioeconomic controls included median household "
    "income, unemployment rate, and percentage uninsured from County Health Rankings 2025. "
    "Urbanicity was measured using the USDA Rural-Urban Continuum Code (RUCC 2023), a 9-point "
    "scale from dense metro (1) to most rural (9)."
)

section_heading("3.4  Statistical Analysis", level=2)
body(
    "Bivariate analysis used Spearman rank correlations. Multivariate analysis used OLS regression "
    "with log-transformed ZHVI as the dependent variable and HC3 heteroskedasticity-robust "
    "standard errors. Health outcome regressions used raw rates controlling for log median income. "
    "Robustness checks re-estimated the primary model with RUCC as an additional control and in "
    "metro-only and non-metro-only subsamples."
)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 4 — RESULTS
# ═══════════════════════════════════════════════════════════════════════════════
section_heading("4. Results")
section_heading("4.1  RunScore Distribution", level=2)
body(
    "RunScore ranges from 0.03 to 100 across 3,143 U.S. counties (mean = 50.0, SD = 28.9 by "
    "construction). High-RunScore counties concentrate in the Northeast corridor, the Mountain "
    "West, the Pacific Northwest, and dense coastal metros. Low-RunScore counties concentrate in "
    "the rural Deep South, the Texas Panhandle, and the Northern Great Plains, characterized by "
    "physical inactivity rates of 40–50%, zero organized race events, and near-zero walkability."
)

italic_note("Table 1: Top and Bottom Counties by RunScore — see Appendix A for full dataset.")

section_heading("4.2  Bivariate Correlations", level=2)
body("Table 2 reports Spearman rank correlations between RunScore and key outcome variables.")

add_table(
    headers=["Outcome Variable", "Spearman r", "n", "Significance"],
    rows=[
        ["Exercise access",          "+0.807", "3,097", "p < 0.001"],
        ["EPA Walkability Index",     "+0.761", "3,132", "p < 0.001"],
        ["Physical inactivity",       "−0.733", "2,956", "p < 0.001"],
        ["Smoking rate",              "−0.710", "2,956", "p < 0.001"],
        ["Fair/poor health",          "−0.673", "2,956", "p < 0.001"],
        ["Diabetes rate",             "−0.676", "2,956", "p < 0.001"],
        ["Hypertension rate",         "−0.648", "2,956", "p < 0.001"],
        ["Heart disease rate",        "−0.645", "2,956", "p < 0.001"],
        ["Median household income",   "+0.634", "3,142", "p < 0.001"],
        ["Home value (ZHVI)",         "+0.604", "3,064", "p < 0.001"],
        ["Life expectancy",           "+0.582", "3,060", "p < 0.001"],
        ["Obesity rate",              "−0.570", "2,956", "p < 0.001"],
        ["Premature death (YPLL)",    "−0.560", "3,080", "p < 0.001"],
        ["Park access",               "+0.554", "2,846", "p < 0.001"],
        ["5-year home appreciation",  "+0.186", "3,013", "p < 0.001"],
        ["1-year home appreciation",  "+0.142", "3,064", "p < 0.001"],
        ["Social associations/10k",   "−0.013", "3,143", "n.s."],
    ],
    col_widths=[2.8, 1.0, 0.8, 1.2]
)
italic_note("Table 2. Spearman rank correlations between RunScore and selected outcomes. n.s. = not significant.")

section_heading("4.3  RunScore and Home Values", level=2)
body(
    "Table 3 presents the OLS regression of log home values on income, controls, and RunScore. "
    "Income alone explains 57.8% of county-level home value variance (Model 1). Adding health "
    "and labor controls raises R² to 61.1% (Model 2). Adding RunScore raises R² to 63.3% — a "
    "statistically significant increment of +2.2 percentage points (p < 0.001). The RunScore "
    "coefficient (β = 0.0035) is significant at p < 0.001 and stable across specifications."
)

add_table(
    headers=["Variable", "Model 1\nIncome only", "Model 2\n+ Controls", "Model 3\n+ RunScore"],
    rows=[
        ["Constant",              "−5.539***", "−6.475***", "−3.935***"],
        ["Log(Median Income)",    "1.617***",  "1.488***",  "1.279***"],
        ["% Unemployed",          "—",         "5.000***",  "4.356***"],
        ["% Uninsured",           "—",         "1.237***",  "1.505***"],
        ["Life Expectancy",       "—",         "0.027***",  "0.022***"],
        ["RunScore",              "—",         "—",         "0.0035***"],
        ["N",                     "3,017",     "3,017",     "3,017"],
        ["R²",                    "0.578",     "0.611",     "0.633"],
        ["Adj. R²",               "0.578",     "0.610",     "0.632"],
    ],
    col_widths=[2.2, 1.4, 1.4, 1.4]
)
italic_note("Table 3. OLS regression, dependent variable = log(ZHVI). HC3 robust standard errors. *** p < 0.001.")

body(
    "Each 10-point increase in RunScore is associated with a 3.5% increase in median home value, "
    "holding all controls constant. Evaluated at the sample median home value of $223,928:"
)
for row in [
    "+10 RunScore points  →  +3.5% home value  →  +$7,885",
    "+25 RunScore points  →  +9.0% home value  →  +$20,237",
    "+50 RunScore points  →  +18.9% home value  →  +$42,304",
]:
    p = doc.add_paragraph(style="List Bullet")
    run = p.add_run(row)
    run.font.name = "Times New Roman"; run.font.size = Pt(12); run.font.bold = True
doc.add_paragraph()

section_heading("4.4  RunScore and Health Outcomes", level=2)
body(
    "Table 4 shows RunScore's coefficient in regressions of health outcomes on RunScore and log "
    "median income. RunScore adds significant explanatory power beyond income for every outcome."
)

add_table(
    headers=["Outcome", "β per point", "SE", "t", "p", "ΔR²"],
    rows=[
        ["Smoking rate (%)",       "−0.0477", "0.0019", "−24.64", "<0.001", "+0.093"],
        ["Hypertension (%)",       "−0.0640", "0.0032", "−20.13", "<0.001", "+0.069"],
        ["Obesity rate (%)",       "−0.0532", "0.0030", "−17.68", "<0.001", "+0.062"],
        ["Heart disease (%)",      "−0.0161", "0.0009", "−17.60", "<0.001", "+0.057"],
        ["Diabetes rate (%)",      "−0.0294", "0.0015", "−19.74", "<0.001", "+0.056"],
        ["Fair/poor health (%)",   "−0.0472", "0.0023", "−20.20", "<0.001", "+0.048"],
        ["Poor sleep (%)",         "−0.0262", "0.0030", "−8.76",  "<0.001", "+0.020"],
        ["Life expectancy (yrs)",  "+0.0196", "0.0021", "+9.29",  "<0.001", "+0.014"],
        ["Premature death (YPLL)", "−19.75",  "2.40",   "−8.23",  "<0.001", "+0.013"],
    ],
    col_widths=[2.2, 1.0, 0.8, 0.9, 0.9, 0.8]
)
italic_note("Table 4. RunScore coefficient in health regressions controlling for log median income. n = 2,955–3,142.")

body(
    "RunScore adds significant explanatory power beyond income for every health outcome tested. "
    "The strongest incremental contribution is for smoking (ΔR² = +0.093), suggesting that running "
    "culture captures a dimension of health behavior that income alone does not. A county moving "
    "from the 25th to 75th percentile of RunScore (a 50-point increase) is associated with "
    "3.2 percentage points lower hypertension, 2.7 percentage points lower obesity, 2.4 percentage "
    "points lower smoking, 1.5 percentage points lower diabetes, and 1.0 additional year of life "
    "expectancy."
)

section_heading("4.5  Robustness Checks", level=2)
body(
    "Table 5 shows the RunScore coefficient across robustness specifications. RunScore "
    "remains significant at p < 0.001 in all subgroups. The effect is larger in "
    "non-metro counties (β = 0.00374) than in metro counties (β = 0.00229), indicating that "
    "running culture adds disproportionate value in rural communities — precisely where "
    "existing platform signals like Walk Score have the thinnest coverage."
)

add_table(
    headers=["Model", "N", "R²", "RunScore β", "SE", "p"],
    rows=[
        ["Full sample (no RUCC)",           "3,017", "0.633", "0.00346", "0.00025", "<0.001"],
        ["+ RUCC urbanicity control",        "3,017", "0.641", "0.00276", "0.00027", "<0.001"],
        ["Metro counties only (RUCC 1–3)",   "1,174", "0.702", "0.00229", "0.00033", "<0.001"],
        ["Non-metro counties (RUCC 4–9)",    "1,843", "0.486", "0.00374", "0.00038", "<0.001"],
    ],
    col_widths=[2.8, 0.6, 0.6, 1.0, 0.8, 0.8]
)
italic_note("Table 5. RunScore coefficient across robustness specifications. All HC3 robust standard errors.")

section_heading("4.6  RunScore and Home Value Appreciation", level=2)
body(
    "The preceding analysis establishes that RunScore is associated with current home values. A more "
    "commercially relevant question for real estate platforms is whether RunScore predicts future "
    "home value growth — that is, whether it functions as a leading indicator."
)

add_table(
    headers=["Variable", "β", "SE", "p"],
    rows=[
        ["Constant",              "−25.69",      "23.53", "0.275"],
        ["Log(Median Income)",    "3.29",        "2.55",  "0.197"],
        ["% Unemployed",          "−186.82***",  "33.53", "<0.001"],
        ["% Uninsured",           "−22.65**",    "8.33",  "0.007"],
        ["Life Expectancy",       "0.30",        "0.17",  "0.076"],
        ["RunScore",              "0.087***",    "0.015", "<0.001"],
        ["RUCC",                  "0.06",        "0.14",  "0.680"],
        ["N",                     "2,983",       "",      ""],
        ["R²",                    "0.093",       "",      ""],
    ],
    col_widths=[2.2, 1.4, 1.0, 1.0]
)
italic_note("Table 6. OLS regression, DV = 5-year home value appreciation (%). HC3 robust SE. ** p<0.01, *** p<0.001.")

body(
    "RunScore is a significant predictor of five-year home value appreciation (β = 0.087, "
    "p < 0.001), even after controlling for income, employment, insurance, life expectancy, and "
    "urbanicity. Notably, income itself is not significant in this model — appreciation is driven "
    "by factors beyond current wealth. Each 10-point RunScore increase predicts 0.9 additional "
    "percentage points of five-year appreciation. For a $300,000 home, a 25-point RunScore "
    "advantage implies approximately $6,600 of additional five-year price growth."
)

section_heading("4.7  Community Deep Dives", level=2)
body(
    "Table 7 profiles eight counties representing the extremes of the RunScore distribution. "
    "The range across extremes is stark: Teton County, WY has a life expectancy of 87.6 years "
    "and home values exceeding $2.1 million with 67.5% five-year appreciation. Oglala Lakota "
    "County, SD has a life expectancy of 56.9 years — comparable to some developing nations — "
    "with no organized race events and 1.9% exercise access."
)
body(
    "Missoula County, MT is instructive: with a median income of $72,882 — well below Nantucket's "
    "$108,671 — Missoula achieves a nearly identical RunScore (99.5 vs. 99.9) and comparable "
    "health outcomes, with home values of $559,508 and 44.5% five-year appreciation. Running "
    "culture, built through trails, a university, and race events, drives outcomes that exceed "
    "what income alone would predict."
)

add_table(
    headers=["Community", "RunScore", "Inactive", "Obese", "Life Exp.", "Home Value", "5yr Appr.", "Income"],
    rows=[
        ["Teton Co., WY",          "99.8", "18.3%", "24.0%", "87.6 yrs", "$2,147,757", "+67.5%", "$130,156"],
        ["Gallatin Co., MT",       "99.5", "13.9%", "23.0%", "82.0 yrs", "$689,955",   "+31.8%", "$90,942"],
        ["Missoula Co., MT",       "99.5", "16.5%", "26.2%", "78.6 yrs", "$559,508",   "+44.5%", "$72,882"],
        ["Nantucket Co., MA",      "99.9", "17.2%", "27.7%", "82.8 yrs", "$3,029,344", "+48.7%", "$108,671"],
        ["New York Co., NY",       "99.8", "20.4%", "19.2%", "83.0 yrs", "$1,217,413", "−9.3%",  "$100,869"],
        ["Humphreys Co., MS",      "0.1",  "47.9%", "52.4%", "66.6 yrs", "$82,469",    "+7.0%",  "$31,538"],
        ["Greene Co., AL",         "0.0",  "44.7%", "52.7%", "70.6 yrs", "$125,975",   "−2.9%",  "$34,619"],
        ["Oglala Lakota Co., SD",  "0.2",  "40.1%", "47.0%", "56.9 yrs", "N/A",        "N/A",    "$42,791"],
    ],
    col_widths=[1.8, 0.7, 0.7, 0.6, 0.8, 1.0, 0.7, 0.9]
)
italic_note("Table 7. Community deep dive profiles. Home value = Zillow ZHVI Feb 2026.")

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 5 — DISCUSSION
# ═══════════════════════════════════════════════════════════════════════════════
section_heading("5. Discussion")
section_heading("5.1  What RunScore Actually Measures", level=2)
body(
    "RunScore is not purely a measure of how much people run. It is a measure of whether a "
    "community has built the conditions — infrastructure, culture, events, facilities, walkable "
    "streets — that make running a normal, accessible part of daily life. A community with high "
    "RunScore is one where the sidewalks are there, the trails are there, the gym is nearby, and "
    "the local race calendar gives people a reason to train. These conditions make running easy "
    "and, critically, normal — which matters for behavior change in ways that one isolated "
    "element does not."
)
body(
    "This is why RunScore predicts home values even after controlling for income. High-RunScore "
    "communities have made specific, observable investments in the built environment and community "
    "programming that buyers want to live in — and buyers reveal this preference through prices."
)

section_heading("5.2  Implications for Real Estate Platforms", level=2)
body(
    "The finding that each 10-point increase in RunScore is associated with a 3.5% increase in "
    "home values, holding income constant, has direct practical implications. But the more "
    "commercially significant finding is the appreciation result: RunScore predicts future home "
    "value growth (β = 0.087 per point, p < 0.001) even when income does not. This transforms "
    "RunScore from a descriptive label into a predictive signal."
)
body(
    "Walk Score measures pedestrian convenience. School ratings measure educational outcomes. "
    "Crime statistics measure safety. RunScore measures whether a community has built the "
    "conditions for a physically active lifestyle — a preference that has grown consistently since "
    "the early 2000s and accelerated through the COVID-19 pandemic's reshaping of residential "
    "priorities. Each 10-point RunScore increase predicts 0.9 additional percentage points of "
    "five-year appreciation, controlling for income, employment, and urbanicity."
)

section_heading("5.3  Practical Implementation for Real Estate Platforms", level=2)
body(
    "RunScore is designed for direct integration into residential real estate platforms. It can be "
    "displayed as a 0–100 badge on individual property listings, analogous to Walk Score. Buyers "
    "could filter by minimum RunScore or sort listings by RunScore within a price range — addressing "
    "a gap in current platform search: no existing filter captures 'communities where people "
    "actually exercise.'"
)
body(
    "For relocation buyers, RunScore provides a single comparable number across the full United "
    "States. A buyer leaving a RunScore-85 community can identify comparable communities in their "
    "target region. The appreciation regression suggests RunScore as a forward-looking signal for "
    "home value growth — counties with rising RunScore components may represent investment "
    "opportunities. All five components are derived from publicly available, annually updated "
    "datasets requiring no proprietary data, no API licensing fees, and no survey infrastructure."
)

section_heading("5.4  Implications for Public Health", level=2)
body(
    "The independent association between RunScore and nine health outcomes — spanning behavioral, "
    "metabolic, cardiovascular, and longevity domains — after controlling for income, supports the "
    "interpretation that running infrastructure and culture have health effects beyond income "
    "itself. The strongest incremental contribution is for smoking (ΔR² = +0.093), suggesting "
    "RunScore captures a generalizable dimension of health culture, not just running behavior."
)
body(
    "Counties that are poor but have relatively high RunScore are healthier than poor counties "
    "with low RunScore. This pattern is consistent with a causal interpretation but does not "
    "establish it; wealthier, healthier movers may select into high-RunScore communities, "
    "generating correlation without direct environmental causation. Establishing causality "
    "requires quasi-experimental designs — an important direction for future work."
)

section_heading("5.5  Limitations", level=2)
for lim in [
    ("Small-county artifacts:", "The race event density component is normalized per 100,000 population. In very small counties (population under 5,000), a single race event produces an outsized per-capita rate. This does not invalidate the regression analysis, where these counties have negligible leverage, but affects the interpretability of the top-ranked counties list."),
    ("Missing data:", "Zillow ZHVI is unavailable for the most rural counties. Fitness facility data is missing for 1,849 counties, replaced with zero. Missing data concentrates in low-RunScore counties, potentially attenuating true effect sizes."),
    ("RunSignUp representativeness:", "Platform penetration varies by region. Events on other registration platforms (e.g., ACTIVE.com) are not captured, which may systematically undercount races in some areas."),
    ("Strava data absence:", "The optimal Component 2 would be GPS-verified running trip counts from Strava Metro. A Strava Metro academic cohort application is pending; this data will substantially strengthen the measure."),
    ("Reverse causality:", "High home values may attract healthier, more active populations. The appreciation regression (Section 4.6) provides partial mitigation: RunScore predicts future price growth, not just current levels. A fully causal design would require quasi-experimental variation."),
    ("Selection bias:", "People who prioritize running culture may self-select into high-RunScore communities, generating observed health differences via sorting rather than environmental effects."),
]:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.3)
    p.paragraph_format.space_after = Pt(4)
    r1 = p.add_run(lim[0] + " ")
    r1.font.name = "Times New Roman"; r1.font.size = Pt(12); r1.font.bold = True
    r2 = p.add_run(lim[1])
    r2.font.name = "Times New Roman"; r2.font.size = Pt(12)

doc.add_paragraph()

section_heading("5.6  Future Work", level=2)
for fw in [
    "Strava Metro integration: Incorporating actual GPS trip counts (pending cohort application) to replace modeled physical inactivity proxies with observed running behavior.",
    "Sub-county resolution: Applying RunScore at the ZIP code or census tract level — the resolution most relevant for individual listing-level real estate applications.",
    "Longitudinal panel design: Testing whether changes in RunScore components predict subsequent home price appreciation, controlling for baseline values.",
    "Causal identification: Using natural experiments — trail construction bond measures, rail-trail conversions, parkrun establishment — to estimate causal effects of running infrastructure.",
    "Platform integration pilot: Partnering with a residential real estate platform to display RunScore alongside existing neighborhood signals and measuring user engagement and buyer satisfaction.",
]:
    p = doc.add_paragraph(style="List Number")
    run = p.add_run(fw)
    run.font.name = "Times New Roman"; run.font.size = Pt(12)

doc.add_paragraph()

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 6 — CONCLUSION
# ═══════════════════════════════════════════════════════════════════════════════
section_heading("6. Conclusion")
body(
    "This study introduces RunScore, a five-component composite index of county-level running "
    "activity and infrastructure, computed for all 3,143 U.S. counties. RunScore demonstrates "
    "strong bivariate correlations with home values (r = +0.604), life expectancy (r = +0.582), "
    "obesity (r = −0.570), and diabetes (r = −0.676). In multivariate regression, RunScore "
    "predicts county-level home values independently of median household income, unemployment, "
    "insurance coverage, life expectancy, and urbanicity, with each 10-point increase associated "
    "with a 3.5% increase in median home value — approximately $7,885. This effect holds across "
    "metro and non-metro subgroups and is robust to a range of control specifications."
)
body(
    "Critically, RunScore also predicts future home value growth: each 10-point increase is "
    "associated with 0.9 additional percentage points of five-year appreciation, controlling for "
    "income, employment, and urbanicity. This forward-looking predictive power — present even when "
    "income itself is not a significant predictor of appreciation — transforms RunScore from a "
    "descriptive community label into an actionable market signal."
)
body(
    "RunScore fills a genuine gap: it is the first nationally comparable, county-level index to "
    "capture running activity as a community behavior and validate it against both health and "
    "real estate outcomes simultaneously. It is replicable from public data, updatable annually, "
    "and directly embeddable in residential real estate platforms as a lifestyle desirability signal. "
    "The methodology is open, the data pipeline requires no proprietary inputs, and the computational "
    "cost is negligible at scale."
)
body(
    "The 30.7-year gap in life expectancy between Oglala Lakota County, SD (56.9 years) and "
    "Teton County, WY (87.6 years) is not explained by running. But running culture — and the "
    "infrastructure and investment decisions that produce it — is one measurable dimension of "
    "what makes some communities places where people live long, healthy lives. RunScore is a "
    "way to see and compare that dimension at scale."
)

# ═══════════════════════════════════════════════════════════════════════════════
# FIGURES
# ═══════════════════════════════════════════════════════════════════════════════
doc.add_page_break()
section_heading("Figures")

fig_files = [
    ("figures/fig1_runscore_vs_homevalue.png",
     "Figure 1. RunScore vs. Median Home Value (ZHVI) across 3,143 U.S. counties. Points colored by income tercile (red = low income, yellow = middle, green = high). Trend line fits all counties. Spearman r = +0.604, p < 0.001."),
    ("figures/fig2_runscore_vs_health.png",
     "Figure 2. RunScore vs. Health Outcomes. Clockwise from top-left: obesity rate, diabetes rate, life expectancy, and fair/poor health rate. All Spearman correlations significant at p < 0.001."),
    ("figures/fig3_deepdive_comparison.png",
     "Figure 3. Community Deep Dive Comparison. Eight selected counties ranked by RunScore (green = high, red = low) across four key metrics. High-RunScore communities dominate on every dimension."),
    ("figures/fig4_runscore_map.png",
     "Figure 4. RunScore Choropleth — Contiguous United States. Green counties rank high on running activity and infrastructure; red counties rank low. The geographic clustering of low-RunScore counties in the rural Deep South and high-RunScore counties in the Mountain West and Northeast is visible."),
]

for fig_path, caption in fig_files:
    if os.path.exists(fig_path):
        doc.add_picture(fig_path, width=Inches(6.0))
        last_p = doc.paragraphs[-1]
        last_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap = doc.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap.paragraph_format.space_after = Pt(18)
        run = cap.add_run(caption)
        run.font.name = "Times New Roman"; run.font.size = Pt(10); run.font.italic = True

# ═══════════════════════════════════════════════════════════════════════════════
# REFERENCES
# ═══════════════════════════════════════════════════════════════════════════════
doc.add_page_break()
section_heading("References")

refs = [
    "Brownson, R. C., Hoehner, C. M., Day, K., Forsyth, A., & Sallis, J. F. (2009). Measuring the built environment for physical activity: State of the science. American Journal of Preventive Medicine, 36(4), S99–S123.",
    "Morris, P., & Weed, M. (2023). parkrun: Much more than just a run in the park. British Journal of Sports Medicine, 57(9), 517–518.",
    "Centers for Disease Control and Prevention. (2023). PLACES: Local data for better health, county data 2023 release. CDC. https://www.cdc.gov/places",
    "Crompton, J. L. (2001). The impact of parks on property values: A review of the empirical evidence. Journal of Leisure Research, 33(1), 1–31.",
    "Joh, K., Nguyen, M. T., & Boarnet, M. G. (2015). Rate of physical activity and community health: Evidence from U.S. counties. Journal of Planning Education and Research, 35(1), 5–17.",
    "Leinberger, C. B., & Alfonzo, M. (2012). Walk this way: The economic promise of walkable places in metropolitan Washington, DC. Brookings Institution.",
    "Physical Activity Guidelines Advisory Committee. (2018). 2018 physical activity guidelines advisory committee scientific report. U.S. Department of Health and Human Services.",
    "Robert Wood Johnson Foundation / University of Wisconsin Population Health Institute. (2025). County Health Rankings & Roadmaps: 2025 national data. https://www.countyhealthrankings.org",
    "Sallis, J. F., Bull, F., Guthold, R., Heath, G. W., Inoue, S., Kelly, P., … & Hallal, P. C. (2016). Progress in physical activity over the Olympic quadrennium. The Lancet, 388(10051), 1325–1336.",
    "Sports & Fitness Industry Association. (2024). 2024 SFIA topline participation report. SFIA.",
    "U.S. Environmental Protection Agency. (2021). National Walkability Index: Methodology and user guide. Office of Sustainable Communities, Smart Growth Program.",
    "U.S. Department of Agriculture, Economic Research Service. (2020). Food environment atlas. https://www.ers.usda.gov/data-products/food-environment-atlas",
    "Zillow Research. (2026). Zillow Home Value Index (ZHVI): Data methodology and downloads. https://www.zillow.com/research/data",
]

for ref in refs:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent   = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.5)
    p.paragraph_format.space_after   = Pt(6)
    run = p.add_run(ref)
    run.font.name = "Times New Roman"; run.font.size = Pt(11)

# ═══════════════════════════════════════════════════════════════════════════════
# APPENDIX C — DATA SOURCES
# ═══════════════════════════════════════════════════════════════════════════════
doc.add_page_break()
section_heading("Appendix — Data Sources")

add_table(
    headers=["Dataset", "Provider", "Year", "Coverage", "Access"],
    rows=[
        ["CDC PLACES — Physical Inactivity", "CDC", "2023", "3,143 counties", "Free: data.cdc.gov"],
        ["County Health Rankings", "UW-RWJF", "2025", "3,143 counties", "Free: countyhealthrankings.org"],
        ["Zillow Home Value Index (ZHVI)", "Zillow Research", "Feb 2026", "3,073 counties", "Free: zillow.com/research/data"],
        ["RunSignUp Race Events", "RunSignUp", "2019–2024", "17,810 events, 50 states", "Free API: runsignup.com/rest"],
        ["EPA National Walkability Index", "U.S. EPA", "2021", "220,739 block groups", "Free: epa.gov/smartgrowth"],
        ["USDA Food Environment Atlas", "USDA ERS", "2020", "3,144 counties", "Free: ers.usda.gov"],
        ["USDA Rural-Urban Continuum Codes", "USDA ERS", "2023", "3,233 counties", "Free: ers.usda.gov"],
        ["Census ZCTA-County Crosswalk", "U.S. Census Bureau", "2020", "All ZCTAs", "Free: census.gov"],
    ],
    col_widths=[2.0, 1.3, 0.7, 1.5, 2.0]
)

# ── Save ─────────────────────────────────────────────────────────────────────
output_path = "RunScore_Paper_Popler_2026.docx"
doc.save(output_path)
import os
size = os.path.getsize(output_path)
print(f"Saved: {output_path}  ({size/1e6:.1f} MB)")