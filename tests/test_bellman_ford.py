import pytest

from shortest_paths.bellman_ford import NegativeCycleError, bellman_ford, reconstruct_path


def test_bellman_ford_handles_negative_edges():
    graph = {
        "S": [("A", 4), ("E", 5)],
        "A": [("B", -2)],
        "B": [("C", 2)],
        "C": [("D", 4)],
        "D": [],
        "E": [("D", -1)],
    }
    dist, prev = bellman_ford(graph, "S")
    assert dist["D"] == 4
    assert reconstruct_path(prev, "S", "D") in (["S", "E", "D"], ["S", "A", "B", "C", "D"])


def test_bellman_ford_negative_cycle_raises():
    graph = {
        "A": [("B", 1)],
        "B": [("C", -2)],
        "C": [("A", -2)],
    }
    with pytest.raises(NegativeCycleError):
        bellman_ford(graph, "A")
