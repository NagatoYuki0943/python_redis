import redis


pool = redis.ConnectionPool(host="localhost", port=6379, decode_responses=True)

r = redis.Redis(connection_pool=pool)


r.set("food", "beef")  # 设置键food的值为beef


# 设置新值并获取原来的值
print(r.getset("food", "barbecue"))  # 设置的新值是barbecue 设置前的值是beef
# beef
print(r.get("food"))  # 获取键food的值，返回barbecue
# barbecue
