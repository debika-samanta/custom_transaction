from web3 import Web3
import requests

wallet_address = "0xD10f4E2DDd6072ae47444022AF6b1736A98ADE58"

# Initialize Web3 with Infura HTTP provider
infura_url = f"https://goerli.infura.io/v3/a93439cd174c456cbd1640bffd139b6a"
w3 = Web3(Web3.HTTPProvider(infura_url))

# Function to handle incoming transactions
def handle_incoming_transaction(event):
    print(f"Incoming transaction detected: {event['transactionHash'].hex()}")

# Create a Web3 contract instance for ERC-20 Token (if needed)
# contract = w3.eth.contract(address="TOKEN_CONTRACT_ADDRESS", abi=ABI)

# Set up an event filter for incoming transactions
filter = w3.eth.filter({'from':'0xeC85984aB1f737979Ae3a640c66F49AB71aba490' ,'to': wallet_address,'chainId': 5})

# Function to poll for new events
def poll_for_events():
    while True:
        try:
            events = w3.eth.get_filter_changes(filter.filter_id)
            for event in events:
                handle_incoming_transaction(event)
        except Exception as e:
            print(f"Error: {e}")

# Keep the script running to continue polling for events
try:
    poll_for_events()
except KeyboardInterrupt:
    pass
