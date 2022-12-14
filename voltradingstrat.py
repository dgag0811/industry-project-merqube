# -*- coding: utf-8 -*-
"""VolTradingStrat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lcWiyCfgj1Y-nGdb7mXyO2RGnnLJ-Udx
"""

# Importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Creating high volatility noise
hv_noise = np.random.normal(0, 1, 250)
# Creating low volatility noise
lv_noise = np.random.normal(0, 0.1, 250)

plt.plot(hv_noise, color = 'red', linewidth = 1.5, label = 'High Volatility')
plt.plot(lv_noise, color = 'green', linewidth = 1.5, label = 'Low Volatility')
plt.axhline(y = 0, color = 'black', linewidth = 1)
plt.grid()
plt.legend()

