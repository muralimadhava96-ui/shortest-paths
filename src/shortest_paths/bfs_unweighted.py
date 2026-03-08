from collections import deque
from typing import Any, Dict, List, Optional


UnweightedGraph = Dict[Any, List[Any]]


def bfs_shortest_path(graph: UnweightedGraph, source: Any, target: Any) -> List[Any]:
    """Return one shortest path in an unweighted graph using BFS."""
    if source not in graph:
        return []
    if source == target:
        return [source]

    parent: Dict[Any, Optional[Any]] = {source: None}
    q = deque([source])

    while q:
        u = q.popleft()
        for v in graph.get(u, []):
            if v in parent:
                continue
            parent[v] = u
            if v == target:
                path: List[Any] = [target]
                cur: Optional[Any] = target
                while parent[cur] is not None:
                    cur = parent[cur]
                    path.append(cur)
                path.reverse()
                return path
            q.append(v)

    return []
