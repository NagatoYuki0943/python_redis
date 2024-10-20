import redis


pool = redis.ConnectionPool(host="localhost", port=6379, decode_responses=True)

r = redis.Redis(connection_pool=pool)


r.set("foo", "goo1")


# incr(self, name, amount=1)
# 自增 name 对应的值，当 name 不存在时，则创建 name＝amount，否则，则自增。
# 参数：
#     name - Redis的name
#     amount - 自增数（必须是整数）


r.set("foo", 1)
print(r.get("foo"))
# 1

r.incr("foo", amount=1)
print(r.get("foo"))
# 2

r.incr("foo", amount=2)
print(r.get("foo"))
# 4
