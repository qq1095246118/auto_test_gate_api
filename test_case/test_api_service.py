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

    def post_test_api_service(self, text='t-123456', currency_pair=None, type=None, accoun=None, side=None,
                              test_check_json1=None):
        test_check_json = {"text": text, "currency_pair": currency_pair, "type": type, "account": accoun,
                           "side": side, ''"iceberg": "0", "amount": "0.5", "price": "1655", "time_in_force": "gtc",
                           "auto_borrow": False}
        if test_check_json1:
            test_check_json.update(test_check_json1)
        test_check_json2 = '{"text": "t-123456", "currency_pair": "GT_USDT", "type": "limit","account": "spot","side": "buy",' \
                           '"iceberg": "0","amount": "0.5","price": "1655","time_in_force": "gtc","auto_borrow": false}'
        self.post_test_api(test_check_json)


case_api = CaseApi()
