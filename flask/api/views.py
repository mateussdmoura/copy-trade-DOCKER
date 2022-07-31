from flask import Blueprint, Response
from .interactions import exec_copy_trade, getTokenAddressFromTxHash

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return '<h2>copy trade</h2>'

@views.route('/swap/<tokenAddress>')
def swap_token(tokenAddress):
    print("Starting Swap!") 
    print("Token Address:", str(tokenAddress))
    swapped, receipt = exec_copy_trade(str(tokenAddress))

    if swapped:
        print("Success Swap using wallet", receipt["from"])
        return Response(status=200)
    else:
        print("Fail Swap")
        return Response(status=404)
        
@views.route('/swap/<tokenAddress>/<gas>')
def swap_token_with_same_gas(tokenAddress, gas):
    print("Starting Swap!") 
    print("Token Address:", str(tokenAddress))
    swapped, receipt = exec_copy_trade(str(tokenAddress, gas=gas))
    print()

    if swapped:
        print("Success Swap using wallet", receipt["from"])
        return Response(status=200)
    else:
        print("Fail Swap")
        return Response(status=404)
    
@views.route('/swap/txHash/<txHash>')
def swap_token_using_receipt(txHash):
    print("Starting Swap!") 
    
    tokenAddress = getTokenAddressFromTxHash(txHash)
    
    print("Token Address:", str(tokenAddress))
    swapped, receipt = exec_copy_trade(str(tokenAddress))

    if swapped:
        print("Success Swap using wallet", receipt["from"])
        return Response(status=200)
    else:
        print("Fail Swap")
        return Response(status=404)

@views.route('/logs')
def show_logs():
    from .read_logs import logs
    return logs