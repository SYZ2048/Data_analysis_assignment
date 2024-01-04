#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Terminal_PJ 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：SYZ
@Date    ：2023/12/13 21:52 
"""

from collision_analyse import location_statistics,time_statistics,weather_statistics,predict_severity
from party_analyse import motorcycle_type_statistics
from victim_analyse import victim_position,factors2injury_degree
from data_load import data_load

if __name__ == '__main__':
    data_load()
    print('data load: Done')
    print('start analyse')
    location_statistics()
    time_statistics()
    weather_statistics()
    predict_severity()
    print('start party analyse')
    motorcycle_type_statistics()
    print('start victim analyse')
    victim_position()
    factors2injury_degree()
