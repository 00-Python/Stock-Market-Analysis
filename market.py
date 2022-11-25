import os
import sys
import datetime
from stocksymbol import StockSymbol
from plotting_system.system import Trading_plotter
import pandas_datareader as pdr

brand_words ='''This is a simple program to get stock data from different online sources and simple plot or candlestick plot the data and/or export it to csv or excel or png. 


Currently Suppoted Data Sources: Yahoo Finance = yahoo'''

print()
print(brand_words)
print()
try:
    try:
        with open("apis/stock_symbol_api.txt", "r", encoding="utf-8") as f:
            stock_symbol_api = f.read()
        if stock_symbol_api == "": raise FileNotFoundError
        ss = StockSymbol(stock_symbol_api)
    except FileNotFoundError:
        print()
        print("WARNING")
        print("----------------")
        print("No API key found for StockSymbol API. Please get one from https://stock-symbol.herokuapp.com/ and save it in apis/stock_symbol_api.txt\nOtherwise you will not be able to get Market List or Stock Symbol Lists.")
        print()
        # change text to red in terminal
        
    # display the list in notepad for easy copy and paste
    while True:
        date = datetime.datetime.now()

        open_market = input("Open markets list? (y/n): ")

        if open_market == "y":
            try:
                market_list = ss.market_list
                with open("markets.txt", "w") as f:
                    for market in market_list:
                        # get market and abbreviation
                        market_name = market["market"]
                        abbreviation = market["abbreviation"]
                        #convert to string
                        market_name = str(market_name)
                        abbreviation = str(abbreviation)
                        f.write(market_name + " - " + abbreviation + "\n")
                os.startfile("markets.txt")
            except:
                print("No API key found for StockSymbol API. Please get one from https://stock-symbol.herokuapp.com/ and save it in apis/stock_symbol_api.txt\nOtherwise you will not be able to get Market List or Stock Symbol Lists.")
            

        open_list = input("Open list of stock symbols (y/n)? ").lower()

        if open_list == "y":
            market = input("Enter market: ").upper()
            symbol_list = ss.get_symbol_list(market=market)
            with open("symbol_list.txt", "w") as f:
                for symbol in symbol_list:
                    # get symbol and name
                    symbol_name = symbol["symbol"]
                    long_name = symbol["longName"]
                    # convert to string
                    symbol_name = str(symbol_name)
                    long_name = str(long_name)
                    f.write(symbol_name + " - " + long_name + "\n")
            os.startfile("symbol_list.txt")
            
        data_source = input("Enter data source (yahoo, google, iex...): ").lower()

        stock_symbol = input("Enter the stock symbol: ")
        # convet upper
        stock_symbol = stock_symbol.upper()

        inp = input(" 1. X days ago \n 2. X weeks ago \n 3. X years ago \n 4. Custom Dates\n Enter the number: ")

        if inp == "1":
            inp = input("Enter the number of days: ")
            inp = int(inp)
            start=date - datetime.timedelta(days=inp) 
            end=date
        elif inp == "2":
            inp = input("Enter the number of weeks: ")
            inp = int(inp) * 7
            start=date - datetime.timedelta(days=inp)
            end=date
        elif inp == "3":
            inp = input("Enter the number of years: ")
            inp = int(inp) * 365
            start=date - datetime.timedelta(days=inp)
            end=date
        elif inp == "4":
            start = input("Enter the start date (YYYY-MM-DD): ")
            end = input("Enter the end date (YYYY-MM-DD): ")
        else:
            # delete the symbol list
            os.remove("symbol_list.txt")
            os.remove("markets.txt")
            print("Invalid timeframe")
            sys.exit()

        data = pdr.DataReader(stock_symbol, data_source, start, end)

        plotter = Trading_plotter(data, stock_symbol)

        try:
            while True:
                os.system("cls")
                # ask the user what they want to do
                inp = input("""

What do you want to do?

1. Print Data to Console
2. Make a Candlestick Plot 
3. Make a linear plot
4. Make CSV File 
5. Make xlsx file (Excel)
6. Back To Market & Stock Selection Menu
Exit

(You can save plots as png by clicking the save button on the visualisation window toolbar)


Enter the number or exit: """).lower()

                # if input is not a letter
                if inp.isalpha():
                    # if input is exit
                    if inp == "exit":
                        try:
                            # delete the symbol list
                            os.remove("symbol_list.txt")
                            os.remove("markets.txt")
                        except FileNotFoundError:
                            pass
                        print("Exiting...")
                        sys.exit()
                    else:
                        print("Invalid input")
                        continue

                # if input is a number
                elif inp.isnumeric():
                    # if input is 1
                    if inp == "1":
                        os.system("cls")
                        print(data)
                        input("Press enter to continue...")
                        continue
                    # if input is 2
                    elif inp == "2":
                        plotter.candlestick_plot()
                        continue
                    # if input is 3
                    elif inp == "3":
                        plotter.make_plot()
                        continue
                    # if input is 4
                    elif inp == "4":
                        plotter.export_data_csv()
                        input("Press enter to continue...")
                        continue
                    # if input is 5
                    elif inp == "5":
                        plotter.export_data_excel()
                        input("Press enter to continue...")
                        continue
                    # if input is 6
                    elif inp == "6":
                        break
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("Invalid input")
                    continue

        except KeyboardInterrupt:
            # delete the file
            try:
                os.remove("symbol_list.txt")
                os.remove("markets.txt")
            except:
                pass
            print("Back to the main menu")
            print()
            continue
except KeyboardInterrupt:
    try:
        # delete the file
        os.remove("symbol_list.txt")
        os.remove("markets.txt")
    except:
        pass
    print("Exit")
    sys.exit()