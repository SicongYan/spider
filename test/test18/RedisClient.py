import random;
import redis;

REDIS_HOST = "127.0.0.1";
REDIS_PORT = "";
REDIS_PASSWORD = "";

"""
redis 工具
"""

class RedisClient(object):
    def __init__(self, type, website, host = REDIS_HOST, port = REDIS_PORT, password = REDIS_PASSWORD):
        """
        建立redis连接
        :param type:
        :param website:
        :param host:
        :param port:
        :param password:
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True);
        self.type = type;
        self.website = website;

    def name(self):
        return "{type}:{website}".format(type=self.type, website=self.website);

    def set(self, username, value):
        """
        设置键值对
        :param username:
        :param value:
        :return:
        """
        return self.db.hset(self.name(), username, value);

    def get(self, username):
        """
        根据键名获取值
        :param username:
        :return:
        """
        return self.db.hget(self.name(), username);

    def delete(self, username):
        """
        根据键名删除
        :param username:
        :return:
        """
        return self.db.hdel(self, username);

    def count(self):
        """
        获取数目
        :return:
        """
        return self.db.hlen(self.name());

    def random(self):
        """
        随机得到键值
        :return:
        """
        return random.choice(self.db.hvals(self.name()));

    def usernames(self):
        """
        获取账户信息
        :return:
        """
        return self.db.hkeys(self.name());

    def all(self):
        """
        获取所有键值对
        :return:
        """
        return self.db.hgetall(self.name());