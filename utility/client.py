"""
@File    :   client.py
@Desc    :   接口底层封装
"""
import json
import os
from sys import _getframe
from common.api_method import post, get, gen_sign, delete, get_user_key
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
        self.key = 'e5e53741af49828c96bc2b7eae102b2c'
        self.secret = 'ca8facf4ff615ae2db1139d8660ce06af67eec8e70730cba88c6ad01048325dd'
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
    def get(self, url, params=None, server='/api/v4', user=None):
        """ get 封装方法 """
        path = f"{server}{url}"
        if not params and isinstance(params, str):
            # Get方法的param只允许传str类型，且不允许为None，否则影响加密底层
            path = f"{server}/{url}?{params}"
        self.method = _getframe().f_code.co_name
        # 加密headers，请求自动携带加密信息
        gen_sign(self.key, self.secret, self.method, url.split('?')[0], url.split('?')[1], params)
        return get(self.host, path).json()

    @log
    def post(self, path, params=None, user=None, query_string="", file_name=None):
        """ post 封装方法 """
        # params处理 支持body str dict类型传参
        if isinstance(params, str):
            pass
        else:
            params = json.dumps(params)
        # 获取当前方法名称
        self.method = _getframe().f_code.co_name
        file_root_path = None
        if file_name:
            # 文件上传
            file_root_path = os.path.join(self.project_root_path, 'testdata', file_name)
        # 交易对手模块，支持多笔吃单
        if user:
            data = get_user_key(user)
            if data is None:
                assert False, f"未找到{user}用户的key与secret_key 请检查输入用户名！！"
            gen_sign(data.get('key'), data.get('secret_key'), self.method, path, query_string, params)
        else:
            gen_sign(self.key, self.secret, self.method, path, query_string, params)
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
    @log
    def delete(self, url, params=None, server='/api/v4'):
        """ delete 封装方法 """
        path = f"{server}{url}"
        if not params and isinstance(params, str):
            # delete方法的param只允许传str类型，且不允许为None，否则影响加密底层
            path = f"{server}/{url}?{params}"
        self.method = _getframe().f_code.co_name
        # 加密headers，请求自动携带加密信息
        gen_sign(self.key, self.secret, self.method, server+url.split('?')[0], url.split('?')[1], params)
        return delete(self.host, path).json()

    def __str__(self):
        # gen_sign(self.key, self.secret, self.method, url, query_string='', body=None)
        pass


request = BasePage()
if __name__ == "__main__":
    pass
