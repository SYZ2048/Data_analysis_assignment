# Readme

### 运行

```
python main.py
```

### 文件结构

```
Terminal_PJ\
	img\								# 存放报告和md文件中插入的图片
	result\								# 存放运行结果图
	traffic_data\						# 存放源数据和生成的数据文件
		switrs.sqlite					# kaggle数据库提供源文件
		collisions.csv					# 保存collisions table数据
		parties.csv						# 保存parties table数据
		victims.csv						# 保存victims table数据
	main.py
	data_load.py						# 由源文件生成traffic_data\*.csv
	collision_analyse.py				# 分析collisions table
	party_analyse.py					# 分析parties table
	victim_analyse.py					# 分析victims table
	Readme.md							# 本文档
```

