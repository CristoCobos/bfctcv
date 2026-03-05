import itertools
import networkx as nx

def is_proper_coloring(graph, coloring):
  for edge in graph.edges():
    if coloring[edge[0]] == coloring[edge[1]]:
      return False
  return True

def is_3_coloring(graph):
  n = graph.order()
  colorings = product([0,1,2], repeat = n)
  for coloring in colorings:
    # Map coloring tuple to dictionary for easier lookup (assuming nodes are 0-indexed if graph.order() is used for product repeat)
    # Or, if graph nodes are not 0-indexed, a different approach might be needed
    # For simplicity, assuming graph nodes can be mapped to indices 0 to n-1 consistent with coloring tuple
    node_coloring = {node: color for node, color in zip(graph.nodes(), coloring)}
    if is_proper_coloring(graph, node_coloring):
      return node_coloring
  return False
