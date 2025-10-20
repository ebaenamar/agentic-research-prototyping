# Ground Truth Collection Protocol

## Purpose
Establish authoritative labels for validating measurements without circular logic.

## General Requirements

### Minimum Standards
- **Sample Size:** ≥100 diverse examples (power analysis to justify)
- **Annotators:** ≥3 independent experts
- **Agreement:** Cohen's kappa ≥ 0.7 (substantial agreement)
- **Documentation:** Complete annotation guidelines
- **Validation:** Held-out test set with known labels

## Protocol Steps

### 1. Define Annotation Task

**Clearly specify:**
- What are annotators labeling?
- What are the possible labels/values?
- What are the decision criteria?
- What are edge cases and how to handle them?

**Example: Bias Annotation**
```markdown
Task: Identify presence of confirmation bias in peer review text

Labels: 
- 0: No confirmation bias present
- 1: Mild confirmation bias (subtle indicators)
- 2: Moderate confirmation bias (clear indicators)
- 3: Strong confirmation bias (pervasive throughout)

Decision Criteria:
- Confirmation bias = reviewer selectively emphasizes evidence 
  supporting their initial judgment while dismissing contradictory evidence

Indicators:
- Asymmetric treatment of similar evidence
- Dismissal of contradictory findings without justification
- Over-emphasis on confirming evidence
- Lack of consideration of alternative explanations

Edge Cases:
- Legitimate criticism vs. bias: If criticism is well-justified 
  with evidence, it's not bias
- Domain expertise: Expert knowledge is not bias if applied consistently
```

### 2. Develop Annotation Guidelines

**Include:**
- Detailed instructions
- Decision trees for complex cases
- Annotated examples (positive and negative)
- Common mistakes to avoid
- Calibration exercises

**Template:**
```markdown
# Annotation Guidelines: [Construct Name]

## Overview
[Brief description of what you're annotating]

## Label Definitions
[Detailed definition of each label with examples]

## Decision Process
1. Read the entire text
2. Identify potential indicators
3. Evaluate each indicator against criteria
4. Consider alternative explanations
5. Assign label based on preponderance of evidence

## Examples

### Example 1: Clear Positive Case
Text: [example text]
Label: [label]
Rationale: [why this label]

### Example 2: Clear Negative Case
Text: [example text]
Label: [label]
Rationale: [why this label]

### Example 3: Ambiguous Case
Text: [example text]
Label: [label]
Rationale: [why this label, acknowledging ambiguity]

## Common Mistakes
1. [Mistake]: [How to avoid]
2. [Mistake]: [How to avoid]

## Calibration Exercise
[10 pre-labeled examples for annotators to practice]
```

### 3. Select Annotators

**Criteria:**
- Domain expertise relevant to construct
- No conflict of interest
- Independent (not involved in research)
- Trained on annotation guidelines

**Minimum:** 3 annotators per example (for reliability calculation)

### 4. Pilot Annotation

**Process:**
1. Select 20-30 examples
2. All annotators label independently
3. Calculate inter-rater reliability (Cohen's kappa)
4. Discuss disagreements
5. Refine guidelines
6. Repeat until κ ≥ 0.7

**If κ < 0.7:**
- Guidelines may be unclear
- Construct may be poorly defined
- Annotators may need more training
- Task may be too subjective

### 5. Full Annotation

**Process:**
1. Randomly sample examples from target distribution
2. Each example labeled by ≥3 annotators
3. Track annotation time and difficulty
4. Monitor inter-rater reliability throughout
5. Resolve disagreements through discussion or majority vote

**Sample Size Calculation:**
```python
# Minimum sample size for validation
from statsmodels.stats.power import zt_ind_solve_power

# For detecting medium effect size (d=0.5) with power=0.8
n = zt_ind_solve_power(
    effect_size=0.5,
    alpha=0.05,
    power=0.8,
    alternative='two-sided'
)
print(f"Minimum sample size: {n} per group")
# Typically ~64 per group, so ~130 total for binary classification
```

### 6. Quality Control

**Monitor:**
- Inter-rater reliability (ongoing)
- Annotation time (flag too fast/slow)
- Annotator agreement patterns
- Edge case frequency

**Red Flags:**
- One annotator consistently disagrees
- Reliability drops over time
- Many "unsure" or skipped examples
- Systematic disagreement on specific types

### 7. Create Gold Standard Dataset

**Components:**
1. **Training Set** (60%)
   - For developing/tuning your measure
   - Can iterate on this

2. **Validation Set** (20%)
   - For selecting between approaches
   - Use during development

3. **Test Set** (20%)
   - For final evaluation
   - **NEVER look at until final evaluation**
   - Report these results

**Format:**
```json
{
  "dataset_name": "bias_annotations_v1",
  "version": "1.0",
  "created": "2025-10-19",
  "annotators": ["expert1", "expert2", "expert3"],
  "inter_rater_reliability": {
    "cohens_kappa": 0.73,
    "fleiss_kappa": 0.71,
    "percent_agreement": 0.82
  },
  "examples": [
    {
      "id": "ex001",
      "text": "...",
      "annotations": [2, 2, 1],
      "gold_label": 2,
      "confidence": "high",
      "notes": "Clear case, one annotator more conservative"
    }
  ]
}
```

## Bias-Specific Ground Truth Protocol

### For Confirmation Bias in Reviews

**Annotation Task:**
- Identify instances where reviewer shows confirmation bias
- Rate severity on 0-3 scale

**Required Context:**
- Full review text
- Paper abstract/summary
- Reviewer's overall recommendation

**Indicators to Annotate:**
1. Asymmetric evidence treatment
2. Dismissal without justification
3. Over-emphasis on confirming evidence
4. Ignoring alternative explanations

**Validation:**
- Compare against established bias detection methods
- Correlate with review outcomes (accept/reject)
- Check for known biases (e.g., prestige bias)

### For Self-Enhancement Bias

**Annotation Task:**
- Identify self-referential language that enhances reviewer's position
- Rate frequency and severity

**Indicators:**
- First-person assertions without evidence
- Claims of superior judgment
- Dismissal of author expertise
- Overconfidence in own assessment

**Validation:**
- Compare to objective language baseline
- Correlate with reviewer experience level
- Check against review quality metrics

## Alternative Ground Truth Sources

### When Expert Annotation is Not Feasible

1. **Synthetic Ground Truth**
   - Create examples with known properties
   - Limitation: May not reflect real distribution
   - Use only for initial validation

2. **Behavioral Ground Truth**
   - Use actual outcomes (e.g., paper acceptance)
   - Limitation: Outcomes may be noisy
   - Requires large sample size

3. **Comparative Ground Truth**
   - Compare to established measures
   - Limitation: Inherits limitations of baseline
   - Better than nothing, but not ideal

4. **Crowdsourced Annotation**
   - Use many non-expert annotators
   - Limitation: May miss subtle cases
   - Requires quality control and validation

**Always document which approach you use and its limitations.**

## Reporting Ground Truth

### In Methods Section

```markdown
## Ground Truth Annotation

We collected ground truth annotations for [construct] using the following protocol:

**Annotators:** Three domain experts with [qualifications] independently 
annotated [N] examples sampled from [distribution].

**Annotation Task:** Annotators rated [construct] on a [scale] based on 
[criteria]. See Appendix A for complete annotation guidelines.

**Inter-Rater Reliability:** Cohen's kappa = [value] (95% CI: [range]), 
indicating [substantial/moderate] agreement. Disagreements were resolved 
through [discussion/majority vote].

**Dataset Split:** Examples were randomly split into training (60%, n=[N]), 
validation (20%, n=[N]), and test (20%, n=[N]) sets. The test set was 
held out until final evaluation.

**Limitations:** [Acknowledge any limitations of the ground truth, such as 
domain specificity, potential annotator biases, or edge cases]
```

### In Results Section

```markdown
## Validation Against Ground Truth

Our measure achieved the following performance on the held-out test set:

| Metric | Value | 95% CI |
|--------|-------|--------|
| Accuracy | 0.XX | [X.XX, X.XX] |
| Precision | 0.XX | [X.XX, X.XX] |
| Recall | 0.XX | [X.XX, X.XX] |
| F1 Score | 0.XX | [X.XX, X.XX] |
| Cohen's κ | 0.XX | [X.XX, X.XX] |

[Include confusion matrix and error analysis]

**Limitations:** Our measure shows lower performance on [specific cases], 
suggesting [interpretation]. This indicates [boundary conditions].
```

## Checklist

Before claiming your measure is validated:

- [ ] Ground truth collected from independent source
- [ ] ≥3 annotators per example
- [ ] Inter-rater reliability ≥ 0.7
- [ ] Complete annotation guidelines documented
- [ ] Held-out test set created and preserved
- [ ] Validation metrics calculated and reported
- [ ] Limitations acknowledged
- [ ] Data and guidelines available for reproducibility

**If ANY item is unchecked, your validation is incomplete.**
