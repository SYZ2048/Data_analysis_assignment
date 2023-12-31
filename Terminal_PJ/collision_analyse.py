#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Terminal_PJ 
@File    ：collision_analyse.py
@IDE     ：PyCharm 
@Author  ：SYZ
@Date    ：2023/12/13 21:58 
"""
import pandas as pd
# from data_load import collisions, parties, victims
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from collections import Counter

pd.options.mode.chained_assignment = None  # default='warn'
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来设置字体样式以正常显示中文标签（黑体）
plt.rcParams['axes.unicode_minus'] = False  # 正确输出负数

filepath = './traffic_data/'
collisions = pd.read_csv(filepath + 'collisions.csv')
collisions.dropna(how='all', inplace=True)  # 清除全为空的行


def time_statistics():
    time_collision = collisions.copy()
    time_collision.dropna(subset=['collision_date', 'collision_time'], inplace=True)
    # 将COLLISION_DATE转换为日期格式，并提取年份
    # print(time_collision['collision_date'][0])
    time_collision['collision_date'] = pd.to_datetime(time_collision['collision_date'])
    time_collision['Year'] = time_collision['collision_date'].dt.year

    # 将COLLISION_TIME转换为时间格式，并提取小时
    time_collision['collision_time'] = pd.to_datetime(time_collision['collision_time'], format='%H:%M:%S').dt.hour

    # 按年份分组并统计数量
    yearly_counts = time_collision.groupby('Year').size()
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
    # 调整刻度大小
    axes[0].tick_params(axis='x', labelsize=16)  # 调整X轴标注点大小
    axes[1].tick_params(axis='x', labelsize=16)  # 调整X轴标注点大小
    plt.show()


def location_statistics():
    position = collisions.copy()
    # 数据清洗
    # 删除latitude和longitude列中含有空值的行
    position.dropna(subset=['latitude', 'longitude'], inplace=True)

    # 加利福尼亚州大城市的经纬度位置
    cities = {
        'Los Angeles': (-118.2437, 34.0522),
        'San Diego': (-117.1611, 32.7157),
        'San Jose': (-121.8863, 37.3382),
        'San Francisco': (-122.4194, 37.7749),
        'Fresno': (-119.7871, 36.7378),
        'Sacramento': (-121.4944, 38.5816)
    }

    # 可视化
    fig, ax = plt.subplots()
    ax.scatter(position['longitude'], position['latitude'], s=3)
    for city, (lon, lat) in cities.items():
        ax.scatter(lon, lat, color='red', zorder=5)
        ax.text(lon, lat+0.2, city, color='black', fontsize=20, ha='center', va='center')

    # 设置标签
    ax.set_xlabel('Longitude', fontsize=18)
    ax.set_ylabel('Latitude', fontsize=18)
    ax.set_title('Collision Positions', fontsize=18)
    # 调整刻度大小
    plt.tick_params(axis='x', labelsize=18)  # 调整X轴标注点大小
    plt.tick_params(axis='y', labelsize=18)  # 调整Y轴标注点大小
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
    axes.set_title('Number of Collisions in Weathers', fontsize=18)
    axes.set_xlabel('Weather', fontsize=18)
    axes.set_ylabel('Number of Collisions', fontsize=18)
    # 在每个柱上显示数据
    for i, value in enumerate(weather_condition):
        axes.text(i, value, str(value), ha='center', va='bottom')
    axes.set_xticklabels(weather_condition.index, rotation=20)
    # 调整刻度大小
    plt.tick_params(axis='x', labelsize=14)  # 调整X轴标注点大小
    plt.tick_params(axis='y', labelsize=24)  # 调整Y轴标注点大小
    plt.show()


def predict_severity():
    severity = collisions.copy()
    # severity.dropna(subset=['killed_victims'], inplace=True)
    severity['killed_victims'].fillna(0, inplace=True)
    severity['alcohol_involved'].fillna(0, inplace=True)
    severity['fatal'] = np.where((severity['killed_victims'] > 0) | (severity['injured_victims'] > 3), 1, 0)

    # conditions = [
    #     (severity['lighting'] == 'dark with no street lights') | (
    #                 severity['lighting'] == 'dark with street lights not functioning'),
    #     (severity['lighting'] == 'dark with street lights') | (severity['lighting'] == 'dusk or dawn'),
    #     (severity['lighting'] == 'daylight')
    # ]
    # choices = ['dark', 'mid', 'light']
    # severity['light'] = np.select(conditions, choices, default='unknown')

    target = 'fatal'
    features = ['alcohol_involved', 'road_surface', 'lighting', 'control_device',
                'pedestrian_collision', 'bicycle_collision', 'motorcycle_collision', 'truck_collision']
    one_hot_encoder = OneHotEncoder()
    preprocessor = ColumnTransformer(
        transformers=[
            ('onehot', one_hot_encoder, features)
        ],
        remainder='passthrough'  # 不对其他列进行转换
    )

    # 创建逻辑回归模型
    model = LogisticRegression()
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('model', model)])

    # 特征和目标变量
    X = severity[features]
    y = severity[target].apply(lambda x: 1 if x > 0 else 0)  # 转换为二元标签

    # 训练
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)
    print(Counter(predictions))  # Counter({0: 55726, 1: 11})
    print(Counter(y_test))  # Counter({0: 53988, 1: 1749})

    print(classification_report(y_test, predictions))


# location_statistics()
# time_statistics()
weather_statistics()
# predict_severity()
