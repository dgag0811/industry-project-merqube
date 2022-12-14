# -*- coding: utf-8 -*-
"""HistoricalVolExample_usingS&Pdata.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YfDJBGmbR1Gym5u_9wMpRl1_iituJc6l
"""

pip install yfinance

import numpy as np
import pandas as pd
import yfinance as yf

# package to download data, from pandas 
import pandas_datareader.data as web

# packages to work with time and dates

import datetime as dt
import matplotlib.dates as mdates

# packages for visulization

import matplotlib.pyplot as plt
plt.style.use('ggplot')

start = dt.datetime(1926, 1, 1)   # Start date to download the data
end = dt.datetime(2022, 1, 1)     # End Date to downlaod the data

sp500 = yf.download('^GSPC', start=start, end=end)

sp500_yearly= sp500.resample('Y').ffill()                            # resample data to get data at the end of each year

sp500_yearly_returns  = sp500_yearly['Adj Close'].pct_change().dropna()*100     # find returns in percentage unit

plt.plot(sp500_yearly_returns)
plt.title("Plot of Yearly Return of S&P 500 Index")
plt.ylabel("Percentage (%)")

vol_sp500= np.std(sp500_yearly_returns)
print("Realized Volatility for S&P 500 index from time period 1926 to 2022 is:\n%.1f" % vol_sp500 )

