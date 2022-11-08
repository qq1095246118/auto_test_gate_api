"""
@File    :   create_delete_front.py
@Desc    :   全局前置，运行方法Case前运行此方法
"""

import time

from config.config_manager import cm
from utility.client import request


class CreateDeleteFront:
    """全局前置方法"""

    def __init__(self):
        pass

    def create_delete_front_test(self):
        """
            前置方法-测试
        """
        pass


create_delete = CreateDeleteFront()
if __name__ == '__main__':
    create_delete.create_delete_front_test()
