# Usage

## Python API

```python
from shortest_paths import dijkstra, bellman_ford, johnson, bfs_shortest_path
```

## CLI

Install editable with dev deps:

```bash
python -m pip install -e .[dev]
```

Run CLI:

```bash
python -m shortest_paths.cli dijkstra --graph graph.json --source A --target D
python -m shortest_paths.cli bellman-ford --graph graph.json --source A --target D
python -m shortest_paths.cli bfs --graph graph_unweighted.json --source A --target F
python -m shortest_paths.cli johnson --graph graph.json
```

Input graph format (weighted):

```json
{
  "A": [["B", 2], ["C", 5]],
  "B": [["C", -1]],
  "C": []
}
```

Input graph format (unweighted):

```json
{
  "A": ["B", "C"],
  "B": ["D"],
  "C": ["D"],
  "D": []
}
```
