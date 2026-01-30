#!/usr/bin/env python3
"""
Diagram Generator - Helper functions for creating technical diagrams
Used by the visualizations skill for white papers and technical documents
"""

import graphviz
import os


def create_architecture_diagram(output_name, components=None):
    """
    Create a system architecture diagram showing component relationships.

    Args:
        output_name: Base filename (without extension)
        components: Dict with 'nodes' and 'edges' or None for default example

    Returns:
        Path to generated PNG file
    """
    dot = graphviz.Digraph(
        comment='System Architecture',
        format='png',
        graph_attr={
            'rankdir': 'TB',
            'splines': 'ortho',
            'nodesep': '0.8',
            'ranksep': '0.8',
            'bgcolor': 'transparent',
            'dpi': '300'
        }
    )

    # Default node style
    dot.attr('node',
             shape='box',
             style='rounded,filled',
             fillcolor='lightblue',
             fontname='Arial',
             fontsize='12',
             penwidth='2')

    if components is None:
        # Default example
        dot.node('SDK', 'Agent SDK\n(Foundation)', fillcolor='#4a90e2', fontcolor='white')
        dot.node('Sub', 'Subagents\n(Specialization)', fillcolor='#50c878', fontcolor='white')
        dot.node('Skills', 'Skills\n(Knowledge)', fillcolor='#f39c12', fontcolor='white')
        dot.node('Hooks', 'Hooks\n(Control)', fillcolor='#e74c3c', fontcolor='white')

        dot.edge('SDK', 'Sub', label='spawns')
        dot.edge('SDK', 'Skills', label='uses')
        dot.edge('SDK', 'Hooks', label='triggers')
        dot.edge('Sub', 'Skills', label='accesses', style='dashed')
        dot.edge('Hooks', 'Sub', label='controls', style='dashed')
    else:
        # Custom components
        for node in components.get('nodes', []):
            dot.node(node['id'], node['label'],
                    fillcolor=node.get('color', 'lightblue'),
                    fontcolor=node.get('fontcolor', 'black'))

        for edge in components.get('edges', []):
            dot.edge(edge['from'], edge['to'],
                    label=edge.get('label', ''),
                    style=edge.get('style', 'solid'))

    dot.render(output_name, cleanup=True)
    return f"{output_name}.png"


def create_workflow_diagram(output_name, steps=None):
    """
    Create a workflow or process flow diagram.

    Args:
        output_name: Base filename (without extension)
        steps: List of steps or None for default example

    Returns:
        Path to generated PNG file
    """
    dot = graphviz.Digraph(
        format='png',
        graph_attr={
            'rankdir': 'LR',
            'splines': 'ortho',
            'bgcolor': 'transparent',
            'dpi': '300'
        }
    )

    dot.attr('node', shape='box', style='rounded', fontname='Arial', fontsize='11')

    if steps is None:
        # Default example
        dot.node('start', 'Start', shape='ellipse', fillcolor='lightgreen', style='filled')
        dot.node('step1', 'Gather\nContext')
        dot.node('step2', 'Take\nAction')
        dot.node('step3', 'Verify\nResults')
        dot.node('decision', 'Complete?', shape='diamond', fillcolor='lightyellow', style='filled')
        dot.node('end', 'End', shape='ellipse', fillcolor='lightcoral', style='filled')

        dot.edge('start', 'step1')
        dot.edge('step1', 'step2')
        dot.edge('step2', 'step3')
        dot.edge('step3', 'decision')
        dot.edge('decision', 'end', label='Yes')
        dot.edge('decision', 'step1', label='No', style='dashed')
    else:
        # Custom steps
        for i, step in enumerate(steps):
            shape = 'box'
            if step.get('type') == 'start' or step.get('type') == 'end':
                shape = 'ellipse'
            elif step.get('type') == 'decision':
                shape = 'diamond'

            dot.node(step['id'], step['label'], shape=shape,
                    fillcolor=step.get('color', 'white'),
                    style=step.get('style', 'rounded'))

        for edge in steps:
            if 'next' in edge:
                dot.edge(edge['id'], edge['next'],
                        label=edge.get('edge_label', ''))

    dot.render(output_name, cleanup=True)
    return f"{output_name}.png"


def create_layered_architecture(output_name, layers=None):
    """
    Create a layered architecture diagram (e.g., presentation, business, data layers).

    Args:
        output_name: Base filename (without extension)
        layers: List of layer names or None for default

    Returns:
        Path to generated PNG file
    """
    dot = graphviz.Digraph(
        format='png',
        graph_attr={
            'rankdir': 'TB',
            'splines': 'ortho',
            'bgcolor': 'transparent',
            'dpi': '300',
            'ranksep': '0.5'
        }
    )

    dot.attr('node',
             shape='box',
             style='filled',
             width='4',
             fontname='Arial',
             fontsize='12',
             penwidth='2')

    if layers is None:
        layers = [
            ('UI', 'Presentation Layer', '#e3f2fd'),
            ('Logic', 'Business Logic Layer', '#fff3e0'),
            ('Data', 'Data Access Layer', '#f3e5f5'),
            ('DB', 'Database', '#e8f5e9')
        ]

    for i, layer in enumerate(layers):
        if isinstance(layer, tuple):
            layer_id, layer_name, color = layer
        else:
            layer_id = f'layer{i}'
            layer_name = layer
            color = 'lightblue'

        dot.node(layer_id, layer_name, fillcolor=color)
        if i > 0:
            prev_id = layers[i-1][0] if isinstance(layers[i-1], tuple) else f'layer{i-1}'
            dot.edge(prev_id, layer_id)

    dot.render(output_name, cleanup=True)
    return f"{output_name}.png"


def create_integration_diagram(output_name, systems=None):
    """
    Create a system integration diagram showing data flow between systems.

    Args:
        output_name: Base filename (without extension)
        systems: Dict with system definitions or None for default

    Returns:
        Path to generated PNG file
    """
    dot = graphviz.Digraph(
        format='png',
        graph_attr={
            'rankdir': 'LR',
            'splines': 'ortho',
            'bgcolor': 'transparent',
            'dpi': '300'
        }
    )

    dot.attr('node', fontname='Arial', fontsize='11', penwidth='2')

    if systems is None:
        # Default integration example
        dot.node('external', 'External\nSystem', shape='cylinder', fillcolor='#e0e0e0', style='filled')
        dot.node('api', 'API\nGateway', shape='box', style='rounded,filled', fillcolor='#4a90e2', fontcolor='white')
        dot.node('service', 'Service\nLayer', shape='box', style='rounded,filled', fillcolor='#50c878', fontcolor='white')
        dot.node('mcp', 'MCP\nIntegration', shape='box', style='rounded,filled', fillcolor='#f39c12', fontcolor='white')
        dot.node('db', 'Database', shape='cylinder', fillcolor='#e0e0e0', style='filled')

        dot.edge('external', 'api', label='HTTPS')
        dot.edge('api', 'service', label='Internal')
        dot.edge('service', 'mcp', label='Protocol')
        dot.edge('service', 'db', label='SQL')
    else:
        # Custom systems
        for system in systems.get('nodes', []):
            shape = 'cylinder' if system.get('type') == 'database' else 'box'
            dot.node(system['id'], system['label'],
                    shape=shape,
                    fillcolor=system.get('color', 'lightblue'),
                    style=system.get('style', 'filled'))

        for conn in systems.get('connections', []):
            dot.edge(conn['from'], conn['to'], label=conn.get('label', ''))

    dot.render(output_name, cleanup=True)
    return f"{output_name}.png"


def create_parallel_processing(output_name, workers=None):
    """
    Create a diagram showing parallel processing with multiple workers.

    Args:
        output_name: Base filename (without extension)
        workers: List of worker names or None for default

    Returns:
        Path to generated PNG file
    """
    dot = graphviz.Digraph(
        format='png',
        graph_attr={
            'rankdir': 'TB',
            'bgcolor': 'transparent',
            'dpi': '300'
        }
    )

    dot.attr('node',
             shape='box',
             style='rounded,filled',
             fontname='Arial',
             fontsize='11',
             penwidth='2')

    dot.node('main', 'Main Agent', fillcolor='#4a90e2', fontcolor='white')

    if workers is None:
        workers = ['Security\nReviewer', 'Performance\nAnalyzer', 'Style\nChecker']

    # Create workers on same rank (horizontal alignment)
    with dot.subgraph() as s:
        s.attr(rank='same')
        for i, worker in enumerate(workers):
            worker_id = f'worker{i}'
            s.node(worker_id, worker, fillcolor='#50c878', fontcolor='white')
            dot.edge('main', worker_id, label='delegate')
            dot.edge(worker_id, 'main', label='results', style='dashed', color='gray')

    dot.render(output_name, cleanup=True)
    return f"{output_name}.png"


if __name__ == '__main__':
    """Test the diagram generator"""
    print("Testing diagram generators...")

    print("1. Architecture diagram...")
    create_architecture_diagram('test-architecture')

    print("2. Workflow diagram...")
    create_workflow_diagram('test-workflow')

    print("3. Layered architecture...")
    create_layered_architecture('test-layers')

    print("4. Integration diagram...")
    create_integration_diagram('test-integration')

    print("5. Parallel processing...")
    create_parallel_processing('test-parallel')

    print("\nAll test diagrams created successfully!")
    print("Check for test-*.png files in current directory.")
