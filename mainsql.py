"""
import mysql.connector

# Paramètres de connexion à la base de données
host = 'localhost'
database = 'blockchain'
user = 'root'
password = ''

# Connexion à la base de données
try:
    conn = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = conn.cursor()

    # Exécution de la requête SELECT
    query = "SELECT * FROM blocs"
    cursor.execute(query)

    # Récupération des résultats
    rows = cursor.fetchall()

    # Affichage des données
    for row in rows:
        block_id = row[0]
        hash = row[1]
        size = row[2]
        nonce = row[3]
        transactions_count = row[4]
        miner_id = row[5]
        output_value = row[6]
        confirmations = row[7]

        print("Block ID:", block_id)
        print("Hash:", hash)
        print("Size:", size)
        print("Nonce:", nonce)
        print("Transactions Count:", transactions_count)
        print("Miner ID:", miner_id)
        print("Output Value:", output_value)
        print("Confirmations:", confirmations)
        print()

    # Fermeture du curseur et de la connexion
    cursor.close()
    conn.close()

except mysql.connector.Error as error:
    print("Erreur de connexion à la base de données:", error)
"""
import mysql.connector

# Se connecter à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="blockchain"
)

# Créer un curseur pour exécuter les requêtes
cursor = conn.cursor()

# Fonction pour rechercher les informations d'un bloc par son identifiant
def recherche_bloc(block_id):
    # Requête SQL pour sélectionner les informations du bloc
    query = "SELECT * FROM blocs WHERE block_id = %s"

    # Exécution de la requête avec l'identifiant du bloc en tant que paramètre
    cursor.execute(query, (block_id,))

    # Récupération du résultat de la requête
    bloc = cursor.fetchone()

    # Vérifier si le bloc a été trouvé
    if bloc:
        # Afficher les informations du bloc
        print("Informations du bloc :")
        print("- Identifiant du bloc :", bloc[0])
        print("- Hash :", bloc[1])
        print("- Taille :", bloc[2])
        print("- Nonce :", bloc[3])
        print("- Nombre de transactions :", bloc[4])
        print("- Identifiant du mineur :", bloc[5])
        print("- Valeur de sortie :", bloc[6],"BTC")
        print("- Confirmations :", bloc[7])
        print("- Valeur:",bloc[8],"$")
        print("- BTC:", bloc[9])
        # Vous pouvez ajouter d'autres informations du bloc ici

        # Demander à l'utilisateur s'il souhaite rechercher un autre bloc
        reponse = input("Voulez-vous rechercher un autre bloc ? (Oui/Non) ")

        if reponse.lower() == "oui":
            # Demander à l'utilisateur de saisir l'identifiant du bloc
            block_id = input("Entrez l'identifiant du bloc : ")
            # Appeler la fonction de recherche du bloc récursivement
            recherche_bloc(block_id)
        else:
            print("Programme terminé.")
    else:
        print("Aucun bloc trouvé avec l'identifiant", block_id)

    # Fermer le curseur et la connexion à la base de données
    cursor.close()
    conn.close()

# Demander à l'utilisateur de saisir l'identifiant du bloc
block_id = input("Entrez l'identifiant du bloc : ")

# Appeler la fonction de recherche du bloc
recherche_bloc(block_id)





