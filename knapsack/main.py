## Imports
import pandas as pd
from pulp import *

def knapsack_func(weights, values, capacity):

    n = len(values)
    
    # Créer le problème
    prob = LpProblem("Knapsack_Problem", LpMaximize)
    
    # Variables de décision (binaires)
    x = [LpVariable(f"x{i}", cat='Binary') for i in range(n)]
    
    # Fonction objectif : maximiser la valeur totale
    prob += lpSum(values[i] * x[i] for i in range(n))
    
    # Contrainte de capacité
    prob += lpSum(weights[i] * x[i] for i in range(n)) <= capacity
    
    # Résoudre le problème
    prob.solve()
    
    # Récupérer les objets sélectionnés
    selected_items = [i for i in range(n) if x[i].varValue == 1]
    chosen_objects = [(i, weights[i - 1], values[i - 1]) for i in selected_items]
    df = pd.DataFrame(chosen_objects, columns=["Item", "Weight", "Value"])

    print(f"{len(selected_items)} items selected. Results saved to 'chosen_items.xlsx'.")
    return df
