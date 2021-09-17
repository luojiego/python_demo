import pandas as pd;
s=pd.read_excel("./1.xlsx", sheet_name="Sheet1")
print(s.head())
print("================================")
print("第一行列名: ", s.columns[0]) # 姓名
print("第二行列名: ", s.columns[1]) # 年龄
print("数据第一行第一列：", s.values[0][0])
print("数据第二行第二列：", s.values[1][1])