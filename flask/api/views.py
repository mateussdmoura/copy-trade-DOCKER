from cgitb import handler
from flask import Blueprint, Response
from .interactions import exec_copy_trade
import logging
from datetime import datetime

views = Blueprint('views', __name__)

logger1 = logging
logger2 = logging

logger1.basicConfig(filename='./logs/swaps.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

logger2.basicConfig(filename='./logs/swaps.log', level=logging.WARNING, format='%(asctime)s:%(levelname)s:%(message)s')

@views.route('/')
def home():
    return '<h2>V1 copy trade bot by mourinha</h2>'

@views.route('/swap/<tokenAddress>')
def swap_token(tokenAddress):
    logger1.info("Starting Swap")
    logger1.info("Token Address:", str(tokenAddress))
    swapped, receipt = exec_copy_trade(str(tokenAddress))

    if swapped:
        logger1.info("Success Swap using wallet", receipt["from"])
        return Response(status=200)
    else:
        logger2.warning("Fail Swap")
        return Response(status=404)
        
@views.route('/swap/<tokenAddress>/<gas>')
def swap_token_with_same_gas(tokenAddress, gas):
    logger1.info("Starting Swap")
    logger1.info("Token Address:", str(tokenAddress))
    swapped, receipt = exec_copy_trade(str(tokenAddress, gas=gas))
    print()

    if swapped:
        logger1.info("Success Swap using wallet", receipt["from"])
        return Response(status=200)
    else:
        logger2.warning("Fail Swap")
        return Response(status=404)
    
