# -*- coding: utf-8 -*-
"""
@File    :   excel_user_key.py
@Time    :   2022/11/30/19:15
@Author  :   Yan-QC
@Desc    :   交易对手处理模块
"""

import os
import pandas as pd
import pytest

from utility.public_variable import variable

# cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # 运行文件目录
# xls_path = os.path.join(cur_path, 'testdata', 'xlsx', 'user_info.xlsx')

#
# def user_method():
#     """
#         读取user_info.xlsx表内key， secret_key
#     """
#     data_list = []
#     # 读取Excel数据信息
#     df = pd.DataFrame(pd.read_excel(io=xls_path, sheet_name="Sheet1"))
#     # 根据行遍历数据
#     for index, row in df.iterrows():
#         data_dict = {'user_name': row.get('user_name'), 'key': row.get('key'), 'secret_key': row.get('secret_key')}
#         data_list.append(data_dict)
#     return data_list


# def get_user_key(user_name):
#     """
#         获取指定用户key信息
#     """
#     for data in variable.userdata:
#         if data.get("user_name") == user_name:
#             return data


if __name__ == '__main__':
    # test1 = user_method()
    # test2 = get_user_key('script')
    print("####" * 20)
    # print(test2)
