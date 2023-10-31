# Readme4

### 数据合并

请编写Python程序将其中相同类别的Excel表合并到一起，有利于今后管理和分析数据

##### 数据类型

源文件为aa.zip，包含12个月的图书销售记录，每月分别保存在一个*.xlsx中，每个sheet包含以下列：

时间	商品名称	SKU	品牌	一级类目	二级类目	三级类目	浏览量	访客数	人均浏览量	平均停留时长	成交商品件数	ISBN	首次入库时间	成交码洋	加购人数

##### 下列输出结果保存至result.xlsx中

##### 各个xlsx表格直接进行轴向连接，按照时间进行排序

输出存储在result.xlsx的sort_by_time sheet中

```python
filenames = os.listdir(dirpath)
# 调整文件的读取顺序，按照月份进行排序
filenames.sort(key=lambda x: int(re.sub('[^0-9]', '', x.split(".")[0])))
for filename in filenames:
    data = pd.read_excel(dirpath + filename, names=['时间', '商品名称', 'SKU', '品牌', '一级类目',
                                                    '二级类目', '三级类目', '浏览量', '访客数',
                                                    '人均浏览量', '平均停留时长', '成交商品件数',
                                                    'ISBN', '首次入库时间', '成交码洋',
                                                    '加购人数'])  # [xxx rows x 16 columns]
    data.sort_values(by='时间', inplace=True)  # sort by time
    data_total.append(data)

# Concatenate pandas objects in all xlsx files
df = pd.concat(data_total)
```

![image-20231019193218459](C:\Users\yxr\AppData\Roaming\Typora\typora-user-images\image-20231019193218459.png)

##### 类目和名称做分层索引，按照时间进行排序

以一级类目、二级类目、三级类目、商品名称、时间做分层索引，结果样例如图所示，该样例输出存储在result.xlsx的sort_by_name sheet中

一级类目：[图书]

二级类目：[计算机与互联网]

三级类目：[编程语言与程序设计，数据库，网页制作/Web技术，移动开发]

```python
df2 = df.set_index(['一级类目', '二级类目', '三级类目', '商品名称', '时间'])
df2.sort_values(by=['商品名称', '时间'], inplace=True)
```

![image-20231019191059594](C:\Users\yxr\AppData\Roaming\Typora\typora-user-images\image-20231019191059594.png)



##### 进行初步数据统计

比如按照书名，对每本书的浏览量、访客数、成交商品件数等进行求和，求所有某书籍购买者的平均停留时长，结果样例如图所示，该样例输出存储在result.xlsx的statistical_data sheet中

```python
df4 = pd.pivot_table(df, index=['name'],
                     values=['view', 'visitor', 'time_on_page', 'number_of_transactions'],
                     aggfunc={'view': np.sum, 'visitor': np.sum, 'time_on_page': np.mean,
                              'number_of_transactions': np.sum}
                     # margins=True)
                     )
```

![image-20231019190303170](C:\Users\yxr\AppData\Roaming\Typora\typora-user-images\image-20231019190303170.png)



