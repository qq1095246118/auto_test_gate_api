import pytest

from api.create_delete_front import create_delete
from utility.public_variable import variable

'''
@File    :   conftest.py
@Desc    :   全局的前置条件和后置条件，每次执行时只会执行一次
'''


@pytest.fixture(scope='session', autouse=True)
def before_after():
    """
        全局前置，用例运行前运行此前置方法
        添加方法条件：在不影响其他前置的情况下，允许添加其他前置方法，不可重新赋值已赋值的全局变量
    :return:
    """
    # 全局前置演示案例
    # variable.password 为全局变量演示案例
    create_delete.create_delete_front_test()

    # 获取用户数据(key, secret_key)
    create_delete.user_method()

    yield before_after  # 后置条件
    """
        后置方法，全局用例运行后运行，用于删除/运行后的无用数据
    """
    pass