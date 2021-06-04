import requests
from bs4 import BeautifulSoup

url = "http://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em")   # 요소 우클릭 > 검사 > 코드 요소 우클릭> copy > copy selector

for tag in tags:
    print(tag.text)