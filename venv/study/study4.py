import datetime

import requests

r= requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")

bitcoin = r.json()      # json 형태의 데이터를 딕셔너리로 변환
print(bitcoin)
# timestamp(최종 체결 시각), last(최종 체결 가격), bid(최우선 매수호가(매수 주문중 가장 높은 가격)), ask(최우선 매도호가(매도 주문중 가장 낮은가격))
# low(최근 24시간 저가), high(최근 24시간 고가), volume(거래량)
print(type(bitcoin))                # bitcoin 의 타입 출력
timestamp = bitcoin['timestamp']         # 최종 체결 시각
date = datetime.datetime.fromtimestamp(timestamp/1000)
print(date)