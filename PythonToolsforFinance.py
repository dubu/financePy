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



# 1. requests HTML 문서 받기
import requests
import json
from BeautifulSoup import BeautifulSoup

url = 'http://www.krx.co.kr/por_kor/popup/JHPKOR13008.jsp'
r = requests.post(url, data={'mkt_typ':'S', 'market_gubun': 'allVal'})

# 2. BeautifulSoup HTML 문서 파싱
soup = BeautifulSoup(r.text)
table = soup.find('table', {'id':'tbl1'})
trs = table.findAll('tr')

# 3. 데이터 추출하여 리스트로 구성
stock_list = []

for tr in trs[1:]:
    stock = {}
    cols = tr.findAll('td')
    stock['code'] = cols[0].text[1:]
    stock['name'] = cols[1].text.replace(";", "")
    stock['full_code'] = cols[2].text
    stock_list.append(stock)

# 4. list를 JSON 포맷으로 저장
j = json.dumps(stock_list)
with open('data/krx_symbols.json', 'w') as f:
    f.write(j)

fn = 'data/krx_symbols.json'
with open(fn, 'r') as f:
    stock_list = json.load(f)

#저장내용확인
# len(stock_list)
for s in stock_list[:10]:
    print s['full_code'], s['code'][1:], s['name']