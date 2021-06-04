import requests
from bs4 import BeautifulSoup

def get_per(code):
    url = "http://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("#_per")
    tag = tags[0]
    return float(tag.text)                              # 결과 값이 소수기 때문에 float 을 사용

def get_dividend(code):
    url = "http://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("#_dvr")                         # 배당수익률의 id 값이 _dvr
    tag = tags[0]
    return float(tag.text)                              # 결과 값이 소수기 때문에 float 을 사용

print(get_per("000660"))                                # 000660(sk 하이닉스) 의 per 출력
print(get_dividend("000660"))                           # 000660(sk 하이닉스) 의 배당 수익률 출력