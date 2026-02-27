from itertools import product, permutations
import networkx as nx

def is_hamiltonian_cycle(graph, cycle):
  """Checks if cycle is a hamiltonian cycle in graph
  graph is a Networkx graph, and cycle is a list of vertices"""
  n = len(set(cycle))
  if n != graph.order(): # Corrected: graph.order() instead of graph.order
    return False
  for i in range(n):
    if not graph.has_edge(cycle[i], cycle[(i + 1) % n]): # Simplified loop for cycle check
      return False
  return True

def is_hamiltonian(graph):
  vertices=list(graph.nodes())
  if len(vertices) < 3:
    return False
  perms = permutations(vertices) # Corrected: permutations directly imported
  for perm in perms:
    if is_hamiltonian_cycle(graph, perm): # Corrected: function name typo
      return perm
  return False

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

def knapsack_problem(desired_value, capacity, profits, weights):
  n = len(profits)
  potencia = list(product([0,1], repeat=n)) # Corrected: product directly imported
  for combination in potencia:
      current_weight = sum(s * w for s, w in zip(combination, weights))
      current_profit = sum(s * p for s, p in zip(combination, profits))
      if current_weight <= capacity and current_profit >= desired_value:
        print("Si hay solución. Una de ellas es la que tupla:")
        return combination
  return False