import pandas as pd
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

# "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
url = 'https://finance.naver.com/item/sise_day.nhn?code=133690&page=1'
# with urlopen(url) as doc:
with requests.get(url, headers={'User-agent': 'Mozilla/5.0'}) as doc:
    html = BeautifulSoup(doc.text, 'lxml')
    print(html)
    pgrr = html.find('td', class_='pgRR')
    s = str(pgrr.a['href']).split('=')
    last_page = s[-1]

df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=133690'
for page in range(1, int(last_page) + 1):
    page_url = '{}&page={}'.format(sise_url, page)

    df = df.append(pd.read_html(requests.get(page_url, headers={'User-agent': 'Mozilla/5.0'}).text)[0])
    df = df.append(pd.read_html(page_url, header=0)[0])
#
# df = df.dropna()
# df = df.iloc[0:30]
# df = df.sort_values(by='날짜')
#
# plt.title('나스닥 100 (close)')
# plt.xticks(rotation=45)
# plt.plot(df['날짜'], df['종가'], 'co-')
# plt.grid(color='gray', linestyle='--')
# plt.show()
