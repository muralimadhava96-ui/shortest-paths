from typing import Any, Dict, List, Optional, Tuple

Node = Any
WeightedEdge = Tuple[Node, float]
WeightedGraph = Dict[Node, List[WeightedEdge]]
Distances = Dict[Node, float]
Previous = Dict[Node, Optional[Node]]
Matrix = Dict[Node, Dict[Node, float]]
NextHop = Dict[Node, Dict[Node, Optional[Node]]]
