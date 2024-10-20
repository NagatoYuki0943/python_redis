# 连接池
# redis-py 使用 connection pool 来管理对一个 redis server 的所有连接，避免每次建立、释放连接的开销。
# 默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数 Redis，这样就可以实现多个 Redis 实例共享一个连接池

import redis


pool = redis.ConnectionPool(host="localhost", port=6379, decode_responses=True)

r = redis.Redis(connection_pool=pool)


# 设置 name 对应的值
r.set("name", "runoob")

# 取出键 name 对应的值
print(r.get("name"))
# runoob
