from .connect import w3
from . import CHAIN_ID
from .load_vars import PRIVATE_KEY, CONTRACT_ADDRESS, WALLET_ADDRESS
import json
from datetime import date


def exec_copy_trade(token_address, gas=1000000):
    address_checked = w3.isAddress(token_address)
    chainId = CHAIN_ID
    if address_checked:
        
        # CopyTradeExec.sol 0x90C39ce808411C41988595a7a8cC8A9e89235A0d
        contract_address = CONTRACT_ADDRESS
        abi = json.loads('''[
            {
                "inputs": [],
                "stateMutability": "nonpayable",
                "type": "constructor"
            },
            {
                "inputs": [
                    {
                        "internalType": "address",
                        "name": "tokenAddress",
                        "type": "address"
                    }
                ],
                "name": "swapEthForTokens",
                "outputs": [],
                "stateMutability": "payable",
                "type": "function"
            },
            {
                "inputs": [],
                "name": "uniswapV2Router",
                "outputs": [
                    {
                        "internalType": "contract IUniswapV2Router02",
                        "name": "",
                        "type": "address"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            }
        ]''')

        # Wallet to buy the tokens
        account = WALLET_ADDRESS

        ###############

        nonce = w3.eth.getTransactionCount(account)

        contract_instance = w3.eth.contract(address=contract_address,abi=abi)

        swap_func = contract_instance.functions.swapEthForTokens(token_address)

        swap_txn = swap_func.build_transaction({
            'chainId': chainId,
            'gas': gas,
            'maxFeePerGas': w3.toWei('2', 'gwei'),
            'maxPriorityFeePerGas': w3.toWei('1','gwei'),
            'value': w3.toWei('0.1', 'ether'),
            'nonce': nonce
        })

        signed_swap_txn = w3.eth.account.sign_transaction(swap_txn, private_key=PRIVATE_KEY)

        signed_swap_txn_hash = signed_swap_txn.hash

        w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)

        txn_receipt = w3.eth.waitForTransactionReceipt(signed_swap_txn_hash)
        
        return True, txn_receipt
    else:
        return False
        

def getTokenAddressFromTxHash(tx_hash: str):
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    
    with open("logs.txt", 'a') as file:
        file.write(tx_hash, date.today(), '\n')
    
    # address do token comprado
    return receipt['logs'][0]['address']
    
    

