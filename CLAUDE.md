# White Paper Writing Guidelines

This document defines the voice, style, and conventions for writing white papers in this project. All skills, agents, and conversations will follow these guidelines to ensure consistency.

---

## Voice & Tone

**Target Audience:** Technical decision-makers (CTOs, Engineering Managers, Senior Developers) who need to understand both technical details and business implications.

**Writing Voice:**
- **Professional but accessible** - Avoid overly academic jargon while maintaining technical credibility
- **Authoritative yet conversational** - Position as expert, but write like you're explaining to a colleague
- **Clear and direct** - Get to the point quickly, respect the reader's time
- **Evidence-based** - Support claims with data, examples, and concrete evidence

**Tone Characteristics:**
- Use "we" for inclusive tone when discussing shared industry challenges
- Use active voice predominantly (passive voice <20% of sentences)
- Vary sentence length for readability (mix short punchy sentences with longer explanatory ones)
- Be confident but acknowledge limitations and tradeoffs
- Show, don't just tell (use examples liberally)

---

## Writing Conventions

### Grammar & Style
- **Oxford comma:** Always use (e.g., "skills, agents, and hooks")
- **Acronyms:** Spell out on first use, then use acronym (e.g., "Model Context Protocol (MCP)")
- **Numbers:** Spell out one through nine, use numerals for 10+
- **Contractions:** Minimal use, only when it improves readability
- **Person:** Use second person ("you") when addressing reader directly, third person for general statements

### Technical Formatting
- **Code blocks:** Always include language identifier
  ```python
  # Good
  ```
  Not just generic code blocks

- **File paths:** Use backticks and absolute paths when specific (e.g., `.claude/skills/SKILL.md`)
- **Tool names:** Capitalize consistently (e.g., Task tool, Read tool, Bash tool)
- **Commands:** Use backticks (e.g., `git commit`, `/outline`)

### Citations & References
- **Citation style:** IEEE format with numbered brackets [1], [2]
- **In-text citations:** Place at end of sentence before period
- **Bibliography:** Full citations at end of document
- **URLs:** Include access date for web sources

---

## Content Structure

### Section Organization
1. **Start with concrete examples** before diving into theory
2. **Use subheadings liberally** to break up long sections (every 3-4 paragraphs)
3. **Include real-world use cases** to illustrate abstract concepts
4. **End sections with key takeaways** when appropriate

### Paragraphs
- **Topic sentence first** - State the main point upfront
- **Support with evidence** - Follow with examples, data, or explanation
- **Transition smoothly** - Connect to next paragraph or section
- **Keep reasonable length** - Aim for 3-5 sentences per paragraph

### Lists & Tables
- **Use bullet points** for unordered information
- **Use numbered lists** for sequential steps or ranked items
- **Use tables** for comparisons or structured data
- **Introduce lists** with a lead-in sentence

---

## Technical Depth Guidelines

**Balance is critical:** Technical enough for engineers, accessible enough for managers.

### When to Go Deep
- Novel technical architectures or implementations
- Performance implications and benchmarks
- Security considerations
- Integration details

### When to Stay High-Level
- Well-known concepts (link to external resources instead)
- Background/context sections
- Executive summaries
- Introductory sections

### Always Include
- **Concrete examples** for abstract concepts
- **Code samples** for implementation guidance
- **Diagrams** for complex relationships or workflows (prefer Mermaid syntax)
- **Performance data** when making claims about efficiency

---

## Prohibited Patterns

**Avoid these common pitfalls:**

- **Marketing language:** No hyperbole, superlatives without evidence, or promotional tone
- **Weasel words:** Avoid "simply," "just," "obviously," "clearly," "everyone knows"
- **Absolutes without evidence:** "always," "never," "impossible" (unless provably true)
- **Gendered language:** Use "they/them" for generic users, avoid "he/she"
- **Passive voice overuse:** Active voice makes writing clearer and more direct
- **Unexplained jargon:** Define technical terms or link to definitions
- **Vague statements:** "Significant improvement" → "40% faster execution time"

---

## Specific Preferences

### Code Examples
- Keep examples short and focused (5-20 lines ideal)
- Include comments explaining non-obvious logic
- Show realistic scenarios, not trivial "hello world" examples
- Provide context: what problem does this solve?

### Diagrams & Visuals
- Use Mermaid for architecture diagrams, flowcharts, sequence diagrams
- Always include descriptive caption
- Reference diagrams in text ("as shown in Figure 1")
- Keep diagrams simple - one concept per diagram

### Data & Statistics
- **Always cite sources** for statistics and data
- **Include context:** "40% faster" → "40% faster than the baseline approach (from 10s to 6s)"
- **Show methodology:** How was this measured?
- **Acknowledge limitations:** Sample size, test conditions, etc.

---

## Review Checklist

Before considering a section complete, verify:

- [ ] Clear topic sentence opens each paragraph
- [ ] Technical claims are supported with evidence
- [ ] Acronyms are spelled out on first use
- [ ] Code blocks include language identifiers
- [ ] Citations are properly formatted [1]
- [ ] No prohibited patterns (weasel words, marketing language)
- [ ] Active voice used predominantly
- [ ] Examples illustrate abstract concepts
- [ ] Transitions connect ideas smoothly
- [ ] Subheadings break up long sections

---

## Agent & Skill Specific Notes

**For research agents:**
- Prioritize sources from last 3 years (unless discussing historical context)
- Favor peer-reviewed sources, then technical documentation, then expert blogs
- Note conflicting viewpoints in research notes
- Flag gaps in current research

**For draft generation skills:**
- Follow all voice and tone guidelines above
- Use placeholder citations [SOURCE-X] if source isn't immediately available
- Mark areas needing further research with [TODO: research X]
- Generate multiple heading variations for review

**For review agents:**
- Check adherence to this guide
- Flag passive voice overuse
- Identify unsupported claims
- Suggest specific improvements (not just "this could be better")

---

*This guide is a living document. Update as you discover additional preferences or patterns during the writing process.*
