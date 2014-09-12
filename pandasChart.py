# -*- coding: UTF-8 -*-
__author__ = 'dubu9'

from matplotlib import pyplot as plt
from pandas.io.data import DataReader

# yahoo 2014 주가 그래프
aapl = DataReader('AAPL', 'yahoo', start='2014')
aapl['Adj Close'].plot()
plt.show()

# 주가변화율
returns = aapl['Adj Close'].pct_change()
returns.plot()
plt.show()


