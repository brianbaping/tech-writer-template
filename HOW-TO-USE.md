# How to Use This White Paper Writing Architecture

This guide explains how to use the custom Claude Code architecture built for writing white papers. You now have skills, agents, and hooks working together to streamline your writing process.

---

## 📁 What You Have

### Skills (Automatic & Manual Invocation)
- **`/outline`** - Generate structured outlines from research
- **`/citations`** - Format citations in IEEE/APA/Chicago
- **`/abstract`** - Write executive summaries
- **`/draft-section`** - Expand outlines into first drafts

### Agents (Spawn for Complex Tasks)
- **`@academic-researcher`** - Autonomous literature review
- **`@citation-validator`** - Verify citation completeness
- **`@technical-reviewer`** - Comprehensive quality review

### Automation (Runs Automatically)
- **Citation validation hook** - Warns about citation issues when writing
- **Bibliography tracking hook** - Logs web sources automatically

### Configuration
- **`CLAUDE.md`** - Your voice descriptor and writing guidelines
- **`.claude/cache/`** - Where research notes and reports are saved

---

## 🚀 Quick Start: Writing Your White Paper

### Phase 1: Research

**Goal:** Gather information and sources

**Option A - Manual Research:**
Just have conversations with Claude and take notes yourself.

**Option B - Automated Research (Recommended):**

```
You: @academic-researcher research multi-agent AI architectures for white papers
```

What happens:
1. The researcher agent spawns in isolated context
2. Searches academic papers, technical docs, industry sources
3. Analyzes and synthesizes findings
4. Writes detailed notes to `.claude/cache/research-notes-[topic].md`
5. Returns a concise summary to you
6. Bibliography tracking hook automatically logs all fetched sources

**To launch multiple research agents in parallel:**

```
You: @academic-researcher research orchestrator patterns
     @academic-researcher research context window management
     @academic-researcher research performance benchmarks
```

All three agents will run simultaneously, then report back with their findings.

**Review the research:**
- Read `.claude/cache/research-notes-*.md` files
- Check `.claude/cache/bibliography-sources.txt` for tracked sources

---

### Phase 2: Planning Structure

**Goal:** Create a clear outline

**Use the `/outline` skill:**

```
You: /outline multi-agent architectures white paper
```

Or if you have research notes:

```
You: /outline using the research notes in .claude/cache/
```

What happens:
1. Skill reads your research notes
2. Identifies key themes and logical flow
3. Generates comprehensive outline with annotations
4. Writes to `outline.md` (or asks where to save)

**Review and adjust:**
- Read the generated outline
- Reorder sections if needed
- Add or remove topics
- Note which sections need more research

---

### Phase 3: Writing Sections

**Goal:** Transform outline into prose

**Two approaches:**

**Approach A - Collaborative Writing (Recommended):**
Write in the main conversation with Claude for strategic sections:

```
You: Let's write the introduction section. Here's what I want to emphasize...

Claude: [Writes introduction collaboratively with you]

You: Good, but make the opening sentence more impactful

Claude: [Revises with your feedback]
```

**Best for:** Introduction, conclusion, argumentative sections, anything requiring nuance

**Approach B - Automated First Drafts:**
Use `/draft-section` skill for mechanical expansion:

```
You: /draft-section Section 3 Technical Architecture
```

What happens:
1. Skill reads the outline and research notes
2. Expands outline bullets into complete paragraphs
3. Adds placeholders for missing pieces
4. Generates first draft for review

**Best for:** Technical explanations, methodology sections, background sections

**As you write:**
- The citation validation hook warns about citation issues
- Add citations using `/citations` skill when needed:

```
You: /citations ieee https://arxiv.org/abs/2401.12345
```

---

### Phase 4: Citation Management

**Goal:** Properly format and track all references

**While writing, format citations:**

```
You: /citations ieee Smith, A. (2024). "Multi-agent patterns." IEEE Trans.
```

Returns formatted in-text citation and reference entry.

**Before finalizing, validate all citations:**

```
You: @citation-validator check my white paper
```

What happens:
1. Agent spawns in isolated context
2. Extracts all citations from document
3. Verifies format consistency
4. Tests all URLs for accessibility
5. Checks correspondence between in-text and references
6. Writes detailed report to `.claude/cache/citation-validation-report.md`
7. Returns summary with prioritized fixes

**Review and fix issues:**
- Read the validation report
- Fix critical errors first (broken links, missing citations)
- Address format inconsistencies
- Re-run validator after fixes

---

### Phase 5: Quality Review

**Goal:** Ensure technical accuracy and professional quality

**Request comprehensive review:**

```
You: @technical-reviewer review my complete white paper
```

What happens:
1. Reviewer agent spawns (using Opus model for critical analysis)
2. Reads entire document carefully
3. Verifies technical accuracy
4. Evaluates logical flow and clarity
5. Tests code examples
6. Checks adherence to CLAUDE.md guidelines
7. Writes detailed report to `.claude/cache/technical-review-report.md`
8. Returns summary with prioritized recommendations

**The review covers:**
- Technical accuracy and correctness
- Logical structure and argumentation
- Clarity and readability
- Completeness (missing sections, gaps)
- Professional polish and formatting
- Code example validation

**Implement revisions:**
1. Review the report (sorted by priority)
2. Fix critical issues first
3. Address major improvements
4. Consider minor polish items
5. Re-run reviewer after major revisions (optional)

---

### Phase 6: Executive Summary

**Goal:** Write compelling abstract/summary

**Generate after completing all sections:**

```
You: /abstract write executive summary for whitepaper.md
```

What happens:
1. Skill reads your entire white paper
2. Identifies key points and findings
3. Writes concise, compelling summary
4. Follows white paper conventions
5. Returns both executive summary and abstract versions

**Why last?** Because you need to know what you actually wrote, not what you planned to write.

---

## 🎯 Complete Workflow Example

Here's a start-to-finish example:

```
# Day 1: Research
You: @academic-researcher research multi-agent AI architectures
     @academic-researcher research context window optimization
     @academic-researcher research performance benchmarks

[Agents work in parallel, return findings]

You: Review the research notes, looks good. Let's outline.

# Day 2: Planning
You: /outline using research from .claude/cache/

[Review generated outline]

You: Looks good, but let's add a section on security considerations

[Adjust outline together]

# Day 3-5: Writing
You: Let's write the introduction together

[Collaborative writing for strategic sections]

You: /draft-section Section 3 Technical Architecture

[Review and refine generated draft]

You: /citations ieee [source info]

[Continue writing remaining sections]

# Day 6: Citations
You: @citation-validator check whitepaper.md

[Review validation report]

[Fix critical citation issues]

# Day 7: Review
You: @technical-reviewer review whitepaper.md

[Review detailed feedback]

[Implement Priority 1 and Priority 2 fixes]

# Day 8: Finalize
You: /abstract write executive summary

[Review and polish executive summary]

You: @citation-validator check whitepaper.md (re-run)

[Confirm all citations pass]

Done! Your white paper is ready for publication.
```

---

## 📋 Reference: When to Use Each Component

### Use Skills When:
- ✅ Single, repeatable task
- ✅ Need consistent output format
- ✅ Want automatic invocation based on context
- ✅ Task can complete in one turn

**Examples:**
- Formatting a citation
- Generating an outline
- Writing an abstract

### Use Agents When:
- ✅ Multi-step process with decision points
- ✅ Need to isolate verbose output from main conversation
- ✅ Want parallel execution of independent tasks
- ✅ Long-running operations (comprehensive research, validation)

**Examples:**
- Conducting literature review
- Validating all citations in document
- Comprehensive technical review

### Stay in Main Conversation When:
- ✅ Strategic or creative decisions
- ✅ Iterative refinement with back-and-forth
- ✅ Nuanced argumentation
- ✅ Need full conversation context

**Examples:**
- Writing introduction and conclusion
- Making architectural decisions about paper structure
- Refining specific paragraphs

---

## 🔍 Finding Generated Files

All generated reports and notes go to `.claude/cache/`:

```bash
.claude/cache/
├── research-notes-[topic].md          # Research agent output
├── citation-validation-report.md      # Citation validator output
├── technical-review-report.md         # Technical reviewer output
└── bibliography-sources.txt           # Auto-tracked web sources
```

To view:
```
You: Read .claude/cache/research-notes-multi-agent.md
```

Or just open them in your text editor.

---

## ⚙️ Customization

### Adjusting Voice and Style

Edit `CLAUDE.md` to change:
- Writing tone and voice
- Target audience
- Citation style (IEEE/APA/Chicago)
- Formatting preferences
- Prohibited patterns

All skills and agents will automatically use your updated guidelines.

### Modifying Skills

Skills are in `.claude/skills/[skill-name]/SKILL.md`

To customize:
1. Edit the SKILL.md file
2. Modify the instructions or behavior
3. Save changes
4. Skill immediately uses new instructions

### Modifying Agents

Agents are in `.claude/agents/[agent-name].md`

To customize:
1. Edit the agent markdown file
2. Change tools, model, or instructions
3. Save changes
4. Agent uses new configuration on next spawn

### Disabling Hooks

Edit `.claude/settings.local.json`:

```json
{
  "disableAllHooks": true
}
```

Or remove specific hooks from the "hooks" section.

---

## 🐛 Troubleshooting

### "Skill not found"

**Problem:** `/outline` doesn't work

**Solution:** Skills are invoked automatically or manually. Try:
```
You: Generate an outline for my white paper
```
Claude should auto-invoke the skill. Or explicitly:
```
You: /outline [topic]
```

### "Agent not responding"

**Problem:** `@academic-researcher` doesn't spawn

**Solution:** Agents need `@` prefix:
```
You: @academic-researcher research [topic]
```

### "Citation hook shows warnings"

**Problem:** Hook reports placeholder citations

**Solution:** This is expected during drafting. Replace `[SOURCE-X]` with proper citations:
```
You: /citations ieee [source information]
```

### "Research notes not found"

**Problem:** Skills can't find research

**Solution:** Check `.claude/cache/` directory exists and has files:
```
You: List files in .claude/cache/
```

If empty, research agents haven't run yet.

---

## 💡 Tips for Success

1. **Research first, write later** - Don't write without adequate research
2. **Outline thoroughly** - A good outline makes writing 10x easier
3. **Use collaborative writing for key sections** - Agents for mechanics, you for strategy
4. **Cite as you write** - Don't save citations for the end
5. **Review early and often** - Don't wait until done to run validators
6. **Iterate** - First drafts are meant to be revised
7. **Leverage parallel agents** - Research multiple topics simultaneously
8. **Trust the process** - Let agents handle tedious work, you focus on content

---

## 📚 Quick Reference Commands

```bash
# Research
@academic-researcher research [topic]

# Planning
/outline [topic or source]

# Writing
/draft-section [section name]
[Or write collaboratively with Claude in main conversation]

# Citations
/citations [style] [source info]
@citation-validator check [file]

# Review
@technical-reviewer review [file]

# Finalize
/abstract [file path]

# View outputs
Read .claude/cache/[filename].md
```

---

## 🎓 Learning More

**About agents and skills in Claude Code:**
- [Claude Code Documentation](https://docs.claude.com/claude-code)

**Project-specific guidelines:**
- Read `CLAUDE.md` for your voice and style guidelines
- Check `.claude/skills/*/SKILL.md` to see how skills work
- Review `.claude/agents/*.md` to understand agent capabilities

---

## ✅ You're Ready!

This architecture is designed to:
- **Speed up** research and drafting
- **Ensure quality** through automated validation
- **Maintain consistency** with voice guidelines
- **Reduce tedium** by automating mechanical tasks
- **Keep you in control** of strategic decisions

Start with research, move to outlining, write collaboratively, validate thoroughly, and review comprehensively.

**Happy writing!** 🚀
