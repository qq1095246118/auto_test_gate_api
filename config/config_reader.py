# -*- coding:utf-8 -*-
"""
@PROJECT: 配置文件操作
"""
import os
import yaml


class Config:
    """
    配置文件操作
    """

    def __init__(self):
        """
            初始化框架配置文件信息
        """
        # 配置文件路径拼装
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.yaml')
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("查配置文件，请确保配置文件存在！")
        # 基本信息配置文件
        self.yaml_file = self.get_yaml_file(self.conf_path)

    @staticmethod
    def get_yaml_file(file_path):
        """读取yaml"""
        yaml.load(file_path, Loader=yaml.BaseLoader)
        yaml.warnings({'YAMLLoadWarning': False})
        file = open(file_path, 'r', encoding='UTF-8')
        return yaml.load(file.read(), yaml.SafeLoader)

    def read_host(self, section=None):
        """
        读取配置文件中host相关信息
        :param section:
        :return:
        """
        if section is None:
            section = 'host'
        host = self.yaml_file[section]
        return host

    def read_directory(self):
        """
        读取配置文件中directory相关信息
        :return:
        """
        host = self.yaml_file['directory']
        return host

    def read_section(self, section):
        """
        读取配置文件中section相关信息
        :return:
        """
        value = self.yaml_file[section]
        return value

