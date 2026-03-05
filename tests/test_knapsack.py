from bfctcv import knapsack_boolean, knapsack_problem

def test_knapsack_boolean():
    assert knapsack_boolean(220, 50, [60, 100, 120], [10, 20, 30]) == True
    assert knapsack_boolean(60, 10, [60, 100, 120], [10, 20, 30]) == True
    assert knapsack_boolean(100, 20, [60, 100, 120], [10, 20, 30]) == True