## Imports
import pandas as pd
from pulp import *

def knapsack_func(weights, values, capacity):

    n = len(weights)
    
    # Création de la matrice pour la programmation dynamique
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Remplissage de la matrice dp
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Récupération des objets sélectionnés
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    
    # Créer un DataFrame avec les informations des objets
    items_data = {
        "Item": [i for i in range(n)],
        "Weight": weights,
        "Value": values
    }
    df = pd.DataFrame(items_data)

    # Ajouter une colonne 'SELECTED' pour indiquer si l'objet est sélectionné
    df['SELECTED'] = df.index.isin(selected_items)

    print(f"{len(selected_items)} items selected. Results saved to 'chosen_items.xlsx'.")
    return df
