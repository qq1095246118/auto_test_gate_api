# -*- coding:utf-8 -*-
"""
@FileName: api_method.py
@Desc    :   API底层封装
"""
import hashlib
import hmac
import json
from time import time

import urllib3
import requests

# 禁用urllib3
urllib3.disable_warnings()

"""
    Get、Post方法请求封装，自动加密
"""

# 公用headers
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}


def gen_sign(key, secret, method, url, query_string, params=None):
    """
        请求加密方法封装
    """
    t = time()
    m = hashlib.sha512()
    m.update((params or "").encode('utf-8'))
    hashed_payload = m.hexdigest()
    # s2 = '%s\n%s\n%s\n%s\n%s' % (method.upper(), url, query_string, hashed_payload, t)
    s = f'{method.upper()}\n{url}\n{query_string}\n{hashed_payload}\n{t}'
    sign = hmac.new(secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
    headers.update({'KEY': key, 'Timestamp': str(t), 'SIGN': sign})


def get(host, url):
    """get method"""
    url = f'{host}/{url}'
    print(url)
    result = requests.get(url, headers=headers, verify=False, timeout=(6.05, 180))
    return result


def post(host, url, params, file_root_path=None, file_name=None):
    """
        post method
            file_root_path：文件上传路径
            file_name：文件名称
    """
    url = f"{host}{url}"
    if file_name:
        files = {'file': (file_name, open(file_root_path, 'rb'))}
        result = requests.post(url, data=params, headers=headers, files=files, verify=False,
                               timeout=(6.05, 180))
    else:
        result = requests.post(url, data=params, headers=headers, verify=False, timeout=(6.05, 180))
    return result


def delete(host, url):
    """delete method"""
    url = f'{host}/{url}'
    result = requests.delete(url, headers=headers, verify=False, timeout=(6.05, 180))
    return result
