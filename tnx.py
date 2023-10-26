from web3 import Web3

# Connect to an Ethereum node
w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/a93439cd174c456cbd1640bffd139b6a'))

# Replace these with the sender and receiver addresses
sender_address = '0xeC85984aB1f737979Ae3a640c66F49AB71aba490'
receiver_address = '0xD10f4E2DDd6072ae47444022AF6b1736A98ADE58'

# Your private key for the sender's address
private_key = 'a564e210c37c8569f90ec5c11d08a3733f68581ac333af3fbc1b48262fbf31a0'

# Convert ETH amount to Wei (1 ETH = 10^18 Wei)
amount_ether = 0.000001  # Change this to the amount you want to send
amount_wei = w3.to_wei(amount_ether, 'ether')

# Add your data in hexadecimal format
data = 'Bob'  # Replace with your own data in hexadecimal

# Get the sender's nonce (number of transactions sent from the address)
nonce = w3.eth.get_transaction_count(sender_address)

# Build the transaction
# The `transaction` dictionary is used to specify the details of the transaction you want to send on
# the Ethereum network. Here's a breakdown of each key-value pair in the dictionary:
data_string = "bob_owner"
hex_data = data_string.encode('utf-8').hex()

transaction = {
    'to': receiver_address,
    'value': amount_wei,
    'gas': 21176,  # Typical gas cost for a simple transaction
    'gasPrice': w3.to_wei('100', 'gwei'),  # Adjust gas price as needed
    'data': hex_data,  # Add your data here
    'nonce': nonce,
    'chainId': 5,  # Geroli
}

data_bytes = bytes.fromhex(hex_data)

# Decode bytes to a string
original_data = data_bytes.decode('utf-8')

# Print the original data
print("Original Data:", original_data)
# Sign the transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key)

# Send the transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Wait for the transaction to be mined
w3.eth.wait_for_transaction_receipt(tx_hash)

print(f'Transaction hash: {tx_hash.hex()}')
