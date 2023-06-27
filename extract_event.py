from web3 import Web3

# URL du nœud Ethereum
infura_url = 'https://mainnet.infura.io/v3/clé_infura'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Filtrer les transactions en attente (de validation)
pending_transactions = web3.eth.get_block('pending').transactions
print("Transactions en attente:")
for tx_hash in pending_transactions:
    tx = web3.eth.get_transaction(tx_hash)
    print("Transaction Hash:", tx_hash.hex())
    print("From Address:", tx['from'])
    print("To Address:", tx['to'],"\n")
