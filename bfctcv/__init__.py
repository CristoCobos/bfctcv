from itertools import product
import networkx as nx

def is_hamltonian_cycle(graph, cycle):
  """Checks if cycle is a hamiltonian cycle in graph
  graph is a Networkx graph, and cycle is a list of verticex"""
  n = len(set(cycle))
  if n != graph.order:
    return False
  for i in range(n-1):
    if not graph.has_edge(cycle[i], cycle[i+1]):
      return False
  if not graph.has_edge(cycle[n-1], cycle[0]):
    return False
  return True

def is_hamiltonian(graph):
  vertices=list(graph.nodes())
  if len(vertices) < 3:
    return False
  perms = itertools.permutations(vertices)
  for perm in perms:
    if is_hamltonian_cycle(graph, perm):
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
    if is_proper_coloring(graph, coloring):
      return coloring
  return False
def knapsack_problem(desired_value, capacity, profits, weights):
  n = len(profits)
  potencia = list(itertools.product([0,1], repeat=n))
  for combination in potencia:
      current_weight = sum(s * w for s, w in zip(combination, weights))
      current_profit = sum(s * p for s, p in zip(combination, profits))
      if current_weight <= capacity and current_profit >= desired_value:
        print("Si hay solución. Una de ellas es la que tupla:")
        return combination
  return False