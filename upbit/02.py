# 사용자 전체 계좌 조회
import config.logging_settings
import os
import jwt # PyJWT
import uuid # uuid
import hashlib # hashlib 
from urllib.parse import urlencode

import requests # requests

access_key = "UwG4jnayrNYlwCxRnWPezAXE2NV5LHsBDFtx0Rpi"
secret_key = "v9x120nLEzGbUaDozbZ4RputZWDCPSwDK44wIU4M"

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get("https://api.upbit.com/v1/accounts", headers=headers)

print(res.json())