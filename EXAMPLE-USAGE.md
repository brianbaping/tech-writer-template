# Example Usage: From Source Documents to White Paper

This guide shows you how to use the architecture when you already have a folder of source documents that need to be transformed into a professional white paper.

---

## 📁 Scenario

You have a folder of documents containing research, notes, specs, and other content:

```
my-whitepaper/
├── source-docs/
│   ├── meeting-notes.md
│   ├── technical-specs.txt
│   ├── research-findings.pdf
│   ├── customer-feedback.md
│   └── competitor-analysis.md
└── [your architecture files]
```

**Goal:** Transform these into a cohesive, professional white paper.

---

## 🚀 Complete Workflow

### Step 1: Set Up Your Project

```bash
# Clone the template
git clone https://github.com/brianbaping/tech-writer-template.git my-whitepaper
cd my-whitepaper

# Make hooks executable
chmod +x .claude/hooks/*.sh

# Customize voice descriptor
cp CLAUDE.template.md CLAUDE.md
# Edit CLAUDE.md with your preferences

# Create source docs folder
mkdir source-docs
# Copy your documents into source-docs/
```

---

### Step 2: Understand Your Content

**Start by having Claude read your source documents:**

```
You: I have source documents in ./source-docs/ that I need to turn into a white paper.
Let's start by reading and understanding what we have.

Read source-docs/meeting-notes.md
Read source-docs/technical-specs.txt
Read source-docs/customer-feedback.md
Read source-docs/competitor-analysis.md
```

**Ask Claude to summarize:**

```
You: Summarize the key themes across these documents. What main topics would make sense for a white paper?
```

Claude will identify:
- Common themes
- Key technical points
- Data and statistics
- Gaps that need research

---

### Step 3: Generate Outline from Your Documents

**Use the outline skill:**

```
You: /outline based on the documents we just read

Or be more specific:

You: /outline
Based on the source documents in ./source-docs/, create a white paper outline about [your topic].
Target audience: [CTOs, engineers, business leaders, etc.]
Focus on: [architecture, performance, business value, etc.]
```

**What happens:**
- Skill reads your source documents
- Identifies key themes and logical flow
- Creates structured outline with section descriptions
- Notes which source docs support each section
- Saves to `outline.md`

**Review and adjust:**

```
You: The outline looks good, but let's add a section on security considerations
```

---

### Step 4: Fill Research Gaps (Optional)

If your documents don't cover everything:

```
You: The source docs mention multi-agent systems but lack performance data.
@academic-researcher research multi-agent AI performance benchmarks and scalability studies
```

**Multiple research agents in parallel:**

```
You: @academic-researcher research multi-agent performance benchmarks
     @academic-researcher research context window optimization techniques
     @academic-researcher research production deployment case studies
```

All three agents work simultaneously, then report back with findings.

---

### Step 5: Write Sections

#### Option A: Collaborative Writing (Recommended for Key Sections)

```
You: Let's write the Introduction section together.
Use the problem statement from meeting-notes.md and the solution overview from technical-specs.txt.
```

**Claude drafts introduction based on your source documents**

```
You: Good, but make the opening sentence more impactful and add the 40% improvement stat from customer-feedback.md

You: Perfect. Now add a brief roadmap of what the paper covers.
```

**Continue iterating until you're satisfied.**

#### Option B: Automated Draft (For Technical Sections)

```
You: /draft-section Section 3: Technical Architecture
```

**What happens:**
- Skill reads the outline for Section 3
- Pulls relevant content from source documents
- Expands outline bullets into complete paragraphs
- Adds placeholders for missing information
- Creates first draft for your review

**Review and refine:**

```
You: The technical architecture section looks good, but let's expand the part about the orchestrator pattern. Add more detail from technical-specs.txt lines 45-67.
```

#### Option C: Hybrid Approach (Recommended)

- **Collaborative** for: Introduction, Conclusion, Executive Summary
- **Automated draft** for: Technical sections, Background, Methodology
- **You write** for: Sections requiring nuanced argumentation

---

### Step 6: Add Citations

#### Cite External Sources

```
You: /citations ieee Smith et al. "Multi-Agent Architectures" mentioned in research-findings.pdf
```

#### Cite Your Own Documents

```
You: /citations ieee
Author: Internal Engineering Team
Title: Technical Specifications v2.1
Organization: Our Company
Date: January 2026
Note: Internal document - source-docs/technical-specs.txt
```

#### Add Multiple Citations

```
You: /citations ieee https://arxiv.org/abs/2401.12345

You: /citations ieee
The benchmark study referenced in customer-feedback.md from Anthropic's research team
```

---

### Step 7: Validate Citations

```
You: @citation-validator check whitepaper.md
```

**What happens:**
- Agent spawns in isolated context
- Extracts all citations from your white paper
- Verifies format consistency (IEEE/APA/Chicago)
- Tests all URLs for accessibility
- Checks in-text citations match reference list
- Identifies missing citations or broken links
- Writes detailed report to `.claude/cache/citation-validation-report.md`
- Returns summary with prioritized fixes

**Review and fix:**

```
You: Read .claude/cache/citation-validation-report.md

You: Fix the broken link in citation [7] - use this updated URL instead: [new URL]

You: Replace [SOURCE-X] in section 4 with proper citation to technical-specs.txt
```

---

### Step 8: Technical Review

```
You: @technical-reviewer review whitepaper.md
```

**What happens:**
- Agent spawns using Opus model (strongest for critical analysis)
- Reads entire document carefully
- Verifies technical accuracy
- Evaluates logical flow and clarity
- Tests code examples (if any)
- Checks adherence to CLAUDE.md guidelines
- Identifies gaps and weaknesses
- Writes detailed report to `.claude/cache/technical-review-report.md`
- Returns summary with prioritized recommendations

**The review covers:**
- Technical accuracy and correctness
- Logical structure and argumentation
- Clarity and readability
- Completeness (missing sections, gaps)
- Professional polish and formatting

**Implement fixes:**

```
You: Read .claude/cache/technical-review-report.md

You: Fix the passive voice issue in Section 4 paragraph 2

You: Add the missing security considerations section after Section 6

You: Update the outdated reference [11] with a more recent source
```

---

### Step 9: Generate Executive Summary

**After all sections are complete:**

```
You: /abstract whitepaper.md
```

**What happens:**
- Skill reads your complete white paper
- Identifies key findings and insights
- Writes compelling executive summary (500-1000 words)
- Generates shorter abstract version (150-300 words)
- Includes quantitative results
- Returns both versions for you to choose

**Why last?** Because you need to know what you actually wrote, not what you planned to write.

---

## 🎯 Complete Example Session

Here's a real conversation from start to finish:

### Initial Setup

```
You: I have source documents in ./source-docs/ about our new multi-agent AI platform.
These include meeting notes, technical specs, customer feedback, and competitor analysis.

Let me show you what we have:

Read source-docs/meeting-notes.md
Read source-docs/technical-specs.txt
Read source-docs/customer-feedback.md
Read source-docs/competitor-analysis.md
```

**Claude:** *Reads all four documents and provides summary*

```
I've reviewed your source documents. Here are the main themes:

1. **Problem:** Context window limitations in single-agent AI systems
2. **Solution:** Multi-agent orchestration with specialized workers
3. **Results:** 40% performance improvement, 80% token reduction
4. **Market:** Strong customer adoption, competitive advantages

These would make an excellent technical white paper for CTOs and architects.
```

### Generate Outline

```
You: /outline

Create a white paper outline for technical decision-makers (CTOs, engineering managers, architects) based on these source documents.

Focus on:
- Technical architecture and design patterns
- Performance and efficiency improvements
- Real-world deployment considerations
- Competitive differentiation
```

**Skill generates comprehensive outline saved to `outline.md`**

```
You: Read outline.md

[Review the structure]

You: Perfect. Let's add a section on security and privacy considerations between sections 6 and 7.
```

### Fill Research Gaps

```
You: The source docs have great internal data, but we need external validation.
@academic-researcher research multi-agent AI architectures - focus on peer-reviewed papers from 2023-2024
@academic-researcher research context window optimization techniques and token efficiency studies
```

**Both agents work in parallel, return findings**

```
You: Excellent. The research validates our approach and provides additional citations.
```

### Write Introduction

```
You: Let's write Section 1 (Introduction) together.

Start with the problem statement from meeting-notes.md - the context window limitation issue.
Then introduce our multi-agent solution from technical-specs.txt.
Include the 40% improvement stat from customer-feedback.md.
Target audience is technical leaders evaluating AI architectures.
```

**Claude writes introduction draft using specified source content**

```
You: Good start. But make the opening sentence more impactful - lead with the statistic:
"Multi-agent AI architectures achieve 40% better performance than single-agent systems while reducing token costs by 80%."

You: Perfect. Now add a brief roadmap paragraph previewing what the paper covers.

You: Excellent. Section 1 is done.
```

### Draft Technical Sections

```
You: /draft-section Section 3: Technical Architecture
```

**Skill generates first draft pulling from technical-specs.txt**

```
You: Read the draft. This is solid. Just expand the orchestrator-worker pattern subsection with more implementation details from technical-specs.txt lines 89-145.
```

**Claude expands that section**

```
You: /draft-section Section 4: Performance Analysis
```

**Skill generates draft using customer-feedback.md data**

```
You: Good. Add the research findings from the academic-researcher agents about token efficiency.
```

### Continue Writing

```
You: Let's write Section 5 (Use Cases) collaboratively.

Pull the three customer examples from customer-feedback.md and expand each into a detailed case study with before/after metrics.
```

**Write remaining sections through collaboration or draft-section skill**

### Add Citations

```
You: /citations ieee
The orchestrator pattern is based on this paper we found:
https://arxiv.org/abs/2401.12345
Smith, A. & Jones, B. "Multi-Agent Orchestration" published March 2024
```

```
You: /citations ieee
Author: Internal Engineering Team
Title: Technical Specifications: Multi-Agent Platform v2.1
Organization: Our Company
Date: January 2026
Note: Internal document
```

### Validate Everything

```
You: @citation-validator check whitepaper.md
```

**Agent returns:**
```
Citation validation completed.

Critical Issues: 2
- Citation [7] has broken URL
- In-text citation [12] missing from reference list

Format Issues: 3
- Three citations placed after periods (should be before)

Detailed report: .claude/cache/citation-validation-report.md
```

```
You: Fix citation [7] with updated URL: https://docs.anthropic.com/en/docs/agents

You: Add missing reference [12] - it's the competitor-analysis.md internal document

You: Fix the three citations to come before periods instead of after
```

**Re-run validator:**

```
You: @citation-validator check whitepaper.md
```

**Agent returns:** ✅ All citations pass validation

### Technical Review

```
You: @technical-reviewer review whitepaper.md
```

**Agent returns comprehensive review:**
```
Technical review completed.

Overall Assessment: Good - Minor revisions needed

Critical Issues: 1
- Technical error in Section 3.2 about attention mechanisms (line 245)

Major Improvements: 4
- Section 4 overuses passive voice (lines 312-318)
- Missing security considerations section (recommended addition)
- Complex sentence needs breaking up (line 456)
- Add 2-3 more use case examples (Section 5)

Minor Polish: 6
[Additional suggestions]

Detailed report: .claude/cache/technical-review-report.md
```

```
You: Read .claude/cache/technical-review-report.md

[Review all findings]

You: Fix the technical error about attention mechanisms in Section 3.2

You: Rewrite Section 4 lines 312-318 in active voice

You: Add new Section 6.5: Security and Privacy Considerations
Include: data isolation, credential management, audit logging, compliance

You: Add two more use case examples to Section 5 - pull from customer-feedback.md
```

### Generate Executive Summary

```
You: /abstract whitepaper.md
```

**Skill generates:**
- Executive Summary (750 words)
- Abstract (200 words)
- Key takeaway statement

```
You: Perfect. Add the executive summary at the beginning of whitepaper.md after the title.
```

### Final Check

```
You: @citation-validator check whitepaper.md
```

✅ Pass

```
You: Read through the complete whitepaper.md one more time for final polish.
```

**Done!** Professional white paper ready for publication.

---

## 💡 Pro Tips for Document-Based Writing

### Create a Source Document Index

```
You: Create a source-docs-index.md file listing all my source documents with:
- Filename
- Brief description of contents
- Key sections or data points
- Which white paper sections they support
```

Then reference it:
```
You: /outline using the documents listed in source-docs-index.md
```

### Extract Key Quotes First

```
You: Read all files in source-docs/ and extract:
- The 10 most important data points
- The 5 best quotes to use in the white paper
- Any gaps that need additional research

Save to key-content.md for reference.
```

### Create Content Mapping

```
You: For each section in outline.md, tell me which source documents contain relevant content and where (specific line numbers or sections).

Create a content-map.md file showing this mapping.
```

This helps you know exactly where to pull information from.

### Handle Different File Formats

The architecture can read:
- **Markdown** (.md) - Native
- **Text files** (.txt) - Native
- **PDFs** (.pdf) - Text extraction
- **Code files** - If containing documentation

```
You: Read source-docs/architecture-diagram.py and extract the documentation comments for the white paper
```

### Organize by Topic

```
source-docs/
├── 01-problem-statement/
│   ├── customer-pain-points.md
│   └── market-analysis.md
├── 02-technical-solution/
│   ├── architecture-specs.txt
│   └── implementation-guide.md
└── 03-results/
    ├── performance-benchmarks.md
    └── customer-testimonials.md
```

Then reference by section:
```
You: /draft-section Introduction using documents from source-docs/01-problem-statement/
```

---

## 🔄 Workflow Patterns

### Pattern 1: Linear (Simple)

```
1. Read all source docs
2. Generate outline
3. Draft all sections sequentially
4. Add citations
5. Validate and review
6. Write abstract
```

Best for: Straightforward content, clear structure

### Pattern 2: Iterative (Complex)

```
1. Read source docs
2. Generate outline
3. Write section 1 (collaboratively)
4. Draft sections 2-4 (automated)
5. Review and revise sections 1-4
6. Identify gaps, spawn research agents
7. Write sections 5-7 (collaboratively)
8. Validate citations
9. Technical review
10. Fix issues
11. Write abstract
```

Best for: Complex topics, multiple iterations

### Pattern 3: Parallel (Fast)

```
1. Read source docs
2. Generate outline
3. Spawn 3 research agents (parallel gaps)
4. Draft sections 2, 4, 6 (while agents work)
5. Write sections 1, 3, 5 collaboratively
6. Integrate research findings
7. Validate and review (both validators parallel)
8. Fix issues
9. Write abstract
```

Best for: Tight deadlines, well-defined scope

---

## 📋 Quick Reference Commands

```bash
# Initial Analysis
Read source-docs/[filename]
"Summarize key themes across these documents"

# Outline
/outline based on source-docs/, targeting [audience]

# Research Gaps
@academic-researcher research [topic]

# Write Sections
"Let's write [section] together using [source-doc]"
/draft-section [section name]

# Citations
/citations [style] [source info]

# Validation
@citation-validator check whitepaper.md
@technical-reviewer review whitepaper.md

# Executive Summary
/abstract whitepaper.md

# View Reports
Read .claude/cache/citation-validation-report.md
Read .claude/cache/technical-review-report.md
```

---

## ✅ Checklist: Source Docs to White Paper

- [ ] Source documents copied to `source-docs/`
- [ ] CLAUDE.md customized for project
- [ ] Claude reads all source documents
- [ ] Key themes and gaps identified
- [ ] Outline generated and reviewed
- [ ] Research gaps filled (if needed)
- [ ] All sections written (collaborative + automated)
- [ ] Citations added and formatted
- [ ] Citation validation passed
- [ ] Technical review completed
- [ ] Issues from review fixed
- [ ] Executive summary written
- [ ] Final proofread complete
- [ ] White paper ready for publication

---

## 🎯 Time Estimates

**Small white paper (5-10 pages):**
- Setup: 10 minutes
- Analysis & outline: 30 minutes
- Writing: 2-4 hours
- Review & fixes: 1-2 hours
- **Total: 4-7 hours**

**Medium white paper (15-25 pages):**
- Setup: 15 minutes
- Analysis & outline: 1 hour
- Research gaps: 1-2 hours
- Writing: 1-2 days
- Review & fixes: 3-4 hours
- **Total: 2-3 days**

**Large white paper (30+ pages):**
- Setup: 20 minutes
- Analysis & outline: 2 hours
- Research: 1 day
- Writing: 3-5 days
- Review & fixes: 1 day
- **Total: 5-7 days**

These estimates assume you have quality source documents. Multiply by 2-3x if starting from scratch.

---

## 🚀 Ready to Start?

If you have source documents ready:

1. Copy the architecture to your project
2. Point Claude at your `source-docs/` folder
3. Follow the workflow above
4. Transform your documents into a professional white paper!

**Questions?** See [HOW-TO-USE.md](HOW-TO-USE.md) for general usage or [SETUP.md](SETUP.md) for customization.
