# -*- coding:utf-8 -*-
"""
@FileName: api_method.py
@Desc    :   API底层封装
"""
import hashlib
import hmac
import json
from sys import _getframe
from time import time

import urllib3
import requests

# 禁用urllib3

urllib3.disable_warnings()

"""
    Get、Post方法请求封装，自动加密
"""

# 公用headers
headers = {'Access-Token': 'application/json', "Content-Type": 'application/json'}


def gen_sign(key, secret, method, url, params=None, body=None):
    """
        请求加密方法封装
    """
    if params is None:
        params = ''
    s = f'{method.upper()}\n{url}\n{params}\n{body}\n{time()}'
    sign = hmac.new(secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
    sign_headers = {'KEY': key, 'Timestamp': str(time()), 'SIGN': sign}
    headers.update(sign_headers)


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
    print(url)
    if file_name:
        files = {'file': (file_name, open(file_root_path, 'rb'))}
        result = requests.post(url, json=params, headers=headers, files=files, verify=False,
                               timeout=(6.05, 180))
    else:
        result = requests.post(url, json=params, headers=headers, verify=False, timeout=(6.05, 180))
    return result


def delete(host, url):
    """delete method"""
    url = f'{host}/{url}'
    result = requests.delete(url, headers=headers, verify=False, timeout=(6.05, 180))
    return result


