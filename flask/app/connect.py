from web3 import Web3
import json

infura_url = 'wss://ropsten.infura.io/ws/v3/aa885358df724383964e75b007989f0f'

w3 = Web3(Web3.WebsocketProvider(infura_url))
