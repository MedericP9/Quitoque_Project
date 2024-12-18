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




from swiglpk import glp

def solve_linear_problem():
    # Créer un problème
    lp = glp.glp_create_prob()
    glp.glp_set_prob_name(lp, "Exemple")
    glp.glp_set_obj_dir(lp, glp.GLP_MAX)

    # Ajouter des variables
    glp.glp_add_cols(lp, 2)
    glp.glp_set_col_name(lp, 1, "x1")
    glp.glp_set_col_bnds(lp, 1, glp.GLP_LO, 0.0, 0.0)  # x1 >= 0
    glp.glp_set_obj_coef(lp, 1, 3.0)  # Coefficient objectif pour x1
    glp.glp_set_col_name(lp, 2, "x2")
    glp.glp_set_col_bnds(lp, 2, glp.GLP_LO, 0.0, 0.0)  # x2 >= 0
    glp.glp_set_obj_coef(lp, 2, 5.0)  # Coefficient objectif pour x2

    # Ajouter une contrainte
    glp.glp_add_rows(lp, 1)
    glp.glp_set_row_name(lp, 1, "c1")
    glp.glp_set_row_bnds(lp, 1, glp.GLP_UP, 0.0, 10.0)  # Contraintes x1 + x2 <= 10

    ia = glp.intArray(3)
    ja = glp.intArray(3)
    ar = glp.doubleArray(3)

    ia[1], ja[1], ar[1] = 1, 1, 1.0  # Coefficient de x1
    ia[2], ja[2], ar[2] = 1, 2, 1.0  # Coefficient de x2
    glp.glp_load_matrix(lp, 2, ia, ja, ar)

    # Résoudre
    simplex = glp.glp_simplex
    simplex(lp, None)

    # Obtenir les résultats
    z = glp.glp_get_obj_val(lp)
    x1 = glp.glp_get_col_prim(lp, 1)
    x2 = glp.glp_get_col_prim(lp, 2)

    # Nettoyer
    glp.glp_delete_prob(lp)

    return z, x1, x2









def knapsack_func(weights, values, capacity):


    print(solve_linear_problem())
    # Paramètres
    num_items = len(values)  # Nombre d'objets
    print(len(weights), len(values), capacity)
    # Pour utiliser pyomo
    solvername = "glpk"
    solver_path = setup_folder_path + "winglpk-4.65/glpk-4.65/w64/glpsol"
    print("Contenu du répertoire:", os.listdir(solver_path) if os.path.exists(solver_path) else "Répertoire introuvable")
    
    print(os.getcwd())
    print(solver_path)

    print("Solver path exists:", os.path.exists(solver_path))
    print("Solver is executable:", os.access(solver_path, os.X_OK))
    
    # Si le fichier n'est pas exécutable, modifiez ses permissions
    if not os.access(solver_path, os.X_OK):
        try:
            os.chmod(solver_path, 0o755)  # Rend le fichier exécutable
            print("Modified file permissions")
        except Exception as e:
            print(f"Could not modify permissions: {e}")
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
    opt = SolverFactory(solvername, executable=solver_path)
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
