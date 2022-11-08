# -*- coding:utf-8 -*-
"""
@FileName: api_method.py
@Desc    :   API底层封装
"""
import urllib3
import requests

# 禁用urllib3

urllib3.disable_warnings()

"""
    Get、Post方法请求封装，携带token，sign信息
    注：使用此post/get替换json中的token，sign信息为前置登陆信息，
    若需独立项目请在config文件中独立配置账户信息
"""


def get(host, url, token):
    """get method"""
    url = f'{host}/{url}'
    headers = {'Access-Token': token, "Content-Type": 'application/json;charset=UTF-8',
               'Pragma': 'no-cache', 'Proxy-Connection': 'keep-alive'}
    res = requests.get(url, headers=headers, verify=False, timeout=(6.05, 180))
    return res


def post(host, url, token, sign, params, file_root_path=None, file_name=None):
    """post method"""
    url = f"{host}{url}"
    headers = {'Access-Token': token, "Content-Type": 'application/json;charset=UTF-8',
               'Pragma': 'no-cache', 'Proxy-Connection': 'keep-alive'}
    # 请求body中携带token，取默认赋值
    if 'token' in str(params):
        params["context"]['token'] = token
        params['sign'] = sign
    if file_name:
        files = {'file': (file_name, open(file_root_path, 'rb'))}
        res = requests.post(url, json=params, headers=headers, files=files, verify=False,
                            timeout=(6.05, 180))
    else:
        res = requests.post(url, json=params, headers=headers, verify=False, timeout=(6.05, 180))
    return res
