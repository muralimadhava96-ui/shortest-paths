from typing import Any, Dict, List, Optional, Tuple

Graph = Dict[Any, List[Tuple[Any, float]]]
Matrix = Dict[Any, Dict[Any, float]]
NextHop = Dict[Any, Dict[Any, Optional[Any]]]


def floyd_warshall(graph: Graph) -> Tuple[Matrix, NextHop]:
    """All-pairs shortest paths using Floyd–Warshall.

    Returns distance and next-hop tables; unreachable pairs stay at inf/None.
    """
    nodes = set(graph.keys()) | {v for edges in graph.values() for v, _ in edges}
    dist: Matrix = {i: {j: float('inf') for j in nodes} for i in nodes}
    next_hop: NextHop = {i: {j: None for j in nodes} for i in nodes}

    for n in nodes:
        dist[n][n] = 0.0

    for u, edges in graph.items():
        for v, w in edges:
            if w < dist[u][v]:
                dist[u][v] = w
                next_hop[u][v] = v

    for k in nodes:
        for i in nodes:
            if dist[i][k] == float('inf'):
                continue
            for j in nodes:
                alt = dist[i][k] + dist[k][j]
                if alt < dist[i][j]:
                    dist[i][j] = alt
                    next_hop[i][j] = next_hop[i][k]

    return dist, next_hop


def reconstruct_fw_path(next_hop: NextHop, source: Any, target: Any) -> List[Any]:
    """Reconstruct path between ``source`` and ``target`` using next-hop table."""
    if source not in next_hop or target not in next_hop[source]:
        return []
    if next_hop[source][target] is None:
        return []

    path = [source]
    while source != target:
        source = next_hop[path[-1]][target]
        if source is None:
            return []
        path.append(source)

    return path
