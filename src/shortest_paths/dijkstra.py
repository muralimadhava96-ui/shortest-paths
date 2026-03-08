import heapq
from typing import Any, List, Optional, Tuple

from .types import Distances, Previous, WeightedGraph


def dijkstra(graph: WeightedGraph, source: Any) -> Tuple[Distances, Previous]:
    """Compute shortest paths from source using Dijkstra's algorithm."""
    nodes = set(graph.keys()) | {v for edges in graph.values() for v, _ in edges}
    distances: Distances = {node: float("inf") for node in nodes}
    previous: Previous = {node: None for node in nodes}

    if source not in nodes:
        return distances, previous

    distances[source] = 0.0
    pq: List[Tuple[float, Any]] = [(0.0, source)]

    while pq:
        dist_u, u = heapq.heappop(pq)
        if dist_u > distances[u]:
            continue

        for v, weight in graph.get(u, []):
            if weight < 0:
                raise ValueError("Dijkstra's algorithm does not support negative weights")
            alt = dist_u + weight
            if alt < distances[v]:
                distances[v] = alt
                previous[v] = u
                heapq.heappush(pq, (alt, v))

    return distances, previous


def reconstruct_path(previous: Previous, target: Any, source: Any = None) -> List[Any]:
    """Reconstruct path from predecessor map.

    If source is provided, returns [] when target is unreachable from source.
    Without source, this follows predecessor links until None.
    """
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
