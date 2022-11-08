# -*- coding:utf-8 -*-
"""
@File    :   frame_constant.py
@Author  :   固定某些共有名称
@Desc    :   全局常量定义
"""


class FrameConstant:
    """全局专用常量 无法被修改"""

    class ConstError(PermissionError):
        """自定义异常处理"""
        pass

    class ConstCaseError(ConstError):
        """自定义异常处理"""
        pass

    def __init__(self):
        """
            框架常量，定义此常量无法被修改，用于全局无法被修改的值
            定义标准：常量名必须全部大写
        """
        self.COUNTER_PARTY_CODE = ""
        pass

    def __setattr__(self, name, value):
        """重写 __setattr__() 方法"""
        if name in self.__dict__:  # 已包含该常量，不能二次赋值
            raise self.ConstError(f"Can't change const {name}")
        if not name.isupper():  # 所有的字母需要大写
            raise self.ConstCaseError(f"const name {name} is not all uppercase")
        self.__dict__[name] = value


frame_constant = FrameConstant()
