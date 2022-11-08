# -*- coding: utf-8 -*-

"""
@File    :   custom_logger.py
@Desc    :   日志模块
"""
import os
import logging
import sys
import time
import inspect
import traceback

from config.config_manager import project_root_path


class CustomLogger:
    """自定义配置log"""
    # 调用此类时创建logger实例，属于静态方法，必须要有返回值
    def __new__(cls):
        # 创建日志解析对象
        my_logger = logging.getLogger()
        # 设置解析器的收集等级
        my_logger.setLevel(logging.DEBUG)
        # 控制台输出收集器
        l_s = logging.StreamHandler(sys.stdout)
        # 输出收集等级
        l_s.setLevel(logging.INFO)
        # 日志文件输出收集器
        cur_time = time.strftime("%Y%m%d%H%M", time.localtime())
        main_path = os.path.join(project_root_path, 'logs')
        if not os.path.exists(main_path):  # 如果路径不存在
            os.makedirs(main_path)
        l_f = logging.FileHandler(main_path + '/{}.log'.format(cur_time), encoding='utf-8')
        # 输出收集等级
        l_f.setLevel(logging.DEBUG)
        # 将控制台和日志文件收集器添加到日志解析器
        my_logger.addHandler(l_s)
        my_logger.addHandler(l_f)
        # 日志输出格式
        fmt = '%(asctime)s - [%(filename)s --> line:%(lineno)d] - %(levelname)s : %(message)s'
        # 日志输出对象
        f_m = logging.Formatter(fmt)
        # 设置控制台和日志文件的格式
        l_s.setFormatter(f_m)
        l_f.setFormatter(f_m)
        # 返回日志解析器
        return my_logger


# 创建日志对象，后续直接引用对象，避免重复创建对象，添加日志Handler，重复写日志
logger_cls = CustomLogger()


def log(method):
    """自定义配置log解析"""
    def tmp(*parameter):
        try:
            response = ""
            key_list = inspect.getfullargspec(method)[0]
            length = len(key_list)
            if len(parameter) < length:
                length = len(parameter)
            log_msg = ''
            for i in range(1, length):
                log_msg += f"\n{key_list[i]}:{parameter[i]}"
            case_name = traceback.extract_stack()
            logging.info("case_name: %s", case_name[-3][2])
            logging.info(log_msg)
            response = method(*parameter)
            logging.info("response:%s", response)
        except Exception as err:
            logging.error(err)
        return response

    return tmp
