# set(name, value, ex=None, px=None, nx=False, xx=False)
# 在 Redis 中设置值，默认，不存在则创建，存在则修改。
# 参数：
#     ex - 过期时间（秒）
#     px - 过期时间（毫秒）
#     nx - 如果设置为True，则只有name不存在时，当前set操作才执行
#     xx - 如果设置为True，则只有name存在时，当前set操作才执行


import time
import redis


pool = redis.ConnectionPool(host="localhost", port=6379, decode_responses=True)

r = redis.Redis(connection_pool=pool)


# 1.ex - 过期时间（秒） 这里过期时间是3秒，3秒后p，键food的值就变成None
print(r.set("food", "mutton", ex=3))
# True
print(r.get("food"))
# mutton
time.sleep(3)
print(r.get("food"))
# None
print()


# 2.px - 过期时间（豪秒） 这里过期时间是3豪秒，3毫秒后，键foo的值就变成None
print(r.set("food", "beef", px=3))
# True
print(r.get("food"))
# beef
time.sleep(0.003)
print(r.get("food"))
# None
print()


# 3.nx - 如果设置为True，则只有name不存在时，当前set操作才执行 （新建）
print(r.set("fruit", "watermelon", nx=True))
# fruit 不存在，那么输出是 True
print(r.set("fruit", "apple", nx=True))
# fruit 已经存在，输出是None
print()


# 4.xx - 如果设置为True，则只有name存在时，当前set操作才执行 （修改）
print((r.set("fruit", "orange", xx=True)))
# fruit 已经存在，输出是 True
print((r.set("flower", "rose", xx=True)))
# flower 不存在，输出是 None
print()


# 5.setex(name, time, value)
# 设置值
# 参数：
#     time - 过期时间（数字秒 或 timedelta对象）
r.setex("food", 5, "noodle")
print(r.get('food'))
# noodle
time.sleep(5)
print(r.get('food'))
# None
print()


# 6.psetex(name, time_ms, value)
# 设置值
# 参数：
#     time_ms - 过期时间（数字毫秒 或 timedelta对象）
r.psetex("food", 3, "noodle")
print(r.get('food'))
# noodle
time.sleep(0.003)
print(r.get('food'))
# None
print()


# 7.setnx(name, value)
# 设置值，只有name不存在时，执行设置操作（添加）
print(r.setnx('hobby', 'basketball'))
# hobby 不存在，输出为 True
print(r.setnx('hobby', 'tennis'))
# hobby 存在，输出为 False
print()
