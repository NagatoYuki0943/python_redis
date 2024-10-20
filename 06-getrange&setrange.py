import redis


pool = redis.ConnectionPool(host="localhost", port=6379, decode_responses=True)

r = redis.Redis(connection_pool=pool)


# getrange(key, start, end)
# 获取子序列（根据字节获取，非字符）
# 参数：
#     name - Redis 的 name
#     start - 起始位置（字节）
#     end - 结束位置（字节）
# 如： "君惜大大" ，0-3表示 "君"


r.set("cn_name", "君惜大大") # 汉字
print(r.getrange("cn_name", 0, 2))   # 取索引号是0-2 前3位的字节 君 切片操作 （一个汉字3个字节 1个字母一个字节 每个字节8bit）
# 君
print(r.getrange("cn_name", 0, -1))  # 取所有的字节 君惜大大 切片操作
# 君惜大大

r.set("en_name","junxi") # 字母
print(r.getrange("en_name", 0, 2))  # 取索引号是0-2 前3位的字节 jun 切片操作 （一个汉字3个字节 1个字母一个字节 每个字节8bit）
print(r.getrange("en_name", 0, -1)) # 取所有的字节 junxi 切片操作
# jun
# junxi


# setrange(name, offset, value)
# 修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
# 参数：
#     offset - 字符串的索引，字节（一个汉字三个字节）
#     value - 要设置的值

r.setrange("en_name", 1, "ccc")
print(r.get("en_name"))    # jccci 原始值是junxi 从索引号是1开始替换成ccc 变成 jccci
# jccci
