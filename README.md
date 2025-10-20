# Agentic Research Prototyping

A comprehensive, rigorous research workflow system for foundational AI models using specialized agents.

## Overview

This system provides a complete workflow from literature review to publication-ready research, preventing common methodological failures like circular logic, unvalidated measures, and non-reproducible results.

### Key Features

- ✅ **4 Specialized Agents** - Clear separation of concerns
- ✅ **Prevents Circular Logic** - Automated detection and blocking
- ✅ **Flexible Validation** - Expert annotation or rigorous alternatives
- ✅ **Pre-specified Analysis** - Prevents p-hacking and HARKing
- ✅ **Multi-stage Review** - 5 comprehensive review stages
- ✅ **Fully Reproducible** - Complete documentation and verification

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    RESEARCH AGENT SYSTEM                         │
│                  4 Specialized Agents                            │
└─────────────────────────────────────────────────────────────────┘

Agent 1: RESEARCH SCOUT 🔍
├─ Literature review
├─ Gap identification
└─ Research question formulation
    ↓
Agent 2: METHODOLOGY ARCHITECT 🏗️
├─ Methodology design
├─ Validation strategy (expert or alternative)
├─ Circular logic detection
└─ Statistical analysis plan
    ↓
Agent 3: EXPERIMENT EXECUTOR ⚙️
├─ Ground truth collection
├─ Measure validation (blocks until validated)
├─ Experiment execution
└─ Quality control
    ↓
Agent 4: RESULTS ANALYST & REVIEWER 📊
├─ Statistical analysis
├─ Honest interpretation
├─ Multi-stage review (5 stages)
└─ Publication preparation
```

## Quick Start

### 1. Understand the System

Read the documentation in order:

1. **[AGENT_SYSTEM.md](docs/AGENT_SYSTEM.md)** - System overview and architecture
2. **[RESEARCH_WORKFLOW.md](docs/RESEARCH_WORKFLOW.md)** - Complete workflow with all phases
3. **[VALIDATION_OPTIONS.md](docs/VALIDATION_OPTIONS.md)** - Validation strategies when experts unavailable

### 2. Review Agent Skills

Each agent has a detailed skill document:

- **[Research Scout Agent](agents/research-scout-agent.md)** - Literature review and gap identification
- **[Methodology Architect Agent](agents/methodology-architect-agent.md)** - Methodology design and validation planning
- **[Experiment Executor Agent](agents/experiment-executor-agent.md)** - Validation execution and experiments
- **[Results Analyst & Reviewer Agent](agents/results-analyst-reviewer-agent.md)** - Analysis and comprehensive review

### 3. Use the Skills

Skills are organized by research phase:

- **[Literature Review Skill](skills/literature-review-skill/)** - Systematic literature search and synthesis
- **[Research Methodology Validator](skills/research-methodology-validator/)** - Prevents circular logic, enforces validation
- **[Validation Without Humans Skill](skills/validation-without-humans-skill/)** - Alternative validation strategies
- **[Experiment Design Skill](skills/experiment-design-skill/)** - Rigorous experiment design
- **[Results Analysis Skill](skills/results-analysis-skill/)** - Statistical analysis with effect sizes
- **[Research Review Skill](skills/research-review-skill/)** - Multi-stage review process

## Timeline

| Phase | Agent | Duration | Output |
|-------|-------|----------|--------|
| 1. Literature Review | Research Scout | 2-4 weeks | Research questions |
| 2. Methodology Design | Methodology Architect | 2-3 weeks | Methodology + validation plan |
| 3. Validation & Experiments | Experiment Executor | 5-7 weeks | Validated data |
| 4. Analysis & Review | Results Analyst & Reviewer | 3-4 weeks | Publication-ready research |

**Total: 12-18 weeks (3-4.5 months)**

## Key Principles

### 1. No Circular Logic

The system automatically detects and prevents circular validation:

```python
# Agent 2: Methodology Architect
circular_check = self.check_circular_logic(validation_strategy)

if circular_check['has_circular_logic']:
    raise ValueError("CANNOT PROCEED - Redesign validation")
```

### 2. Mandatory Validation

All measures must be validated before use:

```python
# Agent 3: Experiment Executor
measure.validate_against_ground_truth(ground_truth)

if not measure.is_validated:
    raise ValueError("Cannot use unvalidated measure")
```

### 3. Pre-specified Analysis

Statistical analysis plan must be written before data collection:

```python
# Agent 2: Methodology Architect
analysis_plan = self.prespecify_statistical_analysis()
# Prevents p-hacking and HARKing
```

### 4. Honest Reporting

All results must be reported, not just significant ones:

```python
# Agent 4: Results Analyst & Reviewer
if self.is_overclaiming(interpretation):
    raise ValueError("Overclaiming detected - revise interpretation")
```

## Validation Strategies

### Expert Annotation (Preferred)

- **Confidence:** HIGH
- **Cost:** $3k-9k
- **Time:** 2-3 months
- **Requirements:** n≥100, ≥3 experts, κ≥0.7

### Alternative Validation (When Experts Unavailable)

1. **Behavioral Ground Truth** - Use actual outcomes (MEDIUM confidence)
2. **Comparative Validation** - Compare to established measures (MEDIUM confidence)
3. **Crowdsourced Validation** - Many non-experts with quality control (MEDIUM confidence)
4. **Hybrid Approach** - Small expert + large behavioral (MEDIUM-HIGH confidence) ⭐ **Recommended**
5. **Multiple Strategies** - Combine 2-3 approaches (MEDIUM-HIGH confidence) ⭐ **Best**

See [VALIDATION_OPTIONS.md](docs/VALIDATION_OPTIONS.md) for complete details.

## Quality Gates

Each phase has mandatory quality gates:

### Gate 1: After Literature Review
- [ ] Comprehensive search completed
- [ ] Gaps validated (genuine, significant, feasible, novel)
- [ ] Research questions formulated

### Gate 2: After Methodology Design
- [ ] Constructs clearly defined
- [ ] Validation strategy independent (NO circular logic)
- [ ] Statistical plan pre-specified

### Gate 3: After Validation & Experiments
- [ ] All measures validated (F1≥0.7 or equivalent)
- [ ] Pilot successful
- [ ] Data verified

### Gate 4: After Analysis & Review
- [ ] Pre-specified plan followed
- [ ] Effect sizes with CIs reported
- [ ] All 5 review stages passed
- [ ] Independent reproduction successful

## Multi-Stage Review

Agent 4 conducts 5 comprehensive review stages:

1. **Methodology Review** - Constructs, validation, circular logic check
2. **Implementation Review** - Code quality, reproducibility
3. **Results Review** - Statistical validity, effect sizes, honest interpretation
4. **Contribution Review** - Novelty, significance, quality
5. **Reproducibility Review** - Independent verification

All stages must be approved before publication.

## Example Usage

```python
# Initialize orchestrator
orchestrator = ResearchOrchestrator()

# Run complete research workflow
research_interest = "Self-correction mechanisms in large language models"

final_output = orchestrator.run_research_workflow(research_interest)

if final_output['status'] == 'approved_for_publication':
    print("✓ Research ready for publication!")
    print(f"Publication package: {final_output['publication_package']}")
else:
    print("⚠️ Revisions needed")
    for issue in final_output['remaining_issues']:
        print(f"  - {issue}")
```

## Documentation Structure

```
agentic-research-prototyping/
├── README.md (this file)
├── docs/
│   ├── AGENT_SYSTEM.md (system architecture)
│   ├── RESEARCH_WORKFLOW.md (complete workflow)
│   └── VALIDATION_OPTIONS.md (validation strategies)
├── agents/
│   ├── research-scout-agent.md
│   ├── methodology-architect-agent.md
│   ├── experiment-executor-agent.md
│   └── results-analyst-reviewer-agent.md
├── skills/
│   ├── literature-review-skill/
│   ├── research-methodology-validator/
│   ├── validation-without-humans-skill/
│   ├── experiment-design-skill/
│   ├── results-analysis-skill/
│   └── research-review-skill/
└── examples/
    └── (coming soon)
```

## Common Pitfalls Prevented

| Pitfall | Prevention |
|---------|-----------|
| Circular validation | Methodology Architect detects, requires independent ground truth |
| Unvalidated measures | Experiment Executor blocks usage until validated |
| P-hacking | Pre-specified analysis plan enforced |
| HARKing | Hypotheses documented before data collection |
| Overclaiming | Results Analyst checks interpretation |
| Non-reproducible | Reproducibility review with independent verification |
| Cherry-picking | All results must be reported |
| Missing effect sizes | Analysis skill requires them |

## Contributing

This system is designed for rigorous research in foundational AI models. Contributions welcome:

- Additional validation strategies
- Example implementations
- Case studies
- Improvements to detection algorithms

## License

MIT License - See LICENSE file for details

## Citation

If you use this system in your research, please cite:

```bibtex
@software{agentic_research_prototyping,
  title = {Agentic Research Prototyping: A Rigorous Workflow for Foundational AI Models},
  author = {Baena, E.},
  year = {2025},
  url = {https://github.com/ebaenamar/agentic-research-prototyping}
}
```

## Contact

For questions or issues, please open a GitHub issue.

---

**Status:** Active Development

**Last Updated:** October 2025
