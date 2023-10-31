"""
# new:      20231011
# syz edit
# handin:   20231017
# data cleaning
# 假设有一份会员数据集（data.xlsx），原始数据如图所示。第一列代表会员的姓名，第二列是性别，第三列是年龄，第四列是体重，第五列是身高。
# 数据集存在以下问题：请编写Python程序对数据集进行清洗。
"""

import pandas as pd
import re
import numpy as np
import os

pd.options.mode.chained_assignment = None  # default='warn'

# 1. 列名为数字，不能知道具体的数据的含义
# read data from xlsx file
data = pd.read_excel('data.xlsx', 'Sheet1', names=['name', 'gender', 'age', 'weight', 'height'])
print("*" * 15 + " original data " + "*" * 15)
print(data)

# 2. 数据的完整性检查
# 发现有一整行记录为空值  ---> delete the row
# 姓名为gloria的体重数据缺失
# print(data.isnull())
print("*" * 15 + " Cleaning step 1 " + "*" * 15)
cleaned = data.dropna(how='all')  # 清除全为空的行
cleaned = cleaned.fillna({'weight': 80})
print(cleaned)

# 3. 数据的全面性检查
# 发现身高的度量单位不统一，有米的，也有厘米的    ---> keep the units the same, we'll do cetimeters
# 姓名的首字母大小写不统一，有大写，也有小写的    ---> names are capitalized
print("*" * 15 + " Cleaning step 2 " + "*" * 15)
height = cleaned['height']
height[height < 2] = height * 100
# cleaned.loc[:, 'height'] = height

cleaned['name'] = cleaned['name'].str.title()
print(cleaned)

# 4. 数据的合法性检查
# 姓名字段存在非ASCII码字符、存在?号非法字符、出现空值    ---> delete special symbols
# 性别字段存在空格
# 年龄字段存在负数  ---> Be corrected as positive number
print("*" * 15 + " Cleaning step 3 " + "*" * 15)
names = cleaned['name']
cleaned['name'] = [re.sub('[^A-Za-z]', '', name) for name in names]  # result = re.sub('[\W_]+', '', s)

age = cleaned['age']
age[age < 0] = np.abs(age)
print(cleaned)

# 5. 数据的唯一性检查
# 姓名为Emma的记录存在重复 --> delete the duplicated one
print("*" * 15 + " Cleaning step 4 " + "*" * 15)
print(cleaned.duplicated())
cleaned = cleaned.drop_duplicates()
print(cleaned)

# 存入xlsx文件
# filepath为文件路径
filepath = 'data_cleaned.xlsx'
cleaned.to_excel(filepath, index=False)
