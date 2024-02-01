# **************Written_By_Ali_Mehrban***************
# This program is a very simplified example of a customized Blockchain Monitoring tool written in Python to 
# replace platform specific tools such as Prometheus or Grafana!
#---------------------------------------------------------------------------------------------------------------

# Library for interacting with Ethereum-based blockchains
import web3  
import time
import logging

# Connect to the blockchain node
w3 = web3.Web3(web3.HTTPProvider("http://localhost:8545"))  # Should be changed based on each node


# Configure logging
logging.basicConfig(filename="blockchain_monitor.log", level=logging.INFO)

# Define monitoring functions
def monitor_block_time():
    latest_block = w3.eth.block_number
    start_time = time.time()
    while w3.eth.block_number == latest_block:
        time.sleep(1)
    end_time = time.time()
    block_time = end_time - start_time
    logging.info(f"Block time: {block_time:.2f} seconds")



def monitor_transaction_count():
    pending_tx_count = w3.eth.get_pending_transaction_count()
    logging.info(f"Pending transactions: {pending_tx_count}")



def monitor_contract_events(contract_address):
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)  # Load contract ABI
    events = contract.events.MyEvent.createFilter(fromBlock="latest")
    for event in events.get_new_entries():
        logging.info(f"Contract event: {event}")



# Schedule monitoring tasks
while True:
    monitor_block_time()
    monitor_transaction_count()
    monitor_contract_events("0x...")  #it is template --> change it with the related contract address
    time.sleep(60)  # Monitor every 60 seconds
