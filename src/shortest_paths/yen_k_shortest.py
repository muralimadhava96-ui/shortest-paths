from typing import Any, List, Tuple

from .dijkstra import dijkstra, reconstruct_path
from .types import WeightedGraph


PathWithCost = Tuple[float, List[Any]]


def _path_cost(graph: WeightedGraph, path: List[Any]) -> float:
    total = 0.0
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        edge_map = {n: w for n, w in graph.get(u, [])}
        if v not in edge_map:
            return float("inf")
        total += edge_map[v]
    return total


def yen_k_shortest_paths(graph: WeightedGraph, source: Any, target: Any, k: int) -> List[PathWithCost]:
    """Compute up to k shortest loopless paths between source and target."""
    if k <= 0:
        return []

    dist, prev = dijkstra(graph, source)
    first_path = reconstruct_path(prev, target, source)
    if not first_path:
        return []

    shortest_paths: List[PathWithCost] = [(dist[target], first_path)]
    candidates: List[PathWithCost] = []

    for kth in range(1, k):
        last_path = shortest_paths[kth - 1][1]
        for i in range(len(last_path) - 1):
            spur_node = last_path[i]
            root_path = last_path[: i + 1]

            modified_graph: WeightedGraph = {u: list(edges) for u, edges in graph.items()}

            for _, p in shortest_paths:
                if len(p) > i and p[: i + 1] == root_path:
                    u, v = p[i], p[i + 1]
                    modified_graph[u] = [(n, w) for n, w in modified_graph.get(u, []) if n != v]

            for root_node in root_path[:-1]:
                modified_graph[root_node] = []

            spur_dist, spur_prev = dijkstra(modified_graph, spur_node)
            spur_path = reconstruct_path(spur_prev, target, spur_node)
            if not spur_path:
                continue

            total_path = root_path[:-1] + spur_path
            total_cost = _path_cost(graph, total_path)
            candidate = (total_cost, total_path)
            if candidate not in candidates:
                candidates.append(candidate)

        if not candidates:
            break

        candidates.sort(key=lambda x: x[0])
        shortest_paths.append(candidates.pop(0))

    return shortest_paths
