"""
@File    :   create_delete_front.py
@Desc    :   全局前置，运行方法Case前运行此方法
"""
import os
import time

import pandas as pd

from config.config_manager import cm
from utility.client import request
from utility.public_variable import variable


class CreateDeleteFront:
    """全局前置方法"""

    def __init__(self):
        pass

    def create_delete_front_test(self):
        """
            前置方法-测试
        """
        print(f'这个是全局前置的测试方法')
    def user_method(self):
        """
            读取user_info.xlsx表内key， secret_key
        """
        # 根目录
        cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # 运行文件目录
        xls_path = os.path.join(cur_path, 'testdata', 'xlsx', 'user_info.xlsx')
        # 读取Excel数据信息
        df = pd.DataFrame(pd.read_excel(io=xls_path, sheet_name="Sheet1"))
        # 根据行遍历数据
        for index, row in df.iterrows():
            data_dict = {'user_name': row.get('user_name'), 'key': row.get('key'), 'secret_key': row.get('secret_key')}
            variable.userdata.append(data_dict)
        return variable.userdata



create_delete = CreateDeleteFront()
if __name__ == '__main__':
    create_delete.create_delete_front_test()
