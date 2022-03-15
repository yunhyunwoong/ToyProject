import requests

url =  "https://api.upbit.com/v1/candles/days?market=KRW-BTT&count=1"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

print(response.json())