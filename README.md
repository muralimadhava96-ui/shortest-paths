# shortest-paths

Python implementations of shortest-path algorithms with tests and CLI examples.

## Included algorithms
- Dijkstra (single-source, non-negative weights)
- A* (single-pair with heuristic)
- Floyd-Warshall (all-pairs)
- Bellman-Ford (single-source, supports negative weights)
- Johnson (all-pairs for sparse graphs, supports negatives without negative cycles)
- BFS shortest path (unweighted graphs)
- 0-1 BFS (single-source for weights in {0, 1})
- DAG shortest path (single-source on directed acyclic graphs)
- Bidirectional Dijkstra (source-target for non-negative weighted graphs)
- Yen's K-shortest loopless paths (multiple alternatives)

## Project structure
```text
.
├── src/shortest_paths/
│   ├── __init__.py
│   ├── a_star.py
│   ├── bellman_ford.py
│   ├── bfs_unweighted.py
│   ├── dijkstra.py
│   ├── floyd_warshall.py
│   ├── johnson.py
│   └── types.py
├── tests/
├── docs/
├── pyproject.toml
└── README.md
```

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Run tests
```bash
pytest
```

## CLI
```bash
python -m shortest_paths.cli dijkstra --graph graph.json --source A --target D
python -m shortest_paths.cli bellman-ford --graph graph.json --source A --target D
python -m shortest_paths.cli bfs --graph graph_unweighted.json --source A --target F
python -m shortest_paths.cli johnson --graph graph.json
python -m shortest_paths.cli zero-one-bfs --graph graph01.json --source A --target D
python -m shortest_paths.cli dag --graph dag.json --source S --target T
python -m shortest_paths.cli bidirectional-dijkstra --graph graph.json --source A --target D
python -m shortest_paths.cli yen-k --graph graph.json --source A --target D --k 3
```

Detailed examples: `docs/USAGE.md`.

## Usage example
```python
from shortest_paths import dijkstra, bellman_ford, johnson

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": []
}

distances, previous = dijkstra(graph, "A")
print(distances["D"])  # 4.0
```
