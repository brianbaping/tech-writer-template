---
name: bibliography
description: Generate and format References/Bibliography sections for technical documents. Collects citations, validates completeness, formats according to style (IEEE/APA/Chicago), and ensures all in-text citations have matching references.
---

# Bibliography Generation Skill

## Overview

This skill helps create professional References/Bibliography sections for technical white papers. It collects all citations used in your document, formats them according to academic standards, validates completeness, and generates a properly structured References section.

## When to Use This Skill

Use this skill when you need to:
- Generate a References section from in-text citations
- Format citations according to IEEE, APA, or Chicago style
- Validate that all citations have complete reference information
- Check for duplicate or missing references
- Alphabetize or number references appropriately
- Convert between citation styles

**Rule of thumb:** Use after drafting is complete, before final review.

## Citation Styles Supported

### IEEE Style (Numbered)

**Best for:** Engineering, computer science, technical papers

**In-text format:**
```markdown
The framework provides extensibility [1].
Multiple citations can be combined [2], [3], [4].
```

**Reference format:**
```
[1] A. Author, "Title of paper," Conference/Journal Name, vol. X, no. Y, pp. 100-105, Month Year.
[2] A. Author and B. Author, "Article title," Journal Name, vol. X, pp. 100-105, Year.
[3] A. Author, Book Title. City: Publisher, Year.
[4] "Web page title," Organization. URL (accessed Month Day, Year).
```

**Ordering:** Numbered by order of first appearance in text

### APA Style (Author-Date)

**Best for:** Business, social sciences, psychology, business white papers

**In-text format:**
```markdown
The framework provides extensibility (Smith, 2024).
Multiple authors (Smith & Jones, 2024).
Multiple citations (Smith, 2024; Jones, 2023).
```

**Reference format:**
```
Smith, J. (2024). Title of article. Journal Name, 10(2), 100-105. https://doi.org/10.xxxx

Smith, J., & Jones, M. (2024). Book title. Publisher.

Smith, J. (2024, January 15). Web page title. Organization Name. https://example.com
```

**Ordering:** Alphabetical by author last name

### Chicago Style (Notes/Bibliography)

**Best for:** Humanities, history, general academic writing

**In-text format:**
```markdown
The framework provides extensibility.¹
Multiple citations can be included.²,³
```

**Reference format:**
```
1. John Smith, "Title of Article," Journal Name 10, no. 2 (2024): 100-105.

2. John Smith and Mary Jones, Book Title (City: Publisher, 2024), 50-55.

3. "Web Page Title," Organization Name, accessed January 15, 2024, https://example.com.
```

**Ordering:** Numbered by order of appearance

## Reference Types and Templates

### 1. Journal Article

**IEEE:**
```
[1] A. Author, B. Coauthor, and C. Coauthor, "Article title," Journal Name, vol. X, no. Y, pp. 100-105, Month Year. [Online]. Available: URL
```

**APA:**
```
Author, A., Coauthor, B., & Coauthor, C. (Year). Article title. Journal Name, Volume(Issue), 100-105. https://doi.org/10.xxxx
```

**Chicago:**
```
1. Author Name, Coauthor Name, and Coauthor Name. "Article Title." Journal Name Volume, no. Issue (Year): 100-105.
```

### 2. Conference Paper

**IEEE:**
```
[1] A. Author, "Paper title," in Proc. Conference Name, City, Country, Year, pp. 100-105.
```

**APA:**
```
Author, A. (Year). Paper title. In Conference Name (pp. 100-105). Publisher.
```

**Chicago:**
```
1. Author Name, "Paper Title" (paper presentation, Conference Name, City, Month Year).
```

### 3. Book

**IEEE:**
```
[1] A. Author, Book Title, Edition. City: Publisher, Year.
```

**APA:**
```
Author, A. (Year). Book title (Edition ed.). Publisher.
```

**Chicago:**
```
1. Author Name. Book Title. Edition. City: Publisher, Year.
```

### 4. Book Chapter

**IEEE:**
```
[1] A. Author, "Chapter title," in Book Title, Editor, Ed. City: Publisher, Year, ch. X, pp. 100-120.
```

**APA:**
```
Author, A. (Year). Chapter title. In Editor Name (Ed.), Book title (pp. 100-120). Publisher.
```

**Chicago:**
```
1. Author Name. "Chapter Title." In Book Title, edited by Editor Name, 100-120. City: Publisher, Year.
```

### 5. Website/Blog Post

**IEEE:**
```
[1] Author or Organization, "Page title," Site Name. URL (accessed Month Day, Year).
```

**APA:**
```
Author, A. (Year, Month Day). Page title. Site Name. https://example.com
```

**Chicago:**
```
1. Author Name or Organization. "Page Title." Site Name. Accessed Month Day, Year. https://example.com.
```

### 6. Technical Report

**IEEE:**
```
[1] A. Author, "Report title," Organization, City, Country, Tech. Rep. Number, Month Year.
```

**APA:**
```
Author, A. (Year). Report title (Report No. XXX). Organization Name.
```

**Chicago:**
```
1. Author Name. "Report Title." Technical Report Number, Organization Name, City, Year.
```

### 7. GitHub Repository

**IEEE:**
```
[1] Author or Organization, "Repository name," GitHub. URL (accessed Month Day, Year).
```

**APA:**
```
Author, A. (Year). Repository name [Computer software]. GitHub. https://github.com/user/repo
```

**Chicago:**
```
1. Author Name or Organization. "Repository Name." GitHub, Year. https://github.com/user/repo.
```

### 8. API Documentation

**IEEE:**
```
[1] Organization, "API name documentation," Version. URL (accessed Month Day, Year).
```

**APA:**
```
Organization. (Year). API name documentation (Version X.X) [API documentation]. https://example.com
```

**Chicago:**
```
1. Organization. "API Name Documentation." Version X.X. Accessed Month Day, Year. https://example.com.
```

## Workflow: Generating a Bibliography

### Step 1: Collect All Citations

Search through your document for citation markers:

**IEEE style:**
```bash
# Find all [N] citations
grep -oE '\[[0-9]+\]' document.md | sort -u
```

**APA style:**
```bash
# Find all (Author, Year) citations
grep -oE '\([A-Z][a-z]+.*[0-9]{4}\)' document.md
```

Make a list of all unique citations that need references.

### Step 2: Extract Citation Information

For each citation, gather:
- **Author(s)** - Full names (First Last)
- **Year** - Publication year
- **Title** - Article/book/page title
- **Source** - Journal, conference, website, etc.
- **Volume/Issue** - For journals
- **Pages** - Page range if applicable
- **Publisher** - For books
- **URL** - For online sources
- **DOI** - If available (preferred for academic papers)
- **Access Date** - For web sources

### Step 3: Format Each Reference

Use the appropriate template for the citation style:

**Example for IEEE:**
```markdown
## References

[1] J. Doe, "Introduction to AI agents," in Proc. Int. Conf. Artificial Intelligence, San Francisco, CA, USA, 2024, pp. 10-15.

[2] M. Smith and J. Johnson, "Multi-agent systems," AI Journal, vol. 15, no. 3, pp. 200-215, Mar. 2024.

[3] Anthropic, "Claude API documentation." https://docs.anthropic.com/claude/reference (accessed Jan. 15, 2024).
```

**Example for APA:**
```markdown
## References

Anthropic. (2024, January 15). Claude API documentation. https://docs.anthropic.com/claude/reference

Doe, J. (2024). Introduction to AI agents. In International Conference on Artificial Intelligence (pp. 10-15). IEEE.

Smith, M., & Johnson, J. (2024). Multi-agent systems. AI Journal, 15(3), 200-215.
```

**Example for Chicago:**
```markdown
## References

1. Doe, John. "Introduction to AI Agents." Paper presented at International Conference on Artificial Intelligence, San Francisco, CA, January 2024.

2. Smith, Mary, and John Johnson. "Multi-agent Systems." AI Journal 15, no. 3 (2024): 200-215.

3. Anthropic. "Claude API Documentation." Accessed January 15, 2024. https://docs.anthropic.com/claude/reference.
```

### Step 4: Order References

**IEEE:** Number by order of first appearance in document
- Citation [1] should be the first reference cited
- Citation [2] should be the second, etc.

**APA:** Alphabetize by author last name
- Multiple works by same author: chronologically (oldest first)
- Same author, same year: add letters (2024a, 2024b)

**Chicago:** Number by order of appearance (like IEEE)

### Step 5: Validate Completeness

Check that:
- ✅ Every in-text citation has a matching reference
- ✅ Every reference has all required fields
- ✅ URLs are working and correctly formatted
- ✅ Author names are consistent throughout
- ✅ Years match between in-text and reference list
- ✅ No duplicate entries
- ✅ Formatting is consistent

## Common Issues and Fixes

### Issue 1: Missing Author

**Problem:** Web page has no clear author

**Solutions:**
- Use organization name as author
- Use "Anonymous" if truly unknown
- Use website name as author

**Example:**
```
[1] Anthropic, "Claude overview," 2024. https://www.anthropic.com/claude
```

### Issue 2: Multiple Authors

**Rules by style:**

**IEEE:** List all authors up to 6, use "et al." for 7+
```
[1] A. Smith, B. Jones, C. Lee, et al., "Title..."
```

**APA:** List up to 20 authors, use ellipsis for 21+
```
Smith, A., Jones, B., Lee, C., ... & Last, Z. (2024). Title...
```

**Chicago:** List all authors, or use "et al." after 4+
```
1. Smith, Jones, Lee, Brown, et al. "Title..."
```

### Issue 3: No Publication Date

**Solutions:**
- Use "(n.d.)" for "no date" in APA
- Use access date for web sources
- Check Internet Archive for archived version with date

**Example (APA):**
```
Smith, J. (n.d.). Article title. Website Name. Retrieved January 15, 2024, from https://example.com
```

### Issue 4: Preprint/Unpublished

**IEEE:**
```
[1] A. Author, "Title," unpublished. [Online]. Available: URL
```

**APA:**
```
Author, A. (Year). Title [Unpublished manuscript]. University Name.
```

**Chicago:**
```
1. Author Name. "Title." Unpublished manuscript, last modified Month Day, Year.
```

### Issue 5: URL Too Long

**Solutions:**
- Use DOI instead if available (preferred)
- Use shortened URL (bit.ly, tinyurl) if acceptable
- Use base URL + path (omit query parameters)

**Example:**
```
# Instead of:
https://example.com/article/2024/01/15/very-long-title-with-many-words?utm_source=twitter&ref=123456

# Use:
https://example.com/article/2024/01/15/very-long-title
```

## Best Practices

### 1. Start Early

Don't wait until the end to collect citations:
- Add references as you write
- Keep a running list in a separate file
- Use consistent formatting from the start

### 2. Use DOIs When Available

DOIs are preferred over URLs for academic papers:
```
✅ https://doi.org/10.1234/abcd
❌ https://journal.com/article/view/12345
```

### 3. Be Consistent

- Same author name format throughout (A. Smith or Adam Smith, not mixed)
- Same date format (Jan. 2024 or January 2024, not mixed)
- Same URL format (with or without "Retrieved from")

### 4. Verify Access Dates

For web sources, use the date you actually accessed the page:
```
(accessed Jan. 15, 2024)  ← The date YOU viewed it
```

### 5. Check for Updates

Before finalizing:
- Verify URLs still work
- Check if preprints were published
- Update access dates if you re-checked sources

## Validation Checklist

Before finalizing your References section:

- [ ] Every in-text citation has a matching reference
- [ ] Every reference has all required fields (author, title, year, source)
- [ ] References are in correct order (numbered or alphabetized)
- [ ] Formatting is consistent (punctuation, capitalization, italics)
- [ ] Author names are formatted consistently
- [ ] URLs are working and complete
- [ ] Access dates are included for web sources
- [ ] DOIs are included where available
- [ ] No duplicate entries
- [ ] Abbreviations are consistent (Proc., Int., Conf., etc.)
- [ ] Volume/issue numbers are correct
- [ ] Page ranges use en-dashes (100–105, not 100-105)

## Advanced Features

### Converting Between Styles

**From IEEE to APA:**
1. Remove numbers [1], [2]
2. Change to (Author, Year) in text
3. Reorder references alphabetically
4. Reformat each reference to APA style

**From APA to IEEE:**
1. Remove (Author, Year) from text
2. Number citations by first appearance
3. Add [N] markers in text
4. Reformat references to IEEE style

### Handling Special Cases

**Multiple works by same author:**

**IEEE:** Number by appearance (no special treatment)
```
[1] A. Smith, "First paper," ...
[3] A. Smith, "Second paper," ...
```

**APA:** Alphabetize by title, add year letters if needed
```
Smith, A. (2024a). First paper...
Smith, A. (2024b). Second paper...
```

**Corporate authors:**
```
IEEE: [1] Google, "Title," ...
APA: Google. (2024). Title...
Chicago: 1. Google. "Title."
```

**No page numbers (online):**
```
IEEE: [1] A. Author, "Title," Journal, vol. X, Art. no. 123456, Year.
APA: Author, A. (Year). Title. Journal, Volume, Article 123456.
```

## Tools and Automation

### Bibliography File Template

Keep a `bibliography.txt` file during writing:

```
# Working Bibliography

## [1] Smith AI Paper
- Author: John Smith, Mary Jones
- Title: Multi-agent systems in production
- Source: AI Journal
- Volume: 15, Issue: 3
- Pages: 200-215
- Year: 2024
- DOI: 10.1234/aij.2024.001

## [2] Anthropic Docs
- Organization: Anthropic
- Title: Claude API documentation
- URL: https://docs.anthropic.com/claude/reference
- Accessed: January 15, 2024

## [3] Conference Paper
- Author: Jane Doe
- Title: Introduction to AI agents
- Conference: International Conference on Artificial Intelligence
- Location: San Francisco, CA, USA
- Pages: 10-15
- Year: 2024
```

Then format all at once using the appropriate style.

### Grep Commands for Validation

**Find all citations in document:**
```bash
# IEEE style [N]
grep -n '\[[0-9]\+\]' document.md

# APA style (Author, Year)
grep -n '([A-Z][a-z]\+.*[0-9]\{4\})' document.md
```

**Check for missing citations:**
```bash
# List all numbers used
grep -oE '\[[0-9]+\]' document.md | sort -u | tr -d '[]'

# Should be continuous: 1, 2, 3, ..., N
# If you see 1, 2, 4, 6 (missing 3, 5), investigate
```

**Find uncited references:**
```bash
# Compare reference numbers to in-text citations
# All reference numbers should appear in text
```

## Examples by Document Type

### Technical White Paper (IEEE)

```markdown
## References

[1] M. Wooldridge, An Introduction to Multi-Agent Systems, 2nd ed. Chichester, UK: Wiley, 2009.

[2] S. Russell and P. Norvig, Artificial Intelligence: A Modern Approach, 4th ed. Hoboken, NJ: Pearson, 2020.

[3] Anthropic, "Claude API documentation," 2024. https://docs.anthropic.com/claude/reference (accessed Jan. 15, 2024).

[4] J. Smith and M. Jones, "Scalable multi-agent architectures," in Proc. Int. Conf. Autonomous Agents and Multiagent Syst., Auckland, New Zealand, 2024, pp. 100-108.

[5] OpenAI, "GPT-4 technical report," arXiv:2303.08774, 2023. [Online]. Available: https://arxiv.org/abs/2303.08774
```

### Business White Paper (APA)

```markdown
## References

Anthropic. (2024, January 15). Claude overview. https://www.anthropic.com/claude

Russell, S., & Norvig, P. (2020). Artificial intelligence: A modern approach (4th ed.). Pearson.

Smith, J., & Jones, M. (2024). Scalable multi-agent architectures. In Proceedings of the International Conference on Autonomous Agents and Multiagent Systems (pp. 100-108). IFAAMAS.

Wooldridge, M. (2009). An introduction to multi-agent systems (2nd ed.). Wiley.
```

### Academic Paper (Chicago)

```markdown
## Bibliography

1. Anthropic. "Claude API Documentation." Accessed January 15, 2024. https://docs.anthropic.com/claude/reference.

2. Russell, Stuart, and Peter Norvig. Artificial Intelligence: A Modern Approach. 4th ed. Hoboken, NJ: Pearson, 2020.

3. Smith, John, and Mary Jones. "Scalable Multi-agent Architectures." In Proceedings of the International Conference on Autonomous Agents and Multiagent Systems, 100-108. Auckland, New Zealand, 2024.

4. Wooldridge, Michael. An Introduction to Multi-Agent Systems. 2nd ed. Chichester, UK: Wiley, 2009.
```

## Quality Checklist

Before finalizing:

**Completeness:**
- [ ] All in-text citations have references
- [ ] All required fields present (author, title, year, source)
- [ ] URLs verified and working
- [ ] DOIs included where available

**Formatting:**
- [ ] Correct style applied consistently (IEEE/APA/Chicago)
- [ ] Proper ordering (numbered or alphabetical)
- [ ] Consistent punctuation and capitalization
- [ ] Author names formatted consistently
- [ ] Italics used correctly (book titles, journal names)

**Accuracy:**
- [ ] Publication years correct
- [ ] Author names spelled correctly
- [ ] Titles match source exactly
- [ ] Volume/issue/page numbers verified
- [ ] No duplicate entries

**Professionalism:**
- [ ] Access dates within last 6 months
- [ ] Reputable sources cited
- [ ] Preprints updated if now published
- [ ] Broken links fixed or archived versions used

---

**Remember:** A well-formatted References section demonstrates scholarly rigor and allows readers to verify your sources. Invest time in getting it right, and use this skill to ensure professional quality.
