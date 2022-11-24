# -*- coding: utf-8 -*-
"""
@File    :   wallet_api.py
@Time    :   2022/11/24/14:54
@Author  :   Yan-QC
@Desc    :   钱包账户
"""
from utility.client import request


class WalletApi:

    """
        钱包账户Api底层
    """

    @staticmethod
    def wallet_sub_account_balances_list():
        """
            查询子账号余额信息
        """
        return request.get('/wallet/sub_account_balances')
