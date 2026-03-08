import heapq
from typing import Any, Callable, Dict, List, Optional, Tuple

from .types import WeightedGraph


def a_star(
    graph: WeightedGraph,
    start: Any,
    goal: Any,
    heuristic: Callable[[Any, Any], float],
) -> Optional[List[Any]]:
    """Find shortest path using A* search."""
    open_list: List[Tuple[float, Any]] = []
    heapq.heappush(open_list, (0.0, start))

    g_cost: Dict[Any, float] = {start: 0.0}
    parent: Dict[Any, Any] = {}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path: List[Any] = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph.get(current, []):
            tentative_g = g_cost[current] + cost
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f, neighbor))
                parent[neighbor] = current

    return None
