## Imports
import pandas as pd
from pulp import *

def knapsack_func(weights, values, capacity):

    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Remplissage de la table de programmation dynamique
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Poids total maximal atteint
    max_weight = max(w for w in range(capacity + 1) if dp[n][w] > 0)

    # Récupération des objets sélectionnés
    w = max_weight
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    # Création du DataFrame
    df = pd.DataFrame({
        'Item': [f'Item{i+1}' for i in selected_items],
        'Weight': [weights[i] for i in selected_items],
        'Value': [values[i] for i in selected_items]
    })
    df = df.sort_values(by='ITEM').reset_index(drop=True)
    print(f"{len(selected_items)} items selected. Results saved to 'chosen_items.xlsx'.")
    
    return df
