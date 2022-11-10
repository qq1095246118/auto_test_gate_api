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
        test_check_json = '{"text": "t-123456", "currency_pair": "GT_USDT", "type": "limit","account": "spot","side": "buy",' \
                          '"iceberg": "0","amount": "0.5","price": "1655","time_in_force": "gtc","auto_borrow": false}'

        return request.post('/api/v4/spot/orders', test_check_json)


case_api = CaseApi()
