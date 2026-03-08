from shortest_paths.johnson import johnson


def test_johnson_all_pairs():
    graph = {
        "A": [("B", 2), ("C", 4)],
        "B": [("C", -1), ("D", 2)],
        "C": [("D", 3)],
        "D": [],
    }
    dist = johnson(graph)
    assert dist["A"]["D"] == 4
    assert dist["A"]["C"] == 1
