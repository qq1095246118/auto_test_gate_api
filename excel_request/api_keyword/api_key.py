#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    这是接口关键字驱动类，用于提供自动化接口测试的关键字方法。
    主要实现常用的关键字内容，并定义好所有的参数内容即可
"""
import hashlib
import hmac
import json
from sys import _getframe
from time import time

import allure
import jsonpath
import requests

from common.api_method import get_user_key

headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}


def excel_gen_sign(key, secret, method, url, query_string, params=None):
    """
        请求加密方法封装
    """
    # if '?' in url:
    #     uro_list = url.split('?')
    #     query_string = uro_list[1]
    #     print(uro_list)
    t = time()
    m = hashlib.sha512()
    m.update((params or "").encode('utf-8'))
    hashed_payload = m.hexdigest()
    # s2 = '%s\n%s\n%s\n%s\n%s' % (method.upper(), url, query_string, hashed_payload, t)
    s = f'{method.upper()}\n{url}\n{query_string}\n{hashed_payload}\n{t}'
    sign = hmac.new(secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
    headers.update({'KEY': key, 'Timestamp': str(t), 'SIGN': sign})


class ApiKey:

    def __init__(self):
        self.excel_key = 'e5e53741af49828c96bc2b7eae102b2c'
        self.excel_secret = 'ca8facf4ff615ae2db1139d8660ce06af67eec8e70730cba88c6ad01048325dd'

    # get请求的封装：因为params可能存在无值的情况，存放默认None
    @allure.step("发送get请求")
    def get(self, path, params=None, **kwargs):
        url = f"{kwargs['server']}{path}"
        method = _getframe().f_code.co_name
        # 交易对手模块，支持多笔吃单
        if "user" in kwargs:
            data_key = get_user_key(kwargs['user'])
            if data_key is None:
                assert False, f"未找到{kwargs['user']}用户的key与secret_key 请检查输入用户名！！"
            # 加密headers，请求自动携带加密信息
            excel_gen_sign(data_key.get('key'), data_key.get('secret_key'), method, path.split('?')[0],
                           path.split('?')[1], str(params))
        else:
            print(url)
            excel_gen_sign(self.excel_key, self.excel_secret, method, path.split('?')[0], path.split('?')[1], params)
        result = requests.get(url, headers=headers, data=params, verify=False, timeout=(6.05, 180))
        try:
            res = result.json()
        except ValueError:
            return result
        if isinstance(result, bool):
            return result
        return res

    @allure.step("发送post请求")
    # post请求的封装：data也可能存在无值得情况，存放默认None
    def post(self, path, **kwargs):
        url = f"{kwargs['server']}{path}"
        print(kwargs)
        method = _getframe().f_code.co_name
        # 交易对手模块，支持多笔吃单
        if kwargs['user']:
            data_key = get_user_key(kwargs['user'])
            if data_key is None:
                assert False, f"未找到{kwargs['user']}用户的key与secret_key 请检查输入用户名！！"
            # 加密headers，请求自动携带加密信息
            excel_gen_sign(data_key.get('key'), data_key.get('secret_key'), method, path, "",
                           str(kwargs['json']))
        else:
            excel_gen_sign(self.excel_key, self.excel_secret, method, path, "", str(kwargs['json']))
        result = requests.post(url, data=str(kwargs['json']), headers=headers, verify=False, timeout=(6.05, 180))
        try:
            res = result.json()
        except ValueError:
            return result
        if isinstance(result, bool):
            return result
        return res

    @allure.step("获取返回结果字典值")
    # 基于jsonpath获取数据的关键字：用于提取所需要的内容
    def get_text(self, data, key):
        # jsonpath获取数据的表达式：成功则返回list，失败则返回false
        # loads是将json格式的内容转换为字典的格式
        # jsonpath接收的是dict类型的数据
        dict_data = json.loads(data)
        value = jsonpath.jsonpath(dict_data, '$..{0}'.format(key))
        return value[0]
