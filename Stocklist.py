import requests
from bs4 import BeautifulSoup
from Stock_class import STOCK

stockList = []
auto_stocklist = []

def get_URL():
    query = input("What stock would you like to look up:  ")
    query = query.replace(' ', '+')
    URL = f"https://google.com/search?q={query}"

    headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    currentPrice = soup.find(jsname = 'vWLAgc').get_text()
    print("$" + currentPrice)

def auto_pricer(query):
    query = query.replace(' ', '+')
    URL_3 = f"https://google.com/search?q={query}+stock"
    #print(URL_3)

    headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    page = requests.get(URL_3, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    currentPricer = soup.find(jsname = 'vWLAgc').get_text()
    #print("$" + currentPricer)

    return currentPricer

#auto_pricer('AAPL')

def addToWatchList():
    query = input("What stock would you like to add to watchlist:  ")
    stockList.append(query)

def print_watchList():
    for stock in stockList:
        query = stock
        query = query.replace(' ', '+')
        URL = f"https://google.com/search?q={query}"

        headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        currentPrice = soup.find(jsname = 'vWLAgc').get_text()
        print(stock + ":  $" + currentPrice)

#response = create_order("AAPL", 100, "buy", "market", "gtc")

def fill_stocklist_auto():
    URL_2 = f"https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/"

    headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    page = requests.get(URL_2, headers=headers)
    soup_2 = BeautifulSoup(page.content, 'html.parser')

    #print(page.status_code)

    topMovers = soup_2.find_all(class_ = "tv-screener__description")

    topMovers = soup_2.find_all(class_ = "tv-screener__symbol")


    #print(topMovers)

    index = 0
    index2 = 0
    Stock_ = []

    for mover in topMovers:
        
        if index > 8:
            break
        elif index % 2 == 0:
            Stock_.append(STOCK())

            #print(index)

            Stock_[index2].name = mover.get_text().strip()
            Stock_[index2].own = False
            Stock_[index2].boughtPrice = 100000
            Stock_[index2].down = 0
            Stock_[index2].up = 0
            #Stock_[index2].basePrice = 0.0
            #Stock_[index2].oldPrice = 0.0
            #Stock_[index2].newPrice = 0.0

            #print(Stock_[index2].name)

            auto_stocklist.append(Stock_[index2])

            index2 += 1
            index += 1
        else:
            index += 1
    
    index = 0

    #print(len(auto_stocklist))
    #print("\n")

    while index < len(auto_stocklist):
        print(Stock_[index].name)
        index += 1

#fill_stocklist_auto()