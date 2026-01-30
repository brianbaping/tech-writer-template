---
name: tables
description: Generate professional tables for technical documents including comparison tables, feature matrices, technical specifications, and data presentations. Use when content needs structured tabular format for clarity and comparison.
---

# Table Generation Skill

## Overview

This skill helps create well-formatted, professional tables for technical white papers. Tables are essential for presenting comparisons, specifications, features, and structured data in a clear, scannable format.

## When to Use Tables

Use tables when you need to:
- Compare multiple options, products, or approaches
- Present technical specifications or parameters
- Show feature matrices or capability comparisons
- Display structured data (metrics, results, configurations)
- List requirements, constraints, or criteria
- Present decision matrices or scoring rubrics

**Rule of thumb:** If you're listing 3+ items with 2+ attributes each, consider a table.

## Table Types and Templates

### 1. Comparison Table

**Best for:** Comparing products, approaches, technologies, or solutions

**Template:**
```markdown
| Feature/Aspect | Option A | Option B | Option C |
|----------------|----------|----------|----------|
| **Criterion 1** | Value | Value | Value |
| **Criterion 2** | Value | Value | Value |
| **Criterion 3** | Value | Value | Value |
| **Best For** | Use case | Use case | Use case |
```

**Example:**
```markdown
| Feature | With Framework | Without Framework |
|---------|---------------|-------------------|
| **Context Management** | Isolated subagents | Single context |
| **Scalability** | High (parallel) | Limited (sequential) |
| **Complexity** | Moderate | High |
| **Best For** | Complex workflows | Simple tasks |
```

### 2. Feature Matrix

**Best for:** Showing which features are available in different versions/tiers

**Template:**
```markdown
| Feature | Basic | Pro | Enterprise |
|---------|-------|-----|------------|
| Feature 1 | ✅ | ✅ | ✅ |
| Feature 2 | ❌ | ✅ | ✅ |
| Feature 3 | ❌ | ❌ | ✅ |
| Feature 4 | ❌ | ❌ | ✅ |
```

**Symbols:**
- ✅ = Available/Yes
- ❌ = Not available/No
- ⚠️ = Partial/Limited
- ⭐ = Recommended/Best choice
- 💰 = Paid/Premium

### 3. Technical Specifications

**Best for:** Hardware specs, API parameters, system requirements

**Template:**
```markdown
| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| **Parameter 1** | 100 | MB | Description |
| **Parameter 2** | 50 | ms | Description |
| **Parameter 3** | 256 | bits | Description |
```

**Example:**
```markdown
| Component | Specification | Notes |
|-----------|--------------|-------|
| **Model** | Claude Sonnet | Default |
| **Context Window** | 200K tokens | Maximum |
| **Cache Support** | Yes | 5-minute TTL |
| **Tool Access** | Configurable | Per agent |
```

### 4. Decision Matrix

**Best for:** Evaluating options with weighted criteria

**Template:**
```markdown
| Criterion | Weight | Option A | Option B | Option C |
|-----------|--------|----------|----------|----------|
| **Criterion 1** | High | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Criterion 2** | Medium | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Criterion 3** | Low | ⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Total Score** | - | 8 | 7 | 8 |
```

### 5. Timeline/Roadmap Table

**Best for:** Project phases, milestones, releases

**Template:**
```markdown
| Phase | Timeline | Deliverables | Status |
|-------|----------|--------------|--------|
| **Phase 1** | Q1 2024 | Items | ✅ Complete |
| **Phase 2** | Q2 2024 | Items | 🔄 In Progress |
| **Phase 3** | Q3 2024 | Items | 📅 Planned |
```

### 6. Requirements Table

**Best for:** System requirements, prerequisites, dependencies

**Template:**
```markdown
| Component | Minimum | Recommended | Required |
|-----------|---------|-------------|----------|
| **CPU** | 2 cores | 4 cores | Yes |
| **RAM** | 4 GB | 8 GB | Yes |
| **Storage** | 10 GB | 20 GB | Yes |
| **OS** | Linux/Mac | Any | Yes |
```

### 7. API Endpoint Table

**Best for:** REST APIs, method documentation

**Template:**
```markdown
| Endpoint | Method | Parameters | Response | Auth |
|----------|--------|------------|----------|------|
| `/api/users` | GET | `page`, `limit` | User list | Required |
| `/api/users/:id` | GET | `id` | User object | Required |
| `/api/users` | POST | User data | Created user | Required |
```

### 8. Results/Metrics Table

**Best for:** Benchmarks, test results, performance data

**Template:**
```markdown
| Test Case | Baseline | Optimized | Improvement |
|-----------|----------|-----------|-------------|
| **Test 1** | 100 ms | 50 ms | 50% faster |
| **Test 2** | 200 ms | 75 ms | 62.5% faster |
| **Test 3** | 150 ms | 60 ms | 60% faster |
| **Average** | 150 ms | 62 ms | 58% faster |
```

## Formatting Guidelines

### Alignment

```markdown
| Left-aligned | Center-aligned | Right-aligned |
|:-------------|:--------------:|--------------:|
| Text | Text | Numbers |
| Text | Text | 1,234 |

# Left: :---
# Center: :---:
# Right: ---:
```

### Column Width

**Keep columns balanced:**
- Short labels: 10-15 characters
- Medium content: 15-30 characters
- Long content: 30-50 characters
- Break very long content into multiple rows

### Header Emphasis

Make headers bold or use title case:
```markdown
| **Header One** | **Header Two** | **Header Three** |
```

Or:
```markdown
| Component | Description | Status |
```

## Best Practices

### 1. Keep It Simple
- ❌ Don't: 10+ columns (hard to read)
- ✅ Do: 3-6 columns (scannable)
- If you need more columns, consider splitting into multiple tables

### 2. Use Consistent Formatting
- Same symbols throughout document (✅/❌ not ✓/✗/yes/no mixed)
- Consistent capitalization in headers
- Consistent alignment per column type

### 3. Add Context
Always add:
- **Table title/caption** above or below
- **Legend** if using symbols (e.g., "✅ = Available, ❌ = Not available")
- **Notes** for important clarifications

**Example:**
```markdown
**Table 1: Feature Comparison**

| Feature | Plan A | Plan B |
|---------|--------|--------|
| Feature 1 | ✅ | ✅ |
| Feature 2 | ❌ | ✅ |

*Legend: ✅ Available, ❌ Not available*
```

### 4. Number Tables

For documents with multiple tables:
```markdown
**Table 1:** System Requirements
**Table 2:** Performance Metrics
**Table 3:** API Endpoints
```

Then reference in text: "As shown in Table 2..."

### 5. Sort Logically

Order rows by:
- **Importance** (most important first)
- **Alphabetically** (for long lists)
- **Chronologically** (for timelines)
- **Hierarchically** (for nested items)
- **By score/value** (highest to lowest)

### 6. Use Visual Hierarchy

```markdown
| Category | Subcategory | Details |
|----------|-------------|---------|
| **Category 1** | | |
| | Subcategory A | Details |
| | Subcategory B | Details |
| **Category 2** | | |
| | Subcategory C | Details |
```

## Common Patterns

### Pattern 1: Before/After Comparison

```markdown
| Aspect | Before | After | Improvement |
|--------|--------|-------|-------------|
| Speed | 100ms | 25ms | 4x faster |
| Memory | 512MB | 128MB | 75% reduction |
| Cost | $100 | $25 | 75% savings |
```

### Pattern 2: Pros/Cons

```markdown
| Approach | Pros | Cons | Best For |
|----------|------|------|----------|
| **Approach A** | • Fast<br>• Simple | • Limited | Small projects |
| **Approach B** | • Flexible<br>• Scalable | • Complex | Large projects |
```

### Pattern 3: Compatibility Matrix

```markdown
| Feature | Windows | macOS | Linux |
|---------|---------|-------|-------|
| Feature 1 | ✅ | ✅ | ✅ |
| Feature 2 | ✅ | ⚠️ | ✅ |
| Feature 3 | ❌ | ✅ | ✅ |

*⚠️ = Limited support*
```

### Pattern 4: Version Comparison

```markdown
| Feature | v1.0 | v2.0 | v3.0 (Current) |
|---------|------|------|----------------|
| Feature 1 | ✅ | ✅ | ✅ |
| Feature 2 | ❌ | ✅ | ✅ |
| Feature 3 | ❌ | ❌ | ✅ |
```

## Workflow: Creating a Table

### Step 1: Identify the Content

What are you comparing/showing?
- Features, options, specifications, results?
- How many items (rows)?
- How many attributes (columns)?

### Step 2: Choose Table Type

Match your content to a template:
- Comparing options → Comparison Table
- Listing features by tier → Feature Matrix
- Showing specs → Technical Specifications
- Presenting results → Results/Metrics Table

### Step 3: Draft the Structure

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1 content | | |
| Row 2 content | | |
```

### Step 4: Fill in Content

Add data systematically:
1. Fill headers
2. Fill first column (row labels)
3. Fill remaining cells row by row
4. Add totals/summaries if needed

### Step 5: Format and Polish

- Align columns appropriately
- Add bold/emphasis where needed
- Verify symbols are consistent
- Add table caption and legend

### Step 6: Review

Check:
- ✅ All cells filled (no empty cells unless intentional)
- ✅ Consistent formatting
- ✅ Headers are clear
- ✅ Table is referenced in text
- ✅ Legend provided if using symbols

## Advanced: Complex Tables

### Grouped Headers

For complex data, group related columns:

```markdown
| Metric | **Baseline** | | **Optimized** | | **Improvement** |
|--------|-------------|-------------|--------------|-------------|-----------------|
| | Value | Unit | Value | Unit | % |
| CPU | 80 | % | 40 | % | 50% reduction |
| Memory | 512 | MB | 256 | MB | 50% reduction |
```

### Multi-line Cells

Use `<br>` for line breaks within cells:

```markdown
| Feature | Description |
|---------|-------------|
| **Multi-line** | Line one<br>Line two<br>Line three |
```

### Nested Lists in Tables

```markdown
| Component | Features |
|-----------|----------|
| **SDK** | • Context management<br>• Tool ecosystem<br>• Session handling |
| **Skills** | • Progressive disclosure<br>• Model-invoked<br>• Portable |
```

## Common Mistakes to Avoid

❌ **Too many columns** (unreadable)
✅ Split into multiple tables or transpose

❌ **Inconsistent symbols** (✅/yes/true mixed)
✅ Pick one symbol set and stick with it

❌ **No table caption**
✅ Always label tables for reference

❌ **Empty cells without explanation**
✅ Use "N/A", "—", or explain in legend

❌ **Unaligned columns** (hard to scan)
✅ Proper markdown table formatting

❌ **Too much text in cells**
✅ Keep cells concise, move details to text

## Table Checklist

Before finalizing a table:

- [ ] Table has a clear caption/title
- [ ] Headers are descriptive and bold
- [ ] All cells are filled (or marked N/A)
- [ ] Alignment is appropriate (left for text, right for numbers)
- [ ] Symbols have a legend
- [ ] Table is referenced in surrounding text
- [ ] Formatting is consistent
- [ ] Table fits on page (not too wide)
- [ ] Data is accurate and current
- [ ] Sources cited if using external data

## Resources

- [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables)
- [ASCII Table Generator](https://ozh.github.io/ascii-tables/)

---

**Remember:** Good tables enhance understanding. Bad tables create confusion. When in doubt, keep it simple and add a clear caption.
