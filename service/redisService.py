import redis

HOST = '42.193.222.127'
PORT = 6379
PASSWD = 'letletguanlaoshiRedis14'

redis_pool = redis.ConnectionPool(host=HOST, port=PORT, password=PASSWD, decode_responses=True)
redis_connection = redis.Redis(connection_pool=redis_pool)


def get_hash_value(key: str):
    return redis_connection.hgetall(key)
