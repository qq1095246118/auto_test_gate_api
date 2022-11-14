# -*- coding: utf-8 -*-
"""
@File    :   futures_api.py
@Time    :   2022/11/14/10:10
@Author  :   Yan-QC
@Desc    :   永续合约
"""
from utility.client import request


class FuturesApi:
    """
        永续合约Api
    """

    @staticmethod
    def futures_contracts_ist(settle_currency='usdt'):
        """
            查询所有的合约信息
        :return:
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/contracts')
        return test_check

    @staticmethod
    def futures_single_contract_information_list(settle_currency, contract):
        """
            查询单个合约信息
            currency:结算货币
            contract:合约标识
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/contracts/{contract}')
        return test_check

    @staticmethod
    def futures_order_book_list(settle_currency='usdt'):
        """
            查询合约市场深度信息
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/order_book')
        return test_check

    @staticmethod
    def futures_trades_list(settle_currency='usdt'):
        """
            查询市场成交记录
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/trades')
        return test_check

    @staticmethod
    def futures_candlesticks_list(settle_currency='usdt'):
        """
            合约市场 K 线图
        :return:
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/candlesticks')
        return test_check

    @staticmethod
    def futures_premium_index_list(settle_currency='usdt'):
        """
            合约溢价指数 K 线图
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/premium_index')
        return test_check

    @staticmethod
    def futures_tickers_list(settle_currency='usdt'):
        """
            获取所有合约交易行情统计
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/tickers')
        return test_check

    @staticmethod
    def futures_funding_rate_ist(settle_currency='usdt'):
        """
            合约市场历史资金费率
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/funding_rate')
        return test_check

    @staticmethod
    def futures_insurance_list(settle_currency='usdt'):
        """
            合约市场保险基金历史
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/insurance')
        return test_check

    @staticmethod
    def futures_contract_stats_list(settle_currency='usdt'):
        """
            合约统计信息
        :return:
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/contract_stats')
        return test_check

    @staticmethod
    def futures_index_constituents_list(settle_currency, index):
        """
            查询指数来源
            settle_currency:结算货币
            index：指数信息
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/index_constituents/{index}')
        return test_check

    @staticmethod
    def futures_liq_orders_list(settle_currency='usdt'):
        """
            查询强平委托历史
        :return:
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/liq_orders')
        return test_check

    @staticmethod
    def futures_accounts_list(settle_currency='usdt'):
        """
            获取合约账号
        :return:
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/accounts')
        return test_check

    @staticmethod
    def futures_account_book_list(settle_currency='usdt'):
        """
            查询合约账户变更历史
        :return:
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/account_book')
        return test_check

    @staticmethod
    def futures_positions_list(settle_currency='usdt'):
        """
            获取用户仓位列表
        :return:
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/positions')
        return test_check

    @staticmethod
    def futures_positions_and_contract_list(settle_currency, contract):
        """
            获取单个仓位信息
            settle_currency:结算货币
            contract:结算标识
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/positions/{contract}')
        return test_check

    @staticmethod
    def futures_positions_contract_margin(settle_currency, contract):
        """
            更新仓位保证金
            settle_currency:结算货币
            contract:结算标识
        :return:
        """
        test_check = request.post(f'/api/v4/futures/{settle_currency.lower()}/positions/{contract}/margin')
        return test_check

    @staticmethod
    def futures_risk_limit(settle_currency, contract):
        """
            更新仓位风险限额
        """
        test_check = request.post(f'/api/v4/futures/{settle_currency}/positions/{contract}/risk_limit')
        return test_check

    @staticmethod
    def futures_dual_mode(settle_currency='usdt'):
        """
            设置持仓模式
            变更模式的前提是，所有仓位没有持仓，并且没有挂单
        """
        test_check = request.post(f'/api/v4/futures/{settle_currency}/dual_mode')
        return test_check

    @staticmethod
    def futures_dual_comp_positions_contract(settle_currency, contract):
        """
            获取双仓模式下的持仓信息
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/dual_comp/positions/{contract}')
        return test_check

    @staticmethod
    def futures_update_risk_limit(settle_currency, contract):
        """
            更新双仓模式下的保证金
        """
        test_check = request.post(f'/api/v4/futures/{settle_currency}/dual_comp/positions/{contract}/margin')
        return test_check

    @staticmethod
    def futures_dual_comp_positions_contract_leverage(settle_currency, contract):
        """
            更新双仓模式下的杠杆
        """
        test_check = request.post(f'/api/v4/futures/{settle_currency}/dual_comp/positions/{contract}/leverage')
        return test_check

    @staticmethod
    def futures_update_dual_comp_risk_limit(settle_currency, contract):
        """
            更新双仓模式下的风险限额
        """
        test_check = request.post(f'/api/v4/futures/{settle_currency}/dual_comp/positions/{contract}/risk_limit')
        return test_check

    @staticmethod
    def futures_orders(settle_currency, test_check_json):
        """
            合约交易下单
        """
        test_check = request.post(f'/api/v4/futures/{settle_currency}/orders', test_check_json)
        return test_check

    @staticmethod
    def futures_orders_list(settle_currency):
        """
           查询合约订单列表
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/orders')
        return test_check

    @staticmethod
    def futures_orders_delete(settle_currency, param):
        """
            合约-批量取消状态为 open 的订单
        """
        test_check = request.delete(f'/api/v4/futures/{settle_currency}/orders?s{param}')
        return test_check

    @staticmethod
    def futures_batch_orders(settle_currency, test_check_json):
        """
            合约-合约交易批量下单
        """
        test_check = request.post(f'/api/v4/futures/{settle_currency}/batch_orders', test_check_json)
        return test_check

    @staticmethod
    def futures_single_order_list(settle_currency, order_id):
        """
            合约-查询单个订单详情
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/orders/{order_id}')
        return test_check

    @staticmethod
    def futures_cancel_single_order(settle_currency, order_id):
        """
            合约-撤销单个订单
        """
        test_check = request.delete(f'/api/v4/futures/{settle_currency}/orders/{order_id}')
        return test_check

    @staticmethod
    def futures_single_order_put(settle_currency, order_id):
        """
           合约-修改单个订单详情
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/orders/{order_id}')
        return test_check

    @staticmethod
    def futures_my_trades_list(settle_currency='usdt'):
        """
            合约-查询个人成交记录
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/my_trades')
        return test_check

    @staticmethod
    def futures_position_close_list(settle_currency='usdt'):
        """
            合约-查询平仓历史
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/position_close')
        return test_check

    @staticmethod
    def futures_liquidates_list(settle_currency='usdt'):
        """
            合约-查询强制平仓历史
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/liquidates')
        return test_check

    @staticmethod
    def futures_countdown_cancel_all(settle_currency, test_check_json):
        """
            合约-倒计时取消订单
        """
        test_check = request.post(f'/api/v4/futures/{settle_currency}/countdown_cancel_all', test_check_json)
        return test_check

    @staticmethod
    def futures_price_orders_api(settle_currency, test_check_json):
        """
            合约-创建价格触发订单
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/price_orders', test_check_json)
        return test_check

    @staticmethod
    def futures_price_orders_list(settle_currency='usdt'):
        """
            合约-查询自动订单列表
        """
        test_check = request.get(f'/api/v4/futures/{settle_currency}/price_orders')
        return test_check

    @staticmethod
    def futures_price_orders_delete():
        """
            合约-批量取消自动订单
        """
        test_check = request.delete('/api/v4/futures/orders')
        return test_check

    @staticmethod
    def futures_details_of_single_order(order_id):
        """
            合约-查询单个自动订单
        """
        test_check = request.get(f'/api/v4/futures/price_orders/{order_id}')
        return test_check

    @staticmethod
    def futures_cancel_automatic_order(order_id):
        """
            合约-撤销单个自动订单
        """
        test_check = request.delete(f'/api/v4/futures/price_orders/{order_id}')
        return test_check
