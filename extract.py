from web3 import Web3
from web3.auto import w3
from eth_account import Account

print("Bienvenue dans mon programme d'extraction de données de la blockchain Ethereum")

INFURA_API_KEY = 'clé_infura'  # Remplacez par votre propre clé API Infura

w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_API_KEY}'))

# Code pour créér une adresse et une private key

account = Account.create()

print(f"New account created: {account.address}")
print(f"Private key: {account._private_key.hex()}\n")


# Code pour rechercher une adresse d'un compte à partir de la private key

from eth_account import Account

private_key = '0xa103f38085813146f241dd091676c4d2a4e5b808804dc56288e4ffb27b28f126'
account = Account.from_key(private_key)
print(f"Compte trouvé: {account.address}")

# Intéragir avec les smarts contracts
# Nécssite l'adresse du contrat et L'ABI

contract_address = 'CONTRACT_ADDRESS'
contract_abi=[...] # Your contract ABI contract=w3.eth.contract(address=contract_address, abi=contract_abi)


""""
CODE POUR TROUVER LE SOLDE D'UN COMPTE A PARTIR DE SON ADRESSE

from web3 import Web3 

address = '0x55d4157e8ffa3368ac6bc15e010394f707ea3d0d'
checksum_address = Web3.to_checksum_address(address)

balance = w3.eth.get_balance(checksum_address)
print(f"Account balance: {w3.from_wei(balance, 'ether')} ETH")


balance = w3.eth.get_balance('')
print(f"Account balance: {w3.from_wei(balance, 'ether')} ETH")
"""


""""
infura_url = 'https://mainnet.infura.io/v3/91e6692c109c47c395f5d115a5a01395'  # Remplacez 'votre_cle_api' par votre clé API Infura
w3 = Web3(Web3.HTTPProvider(infura_url))


latest_block = w3.eth.get_block('latest')
print(latest_block)
latest_block = w3.eth.get_block('latest')
block_dict = dict(latest_block) 
print("Base Fee Per Gas:", block_dict['baseFeePerGas']) 
print("Difficulty:", block_dict['difficulty'])
# ... continuer avec d'autres informations du bloc

block_number = 17463125  # Remplacez par le numéro de bloc souhaité
block = w3.eth.get_block(block_number)
transactions = block['transactions']
print(transactions)
"""













