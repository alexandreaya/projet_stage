# Code pour obtenir le dernier bloc etherum et le solde d'un compte à partir de son adresse

from web3 import Web3
infura_url = "https://mainnet.infura.io/v3/clé_infura"
web3 = Web3(Web3.HTTPProvider(infura_url))

print (web3.is_connected())
print ("le dernier bloc de la blockchain etherum est  :", web3.eth.block_number)

balance = web3.eth.get_balance("0x39C7BC5496f4eaaa1fF75d88E079C22f0519E7b9")
print ("le solde de ce compte est de :",web3.from_wei(balance, 'ether'),"eth")

# adresse etherum valide : 0x39C7BC5496f4eaaa1fF75d88E079C22f0519E7b9

