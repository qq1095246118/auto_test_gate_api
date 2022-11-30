# -*- coding: utf-8 -*-
"""
@File    :   test_case2.py
@Time    :   2022/12/1/0:26
@Author  :   Yan-QC
@Desc    :   
"""

import requests
import time
import hashlib
import hmac


def gen_sign(method, url, query_string=None, payload_string=None):
    key = 'b2b9edeb52b3c34b865b645ff19a711f'  # api_key
    secret = '58badce577556909a1b7c6903542995b87bbfbbb68988da126920f9a11797d76'  # api_secret

    t = time.time()
    m = hashlib.sha512()
    m.update((payload_string or "").encode('utf-8'))
    hashed_payload = m.hexdigest()
    s = '%s\n%s\n%s\n%s\n%s' % (method, url, query_string or "", hashed_payload, t)
    sign = hmac.new(secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
    return {'KEY': key, 'Timestamp': str(t), 'SIGN': sign}


if __name__ == "__main__":
    host = "http://47.110.62.160:8201"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    url = '/spot/orders'
    query_param = ''
    body = '{"text": "t-166982569", "currency_pair": "ETH_USDT", "type": "limit", "account": "spot", "side": "buy", "iceberg": "0", "amount": "1", "price": "3540", "time_in_force": "gtc", "auto_borrow": false}'
    # `gen_sign` 的实现参考认证一章
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
