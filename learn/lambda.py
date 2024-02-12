add = lambda x,y: x+y
print(add(3,5))

def fun_increase(n) :
    return lambda x: x+n

f=fun_increase(40)
print(f(2))