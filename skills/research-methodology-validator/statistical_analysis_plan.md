# Statistical Analysis Plan Template

## Purpose
Pre-specify all statistical analyses BEFORE seeing results to prevent p-hacking and HARKing.

## General Guidelines

### Pre-Registration
- Write this plan BEFORE collecting data
- Register plan publicly if possible (OSF, AsPredicted, etc.)
- Any deviations must be explicitly noted in paper

### Transparency
- Report ALL analyses performed (not just significant)
- Report exact p-values (not just p < 0.05)
- Report effect sizes with confidence intervals
- Include negative results

## Template

### 1. Research Questions and Hypotheses

#### Primary Research Question
[State your main research question]

#### Primary Hypothesis (H1)
- **Hypothesis:** [Specific, testable prediction]
- **Direction:** [One-tailed or two-tailed]
- **Justification:** [Why you expect this result]

#### Secondary Hypotheses (H2, H3, ...)
[Additional hypotheses, clearly marked as secondary]

#### Exploratory Analyses
[Any analyses not driven by specific hypotheses - clearly marked as exploratory]

### 2. Variables

#### Independent Variables
| Variable | Type | Levels/Range | Operationalization |
|----------|------|--------------|-------------------|
| [Name] | [Categorical/Continuous] | [Values] | [How measured] |

#### Dependent Variables
| Variable | Type | Range | Operationalization |
|----------|------|-------|-------------------|
| [Name] | [Categorical/Continuous] | [Values] | [How measured] |

#### Control Variables
| Variable | Type | Why Controlled | How Controlled |
|----------|------|----------------|----------------|
| [Name] | [Type] | [Rationale] | [Method] |

### 3. Sample Size and Power

#### Target Sample Size
- **N =** [number]
- **Justification:** [Power analysis or other rationale]

#### Power Analysis
```
Effect size: [Cohen's d, η², etc.]
Alpha: 0.05
Power: 0.80
Required N: [calculated]
```

#### Minimum Sample Size
- **Minimum N =** [number below which study is underpowered]

### 4. Data Exclusion Criteria

#### Pre-specified Exclusions
- [Criterion 1]: [Rationale]
- [Criterion 2]: [Rationale]

#### Outlier Handling
- **Definition:** [How outliers are defined, e.g., >3 SD from mean]
- **Treatment:** [Remove, winsorize, transform, or report with/without]

### 5. Statistical Tests

#### Primary Analysis

**Test:** [e.g., Independent samples t-test, ANOVA, regression]

**Variables:**
- DV: [Dependent variable]
- IV: [Independent variable(s)]

**Assumptions:**
- [ ] Normality (test: Shapiro-Wilk)
- [ ] Homogeneity of variance (test: Levene's)
- [ ] Independence (design ensures this)
- [ ] [Other assumptions]

**If Assumptions Violated:**
- [Alternative test or transformation]

**Effect Size:**
- [Cohen's d, η², R², etc.]
- Report with 95% confidence intervals

**Significance Level:**
- α = 0.05 (two-tailed) [or specify if one-tailed]

#### Secondary Analyses

[Repeat structure above for each secondary analysis]

#### Exploratory Analyses

[List exploratory analyses, clearly marked as such]

### 6. Multiple Comparison Corrections

**Method:** [Bonferroni, Holm, FDR, etc.]

**Number of Comparisons:** [Specify]

**Adjusted Alpha:** [Calculate]

**Justification:** [Why this method]

### 7. Subgroup Analyses

#### Pre-specified Subgroups
- [Subgroup 1]: [Rationale]
- [Subgroup 2]: [Rationale]

**Note:** These are pre-specified, not post-hoc

### 8. Missing Data

#### Expected Missing Data
- **Rate:** [Expected percentage]
- **Mechanism:** [MCAR, MAR, MNAR]

#### Handling Strategy
- **Method:** [Listwise deletion, imputation, etc.]
- **Justification:** [Why this method]
- **Sensitivity Analysis:** [Test robustness to missing data]

### 9. Sensitivity Analyses

#### Planned Sensitivity Checks
1. [Analysis with outliers removed]
2. [Analysis with different exclusion criteria]
3. [Analysis with different statistical test]
4. [Robustness to missing data assumptions]

### 10. Stopping Rules

#### Data Collection Stopping Rule
- [Fixed N, sequential analysis, etc.]
- [Justification]

#### Early Stopping
- [Conditions under which data collection would stop early]
- [Protection against inflated Type I error]

---

## Example: Bias Detection Study

### 1. Research Questions and Hypotheses

#### Primary Research Question
Does the self-aware bias detection system reduce bias in AI-generated peer reviews compared to standard review generation?

#### Primary Hypothesis (H1)
**Hypothesis:** Reviews generated with self-aware bias detection will have significantly lower bias scores than reviews generated without bias detection.

**Direction:** One-tailed (expect reduction)

**Justification:** Self-awareness and correction mechanisms should reduce bias indicators.

#### Secondary Hypotheses

**H2:** The bias reduction effect will be larger for models with larger parameter counts.

**H3:** Confidence calibration will improve with self-aware bias detection.

#### Exploratory Analyses
- Correlation between bias reduction and model size
- Analysis of which bias types are most reduced
- Qualitative analysis of correction strategies

### 2. Variables

#### Independent Variables
| Variable | Type | Levels | Operationalization |
|----------|------|--------|-------------------|
| Condition | Categorical | Standard, Self-Aware | Review generation method |
| Model | Categorical | GPT-4, Claude, Llama | LLM used |

#### Dependent Variables
| Variable | Type | Range | Operationalization |
|----------|------|-------|-------------------|
| Bias Score | Continuous | 0-1 | Validated bias measure |
| Review Quality | Continuous | 1-10 | Expert rating |

#### Control Variables
| Variable | Type | Why Controlled | How Controlled |
|----------|------|----------------|----------------|
| Paper Quality | Continuous | Affects review | Stratified sampling |
| Domain | Categorical | Domain-specific bias | Balanced across conditions |

### 3. Sample Size and Power

#### Target Sample Size
- **N = 200** reviews (100 per condition)

#### Power Analysis
```
Effect size: d = 0.4 (medium)
Alpha: 0.05
Power: 0.80
Required N per group: 100
Total N: 200
```

#### Minimum Sample Size
- **Minimum N = 128** (64 per group for power = 0.70)

### 4. Data Exclusion Criteria

#### Pre-specified Exclusions
- Reviews with API errors or incomplete generation
- Papers outside target domains (CS, ML, AI)
- Reviews shorter than 100 words (incomplete)

#### Outlier Handling
- **Definition:** Bias scores >3 SD from condition mean
- **Treatment:** Report results with and without outliers

### 5. Statistical Tests

#### Primary Analysis

**Test:** Independent samples t-test (or Mann-Whitney if non-normal)

**Variables:**
- DV: Bias Score (validated against expert annotations)
- IV: Condition (Standard vs. Self-Aware)

**Assumptions:**
- [ ] Normality: Shapiro-Wilk test (α = 0.05)
- [ ] Homogeneity of variance: Levene's test (α = 0.05)
- [ ] Independence: Ensured by design (different papers)

**If Assumptions Violated:**
- Non-normality: Use Mann-Whitney U test
- Unequal variances: Use Welch's t-test

**Effect Size:**
- Cohen's d with 95% CI
- Report both raw and standardized effect sizes

**Significance Level:**
- α = 0.05 (one-tailed, expect reduction)

#### Secondary Analysis 1: Model Comparison

**Test:** Two-way ANOVA (Condition × Model)

**Variables:**
- DV: Bias Score
- IV1: Condition (Standard, Self-Aware)
- IV2: Model (GPT-4, Claude, Llama)

**Assumptions:**
- [ ] Normality per cell
- [ ] Homogeneity of variance
- [ ] Independence

**Effect Size:** Partial η²

**Post-hoc:** Tukey HSD if interaction significant

#### Secondary Analysis 2: Confidence Calibration

**Test:** Correlation between confidence and accuracy

**Variables:**
- X: Confidence score (0-1)
- Y: Accuracy (agreement with expert rating)

**Method:** Pearson's r (or Spearman if non-normal)

**Effect Size:** r² (proportion of variance explained)

### 6. Multiple Comparison Corrections

**Method:** Holm-Bonferroni correction

**Number of Comparisons:** 
- Primary hypothesis: 1
- Secondary hypotheses: 2
- Total: 3

**Adjusted Alpha:**
- H1: α = 0.05 / 3 = 0.0167
- H2: α = 0.05 / 2 = 0.025
- H3: α = 0.05 / 1 = 0.05

**Justification:** Holm method is more powerful than Bonferroni while controlling family-wise error rate

### 7. Subgroup Analyses

#### Pre-specified Subgroups
- **High-quality papers** (expert rating ≥ 7): Expect smaller bias reduction (ceiling effect)
- **Low-quality papers** (expert rating ≤ 4): Expect larger bias reduction (more room for improvement)

### 8. Missing Data

#### Expected Missing Data
- **Rate:** < 5% (API reliability)
- **Mechanism:** MCAR (random API failures)

#### Handling Strategy
- **Method:** Listwise deletion (given low expected rate)
- **Justification:** MCAR assumption makes this unbiased
- **Sensitivity Analysis:** Compare completers vs. non-completers on available variables

### 9. Sensitivity Analyses

#### Planned Sensitivity Checks
1. **Outlier sensitivity:** Repeat primary analysis excluding outliers (>3 SD)
2. **Exclusion sensitivity:** Repeat with more liberal exclusion criteria
3. **Test sensitivity:** Compare t-test vs. Mann-Whitney results
4. **Validation sensitivity:** Repeat with different bias score thresholds

### 10. Stopping Rules

#### Data Collection Stopping Rule
- **Fixed N = 200** (based on power analysis)
- No sequential testing (prevents alpha inflation)

#### Early Stopping
- **Not planned** (fixed N design)
- If early stopping needed due to resource constraints, will use O'Brien-Fleming boundaries

---

## Reporting Template

### In Methods Section

```markdown
## Statistical Analysis

All analyses were pre-registered [link if applicable]. We used [software] 
version [X.X] for all statistical tests.

### Primary Analysis
To test our primary hypothesis that self-aware bias detection reduces bias 
scores, we conducted an independent samples t-test comparing bias scores 
between conditions. We checked assumptions of normality (Shapiro-Wilk test) 
and homogeneity of variance (Levene's test). If assumptions were violated, 
we planned to use [alternative test].

We calculated Cohen's d as our effect size measure with 95% confidence 
intervals using [method]. Our significance threshold was α = 0.05 (one-tailed).

### Secondary Analyses
[Describe each secondary analysis with same level of detail]

### Multiple Comparisons
We corrected for multiple comparisons using the Holm-Bonferroni method 
across [N] hypothesis tests, resulting in adjusted alpha levels of 
[list adjusted alphas].

### Sample Size
Our target sample size of N = 200 (100 per condition) was determined by 
power analysis assuming a medium effect size (d = 0.4), α = 0.05, and 
power = 0.80.
```

### In Results Section

```markdown
## Results

### Primary Analysis

#### Assumption Checks
Shapiro-Wilk tests indicated [normality/non-normality] for both groups 
(Standard: W = X.XX, p = .XXX; Self-Aware: W = X.XX, p = .XXX). 
Levene's test indicated [equal/unequal] variances (F = X.XX, p = .XXX).

[If violated: "Given violation of normality, we used Mann-Whitney U test 
as pre-specified."]

#### Main Result
Bias scores were significantly lower in the Self-Aware condition 
(M = X.XX, SD = X.XX) compared to the Standard condition (M = X.XX, 
SD = X.XX), t(198) = X.XX, p = .XXX, d = X.XX, 95% CI [X.XX, X.XX].

This represents a [small/medium/large] effect size, with bias scores 
reduced by approximately XX% in the Self-Aware condition.

[Include visualization: box plot or violin plot with individual points]

#### Sensitivity Analyses
Results were robust to outlier removal (d = X.XX, 95% CI [X.XX, X.XX]) 
and alternative statistical tests (Mann-Whitney U = XXX, p = .XXX).

### Secondary Analyses
[Report each with same level of detail]

### Exploratory Analyses
[Clearly marked as exploratory, not confirmatory]
```

## Deviations from Plan

If you deviate from the pre-specified plan, document:

```markdown
### Deviations from Pre-registered Plan

1. **Deviation:** [What changed]
   - **Reason:** [Why it changed]
   - **Impact:** [How this affects interpretation]

2. **Additional Analysis:** [Any unplanned analyses]
   - **Reason:** [Why added]
   - **Status:** Exploratory (not confirmatory)
```

## Checklist

Before running analyses:
- [ ] Statistical analysis plan written
- [ ] Plan pre-registered (if applicable)
- [ ] Sample size justified with power analysis
- [ ] All tests pre-specified
- [ ] Multiple comparison corrections planned
- [ ] Assumptions and backup plans specified
- [ ] Effect size measures specified

After running analyses:
- [ ] All pre-specified analyses reported
- [ ] Assumptions checked and reported
- [ ] Effect sizes with CIs reported
- [ ] Negative results reported
- [ ] Deviations documented
- [ ] Exploratory analyses clearly marked
