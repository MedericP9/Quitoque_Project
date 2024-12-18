## Imports

import os
import sys
from wsgiref.validate import validator

# Pour ne pas créer de cache
sys.dont_write_bytecode = True

import numpy as np
import pandas as pd

import random
from pyomo.environ import *


## Gestion des chemins

# Chemins généraux
root_folder_path = os.getcwd()
setup_folder_path = root_folder_path + "/knapsack/setup/"
outputs_folder_path = os.path.abspath(os.path.join(root_folder_path, "..", "outputs"))

def knapsack_func(weights, values, capacity):
    # Paramètres
    num_items = len(values)  # Nombre d'objets
    print(len(weights), len(values), capacity)
    # Pour utiliser pyomo
    solvername = "glpk"
    solver_path = setup_folder_path + "winglpk-4.65/glpk-4.65/w64/glpsol.exe"
    # Création du modèle
    model = ConcreteModel()

    # Indices des objets
    model.item_indexes = RangeSet(num_items)

    # Paramètres de poids et de valeur
    model.weight = Param(
        model.item_indexes, initialize={i + 1: weights[i] for i in range(num_items)}
    )
    model.value = Param(
        model.item_indexes, initialize={i + 1: values[i] for i in range(num_items)}
    )
    # Capacité du sac à dos
    model.capacity = capacity

    # Variable de décision : 1 si l'objet est choisi, 0 sinon
    model.x = Var(model.item_indexes, domain=Binary)

    # Fonction objectif : maximiser la valeur totale
    model.objective = Objective(
        expr=sum(model.value[i] * model.x[i] for i in model.item_indexes),
        sense=maximize,
    )

    # Contrainte : ne pas dépasser la capacité
    def capacity_constraint_rule(model):
        return (
            sum(model.weight[i] * model.x[i] for i in model.item_indexes)
            <= model.capacity
        )

    model.constraint = Constraint(rule=capacity_constraint_rule)
    # Résolution du modèle
    opt = SolverFactory(solvername, executable=solver_path, set_executable=False)
    results = opt.solve(model)

    ## Résultats
    # Récupération des objets choisis
    chosen_items = [i for i in model.item_indexes if model.x[i].value == 1]

    # Création d'un DataFrame pour les résultats
    chosen_objects = [(i, weights[i - 1], values[i - 1]) for i in chosen_items]
    df = pd.DataFrame(chosen_objects, columns=["Item", "Weight", "Value"])

    # Exportation des résultats dans un fichier Excel
    # df.to_excel(outputs_folder_path+'\\chosen_items.xlsx', index=False)

    print(f"{len(chosen_items)} items selected. Results saved to 'chosen_items.xlsx'.")
    return df
