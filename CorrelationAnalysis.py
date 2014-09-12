# -*- coding: UTF-8 -*-
__author__ = 'dubu9'

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pandas.io.data import DataReader

top10_codes = [
    '005930.KS','005380.KS','012330.KS','005490.KS','000660.KS',
    '035420.KS','005935.KS','000270.KS','055550.KS','015760.KS' ]

top5_codes = [
    '005930.KS','005380.KS','012330.KS','005490.KS','000660.KS' ]


start = datetime(2014, 1, 1)
end  = datetime(2014, 12, 31)

df = DataReader(top10_codes, 'yahoo', start=start, end=end)
df = df['Adj Close']

print(df.head())

df = df[top10_codes]
# df = df[top5_codes]
# print(df.head())

code_names = {
    '005930.KS':'Samsung Elec', '005380.KS':'Hyundai Motor',
    '012330.KS':'Hyundai Mobis', '005490.KS':'POSCO',
    '000660.KS':'SK Hynix','035420.KS':'Naver',
    '005935.KS':'Samsung Elec(Prep)', '000270.KS':'Kia Motor',
    '055550.KS':'Shinhan', '015760.KS':'Korea Elc Pwr' }

df = df.rename(columns=code_names)

# print(df.head())

changes = df.pct_change()
print(changes.head())

# plt.scatter(changes['Hyundai Motor'], changes['Hyundai Mobis'])
# plt.xlabel('Hyundai Motor')
# plt.ylabel('Hyundai Mobis')

# plt.show()

##상위 10개 종목 상관관계 차트
# df = DataReader(top10_codes, 'yahoo', start=start, end=end)
# df = df['Adj Close']
# df = df.rename(columns=code_names)
#
# changes = df.pct_change()
# pd.scatter_matrix(changes, diagonal='kde', figsize=(16, 16));
# plt.show()

## 온도차트
# corr = changes.corr()
#
# plt.figure(figsize=(14,8))
# plt.imshow(corr, cmap='hot', interpolation='none')
# plt.colorbar()
# plt.xticks(range(len(corr)), corr.columns, rotation=90)
# plt.yticks(range(len(corr)), corr.columns)
# plt.show()
#

##  KOSPI 와 종목간 상관계수
# code_names = { '^KS11':'KOSPI',
#                '005930.KS':'Samsung Elec', '005380.KS':'Hyundai Motor',
#                '012330.KS':'Hyundai Mobis', '005490.KS':'POSCO',
#                '000660.KS':'SK Hynix','035420.KS':'Naver',
#                '005935.KS':'Samsung Elec(Prep)', '000270.KS':'Kia Motor',
#                '055550.KS':'Shinhan', '015760.KS':'Korea Elc Pwr' }

code_names = { '^KS11':'KOSPI',
               '005930.KS':'Samsung Elec',
               '005380.KS':'Hyundai Motor',
               '012330.KS':'Hyundai Mobis',
               '005490.KS':'POSCO',
               '000660.KS':'SK Hynix',
               '035420.KS':'Naver',
               '005935.KS':'Samsung Elec(Prep)',
               '000270.KS':'Kia Motor',
               '055550.KS':'Shinhan',
               '015760.KS':'Korea Elc Pwr' }

df = DataReader(code_names.keys(), 'yahoo',
                start='2014-01-01', end='2014-12-31')
df = df['Adj Close']
df = df.rename(columns=code_names)

changes = df.pct_change()
chg_corr = changes.corr()
print(chg_corr)

##KOSPI 와 다른 종목간 상관계수
ser = chg_corr['KOSPI']
ser_ord = ser.order(ascending=False)
print(ser_ord[1:])

## 수익과 위험
plt.figure(figsize=(16,8))
plt.scatter(changes.mean(), changes.std())
plt.xlabel('returns')
plt.ylabel('risk')

for label, x, y in zip(changes.columns, changes.mean(), changes.std()):
    plt.annotate( label,xy=(x, y), xytext=(30, -30),
                  textcoords = 'offset points', ha = 'right', va = 'bottom',
                  bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
                  arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

plt.show()

## kospi 가 진리임.