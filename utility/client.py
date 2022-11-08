"""
@File    :   client.py
@Desc    :   接口底层封装
"""
import hashlib
import os
from time import time
import requests

from common.api_method import post, get
from common.custom_logger import log
from config.config_manager import cm, project_root_path
from utility.public_variable import variable


class BasePage:
    """
        VMS基础类,基础信息封装类
    """

    def __init__(self):
        """服务器初始化"""
        cm.reset_host_manage('test71')  # 切换服务器地址
        self.host = cm.host_url         # 接口URL地址
        self.username = cm.user         # 登陆用户名
        self.password = cm.passwd       # 登陆密码
        self.token = None
        self.sign = None
        self.proxies = {
            'http': 'http://localhost:8888',
            'https': 'http://localhost:8888'}
        self.project_root_path = project_root_path  # 项目路径，根目录
        variable.username = cm.user
        variable.password = cm.passwd
    @log
    def login_vms(self, username, password):
        """
           VMS 登陆方法封装
           return：token信息
        """
        path = '/vms/login.json'
        url = self.host + path
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        body = {"data": {"loginAccount": username, "loginPwd": hashlib.md5(password.encode()).hexdigest()},
                "context": {"clientType": "web", "token": "", "clientMac": "", "timestamp": round(time() * 1000),
                            "brandId": ""}, "sign": "login_vms" + str(round(time() * 1000))}
        res = requests.post(url, json=body, headers=headers, verify=False).json()
        # 断言当前登陆状态，登陆失败则抛出异常
        assert res['errorCode'] == 'SUCCESS' and res['errorMsg'] == '成功', f"预期：SUCCESS 实际：{res['errorCode']}"
        # 获取token
        self.token = res['data']['token']
        return self.token

    """
        get、post二次封装
    """

    @log
    def get(self, url):
        """ get 封装方法 """
        # 若token检测为None则执行登陆方法获取token
        if self.token is None:
            self.login_vms(self.username, self.password)
        res = get(self.host, url, self.token)
        return res

    @log
    def post(self, path, params, server='vms', file_name=None):
        """ post 封装方法 """
        # 若token检测为None则执行登陆方法获取token
        if self.token is None:
            self.login_vms(self.username, self.password)
        # 对sign进行md5加密
        sign_md5 = self.token + str(round(time() * 1000)) + "key=" + "MKnEu6zaS04N23XoMUL8GOwOKIQwXMvT"
        self.sign = hashlib.md5(sign_md5.encode('utf-8')).hexdigest().upper()
        url = f"/{server}{path}"
        file_root_path = None
        if file_name:
            file_root_path = os.path.join(self.project_root_path, 'testdata', file_name)
        res = post(self.host, url, self.token, self.sign, params,
                   file_root_path, file_name)
        try:
            res = res.json()
        except ValueError:
            return res
        if isinstance(res, bool):
            return res
        if 'result' in res:
            return res['result']
        return res


request = BasePage()
if __name__ == '__main__':
    request.login_vms('13588888888', '123456')
