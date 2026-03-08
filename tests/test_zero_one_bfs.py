import pytest

from shortest_paths.zero_one_bfs import zero_one_bfs


def test_zero_one_bfs_basic():
    graph = {
        "A": [("B", 0), ("C", 1)],
        "B": [("D", 1)],
        "C": [("D", 0)],
        "D": [],
    }
    dist, _ = zero_one_bfs(graph, "A")
    assert dist["D"] == 1


def test_zero_one_bfs_invalid_weight():
    graph = {"A": [("B", 2)], "B": []}
    with pytest.raises(ValueError):
        zero_one_bfs(graph, "A")
