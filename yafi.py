import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats
import math
import numpy as np

class YaFi:
    def __init__(self, ticker): #add argument of operation and period
        self.df = yf.download(ticker, period='6mo')
        self.total_average = list()

    def getClose(self):
        allClose = self.df.Close
        # We convert that data into a numpy array and iterate it so we can get
        # all the last 5 closes and its mean.
        arr = allClose.to_numpy()
        while True:
            if len(arr) >= 5:
                lastClose = arr[-5:]
                average = np.mean(lastClose)
                self.total_average.append(average)
                arr = np.delete(arr, -1)
            else:
                break
        print(self.total_average)



"""
# We use yfinance module to download the data
df = yf.download('SLB', period='6mo')

allClose = df.Close

# We convert that data into a numpy array and iterate it so we can get
# all the last 5 closes and its mean.
arr = allClose.to_numpy()
total_average = list()
while True:
    if len(arr) >= 5:
        lastClose = arr[-5:]
        average = np.mean(lastClose)
        total_average.append(average)
        arr = np.delete(arr, -1)
    else:
        break
"""



