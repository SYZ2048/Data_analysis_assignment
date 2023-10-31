import pandas as pd
import numpy as np

df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5), 'data2': np.random.randn(5)})
grouped = df['data1'].groupby(df['key1'])

grouped = df.groupby(df.dtypes, axis=1)
df1 = df.groupby('key1')['data1']
df2 = df.groupby('key1')[['data2']]
people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
# print(people)
key_list = ['one', 'one', 'one', 'two', 'two']
grouped = df.groupby('key1')
print(grouped['data1'].quantile(0.9))


