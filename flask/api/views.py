from flask import Blueprint, Response
from .interactions import exec_copy_trade

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return '<h2>V1 copy trade bot by mourinha</h2>'

@views.route('/swap/<tokenAddress>')
def swap_token(tokenAddress):
    print()
    print("Starting Swap")
    print("Token Address:", str(tokenAddress))
    swapped, receipt = exec_copy_trade(str(tokenAddress))
    print()

    if swapped:
        print("Success Swap using wallet", receipt["from"])
        print()
        return Response(status=200)
    else:
        print("Fail Swap")
        print()
        return Response(status=404)
        
@views.route('/swap/<tokenAddress>/<gas>')
def swap_token_with_same_gas(tokenAddress, gas):
    print()
    print("Starting Swap")
    print("Token Address:", str(tokenAddress))
    swapped, receipt = exec_copy_trade(str(tokenAddress, gas=gas))
    print()

    if swapped:
        print("Success Swap using wallet", receipt["from"])
        print()
        return Response(status=200)
    else:
        print("Fail Swap")
        print()
        return Response(status=404)
    
