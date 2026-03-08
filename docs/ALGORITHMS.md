# Algorithms

## Existing algorithms
- Dijkstra
- A*
- Floyd-Warshall

## Added in this update
- Bellman-Ford: handles negative edges and detects negative cycles.
- Johnson: all-pairs shortest paths for sparse graphs with negative weights (no negative cycles).
- BFS shortest path (unweighted): shortest edge-count path in unweighted graphs.

## Additional algorithms
- 0-1 BFS: optimized shortest paths for graphs with edge weights in `{0, 1}`.
- DAG shortest path: linear-time shortest paths in directed acyclic graphs.
- Bidirectional Dijkstra: source-target shortest path with dual-frontier search.
- Yen's K-shortest loopless paths: computes multiple alternative shortest routes.
