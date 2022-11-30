# -*- coding:utf-8 -*-
"""
@FileName: data_helper.py
@Desc    :   文件处理模块
"""
import json

import pandas as pd


def read_file(filepath):
    """读取json文件"""
    with open(filepath, 'r', encoding='UTF-8') as file:
        content = file.read()
    return json.loads(content)

# def read_excel_file(file_path, sheet_name):
#     df = pd.DataFrame(pd.read_excel(io=file_path, sheet_name=sheet_name))
#     for index, row in df.iterrows():


