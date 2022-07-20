from web3 import Web3
from .load_vars import INFURA_URL


w3 = Web3(Web3.WebsocketProvider(INFURA_URL))
