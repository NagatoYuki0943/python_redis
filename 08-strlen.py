import redis


pool = redis.ConnectionPool(host="localhost", port=6379, decode_responses=True)

r = redis.Redis(connection_pool=pool)


r.set("foo", "goo1")

# strlen(name)
# 返回name对应值的字节长度（一个汉字3个字节）
print(r.strlen("foo"))  # 4 'goo1'的长度是4
