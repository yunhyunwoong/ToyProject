# REST API

import requests

url = "https://api.upbit.com/v1/market/all"
resp = requests.get(url)
data = resp.json() # 파이썬의 기본데이터 타입으로 변경
print(len(data))