#!/usr/bin/env python3
"""
Network Visualization for Pravda Network Analysis

This script generates an interactive network visualization from the active probe data.
"""

import re
import json
import networkx as nx
from pyvis.network import Network
from collections import defaultdict
from pathlib import Path
import argparse
import sys

def get_node_color(node_type):
    """Return color based on node type"""
    colors = {
        'domain': '#4e79a7',
        'ip': '#f28e2b',
        'netblock': '#e15759',
        'service': '#59a14f',
        'asn': '#edc948',
        'unknown': '#b07aa1'
    }
    node_type = node_type.lower() if node_type else 'unknown'
    return colors.get(node_type, '#8c8c8c')

def main():
    parser = argparse.ArgumentParser(description='Generate network visualization from probe data')
    parser.add_argument('input_file', help='Path to the probe output file')
    parser.add_argument('-o', '--output', default='network.html', 
                      help='Output HTML file path (default: network.html)')
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Initialize graph
    G = nx.DiGraph()
    
    # Parse the probe data
    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith(('pradeepkumar@', 'export', '#')):
                    continue
                    
                # Parse the line: source (type) --> rel_type --> target (type)
                match = re.match(r'^([^\s(]+)(?:\s*\(([^)]+)\))?\s+-->\s+([^\s]+)\s+-->\s+([^\s(]+)(?:\s*\(([^)]+)\))?$', line)
                if not match:
                    print(f"Skipping malformed line: {line}", file=sys.stderr)
                    continue
                    
                source, source_type, rel_type, target, target_type = match.groups()
                source_type = source_type or 'unknown'
                target_type = target_type or 'unknown'
                
                # Add nodes with type information
                G.add_node(source, type=source_type, title=f"{source}\nType: {source_type}")
                G.add_node(target, type=target_type, title=f"{target}\nType: {target_type}")
                G.add_edge(source, target, title=rel_type, label=rel_type)
    except Exception as e:
        print(f"Error processing input file: {e}", file=sys.stderr)
        sys.exit(1)
    
    if not G.nodes():
        print("No valid data found to visualize.", file=sys.stderr)
        sys.exit(1)
    
    # Create PyVis network
    try:
        net = Network(
            height="800px", 
            width="100%", 
            bgcolor="#ffffff", 
            font_color="#000000", 
            directed=True,
            notebook=False,
            cdn_resources='in_line'
        )
        
        # Configure physics
        net.force_atlas_2based(gravity=-50)
        net.show_buttons(filter_=['physics'])
        
        # Add nodes with styling
        for node in G.nodes():
            node_type = G.nodes[node].get('type', 'unknown').lower()
            net.add_node(
                node,
                title=G.nodes[node].get('title', node),
                color={
                    'background': get_node_color(node_type),
                    'border': '#2B2B2B',
                    'highlight': {
                        'background': get_node_color(node_type),
                        'border': '#2B2B2B'
                    },
                    'hover': {
                        'background': '#D3D3D3',
                        'border': '#2B2B2B'
                    }
                },
                shape='dot',
                size=15 if node_type == 'domain' else 10,
                borderWidth=1
            )
            
        # Add edges
        for edge in G.edges():
            net.add_edge(
                edge[0],
                edge[1],
                title=G.edges[edge].get('title', ''),
                label=G.edges[edge].get('label', ''),
                width=1,
                arrows='to',
                smooth=True
            )
        
        # Generate the visualization
        net.save_graph(str(output_path))
        print(f"Visualization saved to {output_path.absolute()}")
        
    except Exception as e:
        print(f"Error generating visualization: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
