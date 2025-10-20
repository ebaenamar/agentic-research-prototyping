# Complete Research Workflow for Foundational Models

## Visual Workflow

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    RIGOROUS RESEARCH WORKFLOW                              ║
║              From Gap Identification to Publication                        ║
╚═══════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 1: LITERATURE REVIEW & GAP IDENTIFICATION                         │
│ Skill: literature-review-skill                                          │
└─────────────────────────────────────────────────────────────────────────┘
    │
    ├─► Step 1.1: Define Research Scope
    │   ├─ Topic: Specific aspect of foundational models
    │   ├─ Time period: Last 2-3 years
    │   ├─ Venues: arXiv, NeurIPS, ICML, ICLR, ACL, etc.
    │   └─ Model types: LLMs, VLMs, multimodal
    │
    ├─► Step 1.2: Systematic Literature Search
    │   ├─ Keyword search (Boolean operators)
    │   ├─ Venue-specific search
    │   ├─ Citation tracking (forward/backward)
    │   └─ Author tracking
    │
    ├─► Step 1.3: Paper Screening & Analysis
    │   ├─ Title screening → Abstract → Full paper
    │   ├─ Extract: Contribution, Methodology, Results, Limitations
    │   └─ Quality assessment per paper
    │
    ├─► Step 1.4: Synthesis & Categorization
    │   ├─ Group by research questions
    │   ├─ Compare methodologies
    │   ├─ Identify consensus vs. disagreements
    │   └─ Map limitations across papers
    │
    ├─► Step 1.5: Gap Identification
    │   ├─ Knowledge gaps (unanswered questions)
    │   ├─ Methodological gaps (better measures)
    │   ├─ Practical gaps (real-world applications)
    │   └─ Theoretical gaps (mechanisms not understood)
    │
    ├─► Step 1.6: Gap Validation
    │   ├─ Is it genuine? (thorough search confirms)
    │   ├─ Is it significant? (matters to field)
    │   ├─ Is it feasible? (resources available)
    │   └─ Is it novel? (different from existing)
    │
    └─► Step 1.7: Research Question Formulation
        ├─ Specific and answerable
        ├─ Significant to field
        ├─ Novel contribution
        └─ Feasible with resources
    
    ✓ QUALITY GATE 1
    ├─ [ ] Comprehensive literature search completed
    ├─ [ ] Gaps validated (genuine, significant, feasible, novel)
    ├─ [ ] Research questions clearly formulated
    └─ [ ] Contribution statement clear
    
    │
    ▼

┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 2: METHODOLOGY DESIGN & VALIDATION                                │
│ Skill: research-methodology-validator                                   │
└─────────────────────────────────────────────────────────────────────────┘
    │
    ├─► Step 2.1: Construct Definition
    │   ├─ Theoretical definition (what are you measuring?)
    │   ├─ Operational definition (how will you measure it?)
    │   ├─ Relationship to existing constructs
    │   └─ Boundary conditions
    │
    ├─► Step 2.2: Ground Truth Planning
    │   ├─ Identify independent ground truth source
    │   ├─ Develop annotation protocol
    │   ├─ Recruit ≥3 expert annotators
    │   ├─ Power analysis for sample size (n≥100)
    │   └─ Plan inter-rater reliability (target κ≥0.7)
    │
    ├─► Step 2.3: Validation Strategy Design
    │   ├─ Ensure independence (NO circular logic)
    │   ├─ Plan validation metrics (precision, recall, F1, κ)
    │   ├─ Define success thresholds (F1≥0.7, κ≥0.6)
    │   └─ Plan sensitivity analyses
    │
    ├─► Step 2.4: Statistical Analysis Plan (PRE-SPECIFIED)
    │   ├─ Hypotheses (before seeing data!)
    │   ├─ Statistical tests with justification
    │   ├─ Multiple comparison corrections
    │   ├─ Effect size measures
    │   ├─ Power analysis (target power≥0.8)
    │   └─ Significance thresholds (α=0.05)
    │
    ├─► Step 2.5: Circular Logic Check
    │   ├─ Validation method ≠ Measurement method
    │   ├─ Ground truth independent of measure
    │   └─ No self-validation
    │
    └─► Step 2.6: Reproducibility Planning
        ├─ All parameters will be documented
        ├─ Random seeds will be specified
        ├─ Code will be made available
        └─ Data access procedure defined
    
    ✓ QUALITY GATE 2
    ├─ [ ] Constructs clearly defined (theoretical + operational)
    ├─ [ ] Ground truth plan complete (source, protocol, n≥100)
    ├─ [ ] Validation strategy independent (NO circular logic)
    ├─ [ ] Statistical plan pre-specified (before data collection)
    └─ [ ] Reproducibility plan complete
    
    │
    ▼

┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 2.5: GROUND TRUTH COLLECTION & MEASURE VALIDATION                │
│ Skills: research-methodology-validator + validation-without-humans     │
└─────────────────────────────────────────────────────────────────────────┘
    │
    ├─► Decision: Can you get expert annotations?
    │   │
    │   ├─ YES (PREFERRED) → Expert Annotation Path
    │   │   │
    │   │   ├─► Step 2.5.1: Annotation Guidelines Development
    │   │   │   ├─ Clear task definition
    │   │   │   ├─ Label definitions with examples
    │   │   │   ├─ Decision criteria
    │   │   │   └─ Edge case handling
    │   │   │
    │   │   ├─► Step 2.5.2: Pilot Annotation (n=20-30)
    │   │   │   ├─ All annotators label same examples
    │   │   │   ├─ Calculate inter-rater reliability
    │   │   │   ├─ Discuss disagreements
    │   │   │   └─ Refine guidelines until κ≥0.7
    │   │   │
    │   │   ├─► Step 2.5.3: Full Annotation (n≥100)
    │   │   │   ├─ Each example labeled by ≥3 annotators
    │   │   │   ├─ Monitor quality throughout
    │   │   │   ├─ Resolve disagreements
    │   │   │   └─ Create train/val/test splits (60/20/20)
    │   │   │
    │   │   └─► Validation Confidence: HIGH ⭐
    │   │
    │   └─ NO → Alternative Validation Path
    │       │
    │       ├─► Step 2.5.A: Document Why No Experts
    │       │   ├─ Cost prohibitive?
    │       │   ├─ Time constraints?
    │       │   ├─ Experts unavailable?
    │       │   └─ Domain too specialized?
    │       │
    │       ├─► Step 2.5.B: Select Alternative Strategy
    │       │   │
    │       │   ├─ Option 1: Behavioral Ground Truth
    │       │   │   ├─ Use actual outcomes (acceptance, votes, etc.)
    │       │   │   ├─ Control for confounds
    │       │   │   └─ Confidence: MEDIUM
    │       │   │
    │       │   ├─ Option 2: Comparative Validation
    │       │   │   ├─ Compare to established measures
    │       │   │   ├─ Show convergent + discriminant validity
    │       │   │   └─ Confidence: MEDIUM
    │       │   │
    │       │   ├─ Option 3: Crowdsourced Validation
    │       │   │   ├─ Many non-expert annotators (5-10 per example)
    │       │   │   ├─ Quality control (attention checks, gold standard)
    │       │   │   └─ Confidence: MEDIUM (if agreement high)
    │       │   │
    │       │   ├─ Option 4: Hybrid Approach (RECOMMENDED)
    │       │   │   ├─ Small expert sample (n=20-30, affordable)
    │       │   │   ├─ Large behavioral/crowdsourced (n=1000+)
    │       │   │   └─ Confidence: MEDIUM-HIGH
    │       │   │
    │       │   └─ Option 5: Multiple Strategies (BEST)
    │       │       ├─ Combine 2-3 alternative strategies
    │       │       ├─ Triangulation increases confidence
    │       │       └─ Confidence: MEDIUM-HIGH
    │       │
    │       ├─► Step 2.5.C: Implement Alternative Validation
    │       │   ├─ Follow selected strategy rigorously
    │       │   ├─ Document all assumptions
    │       │   ├─ Calculate appropriate metrics
    │       │   └─ Assess robustness
    │       │
    │       └─► Step 2.5.D: Document Limitations
    │           ├─ Why this approach was used
    │           ├─ What limitations it has
    │           ├─ What confidence level achieved
    │           └─ What generalizability boundaries exist
    │
    ├─► Step 2.5.4: Measure Implementation
    │   ├─ Implement as ValidatedMeasure subclass
    │   ├─ Document limitations upfront
    │   └─ Blocks usage until validated
    │
    └─► Step 2.5.5: Measure Validation
        ├─ Validate on training set (or equivalent)
        ├─ Tune on validation set (or equivalent)
        ├─ Final evaluation on test set (HELD OUT)
        ├─ Calculate appropriate metrics for validation type
        ├─ Must meet thresholds (adjusted for validation type)
        └─ Document failure cases and limitations
    
    ✓ QUALITY GATE 2.5
    ├─ [ ] Ground truth collected OR alternative validation completed
    │       Expert path: n≥100, κ≥0.7 (HIGH confidence)
    │       Alternative path: Appropriate strategy with justification (MEDIUM confidence)
    ├─ [ ] All measures validated (cannot use without validation)
    ├─ [ ] Validation metrics meet thresholds (adjusted for validation type)
    ├─ [ ] Limitations explicitly documented
    ├─ [ ] Confidence level clearly stated (HIGH/MEDIUM-HIGH/MEDIUM/LOW)
    ├─ [ ] Generalizability boundaries defined
    └─ [ ] Test set preserved (not examined until final eval)
    
    │
    ▼

┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 3: EXPERIMENT DESIGN & IMPLEMENTATION                             │
│ Skill: experiment-design-skill                                          │
└─────────────────────────────────────────────────────────────────────────┘
    │
    ├─► Step 3.1: Experimental Conditions Design
    │   ├─ Define each condition precisely
    │   ├─ Specify all parameters (model, temp, top_p, etc.)
    │   ├─ Document exact prompts
    │   └─ Justify configuration choices
    │
    ├─► Step 3.2: Control Conditions
    │   ├─ Baseline (standard approach)
    │   ├─ Negative control (should show no effect)
    │   ├─ Positive control (should show known effect)
    │   └─ Ablations (test necessity of components)
    │
    ├─► Step 3.3: Sample Selection
    │   ├─ Define population
    │   ├─ Sampling method (random/stratified)
    │   ├─ Sample size (from power analysis)
    │   ├─ Inclusion/exclusion criteria
    │   └─ Stratification if needed
    │
    ├─► Step 3.4: Randomization
    │   ├─ What gets randomized
    │   ├─ Random seed specification
    │   ├─ Randomization algorithm
    │   └─ Balance verification
    │
    ├─► Step 3.5: Implementation
    │   ├─ Complete configuration file
    │   ├─ Set all random seeds
    │   ├─ Comprehensive logging
    │   ├─ Error handling with retries
    │   └─ Quality control checks
    │
    ├─► Step 3.6: Pilot Run (n=10-20 per condition)
    │   ├─ Test all conditions run without errors
    │   ├─ Verify measurements produce valid values
    │   ├─ Check logging captures everything
    │   ├─ Verify data format
    │   └─ Fix any issues found
    │
    └─► Step 3.7: Full Experiment Execution
        ├─ Run with quality monitoring
        ├─ Log everything
        ├─ Handle errors gracefully
        ├─ Save results continuously
        └─ Verify completion
    
    ✓ QUALITY GATE 3
    ├─ [ ] All conditions precisely specified
    ├─ [ ] Proper controls in place
    ├─ [ ] Sample size adequate (power analysis)
    ├─ [ ] Randomization implemented
    ├─ [ ] Pilot run successful
    ├─ [ ] Full experiment completed
    ├─ [ ] Data verified and cleaned
    └─ [ ] All data saved with backups
    
    │
    ▼

┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 4: STATISTICAL ANALYSIS & INTERPRETATION                          │
│ Skill: results-analysis-skill                                           │
└─────────────────────────────────────────────────────────────────────────┘
    │
    ├─► Step 4.1: Load Pre-Specified Analysis Plan
    │   └─ Follow plan exactly (prevents p-hacking)
    │
    ├─► Step 4.2: Check Statistical Assumptions
    │   ├─ Normality (Shapiro-Wilk)
    │   ├─ Homogeneity of variance (Levene's)
    │   ├─ Independence (design ensures)
    │   └─ Use backup tests if violated
    │
    ├─► Step 4.3: Primary Analysis
    │   ├─ Run pre-specified test
    │   ├─ Calculate test statistic and p-value
    │   ├─ Calculate effect size (Cohen's d, η², etc.)
    │   ├─ Calculate 95% confidence intervals
    │   └─ Report: n, M, SD, test, statistic, p, d, CI
    │
    ├─► Step 4.4: Secondary Analyses
    │   ├─ Run all pre-specified secondary analyses
    │   └─ Same rigor as primary
    │
    ├─► Step 4.5: Multiple Comparison Correction
    │   ├─ Apply pre-specified correction (Holm, FDR, etc.)
    │   ├─ Report original and corrected p-values
    │   └─ Report how many survive correction
    │
    ├─► Step 4.6: Effect Size Interpretation
    │   ├─ Magnitude (small/medium/large)
    │   ├─ Practical significance (not just statistical)
    │   └─ Confidence interval interpretation
    │
    ├─► Step 4.7: Sensitivity Analysis
    │   ├─ Without outliers
    │   ├─ Different exclusion criteria
    │   ├─ Different statistical tests
    │   └─ Assess robustness
    │
    ├─► Step 4.8: Exploratory Analyses (if any)
    │   ├─ CLEARLY MARKED as exploratory
    │   └─ Not treated as confirmatory
    │
    └─► Step 4.9: Honest Interpretation
        ├─ Statistical significance + effect size + CI
        ├─ Practical significance assessment
        ├─ Alternative explanations considered
        ├─ Limitations acknowledged
        ├─ Boundary conditions discussed
        └─ NO OVERCLAIMING
    
    ✓ QUALITY GATE 4
    ├─ [ ] Pre-specified plan followed
    ├─ [ ] Assumptions checked and reported
    ├─ [ ] Effect sizes with CIs calculated
    ├─ [ ] Multiple comparisons corrected
    ├─ [ ] Sensitivity analyses performed
    ├─ [ ] All results reported (not just significant)
    ├─ [ ] Exploratory analyses clearly marked
    ├─ [ ] Interpretation honest (no overclaiming)
    └─ [ ] Limitations acknowledged
    
    │
    ▼

┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 5: MULTI-STAGE REVIEW & VALIDATION                                │
│ Skill: research-review-skill                                            │
└─────────────────────────────────────────────────────────────────────────┘
    │
    ├─► Review Stage 1: METHODOLOGY REVIEW
    │   ├─ Construct validity check
    │   ├─ Validation independence check (NO circular logic)
    │   ├─ Ground truth quality check
    │   ├─ Statistical plan review
    │   └─ Decision: Approve / Revise / Redesign
    │       │
    │       ├─ If REVISE → Fix issues → Re-review
    │       └─ If REDESIGN → Back to Phase 2
    │
    ├─► Review Stage 2: IMPLEMENTATION REVIEW
    │   ├─ Code quality check
    │   ├─ Reproducibility check
    │   ├─ Configuration completeness
    │   ├─ Quality control verification
    │   └─ Decision: Approve / Minor fixes / Major revisions
    │       │
    │       └─ If issues → Fix → Re-review
    │
    ├─► Review Stage 3: RESULTS REVIEW
    │   ├─ Statistical validity check
    │   ├─ Data quality verification
    │   ├─ Interpretation honesty check
    │   ├─ Reporting completeness check
    │   └─ Decision: Approve / Revise / Additional analyses
    │       │
    │       └─ If issues → Fix → Re-review
    │
    ├─► Review Stage 4: CONTRIBUTION REVIEW
    │   ├─ Novelty assessment
    │   ├─ Significance assessment
    │   ├─ Quality assessment
    │   ├─ Clarity assessment
    │   └─ Decision: Strong / Adequate / Weak
    │       │
    │       └─ If weak → Strengthen or reconsider
    │
    ├─► Review Stage 5: REPRODUCIBILITY REVIEW
    │   ├─ Independent person sets up environment
    │   ├─ Independent person runs code
    │   ├─ Verify results match reported values
    │   ├─ Check all claims can be verified
    │   └─ Decision: Fully reproducible / Minor issues / Major issues
    │       │
    │       └─ If issues → Fix → Re-verify
    │
    └─► FINAL APPROVAL
        ├─ All review stages passed
        ├─ All critical issues resolved
        ├─ Independent verification successful
        └─ Ready for publication
    
    ✓ QUALITY GATE 5 (FINAL)
    ├─ [ ] All 5 review stages completed
    ├─ [ ] All critical issues resolved
    ├─ [ ] All major issues addressed
    ├─ [ ] Independent reproduction successful
    ├─ [ ] Complete documentation verified
    ├─ [ ] Code and data publicly available
    ├─ [ ] No overclaiming in any claims
    └─ [ ] All reviewers signed off
    
    │
    ▼

╔═══════════════════════════════════════════════════════════════════════════╗
║                    PUBLICATION-READY RESEARCH                              ║
║                                                                            ║
║  ✓ Methodologically sound (no circular logic)                             ║
║  ✓ All measures validated (against independent ground truth)              ║
║  ✓ Statistically rigorous (effect sizes, CIs, pre-specified)              ║
║  ✓ Fully reproducible (complete documentation, available code/data)       ║
║  ✓ Honestly reported (all results, limitations acknowledged)              ║
║  ✓ Genuine contribution (novel, significant, validated)                   ║
║  ✓ Independently verified (reproduction successful)                       ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

## Detailed Phase Breakdown

### Phase 1: Literature Review (2-4 weeks)
**Input:** Research interest in foundational models  
**Output:** Validated research questions  
**Key Activities:**
- Systematic search (arXiv, conferences, citations)
- Critical analysis (100+ papers → 20-30 core papers)
- Gap identification and validation
- Research question formulation

**Deliverables:**
- Literature synthesis document
- Gap analysis with evidence
- Research questions (specific, answerable, novel)
- Contribution statement

---

### Phase 2: Methodology Design (2-3 weeks)
**Input:** Research questions  
**Output:** Validated methodology design  
**Key Activities:**
- Construct definition (theoretical + operational)
- Ground truth planning (protocol, annotators, sample size)
- Validation strategy (independent, not circular)
- Statistical analysis plan (pre-specified)

**Deliverables:**
- Methodology design document
- Ground truth collection protocol
- Statistical analysis plan
- Reproducibility plan

**Critical Check:** Run `methodology_auditor.py` to detect circular logic

---

### Phase 2.5: Ground Truth & Validation (3-4 weeks)
**Input:** Methodology design  
**Output:** Validated measures  
**Key Activities:**
- Develop annotation guidelines
- Pilot annotation (n=20-30, refine until κ≥0.7)
- Full annotation (n≥100, ≥3 annotators per example)
- Implement ValidatedMeasure classes
- Validate against ground truth (F1≥0.7, κ≥0.6)

**Deliverables:**
- Annotated ground truth dataset (train/val/test)
- Validated measures (with validation metrics)
- Limitation documentation
- Validation report

**Critical Check:** Measures CANNOT be used until validated

---

### Phase 3: Experiment Implementation (2-3 weeks)
**Input:** Validated measures  
**Output:** Experimental data  
**Key Activities:**
- Design experimental conditions
- Implement with reproducibility (seeds, logging, config)
- Pilot run (n=10-20 per condition)
- Full experiment execution
- Data verification and cleaning

**Deliverables:**
- Complete experimental configuration
- Experimental data (raw + processed)
- Comprehensive logs
- Data verification report

**Critical Check:** Pilot run must succeed before full experiment

---

### Phase 4: Analysis & Interpretation (1-2 weeks)
**Input:** Experimental data + pre-specified analysis plan  
**Output:** Statistical results + honest interpretation  
**Key Activities:**
- Follow pre-specified analysis plan
- Check assumptions
- Calculate effect sizes with CIs
- Multiple comparison correction
- Sensitivity analysis
- Honest interpretation (no overclaiming)

**Deliverables:**
- Complete statistical results
- Effect size plots with CIs
- Distribution visualizations
- Results tables
- Honest interpretation with limitations

**Critical Check:** Must follow pre-specified plan (no p-hacking)

---

### Phase 5: Review & Refinement (2-3 weeks)
**Input:** Complete research  
**Output:** Publication-ready work  
**Key Activities:**
- 5-stage review process
- Issue identification and resolution
- Independent reproduction
- Iterative refinement
- Final approval

**Deliverables:**
- Review reports for each stage
- Issue resolution log
- Independent verification report
- Final approval document

**Critical Check:** Independent reproduction must succeed

---

## Timeline Summary

**Total Duration:** 12-19 weeks (3-5 months)

| Phase | Duration | Can Skip? |
|-------|----------|-----------|
| 1. Literature Review | 2-4 weeks | NO |
| 2. Methodology Design | 2-3 weeks | NO |
| 2.5. Ground Truth & Validation | 3-4 weeks | NO |
| 3. Experiment Implementation | 2-3 weeks | NO |
| 4. Analysis & Interpretation | 1-2 weeks | NO |
| 5. Review & Refinement | 2-3 weeks | NO |

**None of these phases can be skipped.** Each builds on the previous.

## Critical Decision Points

### Decision Point 1: After Gap Validation
**Question:** Is the gap genuine, significant, feasible, and novel?
- **YES** → Proceed to Phase 2
- **NO** → Return to gap identification or reconsider project

### Decision Point 2: After Methodology Design
**Question:** Is methodology sound and validation independent?
- **YES** → Proceed to Phase 2.5
- **NO** → Redesign methodology

### Decision Point 3: After Measure Validation
**Question:** Do measures meet validation thresholds (F1≥0.7, κ≥0.6)?
- **YES** → Proceed to Phase 3
- **NO** → Improve measures or reconsider constructs

### Decision Point 4: After Pilot Run
**Question:** Does pilot run succeed without major issues?
- **YES** → Proceed to full experiment
- **NO** → Fix issues and re-pilot

### Decision Point 5: After Results
**Question:** Do results support hypotheses?
- **YES** → Proceed to review (but report honestly)
- **NO** → Also proceed to review (negative results are valid!)

### Decision Point 6: After Each Review Stage
**Question:** Are there critical issues?
- **NO CRITICAL** → Proceed to next stage
- **CRITICAL ISSUES** → Fix and re-review

### Decision Point 7: After Independent Reproduction
**Question:** Can independent person reproduce results?
- **YES** → Final approval
- **NO** → Fix reproducibility issues

## Iteration Loops

### Loop 1: Methodology Refinement
```
Methodology Design → Review → Issues Found → Redesign → Review
                                                  ↑          │
                                                  └──────────┘
                                              (until approved)
```

### Loop 2: Measure Validation
```
Implement Measure → Validate → Below Threshold → Improve → Validate
                                                     ↑          │
                                                     └──────────┘
                                              (until F1≥0.7, κ≥0.6)
```

### Loop 3: Review Refinement
```
Complete Research → Review → Issues → Fix → Review
                                 ↑            │
                                 └────────────┘
                          (until all issues resolved)
```

## Quality Assurance Throughout

### Continuous Checks
- **After each step:** Verify deliverables complete
- **After each phase:** Quality gate must pass
- **Throughout:** Document everything
- **Before proceeding:** Get approval/sign-off

### Automated Tools
- `methodology_auditor.py` - Detect circular logic
- `ValidatedMeasure` framework - Enforce validation
- Statistical analysis templates - Prevent p-hacking
- Reproducibility checker - Verify completeness

### Manual Reviews
- Peer review of methodology
- Code review of implementation
- Statistical review of results
- Independent reproduction attempt

## Success Metrics

### Methodology Quality
- ✓ No circular logic detected
- ✓ All measures validated (F1≥0.7, κ≥0.6)
- ✓ Statistical plan pre-specified
- ✓ Reproducibility complete

### Results Quality
- ✓ Effect sizes with CIs reported
- ✓ All assumptions checked
- ✓ Multiple comparisons corrected
- ✓ Sensitivity analyses performed

### Contribution Quality
- ✓ Novel (genuinely different)
- ✓ Significant (matters to field)
- ✓ Valid (methodologically sound)
- ✓ Reproducible (independently verified)

## Common Pitfalls Prevented

| Pitfall | Prevention |
|---------|-----------|
| Circular validation | Methodology validator detects, requires independent ground truth |
| Unvalidated measures | ValidatedMeasure blocks usage until validated |
| P-hacking | Pre-specified analysis plan enforced |
| HARKing | Hypotheses documented before data collection |
| Overclaiming | Review stage checks interpretation |
| Non-reproducible | Reproducibility review with independent verification |
| Cherry-picking | All results must be reported |
| Missing effect sizes | Analysis skill requires them |

## Final Checklist

Before claiming research is complete:

- [ ] All 5 phases completed
- [ ] All quality gates passed
- [ ] All measures validated against ground truth
- [ ] Pre-specified analysis plan followed
- [ ] Effect sizes with CIs reported
- [ ] All results reported (not just significant)
- [ ] Limitations honestly acknowledged
- [ ] No overclaiming in interpretation
- [ ] Code publicly available
- [ ] Data publicly available or access described
- [ ] Independent reproduction successful
- [ ] All reviewers signed off

**If ANY checkbox is unchecked, research is NOT ready for publication.**
