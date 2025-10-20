# How to Use with Claude Desktop/Code

This guide shows you how to use the Agentic Research Prototyping system with Claude Desktop or Claude Code using Skills.

## What are Claude Skills?

Skills are custom instructions and tools you can upload to Claude Desktop/Code that teach Claude your specific workflows. Claude automatically uses them when relevant to your task.

## Prerequisites

1. **Claude Desktop or Claude Code** installed
2. **Pro, Team, or Enterprise plan** (Skills require paid plan)
3. **Code execution enabled** in Settings > Capabilities

## Quick Setup (5 minutes)

### Step 1: Enable Skills in Claude

1. Open Claude Desktop/Code
2. Go to **Settings > Capabilities**
3. Enable **"Code execution and file creation"**
4. Scroll to **Skills section**

### Step 2: Download Pre-packaged Skills

We've prepared ready-to-use ZIP files for each skill:

**Download from:** https://github.com/ebaenamar/agentic-research-prototyping/releases

Or create them yourself (see below).

### Step 3: Upload Skills to Claude

1. In Claude Settings > Capabilities > Skills section
2. Click **"Upload skill"**
3. Upload the ZIP files one by one:
   - `literature-review-skill.zip`
   - `research-methodology-validator.zip`
   - `validation-without-humans-skill.zip`
   - `experiment-design-skill.zip`
   - `results-analysis-skill.zip`
   - `research-review-skill.zip`

4. Toggle each skill **ON**

### Step 4: Test It!

Start a new conversation in Claude and try:

```
I want to research self-correction mechanisms in large language models. 
Help me conduct a systematic literature review.
```

Claude will automatically use the `literature-review-skill` and guide you through the process!

---

## Creating Skills Manually

If you want to create the ZIP files yourself:

### For Each Skill Directory

```bash
cd /Users/e.baena/CascadeProjects/agentic-research-prototyping/skills

# Example: Literature Review Skill
cd literature-review-skill
mv SKILL.md Skill.md  # Rename to capital S
zip -r ../literature-review-skill.zip .
cd ..

# Repeat for each skill
```

### Required Structure

Each skill ZIP must have this structure:

```
skill-name.zip
└── skill-name/
    ├── Skill.md (required, with YAML frontmatter)
    ├── README.md (optional)
    └── resources/ (optional)
```

**Important:** 
- File must be named `Skill.md` (capital S)
- Must have YAML frontmatter with `name` and `description`
- ZIP root should contain the skill folder

---

## How to Use the Skills

### Agent-Based Workflow

The skills work together as specialized agents:

#### 1. Starting Research (Research Scout Agent)

**Ask Claude:**
```
I want to research [your topic]. Help me find research gaps.
```

**Claude will use:** `literature-review-skill`

**Output:** Research questions

---

#### 2. Designing Methodology (Methodology Architect Agent)

**Ask Claude:**
```
I have these research questions: [paste questions]
Help me design a rigorous methodology.
```

**Claude will use:** `research-methodology-validator`

**Output:** Methodology + validation plan

**Critical:** Claude will check for circular logic automatically!

---

#### 3. Validation Strategy (When You Can't Get Experts)

**Ask Claude:**
```
I can't get expert annotations for validation. 
What are my alternatives?
```

**Claude will use:** `validation-without-humans-skill`

**Output:** Alternative validation strategies with confidence levels

---

#### 4. Running Experiments (Experiment Executor Agent)

**Ask Claude:**
```
I have my methodology. Help me design and run experiments.
```

**Claude will use:** `experiment-design-skill`

**Output:** Experiment design with quality controls

---

#### 5. Analyzing Results (Results Analyst Agent)

**Ask Claude:**
```
I have experimental data. Help me analyze it rigorously.
```

**Claude will use:** `results-analysis-skill`

**Output:** Statistical analysis with effect sizes and CIs

---

#### 6. Reviewing Research (Final Review)

**Ask Claude:**
```
Review my research for publication readiness.
```

**Claude will use:** `research-review-skill`

**Output:** Multi-stage review report with issues

---

## Example Complete Workflow

### Session 1: Literature Review

```
User: I want to research self-correction in LLMs. Help me start.

Claude: [Uses literature-review-skill]
I'll guide you through a systematic literature review...

[Claude walks you through the complete process]

Result: 3 validated research questions
```

### Session 2: Methodology Design

```
User: Here are my research questions: [paste]
Help me design the methodology.

Claude: [Uses research-methodology-validator]
Let me help you design a rigorous methodology...

[Claude checks for circular logic, designs validation]

Result: Complete methodology without circular logic
```

### Session 3: Validation Planning

```
User: I can't afford expert annotations. What are my options?

Claude: [Uses validation-without-humans-skill]
I understand. Let me present alternative validation strategies...

[Claude presents 5 options with pros/cons]

Result: Hybrid validation strategy (MEDIUM-HIGH confidence)
```

### Session 4: Experiment Execution

```
User: I'm ready to run experiments. Guide me.

Claude: [Uses experiment-design-skill]
Let's design your experiments with proper controls...

[Claude designs experiments, quality checks]

Result: Experiment design with pilot plan
```

### Session 5: Results Analysis

```
User: I have my data. Help me analyze it.

Claude: [Uses results-analysis-skill]
I'll follow your pre-specified analysis plan...

[Claude runs analysis, calculates effect sizes]

Result: Complete statistical analysis with honest interpretation
```

### Session 6: Final Review

```
User: Review my research for publication.

Claude: [Uses research-review-skill]
I'll conduct a comprehensive 5-stage review...

[Claude reviews methodology, implementation, results, contribution, reproducibility]

Result: Approved for publication OR list of revisions needed
```

---

## Advanced Usage

### Combining Skills

Claude can use multiple skills in one conversation:

```
User: I need to validate my bias detection measure, but I can't get experts.
Design an alternative validation strategy and then help me implement it.

Claude: [Uses validation-without-humans-skill + experiment-design-skill]
Let me help you design and implement an alternative validation...
```

### Using Scripts

Some skills include Python scripts:

**research-methodology-validator** includes:
- `validated_measure.py` - Enforces measure validation
- `methodology_auditor.py` - Detects circular logic

Claude can run these automatically when needed!

```
User: Check my code for circular logic.

Claude: [Runs methodology_auditor.py]
I found 2 instances of potential circular logic...
```

---

## Troubleshooting

### Skills Not Appearing

**Problem:** Uploaded skill doesn't show in list

**Solution:**
1. Check ZIP structure (skill folder must be at root)
2. Verify `Skill.md` has correct YAML frontmatter
3. Ensure file is named `Skill.md` (capital S)

### Claude Not Using Skill

**Problem:** Claude doesn't use the skill automatically

**Solution:**
1. Check skill is toggled ON in Settings
2. Make your request more specific
3. Explicitly mention the skill: "Use the literature review skill to..."

### Upload Errors

**Problem:** ZIP file won't upload

**Solution:**
1. Check file size (should be < 10MB)
2. Verify ZIP structure
3. Remove any hidden files (`.DS_Store`, etc.)

### Code Execution Disabled

**Problem:** Skills with scripts don't work

**Solution:**
1. Go to Settings > Capabilities
2. Enable "Code execution and file creation"
3. Restart Claude

---

## Best Practices

### 1. Start Simple

Begin with one skill (e.g., literature-review-skill) and learn how it works before adding more.

### 2. Be Specific

Instead of: "Help me with research"
Try: "Use the literature review skill to help me find gaps in LLM self-correction research"

### 3. Use Projects

For long research projects:
1. Create a Project in Claude
2. Enable relevant skills for that project
3. All context is preserved across sessions

### 4. Follow the Workflow

Use skills in order:
1. Literature Review → 2. Methodology → 3. Validation → 4. Experiments → 5. Analysis → 6. Review

### 5. Check Quality Gates

After each phase, verify you've passed the quality gates before moving to the next skill.

---

## Privacy & Security

- **Custom skills are private** to your account
- Skills can execute code (review scripts before uploading)
- Skills can access files you share with Claude
- Skills cannot access files outside Claude's context

---

## Sharing Skills with Team

If you're on a Team or Enterprise plan:

1. Each team member must upload skills individually
2. Or use the API to deploy skills organization-wide
3. Consider creating a shared GitHub repo for your team's skills

---

## Testing Your Setup

### Quick Test

```
User: I want to research bias in AI-generated reviews. 
Use the research methodology validator to check if my approach has circular logic.

Expected: Claude uses the skill and checks for circular logic
```

### Full Workflow Test

```
User: Walk me through the complete research workflow for studying 
self-correction in LLMs, from literature review to publication.

Expected: Claude uses all 6 skills in sequence, guiding you through each phase
```

---

## Example Prompts

### For Literature Review
```
Use the literature review skill to help me:
1. Define search scope for [topic]
2. Conduct systematic search
3. Identify genuine research gaps
```

### For Methodology Design
```
Use the research methodology validator to:
1. Check my methodology for circular logic
2. Design an independent validation strategy
3. Pre-specify my statistical analysis plan
```

### For Alternative Validation
```
I can't get expert annotations. Use the validation without humans skill to:
1. Recommend the best alternative strategy
2. Assess expected confidence level
3. Document limitations honestly
```

### For Experiment Design
```
Use the experiment design skill to:
1. Design experimental conditions
2. Plan quality control procedures
3. Create a pilot run protocol
```

### For Results Analysis
```
Use the results analysis skill to:
1. Follow my pre-specified analysis plan
2. Calculate effect sizes with confidence intervals
3. Check for overclaiming in my interpretation
```

### For Final Review
```
Use the research review skill to:
1. Conduct all 5 review stages
2. Identify any remaining issues
3. Approve for publication or list revisions needed
```

---

## Next Steps

1. **Upload skills** to Claude Desktop/Code
2. **Test with a simple prompt** to verify they work
3. **Start your research** following the agent workflow
4. **Share feedback** on GitHub if you find issues

---

## Support

- **Documentation:** https://github.com/ebaenamar/agentic-research-prototyping
- **Issues:** https://github.com/ebaenamar/agentic-research-prototyping/issues
- **Claude Skills Help:** https://support.claude.com/en/articles/12512180-using-skills-in-claude

---

## Summary

✅ Upload 6 skills to Claude Desktop/Code
✅ Enable Code execution in Settings
✅ Use skills in sequence for complete workflow
✅ Claude automatically detects when to use each skill
✅ Follow quality gates between phases
✅ Get publication-ready research!

**Ready to start? Upload your first skill and try it out!** 🚀
