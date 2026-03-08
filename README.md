# shortest-paths

Python implementations of shortest-path algorithms with tests and CLI examples.

## Included algorithms
- Dijkstra (single-source, non-negative weights)
- A* (single-pair with heuristic)
- Floyd-Warshall (all-pairs)
- Bellman-Ford (single-source, supports negative weights)
- Johnson (all-pairs for sparse graphs, supports negatives without negative cycles)
- BFS shortest path (unweighted graphs)

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
