# Research Validation Checklist

## Pre-Implementation Phase

### Construct Definition
- [ ] Construct has clear theoretical definition
- [ ] Construct relates to established literature
- [ ] Operational definition specified
- [ ] Boundary conditions identified
- [ ] Confounds and alternative explanations considered

### Measurement Design
- [ ] Measurement approach justified theoretically
- [ ] Alternative approaches considered and discussed
- [ ] Known limitations documented
- [ ] Assumptions explicitly stated
- [ ] Validation strategy planned BEFORE implementation

### Ground Truth Plan
- [ ] Independent ground truth source identified
- [ ] Annotation protocol developed
- [ ] Sample size justified with power analysis
- [ ] Inter-rater reliability threshold specified (≥0.7)
- [ ] Data collection timeline and resources allocated

### Statistical Analysis Plan
- [ ] Research questions/hypotheses pre-specified
- [ ] Statistical tests chosen with justification
- [ ] Multiple comparison corrections planned
- [ ] Effect size measures specified
- [ ] Significance threshold justified (typically α=0.05)
- [ ] Power analysis completed (typically power ≥0.8)

## Implementation Phase

### Ground Truth Collection
- [ ] Annotation guidelines finalized and tested
- [ ] Pilot annotation completed (n≥20)
- [ ] Inter-rater reliability calculated (κ≥0.7)
- [ ] Full annotation completed
- [ ] Quality control checks performed
- [ ] Dataset split (train/val/test) created
- [ ] Test set preserved (not examined until final eval)

### Measure Validation
- [ ] Measure validated on training set
- [ ] Hyperparameters tuned on validation set
- [ ] Final evaluation on held-out test set
- [ ] Validation metrics calculated:
  - [ ] Accuracy
  - [ ] Precision
  - [ ] Recall
  - [ ] F1 Score
  - [ ] Cohen's Kappa
  - [ ] Confusion Matrix
- [ ] Confidence intervals calculated
- [ ] Error analysis performed
- [ ] Failure cases documented

### Independence Verification
- [ ] Validation method independent of measurement
- [ ] No circular logic in validation
- [ ] Ground truth not derived from measure
- [ ] External validation sources used when possible

## Experimental Phase

### Experimental Design
- [ ] Control conditions specified
- [ ] Randomization procedure documented
- [ ] Blinding implemented where appropriate
- [ ] Confounds controlled or measured
- [ ] Sample size adequate (power analysis)

### Data Collection
- [ ] Data collection protocol documented
- [ ] All parameters and settings recorded
- [ ] Random seeds documented
- [ ] Preprocessing steps specified
- [ ] Data quality checks performed
- [ ] Outliers identified and handled appropriately

### Statistical Analysis
- [ ] Pre-specified analysis plan followed
- [ ] Assumptions checked:
  - [ ] Normality (if parametric tests)
  - [ ] Independence
  - [ ] Homogeneity of variance
  - [ ] No multicollinearity (if regression)
- [ ] Effect sizes calculated with confidence intervals
- [ ] Multiple comparison corrections applied
- [ ] All tests reported (not just significant ones)
- [ ] Exact p-values reported
- [ ] Statistical software and version documented

## Reporting Phase

### Methods Section
- [ ] Complete implementation details provided
- [ ] All hyperparameters specified
- [ ] Random seeds and initialization documented
- [ ] Data sources and versions specified
- [ ] Preprocessing steps fully described
- [ ] Hardware and runtime environment specified
- [ ] Exact prompts/instructions provided (if LLM)
- [ ] Ground truth collection protocol described
- [ ] Validation procedure explained
- [ ] Statistical analysis plan detailed

### Results Section
- [ ] All validation metrics reported
- [ ] Effect sizes with confidence intervals
- [ ] Complete statistical results (not just p-values)
- [ ] Negative results reported
- [ ] Unexpected findings discussed
- [ ] Figures and tables clearly labeled
- [ ] All data visualizations accurate

### Discussion Section
- [ ] Limitations acknowledged
- [ ] Boundary conditions discussed
- [ ] Alternative explanations considered
- [ ] Generalizability discussed
- [ ] Comparison to prior work
- [ ] Implications clearly stated
- [ ] Future work suggested

### Reproducibility
- [ ] Code publicly available (GitHub, etc.)
- [ ] Data publicly available (or access procedure described)
- [ ] Dependencies listed with versions
- [ ] README with setup instructions
- [ ] Example usage provided
- [ ] License specified
- [ ] Contact information for questions

## Domain-Specific Checklists

### For Bias Detection Research

#### Construct Validity
- [ ] Each bias type theoretically defined
- [ ] Bias types distinguishable from legitimate criticism
- [ ] Relationship to psychological literature established
- [ ] Operational definitions don't conflate language with bias

#### Ground Truth
- [ ] Expert annotators identify bias independently
- [ ] Annotations not based on pattern matching
- [ ] Inter-rater reliability ≥0.7 for each bias type
- [ ] Validation includes diverse review types

#### Measurement
- [ ] Detection method validated against expert annotations
- [ ] Precision/recall/F1 reported for each bias type
- [ ] False positive analysis performed
- [ ] Comparison to baseline methods

#### Experiments
- [ ] Reviews from diverse sources (not just landmark papers)
- [ ] Control for confounds (paper quality, domain, etc.)
- [ ] Real-time vs. post-hoc correction distinguished
- [ ] Actual impact on review quality measured

### For LLM Evaluation Research

#### Construct Validity
- [ ] Evaluation criteria theoretically grounded
- [ ] Criteria distinguishable from superficial features
- [ ] Relationship to human judgment established

#### Ground Truth
- [ ] Human expert evaluations collected
- [ ] Evaluation rubric validated
- [ ] Inter-rater reliability ≥0.7
- [ ] Diverse examples covering edge cases

#### Measurement
- [ ] Automated metrics validated against human judgment
- [ ] Correlation with human ratings reported
- [ ] Failure modes identified and documented

#### Experiments
- [ ] Multiple models compared
- [ ] Diverse tasks and domains
- [ ] Prompt sensitivity analyzed
- [ ] Temperature and sampling effects controlled

### For Self-Correction Research

#### Construct Validity
- [ ] "Self-correction" clearly defined
- [ ] Distinguished from simple refinement
- [ ] Mechanism of correction specified

#### Ground Truth
- [ ] Errors independently identified
- [ ] Corrections independently verified
- [ ] Success criteria pre-specified

#### Measurement
- [ ] Correction accuracy measured
- [ ] False corrections identified
- [ ] Net improvement quantified

#### Experiments
- [ ] Baseline without correction
- [ ] Control for additional compute
- [ ] Real-time vs. post-hoc distinguished
- [ ] Failure cases analyzed

## Red Flags Checklist

**STOP if you encounter any of these:**

### Circular Logic
- [ ] Using method X to validate method X
- [ ] Using model outputs to validate model
- [ ] Using assumptions to validate assumptions
- [ ] Pattern matching validating pattern matching

### Missing Ground Truth
- [ ] No independent validation source
- [ ] "We assume X indicates Y" without validation
- [ ] Self-reported metrics only
- [ ] No comparison to external standard

### Statistical Issues
- [ ] P-values without effect sizes
- [ ] No confidence intervals
- [ ] Underpowered studies (n too small)
- [ ] Multiple comparisons without correction
- [ ] Selective reporting of results
- [ ] Post-hoc hypotheses presented as a priori

### Reproducibility Issues
- [ ] Code "available upon request" (not actually available)
- [ ] Missing hyperparameters
- [ ] Unspecified random seeds
- [ ] Vague descriptions ("standard settings")
- [ ] Proprietary data with no access
- [ ] Missing dependencies or versions

### Validity Issues
- [ ] Construct poorly defined
- [ ] Confounds not controlled
- [ ] Generalizability not addressed
- [ ] Limitations not acknowledged
- [ ] Alternative explanations not considered

## Final Verification

Before submitting/publishing:

- [ ] All checklists completed
- [ ] No red flags present
- [ ] Independent reviewer verified methodology
- [ ] Code and data available
- [ ] Reproducibility verified by independent party
- [ ] All claims supported by evidence
- [ ] Limitations honestly discussed

## Severity Assessment

### Critical Issues (Must Fix)
- Circular logic in validation
- No ground truth
- Unvalidated measures used in experiments
- Statistical assumptions violated
- Non-reproducible

### Major Issues (Should Fix)
- Weak ground truth (low agreement)
- Limited validation
- Missing effect sizes
- Incomplete reproducibility details
- Confounds not addressed

### Minor Issues (Nice to Fix)
- Additional validation would strengthen
- More diverse examples needed
- Additional baselines would help
- More detailed documentation

**Do not proceed with critical or major issues unresolved.**

## Usage

1. **Before starting:** Complete Pre-Implementation checklist
2. **During development:** Complete Implementation checklist
3. **During experiments:** Complete Experimental checklist
4. **Before writing:** Complete Reporting checklist
5. **Before submission:** Complete Final Verification
6. **Continuous:** Check Red Flags checklist

**Save completed checklists with your project for documentation.**
