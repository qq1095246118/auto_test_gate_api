# -*- coding: utf-8 -*-
"""
@File    :   api_key.py
@Time    :   2022/11/30/21:26
@Author  :   Yan-QC
@Desc    :   
"""

import json

import allure
import jsonpath
import requests


class ApiKey:

    # get请求的封装：因为params可能存在无值的情况，存放默认None
    @allure.step("发送get请求")
    def get(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    @allure.step("发送post请求")
    # post请求的封装：data也可能存在无值得情况，存放默认None
    def post(self, url, data=None, **kwargs):
        return requests.post(url=url, data=data, **kwargs)

    @allure.step("获取返回结果字典值")
    # 基于jsonpath获取数据的关键字：用于提取所需要的内容
    def get_text(self, data, key):
        # jsonpath获取数据的表达式：成功则返回list，失败则返回false
        # loads是将json格式的内容转换为字典的格式
        # jsonpath接收的是dict类型的数据
        dict_data = json.loads(data)
        value = jsonpath.jsonpath(dict_data, '$..{0}'.format(key))
        return value[0]
