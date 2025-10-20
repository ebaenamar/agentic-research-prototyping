# Agent-Based Research System

## Overview

Sistema de 4 agentes especializados que trabajan en secuencia para investigación rigurosa en foundational models.

```
┌─────────────────────────────────────────────────────────────────┐
│                    RESEARCH AGENT SYSTEM                         │
│                  4 Specialized Agents                            │
└─────────────────────────────────────────────────────────────────┘

Agent 1: RESEARCH SCOUT
├─ Literature review
├─ Gap identification
└─ Research question formulation
    ↓
Agent 2: METHODOLOGY ARCHITECT
├─ Methodology design
├─ Validation strategy
├─ Ground truth planning
└─ Statistical analysis plan
    ↓
Agent 3: EXPERIMENT EXECUTOR
├─ Implementation
├─ Validation execution
├─ Experiment running
└─ Data collection
    ↓
Agent 4: RESULTS ANALYST & REVIEWER
├─ Statistical analysis
├─ Interpretation
├─ Multi-stage review
└─ Publication preparation
```

## Agent Roles

### Agent 1: Research Scout 🔍
**Responsibility:** Find what to research

**Skills:**
- `literature-review-skill`
- `validation-without-humans-skill` (for gap validation)

**Input:** Research interest
**Output:** Validated research questions

**Capabilities:**
- Systematic literature search
- Critical paper analysis
- Gap identification and validation
- Research question formulation

**Workflow:**
1. Define scope
2. Search systematically
3. Analyze papers
4. Identify gaps
5. Validate gaps (genuine, significant, feasible, novel)
6. Formulate research questions

**Handoff to Agent 2:** Research questions + gap analysis

---

### Agent 2: Methodology Architect 🏗️
**Responsibility:** Design how to research

**Skills:**
- `research-methodology-validator`
- `validation-without-humans-skill`

**Input:** Research questions
**Output:** Validated methodology + validation plan

**Capabilities:**
- Construct definition
- Ground truth planning (expert or alternative)
- Validation strategy design (prevents circular logic)
- Statistical analysis plan (pre-specified)
- Reproducibility planning

**Workflow:**
1. Define constructs (theoretical + operational)
2. Decide validation approach:
   - Can get experts? → Expert annotation plan
   - Cannot? → Alternative validation strategy
3. Design validation (ensure independence)
4. Pre-specify statistical analysis
5. Plan reproducibility
6. Run methodology audit (detect circular logic)

**Handoff to Agent 3:** Methodology design + validation plan + statistical plan

---

### Agent 3: Experiment Executor ⚙️
**Responsibility:** Execute research

**Skills:**
- `experiment-design-skill`
- `research-methodology-validator` (ValidatedMeasure framework)
- `validation-without-humans-skill` (for validation execution)

**Input:** Methodology design
**Output:** Validated data + experimental results

**Capabilities:**
- Ground truth collection (expert or alternative)
- Measure validation (blocks usage until validated)
- Experiment design and implementation
- Quality-controlled execution
- Data verification

**Workflow:**
1. Collect ground truth:
   - Expert path: Recruit experts, pilot, full annotation
   - Alternative path: Behavioral/comparative/crowdsourced/hybrid
2. Implement measures (ValidatedMeasure framework)
3. Validate measures (F1≥0.7 or equivalent)
4. Design experiments (conditions, controls, randomization)
5. Pilot run
6. Full execution with quality monitoring
7. Verify and clean data

**Handoff to Agent 4:** Validated data + experimental results + validation reports

---

### Agent 4: Results Analyst & Reviewer 📊
**Responsibility:** Analyze and validate research

**Skills:**
- `results-analysis-skill`
- `research-review-skill`

**Input:** Experimental data
**Output:** Publication-ready research

**Capabilities:**
- Statistical analysis (pre-specified plan)
- Effect sizes with CIs
- Honest interpretation
- Multi-stage review
- Independent verification
- Publication preparation

**Workflow:**
1. Load pre-specified analysis plan
2. Check assumptions
3. Run primary and secondary analyses
4. Calculate effect sizes with CIs
5. Multiple comparison correction
6. Sensitivity analysis
7. Honest interpretation
8. Multi-stage review:
   - Methodology review
   - Implementation review
   - Results review
   - Contribution review
   - Reproducibility review
9. Iterate until approved
10. Final approval

**Output:** Publication-ready research

---

## Agent Communication Protocol

### Handoff Structure

```python
class AgentHandoff:
    """
    Standard handoff between agents
    """
    def __init__(self, from_agent, to_agent, data, status):
        self.from_agent = from_agent
        self.to_agent = to_agent
        self.data = data
        self.status = status
        self.timestamp = datetime.now()
        self.quality_checks = {}
    
    def validate_handoff(self):
        """
        Ensure handoff meets quality gates
        """
        if self.from_agent == "Research Scout":
            return self._validate_scout_output()
        elif self.from_agent == "Methodology Architect":
            return self._validate_architect_output()
        elif self.from_agent == "Experiment Executor":
            return self._validate_executor_output()
        
    def _validate_scout_output(self):
        """Scout → Architect handoff validation"""
        required = [
            'research_questions',
            'gap_analysis',
            'literature_synthesis',
            'contribution_statement'
        ]
        return all(k in self.data for k in required)
    
    def _validate_architect_output(self):
        """Architect → Executor handoff validation"""
        required = [
            'methodology_design',
            'validation_plan',
            'statistical_analysis_plan',
            'reproducibility_plan'
        ]
        checks = [
            self.data.get('circular_logic_check') == 'passed',
            self.data.get('validation_strategy') in ['expert', 'alternative'],
            self.data.get('statistical_plan_prespecified') == True
        ]
        return all(k in self.data for k in required) and all(checks)
    
    def _validate_executor_output(self):
        """Executor → Analyst handoff validation"""
        required = [
            'experimental_data',
            'validation_reports',
            'quality_control_reports'
        ]
        checks = [
            self.data.get('all_measures_validated') == True,
            self.data.get('data_verified') == True,
            self.data.get('pilot_successful') == True
        ]
        return all(k in self.data for k in required) and all(checks)
```

---

## Agent Orchestration

### Sequential Workflow

```python
class ResearchOrchestrator:
    """
    Orchestrates the 4-agent research workflow
    """
    
    def __init__(self):
        self.agents = {
            'scout': ResearchScout(),
            'architect': MethodologyArchitect(),
            'executor': ExperimentExecutor(),
            'analyst': ResultsAnalyst()
        }
        self.current_phase = None
        self.handoffs = []
    
    def run_research_workflow(self, research_interest):
        """
        Run complete research workflow
        """
        
        # Phase 1: Research Scout
        print("=" * 80)
        print("PHASE 1: RESEARCH SCOUT")
        print("=" * 80)
        
        scout_output = self.agents['scout'].execute(
            input_data={'research_interest': research_interest}
        )
        
        handoff_1 = AgentHandoff(
            from_agent='Research Scout',
            to_agent='Methodology Architect',
            data=scout_output,
            status='pending'
        )
        
        if not handoff_1.validate_handoff():
            raise ValueError("Scout output incomplete. Cannot proceed.")
        
        handoff_1.status = 'approved'
        self.handoffs.append(handoff_1)
        
        # Phase 2: Methodology Architect
        print("\n" + "=" * 80)
        print("PHASE 2: METHODOLOGY ARCHITECT")
        print("=" * 80)
        
        architect_output = self.agents['architect'].execute(
            input_data=scout_output
        )
        
        handoff_2 = AgentHandoff(
            from_agent='Methodology Architect',
            to_agent='Experiment Executor',
            data=architect_output,
            status='pending'
        )
        
        if not handoff_2.validate_handoff():
            raise ValueError("Architect output incomplete. Cannot proceed.")
        
        handoff_2.status = 'approved'
        self.handoffs.append(handoff_2)
        
        # Phase 3: Experiment Executor
        print("\n" + "=" * 80)
        print("PHASE 3: EXPERIMENT EXECUTOR")
        print("=" * 80)
        
        executor_output = self.agents['executor'].execute(
            input_data=architect_output
        )
        
        handoff_3 = AgentHandoff(
            from_agent='Experiment Executor',
            to_agent='Results Analyst',
            data=executor_output,
            status='pending'
        )
        
        if not handoff_3.validate_handoff():
            raise ValueError("Executor output incomplete. Cannot proceed.")
        
        handoff_3.status = 'approved'
        self.handoffs.append(handoff_3)
        
        # Phase 4: Results Analyst & Reviewer
        print("\n" + "=" * 80)
        print("PHASE 4: RESULTS ANALYST & REVIEWER")
        print("=" * 80)
        
        final_output = self.agents['analyst'].execute(
            input_data=executor_output
        )
        
        # Final validation
        if final_output['status'] != 'approved_for_publication':
            print("\n⚠️  Research not yet ready for publication")
            print("Issues to address:")
            for issue in final_output['remaining_issues']:
                print(f"  - {issue}")
            return None
        
        print("\n" + "=" * 80)
        print("✓ RESEARCH COMPLETE AND APPROVED")
        print("=" * 80)
        
        return final_output
```

---

## Agent Implementation

### Agent 1: Research Scout

```python
class ResearchScout:
    """
    Agent 1: Literature review and gap identification
    """
    
    def __init__(self):
        self.skills = [
            'literature-review-skill',
            'validation-without-humans-skill'
        ]
        self.name = "Research Scout"
    
    def execute(self, input_data):
        """
        Execute literature review and gap identification
        """
        research_interest = input_data['research_interest']
        
        # Step 1: Define scope
        scope = self.define_scope(research_interest)
        
        # Step 2: Systematic search
        papers = self.systematic_search(scope)
        
        # Step 3: Screen and analyze
        analyzed_papers = self.analyze_papers(papers)
        
        # Step 4: Synthesize
        synthesis = self.synthesize_literature(analyzed_papers)
        
        # Step 5: Identify gaps
        gaps = self.identify_gaps(synthesis)
        
        # Step 6: Validate gaps
        validated_gaps = self.validate_gaps(gaps)
        
        # Step 7: Formulate research questions
        research_questions = self.formulate_questions(validated_gaps)
        
        return {
            'research_questions': research_questions,
            'gap_analysis': validated_gaps,
            'literature_synthesis': synthesis,
            'contribution_statement': self.generate_contribution_statement(
                research_questions, validated_gaps
            ),
            'key_papers': analyzed_papers[:20]  # Top 20
        }
    
    def validate_gaps(self, gaps):
        """
        Validate that gaps are genuine, significant, feasible, novel
        """
        validated = []
        
        for gap in gaps:
            validation = {
                'gap': gap,
                'genuine': self.check_genuine(gap),
                'significant': self.check_significant(gap),
                'feasible': self.check_feasible(gap),
                'novel': self.check_novel(gap)
            }
            
            if all([
                validation['genuine'],
                validation['significant'],
                validation['feasible'],
                validation['novel']
            ]):
                validated.append(validation)
        
        return validated
```

### Agent 2: Methodology Architect

```python
class MethodologyArchitect:
    """
    Agent 2: Methodology design and validation planning
    """
    
    def __init__(self):
        self.skills = [
            'research-methodology-validator',
            'validation-without-humans-skill'
        ]
        self.name = "Methodology Architect"
    
    def execute(self, input_data):
        """
        Design methodology and validation strategy
        """
        research_questions = input_data['research_questions']
        
        # Step 1: Define constructs
        constructs = self.define_constructs(research_questions)
        
        # Step 2: Decide validation approach
        validation_approach = self.decide_validation_approach()
        
        if validation_approach == 'expert':
            validation_plan = self.plan_expert_annotation(constructs)
        else:
            validation_plan = self.plan_alternative_validation(constructs)
        
        # Step 3: Design validation strategy (ensure no circular logic)
        validation_strategy = self.design_validation_strategy(
            constructs, validation_plan
        )
        
        # Step 4: Check for circular logic
        circular_check = self.check_circular_logic(validation_strategy)
        
        if circular_check['has_circular_logic']:
            raise ValueError(
                f"Circular logic detected: {circular_check['issues']}\n"
                f"Redesign validation to be independent."
            )
        
        # Step 5: Pre-specify statistical analysis
        statistical_plan = self.prespecify_statistical_analysis(
            research_questions, constructs
        )
        
        # Step 6: Plan reproducibility
        reproducibility_plan = self.plan_reproducibility()
        
        return {
            'methodology_design': {
                'constructs': constructs,
                'validation_approach': validation_approach,
                'validation_strategy': validation_strategy
            },
            'validation_plan': validation_plan,
            'statistical_analysis_plan': statistical_plan,
            'reproducibility_plan': reproducibility_plan,
            'circular_logic_check': 'passed',
            'validation_strategy': validation_approach,
            'statistical_plan_prespecified': True
        }
    
    def decide_validation_approach(self):
        """
        Decide between expert annotation or alternative validation
        """
        # Interactive decision
        print("\nValidation Approach Decision:")
        print("1. Can you get expert annotations?")
        print("   - Budget: $3k-9k available?")
        print("   - Time: 2-3 months available?")
        print("   - Access: ≥3 experts accessible?")
        
        response = input("\nCan you get expert annotations? (yes/no): ")
        
        if response.lower() == 'yes':
            return 'expert'
        else:
            print("\nAlternative validation strategies:")
            print("1. Behavioral ground truth")
            print("2. Comparative validation")
            print("3. Crowdsourced validation")
            print("4. Hybrid approach (RECOMMENDED)")
            print("5. Multiple strategies (BEST)")
            
            choice = input("\nSelect strategy (1-5): ")
            
            strategies = {
                '1': 'behavioral',
                '2': 'comparative',
                '3': 'crowdsourced',
                '4': 'hybrid',
                '5': 'multiple'
            }
            
            return strategies.get(choice, 'hybrid')
    
    def check_circular_logic(self, validation_strategy):
        """
        Check for circular logic in validation
        """
        from scripts.methodology_auditor import CircularValidationDetector
        
        detector = CircularValidationDetector()
        
        # Check independence
        is_independent, message = detector.check_independence(
            measure_method=validation_strategy['measure_method'],
            ground_truth_method=validation_strategy['ground_truth_method']
        )
        
        if not is_independent:
            return {
                'has_circular_logic': True,
                'issues': [message]
            }
        
        return {
            'has_circular_logic': False,
            'issues': []
        }
```

### Agent 3: Experiment Executor

```python
class ExperimentExecutor:
    """
    Agent 3: Implementation, validation, and execution
    """
    
    def __init__(self):
        self.skills = [
            'experiment-design-skill',
            'research-methodology-validator',
            'validation-without-humans-skill'
        ]
        self.name = "Experiment Executor"
    
    def execute(self, input_data):
        """
        Execute validation and experiments
        """
        methodology = input_data['methodology_design']
        validation_plan = input_data['validation_plan']
        
        # Step 1: Collect ground truth
        if methodology['validation_approach'] == 'expert':
            ground_truth = self.collect_expert_annotations(validation_plan)
        else:
            ground_truth = self.execute_alternative_validation(validation_plan)
        
        # Step 2: Implement measures
        measures = self.implement_measures(methodology['constructs'])
        
        # Step 3: Validate measures (BLOCKS until validated)
        validation_reports = {}
        for measure_name, measure in measures.items():
            print(f"\nValidating measure: {measure_name}")
            
            validation_report = measure.validate_against_ground_truth(
                ground_truth[measure_name]
            )
            
            if not measure.is_validated:
                raise ValueError(
                    f"Measure {measure_name} failed validation.\n"
                    f"F1={validation_report.f1:.3f} (threshold: 0.7)\n"
                    f"Cannot proceed with unvalidated measure."
                )
            
            validation_reports[measure_name] = validation_report
            print(f"✓ {measure_name} validated (F1={validation_report.f1:.3f})")
        
        # Step 4: Design experiments
        experiment_design = self.design_experiments(
            methodology, measures
        )
        
        # Step 5: Pilot run
        pilot_results = self.run_pilot(experiment_design)
        
        if not pilot_results['successful']:
            raise ValueError(
                f"Pilot run failed: {pilot_results['issues']}\n"
                f"Fix issues before full experiment."
            )
        
        # Step 6: Full execution
        experimental_data = self.run_full_experiment(experiment_design)
        
        # Step 7: Verify data
        verification = self.verify_data(experimental_data)
        
        return {
            'experimental_data': experimental_data,
            'validation_reports': validation_reports,
            'quality_control_reports': verification,
            'all_measures_validated': True,
            'data_verified': True,
            'pilot_successful': True
        }
    
    def execute_alternative_validation(self, validation_plan):
        """
        Execute alternative validation strategy
        """
        strategy = validation_plan['strategy']
        
        if strategy == 'behavioral':
            return self.behavioral_validation(validation_plan)
        elif strategy == 'comparative':
            return self.comparative_validation(validation_plan)
        elif strategy == 'crowdsourced':
            return self.crowdsourced_validation(validation_plan)
        elif strategy == 'hybrid':
            return self.hybrid_validation(validation_plan)
        elif strategy == 'multiple':
            return self.multiple_strategy_validation(validation_plan)
```

### Agent 4: Results Analyst & Reviewer

```python
class ResultsAnalyst:
    """
    Agent 4: Analysis, interpretation, and review
    """
    
    def __init__(self):
        self.skills = [
            'results-analysis-skill',
            'research-review-skill'
        ]
        self.name = "Results Analyst & Reviewer"
    
    def execute(self, input_data):
        """
        Analyze results and conduct multi-stage review
        """
        experimental_data = input_data['experimental_data']
        validation_reports = input_data['validation_reports']
        
        # Step 1: Load pre-specified analysis plan
        analysis_plan = self.load_analysis_plan()
        
        # Step 2: Statistical analysis
        results = self.analyze_results(experimental_data, analysis_plan)
        
        # Step 3: Interpretation
        interpretation = self.interpret_results(results)
        
        # Step 4: Multi-stage review
        review_results = self.multi_stage_review({
            'methodology': input_data.get('methodology_design'),
            'implementation': input_data.get('experiment_design'),
            'results': results,
            'interpretation': interpretation,
            'validation_reports': validation_reports
        })
        
        # Step 5: Check if approved
        if review_results['all_stages_approved']:
            return {
                'status': 'approved_for_publication',
                'results': results,
                'interpretation': interpretation,
                'review_reports': review_results,
                'publication_package': self.prepare_publication_package(
                    results, interpretation, review_results
                )
            }
        else:
            return {
                'status': 'revisions_needed',
                'results': results,
                'interpretation': interpretation,
                'review_reports': review_results,
                'remaining_issues': review_results['issues']
            }
    
    def multi_stage_review(self, research_package):
        """
        Conduct 5-stage review process
        """
        reviews = {}
        
        # Stage 1: Methodology review
        reviews['methodology'] = self.review_methodology(
            research_package['methodology']
        )
        
        # Stage 2: Implementation review
        reviews['implementation'] = self.review_implementation(
            research_package['implementation']
        )
        
        # Stage 3: Results review
        reviews['results'] = self.review_results(
            research_package['results']
        )
        
        # Stage 4: Contribution review
        reviews['contribution'] = self.review_contribution(
            research_package
        )
        
        # Stage 5: Reproducibility review
        reviews['reproducibility'] = self.review_reproducibility(
            research_package
        )
        
        # Check if all approved
        all_approved = all(
            r['status'] == 'approved' for r in reviews.values()
        )
        
        # Collect issues
        issues = []
        for stage, review in reviews.items():
            if review['status'] != 'approved':
                issues.extend([
                    f"[{stage}] {issue}" for issue in review['issues']
                ])
        
        return {
            'reviews': reviews,
            'all_stages_approved': all_approved,
            'issues': issues
        }
```

---

## Usage Example

```python
# Initialize orchestrator
orchestrator = ResearchOrchestrator()

# Run complete research workflow
research_interest = "Self-correction mechanisms in large language models"

final_output = orchestrator.run_research_workflow(research_interest)

if final_output:
    print("\n✓ Research approved for publication!")
    print(f"Publication package: {final_output['publication_package']}")
else:
    print("\n⚠️ Research needs revisions")
```

---

## Agent Interaction Diagram

```
┌──────────────────┐
│ Research Scout   │
│ 🔍               │
│                  │
│ • Literature     │
│ • Gaps           │
│ • Questions      │
└────────┬─────────┘
         │ Handoff 1: Research Questions
         ▼
┌──────────────────┐
│ Methodology      │
│ Architect 🏗️     │
│                  │
│ • Constructs     │
│ • Validation     │
│ • Stats plan     │
└────────┬─────────┘
         │ Handoff 2: Methodology + Validation Plan
         ▼
┌──────────────────┐
│ Experiment       │
│ Executor ⚙️      │
│                  │
│ • Ground truth   │
│ • Validation     │
│ • Experiments    │
└────────┬─────────┘
         │ Handoff 3: Validated Data + Results
         ▼
┌──────────────────┐
│ Results Analyst  │
│ & Reviewer 📊    │
│                  │
│ • Analysis       │
│ • Review         │
│ • Publication    │
└────────┬─────────┘
         │
         ▼
    Publication
```

---

## Benefits of 4-Agent System

### 1. Clear Separation of Concerns
- Each agent has specific responsibility
- No overlap or confusion
- Easy to understand and maintain

### 2. Manageable Complexity
- 4 agents (not 10+)
- Each agent uses 1-2 skills
- Simple sequential workflow

### 3. Quality Gates at Handoffs
- Each handoff validated
- Cannot proceed with incomplete work
- Catches issues early

### 4. Flexible Validation
- Agent 2 decides validation approach
- Agent 3 executes chosen approach
- Handles expert or alternative validation

### 5. Comprehensive Review
- Agent 4 does all review stages
- Single agent ensures consistency
- Iterative improvement built-in

---

## Comparison to Alternatives

### Too Many Agents (10+)
❌ Complex coordination
❌ Confusing handoffs
❌ Hard to maintain

### Too Few Agents (1-2)
❌ Agents do too much
❌ Hard to specialize
❌ Difficult to debug

### 4 Agents (This System)
✅ Clear responsibilities
✅ Manageable complexity
✅ Easy coordination
✅ Specialized but not fragmented

---

## Summary

### 4 Specialized Agents

1. **Research Scout** 🔍
   - Find what to research
   - Output: Research questions

2. **Methodology Architect** 🏗️
   - Design how to research
   - Output: Methodology + validation plan

3. **Experiment Executor** ⚙️
   - Execute research
   - Output: Validated data

4. **Results Analyst & Reviewer** 📊
   - Analyze and validate
   - Output: Publication-ready research

### Key Features

- **Sequential workflow** (clear progression)
- **Quality gates** (validated handoffs)
- **Flexible validation** (expert or alternative)
- **Comprehensive review** (5 stages in Agent 4)
- **Manageable** (4 agents, not 10+)

### Timeline

- Agent 1: 2-4 weeks
- Agent 2: 2-3 weeks
- Agent 3: 5-7 weeks (includes validation)
- Agent 4: 3-4 weeks (includes review loops)

**Total: 12-18 weeks (3-4.5 months)**
