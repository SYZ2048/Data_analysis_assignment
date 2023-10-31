"""
# new:      20231018
# edit:     syz
# handin due:   20231025
# 根据mrtb_data.xlsx文件中的数据绘制堆叠柱状图
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来设置字体样式以正常显示中文标签（黑体）
plt.rcParams['axes.unicode_minus'] = False  # 正确输出负数
df = pd.read_excel('mrtb_data.xlsx')

fig, ax = plt.subplots()
# df1 = df.groupby(['类别', '性别'])['买家实际支付金额'].value_counts().to_frame().unstack()
df1 = df.groupby(['类别', '性别'])['买家实际支付金额'].sum().unstack()
df1 = df1.loc[:, ['男', '女']]
df1.columns = ['女性用户', '男性用户']
# print(df1.index.values)  # Index(['V1会员', 'V2会员', '图书', '明日高级VIP', '编程词典'], dtype='object', name='类别')
# print(df1.columns)    # MultiIndex([('性别', '女'), ('性别', '男')], names=[None, '性别'])


bottom = np.zeros(len(df1.index.values))
x = df1.index.values    # ['V1会员' 'V2会员' '图书' '明日高级VIP' '编程词典']

for sex, sex_count in df1.items():
    p = ax.bar(x, sex_count, 0.6, label=sex, bottom=bottom, alpha=0.7)
    bottom += sex_count
    ax.bar_label(p, label_type='center')


ax.set_title('Number of purchase by sex')
ax.set_ylabel("男女分布")
plt.xticks(rotation=30)  # 旋转30度
ax.legend()

plt.savefig('4_2_3_result.png')  # 图表输出到本地
plt.show()
