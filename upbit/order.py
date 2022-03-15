import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

access_key = "UwG4jnayrNYlwCxRnWPezAXE2NV5LHsBDFtx0Rpi"
secret_key = "v9x120nLEzGbUaDozbZ4RputZWDCPSwDK44wIU4M"
server_url = "https://api.upbit.com/v1/orders"

query = {
    'market': 'KRW-BTC',
    'side': 'bid', # 주문종류(side) =  매수 : bid, 매도 : ask
    'volume': '50', # 주문개수
    'price': '100.0', # 주문금액
    'ord_type': 'limit', # 주문타입(지정가주문)
}
query_string = urlencode(query).encode()

m = hashlib.sha512()
m.update(query_string)
query_hash = m.hexdigest()

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
    'query_hash': query_hash,
    'query_hash_alg': 'SHA512',
}

jwt_token = jwt.encode(payload, secret_key)
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.post(server_url, params=query, headers=headers)


data = res.json()
print(data)