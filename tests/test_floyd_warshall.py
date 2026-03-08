from shortest_paths.floyd_warshall import floyd_warshall, reconstruct_fw_path


def test_floyd_warshall_path_reconstruction():
    graph = {
        "A": [("B", 3), ("C", 10)],
        "B": [("C", 1)],
        "C": [],
    }
    dist, next_hop = floyd_warshall(graph)
    assert dist["A"]["C"] == 4
    assert reconstruct_fw_path(next_hop, "A", "C") == ["A", "B", "C"]
