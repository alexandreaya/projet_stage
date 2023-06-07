""""
#ensoleille = True
#if ensoleille :
#   print ("allons à la plage")
#else :
#   print ("restons à la maison")

#neige = False
#if neige :
#   print ("bohnome de neige")
#else :
#    print ("allons à la plage")
#
#if ensoleille and neige :
#   print ("restons à la maison")
#elif ensoleille and not neige:
#    print ("allons à la plage")

#else :
#   print ("allons au travail")

# import hashlib

#class popcoin :
#   def __init__(self, previous_block_hash, transaction_list):

#       self.previous_block_hash = previous_block_hash
#       self.transaction_list = transaction_list

#       self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
#       self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

#   block1 = popcoin ('firstblock', [t1, t2])


#   print(f"Block 1 data: {block1.block_data}")
#   print(f"Block 1 hash: {block1.block_hash}")

# code pour extraire les données d'une blockchain en utilisant la bibiliothéque "bitcoinlib"

import requests

# Identifiant du bloc

block_id = 792116

# URL de l'API de Blockchain.com pour obtenir les informations d'un bloc
url = f"https://blockchain.info/rawblock/{'0000000000000000000244546811d58e7d57aca2ea8148c4de17748a2abf4428'}"

# Effectuer la requête GET à l'API
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Récupérer les données JSON de la réponse
    block_data = response.json()

    # Afficher les informations du bloc
    print("Informations du bloc :")
    print("- Hash du bloc :", block_data['hash'])
    print("- Horodatage :", block_data['time'])
    print("- Taille :", block_data['size'])
    print("- Nonce :", block_data['nonce'])

    # Ajouter ici d'autres informations du bloc que vous souhaitez extraire
    print("- Nombre de transactions :", len(block_data['tx']))
    print("- Identifiant du mineur :", block_data['tx'][0]['inputs'][0]['prev_out']['addr'])
    print("- Valeur de sortie du bloc :", block_data['tx'][0]['out'][0]['value'])
    # Vous pouvez explorer la structure de données JSON pour extraire d'autres informations souhaitées

else:
    print("Erreur lors de la requête à l'API")

#try:
    #   import hashlib
    #print("Le module hashlib est disponible.")
    #except ImportError:
    #print("Le module hashlib n'est pas disponible.")

# URL de l'API blockchain.com : "wss://ws.blockchain.info/mercury-gateway/v1/ws"
# celle là aussi peut-etre : https://api.blockchain.com/v3/exchange

import requests
import json

# Identifiant du bloc
block_id = 792116

# URL de l'API de Blockchain.com pour obtenir les détails d'un bloc
url = f"https://blockchain.info/rawblock/{block_id}"

# Effectuer la requête GET à l'API
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Récupérer les données JSON de la réponse
    block_data = response.json()

    # Afficher les données JSON formatées
    print(json.dumps(block_data, indent=4))

else:
    print("Erreur lors de la requête à l'API")
"""
import requests

# Saisie de l'identifiant du bloc par l'utilisateur

while True:
    user_input = input("Veuillez saisir L'identifiant du bloc : ")

    if len(user_input) == 6 and user_input.isdigit():
        # Convertir la saisie de l'utilisateur en un entier
        block_id = int(user_input)
        break  # Sortir de la boucle si l'entrée est valide
    else:
        print("Erreur : L'identifiant du bloc doit etre comppoosé de 6 chiffres ")

# Le reste du code continue ici avec l'identifiant de bloc valide (block_id)


# URL de l'API de Blockchain.com pour obtenir les informations d'un bloc
url = f"https://blockchain.info/rawblock/$block_hashpopom{'00000000000000000001f940abcfb886df87b799a1f76b3065775c3b2195330f'}"

# Effectuer la requête GET à l'API
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Récupérer les données JSON de la réponse
    block_data = response.json()

    # Afficher les informations du bloc
    print("Informations du bloc :")
    print("- Hash du bloc :", block_data['hash'])
    print("- Horodatage :", block_data['time'])
    print("- Taille :", block_data['size'])
    print("- Nonce :", block_data['nonce'])

    # Ajouter ici d'autres informations du bloc que vous souhaitez extraire
    print("- Nombre de transactions :", len(block_data['tx']))
    print("- Identifiant du mineur :", block_data['tx'][0]['inputs'][0]['prev_out']['addr'])
    print("- Valeur de sortie du bloc :", block_data['tx'][0]['out'][0]['value'])
    # Vous pouvez explorer la structure de données JSON pour extraire d'autres informations souhaitées

else:
    print("Erreur lors de la requête à l'API")









