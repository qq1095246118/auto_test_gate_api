# -*- coding: utf-8 -*-
"""
@File    :   test_api_service.py
"""

from utility.client import request


class CaseApi:

    @staticmethod
    def get_test_api():
        """
            测试接口
        :return:
        """
        return request.get('/spot/currencies')

    @staticmethod
    def post_test_api():
        """
            Post调试
        :return:
        """
        test_check_json = {"text": "t-123456", "currency_pair": "ETH_USDT", "type": "limit", "account": "spot",
                           "side": "buy", "iceberg": "0", "amount": "1", "price": "5900", "time_in_force": "gtc",
                           "auto_borrow": False}
        return request.post('/spot/orders', test_check_json)


case_api = CaseApi()
