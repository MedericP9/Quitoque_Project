import streamlit as st

st.sidebar.write("Made by Médéric PENIGUEL")
st.sidebar.write("My [linkedIn profil](https://www.linkedin.com/in/mederic-peniguel)")
st.sidebar.write("My [Email](mailto:mederic.peniguel@efrei.net)")

st.markdown("""
    <h2 style='text-align: center; font-size: 28px; color: #4CAF50;'>
        Réponses aux Questions Annexes
    </h2>
    """, unsafe_allow_html=True)


#les données viennent d'une BDD MySQL
st.markdown("""
**1) Comment votre interface serait impactée si les données d’objets doivent désormais être lues depuis une BDD MySQL ?**
""")

st.write("""
    
    Si les données des items doivent maintenant être lues depuis une base de données MySQL,
    il faudra que j'intègre à mes code python une connexion à la base de données. Cela pourrait se faire en utilisant
    une librairie Python comme par exemple pymysql ou SQLAlchemy. Ensuite je ferai en sorte d emodifier l'interface Streamlit pour donner la possibilité soit de faire manuellement soit automatiquement à partir de la BDD.
    """)

st.write("Après quelques recherches voici un code qui pourrait servire à faire cette econnexion à la BDD:")

st.code("""
    import pymysql
    import pandas as pd

    def get_items_from_db():
        connection = pymysql.connect(
            host='localhost', 
            user='root', 
            password='password', 
            database='knapsack_db'
        )
        query = "SELECT value, weight FROM items"
        df = pd.read_sql(query, connection)
        connection.close()
        return df.values.tolist()
    """, language='python')

st.write("""
    Dans le code, la fonction get_items_from_db() se connecte à une base MySQL et exécute une requête SQL
    pour récupérer les valeurs et poids des objets et renvoie les résultats sous forme de liste.
    
    
    """)

#Déploiement sur GCP
st.markdown("**2) Supposons que nous voulons déployer cette application (avec lecture des données depuis MySQL) sur GCP (Google Cloud Platform), comment procéderiez-vous ?**")

st.write("""
    N'ayant jamais déployé d'application sur GCP je me suis renseigné à ce sujet.
    
    Choisir une méthode de déploiement

    soit déployer à partir de Google App Engine (GAE) à l'aide de quelques lignes de commandes en connectant le projet à gcp à l'aide de fichier .yaml pour configurer l'environnemnt puis en déployant le projet
    ou soit via Google Cloud Run : qui est la Plateforme de déploiement google basée sur des conteneurs Docker.

    Pour la deuxième proposition il faut :
    - Créez un fichier Dockerfile pour définir l'environnement de conteneur.
    - Construisez et poussez l'image Docker vers Google Container Registry à partir du repo git.
    - Déployez l'application sur Cloud Run en utilisant des commandes : gcloud run deploy.
    
    A la fin du processus on obtient un lien qui permet d'accéder à la page web.
    """)
    
