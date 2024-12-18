## Imports
import pandas as pd
from pulp import *

def knapsack_func(weights, values, capacity):

    prob=LpProblem("Knapsack Problem", LpMaximize)
    x = [LpVariable(f"x{i}", cat='Binary') for i in range(len(values))]
    prob += lpSum([values[i] * x[i] for i in range(len(values))])
    prob += lpSum([weights[i] * x[i] for i in range(len(values))]) <= capacity
    
    prob.solve()
    selected_items = [i for i in range(len(values)) if x[i].varValue == 1]
    chosen_objects = [(i, weights[i - 1], values[i - 1]) for i in selected_items]
    df = pd.DataFrame(chosen_objects, columns=["Item", "Weight", "Value"])

    print(f"{len(selected_items)} items selected. Results saved to 'chosen_items.xlsx'.")
    return df
