#!/usr/bin/env python
# -*- coding: utf-8 -*-

# excel用例的读取与执行
import os

import allure
import openpyxl

# 读取Excel
import pytest

from excel_request.api_keyword.api_key import ApiKey


# 获取项目根路径
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


# 调试用，打印返回的tulpe_list
# a = read_excel()
# print(a)

@pytest.mark.parametrize('data', read_excel())
def test_01(data):
    """
            01编号
            02 地址
            03 路径
            04 请求方法
            05 请求头
            06 请求参数
            07 参数类型
            08 校验字段
            09 预期结果
            10 实际结果
            11 用例标题
    """

    # 动态生成标题
    allure.dynamic.title(data[10])
    print(data)

    # 如果存在请求头
    # if headers_list_05:
    if data[4] is not None:
        # 存在请求参数
        # if params_list_06:
        if data[5] is not None:
            dict_data = {
                'url': data[1] + data[2],
                # eval官方解释：讲字符串str当做有效的表达式来求值并返回计算结果
                # 这里直接给headers一个字典值
                'headers': eval(data[4]),
                # value[6]参数类型，data请求参数
                data[6]: eval(data[5])
            }
        # 不存在请求参数
        else:
            dict_data = {
                'url': data[1] + data[2],
                # eval官方解释：将字符串str当做有效的表达式来求值并返回计算结果
                # 这里直接给headers一个字典值
                'headers': eval(data[4]),
            }
    # 不存在请求头
    else:
        # 存在请求参数
        if data[5] is not None:
            dict_data = {
                'url': data[1] + data[2],
                # value[6]参数类型，data请求参数
                data[6]: eval(data[5])
            }
        # 不存在请求参数,只有URL
        else:
            dict_data = {
                'url': data[1] + data[2],
            }
    # 模拟请求
    # getattr(ak,value[3]) 是属性 + () 变成函数，()里传参数
    res = getattr(ak, data[3])(**dict_data)
    """
        常规的参数传递：
        requets.get(url="",params="",headers="")
        如果接口封装时，参数做了**kwargs的传递，可以直接通过字典传递
    """
    try:
        # 结果校验
        result = ak.get_text(res.text, data[7])
        print("==========实际结果=========")
        print(result == data[8])
    except:
        print("==========实际结果=========")
        print("请求参数有误，请检查")


# #
if __name__ == '__main__':
    pytest.main(['-v', 'test_excel_read05.py',
                 '--alluredir', './result', '--clean-alluredir'])
    os.system('allure serve result')
