from solders.pubkey import Pubkey
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solders.instruction import Instruction
from solders.system_program import TransferParams, transfer
from solders.transaction import Transaction as SoldersTransaction
from solders.message import Message
from solders.rpc.responses import GetAccountInfoResp

def get_total_minted(contract_address):
    client = Client("https://api.devnet.solana.com")
    contract_address_pubkey = Pubkey.from_string(contract_address)

    account_info = client.get_account_info(contract_address_pubkey).value
    if not account_info:
        print("Error fetching account information.")
        return None

    lamports = account_info.lamports

    return lamports

def get_lp_burned(contract_address, total_minted):
    client = Client("https://api.devnet.solana.com")
    contract_address_pubkey = Pubkey.from_string(contract_address)

    account_info = client.get_account_info(contract_address_pubkey).value
    if not account_info:
        print("Error fetching account information.")
        return None

    lamports = account_info.lamports

    return lamports

#  user input for the Solana token contract address
contract_address = input("Enter Solana token contract address: ")

total_minted = get_total_minted(contract_address)
if total_minted is not None:
    lp_burned = get_lp_burned(contract_address, total_minted)
    if total_minted is not None and lp_burned is not None:
        percentage_burned = (lp_burned / total_minted) * 100  # Calculate percentage
        print(f'Total LP burned for {contract_address}: {lp_burned} SOL ({percentage_burned:.2f}%)')
    else:
        print("Unable to calculate the percentage burned.")