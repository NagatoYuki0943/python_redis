import redis


pool = redis.ConnectionPool(host="localhost", port=6379, decode_responses=True)

r = redis.Redis(connection_pool=pool)


r.set("foo", "goo1")


# setbit(name, offset, value)
# 对 name 对应值的二进制表示的位进行操作
# 参数：
#     name - redis的name
#     offset - 位的索引（将值变换成二进制后再进行索引）
#     value - 值只能是 1 或 0


# 注：如果在Redis中有一个对应： n1 = "foo"，
# 那么字符串foo的二进制表示为：01100110 01101111 01101111
# 所以，如果执行 setbit('n1', 7, 1)，则就会将第7位设置为1，
# 那么最终二进制则变成 01100111 01101111 01101111，即："goo"
source = "陈思维"
source = "foo"
for i in source:
    num = ord(i)
    print(bin(num).replace('b',''))
    # 01100110
    # 01101111
    # 01101111
print()


# 特别的，如果source是汉字 "陈思维"怎么办？
# 答：对于utf-8，每一个汉字占 3 个字节，那么 "陈思维" 则有 9个字节 对于汉字，for循环时候会按照 字节 迭代，
# 那么在迭代时，将每一个字节转换 十进制数，然后再将十进制数转换成二进制 11100110 10101101 10100110 11100110 10110010 10011011 11101001 10111101 10010000


# getbit(name, offset)
# 获取name对应的值的二进制表示中的某位的值 （0或1）
print(r.getbit("foo", 0)) # 0 foo1 对应的二进制 4个字节 32位 第0位是0还是1
# 0
print()


# bitcount(key, start=None, end=None)
# 获取name对应的值的二进制表示中 1 的个数
# 参数：
#     key - Redis的name
#     start - 字节起始位置
#     end - 字节结束位置
print(r.get("foo"))
# goo1: 01100111
print(r.bitcount("foo",0,1))  # 11 表示前2个字节中，1出现的个数
# 11
print()


# bitop(operation, dest, *keys)
# 获取多个值，并将值做位运算，将最后的结果保存至新的name对应的值
# 参数：
#     operation - AND（并） 、 OR（或） 、 NOT（非） 、 XOR（异或）
#     dest - 新的Redis的name
#     *keys - 要查找的Redis的name

r.set("foo","1")  # 0110001
r.set("foo1","2")  # 0110010
print(r.mget("foo", "foo1"))
# ['1', '2']
print(r.bitop("AND","new","foo","foo1"))
# 1
print(r.mget("foo","foo1","new"))
# ['1', '2', '0']
print()

source = "12"
for i in source:
    num = ord(i)
print(num)  # 打印每个字母字符或者汉字字符对应的ascii码值 f-102-0b100111-01100111
# 50
print(bin(num))  # 打印每个10进制ascii码值转换成二进制的值 0b1100110（0b表示二进制）
# 0b110010
print(bin(num).replace('b',''))  # 将二进制0b1100110替换成01100110
# 0110010
print()
