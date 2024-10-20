import redis


pool = redis.ConnectionPool(host="localhost", port=6379, decode_responses=True)

r = redis.Redis(connection_pool=pool)


# mset(*args, **kwargs)
# 批量设置值
# mget(keys, *args)
# 批量获取


print(r.mset({'k1': 'v1', 'k2': 'v2'}) ) # 这里k1 和k2 不能带引号，一次设置多个键值对
# True
print(r.mget("k1", "k2"))   # 一次取出多个键对应的值
# ['v1', 'v2']
print(r.mget("k1"))
# ['v1']

