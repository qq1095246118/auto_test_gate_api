# -*- coding:utf-8 -*-
"""
@FileName: data_helper.py
@Desc    :   文件处理模块
"""
import json


def read_file(filepath):
    """读取json文件"""
    with open(filepath, 'r', encoding='UTF-8') as file:
        content = file.read()
    return json.loads(content)
