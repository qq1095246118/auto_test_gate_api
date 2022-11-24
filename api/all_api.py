# -*- coding:utf-8 -*-
"""
@File    :   all_api.py
@Desc    :   应用层API父类
"""
from api.wallet_api import WalletApi
from test_case.test_api_service import CaseApi


class AllAPI(CaseApi, WalletApi):
    """
        继承所有API
    """
    pass


all_api = AllAPI()
