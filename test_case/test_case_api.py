# -*- coding: utf-8 -*-
"""
@File    :   test_case_api.py
"""
from api.all_api import all_api
from api.spot_service import spot_service
from test_case.test_api_service import case_api


class TestCaseApi:

    def test_case_01(self):
        """
            Get测试Case
        :return:
        """
        res = case_api.get_test_api()
        print('***' * 20)
        print(res)

    def test_case_02(self):
        """
            Post测试
        :return:
        """
        # 第一种调用方式
        # 优点：模块化清晰，调用实例化的服务类的方法较少,比较容易找到封装的方法
        # 缺点：Case或调用较多，对内存影响比较大
        # res = case_api.post_test_api_service()

        # 第二种调用方式：
        # 优点：只需要实例化子类，所有api的类的方法都可以通过all_api一个方法进行调用
        # 缺点：若继承类较多，方法会很多，比较难找到你要的方法
        # res = all_api.post_test_api()

        res = spot_service.spot_orders_service('ETH_USDT', 1, '3540')
        print('***' * 20)
        print(res)



