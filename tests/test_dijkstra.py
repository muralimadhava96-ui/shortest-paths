import pytest

from shortest_paths.dijkstra import dijkstra, reconstruct_path


def test_dijkstra_basic_graph():
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    dist, prev = dijkstra(graph, "A")
    assert dist["D"] == 4
    assert reconstruct_path(prev, "D", "A") == ["A", "B", "C", "D"]


def test_dijkstra_negative_edge_raises():
    graph = {"A": [("B", -1)], "B": []}
    with pytest.raises(ValueError):
        dijkstra(graph, "A")
