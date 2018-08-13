# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import pytz

COLUMNS = ['name', 'country', 'age']
INDEX = ['p1', 'p2', 'p3']

DATAF = [['John', 'US', 26], ['Jane', 'Japan', 24], ['Zhw', 'China', 26]]
DICF = {'name': ['John', 'Jane', 'ZhW'], 'country': ['US', 'Japan', 'China'], 'age': [26, 24, 26]}

DICS = dict(name='Tom', country='US', age=26)

#=======================================================================
"""对象属性"""
def fun1():
    df = DataFrame(DATAF, index=INDEX, columns=COLUMNS)
    """
        name country  age
    p1  John      US   26
    p2  Jane   Japan   24
    p3   Zhw   China   26
    """

    sr = Series(DICS)
    """
    age         26
    country     US
    name       Tom
    """

    n1 = sr.index
    """
    Index([u'age', u'country', u'name'], dtype='object')
    """

    # Series元素值（浅复制）
    n2 = sr.values
    """
    array([26, 'US', 'Tom'], dtype=object)
    """

    n3 = df.index
    """
    Index([u'p1', u'p2', u'p3'], dtype='object')
    """

    n4 = df.index.is_unique
    """
    True
    """

    n5 = df.columns
    """
    Index([u'name', u'country', u'age'], dtype='object')
    """

    n6 = df.values
    """
    array([['John', 'US', 26L],
           ['Jane', 'Japan', 24L],
           ['Zhw', 'China', 26L]], dtype=object)
    """

    n7 = df.shape
    """
    (3, 3)
    """

    df.rename(columns={'name': 'Name'}, inplace=False)
    """
        Name country  age
    p1  John      US   26
    p2  Jane   Japan   24
    p3   Zhw   China   26
    """

    df.rename(index={'p1': 'P1'}, inplace=False)
    """
        name country  age
    P1  John      US   26
    p2  Jane   Japan   24
    p3   Zhw   China   26    
    """


#=======================================================================
"""复制/修改/引用"""
def fun2():
    # 行标签索引：ix、loc、at，行号索引：ix、iloc、iat
    df = DataFrame(DATAF, index=INDEX, columns=COLUMNS)
    dfc = DataFrame(DATAF, index=INDEX, columns=COLUMNS)
    """
        name country  age
    p1  John      US   26
    p2  Jane   Japan   24
    p3   Zhw   China   26
    """

    # 获取单个元素，以下结果一致，at形式获取一个元素效率更高
    n1 = df.ix['p1', 'age']
    n2 = df.ix['p1', 2]
    n3 = df.ix[0, 'age']
    n4 = df.ix[0, 2]
    n5 = df.loc['p1', 'age']
    n6 = df.iloc[0, 2]
    n7 = df.at['p1', 'age']
    n8 = df.iat[0, 2]

    # 修改单个元素
    # dfc.ix['p1']['age'] = 28  修改无效
    # n1 = 28                   修改无效
    dfc['name'][0] = 'John'
    dfc.at['p1', 'age'] = 26
    dfc.loc[df[df['name'] == 'Zhw'].index[0], 'age'] = 26

    # 获取一行DataFrame
    m0 = df.ix[[0]]
    m0 = df[:1]
    """
        name country  age
    p1  John      US   26
    """
    # 获取完整一行Series，以下结果一致
    m1 = df.ix[0]
    m2 = df.ix['p1']
    m3 = df.loc['p1']
    m4 = df.iloc[0]
    """
    name       John
    country      US
    age          26
    """
    # 获取一行Series的部分列，以下结果一致
    b1 = df.ix['p1', ['name', 'country']]
    b2 = df.ix['p1', 'name':'country']
    b3 = df.ix[0, :2]
    """
    name       John
    country      US
    """

    # 改变一行Series，避免通过行赋值的变量修改源DataFrame
    dfc.ix['p1'] = Series({'name': 'Tom', 'age': 23, 'country': 'Canada'})  # 使用Series数据更新，DataFrame未匹配的列为Nan
    """
        name country  age
    p1   Tom  Canada   23
    p2  Jane   Japan   24
    p3   Zhw   China   26
    """
    dfc.ix['p1'] = {'name': 'John', 'age': 25, 'country': 'Canada'}  # 使用字典更新
    """
           name country   age
    p1  country     age  name
    p2     Jane   Japan    24
    p3      Zhw   China    26
    """
    dfc.ix['p1'] = ['John', 'Canada', 25]  # 由于列序不定，不建议此种方式更改行数据
    """
        name country  age
    p1  John  Canada   25
    p2  Jane   Japan   24
    p3   Zhw   China   26
    """
    dfc.ix['p1', ['name', 'age']] = ['John', 25]  # 更新一行Series的部分列
    """
        name country  age
    p1  John  Canada   25
    p2  Jane   Japan   24
    p3   Zhw   China   26
    """

    # 获取DataFrame的多行副本
    a1 = df.ix[['p1', 'p3']]
    """
        name country  age
    p1  John      US   26
    p3   Zhw   China   26
    """
    a2 = df.ix[[0, 2], :]
    """
        name country  age
    p1  John      US   26
    p3   Zhw   China   26
    """
    a3 = df.ix[:, ['name', 'age']]
    """
        name  age
    p1  John   26
    p2  Jane   24
    p3   Zhw   26    
    """
    a4 = df.ix[:2, ['name', 'age']]
    """
        name  age
    p1  John   26
    p2  Jane   24    
    """

    # 改变多行DataFrame，通过DataFrame进行复制时，必须保证行列序与目标DataFrame一致
    dfc.ix[['p1', 'p3']] = DataFrame({'name': ['Tom', 'Zhw'],
                                      'age': [26, 27],
                                      'country': ['Canada', 'China']},
                                     index=['p1', 'p3']).reindex(columns=['name', 'country', 'age'])
    """
        name country  age
    p1   Tom  Canada   26
    p2  Jane   Japan   24
    p3   Zhw   China   27
    """

    # 获取一列DataFrame
    d0 = df[['name']]
    """
        name
    p1  John
    p2  Jane
    p3   Zhw
    """
    # 获取一列Series的引用（浅复制）
    d1 = df['name']
    d2 = df.name
    """
    p1    John
    p2    Jane
    p3     Zhw
    """

    # 修改一列
    dfc['name'] = ['n1', 'n2', 'n3']
    """"
       name country  age
    p1   n1  Canada   26
    p2   n2   Japan   24
    p3   n3   China   27
    """
    dfc['name'] = Series({'p1': 'John', 'p2': 'Jane', 'p3': 'Zhw'})
    """
        name country  age
    p1  John  Canada   26
    p2  Jane   Japan   24
    p3   Zhw   China   27
    """

    # 获取多列副本
    f1 = df[['name', 'age']]
    """
        name  age
    p1  John   26
    p2  Jane   24
    p3   Zhw   26
    """

    df.head(5)  # 前5行（少于5行选择全部）
    df.tail(5)  # 后5行（少于5行选择全部）


#=======================================================================
"""缺失值处理"""
def fun3():
    df = DataFrame(DATAF, index=INDEX, columns=COLUMNS)
    """
        name country  age
    p1  John      US   26
    p2  Jane   Japan   24
    p3   Zhw   China   26
    """

    # iat使用绝对位置改变元素值
    df.iat[0, 1] = np.nan
    """
        name country  age
    p1  John     NaN   26
    p2  Jane   Japan   24
    p3   Zhw   China   26
    """

    # at使用标签名索引改变元素值
    df.at['p3', 'age'] = None
    """
        name country   age
    p1  John     NaN  26.0
    p2  Jane   Japan  24.0
    p3   Zhw   China   NaN
    """

    # 未找到索引或列时自动附加
    df.loc['p4', 'name'] = None
    """
        name country   age
    p1  John     NaN  26.0
    p2  Jane   Japan  24.0
    p3   Zhw   China   NaN
    p4  None     NaN   NaN
    """

    # 返回各元素是否为None或np.nan的DataFrame
    df.isnull()
    """
         name country    age
    p1  False    True  False
    p2  False   False  False
    p3  False   False   True
    p4   True    True   True
    """

    # 非就地填充缺失值，返回填充后的副本
    df.fillna(value='', inplace=False)
    """
        name country age
    p1  John          26
    p2  Jane   Japan  24
    p3   Zhw   China    
    p4 
    """

    # 删除含nan的行（默认为any）, 返回副本
    df.dropna(how='any', inplace=False)
    """
        name country   age
    p2  Jane   Japan  24.0
    """

    # 删除全为nan的行，返回副本
    df.dropna(how='all', inplace=False)
    """
        name country   age
    p1  John     NaN  26.0
    p2  Jane   Japan  24.0
    p3   Zhw   China   NaN
    """

    # 删除含nan的列，返回副本
    df.dropna(how='any', axis=1, inplace=False)
    """
    Empty DataFrame
    """

    # 删除全nan的列，返回副本
    df.dropna(how='all', axis=1, inplace=False)
    """
        name country   age
    p1  John     NaN  26.0
    p2  Jane   Japan  24.0
    p3   Zhw   China   NaN
    p4  None     NaN   NaN
    """


#=======================================================================
"""重复值处理"""
def fun4():
    df = DataFrame({'k1': ['one'] * 3 + ['two'] * 4, 'k2': [1, 1, 2, 3, 3, 4, 4]})
    """
        k1  k2
    0  one   1
    1  one   1
    2  one   2
    3  two   3
    4  two   3
    5  two   4
    6  two   4
    """

    # 查看某列非重复值
    df['k1'].unique()
    """
    array(['one', 'two'], dtype=object)
    """

    # 查看各行是否重复
    df.duplicated()
    """
    0    False
    1     True
    2    False
    3    False
    4     True
    5    False
    6     True
    """

    # 删除重复
    df.drop_duplicates(subset='k1', keep='first', inplace=False)
    """
        k1  k2
    0  one   1
    3  two   3
    """

    df.drop_duplicates(subset=['k1','k2'], keep='first', inplace=False)
    """
        k1  k2
    0  one   1
    2  one   2
    3  two   3
    5  two   4
    """


#=======================================================================
"""选择/过滤"""
def fun5():
    df = DataFrame(DATAF, index=INDEX, columns=COLUMNS)
    """
        name country  age
    p1  John      US   26
    p2  Jane   Japan   24
    p3   Zhw   China   26
    """

    # 选择age列值大于25的行
    df1 = df[df['age'] > 25]
    """
        name country  age
    p1  John      US   26
    p3   Zhw   China   26
    """

    # 选择age列值大于25且小于30的行
    df2 = df[(df['age'] > 20) & (df['age'] < 25)]
    """
        name country  age
    p2  Jane   Japan   24
    """

    # 将age小于25值加1
    df.loc[df[df['age'] < 25].index, 'age'] += 1
    """
    p1  John      US   26
    p2  Jane   Japan   25
    p3   Zhw   China   26
    """

    df['country'].str.lower().str.contains('us')


#=======================================================================
"""替换、增加、删除"""
def fun6():
    df = DataFrame(DATAF, index=INDEX, columns=COLUMNS)
    map_dict = {'china':'A', 'us':'B', 'japan':'C', 'canada':'D'}
    """
        name country  age
    p1  John      US   26
    p2  Jane   Japan   24
    p3   Zhw   China   26
    """

    # 修改某列格式--全部大写
    df['country'] = df['country'].str.upper()
    """
        name country  age
    p1  JOHN      US   26
    p2  JANE   Japan   25
    p3   ZHW   China   26
    """

    # 将country列的JAPAN改为CANADA
    df['country'].replace('JAPAN', 'CANADA', inplace=True)
    """
        name country  age
    p1  John      US   26
    p2  Jane  CANADA   24
    p3   Zhw   CHINA   26
    """

    # 增加列
    df['gender'] = ['M', 'M', 'F']  # 单独赋值
    df['address'] = np.nan          # 赋同一值
    """
        name country  age gender  address
    p1  John      US   26      M      NaN
    p2  Jane  CANADA   24      M      NaN
    p3   Zhw   CHINA   26      F      NaN
    """
    df['rank'] = df['country'].map(lambda x:map_dict[x.lower()]) # 字典映射添加列
    map_dict1 = {'CHINA': 'A', 'US': 'B', 'JAPAN': 'C', 'CANADA': 'D'}
    df['rank'] = df['country'].map(map_dict1)
    """
        name country  age gender  address rank
    p1  John      US   26      M      NaN    B
    p2  Jane  CANADA   24      M      NaN    D
    p3   Zhw   CHINA   26      F      NaN    A
    """

    # 增加行，行索引不存在时自动增加行
    df.at['p4', 'name'] = 'Tom'
    """
        name country   age gender  address
    p1  John      US  26.0      M      NaN
    p2  Jane  CANADA  24.0      M      NaN
    p3   Zhw   CHINA  26.0      F      NaN
    p4   Tom     NaN   NaN    NaN      NaN
    """

    # 使用append附加一行Series
    person1 = Series({'name': 'Alan', 'age': 23}, name='p5')
    df = df.append(person1, ignore_index=False)
    """
        name country   age gender  address
    p1  John      US  26.0      M      NaN
    p2  Jane  CANADA  24.0      M      NaN
    p3   Zhw   CHINA  26.0      F      NaN
    p4   Tom     NaN   NaN    NaN      NaN
    p5  Alan     NaN  23.0    NaN      NaN
    """

    # 使用append附加DataFrame，列序可能改变
    person2 = DataFrame(data=[['Adams', 'GERMANY']], columns=['name', 'country'], index=['p6'])
    df = df.append(person2, ignore_index=False)
    """
        address   age  country gender   name
    p1      NaN  26.0       US      M   John
    p2      NaN  24.0   CANADA      M   Jane
    p3      NaN  26.0    CHINA      F    Zhw
    p4      NaN   NaN      NaN    NaN    Tom
    p5      NaN  23.0      NaN    NaN   Alan
    p6      NaN   NaN  GERMANY    NaN  Adams
    """

    # 删除行
    df.drop(labels=['p5', 'p6'], axis=0, inplace=True)  # 就地删除p5、p6行
    df.drop(labels='p4', axis=0, inplace=True)          # 就地删除p4行

    # 就地删除列
    del df['address']
    df.drop(labels='gender', axis=1, inplace=True)


#=======================================================================
"""排序/变形"""
def fun7():
    df = DataFrame(DATAF, index=INDEX, columns=COLUMNS)
    """
        name country  age
    p1  John      US   26
    p2  Jane   Japan   24
    p3   Zhw   China   26
    """

    # 返回转置副本，columns和index互换
    df1 = df.transpose()
    df2 = df.T
    """
               p1     p2     p3
    name     John   Jane    Zhw
    country    US  Japan  China
    age        26     24     26
    """

    # 重置行序, 非就地
    df.reindex(['p1', 'p3', 'p2'])
    """
        name country  age
    p1  John      US   26
    p3   Zhw   China   26
    p2  Jane   Japan   24
    """

    # 按index(列)升序排列，返回副本
    df.sort_index(level=0, axis=0, inplace=False)
    """
        name country  age
    p1  John      US   26
    p2  Jane   Japan   24
    p3   Zhw   China   26
    """

    # 按columns(行)升序排列(默认升序)
    df.sort_index(axis=1, ascending=True, inplace=False)
    """
        age country  name
    p1   26      US  John
    p2   24   Japan  Jane
    p3   26   China   Zhw
    """

    # 按指定列升序排序，返回副本
    df.sort_values(by='country', inplace=False)
    """
        name country  age
    p3   Zhw   China   26
    p2  Jane   Japan   24
    p1  John      US   26
    """

    # 多列排序，返回副本
    df.sort_values(by=['age', 'country'], inplace=False)
    """
    name country  age
p2  Jane   Japan   24
p3   Zhw   China   26
p1  John      US   26
"""


#=======================================================================
"""多重索引"""
def fun8():
    df = DataFrame(np.arange(10).reshape((5, 2)),
                   columns=['c1', 'c2'],
                   index=[list('aabbc'), list('12122')])
    # 指定索引、列名标签
    df.columns.name = 'columns'
    df.index.names = ['key0', 'key1']
    """
    columns    c1  c2
    key0 key1        
    a    1      0   1
         2      2   3
    b    1      4   5
         2      6   7
    c    2      8   9
    """

    # 使用0级索引提取DataFrame
    a1 = df.loc['a']
    """
    columns  c1  c2
    key1           
    1         0   1
    2         2   3
    """

    # 使用1级索引提取一行series, 以下结果一致
    a2 = df.loc['a', '1']
    a3 = df.loc['a'].loc['1']
    """
    columns
    c1    0
    c2    1
    """

    # 提取一列series, 以下结果一致
    b1 = df.loc['a']['c1']
    b2 = df.loc['a', 'c1']
    b3 = df['c1']['a']
    """
    key1
    1    0
    2    2
    """

    # 使用单个元素, 以下结果一致
    n1 = df.loc['a', '1']['c1']
    n2 = df.loc['a', 'c1']['1']
    n3 = df.loc['a'].loc['1', 'c1']
    """
    0
    """

    # 由第二层索引（level=1或'key1'）升序排列, 默认非就地排序
    df.sortlevel(level=1, inplace=False)
    df.sortlevel(level=0, inplace=False)
    """
    columns    c1  c2
    key0 key1        
    a    1      0   1
    b    1      4   5
    a    2      2   3
    b    2      6   7
    c    2      8   9
    """

    # 交换一二层索引，并由第一层索引升序排列
    df.swaplevel(0, 1).sortlevel(0)
    df.swaplevel('key0', 'key1').sortlevel('key1')
    """
    columns    c1  c2
    key1 key0        
    1    a      0   1
         b      4   5
    2    a      2   3
         b      6   7
         c      8   9
    """

    # 获取第二层索引为'1'的行
    df1 = df.swaplevel('key0', 'key1').sortlevel('key1').loc['1']
    """
    columns  c1  c2
    key0           
    a         0   1
    b         4   5
    """

    # 由第二层索引计算具有相同索引的不同行元素之和
    df.sum(level=1, axis=0)
    """
    columns  c1  c2
    key1           
    1         4   6
    2        16  19
    """

    # 一层索引旋转为DataFrame的列
    df.reset_index(level='key1')
    """
    columns key1  c1  c2
    key0                
    a          1   0   1
    a          2   2   3
    b          1   4   5
    b          2   6   7
    c          2   8   9
    """

    # 多层索引旋转为DataFrame的列
    df2 = df.reset_index(level=['key0', 'key1'])
    """
    columns key0 key1  c1  c2
    0          a    1   0   1
    1          a    2   2   3
    2          b    1   4   5
    3          b    2   6   7
    4          c    2   8   9
    """

    # DataFrame的列旋转为索引, 替换原索引
    df21 = df2.set_index('key0', append=False)
    """
    columns key1  c1  c2
    key0                
    a          1   0   1
    a          2   2   3
    b          1   4   5
    b          2   6   7
    c          2   8   9
    """

    # DataFrame的列旋转为索引, 以内层索引形式添加
    df22 = df21.set_index('key1', append=True)
    """
    columns    c1  c2
    key0 key1        
    a    1      0   1
         2      2   3
    b    1      4   5
         2      6   7
    c    2      8   9
    """

    sr = Series(np.arange(5), index=[list('aabbc'), list('12122')])
    sr.index.names = ['key0', 'key1']
    """
    key0  key1
    a     1       0
          2       1
    b     1       2
          2       3
    c     2       4
    """

    # 获取全部二级索引为'1'的行
    m1 = sr[:, '1']
    """
    key0
    a    0
    b    2
    """

    # 获取全部一级索引为a的行
    m2 = sr['a']
    """
    key1
    1    0
    2    1
    """

    # 由第0层索引展开
    sr.unstack(0)
    sr.unstack('key0')
    """
         a    b    c
    1  0.0  2.0  NaN
    2  1.0  3.0  4.0
    """

    # 由第1层索引展开
    sr.unstack(1)
    sr.unstack('key1')
    """
    key1    1    2
    key0          
    a     0.0  1.0
    b     2.0  3.0
    c     NaN  4.0
    """

    # 索引展开再复原（可逆）, stack默认将行加入内层索引, 交换索引层级并排序之后可复原
    sr.unstack('key0').stack('key0').swaplevel('key0', 'key1').sortlevel('key0')
    """
    a  1    0.0
       2    1.0
    b  1    2.0
       2    3.0
    c  2    4.0
    """


#=======================================================================
"""合并/连接"""
def fun9():
    df1 = DataFrame({'key1': ['b', 'b', 'a', 'c'], 'data1': range(4)})
    """
       data1 key1
    0      0    b
    1      1    b
    2      2    a
    3      3    c    
    """

    df2 = DataFrame({'key2': ['a', 'b', 'd'], 'data2': range(3)})
    """
        data2 key2
    0      0    a
    1      1    b
    2      2    d   
    """

    df3 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
    """
       group_val
    a        3.5
    b        7.0    
    """

    # DataFrame内连接
    pd.merge(df1, df2, left_on='key1', right_on='key2', how='inner')
    """
       data1 key1  data2 key2
    0      0    b      1    b
    1      1    b      1    b
    2      2    a      0    a
    """

    # DataFrame外连接
    pd.merge(df1, df2, left_on='key1', right_on='key2', how='outer')
    """
       data1 key1  data2 key2
    0    0.0    b    1.0    b
    1    1.0    b    1.0    b
    2    2.0    a    0.0    a
    3    3.0    c    NaN  NaN
    4    NaN  NaN    2.0    d    
    """

    # DataFrame左连接
    pd.merge(df1, df2, left_on='key1', right_on='key2', how='left')
    """
       data1 key1  data2 key2
    0      0    b    1.0    b
    1      1    b    1.0    b
    2      2    a    0.0    a
    3      3    c    NaN  NaN
    
    """

    # DataFrame右连接
    pd.merge(df1, df2, left_on='key1', right_on='key2', how='right')
    """
       data1 key1  data2 key2
    0    0.0    b      1    b
    1    1.0    b      1    b
    2    2.0    a      0    a
    3    NaN  NaN      2    d    
    """

    # DataFrame索引作为连接键, df1的key1与df3的index连接
    pd.merge(df1, df3, left_on='key1', right_index=True, how='inner')
    df1.join(df3, on='key1', how='inner')
    """
       data1 key1  group_val
    0      0    b        7.0
    1      1    b        7.0
    2      2    a        3.5    
    """

    # df1, df2按索引合并
    df1.join(df2, how='inner')
    """
       data1 key1  data2 key2
    0      0    b      0    a
    1      1    b      1    b
    2      2    a      2    d    
    """

    # DataFrame纵向拼接, 默认outer, axis=0
    pd.concat([df1, df2], join='outer', ignore_index=True)
    """
       data1  data2 key1 key2
    0    0.0    NaN    b  NaN
    1    1.0    NaN    b  NaN
    2    2.0    NaN    a  NaN
    3    3.0    NaN    c  NaN
    4    NaN    0.0  NaN    a
    5    NaN    1.0  NaN    b
    6    NaN    2.0  NaN    d    
    """

    # DataFrame横向拼接, outer
    pd.concat([df1, df2], join='outer', axis=1)
    """
       data1 key1  data2 key2
    0      0    b    0.0    a
    1      1    b    1.0    b
    2      2    a    2.0    d
    3      3    c    NaN  NaN    
    """

    s1 = Series([0, 1], index=['a', 'b'])
    """
    a    0
    b    1
    """

    s2 = Series([1, 2], index=['b', 'c'])
    """
    b    1
    c    2
    """

    # Series纵向拼接
    pd.concat([s1, s2], axis=0)
    """
    a    0
    b    1
    b    1
    c    2
    """

    # Series横向拼接, 默认outer
    pd.concat([s1, s2], axis=1, join='outer')
    """
         0    1
    a  0.0  NaN
    b  1.0  1.0
    c  NaN  2.0
    """

    # Series纵向拼接为二级索引的形式
    pd.concat([s1, s2], keys=['one', 'two'])
    """
    one  a    0
         b    1
    two  b    1
         c    2
    """

    # Series横向拼接, 键名变为列名
    pd.concat([s1, s2], keys=['one', 'two'], axis=1, join='outer')
    pd.concat([s1, s2], keys=['one', 'two']).unstack(level=0)
    """
       one  two
    a  0.0  NaN
    b  1.0  1.0
    c  NaN  2.0
    """


#=======================================================================
"""旋转"""
def fun10():
    df = DataFrame({'date': ['1959-03-31', '1959-03-31', '1959-03-31', '1959-06-01', '1959-06-01', '1959-06-01'],
                     'item': ['realgdp', 'infl', 'unemp', 'realgdp', 'infl', 'unemp'],
                     'value': [2710.39, 0.0, 5.8, 2778.801, 2.340, 5.10]})
    """
             date     item     value
    0  1959-03-31  realgdp  2710.390
    1  1959-03-31     infl     0.000
    2  1959-03-31    unemp     5.800
    3  1959-06-01  realgdp  2778.801
    4  1959-06-01     infl     2.340
    5  1959-06-01    unemp     5.100    
    
    """

    # 旋转列为索引
    df.set_index(['date', 'item']).unstack('item')  # 将不同的item展开为不同的列
    df.pivot('date', 'item', 'value')
    """
    item        infl   realgdp  unemp
    date                             
    1959-03-31  0.00  2710.390    5.8
    1959-06-01  2.34  2778.801    5.1    
    """

#=======================================================================
"""离散化、画面划分、哑变量"""
def fun11():
    ages = np.array([20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32])
    bins = np.array([18, 25, 35, 60, 100])

    cats = pd.cut(ages,bins)

    # 各元素划分后的等级
    n1 = cats.codes
    """
    array([0, 0, 0, 1, 0, 0, 2, 1, 3, 2, 2, 1], dtype=int8)
    """

    # 划分等级
    n2 = cats.categories
    """
    Index([u'(18, 25]', u'(25, 35]', u'(35, 60]', u'(60, 100]'], dtype='object')
    """

    # 每个划分等级的成员数
    cats.value_counts()
    """
    (18, 25]     5
    (25, 35]     3
    (35, 60]     3
    (60, 100]    1
    """

    # 获取等级为1的元素
    ages1 = ages[ages > 30]
    """
    array([37, 31, 61, 45, 41, 32])
    """

    df = DataFrame({'key':list('bbacab'), 'data1':range(10,16)})
    """
       data1 key
    0     10   b
    1     11   b
    2     12   a
    3     13   c
    4     14   a
    5     15   b
    """

    # 某一列在各行的分布情况
    dummies = pd.get_dummies(df['key']).astype(int)
    """
       a  b  c
    0  0  1  0
    1  0  1  0
    2  1  0  0
    3  0  0  1
    4  1  0  0
    5  0  1  0
    """

    df[['data1']].join(dummies)
    """
       data1  a  b  c
    0     10  0  1  0
    1     11  0  1  0
    2     12  1  0  0
    3     13  0  0  1
    4     14  1  0  0
    5     15  0  1  0
    """


#=======================================================================
"""运算/元素级处理"""
def fun12():
    df1 = DataFrame([[1, 2]], columns=['a', 'b'])
    df2 = DataFrame([[3, 4]], columns=['c', 'a'])

    df1 + df2
    df1 - df2

    df3 = DataFrame(np.arange(9).reshape(3, 3), columns=list('abc'))

    func1 = lambda x: x.max() - x.min()
    func2 = lambda x: Series([x.min(), x.max()], index=['min', 'max'])

    df3.apply(func1, axis=0)  # 对每列的最大-最小
    df3.apply(func1, axis=1)  # 对每行的最大-最小
    df3.apply(func2, axis=0)  # 每列的最大和最小

    df3 = df3.applymap(lambda x: x + 10)  # 每个元素加10
    """
    >>> df1
       a  b
    0  1  2
    
    >>> df2
       c  a
    0  3  4
    
    行列同时匹配的元素进行运算
    ----------------------
    >>> df1 + df2
       a   b   c
    0  5 NaN NaN
    
    >>> df1 - df2
       a   b   c
    0 -3 NaN NaN
    
    >>> df3
       a  b  c
    0  0  1  2
    1  3  4  5
    2  6  7  8
    
    >>> df3.apply(func1, axis=0) 
    a    6
    b    6
    c    6
    dtype: int64
    
    >>> df3.apply(func1, axis=0) 
    0    2
    1    2
    2    2
    dtype: int64
    
    >>> df3.apply(func2, axis=0)
         a  b  c
    min  0  1  2
    max  6  7  8
    """


#=======================================================================
"""文件读写"""
def fun13():
    # .read_xxx()方法
    # 显示指定分隔符时read_csv(',')与read_table('\t')相同
    # index_col=..,可指定哪一列作为索引，默认自动生成索引0,1,...,n
    # skiprow=[...]， 指定忽略哪些行

    """
    # ex_dot.txt
    a,b,c,d,message
    1,2,3,4,hello
    5,6,7,8,world
    9,10,11,12,foo
    """

    pd.read_csv('./document/ex_dot.txt', header=None, sep=',')          # 无列名
    pd.read_csv('./document/ex_dot.txt', header='infer', sep=',')       # 首行作为列(默认)
    pd.read_table('./document/ex_space.txt', sep='\t')                  # 首行作为列，默认'\t'分割
    pd.read_table('./document/ex_space.txt', nrows=10)                  # 限制读取n行

    chunker = pd.read_table('./document/ex_space.txt', chunksize=2)     # 迭代器，每次读取2行
    for piece in chunker:
        print(piece)

    # 写入csv
    pd.read_csv('./document/ex_dot.txt').to_csv(path_or_buf='./document/df_out.csv',
                                                index=False,  # 不写入索引
                                                header=True,  # 写入列名
                                                sep=',',  # ','作为分割
                                                na_rep='NULL',  # 空白字符填充替代
                                                columns=['a', 'b']  # 指定输出列
                                               )


#=======================================================================
"""分组"""
def fun14():
    df = DataFrame({'key1':list('aabba'), 'key2':['one', 'two', 'one', 'two', 'one'],
                    'data1':np.random.randn(5), 'data2':np.random.randn(5)})
    """
          data1     data2 key1 key2
    0 -0.920623  1.020532    a  one
    1 -1.065934 -0.137086    a  two
    2  0.006132  1.514599    b  one
    3  0.661261 -0.727769    b  two
    4 -0.589670  1.618126    a  one  
    """

    # Series分组, 以下结果一致
    grouped = df['data1'].groupby(df['key1'])
    m1 = grouped.mean()
    m2 = df.groupby('key1')['data1'].mean()
    m3 = df.groupby('key1').mean()['data1']
    """
    key1
    a   -0.858742
    b    0.333696
    """
    grouped  = df['data1'].groupby(Series(['b']))
    grouped.mean()
    """
    b   -0.920623
    """
    grouped = df['data1'].groupby([df['key1'], df['key2']])
    grouped.mean()
    """
    key1  key2
    a     one    -0.755147
          two    -1.065934
    b     one     0.006132
          two     0.661261
    """

    # DataFrame分组
    grouped = df.groupby('key1')
    grouped.mean().add_prefix('mean_')
    """
          mean_data1  mean_data2
    key1                        
    a      -0.858742    0.833857
    b       0.333697    0.393415 
    """
    grouped = df.groupby(['key1','key2'])
    means = grouped.mean()
    """
                  data1     data2
    key1 key2                    
    a    one  -0.755147  1.319329
         two  -1.065934 -0.137086
    b    one   0.006132  1.514599
         two   0.661261 -0.727769
    """
    means.unstack('key2')
    """
             data1               data2          
    key2       one       two       one       two
    key1                                        
    a    -0.755147 -1.065934  1.319329 -0.137086
    b     0.006132  0.661261  1.514599 -0.727769
    """

    # 分组迭代
    df.set_index(['key1','key2']).sort_index(level='key1')
    """
                  data1     data2
    key1 key2                    
    a    one  -0.920623  1.020532
         one  -0.589670  1.618126
         two  -1.065934 -0.137086
    b    one   0.006132  1.514599
         two   0.661261 -0.727769
    """
    grouped = df.groupby(['key1', 'key2'])
    # 每次迭代返回含两个元素的元组, 0位为标签，1位为值
    res = [gp for gp in grouped]
    t0 = res[0][0]
    """
    ('a', 'one')
    """
    t1 = res[0][1]
    """
          data1     data2 key1 key2
    0 -0.920623  1.020532    a  one
    4 -0.589670  1.618126    a  one
    """

    # 返回分组字典
    group1 = df.groupby(['key1'])
    group2 = df.groupby(['key1', 'key2'])
    a = dict(list(group1))['a']
    """
         data1     data2 key1 key2
    0 -0.920623  1.020532    a  one
    1 -1.065934 -0.137086    a  two
    4 -0.589670  1.618126    a  one 
    """
    b = dict(list(group1))['b']
    """
          data1     data2 key1 key2
    2  0.006132  1.514599    b  one
    3  0.661261 -0.727769    b  two
    """
    a1 = dict(list(group2))['a','one']
    """
          data1     data2 key1 key2
    0 -0.920623  1.020532    a  one
    4 -0.589670  1.618126    a  one
    """

    # 使用字典分组，以下结果一致（合并两列）
    mapping = {'data1':'sum', 'data2':'sum', 'key1':'char'}
    sum1 = df.groupby(mapping, axis=1).sum()['sum']
    sum2 = df.apply(lambda x: x['data1'] + x['data2'], axis=1)
    """
    0    0.099909
    1   -1.203020
    2    1.520731
    3   -0.066509
    4    1.028456
    """

    # 对索引进行函数处理后分组
    df.index = pd.Index(['Joe', 'Steve', 'Wes', 'Jim', 'Travis'], name='id')
    """
               data1     data2 key1 key2
    id                                  
    Joe    -0.920623  1.020532    a  one
    Steve  -1.065934 -0.137086    a  two
    Wes     0.006132  1.514599    b  one
    Jim     0.661261 -0.727769    b  two
    Travis -0.589670  1.618126    a  one
    """
    df.groupby(len).sum()
    """
          data1     data2
    3  0.527684  0.578207
    5 -0.246603 -0.127241
    6  1.217305 -0.269157
    """
    df.groupby([len, 'key2']).sum()
    """
               data1     data2
      key2                    
    3 one  -0.615099  1.452613
      two   1.142783 -0.874407
    5 two  -0.246603 -0.127241
    6 one   1.217305 -0.269157
    """

    df = DataFrame({'key1':list('aabba'), 'key2':['one', 'two', 'one', 'two', 'one'],
                    'data1':    [-0.920623, -1.065934, 0.006132, 0.661261, -0.589670],
                    'data2':    [1.020532, -0.137086, 1.514599, -0.727769, 1.618126]})

    """
    >>> df.set_index(['key1','key2']).sort_index(level='key1')
                  data1     data2
    key1 key2                    
    a    one  -0.920623  1.020532
         one  -0.589670  1.618126
         two  -1.065934 -0.137086
    b    one   0.006132  1.514599
         two   0.661261 -0.727769
    """

    # 分组函数，对分组结果进行函数处理
    fun1 = lambda x:x.max() - x.min()
    df.groupby(['key1']).agg(fun1)
    """
             data1     data2
    key1                    
    a     0.476264  1.755212
    b     0.655129  2.242368
    """
    df.groupby(['key1', 'key2']).agg(fun1)
    """
                  data1     data2
    key1 key2                    
    a    one   0.330953  0.597594
         two   0.000000  0.000000
    b    one   0.000000  0.000000
         two   0.000000  0.000000
    """
    df.groupby(['key1', 'key2']).agg('mean')
    """
                  data1     data2
    key1 key2                    
    a    one  -0.755146  1.319329
         two  -1.065934 -0.137086
    b    one   0.006132  1.514599
         two   0.661261 -0.727769
    """
    df.groupby(['key1', 'key2'])['data1'].agg('mean')
    """
    key1  key2
    a     one    -0.755146
          two    -1.065934
    b     one     0.006132
          two     0.661261
    """
    # 使用多个分组函数
    df.groupby(['key1', 'key2'])['data1'].agg(['mean', fun1])
    """
                   mean  <lambda>
    key1 key2                    
    a    one  -0.755146  0.330953
         two  -1.065934  0.000000
    b    one   0.006132  0.000000
         two   0.661261  0.000000
    """
    # 使用函数分组且重命名分组名
    df.groupby(['key1', 'key2'])['data1'].agg([('col1', 'mean'), ('col2', fun1)])
    """
                   col1      col2
    key1 key2                    
    a    one  -0.755146  0.330953
         two  -1.065934  0.000000
    b    one   0.006132  0.000000
         two   0.661261  0.000000
    """

    # 分组apply，对所有分组应用函数功能
    def top(df, n=2, column='data1'):
        return df.sort_index(by=column)[-n:]
    # 所有分组中'data1'列最大的两行
    df.groupby('key1').apply(top,n=2,column='data1')
    """
               data1     data2 key1 key2
    key1                                
    a    0 -0.920623  1.020532    a  one
         4 -0.589670  1.618126    a  one
    b    2  0.006132  1.514599    b  one
         3  0.661261 -0.727769    b  two
    """
    df.groupby('key1', group_keys=False).apply(top, n=2, column='data1')
    """
          data1     data2 key1 key2
    0 -0.920623  1.020532    a  one
    4 -0.589670  1.618126    a  one
    2  0.006132  1.514599    b  one
    3  0.661261 -0.727769    b  two
    """

    # 桶分析，某列的前3行、4和5行分别作为不同组，计算最大值、最小值
    def get_stats(group):
        return {'min':group.min(), 'max':group.max()}
    group_key  = ['1']*3  + ['2']*2
    df.groupby(group_key)['data1'].apply(get_stats).unstack(level=1)
    """
            max       min
    1  0.006132 -1.065934
    2  0.661261 -0.589670
    """


#=======================================================================
"""时间序列"""
def fun15():
    """
    pandas.to_datetime(arg, errors='raise', dayfirst=False, yearfirst=False,
        utc=None, box=True, format=None, exact=True, unit=None,
        infer_datetime_format=False, origin='unix', cache=False)

    Parameters
    ----------
    arg : integer, float, string, datetime, list, tuple, 1-d array, Series
    format : 指定输入格式（默认自动匹配），应显示声明
    exact : 是否准确匹配format与目标串，True准确匹配，False任意匹配

    pd.date_range(start=None, end=None, periods=None, freq=None, tz=None,
        normalize=False, name=None, closed=None, **kwargs)

    Parameters
    ----------
    start : 时间序列起始值
    end : 时间序列结束值
    periods : 生成数目
    freq: 生成元素间隔方式
    normalize : 规范化起始结束日期至00:00:00 23:59:59
    """
    pd.to_datetime('2017-01-02 03:00:00', format='%Y-%m-%d', utc=True)
    """
    Timestamp('2017-01-02 03:00:00+0000', tz='UTC')
    """

    # 时间戳
    pd.to_datetime(1490195805, unit='s')
    """
    Timestamp('2017-03-22 15:16:45')
    """
    pd.to_datetime(1490195805433502912, unit='ns')
    """
    Timestamp('2017-03-22 15:16:45.433502912')
    """

    # 时间字符串序列
    datestrs =['7/6/2011', '8/6/2011', '9/6/2011']
    pd.to_datetime(datestrs, format="%m/%d/%Y")
    """
    DatetimeIndex(['2011-07-06', '2011-08-06', '2011-09-06'], 
            dtype='datetime64[ns]', freq=None)
    """
    pd.to_datetime(datestrs, format="%d/%m/%Y")
    """
    DatetimeIndex(['2011-06-07', '2011-06-08', '2011-06-09'], 
            dtype='datetime64[ns]', freq=None)
    """
    datestrs = ['2011-07-06', '2011-08-06', '2011-09-06']
    pd.to_datetime(datestrs, format="%Y-%m-%d")
    """
    DatetimeIndex(['2011-07-06', '2011-08-06', '2011-09-06'], 
                dtype='datetime64[ns]', freq=None)
    """

    # 日期序列索引
    datestrs = ['2018-07-06', '2018-08-06', '2018-09-06']
    rng = pd.Index(pd.to_datetime(datestrs),name='date')
    dfdate = pd.DataFrame(np.arange(6).reshape((3,2)), index=rng, columns=['a', 'b'])
    """'
                a  b
    2018-07-06  0  1
    2018-08-06  2  3
    2018-09-06  4  5
    """
    row = dfdate.loc['20180706']
    """
    a    0
    b    1
    """
    rows = dfdate.loc['07/06/2018':'08/06/2018']
    """
                a  b
    date            
    2018-07-06  0  1
    2018-08-06  2  3
    """

    # 生成日期序列
    rng = pd.date_range(start='20180101 10:00:00', periods=3, freq='2H')
    """
    DatetimeIndex(['2018-01-01 10:00:00', '2018-01-01 12:00:00', '2018-01-01 14:00:00'],
                  dtype='datetime64[ns]', freq='2H')
    """
    dfhour = pd.DataFrame(np.arange(6).reshape((3,2)), index=rng)
    """
                         0  1
    2018-01-01 10:00:00  0  1
    2018-01-01 12:00:00  2  3
    2018-01-01 14:00:00  4  5
    """
    # 重采样
    dfhour.resample('1H').mean()
    """
                           0    1
    2018-01-01 10:00:00  0.0  1.0
    2018-01-01 11:00:00  NaN  NaN
    2018-01-01 12:00:00  2.0  3.0
    2018-01-01 13:00:00  NaN  NaN
    2018-01-01 14:00:00  4.0  5.0
    """
    # 超前/滞后移动数据
    dfhour.shift(1)
    """
                           0    1
    2018-01-01 10:00:00  NaN  NaN
    2018-01-01 12:00:00  0.0  1.0
    2018-01-01 14:00:00  2.0  3.0
    """
    # 超前/滞后移动索引
    dfhour.shift(1,'1D')
    """
                         0  1
    2018-01-02 10:00:00  0  1
    2018-01-02 12:00:00  2  3
    2018-01-02 14:00:00  4  5
    """

    # 时区转换
    # pytz.common_timezones[:] 查看时区
    rng = pd.date_range('20180714', '20180715',periods=3,
                        tz='Asia/Shanghai')     # 生成时间序列， 上海时区Asia/Shanghai
    """
    DatetimeIndex(['2018-07-14 00:00:00+08:00', '2018-07-14 12:00:00+08:00',
                   '2018-07-15 00:00:00+08:00'],
                  dtype='datetime64[ns, Asia/Shanghai]', freq=None)
    """
    rng.tz_convert('UTC')                       # 转换为UTC时间
    """
    DatetimeIndex(['2018-07-13 16:00:00+00:00', '2018-07-14 04:00:00+00:00',
               '2018-07-14 16:00:00+00:00'],
              dtype='datetime64[ns, UTC]', freq=None)
    """

    # Period整段时间范围
    pd.period_range('20180702','20181220',freq='M')
    """
    PeriodIndex(['2018-07', '2018-08', '2018-09', '2018-10', '2018-11', '2018-12'], 
        dtype='period[M]', freq='M')
    """
    pd.date_range('07/14/2018 06:00:00',periods=3,freq='12H').to_period(freq='D')
    """
    PeriodIndex(['2018-07-14', '2018-07-14', '2018-07-15'], dtype='period[D]', freq='D')
    """

    # 重采样/频率统计
    rng = pd.date_range('20180701', periods=10, freq='20D')
    df = pd.DataFrame(np.random.rand(10,2), index=rng)
    """
                       0         1
    2018-07-01  0.043837  0.972748
    2018-07-21  0.144425  0.295941
    2018-08-10  0.377654  0.141837
    2018-08-30  0.673730  0.145267
    2018-09-19  0.916249  0.966635
    2018-10-09  0.528616  0.030620
    2018-10-29  0.455784  0.522004
    2018-11-18  0.177691  0.723932
    2018-12-08  0.987019  0.322120
    2018-12-28  0.329621  0.684657
    """
    df.resample(rule='M', closed='left').sum()
    """
                       0         1
    2018-07-31  0.188263  1.268689
    2018-08-31  1.051384  0.287104
    2018-09-30  0.916249  0.966635
    2018-10-31  0.984400  0.552624
    2018-11-30  0.177691  0.723932
    2018-12-31  1.316640  1.006777
    """
    df.resample(rule='2M', kind='period').sum()
    """
                    0         1
    2018-07  1.239646  1.555793
    2018-09  1.900650  1.519258
    2018-11  1.494331  1.730709
    """
    df.resample(rule='2M', closed='left').sum()
    """
                       0         1
    2018-08-31  1.239646  1.555793
    2018-10-31  1.900650  1.519258
    2018-12-31  1.494331  1.730709
    """
    df.resample(rule='2M', closed='left', label='left').sum()
    """
                       0         1
    2018-06-30  1.239646  1.555793
    2018-08-31  1.900650  1.519258
    2018-10-31  1.494331  1.730709
    """