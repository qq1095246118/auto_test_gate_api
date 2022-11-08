# -*- coding:utf-8 -*-
"""
@PROJECT: 读取配置文件信息
"""
import os
from config.config_reader import Config


def get_template_path():
    """从配置文件取数据模板地址"""
    template_path = cf.read_section('data_template')
    return template_path


# 根目录
project_root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

cf = Config()

class ConfigManager:
    """
        配置文件操作
    """

    def __init__(self):
        """
            初始化接口请求参数
        """
        self.host = 'host'
        self.reset_host_manage()
        self.holidays = []

    def reset_host_manage(self, host=None):
        """
            host关联配置， 配置URL 端口 用户名/密码信息
            数据库关联配置，数据库地址 端口 用户名/密码信息
        """
        host_session = cf.read_host(host)
        # 基本配置信息
        self.host = host
        self.host_url = "http://" + host_session['host'] + ":" + str(host_session['port'])
        self.user = host_session["username"]
        self.passwd = host_session["password"]
        self.ip = host_session['host']
        # 数据相关配置
        self.data_user = host_session['data_user']
        self.data_pawd = host_session['data_pawd']
        self.data_port = host_session['data_port']
        self.data_db = host_session['data_db']

    def get_db_vars(self, section):
        """读取数据库相关配置"""
        db_session = cf.read_section(section)
        ip = db_session.get("host")
        port = db_session.get("port")
        username = db_session.get("user")
        password = db_session.get("pawd")
        database = db_session.get("db")
        return ip, port, username, password, database


cm = ConfigManager()
