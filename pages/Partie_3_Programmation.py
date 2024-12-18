import streamlit as st
import pandas as pd
from knapsack.main import knapsack_func
import matplotlib.pyplot as plt

st.sidebar.write("Made by Médéric PENIGUEL")
st.sidebar.write("My [linkedIn profil](https://www.linkedin.com/in/mederic-peniguel)")
st.sidebar.write("My [Email](mailto:mederic.peniguel@efrei.net)")

st.markdown("""
    <h2 style='text-align: center; font-size: 28px; color: #4CAF50;'>
        Optimisation du Sac à Dos
    </h2>
    """, unsafe_allow_html=True)

st.write("⚠️ Pour la version déployée de l'application Streamlit, j'ai recodé le solveur en Python afin qu'il fonctionne dans un environnement Linux, comme celui de Streamlit Cloud. La version utilisant le solveur fourni est néanmoins disponible dans les fichiers transmis avec le lien de cette application Streamlit.") 

st.header("Paramètres du problème")
values = st.text_input(
    "Valeurs des objets (séparées par des virgules)", "10, 20, 30, 40"
)
weights = st.text_input("Poids des objets (séparés par des virgules)", "1, 3, 4, 5")
capacity = st.number_input("Capacité du sac (poids maximum)", min_value=1, value=7)

try:
    values = [int(x) for x in values.split(",")]
    weights = [int(x) for x in weights.split(",")]
except ValueError:
    st.error("Assurez-vous d'entrer des valeurs valides pour les poids et valeurs.")

# Vérification de cohérence
if len(values) != len(weights):
    st.error("Les valeurs et les poids doivent avoir la même longueur.")
else:  
    if st.button("Lancer l'optimisation"):
        with st.spinner("Optimisation en cours..."):
            selected_items = knapsack_func(weights, values, capacity)
            st.success("Optimisation terminée !")

        st.header("Résultats")
        print(selected_items)
        st.dataframe(selected_items)

        st.download_button(
            label="Télécharger les résultats en Excel",
            data=selected_items.to_csv(index=False),
            file_name="resultats_knapsack.csv",
            mime="text/csv",
        )

        total_weight = sum(selected_items["Weight"])
        fig, ax = plt.subplots()
        ax.barh(["Capacity", "Weight used"], [capacity, total_weight], color=["grey", "green"])
        ax.set_title("Utilisation de la capacité du sac à dos")
        st.pyplot(fig)
