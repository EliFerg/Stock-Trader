import requests, json
from Stocklist import get_URL, addToWatchList, print_watchList
#from Auto_Check import auto_check, price
#addToWatchList()
#print_watchList()

'''Obtain from alpaca's website'''
key = 'KEY'
sec = 'SECRET_KEY'

url = "https://paper-api.alpaca.markets"
account_url = "{}/v2/account".format(url)
order_url = "{}/v2/orders".format(url)

headers = {"APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": sec}

def get_account():
    r = requests.get(account_url, headers=headers)

    #print(r.content)

    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.post(order_url, json = data, headers=headers)

    #print(r.content)

    return json.loads(r.content)

def sell_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.post(order_url, json = data, headers=headers)

    #print(r.content)

    return json.loads(r.content)

def view_orders():
    r = requests.get(order_url, headers=headers)

    return json.loads(r.content)
