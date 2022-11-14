"""
@File    :   client.py
@Desc    :   接口底层封装
"""
import json
import os
from sys import _getframe
from common.api_method import post, get, gen_sign, delete
from common.custom_logger import log
from config.config_manager import cm, project_root_path
from utility.public_variable import variable


class BasePage:
    """
        基础信息封装类
    """

    def __init__(self):
        """服务器初始化"""
        cm.reset_host_manage('test160')  # 切换服务器地址
        self.host = cm.host_url  # 接口URL地址
        self.username = cm.user  # 登陆用户名
        self.password = cm.passwd  # 登陆密码
        self.key = 'c321f06c96cd0ab412e43ffd590c2d5a'
        self.secret = '1784d462e4da650fee20de9cb5d8a9242e287bc8f6a6f7a758da33d80a1f9ee7'
        self.method = None
        self.proxies = {
            'http': 'http://localhost:8888',
            'https': 'http://localhost:8888'}
        self.project_root_path = project_root_path  # 项目路径，根目录
        variable.username = cm.user
        variable.password = cm.passwd

    """
        get、post二次封装
        初版：二次封装请求信息，请求自动加密headers
        后期优化：减少gen_sign调用次数，所有二次封装请求自动指向gen_sign后置
    """

    @log
    def get(self, url, params=None, server='api/v4'):
        """ get 封装方法 """
        path = f"{server}{url}"
        if not params and isinstance(params, str):
            # Get方法的param只允许传str类型，且不允许为None，否则影响加密底层
            path = f"{server}/{url}?{params}"
        self.method = _getframe().f_code.co_name
        # 加密headers，请求自动携带加密信息
        gen_sign(self.key, self.secret, self.method, url, params)
        return get(self.host, path).json()

    @log
    def post(self, path, params=None, file_name=None):
        """ post 封装方法 """
        if isinstance(params, str):
            pass
        else:
            params = json.dumps(params)
        file_root_path = None
        if file_name:
            file_root_path = os.path.join(self.project_root_path, 'testdata', file_name)
        self.method = _getframe().f_code.co_name
        gen_sign(self.key, self.secret, self.method, path, params)
        res = post(self.host, path, params, file_root_path, file_name)
        try:
            res = res.json()
        except ValueError:
            return res
        if isinstance(res, bool):
            return res
        if 'result' in res:
            return res['result']
        return res

    def delete(self, url, params=None, server='api/v4'):
        """ delete 封装方法 """
        path = f"{server}{url}"
        if not params and isinstance(params, str):
            # Get方法的param只允许传str类型，且不允许为None，否则影响加密底层
            path = f"{server}/{url}?{params}"
        self.method = _getframe().f_code.co_name
        # 加密headers，请求自动携带加密信息
        gen_sign(self.key, self.secret, self.method, url, params)
        return delete(self.host, path).json()

    def __str__(self):
        # gen_sign(self.key, self.secret, self.method, url, query_string='', body=None)
        pass


request = BasePage()
if __name__ == "__main__":
    pass
