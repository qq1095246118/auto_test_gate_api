# -*- coding: utf-8 -*-
"""
@File    :   spot_service.py
@Time    :   2022/11/14/10:08
@Author  :   Yan-QC
@Desc    :   现货订单二次封装层
"""
from time import time

from api.spot_api import spot_api


class SpotService:
    """
        现货Api二次封装
    """

    def spot_orders_service(self, currency_pair, amount, price=None, text="t-" + str(time() * 1000)[:6],
                            order_type="limit", account="spot", side="buy", iceberg="0", time_in_force="gtc",
                            auto_borrow=False, user=None):
        """
            现货下单接口
        :param user:
        :param currency_pair: 交易货币对 必填
        :param amount:下单数量 必填
        :param price: 价格 必填
        :param text: 订单自定义信息
        :param order_type:订单类型，limit - 限价单
        :param account:账户类型，spot - 现货账户，margin - 杠杆账户，cross_margin - 全仓杠杆账户
        :param side:买卖方向
        :param iceberg:冰山下单显示的数量，不指定或传 0 都默认为普通下单。如果需要全部冰山，设置为 -1
        :param time_in_force:Time in force 策略
        :param auto_borrow:杠杆(包括逐仓全仓)交易时，如果账户余额不足，是否由系统自动借入不足部分
        """
        if price is None:
            """
                当价格为空时，默认查询当前交易对货币价格
            """
            pass
        test_check_json = {"text": text, "currency_pair": currency_pair, "type": order_type,
                           "account": account, "side": side, "iceberg": iceberg, "amount": str(amount),
                           "price": price, "time_in_force": time_in_force, "auto_borrow": auto_borrow}
        return spot_api.spot_orders_api(test_check_json, user)


spot_service = SpotService()
if __name__ == "__main__":
    spot_service.spot_orders_service('ETH_USDT', 1, '3540')
