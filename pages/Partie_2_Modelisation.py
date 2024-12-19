import streamlit as st

st.sidebar.write("Made by Médéric PENIGUEL")
st.sidebar.write("My [linkedIn profil](https://www.linkedin.com/in/mederic-peniguel)")
st.sidebar.write("My [Email](mailto:mederic.peniguel@efrei.net)")

st.markdown(
    """
    <h2 style='text-align: center; font-size: 28px; color: #4CAF50;'>
        Partie 2 : Modélisation
    </h2>
    """,
    unsafe_allow_html=True,
)

st.markdown("### Approche pour la prédiction des demandes 📊")

st.markdown(
    f"""
    <div style="text-align: justify;">
        Cette page décrit les approches de modélisation visant à résoudre le problème de l'estimation de la répartition des demandes sur différentes recettes. L’objectif de cet exercice est de prédire la répartition des demandes pour de nouvelles recettes sur une semaine donnée, en sachant le nombre total de repas à préparer. Pour cela, il est nécessaire de s'appuyer sur des recettes préparées dans le passé, pour lesquelles des données sur la répartition des demandes ont été collectées.
   </br>
    </br>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    f"""
    <div style="text-align: center;">
        <b>Identification du type de problème :</b>

    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    f"""
    <div style="text-align: justify;">
Pour résoudre ce problème, ma première approche consiste à utiliser un modèle basé sur les similarités entre les recettes. Ce modèle attribuerait un poids à chaque recette en fonction de ces similarités.     </br>
      </br>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div style="text-align: center;">
        <b>Nettoyage des données</b>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    f"""
    <div style="text-align: justify;">
Je ne peux pas mettre en place directement un modèle car les données disponibles ne sont pas numériques mais textuelles. Je commencerai donc par nettoyer et normaliser le texte : 

**suppression des caractères spéciaux**

- suppression des accents et conversion des lettres majuscules en minuscules.

**Traitement des valeurs manquantes :**

- Lorsque des informations sont manquantes, plusieurs stratégies peuvent être utilisées : suppression, imputation, etc.

**Normalisation des données :**

- Pour rendre les features comparables entre elles, on peut normaliser ou standardiser les valeurs (par exemple, en utilisant la méthode Min-Max ou Z-score).
        
 </br>
 </br>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div style="text-align: center;">
        <b>Vectorisation des données textuelles</b>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    f"""
    <div style="text-align: justify;">
Une fois les données nettoyées, je procéderai à la vectorisation des ingrédients pour chaque recette. Par exemple, je pourrais utiliser des méthodes telles que TF-IDF ou Word2Vec pour transformer les ingrédients en vecteurs numériques exploitables. Une représentation par one-hot encoding pourrait également être utilisée si cela est pertinent.
Après avoir obtenu les vecteurs pour les recettes déjà réalisées dans le passé, je reproduirai le même processus pour les nouvelles recettes dont je souhaite estimer la demande future. Ainsi, j’aurai d’un côté les vecteurs représentant les anciennes recettes et, de l’autre, ceux des nouvelles recettes.
</br>
</br>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div style="text-align: center;">
Calcul de la répartition des commandes par semaine
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    f"""
    <div style="text-align: justify;">
Ensuite, pour chaque semaine, je calculerai la répartition des commandes par recette. Pour cela, je diviserai le nombre de commandes de chaque recette par le nombre total de commandes effectuées au cours de la même semaine.

Voici un exemple pour une semaine X (dans la suite de mon explication, j’ai attribué des valeurs fictives) :

        total de commande : 1000
        recette 1 : 200 commandes
        recette 2 : 500 commandes
        recette 3 : 300 commandes
        
        proportion de la recette 1 : 0.2 
        proportion de la recette 2 : 0.5
        proportion de la recette 3 : 0.4
</br>
</br>
    """,
    unsafe_allow_html=True,
)

st.markdown(
        f"""
    <div style="text-align: center;">
        <b>Première approche : Un modèle de machine learning</b>
    </div>
    """,
        unsafe_allow_html=True,
)

st.markdown(
        f"""
    <div style="text-align: justify;">
Ma première approche consisterait à utiliser un **modèle de régression linéaire** ou un autre modèle machine learning.
Les modèles de machine learning, notamment les arbres décisionnels comme le modèle random forest et les réseaux neuronaux, peuvent capturer des relations que l'on appelle non linéaires entre les ingrédients des recettes et la demande, contrairement à des méthodes basées uniquement sur la similarité (deuxième approche). Par exemple, la demande d’une recette pourrait être influencée de manière complexe par plusieurs ingrédients et leur combinaison (par exemple, une recette avec des ingrédients populaires mais peu utilisés ensemble pourrait avoir une demande différente de la somme des demandes des ingrédients individuels).
    </div>
    """,
        unsafe_allow_html=True,
)
st.markdown(
        """
        Ainsi les modèles de machine learning vont capturer les interactions entre les caractéristiques. 
    Étapes :
    1. **Entraînement** :  
       - **Entrées** : Les vecteurs des recettes historiques (basés sur leurs caractéristiques).  
       - **Cibles** : Les proportions de demande correspondantes.  
    
    2. **Prédiction** :  
       Une fois le modèle entraîné, nous utilisons les vecteurs des nouvelles recettes pour prédire leurs proportions de demande.
    
    3. **Ajustement** :
       Après prédiction, je normaliserai les résultats pour respecter le volume total prévu pour la semaine. (explication plus détaillée par la suite)
    
    
    """
)

st.markdown(
        f"""
    <div style="text-align: center;">
        <b>Évaluation des modèles</b>
    </div>
    """,
        unsafe_allow_html=True,
)

st.markdown(
        """
        <div style="text-align: justify;">
            
Tout d'abord je pourrais utiliser la cross-validation :
pour évaluer le modèle sur différents ensembles de données. Cela permet de s’assurer que le modèle généralise bien et n’est pas biaisé par un sous-ensemble spécifique de données.
ensuite pour évaluer les modèles, des métriques comme l'erreur quadratique moyenne (<b>RMSE</b>) ou le score <b>R²</b> peuvent être utilisées. 
Ces métriques permettent de mesurer la précision des prédictions et la qualité globale des modèles.
            </div>
    </br>
            """,
        unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div style="text-align: center;">
        <b>Autre approche : calcul de la similarité entre les anciennes recettes et les nouvelles recettes</b>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    f"""
    <div style="text-align: justify;">
    Ma deuxième approche dans le cas ou la première ne rendrait pas de bon résultat serait pour chaque nouvelle recette, nous évaluons sa similarité avec les anciennes recettes, en utilisant une métrique comme la cosine similarity. Cette mesure permet de comparer les nouvelles recettes avec les anciennes sur la base de leurs caractéristiques (par exemple, leurs ingrédients).
    Dans cet exemple, nous testons la similarité entre deux nouvelles recettes et trois anciennes recettes (les valeurs de similarité sont fictives) :

    Similarité entre la nouvelle recette 1 et les anciennes recettes :
    
        Ancienne recette 1 : 0.4
        Ancienne recette 2 : 0.8
        Ancienne recette 3 : 0.5

    Similarité entre la nouvelle recette 2 et les anciennes recettes :
    
        Ancienne recette 1 : 0.7
        Ancienne recette 2 : 0.4
        Ancienne recette 3 : 0.6
</div>
</br>
</br>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    f"""
    <div style="text-align: center;">
        <b>Calcul du poids des nouvelles recettes pour une semaine</b>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div style="text-align: justify;">
        L'objectif est d'attribuer un poids à chaque nouvelle recette en fonction de sa similarité avec les anciennes recettes et de la popularité de ces dernières. Pour cela, nous multiplions la similarité calculée entre une nouvelle recette et une ancienne recette par la proportion de la demande associée à cette ancienne recette.
        Ainsi, une nouvelle recette fortement similaire à une ancienne recette populaire obtiendra un poids élevé. À l'inverse, une recette similaire à une ancienne recette peu populaire aura un poids faible.
        
        Exemple:
        Rappel répartition de la demande pour une semaine X
        
                proportion de l'ancienne recette : 0.2 
                proportion de l'ancienne recette : 0.5
                proportion de l'ancienne recette : 0.4
        
        Pour la nouvelle recette 1 :
        
                similarité entre nouvelle recette 1 et ancienne recette 1 : 0.4
                similarité entre nouvelle recette 1 et ancienne recette 2 : 0.8
                similarité entre nouvelle recette 1 et ancienne recette 3 : 0.5
                
        estimation du poids de la nouvelle 1 recette vis-à-vis des anciennes recettes de la semaine X : 
        
                0.2*0.4+0.5*0.8+0.4*0.5 = 0.68
        
        Pour la nouvelle recette 2 : 
        
                similarité entre nouvelle recette 2 et ancienne recette 1 : 0.7
                similarité entre nouvelle recette 2 et ancienne recette 2 : 0.4
                similarité entre nouvelle recette 2 et ancienne recette 3 : 0.6
                
               
        estimation du poids de la nouvelle recette 2 vis-à-vis des anciennes recettes de la semaine X : 
        
                0.2*0.7+0.5*0.4+0.4*0.6 = 0.58    
        
</br>
</br>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    f"""
    <div style="text-align: justify;">
        Ainsi, la nouvelle recette 1 obtient un poids plus élevé car elle est plus similaire à l’ancienne recette 2, qui était très populaire.    </div>
</br>
</br>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    f"""
    <div style="text-align: center;">
        <b>Calcul du poids des nouvelles recettes sur plusieurs semaines</b>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div style="text-align: justify;">
        Pour estimer le poids d'une nouvelle recette en fonction de plusieurs semaines, nous additionnons les poids calculés pour chaque semaine précédente. Cette approche permet de capturer l'évolution des tendances au fil du temps.
        À la fin de ce processus, chaque nouvelle recette est associée à un poids total, calculé sur la base des similarités avec les recettes précédentes et de la popularité historique de ces dernières.    </div>
</br>
</br>
""",
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div style="text-align: center;">
        <b>Estimation de la répartition des commandes (pour les deux approches)</b>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div style="text-align: justify;">
        Pour obtenir la proportion estimée de chaque nouvelle recette, il suffit de diviser le poids ou la proportion obtenue dans les différentes approches pour cette recette par la somme des poids ou des proportions de toutes les nouvelles recettes.
        Ensuite, pour déterminer le nombre de commandes pour une recette donnée, on multiplie cette proportion par le volume total de commandes prévu pour la semaine.
</br>
</br>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div style="text-align: center;">
        <b>Limites des approches</b>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
        <div style="text-align: justify;">
        
- Les modèles se basent sur des données historiques, ce qui peut poser problème pour les recettes avec des ingrédients nouveaux.  

- Lors de semaines avec un faible volume de commandes, les proportions calculées peuvent être peu représentatives, car la proportion se calcule uniquement sur une semaine. Ainsi, une proportion de 0,2 d'une semaine n'est pas toujours équivalente à une proportion de 0,2 d'une autre semaine. On pourrait donc modifier le calcul pour qu'il soit proportionnel au nombre de commandes. Cependant, dans ce cas, les anciennes recettes, qui attiraient généralement moins de clients car l'entreprise en était à ses débuts, seraient pénalisées, bien qu'elles soient populaires.

</div>
</br>
</br>
        """,
    unsafe_allow_html=True,
)

st.markdown(
        f"""
    <div style="text-align: center;">
        <b>Pour améliorer les prédictions</b>
    </div>
    """,
        unsafe_allow_html=True,
)

st.markdown(
        """
            <div style="text-align: justify;">
Pour essayer d'améliorer les prédictions il pourrait être très interessant de prendre en compte des éléments dans les modèles comme les saisons et les tendances :

- Saisonnalité des ingrédients : des ingrédients sont populaires à certaines périodes de l'année (par exemple, des recettes à base de courge en automne). Intégrer cette information dans les modèles pourrait améliorer les prédictions pour ne pas prendre en compte les recettes qui ne correspondent pas à la bonne saison et qui pourraient donc impacter négativement les prédictions.
                
- Analyse de la tendance des consommateurs : Utiliser les données sur la consommation des clients au fil des années pour identifier les tendances de long terme et les évolutions dans les préférences alimentaires.
        
- Enfin dans le cas d'un modèle de machine learning il resterait très important de réentrainer celui-ci régulièrement pour qu'il puisse rester à jour sur les évolutions de la consommation.
        
</div>
            """,
        unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div style="text-align: center;">
        <b>Conclusion</b>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
        <div style="text-align: justify;">
        Ces approches, qu'elles soient basées sur les similarités ou des modèles de machine learning, vise à estimer la répartition des commandes pour de nouvelles recettes. 
        Bien que des ajustements et une réflexion plus profonde soient nécessaires pour surmonter certaines limites, ces solutions offrent une bonne base pour résoudre ce type de problème.
        </div>
        """,
    unsafe_allow_html=True,
)

