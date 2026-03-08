from typing import Any, List, Optional, Tuple

from .types import Distances, Previous, WeightedGraph


class NegativeCycleError(ValueError):
    """Raised when a reachable negative-weight cycle exists."""


def bellman_ford(graph: WeightedGraph, source: Any) -> Tuple[Distances, Previous]:
    """Single-source shortest paths allowing negative edge weights."""
    nodes = set(graph.keys()) | {v for edges in graph.values() for v, _ in edges}
    distances: Distances = {node: float("inf") for node in nodes}
    previous: Previous = {node: None for node in nodes}

    if source not in nodes:
        return distances, previous

    distances[source] = 0.0
    edges: List[Tuple[Any, Any, float]] = []
    for u, neighbors in graph.items():
        for v, w in neighbors:
            edges.append((u, v, w))

    for _ in range(len(nodes) - 1):
        changed = False
        for u, v, w in edges:
            if distances[u] == float("inf"):
                continue
            alt = distances[u] + w
            if alt < distances[v]:
                distances[v] = alt
                previous[v] = u
                changed = True
        if not changed:
            break

    for u, v, w in edges:
        if distances[u] != float("inf") and distances[u] + w < distances[v]:
            raise NegativeCycleError("Graph contains a reachable negative-weight cycle")

    return distances, previous


def reconstruct_path(previous: Previous, source: Any, target: Any) -> List[Any]:
    """Reconstruct path from source to target from predecessor map."""
    if target not in previous or source not in previous:
        return []

    path: List[Any] = []
    cur: Optional[Any] = target
    while cur is not None:
        path.append(cur)
        cur = previous[cur]

    path.reverse()
    return path if path and path[0] == source else []
