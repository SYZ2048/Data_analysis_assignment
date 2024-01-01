#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Terminal_PJ 
@File    ：data_analyse.py
@IDE     ：PyCharm 
@Author  ：SYZ
@Date    ：2023/12/13 21:58 
"""
import pandas as pd
# from data_load import collisions, parties, victims
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

pd.options.mode.chained_assignment = None  # default='warn'
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来设置字体样式以正常显示中文标签（黑体）
plt.rcParams['axes.unicode_minus'] = False  # 正确输出负数

filepath = './traffic_data/'
collisions = pd.read_csv(filepath + 'collisions.csv')
parties = pd.read_csv(filepath + 'parties.csv')
victims = pd.read_csv(filepath + 'victims.csv')


collisions.dropna(how='all', inplace=True)  # 清除全为空的行
parties.dropna(how='all', inplace=True)  # 清除全为空的行
victims.dropna(how='all', inplace=True)  # 清除全为空的行


def time_statistics():
    time_collision = collisions.copy()
    time_collision.dropna(subset=['collision_date', 'collision_time'], inplace=True)
    # 将COLLISION_DATE转换为日期格式，并提取年份
    # print(time_collision['collision_date'][0])
    time_collision['collision_date'] = pd.to_datetime(time_collision['collision_date'])
    time_collision['YEAR'] = time_collision['collision_date'].dt.year

    # 将COLLISION_TIME转换为时间格式，并提取小时
    time_collision['collision_time'] = pd.to_datetime(time_collision['collision_time'], format='%H:%M:%S').dt.hour

    # 按年份分组并统计数量
    yearly_counts = time_collision.groupby('YEAR').size()
    print(yearly_counts)
    # 按小时分组并统计数量
    hourly_counts = time_collision.groupby('collision_time').size()

    # 可视化
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
    # 年份统计
    yearly_counts.plot(kind='line', ax=axes[0])
    axes[0].scatter(yearly_counts.index, yearly_counts.values, marker='o', linestyle='-', c='g')
    axes[0].set_title('Number of Collisions by Year')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Number of Collisions')
    axes[0].xaxis.set_major_locator(MaxNLocator(integer=True))  # 控制横坐标间隔为整数

    # 24小时统计
    hourly_counts.plot(kind='line', ax=axes[1])
    axes[1].scatter(hourly_counts.index, hourly_counts.values, marker='o', linestyle='-', c='g')
    axes[1].set_title('Number of Collisions by Hour of the Day')
    axes[1].set_xlabel('Hour of the Day')
    axes[1].set_ylabel('Number of Collisions')
    axes[1].set_xticks(range(0, 24))
    axes[1].set_xticks(np.arange(0, 24, 1))  # 控制小时间隔为1小时
    plt.tight_layout()
    plt.show()


def location_statistics():
    position = collisions.copy()
    # 数据清洗
    # 删除latitude和longitude列中含有空值的行
    position.dropna(subset=['latitude', 'longitude'], inplace=True)

    # 可视化
    fig, ax = plt.subplots()
    ax.scatter(position['longitude'], position['latitude'], s=5)
    # 设置标签
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('Collision Positions')
    plt.show()


def weather_statistics():
    weather = collisions.copy()
    # 数据清洗
    # 替换其中空的数据为-，每个事故信息含[0,2]个天气信息
    weather[['weather_1', 'weather_2']] = weather[['weather_1', 'weather_2']].replace(np.nan, '-')
    # 按(weather1,weather2)分组并统计数量
    weather_counts = weather.groupby(['weather_1', 'weather_2']).size()
    # print(weather_counts)
    weather_condition_type = weather_counts[0:10].index.tolist()
    weather_condition = weather_counts.nlargest(10)
    # print(weather_condition)

    # 可视化
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))
    # 年份统计
    weather_condition.plot(kind='bar')
    axes.set_title('Number of Collisions in Weathers')
    axes.set_xlabel('Weather')
    axes.set_ylabel('Number of Collisions')
    # 在每个柱上显示数据
    for i, value in enumerate(weather_condition):
        axes.text(i, value, str(value), ha='center', va='bottom')
    axes.set_xticklabels(weather_condition.index, rotation=30)
    plt.show()


def


# location_statistics()
# time_statistics()
# weather_statistics()
