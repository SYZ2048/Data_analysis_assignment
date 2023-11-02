"""
# new:      20231101
# syz edit
# data cleaning and analysis
# 对房价数据集（data.xlsx）进行清洗和数据分析，并进行可视化
"""
import matplotlib.pyplot as plt
import pandas as pd
import re

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来设置字体样式以正常显示中文标签（黑体）
plt.rcParams['axes.unicode_minus'] = False  # 正确输出负数

data = pd.read_csv('data.csv')
pd.options.mode.chained_assignment = None  # default='warn'
# print(data.shape)   # (2583, 10)
# print(data)


# 发现有一整行记录为空值  ---> delete the row
data.drop(data.columns[0], axis=1, inplace=True)
data.dropna(how='all', inplace=True)  # 清除全为空的行

data['总价'] = [re.sub('[^0-9.]', '', price) for price in data['总价']]
data['建筑面积'] = [re.sub('[^0-9.]', '', area) for area in data['建筑面积']]
data['单价'] = [re.sub('[^0-9.]', '', price_per) for price_per in data['单价']]
# Index(['小区名字', '总价', '户型', '建筑面积', '单价', '朝向', '楼层', '装修', '区域'], dtype='object')
data['总价'] = data['总价'].astype(float)
data['单价'] = data['单价'].astype(float)

# filepath = 'data_cleaned.xlsx'
# cleaned.to_excel(filepath, index=False)


# 各区二手房均价分析
# done
def average_price():
    # 均价计算
    data1 = data.groupby(['区域'])['单价'].mean()

    # 可视化
    # 创建条形图
    plt.close()  # 关闭当前图像窗口
    ax = data1.plot.bar()

    # 添加标题和轴标签
    plt.title('各区二手房均价分析')
    plt.xlabel('区域', fontsize=15)
    plt.ylabel('各区均价', fontsize=15)
    plt.xticks(fontsize=12, rotation=0)  # 旋转30度
    plt.yticks(fontsize=12)
    # 在每个柱子上显示数值
    for a, b in enumerate(data1):
        plt.text(a, b, int(b), ha='center', va='bottom', fontsize=12)

    # 显示图表
    plt.draw()
    plt.pause(0.001)


# 各区二手房数量所占比例
# done
def number_proportion():
    data2 = data['区域'].value_counts()

    # 创建饼状图
    plt.close()  # 关闭当前图像窗口
    data2.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.legend(data2.index, title="图例", loc="upper right", bbox_to_anchor=(1.3, 1.1))

    plt.title("各区二手房数量所占比例")
    plt.ylabel('')  # 这将删除标签“values”，使图看起来更干净
    plt.draw()
    plt.pause(0.001)

    # print(data2)


# 全市二手房装修程度分析
# done
def house_decoration():
    data3 = data['装修'].value_counts()

    # 可视化
    # 创建条形图
    plt.close()  # 关闭当前图像窗口
    ax = data3.plot.bar()

    # 添加标题和轴标签
    plt.title('全市二手房装修程度分析')
    plt.xlabel('装修', fontsize=15)
    plt.ylabel('套数', fontsize=15)
    plt.xticks(fontsize=12, rotation=0)  # 旋转30度
    plt.yticks(fontsize=12)
    # 在每个柱子上显示数值
    for a, b in enumerate(data3):
        plt.text(a, b, int(b), ha='center', va='bottom', fontsize=12)

    # 显示图表
    plt.draw()
    plt.pause(0.001)


# 热门户型均价分析
# done
def type_average_price():
    num_per_type = data['户型'].value_counts()

    # print(data4.index)
    # print(data4.columns)
    # print(num_per_type)
    popular_type = num_per_type[0:6].index.tolist()
    # print(popular_type)
    data4 = data.groupby(['户型'])['单价'].mean()
    data4 = data4[popular_type]


    # 可视化
    # 创建条形图
    plt.close()  # 关闭当前图像窗口
    ax = data4.plot.bar()

    # 添加标题和轴标签
    plt.title('热门户型均价分析')
    plt.xlabel('户型', fontsize=15)
    plt.ylabel('均价', fontsize=15)
    plt.xticks(fontsize=12, rotation=0)  # 旋转30度
    plt.yticks(fontsize=12)
    # 在每个柱子上显示数值
    for a, b in enumerate(data4):
        plt.text(a, b, int(b), ha='center', va='bottom', fontsize=12)

    # 显示图表
    plt.draw()
    plt.pause(0.001)


# 二手房售价预测
def price_prediction():
    print("5")


if __name__ == '__main__':
    number_proportion()
