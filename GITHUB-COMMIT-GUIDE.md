# GitHub Repository Setup Guide

Quick reference for pushing this architecture to https://github.com/brianbaping/tech-writer-template

---

## 📋 Pre-Commit Checklist

Before committing, ensure:

- [ ] `.gitignore` is in place
- [ ] `CLAUDE.md` is renamed to `CLAUDE.template.md` (template version only)
- [ ] `test-sample.md` is removed (or added to .gitignore)
- [ ] `.claude/cache/` is empty or excluded
- [ ] All hooks are executable
- [ ] LICENSE file is present
- [ ] README.md references correct GitHub repo URL

---

## 🗂️ Files to Commit

### ✅ Must Commit (Core Architecture)

```
.claude/
├── skills/
│   ├── outline/SKILL.md
│   ├── citations/SKILL.md
│   ├── abstract/SKILL.md
│   └── draft-section/SKILL.md
├── agents/
│   ├── academic-researcher.md
│   ├── citation-validator.md
│   └── technical-reviewer.md
├── hooks/
│   ├── validate-citation-format.sh
│   └── track-bibliography.sh
└── settings.local.json
```

### ✅ Must Commit (Documentation)

```
README.md
SETUP.md
HOW-TO-USE.md
CLAUDE.template.md  (template version, NOT CLAUDE.md)
LICENSE
.gitignore
```

### ❌ Do NOT Commit (Generated/Project-Specific)

```
.claude/cache/              (generated during use)
CLAUDE.md                   (project-specific, users create from template)
test-sample.md              (just for testing)
outline.md                  (project-specific)
whitepaper.md              (project-specific)
*.md drafts                (project-specific)
GITHUB-COMMIT-GUIDE.md     (this file - just for you)
```

---

## 🚀 Git Commands

### Initial Setup (First Time)

```bash
cd /home/brian/writing/sample

# Initialize git if not already done
git init

# Add remote (if not already added)
git remote add origin https://github.com/brianbaping/tech-writer-template.git

# Create .gitignore (already done)
# Create CLAUDE.template.md from CLAUDE.md (already done)
```

### Clean Up Project-Specific Files

```bash
# Remove test file
rm -f test-sample.md

# Create empty cache directory (Git tracks directories with files)
touch .claude/cache/.gitkeep

# Add .gitkeep to .gitignore exceptions
echo "!.claude/cache/.gitkeep" >> .gitignore
```

### Stage Files for Commit

```bash
# Add architecture files
git add .claude/

# Add documentation
git add README.md SETUP.md HOW-TO-USE.md CLAUDE.template.md

# Add config files
git add .gitignore LICENSE

# Check what will be committed
git status

# Should show:
# - All .claude/ files
# - All documentation files
# - .gitignore and LICENSE
#
# Should NOT show:
# - .claude/cache/* (except .gitkeep)
# - CLAUDE.md (project-specific)
# - test-sample.md
# - Any personal draft files
```

### Commit and Push

```bash
# Initial commit
git commit -m "Initial commit: Technical white paper writing architecture

- 4 skills for writing tasks (outline, citations, abstract, draft-section)
- 3 agents for complex workflows (research, validation, review)
- 2 automation hooks (citation validation, bibliography tracking)
- Complete documentation (README, SETUP, HOW-TO-USE)
- Customizable voice descriptor template (CLAUDE.template.md)
- MIT License"

# Push to GitHub
git branch -M main
git push -u origin main
```

### Verify on GitHub

After pushing, verify:
1. Go to https://github.com/brianbaping/tech-writer-template
2. Check that `.claude/` directory structure is visible
3. Verify README.md displays correctly with badges
4. Ensure CLAUDE.template.md is present (not CLAUDE.md)
5. Confirm LICENSE is visible
6. Check that `.claude/cache/` only contains `.gitkeep`

---

## 📝 Creating Releases

### Tag a Version

```bash
# After initial commit, create v1.0.0 release
git tag -a v1.0.0 -m "Release v1.0.0: Initial architecture"
git push origin v1.0.0
```

### GitHub Release

1. Go to https://github.com/brianbaping/tech-writer-template/releases
2. Click "Create a new release"
3. Select tag: `v1.0.0`
4. Release title: `v1.0.0 - Technical White Paper Writing Architecture`
5. Description:
   ```markdown
   ## Initial Release

   Complete Claude Code architecture for technical white paper writing.

   ### Features
   - 4 intelligent skills (outline, citations, abstract, draft-section)
   - 3 autonomous agents (research, validation, review)
   - 2 automation hooks (citation validation, bibliography tracking)
   - Complete documentation and customization guides

   ### Getting Started
   See [SETUP.md](SETUP.md) for installation instructions.

   ### What's Included
   - Professional voice descriptor template
   - IEEE/APA/Chicago citation support
   - Parallel research capabilities
   - Automated quality checks
   ```
6. Click "Publish release"

---

## 🔄 Future Updates

### Adding New Features

```bash
# Create feature branch
git checkout -b feature/new-skill

# Make changes
# ... edit files ...

# Commit changes
git add .
git commit -m "Add new skill: [skill-name]"

# Push branch
git push origin feature/new-skill

# Create pull request on GitHub
# Merge after review
```

### Bug Fixes

```bash
# Create fix branch
git checkout -b fix/citation-hook-bug

# Fix the issue
# ... edit files ...

# Commit fix
git add .
git commit -m "Fix: Citation hook not detecting [SOURCE-X] placeholders"

# Push and create PR
git push origin fix/citation-hook-bug
```

### Version Bumps

```bash
# After merging significant changes
git checkout main
git pull

# Tag new version
git tag -a v1.1.0 -m "Release v1.1.0: Added XYZ feature"
git push origin v1.1.0

# Create GitHub release (as above)
```

---

## 📊 Repository Settings

### Recommended GitHub Settings

**General:**
- ✅ Enable "Issues"
- ✅ Enable "Discussions" (optional, for community Q&A)
- ✅ Add topics: `claude-code`, `technical-writing`, `white-paper`, `ai-tools`, `documentation`

**Branch Protection:**
- Protect `main` branch
- Require pull request reviews (if collaborating)
- Require status checks to pass

**Description:**
```
AI-powered technical white paper writing architecture for Claude Code. Includes skills, agents, and automation for research, writing, and quality review.
```

**Website:**
```
https://github.com/brianbaping/tech-writer-template
```

**Topics to Add:**
- `claude-code`
- `technical-writing`
- `documentation`
- `white-paper`
- `ai-tools`
- `llm`
- `automation`
- `research-tools`

---

## ✅ Final Checklist

Before making the repository public:

- [ ] All documentation proofread
- [ ] No sensitive information in files
- [ ] No API keys or credentials
- [ ] Test: Clone repo fresh and follow SETUP.md
- [ ] README.md badges work correctly
- [ ] All links in documentation work
- [ ] LICENSE file is correct
- [ ] .gitignore excludes sensitive/generated files
- [ ] Repository description and topics set

---

## 🎉 Ready to Push!

Your architecture is now ready for GitHub. Follow the "Git Commands" section above to commit and push.

After pushing, share your repository:
- Claude Code community
- Technical writing forums
- Dev.to article
- Twitter/LinkedIn announcement

**Repository URL:** https://github.com/brianbaping/tech-writer-template
