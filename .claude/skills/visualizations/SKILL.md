---
name: visualizations
description: Create professional diagrams, charts, and visual aids for technical documents including architecture diagrams, workflows, data visualizations, and system interactions. Use when writing technical content that would benefit from visual representation of concepts, relationships, processes, or data.
---

# Technical Document Visualization Skill

## Overview

This skill teaches you how to create professional diagrams and visualizations for technical documents. Visualizations enhance understanding of complex concepts, architectures, workflows, and data relationships.

## When to Use Visualizations

Add diagrams when:
- Explaining system architectures or component relationships
- Describing workflows, processes, or sequences
- Showing data flows or information paths
- Comparing options or approaches
- Illustrating hierarchies or organizational structures
- Presenting statistical data or trends
- Clarifying complex concepts that are hard to describe in text alone

**Rule of thumb:** If you're writing "as shown in the diagram" or "the following illustrates", you need a diagram.

## Visualization Types and Tools

### 1. Architecture Diagrams (Graphviz)

**Best for:** System components, relationships, dependencies, hierarchies

**Python Implementation:**
```python
import graphviz

def create_architecture_diagram(output_name):
    dot = graphviz.Digraph(
        comment='System Architecture',
        format='png',
        graph_attr={'rankdir': 'TB', 'splines': 'ortho', 'nodesep': '0.8', 'ranksep': '0.8'}
    )

    # Define node styles
    dot.attr('node', shape='box', style='rounded,filled', fillcolor='lightblue',
             fontname='Arial', fontsize='12')

    # Add nodes
    dot.node('SDK', 'Agent SDK\n(Foundation)', fillcolor='#4a90e2', fontcolor='white')
    dot.node('Sub', 'Subagents\n(Specialization)', fillcolor='#50c878', fontcolor='white')
    dot.node('Skills', 'Skills\n(Knowledge)', fillcolor='#f39c12', fontcolor='white')
    dot.node('Hooks', 'Hooks\n(Control)', fillcolor='#e74c3c', fontcolor='white')

    # Add edges
    dot.edge('SDK', 'Sub', label='spawns')
    dot.edge('SDK', 'Skills', label='uses')
    dot.edge('SDK', 'Hooks', label='triggers')
    dot.edge('Sub', 'Skills', label='accesses', style='dashed')
    dot.edge('Hooks', 'Sub', label='controls', style='dashed')

    # Render
    dot.render(output_name, cleanup=True)
    return f"{output_name}.png"
```

**Common Patterns:**
- Component diagrams: `rankdir='TB'` (top to bottom)
- Flow diagrams: `rankdir='LR'` (left to right)
- Hierarchies: Use `rankdir='TB'` with `ranksep='1.0'`

### 2. Workflow/Sequence Diagrams (Graphviz)

**Best for:** Process flows, sequences, state machines, decision trees

```python
def create_workflow_diagram(output_name):
    dot = graphviz.Digraph(
        format='png',
        graph_attr={'rankdir': 'LR'}
    )

    # Different shapes for different elements
    dot.attr('node', shape='box', style='rounded')
    dot.node('start', 'Start', shape='ellipse', fillcolor='lightgreen', style='filled')
    dot.node('step1', 'Gather Context')
    dot.node('step2', 'Take Action')
    dot.node('step3', 'Verify Results')
    dot.node('decision', 'Complete?', shape='diamond', fillcolor='lightyellow', style='filled')
    dot.node('end', 'End', shape='ellipse', fillcolor='lightcoral', style='filled')

    # Edges with labels
    dot.edge('start', 'step1')
    dot.edge('step1', 'step2')
    dot.edge('step2', 'step3')
    dot.edge('step3', 'decision')
    dot.edge('decision', 'end', label='Yes')
    dot.edge('decision', 'step1', label='No', style='dashed')

    dot.render(output_name, cleanup=True)
    return f"{output_name}.png"
```

### 3. Data Visualizations (Matplotlib)

**Best for:** Performance metrics, comparisons, trends, distributions

```python
import matplotlib.pyplot as plt
import numpy as np

def create_comparison_chart(output_name):
    """Bar chart comparing different approaches"""
    categories = ['Context\nEfficiency', 'Flexibility', 'Control', 'Complexity']
    approach1 = [85, 90, 70, 60]
    approach2 = [70, 70, 95, 80]

    x = np.arange(len(categories))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width/2, approach1, width, label='With Framework', color='#4a90e2')
    rects2 = ax.bar(x + width/2, approach2, width, label='Without Framework', color='#e74c3c')

    ax.set_ylabel('Score', fontsize=12)
    ax.set_title('Framework Comparison', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    ax.set_ylim(0, 100)
    ax.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for rect in rects1:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.savefig(f'{output_name}.png', dpi=300, bbox_inches='tight')
    plt.close()
    return f"{output_name}.png"

def create_performance_trend(output_name):
    """Line chart showing performance over time"""
    x = np.linspace(0, 10, 100)
    y1 = 100 - 20 * np.exp(-x/3)  # Performance improvement
    y2 = 100 - 60 * np.exp(-x/2)  # Cost reduction

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y1, label='Performance', linewidth=2, color='#4a90e2')
    ax.plot(x, y2, label='Cost', linewidth=2, color='#50c878')

    ax.set_xlabel('Optimization Level', fontsize=12)
    ax.set_ylabel('Improvement (%)', fontsize=12)
    ax.set_title('Optimization Impact', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(alpha=0.3)
    ax.set_ylim(0, 100)

    plt.tight_layout()
    plt.savefig(f'{output_name}.png', dpi=300, bbox_inches='tight')
    plt.close()
    return f"{output_name}.png"
```

### 4. Tables for Complex Comparisons

**When diagrams aren't ideal, use formatted tables:**

```markdown
| Feature | Approach A | Approach B | Approach C |
|---------|-----------|-----------|-----------|
| **Context Efficiency** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Setup Complexity** | Low | Medium | High |
| **Flexibility** | High | Medium | Very High |
| **Best For** | General use | Specialized | Enterprise |
```

## Workflow: Creating Visualizations

### Step 1: Identify the Need

As you write, watch for:
- Complex concepts requiring multiple paragraphs to explain
- Lists of components that have relationships
- Processes with multiple steps
- Comparisons between options
- Data or metrics being discussed

### Step 2: Choose the Right Type

- **Architecture/Components** → Graphviz diagram
- **Process/Workflow** → Graphviz with flow layout
- **Data/Metrics** → Matplotlib chart
- **Comparisons** → Table or bar chart
- **Hierarchies** → Graphviz tree diagram

### Step 3: Generate the Visualization

```python
# Example: Generate an architecture diagram for the current section
import os

# Ensure we're in the document directory
doc_dir = os.getcwd()

# Create the diagram
from scripts.diagram_generator import create_architecture_diagram
diagram_path = create_architecture_diagram('fig-architecture')

print(f"Created diagram: {diagram_path}")
```

### Step 4: Insert into Markdown

```markdown
## Architecture Overview

The framework consists of four integrated components:

![Framework Architecture](fig-architecture.png)

*Figure 1: Core components of the extensibility framework showing their relationships and interactions.*

As illustrated above, the SDK forms the foundation...
```

**Best Practices:**
- Always include alt text for accessibility
- Add figure captions explaining what the diagram shows
- Reference figures in text: "As shown in Figure 1..."
- Number figures sequentially: Figure 1, Figure 2, etc.
- Place diagrams near the text that references them

## Installation Requirements

Ensure these are installed (run once per system):

```bash
# Install graphviz (for architecture/flow diagrams)
sudo apt-get install -y graphviz

# Install Python packages
pip3 install --user graphviz matplotlib numpy
```

## Helper Scripts Location

Pre-built diagram generation functions are in:
- `scripts/diagram_generator.py` - Common diagram templates
- `scripts/chart_generator.py` - Chart and graph templates

## Common Patterns for Technical Documents

### Pattern 1: Layered Architecture

```python
dot = graphviz.Digraph(graph_attr={'rankdir': 'TB'})
dot.node('layer1', 'Presentation Layer')
dot.node('layer2', 'Business Logic Layer')
dot.node('layer3', 'Data Access Layer')
dot.node('layer4', 'Database')
dot.edges([('layer1', 'layer2'), ('layer2', 'layer3'), ('layer3', 'layer4')])
```

### Pattern 2: Parallel Processing

```python
dot = graphviz.Digraph()
dot.node('main', 'Main Process')
with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('worker1', 'Worker 1')
    s.node('worker2', 'Worker 2')
    s.node('worker3', 'Worker 3')
dot.edge('main', 'worker1')
dot.edge('main', 'worker2')
dot.edge('main', 'worker3')
```

### Pattern 3: Integration Flow

```python
dot = graphviz.Digraph(graph_attr={'rankdir': 'LR'})
dot.node('external', 'External System', shape='cylinder')
dot.node('api', 'API Gateway', shape='box')
dot.node('service', 'Service Layer', shape='box')
dot.node('db', 'Database', shape='cylinder')
dot.edges([('external', 'api'), ('api', 'service'), ('service', 'db')])
```

## Styling Guidelines

### Colors (Professional Palette)
- Primary: `#4a90e2` (blue)
- Success: `#50c878` (green)
- Warning: `#f39c12` (orange)
- Error: `#e74c3c` (red)
- Neutral: `#95a5a6` (gray)

### Fonts
- Sans-serif: Arial, Helvetica
- Font sizes: 10-14pt for nodes, 8-10pt for labels

### Layout
- Adequate spacing: `nodesep='0.8'`, `ranksep='0.8'`
- Consistent shapes: boxes for processes, ellipses for start/end, diamonds for decisions
- Clear edge labels when showing relationships

## Examples for Common White Paper Sections

### For "Architecture Overview" sections:
```python
create_architecture_diagram('architecture-overview')
```
→ Component diagram showing system structure

### For "Workflow" or "Process" sections:
```python
create_workflow_diagram('workflow-example')
```
→ Flow diagram showing step-by-step process

### For "Performance" or "Comparison" sections:
```python
create_comparison_chart('performance-comparison')
```
→ Bar chart comparing metrics

### For "Results" or "Analysis" sections:
```python
create_performance_trend('results-trend')
```
→ Line chart showing trends

## Quality Checklist

Before finalizing diagrams:
- ✅ Diagram is clear at 100% zoom and 50% zoom
- ✅ Text is readable (not too small)
- ✅ Colors are accessible (not just red/green)
- ✅ Arrows/relationships are labeled
- ✅ Caption explains what diagram shows
- ✅ Diagram is referenced in surrounding text
- ✅ File naming is consistent (fig-section-name.png)
- ✅ High resolution (300 DPI for print, 150 DPI minimum for digital)

## Tips

1. **Keep it simple**: One concept per diagram
2. **Be consistent**: Use same colors/styles throughout document
3. **Label everything**: Nodes, edges, axes, legends
4. **Size appropriately**: Large enough to read, small enough to fit page
5. **Version control**: Keep diagram source code in repo, not just images
6. **Iterate**: Review and refine based on feedback

## Common Mistakes to Avoid

❌ Too much information in one diagram
❌ Unlabeled arrows or connections
❌ Inconsistent styling across diagrams
❌ Missing figure captions
❌ Diagrams that duplicate text exactly
❌ Low resolution images (blurry when printed)
❌ Color-only distinctions (not accessible)

## Advanced: Creating Custom Diagrams

For complex custom diagrams not covered by templates:

```python
import graphviz

dot = graphviz.Digraph(
    comment='Custom Diagram',
    format='png',
    graph_attr={
        'rankdir': 'TB',  # Direction: TB, LR, BT, RL
        'splines': 'ortho',  # Edge routing: ortho, curved, polyline
        'nodesep': '1.0',  # Horizontal spacing
        'ranksep': '1.0',  # Vertical spacing
        'bgcolor': 'transparent',  # Background
        'dpi': '300'  # Resolution
    }
)

# Customize nodes
dot.attr('node',
         shape='box',  # box, ellipse, diamond, cylinder, etc.
         style='filled,rounded',
         fontname='Arial',
         fontsize='12',
         fillcolor='lightblue',
         color='darkblue',
         penwidth='2')

# Add your content
dot.node('A', 'Component A')
dot.node('B', 'Component B')
dot.edge('A', 'B', label='relationship', color='blue')

dot.render('custom-diagram', cleanup=True)
```

## Resources

- Graphviz documentation: https://graphviz.org/documentation/
- Matplotlib gallery: https://matplotlib.org/stable/gallery/
- Color accessibility: https://colorbrewer2.org/

---

**Remember:** Good visualizations enhance understanding—bad ones create confusion. When in doubt, start simple and add complexity only if it adds clarity.
