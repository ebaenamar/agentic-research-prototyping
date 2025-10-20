---
name: literature-review-skill
description: Systematic literature review and gap identification for foundational models research. Guides comprehensive literature search, synthesis, gap analysis, and research question formulation. Ensures gaps are genuine, significant, and lead to meaningful contributions.
---

# Literature Review & Gap Identification

Systematic approach to reviewing literature and identifying genuine research gaps.

## Objectives

1. **Comprehensive Coverage**: Review all relevant work
2. **Critical Analysis**: Evaluate quality and contributions
3. **Gap Identification**: Find genuine, significant gaps
4. **Question Formulation**: Develop answerable research questions

## Workflow

### Step 1: Define Scope

**Questions to Answer:**
- What specific aspect of foundational models?
- What time period? (typically last 2-3 years for fast-moving field)
- What venues? (arXiv, NeurIPS, ICML, ICLR, ACL, etc.)
- What model types? (LLMs, VLMs, multimodal, etc.)

**Output: Scope Document**
```markdown
## Research Scope

**Topic:** [Specific aspect, e.g., "Self-correction in LLMs"]

**Time Period:** [e.g., "2023-2025"]

**Venues:**
- arXiv (cs.CL, cs.LG, cs.AI)
- NeurIPS, ICML, ICLR
- ACL, EMNLP, NAACL
- [Other relevant venues]

**Model Types:**
- Large Language Models (>7B parameters)
- Focus on: [specific architectures/families]

**Exclusions:**
- [What you're NOT covering]
```

### Step 2: Systematic Search

**Search Strategy:**

1. **Keyword Search**
   ```
   Primary keywords: [main topic]
   Secondary keywords: [related concepts]
   Boolean operators: AND, OR, NOT
   ```

2. **Venue Search**
   - Search each venue systematically
   - Use venue-specific search tools
   - Track search date and results count

3. **Citation Tracking**
   - Forward citations (who cited this?)
   - Backward citations (what did they cite?)
   - Use Google Scholar, Semantic Scholar

4. **Author Tracking**
   - Identify key researchers
   - Check their recent work
   - Follow research groups

**Search Documentation:**
```markdown
## Search Log

### Search 1: arXiv
- Date: 2025-10-19
- Query: "self-correction" AND "language model"
- Results: 150 papers
- After filtering: 45 relevant

### Search 2: NeurIPS 2024
- Date: 2025-10-19
- Query: [query]
- Results: [count]
- After filtering: [count]

[Continue for all searches]
```

### Step 3: Paper Screening

**Screening Criteria:**

**Include if:**
- Directly relevant to research scope
- Methodologically sound
- Published in reputable venue or by known researchers
- Sufficient detail to evaluate

**Exclude if:**
- Out of scope
- Methodologically flawed
- Insufficient detail
- Duplicate or superseded work

**Screening Process:**
1. Title screening (quick pass)
2. Abstract screening (relevance check)
3. Full paper screening (detailed evaluation)

**Track Decisions:**
```markdown
## Screening Results

Total papers found: [N]
After title screening: [N]
After abstract screening: [N]
After full screening: [N]

Final papers for review: [N]
```

### Step 4: Paper Analysis

**For Each Paper, Extract:**

1. **Core Contribution**
   - What is the main claim?
   - What is novel?
   - What problem does it solve?

2. **Methodology**
   - What approach is used?
   - Is it validated?
   - What are the limitations?

3. **Results**
   - What are the key findings?
   - Are they reproducible?
   - What is the evidence quality?

4. **Limitations**
   - What do authors acknowledge?
   - What do they miss?
   - What are boundary conditions?

**Paper Summary Template:**
```markdown
## [Paper Title] (Authors, Year)

**Contribution:** [1-2 sentences]

**Methodology:**
- Approach: [description]
- Validation: [how validated]
- Limitations: [key limitations]

**Key Results:**
- Finding 1: [with evidence]
- Finding 2: [with evidence]

**Relevance to Our Work:**
- [How this relates to our research question]

**Quality Assessment:**
- Methodology: [Strong/Adequate/Weak]
- Evidence: [Strong/Adequate/Weak]
- Reproducibility: [High/Medium/Low]

**Citation:** [BibTeX]
```

### Step 5: Synthesis & Categorization

**Organize Papers by:**

1. **Research Questions**
   - What questions do they address?
   - Group papers by question

2. **Methodologies**
   - What approaches are used?
   - Compare and contrast

3. **Findings**
   - What do we know?
   - Where is consensus?
   - Where is disagreement?

4. **Limitations**
   - What gaps do they leave?
   - What do they acknowledge as future work?

**Synthesis Document:**
```markdown
## Literature Synthesis

### Research Question 1: [Question]

**Papers:** [List]

**Consensus Findings:**
- [Finding with citations]
- [Finding with citations]

**Disagreements:**
- [Point of disagreement with citations]
- Possible reasons: [analysis]

**Methodologies Used:**
- Approach A: [papers using it]
- Approach B: [papers using it]
- Comparison: [strengths/weaknesses]

**Limitations Acknowledged:**
- [Common limitation across papers]
- [Limitation specific to approach]

### [Repeat for each research question]
```

### Step 6: Gap Identification

**Types of Gaps:**

1. **Knowledge Gaps**
   - Questions not yet answered
   - Phenomena not yet explained
   - Relationships not yet explored

2. **Methodological Gaps**
   - Better ways to measure/evaluate
   - More rigorous validation approaches
   - Novel experimental designs

3. **Practical Gaps**
   - Real-world applications not addressed
   - Scalability issues not solved
   - Deployment challenges not tackled

4. **Theoretical Gaps**
   - Mechanisms not understood
   - Theories not developed
   - Frameworks not established

**Gap Validation Criteria:**

For each potential gap, ask:

1. **Is it genuine?**
   - Has no one addressed this?
   - Double-check with thorough search
   - Verify with recent preprints

2. **Is it significant?**
   - Does it matter to the field?
   - Would answering it advance knowledge?
   - Is there demand/interest?

3. **Is it feasible?**
   - Can it be addressed with available resources?
   - Are methods available or developable?
   - Is timeline realistic?

4. **Is it novel?**
   - Different from existing work?
   - Not just incremental?
   - Offers new insights?

**Gap Analysis Template:**
```markdown
## Gap: [Brief description]

### Evidence for Gap
- [Citation showing limitation]
- [Citation showing unanswered question]
- [Citation acknowledging future work]

### Significance
**Why it matters:**
- [Impact on field]
- [Practical implications]
- [Theoretical importance]

**Who cares:**
- [Research community interest]
- [Industry relevance]
- [Societal impact]

### Feasibility
**Resources needed:**
- Compute: [requirements]
- Data: [availability]
- Expertise: [required skills]

**Timeline:** [realistic estimate]

**Risks:** [potential challenges]

### Novelty
**How it differs from existing work:**
- [Comparison to related work]
- [What's genuinely new]

**Expected contribution:**
- [What we'll learn]
- [How field advances]

### Validation
- [ ] Confirmed gap exists (thorough search)
- [ ] Significance validated (expert consultation)
- [ ] Feasibility assessed (resource check)
- [ ] Novelty verified (comparison to related work)
```

### Step 7: Research Question Formulation

**From Gaps to Questions:**

For each validated gap, formulate specific research questions.

**Good Research Questions are:**
- **Specific**: Clearly defined scope
- **Answerable**: Can be addressed empirically
- **Significant**: Matters to the field
- **Novel**: Not already answered
- **Feasible**: Achievable with resources

**Question Template:**
```markdown
## Research Question [N]

**Question:** [Specific, answerable question]

**Gap Addressed:** [Which gap from analysis]

**Significance:**
- [Why this question matters]
- [Expected impact]

**Approach:**
- [How we'll answer it]
- [Methods to use]
- [Validation strategy]

**Expected Contribution:**
- [What we'll learn]
- [How it advances field]

**Success Criteria:**
- [How we'll know we answered it]
- [What evidence is needed]

**Risks & Mitigation:**
- Risk: [potential issue]
  - Mitigation: [how to address]
```

### Step 8: Contribution Statement

**Synthesize into Contribution Statement:**

```markdown
## Research Contribution Statement

### Problem
[What problem are we addressing? Why does it matter?]

### Gap
[What specific gap in knowledge/methodology/practice?]

### Our Approach
[How will we address this gap? What's novel about our approach?]

### Expected Contributions

**Empirical Contributions:**
- [New findings/insights]
- [Evidence for/against theories]

**Methodological Contributions:**
- [New methods/measures]
- [Improved validation approaches]

**Theoretical Contributions:**
- [New understanding/frameworks]
- [Explanations of phenomena]

**Practical Contributions:**
- [Applications/tools]
- [Guidelines/best practices]

### Significance
[Why this matters to the field and beyond]

### Validation Plan
[How we'll ensure contributions are valid and reproducible]
```

## Quality Checks

### Before Proceeding to Methodology Design:

- [ ] Comprehensive literature search completed
- [ ] All relevant papers reviewed and synthesized
- [ ] Gaps identified and validated
- [ ] Research questions formulated and validated
- [ ] Contribution statement clear and significant
- [ ] Feasibility confirmed
- [ ] Novelty verified
- [ ] Expert feedback obtained (if possible)

## Red Flags

**STOP if:**
- Gap is not genuine (already addressed)
- Gap is not significant (doesn't matter)
- Gap is not feasible (can't be addressed)
- Question is too vague (can't be answered)
- Contribution is incremental only (not novel enough)
- Literature review is incomplete (missing key work)

## Tools & Resources

### Search Tools
- **arXiv**: arxiv.org
- **Google Scholar**: scholar.google.com
- **Semantic Scholar**: semanticscholar.org
- **Papers with Code**: paperswithcode.com
- **Connected Papers**: connectedpapers.com

### Organization Tools
- **Zotero**: Reference management
- **Notion/Obsidian**: Note-taking and synthesis
- **Spreadsheets**: Tracking papers and screening

### Analysis Tools
- See `scripts/literature_analyzer.py` for automated analysis
- See `scripts/gap_validator.py` for gap validation

## Example: Self-Correction in LLMs

```markdown
## Gap Analysis: Real-time Self-Correction Mechanisms

### Evidence for Gap
- Smith et al. (2024): "Post-hoc correction shows promise, but 
  real-time mechanisms remain unexplored"
- Jones et al. (2024): "Future work should investigate online 
  correction during generation"
- Current work focuses on post-generation correction

### Significance
**Why it matters:**
- Real-time correction could improve output quality without 
  additional inference passes
- Reduces latency and computational cost
- More natural interaction pattern

**Who cares:**
- Researchers: Understanding correction mechanisms
- Industry: Deploying more efficient models
- Users: Better real-time interactions

### Feasibility
**Resources needed:**
- Compute: Access to LLMs (API or local)
- Data: Benchmark datasets for evaluation
- Expertise: LLM evaluation, prompt engineering

**Timeline:** 3-4 months

**Risks:** 
- May be difficult to implement real-time correction
- Mitigation: Start with simpler approaches, iterate

### Novelty
**How it differs:**
- Existing: Post-hoc correction (separate pass)
- Ours: Real-time correction (during generation)
- Novel mechanism for online error detection

**Expected contribution:**
- Understanding of when/how models can self-correct
- Practical real-time correction method
- Comparison to post-hoc approaches

### Validation
- [x] Confirmed gap exists (no real-time work found)
- [x] Significance validated (multiple papers cite as future work)
- [x] Feasibility assessed (have resources)
- [x] Novelty verified (genuinely different approach)
```

## Output Deliverables

1. **Literature Review Document**
   - Comprehensive synthesis
   - Organized by themes/questions
   - Critical analysis

2. **Gap Analysis Document**
   - Validated gaps
   - Evidence and significance
   - Feasibility assessment

3. **Research Questions**
   - Specific, answerable questions
   - Linked to gaps
   - With success criteria

4. **Contribution Statement**
   - Clear problem and gap
   - Novel approach
   - Expected contributions
   - Significance

5. **Bibliography**
   - All papers reviewed
   - Properly formatted
   - Organized by relevance

## Next Phase

Once literature review is complete and validated:
→ Proceed to **Methodology Design** (research-methodology-validator skill)

Bring forward:
- Research questions
- Gap analysis
- Contribution statement
- Key related work
