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
st.sidebar.write("My [Email](mailto:mederic.peniguel@efrei.net)")


st.markdown("""
    <h2 style='text-align: center; font-size: 28px; color: #4CAF50;'>
        Bienvenue sur ma candidature pour le poste de Data Scientist / ML Ops Engineer (H/F) – Stage 6 mois chez Quitoque
    </h2>
    """, unsafe_allow_html=True)

# Présentation personnelle
st.header("À propos de moi")
st.write("""
Bonjour,

Je suis Médéric PENIGUEL, passionné par l’intelligence artificielle, l’analyse de données et l’utilisation de technologies innovantes pour résoudre les problèmes complexes. Compétent en Mathématiques, Python, Machine learning et deep learning , je recherche un stage de fin d’études pour mettre mes compétences techniques et analytiques au service de projets ambitieux en data engineering et IA. Rigoureux, organisé et créatif, je souhaite contribuer activement en équipe à des solutions innovantes. je suis enthousiaste à l'idée de contribuer à l'innovation culinaire de Quitoque.
""")


# Navigation vers les différentes sections
st.header("Explorez mon travail")
st.write("""
- **PARTIE 1 : Présentation des requêtes SQL**  
- **PARTIE 2 : Modélisation**  
- **PARTIE 3 : Programmation, Optimisation du Sac à Dos**  
- **PARTIE 4 : Questions annexes**  
""")
