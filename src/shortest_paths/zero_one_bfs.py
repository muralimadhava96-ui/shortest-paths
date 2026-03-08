from collections import deque
from typing import Any, List, Optional, Tuple

from .types import Distances, Previous, WeightedGraph


def zero_one_bfs(graph: WeightedGraph, source: Any) -> Tuple[Distances, Previous]:
    """Single-source shortest paths for graphs with edge weights 0 or 1."""
    nodes = set(graph.keys()) | {v for edges in graph.values() for v, _ in edges}
    distances: Distances = {node: float("inf") for node in nodes}
    previous: Previous = {node: None for node in nodes}

    if source not in nodes:
        return distances, previous

    distances[source] = 0.0
    dq = deque([source])

    while dq:
        u = dq.popleft()
        for v, w in graph.get(u, []):
            if w not in (0, 1):
                raise ValueError("0-1 BFS requires all edge weights to be 0 or 1")
            alt = distances[u] + w
            if alt < distances[v]:
                distances[v] = alt
                previous[v] = u
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)

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
