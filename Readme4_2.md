# Readme4_2

### 绘制函数图

##### 代码在`4_2_1.py`中，输出结果保存至`4_2_1_result.png`中

使用matplotlib绘制如下函数，其中x的取值范围为[0, 2]
$$
f(x) = sin^2(x-2)^2 * e^{-x^2}
$$

```python
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(0, 2, 100)
fig = plt.figure()

f = (np.sin(x - 2)) ** 2 * np.e ** (-x ** 2)
plt.plot(x, f, "r-", label="f(x)")  # "r"为红色, "-"为实线
plt.legend()

# 设置坐标轴范围
plt.xlim((-0.5, 2.5))
plt.ylim((-0.2, 1.2))
# 设置坐标轴刻度
my_x_ticks = np.arange(-0.5, 2.5, 0.3)
plt.xticks(my_x_ticks)

# 设置轴标签和图名
plt.title('f(x)= (sin((x-2))^2 * e^(-x^2)')
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.savefig('4_2_result.png', dpi=400, bbox_inches='tight')
plt.show()

```

##### 结果如图所示

<img src="D:\code_python\Data_assignment\4_2_1_result.png" alt="4_2_1_result" style="zoom: 25%;" />



### 根据mrbook.xlsx 文件中的数据绘制双y轴可视化数据分析表

##### 代码在`4_2_2.py`中，输出结果保存至`4_2_2_result.png`中

创建一个图形和两个y轴

```python
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
```

分别使用`ax2.plot`绘制折线图line和使用`ax1.bar`柱状图bar，此处ax2.plot返回一个包含一个Line2D对象的列表

```python
x = df["月份"]
y1 = df["销量"]
y2 = df["rate"]
line, = ax2.plot(x, y2, label='rate', color='black', marker='o', ls='--')
bar = ax1.bar(x, y1,  label='销量（册）', color='royalblue', width=0.4)
```

设置x轴和y轴的标签，图名

```python
ax1.set_xlabel('月份', fontdict={'size': 16})
ax1.set_ylabel('销量（册）', fontdict={'size': 16})
ax2.set_ylabel('增长率', fontdict={'size': 16})
plt.title('销量情况对比')
```

将两种图表的图例合并起来

```python
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines = lines1 + lines2
labels = labels1 + labels2
ax1.legend(lines, labels, loc='upper left')
```

在折线图的点上标注增长率的数值

```python
for x, y in zip(df['月份'], df['rate']):
    ax2.text(x, y, '%.2f' % y, ha='center', va='bottom', fontsize=10, color='r')
```

结果如下图

![4_2_2_result](D:\code_python\Data_assignment\4_2_2_result.png)



### 根据mrtb_data.xlsx文件中的数据绘制堆叠柱状图。

##### 代码在`4_2_3.py`中，输出结果保存至`4_2_3_result.png`中

mrtb_data.xlsx中的数据如图所示，代码中只关注“类别”和“性别”两列数据

![image-20231021001540290](C:\Users\yxr\AppData\Roaming\Typora\typora-user-images\image-20231021001540290.png)

根据原始数据，首先对“类别”和“性别”进行数据统计，先对“类别”“性别”进行分组，然后分别计算不同的组中“买家实际支付金额”的总和

```python
df1 = df.groupby(['类别', '性别'])['买家实际支付金额'].sum().unstack()
```

更改index为`['女性用户', '男性用户']`

```python
df1 = df1.loc[:, ['男', '女']]
df1.columns = ['女性用户', '男性用户']
```

使用`ax.bar`绘制堆叠柱状图，并使用`ax.bar_label`标注柱状图的数据，该函数在matplotlib 3.4.0以上版本中引入，需要python3.9以上支持

```python
bottom = np.zeros(len(df1.index.values))
x = df1.index.values
for sex, sex_count in df1.items():
    p = ax.bar(x, sex_count, 0.6, label=sex, bottom=bottom, alpha=0.6)
    bottom += sex_count
    ax.bar_label(p, label_type='center')
```

结果如下图

<img src="D:\code_python\Data_assignment\4_2_3_result.png" alt="4_2_3_result"  />