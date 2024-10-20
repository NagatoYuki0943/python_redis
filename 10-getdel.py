import redis


pool = redis.ConnectionPool(host="localhost", port=6379, decode_responses=True)

r = redis.Redis(connection_pool=pool)


# getdel(name) 从 Redis 中获取并删除该键对应的值，返回值。

print(r.set("food", "mutton"))
# True
print(r.getdel("food"))
# mutton
print(r.get("food"))
# None
print(r.getdel("food"))
# None 没有值返回 None

