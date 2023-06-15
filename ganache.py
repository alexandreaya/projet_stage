# Code pour faire des transactions entre deux comptes

from web3 import Web3
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.eth.block_number)

account_1 = "0x68578085b3649430Ef056C5d3F261af4b307f727"

account_2 = "0x597a282998243244a0Bb3d074A6170Ef0E4D1abD"

private_key = "0x03594cfea057fe4e10897ca1095796ba3c6dec20cfd4a7c6825850f91b27c627"

# obtention du nonce

nonce = web3.eth.get_transaction_count(account_1)

# Effectuer une transaction

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.to_wei(1,'ether'),
    'gas': 2000000,
    'gasPrice': web3.to_wei('50','gwei')

}
# Signer la  transaction

signed_tx = web3.eth.account.sign_transaction(tx,private_key)
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(web3.to_hex(tx_hash))

