#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:49:08 2021

@author: tatianasorroche
"""
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats
import math
import numpy as np

yafi = yf.download('AAPL', period='12mo')

"""
all_closed = yafi['Close'].to_numpy()
total_average = list()

while True:
    if len(all_closed) >= 5:
        lastClose = all_closed[-5:]
        average = np.mean(lastClose)
        total_average.append(average)
        all_closed = np.delete(all_closed, -1)
    else:
        break
"""

media30 = pd.DataFrame()
media30['Close'] = yafi['Close'].rolling(window = 30).mean()

plt.figure(figsize = (10, 5))
plt.plot(yafi['Close'], label = 'Apple Stock')
plt.plot(media30, label = 'Media móvil 30')
plt.title('Acciones de Apple - Precio de sus acciones desde los últimos 12 meses')
plt.xlabel('últimos 12 meses')
plt.ylabel('Precio de cierre ($)')
plt.legend(loc = 'upper left')
plt.show()