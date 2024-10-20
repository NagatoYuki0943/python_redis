# redis 提供两个类 Redis 和 StrictRedis, StrictRedis 用于实现大部分官方的命令，Redis 是 StrictRedis 的子类，用于向后兼用旧版本。
# redis 取出的结果默认是字节，我们可以设定 decode_responses=True 改成字符串。

import redis  # 导入redis 模块


r = redis.Redis(host="localhost", port=6379, decode_responses=True)


r.set("name", "runoob")  # 设置 name 对应的值

# 这样 key 不存在会报错
print(r["name"])
# runoob

# 取出键 name 对应的值
print(r.get("name"))
# runoob


# 删除键 name
# 可以多次删除同一个键，不会报错
r.delete("name")
r.delete("name")


# 取出键 name 对应的值
print(r.get("name"))
# None
