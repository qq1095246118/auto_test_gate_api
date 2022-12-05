#!/usr/bin/env python
# -*- coding: utf-8 -*-

# excel用例的读取与执行
import os
import time

import allure
import openpyxl

# 读取Excel
import pytest

from excel_request.api_keyword.api_key import ApiKey

# 获取项目根路径
from utility.public_variable import variable

cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 运行文件目录
xls_paths = os.path.join(cur_path, 'case', 'api_cases.xlsx')
excel = openpyxl.load_workbook(xls_paths)
sheet = excel['Sheet1']
ak = ApiKey()


# 读取excel内容，实现文件驱动自动化执行
def read_excel():
    tulpe_list = []
    # 逐行循环读取Excel数据
    for value in sheet.values:
        # 判断当前行第一列的值，是否是数字编号
        if type(value[0]) is int:
            # 将元祖装载进list
            tulpe_list.append(value)
    return tulpe_list


@pytest.mark.parametrize('case', read_excel())
def test_case_1(case):
    # 动态生成标题
    allure.dynamic.title(case[2])
    # 判断Json与用户参数是否为空
    if case[5] is None and case[8] is None:
        if 'orderid' in case[3]:
            dict_data = {'server': case[2], "path": case[3].replace("orderid", variable.orderid), }
        else:
            dict_data = {'server': case[2], "path": case[3]}
    elif case[5] is not None and case[8] is None:
        if 'orderid' in case[3]:
            # 拼接路径，data请求参数，用户信息
            dict_data = {'server': case[2], "path": case[3].replace("orderid", variable.orderid), 'json': str(case[5])}
        else:
            dict_data = {'server': case[2], "path": case[3], 'json': str(case[5])}
    else:
        if 'orderid' in case[3]:
            dict_data = {'server': case[2], "path": case[3].replace("orderid", variable.orderid),
                         'json': str(case[5]), 'user': case[8]}
        else:
            dict_data = {'server': case[2], "path": case[3], 'json': str(case[5]), 'user': case[8]}
    time.sleep(1)
    # 模拟请求，将请求参数反射至封装请求内
    res = getattr(ak, case[4])(**dict_data)
    # 将结果写入Excel
    sheet.cell(row=int(case[0]) + 1, column=8).value = str(res)
    excel.save(xls_paths)
    try:
        contrast = case[5]
        if 'id' in str(res):
            variable.orderid = res['id']
        if isinstance(res, dict):
            # 去除时间戳等相关参数
            key_list = []
            for key in res.keys():
                if '_time' in key:
                    key_list.append(key)
            for key2 in key_list:
                res.pop(key2)
        # 结果校验
        print("==========实际结果=========")
        print('****' * 20)
        print(type(contrast))
        print(contrast)
        print(str(res) == case[6])
        print(str(res))
        print(variable.orderid)
        # print(res == case[6])
    except KeyError:
        print("当前请求的返回值内没有id参数")
    except:
        pass


# #
if __name__ == '__main__':
    pytest.main(['-v', 'test_excel_read05.py',
                 '--alluredir',
                 './result',
                 '--clean-alluredir'])
    # 报告
    # os.system('allure serve result')
