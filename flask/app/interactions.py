from .connect import w3
from . import CHAIN_ID
import json
from time import sleep

def exec_copy_trade(token_address, gas=1000000):
    address_checked = w3.isAddress(token_address)
    chainId = CHAIN_ID
    if address_checked:
        
        # CopyTradeExec.sol 0x90C39ce808411C41988595a7a8cC8A9e89235A0d
        contract_address = '0x90C39ce808411C41988595a7a8cC8A9e89235A0d'
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
        account = '0x5b9d44F1660826e9F0DC7dD6c5Fc44DEDBa79873'
        private_key = 'bb7fa0ce99ba256d30cb38e63b3afa541d5ef89f4a62f3883c88c737ea3a39a6'

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

        signed_swap_txn = w3.eth.account.sign_transaction(swap_txn, private_key=private_key)

        signed_swap_txn_hash = signed_swap_txn.hash

        w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)

        txn_receipt = w3.eth.waitForTransactionReceipt(signed_swap_txn_hash)
        
        return True, txn_receipt
    else:
        return False
        


