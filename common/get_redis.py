# -*- coding: utf-8 -*-
"""
@FileName: get_redis.py
@Desc    :   Redis模块
"""

from redis import StrictRedis

from config.config_manager import cm


class RedisBase:

    # host代表主机地址，port为端口号,默认为6379， db为数据库的索引值

    @staticmethod
    def redis_strict():
        """
            Redis方法封装,默认取出结果为字符串
        """
        res = StrictRedis(host=cm.host,  port=6380, db=1,
                          password='', decode_responses=True)
        return res

    def redis_clear(self):
        """
            清空Redis信息
        """
        self.redis_strict().close()

    def redis_set_value(self, key, value):
        """
            添加key:value到Redis
        """
        rds = self.redis_strict().set(key, value)
        # 校验是否添加成功，否则返回None
        if rds.get(key) == value:
            print('新增Redis的Key信息成功')
            return True
        else:
            return None

    def redis_get_value(self, key):
        """根据key获取redis中的值,如果值为空进行错误提示"""
        rds = self.redis_strict().get(key)
        print('根据key查询redis中值为：' + rds)
        if rds is not None:
            return rds
        else:
            print('KeyError:')
            print("根据key未找到redis值！")

    def redis_delete_key(self, key):
        """
            删除当前Redis中的key信息
        """
        rds = self.redis_strict()
        # 删除当前key信息
        rds.delete(key)
        # 校验是否删除成功
        value = rds.get(key)
        if value is None:
            print('删除当前Redis的Key成功')
            return True
