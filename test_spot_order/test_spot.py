# -*- coding: utf-8 -*-
"""
@File    :   test_spot.py
@Time    :   2022/11/24/14:13
@Author  :   Yan-QC
@Desc    :   现货下单-基本功能覆盖
"""
import time

import pytest

from api.all_api import all_api
from api.spot_api import spot_api
from api.spot_service import spot_service


class TestSpot:

    def test_spot_order_buy_first_and_sell_later(self):
        """
            现货下单-先买后卖-全部成交

                    先买后卖-多笔成交
        """
        # 查询账户余额
        balances = all_api.wallet_sub_account_balances_list()
        # 查询市场深度
        book_data = spot_api.spot_order_book('BTC_USDT')
        assert book_data['asks'] != [] and book_data['bids'] != [], \
            f"预期结果：卖方深度与买方深度列表不应为空 实际：{book_data}"
        # 现货下单-买 全部成交
        test_check = spot_service.spot_orders_service('BTC_USDT', 1, "3000")
        assert test_check['currency_pair'] == 'BTC_USDT' and test_check['amount'] == "1" \
               and test_check['price'] == "3000", f"预期结果：{test_check}"
        # 查询账户余额
        balances_after = all_api.wallet_sub_account_balances_list()
        # 判断账户BTC账户余额是否买入成功
        assert int(balances[0]['available']['BTC']) + 1 == int(balances_after[0]['available']['BTC']), \
            f"预期结果：BTC余额为：{int(balances[0]['available']['BTC'])} " \
            f"实际结果：BTC余额为：{int(balances_after[0]['available']['BTC'])}"
        # 现货下单-卖 全部成交
        # test_check = spot_service.spot_orders_service('BTC_USDT', 1, "3000", side="sell")


    def test_spot_cancel_the_order(self):
        """
            现货下单后撤单-单笔
        :return:
        """
        # 查询账户余额
        balances = all_api.wallet_sub_account_balances_list()
        # 查询市场深度
        book_data = spot_api.spot_order_book('BTC_USDT')
        assert book_data['asks'] != [] and book_data['bids'] != [], \
            f"预期结果：卖方深度与买方深度列表不应为空 实际：{book_data}"
        # 现货下单-买 全部成交
        test_check = spot_service.spot_orders_service('BTC_USDT', 1, "3000")
        assert test_check['currency_pair'] == 'BTC_USDT' and test_check['amount'] == "1" \
               and test_check['price'] == "3000", f"预期结果：{test_check}"
        # 撤单
        order_delete = spot_api.spot_orders_delete(test_check['id'], "BTC_USDT")
        time.sleep(2)
        # assert order_delete['currency_pair'] == "BTC_USDT" and order_delete['status'] == "cancelled"

    def test_spot_cancel_multiple_orders(self):
        """
            现货下单后撤单-先买后卖-部分成交
        :return:
        """
        # 查询账户余额
        balances = all_api.wallet_sub_account_balances_list()
        # 查询市场深度
        book_data = spot_api.spot_order_book('BTC_USDT')
        assert book_data['asks'] != [] and book_data['bids'] != [], \
            f"预期结果：卖方深度与买方深度列表不应为空 实际：{book_data}"
        # 现货下单-买 全部成交
        test_check = spot_service.spot_orders_service('BTC_USDT', 1, "3000")
        assert test_check['currency_pair'] == 'BTC_USDT' and test_check['amount'] == "1" \
               and test_check['price'] == "3000", f"预期结果："

