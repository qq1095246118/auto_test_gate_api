#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import pytest


def run():
    # 指定目录/文件执行用例
    pytest.main(['-v', './pytest_excel2/test_excel_read05.py',
                 '--alluredir',
                 './result',
                 '--clean-alluredir'])


if __name__ == '__main__':
    run()
