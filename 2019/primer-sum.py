def isPrimer(k):

    for i in range(2, k//2+1):
        if k % i == 0:
            return False
    return True
    
result = 1
for i in range(2, 101):
    if isPrimer(i):
        print(i)
        result += i
print(result)
