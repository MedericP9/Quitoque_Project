import streamlit as st

st.sidebar.write("Made by Médéric PENIGUEL")
st.sidebar.write("My [linkedIn profil](https://www.linkedin.com/in/mederic-peniguel)")
st.sidebar.write("My [Email](mailto:votre.email@example.com)")

st.title("PARTIE 2 : Modélisation")
st.markdown("### Approche pour la prédiction des demandes 📊")
st.write("""
**Contexte :**  
Prédiction du volume de commandes pour des nouvelles recettes en se basant sur des recettes historiques.

**Approche proposée :**  
- Traitement des intitulés avec **TF-IDF** ou **Word2Vec**.
- Calcul de similarité entre recettes avec **cosine similarity**.
- Utilisation de la demande moyenne des recettes similaires pour prédire la demande.

**Alternative :**  
Modèles supervisés comme **régression linéaire** ou **Random Forest**.
""")

# Ajout d'une documentation intégrée
st.markdown("""
#### Instructions :
Cette page décrit les approches de modélisation pour résoudre le problème.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Linear_regression.svg/640px-Linear_regression.svg.png",
        caption="Exemple de prédiction avec régression linéaire")
