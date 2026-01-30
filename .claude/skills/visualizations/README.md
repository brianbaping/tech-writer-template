# Visualizations Skill

Professional diagram and chart generation for technical white papers and documentation.

## Installation Requirements

Install these dependencies once per system:

```bash
# Install graphviz (for architecture/flow diagrams)
sudo apt-get install -y graphviz

# Install Python packages
pip3 install --user graphviz matplotlib numpy
```

## Quick Start

The skill activates automatically when writing technical content that would benefit from visualizations.

### Example Usage

```python
# In your document directory
from .claude.skills.visualizations.scripts.diagram_generator import *
from .claude.skills.visualizations.scripts.chart_generator import *

# Create an architecture diagram
create_architecture_diagram('fig-architecture')

# Create a workflow diagram
create_workflow_diagram('fig-workflow')

# Create a comparison chart
create_comparison_chart('fig-comparison')
```

Then reference in markdown:
```markdown
![Architecture Overview](fig-architecture.png)

*Figure 1: System architecture showing component relationships.*
```

## Available Generators

### Diagrams (diagram_generator.py)
- `create_architecture_diagram()` - Component relationships
- `create_workflow_diagram()` - Process flows
- `create_layered_architecture()` - Layered systems
- `create_integration_diagram()` - System integrations
- `create_parallel_processing()` - Concurrent operations

### Charts (chart_generator.py)
- `create_comparison_chart()` - Bar chart comparisons
- `create_performance_trend()` - Line chart trends
- `create_distribution_chart()` - Pie/donut charts
- `create_timeline_chart()` - Timeline milestones
- `create_heatmap()` - Relationship matrices
- `create_stacked_area()` - Cumulative values

## Testing

Test all generators:

```bash
cd .claude/skills/visualizations/scripts

# Test diagrams
python3 diagram_generator.py

# Test charts
python3 chart_generator.py
```

This creates test-*.png files to verify everything works.

## Conversion to PDF

When converting documents with diagrams to PDF:

```bash
pandoc document.md -o document.pdf \
  --pdf-engine=pdflatex \
  -V geometry:margin=1in \
  --toc
```

The PNG images embed automatically in the PDF.

## Tips

1. **Generate before writing** - Create diagrams first, then write text referencing them
2. **Name consistently** - Use `fig-section-name.png` pattern
3. **High resolution** - Scripts generate 300 DPI for print quality
4. **Version control** - Keep the Python scripts, not just the images
5. **Iterate** - Generate → review → refine → regenerate

## Common Issues

**Import Error**: Ensure graphviz and matplotlib are installed
```bash
pip3 install --user graphviz matplotlib numpy
```

**GraphViz Error**: Install system graphviz package
```bash
sudo apt-get install -y graphviz
```

**Permission Denied**: Make scripts executable
```bash
chmod +x scripts/*.py
```

## Examples

See the SKILL.md file for comprehensive examples and patterns.
