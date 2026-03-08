import argparse
import json
from typing import Any, Dict, List, Tuple

from .bellman_ford import NegativeCycleError, bellman_ford, reconstruct_path as bf_path
from .bfs_unweighted import bfs_shortest_path
from .dijkstra import dijkstra, reconstruct_path as dijkstra_path
from .johnson import johnson

WeightedGraph = Dict[Any, List[Tuple[Any, float]]]
UnweightedGraph = Dict[Any, List[Any]]


def read_weighted_graph(path: str) -> WeightedGraph:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    graph: WeightedGraph = {}
    for node, edges in data.items():
        normalized: List[Tuple[Any, float]] = []
        for edge in edges:
            if isinstance(edge, (list, tuple)) and len(edge) >= 2:
                normalized.append((edge[0], float(edge[1])))
            elif isinstance(edge, dict):
                normalized.append((edge["to"], float(edge["weight"])))
            else:
                raise ValueError(f"Invalid edge format for node {node}: {edge}")
        graph[node] = normalized
    return graph


def read_unweighted_graph(path: str) -> UnweightedGraph:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("Unweighted graph must be a JSON object of node -> neighbor list")
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description="Shortest path algorithms CLI")
    sub = parser.add_subparsers(dest="algorithm", required=True)

    d = sub.add_parser("dijkstra", help="Run Dijkstra on weighted graph JSON")
    d.add_argument("--graph", required=True)
    d.add_argument("--source", required=True)
    d.add_argument("--target")

    b = sub.add_parser("bellman-ford", help="Run Bellman-Ford on weighted graph JSON")
    b.add_argument("--graph", required=True)
    b.add_argument("--source", required=True)
    b.add_argument("--target")

    u = sub.add_parser("bfs", help="Run BFS shortest path on unweighted graph JSON")
    u.add_argument("--graph", required=True)
    u.add_argument("--source", required=True)
    u.add_argument("--target", required=True)

    j = sub.add_parser("johnson", help="Run Johnson all-pairs on weighted graph JSON")
    j.add_argument("--graph", required=True)

    args = parser.parse_args()

    if args.algorithm == "dijkstra":
        graph = read_weighted_graph(args.graph)
        dist, prev = dijkstra(graph, args.source)
        if args.target:
            path = dijkstra_path(prev, args.target, args.source)
            print(json.dumps({"distance": dist.get(args.target), "path": path}, indent=2))
            return
        print(json.dumps(dist, indent=2))
        return

    if args.algorithm == "bellman-ford":
        graph = read_weighted_graph(args.graph)
        try:
            dist, prev = bellman_ford(graph, args.source)
        except NegativeCycleError as exc:
            raise SystemExit(str(exc)) from exc
        if args.target:
            path = bf_path(prev, args.source, args.target)
            print(json.dumps({"distance": dist.get(args.target), "path": path}, indent=2))
            return
        print(json.dumps(dist, indent=2))
        return

    if args.algorithm == "bfs":
        graph = read_unweighted_graph(args.graph)
        path = bfs_shortest_path(graph, args.source, args.target)
        print(json.dumps({"path": path, "hops": max(0, len(path) - 1)}, indent=2))
        return

    if args.algorithm == "johnson":
        graph = read_weighted_graph(args.graph)
        print(json.dumps(johnson(graph), indent=2))


if __name__ == "__main__":
    main()
