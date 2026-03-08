from shortest_paths.a_star import a_star


def zero_heuristic(_, __):
    return 0


def test_a_star_returns_path():
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    path = a_star(graph, "A", "D", zero_heuristic)
    assert path == ["A", "B", "C", "D"]
