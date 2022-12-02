#!/usr/bin/env python
# -*- coding: utf-8 -*-


# excel用例的读取与执行
import openpyxl

#读取Excel
from excel_request.api_keyword.api_key import ApiKey

excel = openpyxl.load_workbook('../case/api_cases.xlsx')
sheet = excel['Sheet1']
# print("===============Sheet数据类型==============")
# print(sheet)
ak = ApiKey()
# print(type(sheet.values))

#读取excel内容，实现文件驱动自动化执行
# 逐行循环读取Excel数据
for value in sheet.values:
    # print(value)
    # 判断当前行第一列的值，是否是数字编号
    if type(value[0]) is int:
        # 校验取值信息，调试用
        # print(value[0])
        # print(value[1])
        # 准备需要的测试数据
        # 请求参数
        data = value[5]
        # 调试使用，打印参数信息
        # print("==========参数=========")
        # print(data)

        # 校验字段
        assert_value = value[7]
        # 调试使用，打印信息
        # print("==========校验字段=========")
        # print(assert_value)

        # 预期结果
        # 调试使用，打印信息
        expect_value = value[8]
        # print("==========预期结果=========")
        # print(expect_value)


        # 如果存在请求头
        if value[4]:
            #存在请求参数
            if value[5]:
                dict_data = {
                    'url': value[1] + value[2],
                    # eval官方解释：讲字符串str当做有效的表达式来求值并返回计算结果
                    # 这里直接给headers一个字典值
                    'headers': eval(value[4]),
                    # value[6]参数类型，data请求参数
                    value[6]: eval(data)
                }
            #不存在请求参数
            else:
                dict_data = {
                    'url': value[1] + value[2],
                    # eval官方解释：将字符串str当做有效的表达式来求值并返回计算结果
                    # 这里直接给headers一个字典值
                    'headers': eval(value[4]),
                }
        # 不存在请求头
        else:
            #存在请求参数
            if value[5]:
                dict_data = {
                    'url': value[1] + value[2],
                    # value[6]参数类型，data请求参数
                    value[6]: eval(data)
                }
            #不存在请求参数,只有URL
            else:
                dict_data = {
                    'url': value[1] + value[2],
                }
        # 打印dict_data，调试用
        # print(dict_data)

        # 模拟请求
        # getattr(ak,value[3]) 是属性 + () 变成函数，()里传参数
        res = getattr(ak,value[3])(**dict_data)
        """
            常规的参数传递：
            requets.get(url="",params="",headers="")
            如果接口封装时，参数做了**kwargs的传递，可以直接通过字典传递
        """
        try:
            # 结果校验
            result = ak.get_text(res.text,assert_value)
            print("==========实际结果=========")
            print(result == expect_value)
        except:
            print("==========实际结果=========")
            print("请求参数有误，请检查")
