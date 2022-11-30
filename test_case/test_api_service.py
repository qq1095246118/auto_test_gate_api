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
    def post_test_api(test_check_json):
        """
            Post调试
        :return:
        """
        return request.post('/api/v4/spot/orders', test_check_json)

    def post_test_api_service(self):
        # test_check_json = {"text": text, "currency_pair": currency_pair, "type": type, "account": accoun,
        #                    "side": side, ''"iceberg": "0", "amount": "0.5", "price": "1655", "time_in_force": "gtc",
        #                    "auto_borrow": False}
        # if test_check_json1:
        #     test_check_json.update(test_check_json1)
        json3 = {'text': 't1668422436', 'currency_pair': 'ETH_USDT', 'type': 'limit', 'account': 'spot', 'side': 'buy',
                 'iceberg': '0', 'amount': '1', 'price': '3540', 'time_in_force': 'gtc', 'auto_borrow': False}
        test_check_json2 = '{"text": "t-123456", "currency_pair": "ETH_USDT", "type": "limit","account": "spot","side": "buy",' \
                           '"iceberg": "0","amount": "0.5","price": "3540","time_in_force": "gtc","auto_borrow": false}'
        self.post_test_api(test_check_json2)


case_api = CaseApi()
