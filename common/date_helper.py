# -*- coding:utf-8 -*-
"""
@File    :   date_helper.py
@Desc    :   工具方法
"""
import datetime
import time
import chinese_calendar
import dateutil
from datetime import date


def get_the_specified_date(date, days):
    """获取给定日期的指定日期
    :param date: 给定日期（%Y-%m-%d）
    :param days: 距给定日期的天数
    :return: %Y-%m-%d
    """
    return (datetime.datetime.strptime(date, "%Y-%m-%d") +
            datetime.timedelta(days=days)).strftime("%Y-%m-%d")


def calc_date_days(date1, date2):
    """日期相减计算天数"""
    time_array1 = time.strptime(date1, "%Y-%m-%d")
    timestamp_day1 = int(time.mktime(time_array1))
    time_array2 = time.strptime(date2, "%Y-%m-%d")
    timestamp_day2 = int(time.mktime(time_array2))
    result = (timestamp_day2 - timestamp_day1) // 60 // 60 // 24
    return result + 1


def holiday_judge(date):
    """判断某日期是否为节假日。date为2021-07-10这样类型的日期"""
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:10])
    demo_time = datetime.date(year, month, day)
    data_is_holiday = chinese_calendar.is_holiday(demo_time)
    return data_is_holiday


def date_month_plus_reduce(date, month_nums):
    """date为要处理的日期，month_nums为要加减的月数，month_nums正数，为减一个月，month_nums负数，为加一个月，"""
    d = datetime.datetime.strptime(date, "%Y-%m-%d")
    # 获取年月日 YYYY-MM-DD
    d2 = str(d - dateutil.relativedelta.relativedelta(months=month_nums))[:10]
    return d2


def get_sunday(date):
    """
    传入一个日期返回该日期的周日
    :params date: 基本日期
    """
    sunday = datetime.datetime.strptime(date, "%Y-%m-%d")
    one_day = datetime.timedelta(days=1)
    while sunday.weekday() != 6:
        sunday += one_day
    sunday = str(sunday).split(' ')
    # 返回当前周的星期一和星期天的日期
    return sunday[0]


def get_today():
    """获取今天的日期"""
    today_date = date.today()
    return str(today_date)


def get_yesterday():
    """获取昨天的日期"""
    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    yesterday = today - one_day
    return str(yesterday)


def party_create_time():
    """
    :return:时间戳,获取当前时间
    """
    time_stamp = time.time()
    ends = str(time_stamp - int(time_stamp))[2:4]
    return time.strftime('%Y%m%d%H%S', time.localtime()) + ends
