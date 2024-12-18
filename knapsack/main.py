## Imports
import pandas as pd
from pulp import *

def knapsack_func(weights, values, capacity):

    n = len(items)
    
    # Table de programmation dynamique
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Remplissage de la table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Valeur maximale obtenue
    max_value = dp[n][capacity]
    
    # Récupération des objets sélectionnés
    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    
    # Création du DataFrame
    df = pd.DataFrame({
        'Item': [items[i] for i in selected_items],
        'Weight': [weights[i] for i in selected_items],
        'Value': [values[i] for i in selected_items]
    })

    # Ajouter une colonne 'SELECTED' pour indiquer si l'objet est sélectionné
    df['SELECTED'] = df.index.isin(selected_items)

    print(f"{len(selected_items)} items selected. Results saved to 'chosen_items.xlsx'.")
    return df
