# Repository Structure

```
agentic-research-prototyping/
│
├── README.md                    # Main documentation and overview
├── QUICKSTART.md               # Quick start guide (5 steps)
├── CONTRIBUTING.md             # Contribution guidelines
├── LICENSE                     # MIT License
├── .gitignore                  # Git ignore rules
│
├── docs/                       # Core documentation
│   ├── AGENT_SYSTEM.md        # System architecture and agent overview
│   ├── RESEARCH_WORKFLOW.md   # Complete workflow with all phases
│   └── VALIDATION_OPTIONS.md  # Validation strategies when experts unavailable
│
├── agents/                     # Agent skill documents
│   ├── research-scout-agent.md           # Agent 1: Literature review & gaps
│   ├── methodology-architect-agent.md    # Agent 2: Methodology design
│   ├── experiment-executor-agent.md      # Agent 3: Validation & experiments
│   └── results-analyst-reviewer-agent.md # Agent 4: Analysis & review
│
├── skills/                     # Detailed skill implementations
│   ├── literature-review-skill/
│   │   └── SKILL.md           # Systematic literature review
│   │
│   ├── research-methodology-validator/
│   │   ├── SKILL.md           # Main methodology validation skill
│   │   ├── README.md          # Overview
│   │   ├── ground_truth_protocol.md      # Ground truth collection
│   │   ├── validation_checklist.md       # Validation checklist
│   │   ├── statistical_analysis_plan.md  # Statistical planning
│   │   └── scripts/
│   │       ├── validated_measure.py      # ValidatedMeasure framework
│   │       ├── methodology_auditor.py    # Circular logic detection
│   │       └── ground_truth_dataset.py   # Ground truth handling
│   │
│   ├── validation-without-humans-skill/
│   │   └── SKILL.md           # Alternative validation strategies
│   │
│   ├── experiment-design-skill/
│   │   └── SKILL.md           # Rigorous experiment design
│   │
│   ├── results-analysis-skill/
│   │   └── SKILL.md           # Statistical analysis with effect sizes
│   │
│   └── research-review-skill/
│       └── SKILL.md           # Multi-stage review process
│
└── examples/                   # Examples (to be added)
    └── (coming soon)
```

## Key Files

### Getting Started
- **README.md** - Start here for system overview
- **QUICKSTART.md** - 5-step quick start guide
- **docs/AGENT_SYSTEM.md** - Understand the 4-agent architecture

### Core Documentation
- **docs/RESEARCH_WORKFLOW.md** - Complete workflow from start to publication
- **docs/VALIDATION_OPTIONS.md** - What to do when you can't get expert annotations

### Agent Skills
- **agents/research-scout-agent.md** - How to find research gaps
- **agents/methodology-architect-agent.md** - How to design rigorous methodology
- **agents/experiment-executor-agent.md** - How to validate and run experiments
- **agents/results-analyst-reviewer-agent.md** - How to analyze and review

### Detailed Skills
- **skills/research-methodology-validator/** - Prevents circular logic, enforces validation
- **skills/validation-without-humans-skill/** - Alternative validation when experts unavailable
- All other skills provide detailed workflows for each research phase

## Navigation Guide

### I want to...

**Understand the system**
→ README.md → docs/AGENT_SYSTEM.md

**Start a new research project**
→ QUICKSTART.md → agents/research-scout-agent.md

**Design methodology**
→ agents/methodology-architect-agent.md → skills/research-methodology-validator/

**Validate without experts**
→ docs/VALIDATION_OPTIONS.md → skills/validation-without-humans-skill/

**Run experiments**
→ agents/experiment-executor-agent.md → skills/experiment-design-skill/

**Analyze results**
→ agents/results-analyst-reviewer-agent.md → skills/results-analysis-skill/

**Review research quality**
→ skills/research-review-skill/

## File Sizes

- **Documentation:** ~100KB total
- **Skills:** ~200KB total
- **Scripts:** ~50KB total
- **Total:** ~350KB

All text-based, no binary files.

## Dependencies

- Python 3.8+ (for scripts)
- Standard libraries only (no external dependencies for core functionality)
- Optional: scipy, numpy, sklearn (for statistical analysis examples)

## Updates

This structure is designed to be:
- **Modular** - Each component independent
- **Extensible** - Easy to add new skills/agents
- **Clear** - Obvious where everything is
- **Maintainable** - Simple to update

Last updated: October 2025
