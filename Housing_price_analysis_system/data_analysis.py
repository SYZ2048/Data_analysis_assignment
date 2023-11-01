"""
# new:      20231101
# syz edit
# data cleaning and analysis
# 对房价数据集（data.xlsx）进行清洗和数据分析，并进行可视化
"""

import pandas as pd


data = pd.read_csv('data.csv')
pd.options.mode.chained_assignment = None  # default='warn'
# print(data.head)

# 发现有一整行记录为空值  ---> delete the row
cleaned = data.dropna(how='all')  # 清除全为空的行