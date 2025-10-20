---
name: research-methodology-validator
description: Enforces rigorous research methodology standards to prevent circular logic, unvalidated measures, and non-reproducible experiments. Use when designing experiments, validating measurements, or reviewing research claims. Ensures construct validity, ground truth establishment, statistical rigor, and reproducibility before any implementation.
---

# Research Methodology Validator

This skill enforces strict methodological standards to prevent common research pitfalls including circular logic, unvalidated measures, and non-reproducible experiments.

## Core Principles

### 1. No Circular Logic
**NEVER** use the same method to both generate and validate results.

**Examples of Circular Logic to AVOID:**
- Using pattern matching to detect bias, then claiming the patterns validate the detection
- Using an LLM to generate reviews, then using the same LLM to validate those reviews
- Creating a metric based on assumptions, then using results to validate those assumptions

**Valid Alternatives:**
- Independent validation with human annotations
- Cross-validation with established external benchmarks
- Triangulation with multiple independent measurement methods

### 2. Construct Validity Requirements

Before implementing ANY measurement system, you MUST:

1. **Define the construct theoretically**
   - What exactly are you measuring?
   - What is the theoretical basis?
   - How does it relate to established constructs?

2. **Establish ground truth**
   - How do you know when the construct is present/absent?
   - What is the gold standard measurement?
   - Who/what can provide authoritative labels?

3. **Validate the measurement**
   - Compare against ground truth on labeled data
   - Calculate precision, recall, F1, Cohen's kappa
   - Report inter-rater reliability if humans are involved
   - Show convergent and discriminant validity

4. **Document limitations**
   - What does your measure NOT capture?
   - What are the boundary conditions?
   - What confounds might exist?

### 3. Ground Truth Establishment

**REQUIRED before claiming any measurement is valid:**

```python
# Example: Bias Detection Ground Truth
ground_truth_requirements = {
    "source": "Independent expert annotations",
    "annotators": "≥3 domain experts",
    "agreement": "Cohen's kappa ≥ 0.7",
    "sample_size": "≥100 diverse examples",
    "annotation_guidelines": "Explicit, documented, tested",
    "validation": "Held-out test set with known labels"
}
```

**RED FLAGS indicating missing ground truth:**
- "We assume X indicates Y"
- "Pattern matching suggests..."
- "The model's confidence indicates..."
- "Self-reported metrics show..."
- No comparison to external validation

### 4. Statistical Rigor

**MANDATORY for any quantitative claim:**

1. **Pre-specify analysis plan**
   - Hypotheses before seeing data
   - Statistical tests chosen a priori
   - Multiple comparison corrections planned

2. **Report complete statistics**
   - Sample size and power analysis
   - Effect sizes with confidence intervals
   - Exact p-values (not just p < 0.05)
   - All tests performed (not just significant ones)

3. **Check assumptions**
   - Normality tests for parametric tests
   - Independence assumptions verified
   - Homogeneity of variance checked
   - Document violations and adjustments

4. **Avoid statistical sins**
   - No p-hacking (testing until significant)
   - No HARKing (hypothesizing after results known)
   - No cherry-picking (reporting only favorable results)
   - No underpowered studies claiming null results

### 5. Reproducibility Checklist

**REQUIRED before claiming any result:**

- [ ] Complete implementation details documented
- [ ] All hyperparameters and settings specified
- [ ] Random seeds and initialization documented
- [ ] Data sources and versions specified
- [ ] Preprocessing steps fully described
- [ ] Code available (or detailed pseudocode)
- [ ] Dependencies and versions listed
- [ ] Hardware and runtime environment specified
- [ ] Exact prompts/instructions provided
- [ ] All data artifacts available or described

**If ANY checkbox is unchecked, the work is NOT reproducible.**

## Validation Workflow

### Phase 1: Design Validation (BEFORE Implementation)

```markdown
## Measurement Design Review

### Construct Definition
- [ ] Theoretical definition provided
- [ ] Operational definition specified
- [ ] Relationship to existing constructs explained

### Ground Truth Plan
- [ ] Source of ground truth identified
- [ ] Annotation protocol documented
- [ ] Inter-rater reliability plan specified
- [ ] Sample size justified with power analysis

### Validation Strategy
- [ ] Validation method independent of measurement
- [ ] Comparison to established benchmarks planned
- [ ] Multiple validation approaches specified

### Statistical Plan
- [ ] Hypotheses pre-specified
- [ ] Statistical tests chosen with justification
- [ ] Multiple comparison corrections planned
- [ ] Effect size measures specified
```

### Phase 2: Implementation Validation (DURING Development)

```python
# Example validation code structure
class ValidatedMeasure:
    def __init__(self):
        self.ground_truth_data = None
        self.validation_metrics = {}
        self.is_validated = False
    
    def validate_against_ground_truth(self, ground_truth_dataset):
        """
        REQUIRED: Validate measure against independent ground truth
        """
        if ground_truth_dataset is None:
            raise ValueError("Cannot validate without ground truth")
        
        predictions = self.measure(ground_truth_dataset.samples)
        labels = ground_truth_dataset.labels
        
        # Calculate validation metrics
        self.validation_metrics = {
            'accuracy': calculate_accuracy(predictions, labels),
            'precision': calculate_precision(predictions, labels),
            'recall': calculate_recall(predictions, labels),
            'f1': calculate_f1(predictions, labels),
            'cohens_kappa': calculate_kappa(predictions, labels),
            'confusion_matrix': confusion_matrix(predictions, labels)
        }
        
        # Require minimum thresholds
        if self.validation_metrics['f1'] < 0.7:
            raise ValueError(f"Validation F1 {self.validation_metrics['f1']} below threshold 0.7")
        
        self.is_validated = True
        return self.validation_metrics
    
    def measure(self, samples):
        """
        Only callable after validation
        """
        if not self.is_validated:
            raise RuntimeError("Cannot use measure before validation")
        
        # Actual measurement logic here
        pass
```

### Phase 3: Results Validation (AFTER Experiments)

**Before reporting ANY result, verify:**

1. **Measurement Validity**
   - All measures validated against ground truth
   - Validation metrics reported
   - Limitations acknowledged

2. **Statistical Validity**
   - Assumptions checked and reported
   - Complete statistics provided
   - Effect sizes with confidence intervals
   - Multiple comparison corrections applied

3. **Reproducibility**
   - All checklist items completed
   - Code and data available
   - Results independently verified if possible

## Red Flags: Immediate Rejection Criteria

**STOP and redesign if you encounter:**

1. **Circular Validation**
   - "We use method X to detect Y, and the presence of Y validates X"
   - "The model's confidence correlates with accuracy, validating our confidence measure"

2. **Unvalidated Proxies**
   - "We assume pattern P indicates construct C"
   - "Dictionary-based detection of complex psychological constructs"
   - No comparison to ground truth

3. **Missing Ground Truth**
   - "We measure X but have no way to verify if X is actually present"
   - "Self-reported metrics without external validation"

4. **Statistical Red Flags**
   - p-values without effect sizes
   - "Significant" results with tiny samples
   - No correction for multiple comparisons
   - Selective reporting of results

5. **Reproducibility Failures**
   - "We used standard settings" (without specifying)
   - "Code available upon request" (not actually available)
   - Missing hyperparameters or random seeds

## Example: Bias Detection Validation

### ❌ INVALID Approach (Circular Logic)

```python
# BAD: Circular validation
def detect_bias(text):
    # Use pattern matching
    bias_score = count_bias_patterns(text)
    return bias_score

def validate_bias_detection():
    # BAD: Using same patterns to validate
    test_texts = generate_texts_with_patterns()
    scores = [detect_bias(t) for t in test_texts]
    print(f"Detection works! Found {sum(scores)} biases")
    # This is circular - patterns validate patterns
```

### ✅ VALID Approach (Independent Validation)

```python
# GOOD: Independent validation
def detect_bias(text):
    bias_score = count_bias_patterns(text)
    return bias_score

def validate_bias_detection():
    # GOOD: Independent ground truth from experts
    ground_truth_data = load_expert_annotated_reviews()
    # 100+ reviews annotated by 3+ experts with κ ≥ 0.7
    
    predictions = [detect_bias(r.text) for r in ground_truth_data]
    labels = [r.expert_bias_label for r in ground_truth_data]
    
    # Calculate validation metrics
    metrics = {
        'precision': precision_score(labels, predictions),
        'recall': recall_score(labels, predictions),
        'f1': f1_score(labels, predictions),
        'cohens_kappa': cohen_kappa_score(labels, predictions)
    }
    
    # Report limitations
    print(f"Validation metrics: {metrics}")
    print("Limitations: Only validated on academic reviews")
    print("May not generalize to other domains")
    
    return metrics
```

## Integration with Research Workflow

### When Designing Experiments

1. **Before writing ANY code:**
   - Define constructs theoretically
   - Identify ground truth sources
   - Plan validation strategy
   - Pre-specify statistical analysis

2. **Document design decisions:**
   - Why this measurement approach?
   - What are the alternatives?
   - What are the limitations?
   - How will you validate?

### When Implementing Measures

1. **Validate before using:**
   - Collect ground truth data
   - Validate against ground truth
   - Report validation metrics
   - Document limitations

2. **No shortcuts:**
   - Cannot skip validation "for now"
   - Cannot assume validity
   - Cannot use unvalidated measures in experiments

### When Reporting Results

1. **Complete transparency:**
   - Report all validation metrics
   - Acknowledge all limitations
   - Provide reproducibility details
   - Share code and data

2. **Honest interpretation:**
   - Don't overclaim
   - Acknowledge uncertainty
   - Discuss alternative explanations
   - Note boundary conditions

## Common Pitfalls and Solutions

### Pitfall 1: "We'll validate later"
**Solution:** No. Validate first. Invalid measures produce meaningless results.

### Pitfall 2: "Pattern matching is good enough"
**Solution:** No. Validate against ground truth or don't claim validity.

### Pitfall 3: "The model knows best"
**Solution:** No. Models need external validation, not self-validation.

### Pitfall 4: "Small sample but significant p-value"
**Solution:** Report effect sizes and confidence intervals. Check power.

### Pitfall 5: "Code available upon request"
**Solution:** Make code actually available now, not upon request.

## Validation Templates

See additional files:
- `validation_checklist.md` - Complete validation checklist
- `ground_truth_protocol.md` - Ground truth collection protocol
- `statistical_analysis_plan.md` - Statistical analysis template
- `reproducibility_checklist.md` - Full reproducibility checklist

## Usage in Code Reviews

When reviewing code or research designs, ask:

1. **Is there circular logic?**
   - Does validation use the same method as measurement?
   - Are assumptions used to validate themselves?

2. **Is there ground truth?**
   - How do we know the measure is correct?
   - What is the gold standard?

3. **Are statistics rigorous?**
   - Are assumptions checked?
   - Are effect sizes reported?
   - Is power adequate?

4. **Is it reproducible?**
   - Can someone else replicate this?
   - Are all details provided?

**If the answer to ANY question is "no" or "unclear," the work is not ready.**

## Remember

**The goal is not to publish quickly, but to publish correctly.**

Rigorous methodology takes more time upfront but produces:
- Valid findings that others can trust
- Reproducible results that others can build on
- Scientific progress that actually advances the field

**No shortcuts. No circular logic. No unvalidated claims.**
