upname = ['LUO', 'JIE', 'AO', 'LI', 'AO']
lowname = []
for i in range(len(upname)): 
    lowname.append(upname[i].lower())
print(lowname)

# 函数式
def toUpper(item):
    return item.upper()

upper_name = map(toUpper, ['LUO', 'JIE', 'AO', 'LI', 'AO'])

print(upper_name)