import streamlit as st

from PIL import Image

# Configuration de la page
st.set_page_config(
    page_title="Bienvenue chez Quitoque",
    page_icon="🥕",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.sidebar.write("Made by Médéric PENIGUEL")
st.sidebar.write("My [linkedIn profil](https://www.linkedin.com/in/mederic-peniguel)")
st.sidebar.write("My [Email](mailto:votre.email@example.com)")


st.markdown("""
    <h2 style='text-align: center; font-size: 28px; color: #4CAF50;'>
        Bienvenue sur ma candidature pour le poste de Data MLOps chez Quitoque
    </h2>
    """, unsafe_allow_html=True)

# Présentation personnelle
st.header("À propos de moi")
st.write("""
Bonjour,

Je suis Médéric PENIGUEL, passionné par les données et les opérations de machine learning. 
Fort d'une expérience en [votre expérience pertinente], je suis enthousiaste à l'idée de contribuer à l'innovation culinaire de Quitoque.
""")


# Navigation vers les différentes sections
st.header("Explorez mon travail")
st.write("""
- **PARTIE 1 : SQL**  
  Découvrez mes compétences en requêtes SQL avancées.
- **PARTIE 2 : Modélisation**  
  Plongez dans mes approches de modélisation pour la prédiction de la demande.
- **PARTIE 3 : Knapsack**  
  Testez mon implémentation interactive de l'algorithme du sac à dos.
""")
