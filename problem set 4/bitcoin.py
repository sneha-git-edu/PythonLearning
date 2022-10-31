#implement a program that:
#Expects the user to specify as a command-line argument the number of Bitcoins n, , that they would like to buy. If that argument
#  cannot be converted to a float, the program should exit via sys.exit with an error message.
#Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON
#  object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
#Outputs the current cost of  Bitcoins in USD to four decimal places, using , as a thousands separator.
import json
import requests 
import sys
try:
    if sys.argv[1].isnumeric():
        bitcoin_price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json' )
        o = bitcoin_price.json()
        price = o.keys()
        price = o.get('bpi')
        price_ = price.get('USD')
        price_ = (price_.get('rate_float'))
 
        amount = (float(price_))*(float(sys.argv[1]))
        print(f"${amount:,.4f}")
    else:
        print('Command-line argument is not a number')
    

except IndexError :
    print('Missing command-line argument')
    sys.exit()

