import heapq
from typing import Any, Dict, List, Optional, Tuple

from .types import Distances, Previous, WeightedGraph


def _build_reverse_graph(graph: WeightedGraph) -> WeightedGraph:
    reverse: WeightedGraph = {}
    for u, edges in graph.items():
        reverse.setdefault(u, [])
        for v, w in edges:
            reverse.setdefault(v, []).append((u, w))
    return reverse


def bidirectional_dijkstra(graph: WeightedGraph, source: Any, target: Any) -> Tuple[float, List[Any]]:
    """Shortest path between source and target using bidirectional Dijkstra."""
    if source == target:
        return 0.0, [source]

    reverse = _build_reverse_graph(graph)
    nodes = set(graph.keys()) | set(reverse.keys())
    if source not in nodes or target not in nodes:
        return float("inf"), []

    dist_f: Distances = {n: float("inf") for n in nodes}
    dist_b: Distances = {n: float("inf") for n in nodes}
    prev_f: Previous = {n: None for n in nodes}
    prev_b: Previous = {n: None for n in nodes}

    dist_f[source] = 0.0
    dist_b[target] = 0.0
    pq_f: List[Tuple[float, Any]] = [(0.0, source)]
    pq_b: List[Tuple[float, Any]] = [(0.0, target)]
    seen_f = set()
    seen_b = set()

    best = float("inf")
    meet: Optional[Any] = None

    while pq_f and pq_b:
        if pq_f[0][0] + pq_b[0][0] >= best:
            break

        d_u, u = heapq.heappop(pq_f)
        if d_u <= dist_f[u]:
            seen_f.add(u)
            if u in seen_b and dist_f[u] + dist_b[u] < best:
                best = dist_f[u] + dist_b[u]
                meet = u

            for v, w in graph.get(u, []):
                if w < 0:
                    raise ValueError("Bidirectional Dijkstra requires non-negative weights")
                alt = dist_f[u] + w
                if alt < dist_f[v]:
                    dist_f[v] = alt
                    prev_f[v] = u
                    heapq.heappush(pq_f, (alt, v))

        d_u, u = heapq.heappop(pq_b)
        if d_u <= dist_b[u]:
            seen_b.add(u)
            if u in seen_f and dist_f[u] + dist_b[u] < best:
                best = dist_f[u] + dist_b[u]
                meet = u

            for v, w in reverse.get(u, []):
                if w < 0:
                    raise ValueError("Bidirectional Dijkstra requires non-negative weights")
                alt = dist_b[u] + w
                if alt < dist_b[v]:
                    dist_b[v] = alt
                    prev_b[v] = u
                    heapq.heappush(pq_b, (alt, v))

    if meet is None:
        return float("inf"), []

    path_f: List[Any] = []
    cur: Optional[Any] = meet
    while cur is not None:
        path_f.append(cur)
        cur = prev_f[cur]
    path_f.reverse()

    path_b: List[Any] = []
    cur = prev_b[meet]
    while cur is not None:
        path_b.append(cur)
        cur = prev_b[cur]

    return best, path_f + path_b
