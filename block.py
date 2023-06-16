from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/91e6692c109c47c395f5d115a5a01395"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Pour avoir le numéro du dernier bloc
latest = web3.eth.block_number
print("Numéro du dernier bloc:",latest,"\n")

print ("Information du dernier bloc:",web3.eth.get_block(latest),"\n")

# Pour avoir les informations des 10 derniers blocs
print("Informations des 10 derniers blocs : \n")

for i in range (0,8) :
    print(web3.eth.get_block(latest - i))
hash = '0xe0884c6f8503f8b3e0386aaa00fcfdfcc66a2bc3f79814de6afa400a531c7d2d'
print(web3.eth.get_transaction_by_block(hash,2))











