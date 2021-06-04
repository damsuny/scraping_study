import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=000660"     # 데이터를 가져올 url
html = requests.get(url).text                                   # 텍스트를 가져 옵니다.

soup = BeautifulSoup(html, 'html5lib')                          # html 객체를 html5lib 모듈을 사용하여 파싱합니다.
tags = soup.select("#_per")                                     # 페이지에서 id가 _per 를 가져옵니다.
tag = tags[0]                                                   # tag 에 데이터를 넣어줍니다.
print(tag.text)                                                 # 텍스트 형식으로 되어 있는 데이터를 출력해줍니다.