# -*- coding: utf-8 -*-
"""
@file：handle_config
@Desc: 配置文件
"""
from configparser import RawConfigParser


class HandleConfig:
    """处理配置文件"""

    def __init__(self, file_path):
        self.filePath = file_path
        self.config = RawConfigParser()
        self.config.read(self.filePath, encoding="utf-8")

    def get_value(self, section, option):
        """get_value"""
        return self.config.get(section, option)

    def get_int(self, section, option):
        """get_int"""
        return self.config.getint(section, option)

    def write_config(self, section, option, value):
        """写配置文件"""
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option, value)
        with open(self.filePath, "w") as f:
            self.config.write(f)

    def del_config(self, section, option=None):
        """删除配置文件"""
        if option is None:
            self.config.remove_section(section)
        else:
            self.config.remove_option(section, option)
