from shortest_paths.yen_k_shortest import yen_k_shortest_paths


def test_yen_k_shortest_paths_returns_multiple():
    graph = {
        "A": [("B", 1), ("C", 2)],
        "B": [("D", 2), ("C", 1)],
        "C": [("D", 1)],
        "D": [],
    }
    paths = yen_k_shortest_paths(graph, "A", "D", 3)
    assert len(paths) >= 2
    assert paths[0][0] == 3
    assert paths[0][1] in (["A", "C", "D"], ["A", "B", "D"], ["A", "B", "C", "D"])
