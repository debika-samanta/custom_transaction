from web3 import Web3
import time

infura_url = 'https://goerli.infura.io/v3/a93439cd174c456cbd1640bffd139b6a'
account = '0xD10f4E2DDd6072ae47444022AF6b1736A98ADE58'
web3 = Web3(Web3.HTTPProvider(infura_url))

def confirmations(tx_hash):
    tx = web3.eth.get_transaction(tx_hash)
    return web3.eth.block_number - tx.blockNumber

def watch():
    while True:
        block = web3.eth.get_block('latest')
        print("Searching in block " + str(block.number))

        if block and block.transactions:
            for transaction in block.transactions:
                tx_hash = transaction.hex() # the hashes are stored in a hexBytes format
                tx = web3.eth.get_transaction(tx_hash)
                if tx.to != None:
                    if tx.to == account:
                        print("Transaction found in block {} :".format(block.number))
                        print({
                            "hash": tx_hash,
                            "from": tx["from"],
                            "value": web3.from_wei(tx["value"], 'ether'),
                            "input": str(tx["input"])
                            })
                        

        

watch()
# print(confirmations("0x0d40d60e118e9e1f61c2baa2252cc5f8b8ed491c885ec35db6fd6cfc8589c1a7"))