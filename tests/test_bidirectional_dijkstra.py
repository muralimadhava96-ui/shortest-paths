import pytest

from shortest_paths.bidirectional_dijkstra import bidirectional_dijkstra


def test_bidirectional_dijkstra_basic():
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    cost, path = bidirectional_dijkstra(graph, "A", "D")
    assert cost == 4
    assert path == ["A", "B", "C", "D"]


def test_bidirectional_dijkstra_negative_raises():
    graph = {"A": [("B", -1)], "B": []}
    with pytest.raises(ValueError):
        bidirectional_dijkstra(graph, "A", "B")
