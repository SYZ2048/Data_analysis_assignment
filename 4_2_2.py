"""
# new:      20231018
# edit:     syz
# handin due:   20231025
# 双Y轴可视化产品销量
"""

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来设置字体样式以正常显示中文标签（黑体）
plt.rcParams['axes.unicode_minus'] = False  # 正确输出负数
df = pd.read_excel('mrbook.xlsx')

# 创建一个图形和两个y轴
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

x = df["月份"]
y1 = df["销量"]
y2 = df["rate"]
# plt.bar(x, y1)
# plt.plot(x, y2)

line, = ax2.plot(x, y2, label='rate', color='black', marker='o', ls='--')
bar = ax1.bar(x, y1,  label='销量（册）', color='royalblue', width=0.4)

# 设置x轴和y轴的标签，指明坐标含义
ax1.set_xlabel('月份', fontdict={'size': 16})
ax1.set_ylabel('销量（册）', fontdict={'size': 16})
ax2.set_ylabel('增长率', fontdict={'size': 16})
# 添加图表题
plt.title('销量情况对比')
# 添加图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines = lines1 + lines2
labels = labels1 + labels2
ax1.legend(lines, labels, loc='upper left')

for x, y in zip(df['月份'], df['rate']):
    ax2.text(x, y, '%.2f' % y, ha='center', va='bottom', fontsize=10, color='r')

plt.savefig('4_2_2_result.png')  #图表输出到本地
plt.show()

