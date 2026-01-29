# Technical White Paper Writing Architecture

> A complete Claude Code system for professional technical white paper development

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-blue)](https://claude.ai)

**Transform your white paper writing with AI-powered skills, autonomous agents, and automated quality checks.**

---

## 🎯 What This Is

A production-ready Claude Code architecture that streamlines every phase of white paper development:

- **4 Skills** - Automatic invocation for outlines, citations, abstracts, and drafts
- **3 Agents** - Autonomous research, citation validation, and technical review
- **2 Automation Hooks** - Real-time citation validation and bibliography tracking
- **Complete Voice Control** - Customizable style guidelines shared across all components

**Perfect for:** Technical writers, developer advocates, researchers, and anyone writing professional technical documentation.

---

## ✨ Features

### 🤖 Intelligent Skills

| Skill | Purpose | Invocation |
|-------|---------|------------|
| `/outline` | Generate structured white paper outlines | Automatic or `/outline [topic]` |
| `/citations` | Format citations (IEEE/APA/Chicago) | `/citations [style] [source]` |
| `/abstract` | Write executive summaries | `/abstract [file]` |
| `/draft-section` | Expand outlines into prose | `/draft-section [section]` |

### 🚀 Autonomous Agents

| Agent | Model | Purpose |
|-------|-------|---------|
| `@academic-researcher` | Haiku | Parallel literature review & source gathering |
| `@citation-validator` | Sonnet | Verify citation completeness & format |
| `@technical-reviewer` | Opus | Comprehensive technical quality review |

### ⚡ Automation

- **Citation Validation Hook** - Warns about placeholder citations and format issues
- **Bibliography Tracking Hook** - Automatically logs all web sources for easy citation

### 🎨 Customizable

- **Voice descriptor** (`CLAUDE.md`) shared across all skills and agents
- **Flexible citation styles** (IEEE, APA, Chicago)
- **Adjustable technical depth** for different audiences
- **Project-specific** - each white paper can have unique guidelines

---

## 🚀 Quick Start

### Prerequisites

- [Claude Code](https://claude.ai/code) installed and configured
- Basic familiarity with Claude Code skills and agents

### Installation

```bash
# Clone the repository
git clone https://github.com/brianbaping/tech-writer-template.git
cd tech-writer-template

# Make hooks executable
chmod +x .claude/hooks/*.sh

# Customize for your project
cp CLAUDE.template.md CLAUDE.md
# Edit CLAUDE.md with your preferences

# Start writing!
```

### First Steps

1. **Research your topic:**
   ```
   @academic-researcher research multi-agent AI architectures
   ```

2. **Generate an outline:**
   ```
   /outline using research from .claude/cache/
   ```

3. **Write collaboratively or use draft skill:**
   ```
   /draft-section Introduction
   ```

4. **Validate and review:**
   ```
   @citation-validator check whitepaper.md
   @technical-reviewer review whitepaper.md
   ```

**See [HOW-TO-USE.md](HOW-TO-USE.md) for complete workflows and examples.**

### Working with Existing Documents?

If you have a folder of source documents (meeting notes, specs, research) that need to be transformed into a white paper:

📘 **[EXAMPLE-USAGE.md](EXAMPLE-USAGE.md)** - Complete workflow for turning source documents into professional white papers

**Quick preview:**
```
1. Point Claude at your source-docs/ folder
2. Generate outline from existing content
3. Draft sections using your documents
4. Validate and review
5. Professional white paper ready!
```

---

## 📁 Architecture Overview

```
tech-writer-template/
├── CLAUDE.template.md          # Voice & style template (customize this!)
├── HOW-TO-USE.md              # Complete usage guide
├── SETUP.md                   # Installation & customization guide
├── README.md                  # This file
│
└── .claude/
    ├── skills/                # 4 skills for writing tasks
    │   ├── outline/
    │   ├── citations/
    │   ├── abstract/
    │   └── draft-section/
    │
    ├── agents/                # 3 agents for complex workflows
    │   ├── academic-researcher.md
    │   ├── citation-validator.md
    │   └── technical-reviewer.md
    │
    ├── hooks/                 # 2 automation scripts
    │   ├── validate-citation-format.sh
    │   └── track-bibliography.sh
    │
    ├── cache/                 # Generated reports (created during use)
    │
    └── settings.local.json    # Configuration
```

---

## 📖 Documentation

- **[SETUP.md](SETUP.md)** - Detailed installation and customization guide
- **[HOW-TO-USE.md](HOW-TO-USE.md)** - Complete workflows with examples
- **[EXAMPLE-USAGE.md](EXAMPLE-USAGE.md)** - Transform existing documents into white papers
- **[CLAUDE.template.md](CLAUDE.template.md)** - Voice descriptor template

---

## 🎯 Use Cases

### Academic Research Papers
- Strict citation requirements
- Peer-reviewed source preference
- Formal academic tone
- Multiple co-authors

### Technical White Papers
- Balanced technical depth
- IEEE citation format
- Professional but accessible
- Code examples and benchmarks

### Business White Papers
- Executive-friendly language
- ROI-focused content
- APA citation style
- Persuasive tone

### Internal Documentation
- Company-specific terminology
- Informal citation style
- Practical, direct tone
- Integration with internal sources

---

## 💡 Key Benefits

✅ **Save Time** - Autonomous agents handle research and validation in parallel
✅ **Ensure Quality** - Automated reviews catch errors before publication
✅ **Maintain Consistency** - Shared voice guidelines across all components
✅ **Stay Focused** - Automation handles tedious tasks, you focus on content
✅ **Collaborate Better** - Version control your writing process and guidelines

---

## 🛠️ Customization

### Quick Customization

1. Copy `CLAUDE.template.md` to `CLAUDE.md`
2. Customize five key sections:
   - Target audience
   - Writing voice
   - Citation style (IEEE/APA/Chicago)
   - Prohibited patterns
   - Review checklist

### Advanced Customization

- **Skills** - Edit `.claude/skills/[name]/SKILL.md` to change behavior
- **Agents** - Modify `.claude/agents/[name].md` to adjust tools or models
- **Hooks** - Update `.claude/hooks/*.sh` for custom validation rules

**See [SETUP.md](SETUP.md) for detailed customization examples.**

---

## 🔄 Workflow Example

```bash
# Day 1: Research (parallel agents)
@academic-researcher research topic A
@academic-researcher research topic B
@academic-researcher research topic C

# Day 2: Planning
/outline using research notes

# Day 3-5: Writing
/draft-section Introduction
[Collaborative writing with Claude for strategic sections]
/citations ieee [sources]

# Day 6: Validation
@citation-validator check whitepaper.md

# Day 7: Review
@technical-reviewer review whitepaper.md

# Day 8: Finalize
/abstract whitepaper.md
```

---

## 🤝 Contributing

Contributions welcome! Areas for improvement:

- Additional citation styles (MLA, Vancouver, etc.)
- More specialized agents (code validator, diagram generator)
- Integration with reference managers (Zotero, Mendeley)
- Additional output formats (LaTeX, Markdown variants)

Please open an issue or pull request.

---

## 📜 License

[MIT License](LICENSE) - feel free to use, modify, and distribute.

---

## 🌟 Why This Architecture?

**Traditional writing workflow:**
- Manual research across multiple sources
- Copy-paste citations with inconsistent formatting
- Self-review (easy to miss errors)
- Linear process (can't parallelize)

**With this architecture:**
- ✅ Agents research in parallel while you work
- ✅ Automatic citation formatting and validation
- ✅ AI-powered technical review (like having a senior editor)
- ✅ Automated quality checks throughout

**Result:** Write better white papers, faster, with fewer errors.

---

## 📞 Support

- **Documentation:** See [HOW-TO-USE.md](HOW-TO-USE.md) and [SETUP.md](SETUP.md)
- **Issues:** [GitHub Issues](https://github.com/brianbaping/tech-writer-template/issues)
- **Questions:** Open a discussion or issue

---

## 🎓 Learn More

- [Claude Code Documentation](https://docs.claude.com/claude-code)
- [Understanding Skills vs Agents](HOW-TO-USE.md#reference-when-to-use-each-component)
- [Customization Examples](SETUP.md#project-specific-setup-examples)

---

## ⭐ Show Your Support

If this architecture helps your writing workflow, please:
- ⭐ Star this repository
- 🔄 Share with your network
- 🐛 Report issues or suggest improvements
- 🤝 Contribute enhancements

---

**Built for technical writers by technical writers, powered by Claude Code.**

*Start writing professional white papers with AI assistance today.*

[Get Started](SETUP.md) | [View Documentation](HOW-TO-USE.md) | [Report Issue](https://github.com/brianbaping/tech-writer-template/issues)
