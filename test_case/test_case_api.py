# -*- coding: utf-8 -*-
"""
@File    :   test_case_api.py
"""
from test_case.test_api_service import case_api


class TestCaseApi:

    def test_case_01(self):
        """
            Get测试Case
        :return:
        """
        res = case_api.get_test_api()
        print('***' * 20)
        print(res)

    def test_case_02(self):
        """
            Post测试
        :return:
        """
        res = case_api.post_test_api()
        print('***' * 20)
        print(res)


