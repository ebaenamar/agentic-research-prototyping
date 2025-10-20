---
name: research-review-skill
description: Multi-stage review process to validate research quality before publication. Implements review loops for methodology, results, interpretation, and contribution. Ensures work is rigorous, reproducible, and makes genuine contributions. Use before finalizing any research for publication.
---

# Research Review & Validation

Comprehensive review process with multiple validation loops.

## Review Philosophy

**Goal:** Ensure research is:
1. **Methodologically sound**: No circular logic, proper validation
2. **Statistically rigorous**: Proper tests, effect sizes, honest reporting
3. **Reproducible**: Complete details, available code/data
4. **Honest**: Limitations acknowledged, no overclaiming
5. **Significant**: Genuine contribution to field

## Review Stages

### Stage 1: Methodology Review

**Review Question:** Is the methodology sound?

#### Checklist

**Construct Validity**
- [ ] All constructs clearly defined (theoretical + operational)
- [ ] Constructs validated against independent ground truth
- [ ] Validation metrics reported (precision, recall, F1, κ)
- [ ] Validation meets thresholds (F1 ≥ 0.7, κ ≥ 0.7)
- [ ] No circular logic in validation
- [ ] Limitations of measures acknowledged

**Experimental Design**
- [ ] Research questions clearly stated
- [ ] Hypotheses pre-specified
- [ ] Control conditions appropriate
- [ ] Confounds controlled or measured
- [ ] Sample size justified (power analysis)
- [ ] Randomization implemented
- [ ] Blinding where appropriate

**Statistical Plan**
- [ ] Analysis plan pre-specified
- [ ] Statistical tests appropriate
- [ ] Assumptions to be checked
- [ ] Multiple comparison corrections planned
- [ ] Effect size measures specified
- [ ] Significance thresholds justified

**Reproducibility**
- [ ] All parameters documented
- [ ] Random seeds specified
- [ ] Code structure clear
- [ ] Data format defined
- [ ] Dependencies listed

#### Red Flags

**STOP if you find:**
- Circular validation (method validates itself)
- Unvalidated measures used in experiments
- No ground truth for validation
- Statistical plan missing or vague
- Reproducibility details incomplete

#### Review Output

```markdown
## Methodology Review

**Date:** [date]
**Reviewer:** [name/role]

### Strengths
1. [Strength 1]
2. [Strength 2]

### Issues Found

#### Critical Issues (Must Fix)
1. [Issue]: [Description]
   - **Impact:** [How this affects validity]
   - **Fix:** [How to address]

#### Major Issues (Should Fix)
1. [Issue]: [Description]
   - **Impact:** [How this affects quality]
   - **Fix:** [How to address]

#### Minor Issues (Nice to Fix)
1. [Issue]: [Description]
   - **Fix:** [How to address]

### Recommendations
1. [Recommendation 1]
2. [Recommendation 2]

### Decision
- [ ] Approved - proceed to implementation
- [ ] Revisions needed - address issues and re-review
- [ ] Major redesign needed - fundamental issues

### Next Steps
[What needs to happen before next review]
```

### Stage 2: Implementation Review

**Review Question:** Is the implementation correct and reproducible?

#### Checklist

**Code Quality**
- [ ] Code follows methodology design
- [ ] All parameters match specification
- [ ] Random seeds set correctly
- [ ] Logging comprehensive
- [ ] Error handling appropriate
- [ ] Comments explain non-obvious code

**Reproducibility**
- [ ] Configuration file complete
- [ ] All dependencies listed with versions
- [ ] Environment setup documented
- [ ] README with clear instructions
- [ ] Example usage provided

**Data Management**
- [ ] Data storage organized
- [ ] Data format standardized
- [ ] Metadata complete
- [ ] Backup strategy in place

**Quality Control**
- [ ] Pilot run completed successfully
- [ ] Quality checks implemented
- [ ] Monitoring in place
- [ ] Verification procedures defined

#### Code Review Process

```python
def review_implementation(code_path):
    """
    Automated checks for implementation quality
    """
    issues = []
    
    # Check for random seeds
    if not has_random_seed(code_path):
        issues.append({
            'severity': 'major',
            'issue': 'No random seed set',
            'fix': 'Add random seed for reproducibility'
        })
    
    # Check for hardcoded values
    hardcoded = find_hardcoded_values(code_path)
    if hardcoded:
        issues.append({
            'severity': 'minor',
            'issue': f'Hardcoded values: {hardcoded}',
            'fix': 'Move to configuration file'
        })
    
    # Check for logging
    if not has_logging(code_path):
        issues.append({
            'severity': 'major',
            'issue': 'No logging implemented',
            'fix': 'Add comprehensive logging'
        })
    
    return issues
```

#### Review Output

```markdown
## Implementation Review

**Date:** [date]
**Reviewer:** [name/role]

### Code Quality: [Excellent/Good/Needs Work]

### Reproducibility: [High/Medium/Low]

### Issues Found
[List issues with severity and fixes]

### Verification
- [ ] Code runs without errors
- [ ] Produces expected output format
- [ ] Logging captures necessary information
- [ ] Configuration matches methodology

### Decision
- [ ] Approved - proceed to experiments
- [ ] Minor fixes needed
- [ ] Major revisions needed

### Next Steps
[What needs to happen before experiments]
```

### Stage 3: Results Review

**Review Question:** Are the results valid and honestly reported?

#### Checklist

**Statistical Validity**
- [ ] Pre-specified analysis plan followed
- [ ] Assumptions checked and reported
- [ ] Appropriate tests used
- [ ] Effect sizes calculated with CIs
- [ ] Multiple comparisons corrected
- [ ] All analyses reported (not just significant)

**Data Quality**
- [ ] Data verified and cleaned
- [ ] Cleaning documented
- [ ] No systematic errors
- [ ] Balance across conditions
- [ ] Outliers handled appropriately

**Interpretation**
- [ ] Interpretation matches results
- [ ] No overclaiming
- [ ] Alternative explanations considered
- [ ] Limitations acknowledged
- [ ] Practical significance assessed

**Reporting**
- [ ] Complete statistics reported
- [ ] Visualizations clear and accurate
- [ ] Tables properly formatted
- [ ] Negative results included
- [ ] Exploratory analyses marked

#### Statistical Review

```python
def review_statistics(results):
    """
    Check statistical reporting quality
    """
    issues = []
    
    for analysis in results:
        # Check for p-value without effect size
        if 'p_value' in analysis and 'effect_size' not in analysis:
            issues.append({
                'severity': 'major',
                'analysis': analysis['name'],
                'issue': 'P-value reported without effect size',
                'fix': 'Calculate and report effect size with CI'
            })
        
        # Check for "significant" without details
        if analysis.get('significant') and not analysis.get('complete_stats'):
            issues.append({
                'severity': 'major',
                'analysis': analysis['name'],
                'issue': 'Significance claimed without complete statistics',
                'fix': 'Report test statistic, p-value, effect size, CI'
            })
        
        # Check for overclaiming
        interpretation = analysis.get('interpretation', '')
        if any(word in interpretation.lower() for word in ['proves', 'demonstrates conclusively']):
            issues.append({
                'severity': 'minor',
                'analysis': analysis['name'],
                'issue': 'Overclaiming in interpretation',
                'fix': 'Use more cautious language (e.g., "suggests", "provides evidence")'
            })
    
    return issues
```

#### Review Output

```markdown
## Results Review

**Date:** [date]
**Reviewer:** [name/role]

### Statistical Rigor: [Excellent/Good/Needs Work]

### Interpretation Quality: [Excellent/Good/Needs Work]

### Issues Found

#### Statistical Issues
1. [Issue]: [Description and fix]

#### Interpretation Issues
1. [Issue]: [Description and fix]

#### Reporting Issues
1. [Issue]: [Description and fix]

### Strengths
1. [What was done well]

### Recommendations
1. [Recommendation for improvement]

### Decision
- [ ] Approved - results are sound
- [ ] Minor revisions needed
- [ ] Major revisions needed
- [ ] Additional analyses needed

### Next Steps
[What needs to happen before finalization]
```

### Stage 4: Contribution Review

**Review Question:** Does this make a genuine contribution?

#### Checklist

**Novelty**
- [ ] Genuinely different from existing work
- [ ] Not just incremental
- [ ] Addresses identified gap
- [ ] Offers new insights

**Significance**
- [ ] Matters to the field
- [ ] Advances knowledge
- [ ] Has practical implications
- [ ] Generates future research directions

**Quality**
- [ ] Methodologically sound
- [ ] Statistically rigorous
- [ ] Reproducible
- [ ] Honestly reported

**Clarity**
- [ ] Contribution clearly stated
- [ ] Relationship to prior work clear
- [ ] Limitations acknowledged
- [ ] Implications discussed

#### Contribution Assessment

```markdown
## Contribution Assessment

### What is the contribution?
[Clear statement of contribution]

### How is it novel?
**Compared to [Related Work 1]:**
- [How it differs]
- [What's new]

**Compared to [Related Work 2]:**
- [How it differs]
- [What's new]

### Why does it matter?

**To the field:**
- [Impact on research]
- [Advances in understanding]

**To practice:**
- [Practical applications]
- [Real-world impact]

### What are the limitations?
1. [Limitation 1]: [Impact on contribution]
2. [Limitation 2]: [Impact on contribution]

### What are the boundary conditions?
- [When does this apply?]
- [When might it not apply?]

### Assessment
**Novelty:** [High/Medium/Low]
**Significance:** [High/Medium/Low]
**Quality:** [High/Medium/Low]

**Overall Contribution:** [Strong/Adequate/Weak]
```

#### Review Output

```markdown
## Contribution Review

**Date:** [date]
**Reviewer:** [name/role]

### Contribution Statement
[Clear statement of what this work contributes]

### Novelty Assessment: [High/Medium/Low]
[Justification]

### Significance Assessment: [High/Medium/Low]
[Justification]

### Quality Assessment: [High/Medium/Low]
[Justification]

### Comparison to Related Work
[How this compares to key related work]

### Limitations and Boundary Conditions
[What limits the contribution]

### Decision
- [ ] Strong contribution - ready for publication
- [ ] Adequate contribution - minor improvements
- [ ] Weak contribution - major revisions or reconsider

### Recommendations
[How to strengthen contribution]
```

### Stage 5: Reproducibility Review

**Review Question:** Can someone else reproduce this work?

#### Checklist

**Documentation**
- [ ] Complete methods section
- [ ] All parameters specified
- [ ] All settings documented
- [ ] Exact prompts provided (if LLMs)
- [ ] Hardware/environment specified

**Code**
- [ ] Code publicly available
- [ ] README with setup instructions
- [ ] Dependencies listed with versions
- [ ] Example usage provided
- [ ] License specified

**Data**
- [ ] Data publicly available OR
- [ ] Data access procedure clearly described
- [ ] Data format documented
- [ ] Preprocessing steps specified

**Verification**
- [ ] Independent person can set up environment
- [ ] Independent person can run code
- [ ] Independent person gets same results
- [ ] All claims can be verified

#### Reproducibility Test

```markdown
## Reproducibility Test

**Tester:** [Independent person, not author]
**Date:** [date]

### Setup
- [ ] Environment setup successful
- [ ] Dependencies installed without issues
- [ ] Data accessible
- [ ] Code runs without errors

**Time to setup:** [hours]
**Issues encountered:** [list]

### Execution
- [ ] Main experiments run successfully
- [ ] Results match reported values
- [ ] Figures can be regenerated
- [ ] Tables can be regenerated

**Time to run:** [hours]
**Issues encountered:** [list]

### Verification
- [ ] Key findings reproduced
- [ ] Effect sizes within reported CIs
- [ ] Statistical tests give same results

**Discrepancies:** [list any differences]

### Overall Reproducibility: [High/Medium/Low]

### Recommendations
[How to improve reproducibility]
```

#### Review Output

```markdown
## Reproducibility Review

**Date:** [date]
**Reviewer:** [name/role]

### Documentation Quality: [Excellent/Good/Needs Work]

### Code Availability: [Excellent/Good/Needs Work]

### Data Availability: [Excellent/Good/Needs Work]

### Reproducibility Test Results
[Summary of independent reproduction attempt]

### Issues Found
1. [Issue]: [Impact and fix]

### Decision
- [ ] Fully reproducible - ready for publication
- [ ] Minor documentation improvements needed
- [ ] Major reproducibility issues - must fix

### Next Steps
[What needs to happen to ensure reproducibility]
```

## Review Loops

### When to Iterate

**Trigger new review loop if:**
- Critical issues found in any stage
- Major methodology changes
- Significant new results
- Contribution substantially changes

### Iteration Process

```markdown
## Review Iteration [N]

**Date:** [date]
**Trigger:** [What prompted re-review]

### Changes Since Last Review
1. [Change 1]: [Description]
2. [Change 2]: [Description]

### Re-review Focus
[Which stages need re-review]

### New Issues Found
[Any new issues]

### Resolution of Previous Issues
- [Issue 1]: [How resolved]
- [Issue 2]: [How resolved]

### Decision
- [ ] Issues resolved - proceed
- [ ] Additional iteration needed
- [ ] Fundamental redesign required
```

## Final Approval

### Pre-Publication Checklist

**Before submitting/publishing:**

- [ ] All review stages completed
- [ ] All critical issues resolved
- [ ] All major issues addressed
- [ ] Methodology validated
- [ ] Implementation verified
- [ ] Results reviewed and sound
- [ ] Contribution clear and significant
- [ ] Reproducibility confirmed
- [ ] Independent verification completed
- [ ] All documentation complete
- [ ] Code and data available
- [ ] Limitations honestly discussed
- [ ] No overclaiming in claims

### Final Sign-Off

```markdown
## Final Research Approval

**Date:** [date]
**Approvers:** [List all reviewers]

### Summary
This work has completed all review stages and is ready for publication.

### Strengths
1. [Key strength 1]
2. [Key strength 2]
3. [Key strength 3]

### Remaining Limitations
[Honest assessment of what limitations remain]

### Contribution
[Clear statement of contribution]

### Recommendation
**Approved for publication**

Target venues: [List appropriate venues]

### Signatures
[All reviewers sign off]
```

## Review Tools

### Automated Checks

```python
def run_automated_review(project_path):
    """
    Run automated checks across all review dimensions
    """
    from scripts.methodology_auditor import MethodologyAuditor
    from scripts.reproducibility_checker import ReproducibilityChecker
    from scripts.statistical_validator import StatisticalValidator
    
    results = {
        'methodology': MethodologyAuditor().audit(project_path),
        'reproducibility': ReproducibilityChecker().check(project_path),
        'statistics': StatisticalValidator().validate(project_path)
    }
    
    # Generate report
    report = generate_review_report(results)
    
    return report
```

### Review Templates

See additional files:
- `methodology_review_template.md`
- `implementation_review_template.md`
- `results_review_template.md`
- `contribution_review_template.md`
- `reproducibility_review_template.md`

## Best Practices

### 1. Multiple Reviewers

- Have at least 2 independent reviewers
- Include someone not involved in the project
- Get domain expert feedback

### 2. Honest Feedback

- Focus on improving the work
- Be specific about issues
- Provide actionable recommendations
- Acknowledge strengths

### 3. Iterative Process

- Don't expect perfection first time
- Each iteration improves quality
- Document all changes
- Track resolution of issues

### 4. Independent Verification

- Have someone else reproduce results
- Fresh eyes catch issues
- Validates reproducibility claims

## Output

### Review Documentation

Maintain complete review history:
```
reviews/
├── methodology_review_v1.md
├── methodology_review_v2.md
├── implementation_review_v1.md
├── results_review_v1.md
├── contribution_review_v1.md
├── reproducibility_review_v1.md
└── final_approval.md
```

### Improvement Log

Track all improvements:
```markdown
## Improvement Log

### Issue: [Description]
- **Found in:** [Review stage]
- **Severity:** [Critical/Major/Minor]
- **Fix applied:** [What was done]
- **Verified:** [Date and by whom]

[Repeat for all issues]
```

## Success Criteria

**Work is ready for publication when:**
- All review stages passed
- All critical issues resolved
- Independent reproduction successful
- Contribution validated
- No overclaiming
- Limitations honestly discussed
- Complete documentation
- Code and data available

**Do not publish if:**
- Critical issues remain
- Reproducibility not verified
- Contribution unclear or weak
- Overclaiming present
- Documentation incomplete
