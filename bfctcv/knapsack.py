import itertools

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

def knapsack_boolean(desired_value, capacity, profits, weights):
  n = len(profits)
  potencia = list(product([0,1], repeat=n)) # Corrected: product directly imported
  for combination in potencia:
      current_weight = sum(s * w for s, w in zip(combination, weights))
      current_profit = sum(s * p for s, p in zip(combination, profits))
      if current_weight <= capacity and current_profit >= desired_value:
        print("Si hay solución. Una de ellas es la que tupla:")
        return True
  return False