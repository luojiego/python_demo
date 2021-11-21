def dayUP(df):
    dayup = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
    
dayfactor = 0.01    
a = round(pow((1 + dayfactor), 365), 2)
#print(a)

df = 0.01
while dayUP(df) < a:
    df += 0.001

print("工作日的努力参数是:{:.3f}".format(df))
