# Quick Start Guide

Get started with the Agentic Research Prototyping system in 5 steps.

## Step 1: Understand the System (15 minutes)

Read these in order:

1. **[README.md](README.md)** - System overview
2. **[AGENT_SYSTEM.md](docs/AGENT_SYSTEM.md)** - How the 4 agents work together
3. **[RESEARCH_WORKFLOW.md](docs/RESEARCH_WORKFLOW.md)** - Complete workflow

**Key Takeaway:** 4 agents work sequentially, each with quality gates.

---

## Step 2: Choose Your Starting Point

### Option A: New Research Project

Start from scratch with a research interest:

1. Use **Agent 1: Research Scout** to find gaps
2. Follow the complete workflow

**Go to:** [Research Scout Agent](agents/research-scout-agent.md)

### Option B: Existing Project (Need Validation)

You have measures but need to validate them:

1. Check if you can get expert annotations
2. If not, choose alternative validation strategy
3. Use **Agent 3: Experiment Executor** for validation

**Go to:** [VALIDATION_OPTIONS.md](docs/VALIDATION_OPTIONS.md)

### Option C: Have Data (Need Analysis)

You have validated data and need analysis:

1. Ensure you have pre-specified analysis plan
2. Use **Agent 4: Results Analyst & Reviewer**

**Go to:** [Results Analyst Agent](agents/results-analyst-reviewer-agent.md)

---

## Step 3: Check for Common Issues (10 minutes)

### Do You Have Circular Logic?

**Test:** Is your validation method the same as your measurement method?

- ❌ **Bad:** "We validate our pattern-matching bias detector by checking if it finds patterns"
- ✅ **Good:** "We validate our bias detector against independent expert annotations"

**If you have circular logic:**
- Read: [Research Methodology Validator](skills/research-methodology-validator/SKILL.md)
- Use: Circular logic detection tools
- Redesign: Validation must be independent

### Are Your Measures Validated?

**Test:** Do you have validation metrics (F1, κ, correlation)?

- ❌ **Bad:** "Our measure detects bias" (no validation)
- ✅ **Good:** "Our measure achieves F1=0.85 against expert annotations"

**If measures not validated:**
- Read: [VALIDATION_OPTIONS.md](docs/VALIDATION_OPTIONS.md)
- Choose: Expert or alternative validation
- Validate: Before using measures

### Is Your Analysis Pre-specified?

**Test:** Did you write your analysis plan before seeing data?

- ❌ **Bad:** "We tried different tests and report the significant ones"
- ✅ **Good:** "We pre-specified all analyses on [date] before data collection"

**If not pre-specified:**
- Read: [Results Analysis Skill](skills/results-analysis-skill/SKILL.md)
- Mark: Current analyses as exploratory
- Pre-specify: Future analyses

---

## Step 4: Use the Appropriate Agent (varies)

### Agent 1: Research Scout 🔍

**When:** Starting new research
**Input:** Research interest
**Output:** Validated research questions
**Time:** 2-4 weeks

**Workflow:**
1. Define scope
2. Systematic search (100+ papers)
3. Identify and validate gaps
4. Formulate research questions

**Read:** [Research Scout Agent](agents/research-scout-agent.md)

### Agent 2: Methodology Architect 🏗️

**When:** Have research questions, need methodology
**Input:** Research questions
**Output:** Methodology + validation plan
**Time:** 2-3 weeks

**Workflow:**
1. Define constructs
2. Decide: Expert or alternative validation
3. Check for circular logic
4. Pre-specify statistical analysis

**Read:** [Methodology Architect Agent](agents/methodology-architect-agent.md)

### Agent 3: Experiment Executor ⚙️

**When:** Have methodology, need to execute
**Input:** Methodology + validation plan
**Output:** Validated data
**Time:** 5-7 weeks

**Workflow:**
1. Collect ground truth
2. Validate measures (blocks until validated)
3. Run experiments
4. Verify data

**Read:** [Experiment Executor Agent](agents/experiment-executor-agent.md)

### Agent 4: Results Analyst & Reviewer 📊

**When:** Have validated data, need analysis
**Input:** Experimental data
**Output:** Publication-ready research
**Time:** 3-4 weeks

**Workflow:**
1. Follow pre-specified analysis plan
2. Calculate effect sizes with CIs
3. Interpret honestly
4. Multi-stage review (5 stages)

**Read:** [Results Analyst & Reviewer Agent](agents/results-analyst-reviewer-agent.md)

---

## Step 5: Pass Quality Gates

Each phase has mandatory quality gates. You cannot proceed without passing.

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

---

## Common Scenarios

### Scenario 1: "I can't get expert annotations"

**Solution:** Use alternative validation

1. Read [VALIDATION_OPTIONS.md](docs/VALIDATION_OPTIONS.md)
2. Choose strategy:
   - **Behavioral** (outcomes as validation)
   - **Comparative** (vs. established measures)
   - **Crowdsourced** (many non-experts)
   - **Hybrid** (small expert + large behavioral) ⭐ Recommended
   - **Multiple** (combine 2-3 strategies) ⭐ Best
3. Document limitations honestly
4. State confidence level (MEDIUM vs. HIGH)

### Scenario 2: "My validation failed"

**Possible reasons:**
- Measure implementation has issues
- Ground truth quality insufficient
- Construct definition unclear
- Threshold too high

**Solutions:**
1. Improve measure implementation
2. Collect better ground truth
3. Refine construct definition
4. If all else fails, reconsider construct

**Do NOT:**
- Lower thresholds arbitrarily
- Use unvalidated measures
- Skip validation

### Scenario 3: "My results aren't significant"

**This is OK!** Negative results are valid.

**Do:**
- Report honestly
- Calculate effect sizes anyway
- Discuss why (power? no effect?)
- Suggest future work

**Do NOT:**
- P-hack (try different tests until significant)
- HARKing (pretend you predicted this)
- Hide negative results
- Overclaim from exploratory analyses

### Scenario 4: "The review found issues"

**This is normal!** Iterate until resolved.

**Process:**
1. Review identifies issues
2. You fix issues
3. Re-review
4. Repeat until approved

**Common issues:**
- Circular logic → Redesign validation
- Missing effect sizes → Calculate them
- Overclaiming → Revise interpretation
- Not reproducible → Add documentation

---

## Next Steps

After completing the quick start:

1. **Deep dive** into relevant agent skills
2. **Use the checklists** in each skill
3. **Follow quality gates** strictly
4. **Document everything** for reproducibility
5. **Be honest** about limitations

---

## Need Help?

- **Documentation:** Check [docs/](docs/) folder
- **Specific skills:** Check [skills/](skills/) folder
- **Issues:** Open a GitHub issue
- **Questions:** Start a discussion

---

## Timeline Expectations

**Minimum viable research:** 12 weeks (3 months)

**Realistic timeline:** 16 weeks (4 months)

**High-quality research:** 18 weeks (4.5 months)

**Don't rush.** Rigorous research takes time.

---

## Success Criteria

Your research is ready for publication when:

✅ All measures validated (F1≥0.7 or equivalent)
✅ No circular logic detected
✅ Statistical plan pre-specified and followed
✅ Effect sizes with CIs reported
✅ All results reported (not cherry-picked)
✅ Interpretation honest (no overclaiming)
✅ Limitations acknowledged
✅ Fully reproducible
✅ All 5 review stages approved
✅ Independent reproduction successful

**If any item is unchecked, keep working.**

Good luck with your research! 🚀
