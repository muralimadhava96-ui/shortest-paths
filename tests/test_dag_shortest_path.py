import pytest

from shortest_paths.dag_shortest_path import dag_shortest_path, reconstruct_path


def test_dag_shortest_path_basic():
    graph = {
        "S": [("A", 1), ("B", 5)],
        "A": [("B", 2), ("C", 4)],
        "B": [("C", 1)],
        "C": [],
    }
    dist, prev = dag_shortest_path(graph, "S")
    assert dist["C"] == 4
    assert reconstruct_path(prev, "C", "S") == ["S", "A", "B", "C"]


def test_dag_shortest_path_cycle_raises():
    graph = {"A": [("B", 1)], "B": [("A", 1)]}
    with pytest.raises(ValueError):
        dag_shortest_path(graph, "A")
