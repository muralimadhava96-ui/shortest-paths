#!/usr/bin/env python3
import argparse
import json
import sys
from typing import Any, Dict, List, Tuple

# Ensure parent directory is on sys.path when running tests directly
import os
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, os.pardir))
if root not in sys.path:
    sys.path.insert(0, root)

src = os.path.join(root, "src")
if src not in sys.path:
    sys.path.insert(0, src)

from shortest_paths.a_star import a_star

def read_graph_json(path: str) -> Dict[Any, List[Tuple[Any, float]]]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    graph = {}
    for k, v in data.items():
        edges = []
        for item in v:
            if isinstance(item, list) or isinstance(item, tuple):
                neighbor, weight = item[0], float(item[1])
            elif isinstance(item, dict):
                neighbor = item.get('to') or item.get('neighbor')
                weight = float(item.get('weight'))
            else:
                raise ValueError('Unrecognized edge format in JSON')
            edges.append((neighbor, weight))
        graph[k] = edges
    return graph

# A simple placeholder heuristic. For a real A* application, this would be problem-specific.
# This heuristic makes A* behave like Dijkstra's algorithm.
def zero_heuristic(node, goal):
    return 0

def main():
    p = argparse.ArgumentParser(description='A* CLI — compute shortest paths with a heuristic')
    p.add_argument('graph_file', help='Path to graph file (JSON format)')
    p.add_argument('start_node', help='Start node')
    p.add_argument('goal_node', help='Goal node')
    p.add_argument(
        "--heuristic_mode",
        default="zero",
        choices=["zero"],
        help="Heuristic mode to use. Currently only 'zero' is supported.",
    )

    args = p.parse_args()

    try:
        graph = read_graph_json(args.graph_file)
    except FileNotFoundError:
        print(f"Error: Graph file not found at {args.graph_file}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in graph file {args.graph_file}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e} in graph file {args.graph_file}", file=sys.stderr)
        sys.exit(1)

    heuristic_func = None
    if args.heuristic_mode == 'zero':
        heuristic_func = zero_heuristic
    # Add more heuristic options here if needed in the future

    if heuristic_func is None:
        print(f"Error: Unknown heuristic mode {args.heuristic_mode}", file=sys.stderr)
        sys.exit(1)

    if args.start_node not in graph:
        print(f"Error: Start node '{args.start_node}' not found in graph.", file=sys.stderr)
        sys.exit(1)
    if args.goal_node not in graph:
        print(f"Error: Goal node '{args.goal_node}' not found in graph.", file=sys.stderr)
        sys.exit(1)

    path = a_star(graph, args.start_node, args.goal_node, heuristic_func)

    if path:
        print(f"Shortest path from {args.start_node} to {args.goal_node}:")
        print(" -> ".join(map(str, path)))
    else:
        print(f"No path found from {args.start_node} to {args.goal_node}.")

if __name__ == '__main__':
    main()
