from Config_Functions import get_account, create_order, sell_order, view_orders
from Stocklist import get_URL, addToWatchList, print_watchList
from Auto_Check import auto_check, price, autoTrade

cont = "0"
answer = ""
answer2 = ""

while(cont != "-1"):
    print("1-Review Account\n2-Edit Acount\n3-Run Auto-Pilot\n4-Cancel Program")
    answer = input("What would you like to do:  ")
    print("\n\n")

    if answer == "1":
        print("1-Account info\n2-View Current Orders\n3-View Watchlist")
        answer2 = input("What would you like to do:  ")

        if answer2 == "1":
            print("\n\n")
            for content in get_account():
                contentValue = get_account().get(content)
                print(content + " - " + str(contentValue))
            print("\n\n")
        
        elif answer2 == "2":
            print("\n\n" + str(view_orders()) + "\n\n")

        elif answer2 == "3":
            print("\n\n")
            print_watchList()
            print("\n\n")
        
        elif answer2 == "-1":
            cont == "1"
    
    elif answer == "2":
        print("1-Buy a Stock\n2-Sell a Stock\n3-Add stock to watchlist")
        answer2 = input("What would you like to do:  ")

        if answer2 == "1":
            sm = input("Company: ")
            qn = input("Quantity: ")
            sd = "buy"
            tp = input("Type of market(market): ")
            tif = input("Day vs gtc: ")

            create_order(sm, qn, sd, tp, tif)
        
        elif answer2 == "2":
            sm = input("Company: ")
            qn = input("Quantity: ")
            sd = "sell"
            tp = input("Type of market(market): ")
            tif = input("Day vs gtc: ")

            sell_order(sm, qn, sd, tp, tif)

        elif answer2 == "3":
            print("\n\n")
            addToWatchList()
            print("Added\n\n")

        elif answer2 == "-1":
            cont == "1"
    
    elif answer == "3":
        autoTrade()

    elif answer == "-1":
        exit()