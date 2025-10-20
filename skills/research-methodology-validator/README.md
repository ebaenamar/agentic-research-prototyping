# Research Methodology Validator Skill

## Purpose

This skill prevents common research methodology failures including:
- **Circular logic** in validation
- **Unvalidated measures** used in experiments
- **Missing ground truth** for validation
- **Non-reproducible** experiments
- **Weak statistical** claims

## The Problem

Your previous submission received criticism for exactly these issues:

> "The construct validity of the bias measures is weak, relying on simplistic dictionary-based pattern matching that risks conflating ordinary language with bias and lacks proper validation."

> "The evaluation is undermined by missing or unclear ground truth, making metrics like self-detection accuracy and confidence calibration uninterpretable."

> "Statistical claims are implausibly strong given the small sample size and lack of transparency about tests and assumptions."

**The issue:** Your system can identify these problems in other papers but doesn't apply the same standards to itself.

## The Solution

This skill enforces rigorous methodology at every stage:

### 1. Pre-Implementation: Design Validation

Before writing any code, complete:
- Construct definition (theoretical + operational)
- Ground truth plan (source, protocol, sample size)
- Validation strategy (independent, not circular)
- Statistical analysis plan (pre-specified)

### 2. Implementation: Measure Validation

Use the `ValidatedMeasure` class that:
- **Blocks usage** until validated against ground truth
- **Requires** independent validation (no circular logic)
- **Calculates** proper metrics (precision, recall, F1, Cohen's κ)
- **Documents** limitations explicitly

### 3. Experiments: Rigorous Analysis

Follow checklists for:
- Statistical assumptions
- Effect sizes with confidence intervals
- Multiple comparison corrections
- Complete reporting (not just significant results)

### 4. Reporting: Full Transparency

Provide:
- Complete implementation details
- All validation metrics
- Honest limitations
- Reproducible code and data

## Usage

### Quick Start

1. **Before implementing anything:**
   ```bash
   # Review the validation checklist
   cat validation_checklist.md
   ```

2. **Design your measure:**
   - Define construct theoretically
   - Plan ground truth collection
   - Design validation strategy

3. **Implement with validation:**
   ```python
   from scripts.validated_measure import ValidatedMeasure, GroundTruthDataset
   
   class YourMeasure(ValidatedMeasure):
       def __init__(self):
           super().__init__(
               name="your_measure",
               description="What it measures and when to use it"
           )
           
           # Document limitations upfront
           self.add_limitation("Limitation 1")
           self.add_limitation("Limitation 2")
       
       def _measure_impl(self, sample):
           # Your measurement logic
           return result
   
   # Create measure
   measure = YourMeasure()
   
   # Collect ground truth (from independent experts)
   ground_truth = GroundTruthDataset(
       samples=expert_annotated_samples,
       labels=expert_labels,
       metadata={
           'source': 'Expert annotations',
           'num_annotators': 3,
           'inter_rater_reliability': {'cohens_kappa': 0.75}
       }
   )
   
   # Validate (will raise error if validation fails)
   metrics = measure.validate_against_ground_truth(ground_truth)
   
   # Now you can use it
   result = measure.measure(new_sample)
   ```

4. **Run experiments:**
   - Follow statistical analysis plan
   - Check assumptions
   - Report complete results

5. **Write paper:**
   - Use validation report
   - Include all metrics
   - Acknowledge limitations

## Files

- **SKILL.md** - Main skill instructions (loaded by Claude)
- **validation_checklist.md** - Complete validation checklist
- **ground_truth_protocol.md** - How to collect ground truth
- **scripts/validated_measure.py** - Python framework for validated measures
- **README.md** - This file

## Example: Fixing Your Bias Detector

### Current Problem (Circular Logic)

```python
# BAD: Current implementation
class BiasDetector:
    def detect_bias(self, text):
        # Use pattern matching
        return count_patterns(text)
    
    def validate(self):
        # BAD: Using patterns to validate patterns
        test_texts = generate_texts_with_patterns()
        scores = [self.detect_bias(t) for t in test_texts]
        print("Works!")  # This is circular!
```

### Fixed Version (Independent Validation)

```python
# GOOD: Fixed implementation
from scripts.validated_measure import ValidatedMeasure, GroundTruthDataset

class BiasDetector(ValidatedMeasure):
    def __init__(self):
        super().__init__(
            name="confirmation_bias_detector",
            description="Detects confirmation bias in peer reviews"
        )
        
        # Document limitations
        self.add_limitation(
            "Only validated on CS peer reviews"
        )
        self.add_limitation(
            "May not generalize to other domains"
        )
    
    def _measure_impl(self, text):
        # Your pattern matching logic
        return bias_score

# Collect INDEPENDENT ground truth
# Get 3+ experts to annotate 100+ reviews
# Calculate inter-rater reliability (κ ≥ 0.7)
ground_truth = collect_expert_annotations()

# Validate
detector = BiasDetector()
metrics = detector.validate_against_ground_truth(ground_truth)

# Print validation report
print(detector.get_validation_report())

# Now you can use it (and report validation metrics in paper)
bias_score = detector.measure(review_text)
```

## Key Principles

### 1. No Circular Logic

**NEVER:**
- Use method X to validate method X
- Use model outputs to validate model
- Use assumptions to validate assumptions

**ALWAYS:**
- Validate against independent ground truth
- Use external benchmarks
- Triangulate with multiple methods

### 2. Ground Truth First

**BEFORE implementing:**
- Identify ground truth source
- Develop annotation protocol
- Collect expert annotations
- Calculate inter-rater reliability

**NEVER:**
- Assume patterns indicate constructs
- Use model confidence as ground truth
- Skip validation "for now"

### 3. Statistical Rigor

**ALWAYS:**
- Pre-specify hypotheses
- Check assumptions
- Report effect sizes with CIs
- Correct for multiple comparisons
- Report all results (not just significant)

**NEVER:**
- P-hack (test until significant)
- HARK (hypothesize after results)
- Cherry-pick results
- Claim significance with tiny samples

### 4. Full Reproducibility

**PROVIDE:**
- Complete code (actually available)
- All data (or access procedure)
- All hyperparameters
- All random seeds
- All dependencies with versions

**NEVER:**
- "Code available upon request"
- "Standard settings"
- Vague descriptions
- Missing details

## Integration with Your Project

### Step 1: Audit Current Code

Run the circular validation detector:

```python
from scripts.validated_measure import CircularValidationDetector

is_independent, explanation = CircularValidationDetector.check_independence(
    measure_method="pattern matching on bias indicators",
    ground_truth_method="pattern matching on test texts"  # BAD!
)
print(explanation)
```

### Step 2: Collect Ground Truth

Follow `ground_truth_protocol.md`:
1. Develop annotation guidelines
2. Recruit 3+ expert annotators
3. Pilot annotation (n=20-30)
4. Calculate inter-rater reliability
5. Full annotation (n≥100)
6. Create train/val/test splits

### Step 3: Reimplement with Validation

Convert your measures to `ValidatedMeasure` subclasses:
- Blocks usage until validated
- Requires independent ground truth
- Calculates proper metrics
- Documents limitations

### Step 4: Re-run Experiments

With validated measures:
- Follow statistical analysis plan
- Check assumptions
- Report complete results
- Include validation metrics

### Step 5: Rewrite Paper

Include:
- Validation methodology
- All validation metrics
- Honest limitations
- Reproducibility details

## Checklist for Your Project

- [ ] Audit current code for circular logic
- [ ] Develop annotation guidelines for each bias type
- [ ] Recruit expert annotators
- [ ] Collect ground truth (n≥100, κ≥0.7)
- [ ] Reimplement measures with validation
- [ ] Validate all measures against ground truth
- [ ] Re-run experiments with validated measures
- [ ] Update paper with validation details
- [ ] Make code and data available
- [ ] Independent verification of reproducibility

## Expected Outcomes

### Before (Current State)

- Circular validation (patterns validate patterns)
- No ground truth
- Unvalidated measures
- Weak statistical claims
- Non-reproducible

**Result:** Rejection with criticism of methodology

### After (With This Skill)

- Independent validation against expert annotations
- Proper ground truth with inter-rater reliability
- All measures validated before use
- Rigorous statistics with effect sizes
- Fully reproducible

**Result:** Methodologically sound research that can be trusted

## Questions?

Review the skill files:
- `SKILL.md` - Core principles and guidelines
- `validation_checklist.md` - Step-by-step checklist
- `ground_truth_protocol.md` - How to collect ground truth
- `scripts/validated_measure.py` - Implementation framework

## Remember

**The goal is not to publish quickly, but to publish correctly.**

Rigorous methodology takes more time upfront but produces:
- Valid findings that others can trust
- Reproducible results that others can build on
- Scientific progress that actually advances the field

**No shortcuts. No circular logic. No unvalidated claims.**
