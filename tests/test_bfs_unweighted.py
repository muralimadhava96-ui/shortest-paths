from shortest_paths.bfs_unweighted import bfs_shortest_path


def test_bfs_shortest_path():
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["F"],
        "E": ["F"],
        "F": [],
    }
    path = bfs_shortest_path(graph, "A", "F")
    assert len(path) == 4
    assert path[0] == "A"
    assert path[-1] == "F"
