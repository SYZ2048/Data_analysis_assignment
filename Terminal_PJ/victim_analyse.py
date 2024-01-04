#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Data_assignment 
@File    ：victim_analyse.py
@IDE     ：PyCharm 
@Author  ：SYZ
@Date    ：2024/1/2 18:52 
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
victims = pd.read_csv(filepath + 'victims.csv')
victims.dropna(how='all', inplace=True)  # 清除全为空的行


def victim_position():
    victim_pos = victims.copy()
    # 数据清洗
    # 删除victim_seating_position列中含有空值的行
    victim_pos.dropna(subset=['victim_seating_position'], inplace=True)
    victim_pos_counts = victim_pos.groupby(['victim_seating_position']).size()
    victim_pos_counts = victim_pos_counts.sort_values(ascending=False)
    # 可视化
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))
    # 年份统计
    victim_pos_counts.plot(kind='bar')
    axes.set_title('Number of Victims in Seating Positions')
    axes.set_xlabel('Victim Seating Position')
    axes.set_ylabel('Number of Victims')
    # 在每个柱上显示数据
    for i, value in enumerate(victim_pos_counts):
        axes.text(i, value, str(value), ha='center', va='bottom')
    axes.set_xticklabels(victim_pos_counts.index, rotation=20)
    plt.show()


def factors2injury_degree():
    injury_factors = victims.copy()
    # 数据清洗
    factor = ['victim_degree_of_injury', 'victim_role', 'victim_sex',
              'victim_age', 'victim_seating_position',
              'victim_safety_equipment_1', 'victim_safety_equipment_2',
              'victim_ejected']
    injury_factors.dropna(subset=factor, inplace=True)
    # 这里假设这些列是分类数据
    for column in factor:
        injury_factors[column] = injury_factors[column].astype('category').cat.codes

    # 计算相关性
    correlation_matrix_full = injury_factors[factor].corr()  # -1到1之间，其中1表示完全正相关，-1表示完全负相关，0表示没有相关性
    correlation_matrix = correlation_matrix_full[['victim_degree_of_injury']].sort_values(
        by='victim_degree_of_injury', ascending=False)

    # 可视化
    plt.figure(figsize=(8, 8))
    # sns.heatmap(correlation_matrix_full, annot=True, cmap='coolwarm')
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Analysis')
    plt.xticks(rotation=0)
    plt.yticks(rotation=20)
    plt.show()

    # 卡方检验
    # 创建列联表
    for column in factor:
        contingency_table = pd.crosstab(injury_factors[column][0:10000],
                                        injury_factors['victim_degree_of_injury'][0:10000])
        # 执行卡方检验
        chi2, p, dof, expected = chi2_contingency(contingency_table)

        # 输出卡方检验的结果
        print("Chi2 Statistic:", chi2)
        print("P-value:", p)
    # result
    # Chi2
    # Statistic: 40000.0
    # P - value: 0.0
    # Chi2
    # Statistic: 7214.8009646423225
    # P - value: 0.0
    # Chi2
    # Statistic: 1533.6354772905293
    # P - value: 0.0
    # Chi2
    # Statistic: 2712.1421138353453
    # P - value: 0.0
    # Chi2
    # Statistic: 8307.397274813296
    # P - value: 0.0
    # Chi2
    # Statistic: 4294.1488238570155
    # P - value: 0.0
    # Chi2
    # Statistic: 7280.980206196597
    # P - value: 0.0
    # Chi2
    # Statistic: 4247.944239138149
    # P - value: 0.0


victim_position()
# factors2injury_degree()
