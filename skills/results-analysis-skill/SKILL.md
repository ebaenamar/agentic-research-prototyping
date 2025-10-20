---
name: results-analysis-skill
description: Rigorous statistical analysis and honest interpretation of experimental results. Ensures proper statistical tests, effect sizes, confidence intervals, and honest reporting of all findings including negative results. Prevents p-hacking, HARKing, and overclaiming.
---

# Results Analysis & Interpretation

Rigorous approach to analyzing and interpreting experimental results.

## Core Principles

1. **Follow Pre-specified Plan**: Stick to statistical analysis plan
2. **Report Everything**: All results, not just significant ones
3. **Effect Sizes Matter**: P-values alone are insufficient
4. **Honest Interpretation**: Don't overclaim or cherry-pick
5. **Acknowledge Limitations**: Be transparent about boundaries

## Analysis Workflow

### Step 1: Load Pre-specified Analysis Plan

**Before looking at results:**

```python
# Load the pre-specified statistical analysis plan
with open('statistical_analysis_plan.md', 'r') as f:
    analysis_plan = f.read()

print("Following pre-specified analysis plan:")
print(analysis_plan)

# This prevents p-hacking and HARKing
```

### Step 2: Check Assumptions

**For each statistical test, verify assumptions:**

```python
def check_assumptions(data, test_type='t-test'):
    """
    Check statistical assumptions before running tests
    """
    results = {}
    
    if test_type == 't-test':
        # Check normality
        from scipy.stats import shapiro
        stat, p = shapiro(data)
        results['normality'] = {
            'test': 'Shapiro-Wilk',
            'statistic': stat,
            'p_value': p,
            'assumption_met': p > 0.05
        }
        
        # Check homogeneity of variance
        from scipy.stats import levene
        # ... (for two groups)
        
    # Log results
    logger.info(f"Assumption checks for {test_type}:")
    for assumption, result in results.items():
        logger.info(f"  {assumption}: {result}")
        if not result['assumption_met']:
            logger.warning(f"  ⚠️  Assumption violated: {assumption}")
    
    return results
```

**If assumptions violated:**

```python
def handle_violated_assumptions(assumption_results, backup_plan):
    """
    Use pre-specified backup tests when assumptions violated
    """
    if not assumption_results['normality']['assumption_met']:
        logger.info("Normality violated, using non-parametric test")
        return backup_plan['non_parametric_test']
    
    if not assumption_results['homogeneity']['assumption_met']:
        logger.info("Homogeneity violated, using Welch's test")
        return backup_plan['welch_test']
    
    return backup_plan['primary_test']
```

### Step 3: Primary Analysis

**Run pre-specified primary analysis:**

```python
def run_primary_analysis(data, analysis_plan):
    """
    Run primary analysis exactly as pre-specified
    """
    results = {}
    
    # Extract conditions
    condition_a = data[data['condition'] == 'baseline']['outcome']
    condition_b = data[data['condition'] == 'intervention']['outcome']
    
    # Check assumptions
    assumptions = check_assumptions([condition_a, condition_b])
    
    # Run appropriate test
    if assumptions['normality']['assumption_met']:
        from scipy.stats import ttest_ind
        stat, p_value = ttest_ind(condition_a, condition_b)
        test_used = 'Independent t-test'
    else:
        from scipy.stats import mannwhitneyu
        stat, p_value = mannwhitneyu(condition_a, condition_b)
        test_used = 'Mann-Whitney U test'
    
    # Calculate effect size
    effect_size = calculate_cohens_d(condition_a, condition_b)
    ci = calculate_confidence_interval(effect_size, len(condition_a), len(condition_b))
    
    results = {
        'test': test_used,
        'statistic': stat,
        'p_value': p_value,
        'effect_size': effect_size,
        'ci_lower': ci[0],
        'ci_upper': ci[1],
        'n_a': len(condition_a),
        'n_b': len(condition_b),
        'mean_a': np.mean(condition_a),
        'std_a': np.std(condition_a),
        'mean_b': np.mean(condition_b),
        'std_b': np.std(condition_b)
    }
    
    return results

def calculate_cohens_d(group1, group2):
    """Calculate Cohen's d effect size"""
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    return (np.mean(group1) - np.mean(group2)) / pooled_std

def calculate_confidence_interval(d, n1, n2, confidence=0.95):
    """Calculate CI for Cohen's d"""
    from scipy.stats import t
    se = np.sqrt((n1 + n2) / (n1 * n2) + d**2 / (2 * (n1 + n2)))
    df = n1 + n2 - 2
    t_crit = t.ppf((1 + confidence) / 2, df)
    margin = t_crit * se
    return (d - margin, d + margin)
```

### Step 4: Secondary Analyses

**Run all pre-specified secondary analyses:**

```python
def run_secondary_analyses(data, analysis_plan):
    """
    Run all pre-specified secondary analyses
    """
    results = {}
    
    for analysis_name, analysis_spec in analysis_plan['secondary'].items():
        logger.info(f"Running secondary analysis: {analysis_name}")
        
        result = run_analysis(data, analysis_spec)
        results[analysis_name] = result
    
    return results
```

### Step 5: Multiple Comparison Correction

**Apply pre-specified corrections:**

```python
def apply_multiple_comparison_correction(p_values, method='holm'):
    """
    Apply multiple comparison correction
    """
    from statsmodels.stats.multitest import multipletests
    
    # Apply correction
    reject, p_corrected, _, _ = multipletests(
        p_values,
        alpha=0.05,
        method=method
    )
    
    results = {
        'method': method,
        'original_p_values': p_values,
        'corrected_p_values': p_corrected,
        'reject_null': reject,
        'num_significant_original': sum(p < 0.05 for p in p_values),
        'num_significant_corrected': sum(reject)
    }
    
    logger.info(f"Multiple comparison correction ({method}):")
    logger.info(f"  Original significant: {results['num_significant_original']}")
    logger.info(f"  After correction: {results['num_significant_corrected']}")
    
    return results
```

### Step 6: Effect Size Interpretation

**Interpret effect sizes honestly:**

```python
def interpret_effect_size(d):
    """
    Interpret Cohen's d effect size
    Based on Cohen (1988) guidelines
    """
    abs_d = abs(d)
    
    if abs_d < 0.2:
        magnitude = "negligible"
    elif abs_d < 0.5:
        magnitude = "small"
    elif abs_d < 0.8:
        magnitude = "medium"
    else:
        magnitude = "large"
    
    return {
        'magnitude': magnitude,
        'interpretation': f"Cohen's d = {d:.3f} represents a {magnitude} effect size",
        'practical_significance': assess_practical_significance(d)
    }

def assess_practical_significance(d):
    """
    Assess practical significance beyond statistical significance
    """
    # This depends on domain and context
    # Example for bias reduction:
    if abs(d) < 0.3:
        return "Statistically detectable but may not be practically meaningful"
    elif abs(d) < 0.6:
        return "Moderate practical significance"
    else:
        return "Strong practical significance"
```

### Step 7: Sensitivity Analysis

**Test robustness of findings:**

```python
def sensitivity_analysis(data, primary_result):
    """
    Test robustness of findings to different assumptions
    """
    sensitivity_results = {}
    
    # 1. Outlier sensitivity
    data_no_outliers = remove_outliers(data, method='iqr')
    result_no_outliers = run_primary_analysis(data_no_outliers, analysis_plan)
    sensitivity_results['without_outliers'] = result_no_outliers
    
    # 2. Different exclusion criteria
    data_liberal = apply_exclusion(data, criteria='liberal')
    result_liberal = run_primary_analysis(data_liberal, analysis_plan)
    sensitivity_results['liberal_exclusion'] = result_liberal
    
    # 3. Different statistical test
    result_nonparametric = run_nonparametric_test(data)
    sensitivity_results['nonparametric'] = result_nonparametric
    
    # Compare results
    comparison = compare_sensitivity_results(primary_result, sensitivity_results)
    
    return sensitivity_results, comparison

def compare_sensitivity_results(primary, sensitivity):
    """
    Compare primary result to sensitivity analyses
    """
    comparisons = []
    
    for name, result in sensitivity.items():
        # Check if conclusion changes
        primary_sig = primary['p_value'] < 0.05
        sens_sig = result['p_value'] < 0.05
        
        # Check if effect size similar
        effect_diff = abs(primary['effect_size'] - result['effect_size'])
        
        comparisons.append({
            'analysis': name,
            'conclusion_same': primary_sig == sens_sig,
            'effect_size_diff': effect_diff,
            'robust': effect_diff < 0.2  # Within small effect size
        })
    
    overall_robust = all(c['robust'] for c in comparisons)
    
    return {
        'comparisons': comparisons,
        'overall_robust': overall_robust
    }
```

### Step 8: Exploratory Analyses

**Clearly mark exploratory analyses:**

```python
def run_exploratory_analysis(data, analysis_description):
    """
    Run exploratory analysis - clearly marked as NOT confirmatory
    """
    logger.warning("⚠️  EXPLORATORY ANALYSIS (not pre-specified)")
    logger.info(f"Analysis: {analysis_description}")
    
    # Run analysis
    result = perform_analysis(data)
    
    # Mark as exploratory
    result['exploratory'] = True
    result['description'] = analysis_description
    result['note'] = "This analysis was not pre-specified and should be considered exploratory only"
    
    return result
```

## Interpretation

### 1. Honest Interpretation Framework

**For each finding, answer:**

```markdown
## Finding: [Brief description]

### Statistical Result
- Test: [test used]
- Statistic: [value]
- P-value: [exact value, not just < 0.05]
- Effect size: [Cohen's d or other] = [value]
- 95% CI: [[lower, upper]]
- Sample size: n = [N]

### Interpretation

**Statistical Significance:**
[Is p < 0.05? But don't stop there...]

**Effect Size:**
[What is the magnitude? Small/medium/large?]
[What does this mean in practical terms?]

**Practical Significance:**
[Does this effect size matter in practice?]
[Is it large enough to be meaningful?]

**Confidence Interval:**
[What is the range of plausible effect sizes?]
[Does the CI include practically insignificant values?]

**Robustness:**
[Is finding robust to sensitivity analyses?]
[Does it hold under different assumptions?]

### Alternative Explanations

**Could this be due to:**
1. [Alternative explanation 1]
   - Evidence for/against: [...]
2. [Alternative explanation 2]
   - Evidence for/against: [...]

### Limitations

**This finding is limited by:**
1. [Limitation 1]
2. [Limitation 2]

**Boundary conditions:**
- [When does this apply?]
- [When might it not apply?]

### Honest Conclusion

[What can we confidently conclude?]
[What remains uncertain?]
[What should future work address?]
```

### 2. Avoid Overclaiming

**RED FLAGS - Don't say:**

❌ "This proves that..."
✅ "This provides evidence that..."

❌ "X causes Y"
✅ "X is associated with Y" (unless true experiment)

❌ "Our method is better"
✅ "Our method showed better performance on [specific metrics] in [specific context]"

❌ "This will revolutionize..."
✅ "This suggests potential for..."

❌ "Significant improvement" (p < 0.05 only)
✅ "Statistically significant improvement (p = .03, d = 0.45, 95% CI [0.15, 0.75])"

### 3. Report Negative Results

**If results don't support hypothesis:**

```markdown
## Negative Result: [Hypothesis not supported]

### What we found
[Describe actual results honestly]

### Why this matters
[Negative results are informative!]
- Rules out this explanation
- Suggests alternative mechanisms
- Informs future research

### Possible reasons
1. [Hypothesis was wrong]
2. [Effect too small to detect]
3. [Methodological limitations]
4. [Boundary conditions not met]

### What we learned
[What does this tell us?]
[How does this advance knowledge?]
```

## Reporting

### 1. Results Section Template

```markdown
## Results

### Assumption Checks

We checked assumptions for all statistical tests as pre-specified.

**Normality:** Shapiro-Wilk tests indicated [normal/non-normal] 
distributions for [conditions] (W = [value], p = [value]).

**Homogeneity of variance:** Levene's test indicated [equal/unequal] 
variances (F = [value], p = [value]).

[If violated:] Given violation of [assumption], we used [backup test] 
as pre-specified in our analysis plan.

### Primary Analysis

[Hypothesis being tested]

**Descriptive Statistics:**
- Baseline: M = [value], SD = [value], n = [N]
- Intervention: M = [value], SD = [value], n = [N]

**Inferential Statistics:**
We conducted [test name] comparing [conditions]. [Condition A] showed 
[higher/lower] scores (M = [value], SD = [value]) compared to 
[Condition B] (M = [value], SD = [value]), [test statistic] = [value], 
p = [exact value], Cohen's d = [value], 95% CI [[lower, upper]].

**Effect Size Interpretation:**
This represents a [small/medium/large] effect size. [Practical interpretation]

**Sensitivity Analysis:**
Results were robust to [list sensitivity checks]. [Details]

[Include visualization: box plot, violin plot, or effect size plot]

### Secondary Analyses

[Repeat structure for each secondary analysis]

### Multiple Comparison Correction

We applied [method] correction across [N] hypothesis tests. After 
correction, [N] tests remained significant at α = .05.

### Exploratory Analyses

[Clearly marked as exploratory]
[Results with appropriate caveats]
```

### 2. Visualization Requirements

**Every result should have:**

1. **Effect Size Plot**
```python
import matplotlib.pyplot as plt
import seaborn as sns

def plot_effect_sizes(results):
    """
    Plot effect sizes with confidence intervals
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Extract data
    names = list(results.keys())
    effects = [r['effect_size'] for r in results.values()]
    cis = [(r['ci_lower'], r['ci_upper']) for r in results.values()]
    
    # Plot
    y_pos = np.arange(len(names))
    ax.errorbar(effects, y_pos, 
                xerr=[[e - ci[0] for e, ci in zip(effects, cis)],
                      [ci[1] - e for e, ci in zip(effects, cis)]],
                fmt='o', capsize=5)
    
    # Reference lines
    ax.axvline(0, color='black', linestyle='--', alpha=0.3)
    ax.axvline(0.2, color='gray', linestyle=':', alpha=0.3, label='Small')
    ax.axvline(0.5, color='gray', linestyle=':', alpha=0.3, label='Medium')
    ax.axvline(0.8, color='gray', linestyle=':', alpha=0.3, label='Large')
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names)
    ax.set_xlabel("Cohen's d (95% CI)")
    ax.set_title("Effect Sizes with Confidence Intervals")
    ax.legend()
    
    plt.tight_layout()
    return fig
```

2. **Distribution Plots**
```python
def plot_distributions(data):
    """
    Plot distributions for each condition
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Violin plot
    sns.violinplot(data=data, x='condition', y='outcome', ax=axes[0])
    sns.swarmplot(data=data, x='condition', y='outcome', 
                  color='black', alpha=0.3, ax=axes[0])
    axes[0].set_title('Distribution by Condition')
    
    # Histogram
    for condition in data['condition'].unique():
        subset = data[data['condition'] == condition]
        axes[1].hist(subset['outcome'], alpha=0.5, label=condition)
    axes[1].set_xlabel('Outcome')
    axes[1].set_ylabel('Frequency')
    axes[1].set_title('Outcome Distributions')
    axes[1].legend()
    
    plt.tight_layout()
    return fig
```

### 3. Tables

**Complete Statistical Results Table:**

```python
def create_results_table(results):
    """
    Create comprehensive results table
    """
    import pandas as pd
    
    table_data = []
    for name, result in results.items():
        table_data.append({
            'Analysis': name,
            'N': f"{result['n_a']}, {result['n_b']}",
            'M (SD)': f"{result['mean_a']:.2f} ({result['std_a']:.2f}), "
                     f"{result['mean_b']:.2f} ({result['std_b']:.2f})",
            'Test': result['test'],
            'Statistic': f"{result['statistic']:.3f}",
            'p': f"{result['p_value']:.4f}",
            "Cohen's d": f"{result['effect_size']:.3f}",
            '95% CI': f"[{result['ci_lower']:.3f}, {result['ci_upper']:.3f}]"
        })
    
    df = pd.DataFrame(table_data)
    return df
```

## Quality Checks

**Before finalizing results:**

- [ ] All pre-specified analyses completed
- [ ] Assumptions checked and reported
- [ ] Effect sizes calculated with CIs
- [ ] Multiple comparisons corrected
- [ ] Sensitivity analyses performed
- [ ] Negative results reported
- [ ] Exploratory analyses clearly marked
- [ ] Visualizations created
- [ ] Alternative explanations considered
- [ ] Limitations acknowledged
- [ ] No overclaiming in interpretation

## Common Pitfalls to Avoid

### 1. P-hacking
❌ Testing multiple ways until something is significant
✅ Follow pre-specified analysis plan

### 2. HARKing
❌ Hypothesizing After Results are Known
✅ Clearly mark exploratory analyses

### 3. Cherry-picking
❌ Reporting only favorable results
✅ Report all pre-specified analyses

### 4. Overclaiming
❌ "Proves", "demonstrates conclusively"
✅ "Provides evidence", "suggests"

### 5. Ignoring Effect Sizes
❌ "Significant (p < .05)"
✅ "Significant with medium effect (p = .03, d = 0.52)"

## Next Phase

Once analysis is complete and honest:
→ Proceed to **Research Review** (research-review-skill)

Bring forward:
- Complete statistical results
- All visualizations
- Honest interpretation
- Limitations analysis
- Alternative explanations considered
