import json
from web3 import Web3
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.default_account = web3.eth.accounts[0]

abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

address = web3.to_checksum_address("0x7C004C5Ed108a5F15a04FdD4773d51E9ad5cc5E0")
contract = web3.eth.contract(address=address, abi=abi)

print(contract.functions.greet().call())
tx_hash = (contract.functions.setGreeting('Bonjour !').transact())

web3.eth.wait_for_transaction_receipt(tx_hash)
print('Uptaded greeting: {}'.format(
    contract.functions.greet().call()
))


