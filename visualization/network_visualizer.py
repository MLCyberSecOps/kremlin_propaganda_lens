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
    with open(args.input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('pradeepkumar@') or line.startswith('export'):
                continue
                
            # Parse the line: source (type) --> rel_type --> target (type)
            match = re.match(r'^([^\s(]+)\s+\(([^)]+)\)\s+-->\s+([^\s]+)\s+-->\s+([^\s(]+)(?:\s*\(([^)]+)\))?$', line)
            if not match:
                continue
                
            source, source_type, rel_type, target, target_type = match.groups()
            
            # Add nodes and edge
            G.add_node(source, type=source_type, title=source_type)
            G.add_node(target, type=target_type or 'unknown', title=target_type or 'unknown')
            G.add_edge(source, target, title=rel_type, label=rel_type)
    
    # Create PyVis network
    net = Network(height="800px", width="100%", bgcolor="#ffffff", font_color="#000000", directed=True)
    
    # Add nodes and edges to PyVis
    for node in G.nodes():
        net.add_node(node, **G.nodes[node])
        
    for edge in G.edges():
        net.add_edge(edge[0], edge[1], **G.edges[edge])
    
    # Generate the visualization
    net.show(str(output_path))
    print(f"Visualization saved to {output_path.absolute()}")

if __name__ == "__main__":
    main()
