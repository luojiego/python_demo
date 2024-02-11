import this

print(this.s)

d = {}
# 注意这里没有 range，只取一个 65 和 97
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)
print(d)

# 使用 help 函数查看函数的帮助文档
help(d.get)
__doc__ = d.get.__doc__
print(__doc__)

print("".join([d.get(c, c) for c in this.s]))

# Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。
print(d.get('A', '?'))
print(d.get('?', '&'))

# 这是 this.py 中的一段代码，它将字典 d 用于加密字符串 s。
# chr 是将整数转换为字符，ord 是将字符转换为整数。
print(ord('A'))
print(ord('Z'))
print(ord('a'))

for i in range(91,96):
    print("{}:{}".format(i, chr(i)))
