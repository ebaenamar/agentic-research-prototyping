# Claude Skills - Ready to Upload

These ZIP files are ready to upload to Claude Desktop or Claude Code.

## Quick Start

### 1. Prerequisites
- Claude Desktop or Claude Code installed
- Pro, Team, or Enterprise plan
- Code execution enabled

### 2. Upload Skills

1. Open Claude Desktop/Code
2. Go to **Settings > Capabilities**
3. Enable **"Code execution and file creation"**
4. Scroll to **Skills section**
5. Click **"Upload skill"**
6. Upload each ZIP file:

   - ✅ `literature-review-skill.zip` (4.8K)
   - ✅ `research-methodology-validator.zip` (29K) - includes Python scripts
   - ✅ `validation-without-humans-skill.zip` (8.2K)
   - ✅ `experiment-design-skill.zip` (5.0K)
   - ✅ `results-analysis-skill.zip` (5.9K)
   - ✅ `research-review-skill.zip` (5.2K)

7. Toggle each skill **ON**

### 3. Test It

Start a new conversation:

```
I want to research self-correction in LLMs. 
Help me conduct a systematic literature review.
```

Claude will automatically use the appropriate skill!

## What Each Skill Does

### 📚 literature-review-skill.zip
**When to use:** Starting new research, finding gaps
**What it does:** Systematic literature search, gap identification, research question formulation
**Agent:** Research Scout

### 🏗️ research-methodology-validator.zip
**When to use:** Designing methodology, checking for circular logic
**What it does:** Methodology design, validation planning, circular logic detection
**Agent:** Methodology Architect
**Special:** Includes Python scripts for automated checks

### 🔬 validation-without-humans-skill.zip
**When to use:** Can't get expert annotations
**What it does:** Alternative validation strategies with confidence assessment
**Agent:** Methodology Architect (alternative path)

### ⚙️ experiment-design-skill.zip
**When to use:** Ready to run experiments
**What it does:** Experiment design, quality control, pilot planning
**Agent:** Experiment Executor

### 📊 results-analysis-skill.zip
**When to use:** Have data, need analysis
**What it does:** Statistical analysis, effect sizes, honest interpretation
**Agent:** Results Analyst

### ✅ research-review-skill.zip
**When to use:** Research complete, need review
**What it does:** Multi-stage review (5 stages), publication readiness check
**Agent:** Results Analyst & Reviewer

## Workflow

Use skills in sequence:

```
1. Literature Review (literature-review-skill)
   ↓
2. Methodology Design (research-methodology-validator)
   ↓
3. Validation Strategy (validation-without-humans-skill if needed)
   ↓
4. Experiments (experiment-design-skill)
   ↓
5. Analysis (results-analysis-skill)
   ↓
6. Review (research-review-skill)
```

## Example Prompts

### Starting Research
```
I want to research [topic]. Use the literature review skill to help me find gaps.
```

### Designing Methodology
```
Check my methodology for circular logic using the research methodology validator.
```

### Alternative Validation
```
I can't get expert annotations. What are my validation options?
```

### Running Experiments
```
Help me design experiments with proper controls.
```

### Analyzing Results
```
Analyze my data following the pre-specified plan.
```

### Final Review
```
Review my research for publication readiness.
```

## Troubleshooting

### Skills not appearing?
- Check ZIP uploaded successfully
- Verify skill is toggled ON
- Restart Claude

### Claude not using skill?
- Be more specific in your request
- Explicitly mention the skill name
- Check "Code execution" is enabled

### Upload errors?
- File size should be < 10MB (all are)
- Check internet connection
- Try uploading one at a time

## Full Documentation

See **CLAUDE_SKILLS_SETUP.md** in the repository root for:
- Detailed setup instructions
- Advanced usage examples
- Complete workflow guide
- Best practices
- Privacy & security info

## Support

- **Repository:** https://github.com/ebaenamar/agentic-research-prototyping
- **Issues:** https://github.com/ebaenamar/agentic-research-prototyping/issues
- **Claude Help:** https://support.claude.com/en/articles/12512180-using-skills-in-claude

---

**Ready to start? Upload the skills and try your first prompt!** 🚀
