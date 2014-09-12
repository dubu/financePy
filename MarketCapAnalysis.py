# -*- coding: UTF-8 -*-
from numpy.ma import arange

__author__ = 'dubu9'

# 1. from goole docs csv

# import pandas as pd
# import requests
# from StringIO import StringIO
# # 2013년 시가총액
# url = "https://docs.google.com/spreadsheet/ccc?" +
# "key=0Auils-M1uCmvdGFSZFVual9aYVp1UE9oWnZocE5aQVE" +
# "&output=csv"
# url = "http://goo.gl/WfQnX0" # csv 로 다운로드
# r = requests.get(url)
# data = r.content

# 2. from xls file
import pandas as pd
import numpy as np

# fn = 'data/Data_140912.xls' # krx 주식 시가총액 엑셀다운로드 http://www.krx.co.kr/m2/m2_4/m2_4_4/JHPKOR02004_04.jsp
# xl = pd.ExcelFile(fn,dtype={'code':np.str})
# print(xl.sheet_names)
# df = xl.parse("Sheet1")
# print(df.head())

fn = 'data/marcap-2013.csv' # krx 주식 시가총액 엑셀다운로드 http://www.krx.co.kr/m2/m2_4/m2_4_4/JHPKOR02004_04.jsp
df = pd.read_csv(fn, dtype={'code':np.str})

df2 = df[['code', 'name', 'marcap', 'sector']]
print(df2.head(10))

sector_counts = df2['sector'].value_counts()

print sector_counts.count() # 업종수
print sector_counts.index # 업종항목
print sector_counts.values # 업종내 기업수

#식별되는 업종의 수: 80개
#자동차부품, 화학, 기계, 제약 종목이 각각 120, 109, 98, 95개

from itertools import cycle

colors_list = [ "#C41F3B", "#FF7D0A", "#ABD473", "#69CCF0", "#00FF96", "#F58CBA", "#FFFFFF", "#FFF569", "#0070DE", "#9482C9", "#C79C6E" ]
color = cycle(colors_list)

print next(color)
print next(color)
print next(color)

# 업종분포차트
import matplotlib.pylab as plt
import matplotlib.font_manager as fm
fontprop = fm.FontProperties(fname="fonts/malgun.ttf")

top20 = sector_counts[0:20]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title(u'업종분포', fontproperties=fontprop)
pos = arange(20)
pos = pos[::-1] # reverse pos list
plt.yticks(pos, [x.decode('utf8') for x in top20.index], fontproperties=fontprop)
plt.barh(pos, top20.values, align='center', color=colors_list, alpha=0.7)
# plt.show()

df_semi = df[df['sector']=='소프트웨어']
print(df_semi.head(10))

#시가총액 합산
from pandas.tools.pivot import pivot_table
ttable = df[['sector', 'marcap']]
piv = pivot_table(ttable, values='marcap', rows=['sector'], aggfunc=np.sum)
sector_marcap = piv.copy()
sector_marcap.sort(ascending=False)
print(sector_marcap[:10])

#업종별 시가총액 차트
import matplotlib.pylab as plt
import matplotlib.font_manager as fm
fontprop = fm.FontProperties(fname="fonts/malgun.ttf")

top20 = sector_marcap[0:20]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title(u'업종별 시가총액', fontproperties=fontprop)
pos = arange(20)
pos = pos[::-1] # reverse pos list
plt.yticks(pos, [x.decode('utf8') for x in top20.index], fontproperties=fontprop)
plt.barh(pos, top20.values, align='center', color=colors_list, alpha=0.7)
# plt.show()

#업종별 시가총액 비중
sector_marcap_pct = sector_marcap / sector_marcap.sum()
print(sector_marcap_pct[:10])

print sector_counts.index[:10]
print sector_counts.values[:10]

print sector_marcap.index[:10]
print sector_marcap.values[:10]

#시가총액 비중 차트(파이)
import matplotlib.font_manager as fm
fontprop = fm.FontProperties(fname="fonts/malgun.ttf")

fig, axes = plt.subplots(nrows=1, ncols=2)
fig.set_size_inches(18, 8)


# 첫번쨰 파이 차트 (업종내 종목수)
sec_stock_top = sector_counts[:10]
labels = sec_stock_top.index.astype(str) + '\n' + sec_stock_top.values.astype(str)
ulabels = [x.decode('utf-8') for x in labels]

axes[0].set_title(u"2013 업종내 종목수 TOP 10", fontproperties=fontprop)
patches, texts = axes[0].pie(sec_stock_top, labels=ulabels, startangle=90, colors=colors_list)
plt.setp(texts, fontproperties=fontprop)

# 두번쨰 파이 차트 (업종별 시가총액)
sec_mar_top = sector_marcap[:10]
labels = sec_mar_top.index.astype(str) + '\n' + sec_mar_top.values.astype(str)
ulabels = [x.decode('utf-8') for x in labels]

axes[1].set_title(u"2013 업종별 시가총액 TOP 10", fontproperties=fontprop)
patches, texts = axes[1].pie(sec_mar_top, labels=ulabels, startangle=90, colors=colors_list)
plt.setp(texts, fontproperties=fontprop)

plt.show()