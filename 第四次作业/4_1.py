"""
# new:      20231018
# syz edit
# handin due:   20231025
# 将其中相同类别的Excel表合并到一起
"""

import os
import pandas as pd
import re
import numpy as np

dirpath = 'aa/'

# 遍历文件夹
filenames = os.listdir(dirpath)
# 调整文件的读取顺序，按照月份进行排序
filenames.sort(key=lambda x: int(re.sub('[^0-9]', '', x.split(".")[0])))

# 时间	商品名称	SKU	品牌	一级类目	二级类目	三级类目	浏览量	访客数	人均浏览量	平均停留时长	成交商品件数	ISBN	首次入库时间	成交码洋	加购人数
data_total = []
dfs = []
for filename in filenames:
    data = pd.read_excel(dirpath + filename, names=['时间', '商品名称', 'SKU', '品牌', '一级类目',
                                                    '二级类目', '三级类目', '浏览量', '访客数',
                                                    '人均浏览量', '平均停留时长', '成交商品件数',
                                                    'ISBN', '首次入库时间', '成交码洋',
                                                    '加购人数'])  # [xxx rows x 16 columns]
    data.sort_values(by='时间', inplace=True)  # sort by time
    data_total.append(data)

# Concatenate pandas objects in all xlsx files
df = pd.concat(data_total)

# sort by name
df2 = df.set_index(['一级类目', '二级类目', '三级类目', '商品名称', '时间'])
df2.sort_values(by=['商品名称', '时间'], inplace=True)
df3 = pd.pivot_table(df, index=['商品名称'],
                     values=['浏览量', '访客数', '平均停留时长', '成交商品件数'],
                     aggfunc={'浏览量': np.sum, '访客数': np.sum, '平均停留时长': np.mean,
                              '成交商品件数': np.sum}
                     # margins=True)
                     )
#

# 保存
writer = pd.ExcelWriter("result.xlsx")
df.to_excel(writer, sheet_name="sort_by_time", index=False)
df2.to_excel(writer, sheet_name="sort_by_name")
df3.to_excel(writer, sheet_name="statistical_data")
writer.save()
writer.close()
