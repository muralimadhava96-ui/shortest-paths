from typing import Any

from .bellman_ford import bellman_ford
from .dijkstra import dijkstra
from .types import Matrix, WeightedGraph


def johnson(graph: WeightedGraph) -> Matrix:
    """All-pairs shortest paths for sparse weighted graphs (supports negatives, no negative cycles)."""
    nodes = set(graph.keys()) | {v for edges in graph.values() for v, _ in edges}
    super_source = "__johnson_source__"
    while super_source in nodes:
        super_source += "_"

    g2: WeightedGraph = {u: list(edges) for u, edges in graph.items()}
    for node in nodes:
        g2.setdefault(node, [])
    g2[super_source] = [(node, 0.0) for node in nodes]

    h, _ = bellman_ford(g2, super_source)

    reweighted: WeightedGraph = {}
    for u, edges in g2.items():
        if u == super_source:
            continue
        reweighted[u] = []
        for v, w in edges:
            reweighted[u].append((v, w + h[u] - h[v]))

    result: Matrix = {u: {v: float("inf") for v in nodes} for u in nodes}
    for u in nodes:
        dist_u, _ = dijkstra(reweighted, u)
        for v in nodes:
            if dist_u[v] != float("inf"):
                result[u][v] = dist_u[v] - h[u] + h[v]
    return result
