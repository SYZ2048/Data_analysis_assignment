#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Data_assignment 
@File    ：party_analyse.py
@IDE     ：PyCharm 
@Author  ：SYZ
@Date    ：2024/1/2 19:38 
"""

import pandas as pd
# from data_load import collisions, parties, victims
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
import seaborn as sns
from scipy.stats import chi2_contingency

pd.options.mode.chained_assignment = None  # default='warn'
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来设置字体样式以正常显示中文标签（黑体）
plt.rcParams['axes.unicode_minus'] = False  # 正确输出负数

filepath = './traffic_data/'
parties = pd.read_csv(filepath + 'parties.csv')
parties.dropna(how='all', inplace=True)  # 清除全为空的行


def motorcycle_type_statistics():
    motorcycle_type = parties.copy()
    # 数据清洗
    motorcycle_type.dropna(subset=['vehicle_make'], inplace=True)
    # 统计数量
    motorcycle_type_counts = motorcycle_type.groupby(['vehicle_make']).size()
    motorcycle_type_counts_top = motorcycle_type_counts.nlargest(10)

    # 可视化
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))
    # 年份统计
    motorcycle_type_counts_top.plot(kind='bar')
    axes.set_title('Number of Motorcycle_type in Collision')
    axes.set_xlabel('Motorcycle_type')
    axes.set_ylabel('Number of Motorcycle_type')
    # 在每个柱上显示数据
    for i, value in enumerate(motorcycle_type_counts_top):
        axes.text(i, value, str(value), ha='center', va='bottom')
    axes.set_xticklabels(motorcycle_type_counts_top.index, rotation=30)
    plt.show()


motorcycle_type_statistics()
