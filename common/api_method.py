# -*- coding:utf-8 -*-
"""
@FileName: api_method.py
@Desc    :   API底层封装
"""
import hashlib
import hmac
import json
import os
from time import time

import pandas as pd
import urllib3
import requests

# 禁用urllib3
from utility.public_variable import variable

urllib3.disable_warnings()

"""
    Get、Post方法请求封装，自动加密
"""

# 公用headers
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}


def get_user_key(user_name):
    """
        获取指定用户key信息
    """
    """
        读取user_info.xlsx表内key， secret_key
    """
    user_list = []
    # 根目录
    cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 运行文件目录
    xls_path = os.path.join(cur_path, 'testdata', 'xlsx', 'user_info.xlsx')
    # 读取Excel数据信息
    df = pd.DataFrame(pd.read_excel(io=xls_path, sheet_name="Sheet1"))
    # 根据行遍历数据
    for index, row in df.iterrows():
        data_dict = {'user_name': row.get('user_name'), 'key': row.get('key'), 'secret_key': row.get('secret_key')}
        user_list.append(data_dict)
    for data in user_list:
        if data.get("user_name") == user_name:
            return data


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
        print(url)
        result = requests.post(url, data=params, headers=headers, verify=False, timeout=(6.05, 180))
    return result


def delete(host, url):
    """delete method"""
    url = f'{host}/{url}'
    print(url)
    result = requests.delete(url, headers=headers, verify=False, timeout=(6.05, 180))
    return result
