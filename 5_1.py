#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Data_assignment
@File    ：5_1.py
@IDE     ：PyCharm
@Author  ：SYZ
@Date    ：2023/11/16 12:51
1. 请创建包含100万个数的列表，用本章定义的linear_contains()和binary_contains()函数分别
在该列表中查找多个数并计时，演示二分搜索相对于线性搜索的性能优势。
"""

import numpy as np
import time
import random

def linear_contains(lst, key):
    for idx in range(len(lst)):
        if lst[idx] == key:
            return idx
    return -1

def binary_contains(lst, key):
    low = 0
    high = len(lst) - 1
    while low <= high:
        # while there is still a search space
        mid = (low + high) // 2  # 向下取整
        if lst[mid] < key:
            low = mid + 1
        elif lst[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1


def sort_performance():
    # lst = [random.randint(0, 1000) for i in range(10)]
    position1 = []
    position2 = []
    data_lst = list(range(1000000))
    key_lst = [random.randint(0, 1100000) for i in range(1000)]  # 在[0,1100000)中随机取值，即存在检索失败情况
    print(key_lst)
    start_time1 = time.time()
    for value in key_lst:
        pos = linear_contains(data_lst, value)
        # position1.append(pos)
    end_time1 = time.time()

    start_time2 = time.time()
    for value in key_lst:
        pos = binary_contains(data_lst, value)
        # position2.append(pos)
    end_time2 = time.time()
    # print(position1)
    # print(position2)
    # if position1 == position2:
    print("Time to search for 1000 numbers by linear_contains: ", end_time1-start_time1)
    print("Time to search for 1000 numbers by binary_contains: ", end_time2-start_time2)



if __name__ == '__main__':
    sort_performance()
