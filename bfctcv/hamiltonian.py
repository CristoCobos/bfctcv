import networkx as nx
import itertools

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
