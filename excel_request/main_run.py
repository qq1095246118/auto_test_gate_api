#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import pytest


def run():
    # 指定目录/文件执行用例
    pytest.main(['-sv', './pytest_excel2/test_excel_read05.py',
                 '--alluredir', './result', '--clean-alluredir',
                 # 报错退出，调试用
                 '-x',
                 # 最大出错数
                 '--maxfail=2'
                 ])
    # os.system('allure generate ./result/ -o ./report_allure/ --clean')
    os.system('allure serve result')


if __name__ == '__main__':
    run()
