# Setup Guide: White Paper Writing Architecture

This guide walks you through setting up the white paper writing architecture in a new project.

---

## 📋 Prerequisites

- Claude Code installed and configured
- Basic familiarity with Claude Code (skills, agents, commands)
- A project directory where you'll write your white paper

---

## 🚀 Quick Setup (5 Minutes)

### Step 1: Copy Architecture Files

Copy the architecture to your new project:

```bash
# From your new project directory
cp -r /home/brian/writing/sample/.claude ./
cp /home/brian/writing/sample/CLAUDE.md ./
cp /home/brian/writing/sample/HOW-TO-USE.md ./
cp /home/brian/writing/sample/README.md ./
```

Or if using from GitHub:

```bash
# Clone the template repository
git clone https://github.com/yourusername/claude-whitepaper-template.git
cd claude-whitepaper-template

# Remove git history if you want a fresh repo
rm -rf .git
```

### Step 2: Verify File Structure

Your project should now have:

```
your-project/
├── CLAUDE.md                    # Voice & style guidelines
├── HOW-TO-USE.md               # Usage guide
├── README.md                   # Quick reference
│
└── .claude/
    ├── skills/                 # 4 skills installed
    │   ├── outline/
    │   ├── citations/
    │   ├── abstract/
    │   └── draft-section/
    │
    ├── agents/                 # 3 agents configured
    │   ├── academic-researcher.md
    │   ├── citation-validator.md
    │   └── technical-reviewer.md
    │
    ├── hooks/                  # 2 automation scripts
    │   ├── validate-citation-format.sh
    │   └── track-bibliography.sh
    │
    ├── cache/                  # Empty directory (files generated during use)
    │
    └── settings.local.json     # Configuration
```

### Step 3: Verify Hooks are Executable

```bash
chmod +x .claude/hooks/*.sh
```

### Step 4: Customize CLAUDE.md

**This is the most important step!** Edit `CLAUDE.md` to match your project:

#### Required Customizations:

**1. Target Audience** (Line ~10)
```markdown
**Target Audience:** [CHANGE THIS]
```

Examples:
- "C-level executives and technical decision-makers"
- "Software engineers and architects"
- "Data scientists and ML practitioners"
- "CTOs, engineering managers, and senior developers"

**2. Citation Style** (Line ~47)
```markdown
**Citation style:** [CHANGE THIS - IEEE, APA, or Chicago]
```

Choose based on your field:
- **IEEE** - Engineering, computer science, technical papers (default)
- **APA** - Business, social sciences, psychology
- **Chicago** - Humanities, history, general academic

**3. Voice Characteristics** (Line ~18-23)

Adjust the tone descriptions:
```markdown
**Writing Voice:**
- Professional but accessible
- Authoritative yet conversational
[CUSTOMIZE THESE to match your style]
```

#### Optional Customizations:

**4. Specific Preferences** (Throughout the file)
- Acronym handling
- Number formatting
- Technical depth
- Prohibited words/patterns

**5. Review Checklist** (End of file)
- Add project-specific requirements
- Remove items that don't apply

### Step 5: Test the Setup

Verify everything works:

```bash
# Start Claude Code in your project directory
cd your-project

# Test that skills are discoverable
# In Claude Code, type: /
# You should see: outline, citations, abstract, draft-section
```

Create a test file to verify hooks:

```bash
# Create a test markdown file with placeholder citation
echo "This is a test [SOURCE-X]." > test.md
```

When you write files, the citation validation hook should warn about `[SOURCE-X]`.

---

## 🎨 Customization Guide

### Customizing for Different Paper Types

#### Academic Research Paper
```markdown
# In CLAUDE.md, adjust:

**Target Audience:** Academic researchers and peer reviewers
**Citation style:** APA or Chicago
**Tone:** Formal, objective, evidence-focused
**Technical depth:** High - assume domain expertise
```

#### Technical White Paper (Current Default)
```markdown
**Target Audience:** Technical decision-makers (CTOs, architects)
**Citation style:** IEEE
**Tone:** Professional but accessible
**Technical depth:** Medium-high - balance details with clarity
```

#### Business White Paper
```markdown
**Target Audience:** C-level executives and business leaders
**Citation style:** APA
**Tone:** Professional, persuasive, business-value focused
**Technical depth:** Low-medium - minimal jargon
```

#### Tutorial/Educational Content
```markdown
**Target Audience:** Practitioners learning a new technology
**Citation style:** IEEE or informal
**Tone:** Conversational, encouraging, practical
**Technical depth:** Start simple, build to intermediate
```

### Customizing Skills

Edit `.claude/skills/[skill-name]/SKILL.md` to change behavior:

**Example: Change outline structure**

Edit `.claude/skills/outline/SKILL.md`:
```markdown
# Around line 50, modify the template structure

## Your Custom Structure
1. Executive Summary (not Introduction)
2. Problem Statement
3. Solution Overview
[etc.]
```

**Example: Add new citation style**

Edit `.claude/skills/citations/SKILL.md`:
```markdown
# Add new style section after Chicago

### MLA Format
**In-text citation:**
(Author Page)

**Works Cited entry:**
Author. "Title." Publication, Date.
```

### Customizing Agents

Edit `.claude/agents/[agent-name].md`:

**Example: Change research agent model**

Edit `.claude/agents/academic-researcher.md`:
```yaml
---
name: academic-researcher
model: sonnet  # Changed from haiku for better quality
---
```

**Example: Modify research scope**

In the same file, adjust instructions:
```markdown
## Research Methodology

**Source quality indicators:**
- Peer-reviewed publications (REQUIRED)  # Make stricter
- Last 2 years only (not 3)              # More recent
- Minimum 10 citations per source        # Add filter
```

### Customizing Hooks

Edit `.claude/hooks/validate-citation-format.sh`:

**Make hook blocking instead of warning:**

```bash
# At the end of the script, change:
exit 0  # Currently allows write

# To:
if [ ${#ISSUES[@]} -gt 0 ]; then
  exit 1  # Block write if issues found
fi
exit 0
```

**Add custom validation rules:**

```bash
# Add before the ISSUES array check:

# Check for your custom pattern
if echo "$CONTENT" | grep -q 'forbidden-word'; then
  ISSUES+=("Document contains forbidden word")
fi
```

---

## 🔍 Verification Checklist

After setup, verify:

- [ ] `.claude/` directory exists with all subdirectories
- [ ] 4 skills present in `.claude/skills/`
- [ ] 3 agents present in `.claude/agents/`
- [ ] 2 hooks present and executable in `.claude/hooks/`
- [ ] `CLAUDE.md` exists and is customized for your project
- [ ] `HOW-TO-USE.md` and `README.md` are present
- [ ] `.claude/cache/` directory exists (may be empty)
- [ ] Hook scripts are executable (`ls -l .claude/hooks/*.sh` shows `x` permission)

Test each component:

```bash
# In Claude Code:

# Test skill invocation
/outline test

# Test agent invocation
@academic-researcher research test topic

# Test hooks (create a test file with [SOURCE-X])
# Should see warning about placeholder citations
```

---

## 🎯 Project-Specific Setup Examples

### Example 1: Multi-Author Research Paper

**Scenario:** Academic paper with multiple co-authors, strict citation requirements

**Setup:**
```bash
# 1. Copy architecture
cp -r ~/whitepaper-template/.claude ./

# 2. Customize CLAUDE.md
# - Set citation style: APA
# - Set audience: "Academic researchers"
# - Set tone: "Formal, objective"
# - Add: "Use 'we' for author voice"

# 3. Make citation hook blocking
# Edit .claude/hooks/validate-citation-format.sh
# Change exit 0 to exit 1 for errors

# 4. Adjust research agent for stricter sources
# Edit .claude/agents/academic-researcher.md
# Require peer-reviewed only, last 2 years
```

### Example 2: Technical Product White Paper

**Scenario:** Marketing-adjacent technical paper for prospects

**Setup:**
```bash
# 1. Copy architecture
cp -r ~/whitepaper-template/.claude ./

# 2. Customize CLAUDE.md
# - Set citation style: IEEE (but more relaxed)
# - Set audience: "Technical buyers and evaluators"
# - Set tone: "Professional, persuasive, clear ROI focus"
# - Allow: Some marketing language (carefully)

# 3. Add custom section to outline skill
# Edit .claude/skills/outline/SKILL.md
# Add "ROI Analysis" and "Competitive Comparison" sections

# 4. Adjust abstract skill for executive focus
# Edit .claude/skills/abstract/SKILL.md
# Emphasize business value over technical details
```

### Example 3: Internal Technical Documentation

**Scenario:** Company-internal architecture documentation

**Setup:**
```bash
# 1. Copy architecture
cp -r ~/whitepaper-template/.claude ./

# 2. Customize CLAUDE.md
# - Set audience: "Internal engineering team"
# - Set tone: "Direct, practical, informal citations OK"
# - Set citation style: Informal/URL-based
# - Add: Company-specific terminology

# 3. Simplify citation requirements
# Edit .claude/hooks/validate-citation-format.sh
# Remove strict format checks, just ensure URLs work

# 4. Focus research agent on internal docs
# Edit .claude/agents/academic-researcher.md
# Add company wiki, Confluence, internal GitHub
```

---

## 📦 Version Control Setup

If you want to version control your white paper with the architecture:

### Create .gitignore

```bash
cat > .gitignore << 'EOF'
# Claude Code generated files (don't commit)
.claude/cache/
.claude/cache/*

# Drafts and working files (optional - decide per project)
draft*.md
scratch/
notes/

# Keep the architecture files (these SHOULD be committed)
!.claude/skills/
!.claude/agents/
!.claude/hooks/
!.claude/settings.local.json

# Keep documentation
!*.md
!CLAUDE.md
!HOW-TO-USE.md
!README.md
EOF
```

### Initial Commit

```bash
git init
git add .claude/ *.md .gitignore
git commit -m "Initial setup: White paper writing architecture"
```

---

## 🔧 Troubleshooting Setup

### Skills Not Found

**Problem:** `/outline` says "skill not found"

**Solution:**
```bash
# Verify skills directory structure
ls -la .claude/skills/outline/SKILL.md

# If missing, re-copy skills directory
cp -r ~/whitepaper-template/.claude/skills .claude/
```

### Agents Not Spawning

**Problem:** `@academic-researcher` doesn't respond

**Solution:**
```bash
# Verify agents exist
ls -la .claude/agents/academic-researcher.md

# Check file has proper YAML frontmatter
head -n 10 .claude/agents/academic-researcher.md
# Should show:
# ---
# name: academic-researcher
# description: ...
# ---
```

### Hooks Not Running

**Problem:** No warnings when writing files with `[SOURCE-X]`

**Solution:**
```bash
# Make hooks executable
chmod +x .claude/hooks/*.sh

# Test hook manually
export TOOL_PARAMS='{"content":"test [SOURCE-X]"}'
.claude/hooks/validate-citation-format.sh

# Verify settings.local.json has hooks configured
cat .claude/settings.local.json | grep -A 10 hooks
```

### CLAUDE.md Not Being Used

**Problem:** Skills/agents don't follow your voice guidelines

**Solution:**
```bash
# Verify CLAUDE.md is in project root (not inside .claude/)
ls -la CLAUDE.md

# Should be at: ./CLAUDE.md
# Not at: ./.claude/CLAUDE.md

# If in wrong location, move it
mv .claude/CLAUDE.md ./CLAUDE.md
```

---

## 🎓 Next Steps After Setup

1. **Read HOW-TO-USE.md** for complete workflow guide
2. **Customize CLAUDE.md** for your specific project
3. **Test with a small section** before writing full paper
4. **Iterate on customizations** as you discover preferences

---

## ✅ Setup Complete!

You're ready to write. Start with:

```bash
# In Claude Code:
@academic-researcher research [your topic]
```

Or jump straight to outlining if you already have research:

```bash
/outline [your topic]
```

See `HOW-TO-USE.md` for complete workflows and examples.

---

**Questions or Issues?**
- Check `HOW-TO-USE.md` for usage guidance
- Review `README.md` for architecture overview
- Consult troubleshooting section above
