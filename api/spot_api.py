# -*- coding: utf-8 -*-
"""
@File    :   spot_api.py
@Time    :   2022/11/10/21:01
@Author  :   Yan-QC
@Desc    :   现货交易API
"""
from utility.client import request


class SpotApi:
    """
        现货交易API
    """

    @staticmethod
    def spot_currencies():
        """
            查询所有币种信息Api
        :return:
        """
        test_check = request.get('/api/v4/spot/currencies')
        return test_check

    @staticmethod
    def spot_currencies_currency(currency):
        """
            查询单个币种信息
        """
        test_check = request.get(f'/api/v4/spot/currencies{currency}')
        return test_check

    @staticmethod
    def spot_currency_pairs(currency_pair):
        """
            currency_pair未传参 默认查询所有交易对
            currency_pair传参 查询单个交易对
            1、查询所有交易对
            2、查询单个交易对详情
        """
        if currency_pair:
            test_check = request.get(f'/api/v4/spot/currency_pairs/{currency_pair}')
        else:
            test_check = request.get('/api/v4/spot/currency_pairs')
        return test_check

    @staticmethod
    def spot_tickers_query():
        """
            获取交易对tickers
        """
        test_check = request.get('/api/v4/spot/tickers')
        return test_check

    @staticmethod
    def spot_order_book(query_param):
        """
            获取市场深度信息
        """
        test_check = request.get(f'/spot/order_book?currency_pair={query_param}')
        return test_check

    @staticmethod
    def spot_trades():
        """
            查询成交记录
        """
        test_check = request.get('/spot/trades')
        return test_check

    @staticmethod
    def spot_candlesticks():
        """
            市场K线图
        """
        test_check = request.get('/api/v4/spot/candlesticks')
        return test_check

    @staticmethod
    def spot_fee():
        """
            查询账户费率
        """
        test_check = request.get('/api/v4/spot/fee')
        return test_check

    @staticmethod
    def spot_accounts():
        """
            获取现货列表
        """
        test_check = request.get('/api/v4/spot/accounts')
        return test_check

    @staticmethod
    def spot_batch_orders(test_check_json):
        """
            批量下单
        """
        test_check = request.post('/api/v4/spot/batch_orders', test_check_json)
        return test_check

    @staticmethod
    def spot_open_orders():
        """
            查询所有挂单
        """
        test_check = request.get('/api/v4/spot/open_orders')
        return test_check

    @staticmethod
    def spot_cross_liquidate_orders(test_check_json):
        """
            查询成交记录
        """
        test_check = request.get('/api/v4/spot/cross_liquidate_orders', test_check_json)
        return test_check

    @staticmethod
    def spot_orders_api(test_check_json):
        """
            现货下单
        """
        test_check = request.post('/api/v4/spot/orders', test_check_json)
        return test_check

    @staticmethod
    def spot_orders_list():
        """
            查询订单列表
        """
        test_check = request.get('/api/v4/spot/orders')
        return test_check

    @staticmethod
    def spot_orders_open_status_cancel():
        """
            批量取消一个交易对里状态为 open 的订单
        """
        test_check = request.delete('/api/v4/spot/orders')
        return test_check

    @staticmethod
    def spot_cancel_batch_orders(test_check_json):
        """
            查询所有挂单
        """
        test_check = request.get('/api/v4/spot/cancel_batch_orders', test_check_json)
        return test_check

    @staticmethod
    def spot_single_order_list(order_id, currency_pair):
        """
            查询单笔订单信息
        """
        test_check = request.get(f'/api/v4/spot/orders/{order_id}?currency_pair={currency_pair}')
        return test_check

    @staticmethod
    def spot_orders_delete(order_id, currency_pair):
        """
            撤销单个订单
        """
        test_check = request.get(f'/api/v4/orders/{order_id}?currency_pair={currency_pair}')
        return test_check

    @staticmethod
    def spot_orders_my_trades_list():
        """
            查询个人成交记录
        """
        test_check = request.get('/api/v4/spot/my_trades')
        return test_check

    @staticmethod
    def spot_service_time():
        """
            获取服务器时间
        """
        test_check = request.get('/api/v4/spot/orders')
        return test_check

    @staticmethod
    def spot_orders_countdown_cancel_all(test_check_json):
        """
            倒计时取消
        """
        test_check = request.post('/api/v4/spot/countdown_cancel_all', test_check_json)
        return test_check

    @staticmethod
    def spot_price_orders(test_check_json):
        """
            创建价格触发订单
        """
        test_check = request.post('/api/v4/spot/price_orders', test_check_json)
        return test_check

    @staticmethod
    def spot_price_orders_conduct_list():
        """
            查询进行中自动订单列表
        """
        test_check = request.get('/api/v4/spot/orders')
        return test_check

    @staticmethod
    def spot_price_orders_delete():
        """
            批量取消自动订单
        """
        test_check = request.delete('/api/v4/spot/orders')
        return test_check

    @staticmethod
    def spot_details_of_single_order(order_id):
        """
            查询单个自动订单
        """
        test_check = request.get(f'/api/v4/spot/price_orders/{order_id}')
        return test_check

    @staticmethod
    def spot_cancel_automatic_order(order_id):
        """
            撤销单个自动订单
        """
        test_check = request.delete(f'/api/v4/spot/price_orders/{order_id}')
        return test_check


spot_api = SpotApi()
