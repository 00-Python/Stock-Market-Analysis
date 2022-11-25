# import pandas datareader as pdr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import sys
# import talib

import datetime as dt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

class Trading_plotter:
    # initialize the class
    def __init__(self, data, stock):
        # set the stock name
        self.stock = stock
        # get the data
        self.data = data
        # get the close price
        self.close = self.data["Close"]
        # get the high price
        self.high = self.data["High"]
        # get the low price
        self.low = self.data["Low"]
        # get the open price
        self.open = self.data["Open"]
        # get the volume
        self.volume = self.data["Volume"]
        # get the date
        self.date = self.data.index

    # candlestick plot
    def candlestick_plot(self):
        pd.options.mode.chained_assignment = None  # default='warn'
        # Reorder the 4 crucial columns
        self.df = self.data[['Open', 'High', 'Low', 'Close']]

        # Reset the index and convert date into float
        self.df.reset_index(inplace=True)
        self.df['Date'] = self.df['Date'].map(mdates.date2num)

        # Define a new subplot
        ax = plt.subplot()
        ax.grid(True)

        # Plot the candlestick chart and put date on x-Axis
        candlestick_ohlc(ax, self.df.values, width=5, colorup='g', colordown='r')
        ax.xaxis_date()
        ax.set_axisbelow(True)
        ax.set_title(self.stock + " Stock Price from " + str(self.date[0]) + " to " + str(self.date[-1]))
        # change title label size and color
        ax.title.set_size(12)
        ax.title.set_color("white")
        ax.set_facecolor('White')
        ax.figure.set_facecolor('#121212')
        ax.tick_params(axis='x', colors='White')
        ax.tick_params(axis='y', colors='white')
        # Turn on grid
        ax.xaxis_date()


        # Show plot
        plt.show()
        
    # save candlestick plot
    def save_candlestick_plot(self):
        pd.options.mode.chained_assignment = None
        # Reorder the 4 crucial columns
        self.df = self.data[['Open', 'High', 'Low', 'Close']]
        # Reset the index and convert date into float
        self.df.reset_index(inplace=True)
        self.df['Date'] = self.df['Date'].map(mdates.date2num)
        # Define a new subplot
        ax = plt.subplot()
        ax.grid(True)
        # Plot the candlestick chart and put date on x-Axis
        candlestick_ohlc(ax, self.df.values, width=5, colorup='g', colordown='r')
        ax.xaxis_date()
        ax.set_axisbelow(True)
        ax.set_title(self.stock + " Stock Price from " + str(self.date[0]) + " to " + str(self.date[-1]))
        # change title label size and color
        ax.title.set_size(12)
        ax.title.set_color("white")
        ax.set_facecolor('White')
        ax.figure.set_facecolor('#121212')
        ax.tick_params(axis='x', colors='White')
        ax.tick_params(axis='y', colors='white')
        # Turn on grid
        ax.xaxis_date()
        # check if there is a data folder if not create one
        if not os.path.exists("candlestick_plot"):
            os.makedirs("candlestick_plot")
        # check if there is a folder for the stock inside the data folder if not create one
        if not os.path.exists("candlestick_plot/" + self.stock):
            os.makedirs("candlestick_plot/" + self.stock)
        # save the plot with date
        plt.savefig("candlestick_plot/" + self.stock + "/" + self.stock + "_" + str(self.date[0]) + "_" + str(self.date[-1]) + ".png")
            

    # plot the data
    def make_plot(self):
        self.stock = self.stock

        # window size
        plt.figure(figsize=(9, 6))

        plt.grid(True)

        plt.plot(self.date, self.open, label="Open")
        plt.plot(self.date, self.high, label="High")
        plt.plot(self.date, self.low, label="Low")
        plt.plot(self.date, self.close, label="Close")
        plt.legend()
        # show the plot
        plt.suptitle(self.stock + " Stock Price from " + str(self.date[0]) + " to " + str(self.date[-1]))
        
        plt.show()

    # save plot
    def save_plot(self):
        self.stock = self.stock

        # window size
        plt.figure(figsize=(14, 11))
        plt.grid(True)

        plt.plot(self.date, self.open, label="Open")
        plt.plot(self.date, self.high, label="High")
        plt.plot(self.date, self.low, label="Low")
        plt.plot(self.date, self.close, label="Close")
        plt.legend()
        plt.suptitle(self.stock + " Stock Price from" + str(self.date[0]) + " to " + str(self.date[-1]))

        # chech if there is a plot folder if not create one
        if not os.path.exists("plots"):
            os.makedirs("plots")
        # chech if there is a folder for the stock inside the plots folder if not create one
        if not os.path.exists("plots/" + self.stock):
            os.makedirs("plots/" + self.stock)
        # crate a name for the file with the stock name and date and time
        file_name = "plots/" + self.stock + "/" + self.stock + "_" + str(dt.datetime.now().date()) + "_" + str(dt.datetime.now().time()).replace(":", "-") + ".png"
        # save the plot
        plt.savefig(file_name)

    # exoprt the data
    def export_data_csv(self):
        # check if there is a data folder if not create one
        if not os.path.exists("csv"):
            os.makedirs("csv")
        # check if there is a folder for the stock inside the data folder if not create one
        if not os.path.exists("csv/" + self.stock):
            os.makedirs("csv/" + self.stock)

        # crate a name for the file with the stock name and date and time
        file_name = "csv/" + self.stock + "/" + self.stock + "_" + str(dt.datetime.now().date()) + "_" + str(dt.datetime.now().time()).replace(":", "-") + ".csv"
        # export the data to csv
        self.data.to_csv(file_name)
        print("File Saved to " + file_name)
        

    # export the data to excel
    def export_data_excel(self):
        # check if there is a data folder if not create one
        if not os.path.exists("excel"):
            os.makedirs("excel")
        # check if there is a folder for the stock inside the data folder if not create one
        if not os.path.exists("excel/" + self.stock):
            os.makedirs("excel/" + self.stock)
        file_name = "excel/" + self.stock + "/" + self.stock + "_" + str(dt.datetime.now().date()) + "_" + str(dt.datetime.now().time()).replace(":", "-") + ".xlsx"
        # export the data to excel
        self.data.to_excel(file_name)
        # print Fiels Saved to the path 
        print("File Saved to " + file_name)

if __name__ == "__main__":
    pass