# 函数编程示例
def inc(x):
    def incx(y):
        return x+y
    return incx

inc2 = inc(2)

inc5 = inc(5)

print(inc2(5))
print(inc5(5))