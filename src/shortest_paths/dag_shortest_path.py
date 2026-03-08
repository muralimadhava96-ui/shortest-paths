from collections import deque
from typing import Any, List, Optional, Tuple

from .types import Distances, Previous, WeightedGraph


def _topological_order(graph: WeightedGraph) -> List[Any]:
    nodes = set(graph.keys()) | {v for edges in graph.values() for v, _ in edges}
    indegree = {n: 0 for n in nodes}
    for u in graph:
        for v, _ in graph[u]:
            indegree[v] += 1

    q = deque([n for n, d in indegree.items() if d == 0])
    order: List[Any] = []

    while q:
        u = q.popleft()
        order.append(u)
        for v, _ in graph.get(u, []):
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if len(order) != len(nodes):
        raise ValueError("Graph is not a DAG")
    return order


def dag_shortest_path(graph: WeightedGraph, source: Any) -> Tuple[Distances, Previous]:
    """Single-source shortest paths in a directed acyclic graph."""
    order = _topological_order(graph)
    nodes = set(order)
    distances: Distances = {node: float("inf") for node in nodes}
    previous: Previous = {node: None for node in nodes}

    if source not in nodes:
        return distances, previous

    distances[source] = 0.0

    for u in order:
        if distances[u] == float("inf"):
            continue
        for v, w in graph.get(u, []):
            alt = distances[u] + w
            if alt < distances[v]:
                distances[v] = alt
                previous[v] = u

    return distances, previous


def reconstruct_path(previous: Previous, target: Any, source: Any = None) -> List[Any]:
    """Reconstruct path from predecessor map."""
    if target not in previous:
        return []

    path: List[Any] = []
    cur: Optional[Any] = target
    while cur is not None:
        path.append(cur)
        cur = previous[cur]

    path.reverse()
    if source is None:
        return path
    return path if path and path[0] == source else []
