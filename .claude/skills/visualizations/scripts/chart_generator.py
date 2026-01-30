#!/usr/bin/env python3
"""
Chart Generator - Helper functions for creating charts and data visualizations
Used by the visualizations skill for white papers and technical documents
"""

import matplotlib.pyplot as plt
import numpy as np


def create_comparison_chart(output_name, data=None):
    """
    Create a bar chart comparing different options or approaches.

    Args:
        output_name: Base filename (without extension)
        data: Dict with categories, series, and values or None for default

    Returns:
        Path to generated PNG file
    """
    if data is None:
        # Default comparison
        categories = ['Context\nEfficiency', 'Flexibility', 'Control', 'Complexity']
        series_labels = ['With Framework', 'Without Framework']
        values = [
            [85, 90, 95, 60],  # With framework
            [50, 70, 40, 90]   # Without framework
        ]
        colors = ['#4a90e2', '#e74c3c']
    else:
        categories = data['categories']
        series_labels = data['series']
        values = data['values']
        colors = data.get('colors', ['#4a90e2', '#50c878', '#f39c12', '#e74c3c'])

    x = np.arange(len(categories))
    width = 0.35 if len(values) == 2 else 0.25

    fig, ax = plt.subplots(figsize=(10, 6))

    # Create bars for each series
    bars = []
    for i, (series_values, label) in enumerate(zip(values, series_labels)):
        offset = width * (i - len(values)/2 + 0.5)
        rects = ax.bar(x + offset, series_values, width,
                      label=label, color=colors[i % len(colors)])
        bars.append(rects)

        # Add value labels on bars
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontsize=9)

    ax.set_ylabel('Score', fontsize=12)
    ax.set_title('Comparison Analysis', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=10)
    ax.legend(fontsize=10)
    ax.set_ylim(0, 105)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(f'{output_name}.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    return f"{output_name}.png"


def create_performance_trend(output_name, data=None):
    """
    Create a line chart showing trends over time.

    Args:
        output_name: Base filename (without extension)
        data: Dict with x, y values and labels or None for default

    Returns:
        Path to generated PNG file
    """
    if data is None:
        # Default performance trend
        x = np.linspace(0, 10, 50)
        series = [
            {
                'x': x,
                'y': 100 - 80 * np.exp(-x/2),
                'label': 'Performance',
                'color': '#4a90e2'
            },
            {
                'x': x,
                'y': 100 - 90 * np.exp(-x/3),
                'label': 'Cost Efficiency',
                'color': '#50c878'
            }
        ]
        title = 'Improvement Over Time'
        xlabel = 'Optimization Level'
        ylabel = 'Improvement (%)'
    else:
        series = data['series']
        title = data.get('title', 'Trend Analysis')
        xlabel = data.get('xlabel', 'Time')
        ylabel = data.get('ylabel', 'Value')

    fig, ax = plt.subplots(figsize=(10, 6))

    for s in series:
        ax.plot(s['x'], s['y'],
               label=s['label'],
               linewidth=2.5,
               color=s['color'],
               marker='o' if len(s['x']) < 20 else None,
               markersize=6)

    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(fontsize=10, loc='best')
    ax.grid(alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(f'{output_name}.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    return f"{output_name}.png"


def create_distribution_chart(output_name, data=None):
    """
    Create a pie or donut chart showing distribution.

    Args:
        output_name: Base filename (without extension)
        data: Dict with labels and values or None for default

    Returns:
        Path to generated PNG file
    """
    if data is None:
        # Default distribution
        labels = ['SDK Usage', 'Subagent Operations', 'Skill Activations', 'Hook Executions']
        sizes = [35, 30, 20, 15]
        colors = ['#4a90e2', '#50c878', '#f39c12', '#e74c3c']
        title = 'Resource Distribution'
    else:
        labels = data['labels']
        sizes = data['values']
        colors = data.get('colors', ['#4a90e2', '#50c878', '#f39c12', '#e74c3c'])
        title = data.get('title', 'Distribution')

    fig, ax = plt.subplots(figsize=(10, 7))

    # Create donut chart
    wedges, texts, autotexts = ax.pie(sizes,
                                       labels=labels,
                                       autopct='%1.1f%%',
                                       colors=colors,
                                       startangle=90,
                                       pctdistance=0.85,
                                       textprops={'fontsize': 11})

    # Draw circle for donut effect
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)

    # Style the text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')

    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    ax.axis('equal')

    plt.tight_layout()
    plt.savefig(f'{output_name}.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    return f"{output_name}.png"


def create_timeline_chart(output_name, events=None):
    """
    Create a timeline chart showing milestones or phases.

    Args:
        output_name: Base filename (without extension)
        events: List of event dicts with 'time', 'label' or None for default

    Returns:
        Path to generated PNG file
    """
    if events is None:
        # Default timeline
        events = [
            {'time': 0, 'label': 'Project Start'},
            {'time': 2, 'label': 'Requirements'},
            {'time': 5, 'label': 'Design'},
            {'time': 8, 'label': 'Implementation'},
            {'time': 12, 'label': 'Testing'},
            {'time': 15, 'label': 'Deployment'}
        ]

    fig, ax = plt.subplots(figsize=(12, 4))

    times = [e['time'] for e in events]
    labels = [e['label'] for e in events]

    # Draw timeline
    ax.plot(times, [0]*len(times), 'o-', markersize=10,
           linewidth=2, color='#4a90e2')

    # Add labels
    for time, label in zip(times, labels):
        ax.text(time, 0.3, label, ha='center', va='bottom',
               fontsize=10, rotation=45)

    ax.set_ylim(-1, 1.5)
    ax.set_xlabel('Time', fontsize=12)
    ax.set_title('Project Timeline', fontsize=14, fontweight='bold')
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_yticks([])
    ax.grid(axis='x', alpha=0.3)

    plt.tight_layout()
    plt.savefig(f'{output_name}.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    return f"{output_name}.png"


def create_heatmap(output_name, data=None):
    """
    Create a heatmap showing relationships or intensity.

    Args:
        output_name: Base filename (without extension)
        data: Dict with matrix, row/col labels or None for default

    Returns:
        Path to generated PNG file
    """
    if data is None:
        # Default compatibility matrix
        matrix = np.array([
            [1.0, 0.8, 0.9, 0.7],
            [0.8, 1.0, 0.6, 0.8],
            [0.9, 0.6, 1.0, 0.5],
            [0.7, 0.8, 0.5, 1.0]
        ])
        row_labels = ['Component A', 'Component B', 'Component C', 'Component D']
        col_labels = row_labels
        title = 'Component Compatibility'
    else:
        matrix = np.array(data['matrix'])
        row_labels = data['row_labels']
        col_labels = data['col_labels']
        title = data.get('title', 'Heatmap')

    fig, ax = plt.subplots(figsize=(10, 8))

    im = ax.imshow(matrix, cmap='RdYlGn', aspect='auto', vmin=0, vmax=1)

    # Set ticks and labels
    ax.set_xticks(np.arange(len(col_labels)))
    ax.set_yticks(np.arange(len(row_labels)))
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

    # Rotate x labels
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

    # Add text annotations
    for i in range(len(row_labels)):
        for j in range(len(col_labels)):
            text = ax.text(j, i, f'{matrix[i, j]:.2f}',
                         ha='center', va='center',
                         color='black' if matrix[i, j] > 0.5 else 'white',
                         fontsize=10, fontweight='bold')

    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Compatibility Score', rotation=270, labelpad=20)

    plt.tight_layout()
    plt.savefig(f'{output_name}.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    return f"{output_name}.png"


def create_stacked_area(output_name, data=None):
    """
    Create a stacked area chart showing cumulative values over time.

    Args:
        output_name: Base filename (without extension)
        data: Dict with x values and multiple y series or None for default

    Returns:
        Path to generated PNG file
    """
    if data is None:
        # Default resource usage over time
        x = np.arange(0, 11)
        y1 = [5, 8, 12, 15, 18, 20, 22, 23, 24, 24, 25]
        y2 = [3, 5, 8, 12, 15, 18, 20, 22, 23, 24, 24]
        y3 = [2, 3, 5, 7, 10, 12, 14, 16, 17, 18, 18]

        labels = ['CPU Usage', 'Memory Usage', 'Network Usage']
        colors = ['#4a90e2', '#50c878', '#f39c12']
        title = 'Resource Usage Over Time'
        xlabel = 'Time (hours)'
        ylabel = 'Usage (%)'
    else:
        x = data['x']
        y_series = data['y_series']
        labels = data['labels']
        colors = data.get('colors', ['#4a90e2', '#50c878', '#f39c12', '#e74c3c'])
        title = data.get('title', 'Stacked Area Chart')
        xlabel = data.get('xlabel', 'X Axis')
        ylabel = data.get('ylabel', 'Y Axis')

    fig, ax = plt.subplots(figsize=(10, 6))

    if data is None:
        ax.stackplot(x, y1, y2, y3, labels=labels, colors=colors, alpha=0.8)
    else:
        ax.stackplot(x, *y_series, labels=labels, colors=colors, alpha=0.8)

    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(f'{output_name}.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    return f"{output_name}.png"


if __name__ == '__main__':
    """Test the chart generator"""
    print("Testing chart generators...")

    print("1. Comparison chart...")
    create_comparison_chart('test-comparison')

    print("2. Performance trend...")
    create_performance_trend('test-trend')

    print("3. Distribution chart...")
    create_distribution_chart('test-distribution')

    print("4. Timeline chart...")
    create_timeline_chart('test-timeline')

    print("5. Heatmap...")
    create_heatmap('test-heatmap')

    print("6. Stacked area chart...")
    create_stacked_area('test-stacked')

    print("\nAll test charts created successfully!")
    print("Check for test-*.png files in current directory.")
