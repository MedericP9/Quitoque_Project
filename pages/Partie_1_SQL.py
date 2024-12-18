import streamlit as st

st.sidebar.write("Made by Médéric PENIGUEL")
st.sidebar.write("My [linkedIn profil](https://www.linkedin.com/in/mederic-peniguel)")
st.sidebar.write("My [Email](mailto:mederic.peniguel@efrei.net)")

st.markdown("""
    <h2 style='text-align: center; font-size: 28px; color: #4CAF50;'>
        Partie 1 : Présentation des requêtes SQL 📄
    </h2>
    """, unsafe_allow_html=True)

st.markdown("""
#### Instructions :
Cette page présente les requêtes SQL demandées dans le test technique.
""")

st.write("""
**Requête 1 :**  
Sélectionner pour chaque client sa ville, son régime alimentaire, la date de sa dernière commande payée, 
et le nombre total de commandes payées.
    """)

# Exemple d'affichage des requêtes SQL
st.code("""
SELECT 
    client.id_client,
    client.ville,
    client.regime_alimentaire,
    MAX(commande.date_livraison) AS derniere_date_commande_payee,
    COUNT(commande.id_commande) AS nombre_commandes_payees
FROM 
    client
JOIN 
    commande 
ON 
    client.id_client = commande.id_client
WHERE 
    commande.statut = 'PAYED'
GROUP BY 
    client.id_client;
""", language="sql")

st.markdown("""
**Requête 2 :**
Lister toutes les commandes avec les informations suivantes : ID commande, date de livraison, prix TTC,
et somme totale des commandes du client.
""")

st.code("""
SELECT 
    c1.id_commande,
    c1.date_livraison,
    c1.prix_TTC,
    SUM(c2.prix_TTC) AS somme_prix_TTC_client
FROM 
    commande c1, commande c2
WHERE 
    c1.id_client = c2.id_client
GROUP BY 
    c1.id_commande;
""", language="sql")
