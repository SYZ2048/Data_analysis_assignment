#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Terminal_PJ 
@File    ：data_load.py.py
@IDE     ：PyCharm 
@Author  ：SYZ
@Date    ：2023/12/13 21:53 
"""

import pandas as pd
from pandas_datareader import data as pdr
from datetime import datetime
import sqlite3

# Connect to SQLite database
filename = './traffic_data/switrs.sqlite'   # # table: case_ids\collisions\victims\parties
conn = sqlite3.connect(filename)

# Create a cursor object
cursor = conn.cursor()

# # Query for all table names
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#     print(table[0])
# # Execute a query
# cursor.execute("SELECT * FROM collisions")
# # Fetch all rows from the query
# rows = cursor.fetchall()
# print(rows[0:20])

# 只选取摩托车交通事故中的参与方
parties_query = " SELECT * FROM parties WHERE case_id IN \
(SELECT case_id FROM collisions WHERE motorcycle_collision == 1)"

# 只选取摩托车交通事故中的受害人
victims_query = " SELECT * FROM victims WHERE case_id IN \
(SELECT case_id FROM collisions WHERE motorcycle_collision == 1)"

# 只选取摩托车交通事故
collisions_query = "SELECT * FROM collisions WHERE motorcycle_collision == 1"
# Read the data
collisions = pd.read_sql_query(collisions_query, conn)
parties = pd.read_sql_query(parties_query, conn)
victims = pd.read_sql_query(victims_query, conn)

# 将选取的摩托车事故信息保存为csv，便于后续读取
filepath = './traffic_data/'
collisions.to_csv(filepath + 'collisions.csv', index=False)
parties.to_csv(filepath + 'parties.csv', index=False)
victims.to_csv(filepath + 'victims.csv', index=False)

# Close the connection
conn.close()
