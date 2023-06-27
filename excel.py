import openpyxl
from web3 import Web3
import datetime

infura_url = "https://mainnet.infura.io/v3/clé_infura"
web3 = Web3(Web3.HTTPProvider(infura_url))

start_block = 17534075
end_block = 17534126


excel_file_path = 'exported_data.xlsx'

try:
    workbook = openpyxl.load_workbook(excel_file_path)
except FileNotFoundError:
    workbook = openpyxl.Workbook()

sheet = workbook.active

sheet['A1'] = 'Numéro de bloc'
sheet['B1'] = 'Timestamp'
sheet['C1'] = 'Hash du bloc'
sheet['D1'] = 'Nombre de transactions'
sheet['E1'] = 'Gas utilisé'



row = 2

for block_number in range(end_block, start_block - 1, -1):
    block = web3.eth.get_block(block_number)
    block_hash = block['hash'].hex()
    timestamp = datetime.datetime.fromtimestamp(block['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
    transactions = len(block['transactions'])
    gas_used = block['gasUsed']

    sheet[f'A{row}'] = block_number
    sheet[f'B{row}'] = timestamp
    sheet[f'C{row}'] = block_hash
    sheet[f'D{row}'] = transactions
    sheet[f'E{row}'] = gas_used


    row += 1

workbook.save(excel_file_path)
