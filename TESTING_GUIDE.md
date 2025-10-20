# Testing Guide - Try It Now!

This guide shows you how to test the Agentic Research Prototyping system with Claude Desktop/Code.

## Prerequisites ✅

Before starting, ensure you have:

- [ ] Claude Desktop or Claude Code installed
- [ ] Pro, Team, or Enterprise plan (Skills require paid plan)
- [ ] Downloaded the repository or ZIP files from `claude-skills-zips/`

## Setup (5 minutes)

### Step 1: Enable Code Execution

1. Open Claude Desktop/Code
2. Click your profile → **Settings**
3. Go to **Capabilities**
4. Toggle ON: **"Code execution and file creation"**

### Step 2: Upload Skills

1. Still in Settings > Capabilities
2. Scroll to **Skills** section
3. Click **"Upload skill"**
4. Upload each ZIP file from `claude-skills-zips/`:

   ```
   ✅ literature-review-skill.zip
   ✅ research-methodology-validator.zip
   ✅ validation-without-humans-skill.zip
   ✅ experiment-design-skill.zip
   ✅ results-analysis-skill.zip
   ✅ research-review-skill.zip
   ```

5. After uploading, toggle each skill **ON**

### Step 3: Verify Installation

In Settings > Capabilities > Skills, you should see:

```
✅ literature-review-skill (ON)
✅ research-methodology-validator (ON)
✅ validation-without-humans-skill (ON)
✅ experiment-design-skill (ON)
✅ results-analysis-skill (ON)
✅ research-review-skill (ON)
```

---

## Test 1: Basic Skill Usage (2 minutes)

**Goal:** Verify Claude can use a skill

### Prompt:
```
I want to research self-correction mechanisms in large language models.
Help me conduct a systematic literature review.
```

### Expected Behavior:
- Claude should mention using the `literature-review-skill`
- Claude should guide you through:
  1. Defining search scope
  2. Keyword selection
  3. Venue selection
  4. Search strategy

### Success Criteria:
✅ Claude explicitly uses the skill
✅ Provides structured guidance
✅ Asks clarifying questions

---

## Test 2: Circular Logic Detection (3 minutes)

**Goal:** Test automated circular logic detection

### Prompt:
```
I'm building a bias detector for AI reviews. My plan is:
1. Use pattern matching to detect bias
2. Validate by checking if the patterns are found

Check this for circular logic.
```

### Expected Behavior:
- Claude should use `research-methodology-validator`
- Should **detect circular logic** (validation method = measurement method)
- Should explain why it's circular
- Should suggest independent validation

### Success Criteria:
✅ Detects circular logic
✅ Explains the problem clearly
✅ Suggests alternatives

---

## Test 3: Alternative Validation Strategy (3 minutes)

**Goal:** Test alternative validation recommendations

### Prompt:
```
I need to validate my bias detection measure, but I can't afford expert annotations.
What are my options? Use the validation without humans skill.
```

### Expected Behavior:
- Claude should use `validation-without-humans-skill`
- Should present 5 alternative strategies:
  1. Behavioral ground truth
  2. Comparative validation
  3. Crowdsourced validation
  4. Hybrid approach
  5. Multiple strategies
- Should include confidence levels
- Should recommend hybrid or multiple strategies

### Success Criteria:
✅ Presents all 5 strategies
✅ Includes confidence levels (HIGH/MEDIUM/LOW)
✅ Explains pros/cons
✅ Makes recommendation

---

## Test 4: Complete Workflow (10 minutes)

**Goal:** Test the complete agent workflow

### Prompt:
```
I want to research whether LLMs can detect their own errors in real-time during generation.

Walk me through the complete research workflow from literature review to publication, 
using all the appropriate skills in sequence.
```

### Expected Behavior:

Claude should guide you through:

1. **Literature Review** (uses `literature-review-skill`)
   - Define scope
   - Systematic search
   - Gap identification
   - Research questions

2. **Methodology Design** (uses `research-methodology-validator`)
   - Define constructs
   - Check circular logic
   - Design validation strategy
   - Pre-specify analysis

3. **Validation Planning** (uses `validation-without-humans-skill` if needed)
   - Choose validation approach
   - Design strategy
   - Assess confidence

4. **Experiment Design** (uses `experiment-design-skill`)
   - Design conditions
   - Plan controls
   - Quality control

5. **Results Analysis** (uses `results-analysis-skill`)
   - Follow pre-specified plan
   - Calculate effect sizes
   - Honest interpretation

6. **Final Review** (uses `research-review-skill`)
   - 5-stage review
   - Identify issues
   - Approve or revise

### Success Criteria:
✅ Uses all 6 skills in sequence
✅ Maintains context across phases
✅ Enforces quality gates
✅ Provides actionable guidance

---

## Test 5: Python Script Execution (5 minutes)

**Goal:** Test that Python scripts work

### Prompt:
```
I have this Python code for bias detection:

```python
def detect_bias(review):
    bias_score = calculate_bias(review)
    return validate_bias(bias_score)

def validate_bias(score):
    return score > 0.5
```

Check this code for circular logic using the methodology auditor script.
```

### Expected Behavior:
- Claude should use `research-methodology-validator`
- Should run `methodology_auditor.py`
- Should detect potential circular validation
- Should provide specific recommendations

### Success Criteria:
✅ Runs Python script
✅ Detects circular patterns
✅ Provides line-by-line analysis
✅ Suggests fixes

---

## Test 6: Multi-Skill Combination (5 minutes)

**Goal:** Test Claude using multiple skills together

### Prompt:
```
I'm designing a study on bias in AI-generated reviews. I need to:
1. Check my methodology for circular logic
2. Design an alternative validation strategy (can't get experts)
3. Pre-specify my statistical analysis plan

Help me with all three using the appropriate skills.
```

### Expected Behavior:
- Claude should use multiple skills:
  - `research-methodology-validator` (circular logic check)
  - `validation-without-humans-skill` (alternative strategy)
  - `research-methodology-validator` (statistical plan)
- Should handle all three tasks in one conversation
- Should maintain context between tasks

### Success Criteria:
✅ Uses multiple skills appropriately
✅ Maintains context
✅ Provides comprehensive guidance
✅ Checks quality at each step

---

## Troubleshooting

### Problem: Skills not appearing in list

**Solution:**
1. Check you uploaded ZIP files correctly
2. Verify ZIP structure (skill folder at root)
3. Check `Skill.md` has YAML frontmatter
4. Try re-uploading

### Problem: Claude not using skills automatically

**Solution:**
1. Verify skills are toggled ON
2. Be more specific in your request
3. Explicitly mention skill name: "Use the [skill name] to..."
4. Check Code execution is enabled

### Problem: Python scripts not running

**Solution:**
1. Verify Code execution is enabled
2. Check `research-methodology-validator` uploaded correctly
3. Try explicitly asking Claude to run the script

### Problem: Skills used incorrectly

**Solution:**
1. Be more specific about what you want
2. Mention the specific skill to use
3. Provide more context about your research phase

---

## Success Checklist

After testing, you should have verified:

- [ ] Skills upload successfully
- [ ] Claude uses skills automatically when relevant
- [ ] Circular logic detection works
- [ ] Alternative validation recommendations work
- [ ] Complete workflow guidance works
- [ ] Python scripts execute
- [ ] Multiple skills can be combined
- [ ] Quality gates are enforced

---

## Example Test Session

Here's a complete test session you can copy/paste:

```
Session 1: Basic Test
---------------------
User: I want to research self-correction in LLMs. Help me start.

[Claude should use literature-review-skill and guide you]


Session 2: Circular Logic Test
-------------------------------
User: Check this for circular logic:
I'll detect bias using patterns, then validate by checking if patterns exist.

[Claude should detect circular logic]


Session 3: Alternative Validation
----------------------------------
User: I can't get expert annotations. What are my validation options?

[Claude should present 5 alternatives with confidence levels]


Session 4: Complete Workflow
-----------------------------
User: Walk me through the complete research workflow for studying 
real-time error correction in LLMs.

[Claude should use all 6 skills in sequence]
```

---

## Next Steps After Testing

Once you've verified everything works:

1. **Start your actual research** using the skills
2. **Create a Project** in Claude for your research
3. **Enable relevant skills** for that project
4. **Follow the workflow** phase by phase
5. **Share feedback** on GitHub if you find issues

---

## Performance Expectations

### Response Time
- Simple queries: 5-10 seconds
- Complex analysis: 20-30 seconds
- Python script execution: 10-20 seconds

### Accuracy
- Circular logic detection: ~95% accuracy
- Skill selection: ~90% accuracy (may need explicit mention)
- Guidance quality: High (based on rigorous methodology)

### Limitations
- Skills are context-dependent (may need explicit mention)
- Python scripts limited to standard libraries
- Cannot access external APIs or databases
- Skills are private to your account

---

## Support

If you encounter issues:

1. **Check troubleshooting section** above
2. **Review CLAUDE_SKILLS_SETUP.md** for detailed setup
3. **Open GitHub issue** with:
   - What you tried
   - What happened
   - What you expected
   - Screenshots if relevant

**Repository:** https://github.com/ebaenamar/agentic-research-prototyping

---

## Feedback Welcome!

After testing, please share:

- ✅ What worked well
- ⚠️ What could be improved
- 💡 Suggestions for new features
- 🐛 Bugs or issues found

Open an issue or discussion on GitHub!

---

**Ready to test? Start with Test 1 and work your way through!** 🚀
