# -*- coding: utf-8 -*-
""""""

"""
标准模板库(Standard Tamplate Library)

sys, os, heap, deque, OrderedDict, Counter, time, Datetime, random

########################################################################
###  环境变量
#
# sys.path包含编译系统环境变量，放置在site-packages内的文件任何用户均可加载（需管理员权限）
# 添加sys.path.append()添加自定义环境变量，此方法仅一次有效
#
# windows新建系统环境变量:
#     variable name: PYTHONPATH, 变量中添加路径即可，永久有效


########################################################################
###  模块与包
#
# 模块载入时文件将被执行，重复载入的模块仅载入一次，可使用importlib.reload()函数重新加载
# 放置在site-packages内的文件任何用户均可加载（需管理员权限）
#
# __name__    当前文件为执行文件时，值为'__main__'；当前文件作为载入模块时，值为py文件名
# __all__     包含使用from module import * 可直接导入的内容
# __init__.py 导入包及其内的任何文件均会执行
#
# 包名drawing, 目录下含colors.py、__init__.py
# colors.py:
#     import drawing                # 仅执行__init__.py文件
#     import drawing.colors         # 导入colors.py，使用全部限定名drawing.colors.TAGNAME访问变量
#     import drawing.colors as col  # 导入colors.py，使用colors.TAGNAME访问变量
#     from drawing import colors    # 导入color.py，使用colors.TAGNAME访问变量
"""

########################################################################
###  sys    os
########################################################################
def moduleSysOs():
    import os,sys
    sys.argv()                      # 包含向Python解释器传递的参数，包括脚本名
    # sys.exit()                    # 退出主程序
    sys.path.append('../')          # 加入上级目录至编译器环境变量

    os.system("")                   # 执行程序，受限于空白(必须使用双引号包围)，
                                    # os.system(r'C:\"Program Files"\"Internet Explorer"\iexplore.exe')
    os.startfile('')                # 执行程序，不受限空白,os.startfile(r'C:\Program Files\Internet Explorer\iexplore.exe')

    os.listdir('dir')               # 获取目录下的全部文件名称
    os.path.walk('dir')             # 递归获取目录下所有文件和目录名称，返回元组path,dirnames,filenames
    os.path.basename(__file__)      # 返回当前文件名称
    os.path.dirname(__file__)       # 返回当前文件所在目录（不含文件名）
    os.path.abspath(__file__)       # 返回当前文件绝地路径（含文件名）
    os.path.abspath('..')           # 返回父级目录绝对路径
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))    # 返回父级目录绝对路径


########################################################################
###  heap
########################################################################
def moduleHeapq():
    import heapq
    heap, data = [], [0, 4, 5, 6, 3, 2, 1, 7, 8, 9]

    for n in data:                  # heapify(data)列表快速堆化
        heapq.heappush(heap,n)            # 压入堆, heap = [0, 3, 1, 6, 4, 5, 2, 7, 8, 9]

    assert heapq.heapreplace(heap,6) == 0 # 弹出最小元素，并压入新元素

    while len(heap):
        heapq.heappop(heap)               # 弹出堆,[1,2,3,4,5,6,6,7,8,9]


########################################################################
###  deque   OrderedDict    Counter
########################################################################
def moduleConllection():
    from collections import Counter,deque,OrderedDict
    ### deque--双端队列(doubel-ended queue),实现从列头/尾快速取出、队列旋转
    dq = deque()                    # 可直接在此初始化
    dq.extend([6,0,1,2,3])
    dq.append(4)                    # 右端添加元素, deque([6, 0, 1, 2, 3, 4])
    dq.appendleft(5)                # 左端添加元素, deque([5, 6, 0, 1, 2, 3, 4])
    dq.rotate(-2)                   # 旋转/整体移动.deque([0, 1, 2, 3, 4, 5, 6])

    ### Counter--计数器
    cou = Counter()
    sub = Counter('aabb')           # Counter({'a': 2, 'b': 2})
    cou.update('abccababb')         # 更新，Counter({'b': 4, 'a': 3, 'c': 2})
    res = cou.most_common(2)        # 数目最多的元素，[('b', 4), ('a', 3)]
    cou.subtract(sub)               # 减法，Counter({'c': 2, 'b': 2, 'a': 1})
    it = cou.elements()             # 返回迭代器

    ### OrderedDict--有序字典，利用列表存储键名
    items = ('a',1),('b',2),('c',3)
    odic = OrderedDict(items)       # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    odic.keys()                     # ['a', 'b', 'c']
    odic.popitem()                  # OrderedDict([('a', 1), ('b', 2)])


########################################################################
###  time   Datetime
########################################################################
def moduleTime():
    import time as tm
    from datetime import datetime, date, time, timedelta
    SECS = 1529239510.737           # 自1970-01-01 00:00:00 UTC以来的秒数

    # 日期元组字段(0,Year),(1,Month),(2,Day)，(3,Hour)，(4,Minute)，(5,Second)，(6,Week)...
    TUP, YEAR, MONTH, DAY = (2018,6,17,20,45,10,6,168,0), 2018, 6 , 17

    ISO_TM = '2018-06-17 20:45:10'
    ISO_FORMAT = '%Y-%m-%d %H:%M:%S'

    C_TM = 'Sun Jun 17 20:45:10 2018'
    C_FORMAT = '%a %b %d %H:%M:%S %Y'

    DATE_TIME, DATE, TIME = datetime(2018,06,17,20,45,10), date(2018,06,17), time(20,45,10)

    tm.time()            # 1529239510.737
    tm.localtime(SECS)   # 本地秒数转换为本地时间元组对象
    tm.gmtime(SECS)      # 本地秒数转换为UTC时间元组对象

    tm.mktime(TUP)       # 本地元组到本地秒, 1529239510.0
    tm.ctime(SECS)       # 本地秒到本地字符串， 'Sun Jun 17 20:45:10 2018'
    tm.asctime(TUP)      # 本地元组到本地字符串， 'Sun Jun 17 20:45:10 2018'

    tm.strftime(ISO_FORMAT, TUP)        # 元组到指定格式， '2018-06-17 20:45:10'
    tm.strptime(ISO_TM, ISO_FORMAT)     # 指定格式到元组
    ### time.struct_time(tm_year=2018,tm_mon=6,tm_mday=17,tm_hour=20,tm_min=45,tm_sec=10,tm_wday=6,tm_yday=168,tm_isdst=-1)

    tm.ctime(SECS - 3600 * 10)         # 时间减10时， 'Sun Jun 17 10:45:10 2018'

    datetime.now()                     # 类方法, 返回当前本地datetime对象
    datetime.utcnow()                  # 类方法，返回当前UTC datetime对象

    datetime.combine(DATE,TIME)        # 类方法, 由日期和时间返回datetime对象, datetime.datetime(2018, 6, 17, 20, 45, 10)

    datetime.strptime(ISO_TM,ISO_FORMAT) # 类方法, 返回datetime对象, datetime.datetime(2018, 6, 17, 20, 45, 10)
    datetime.strptime(C_TM,C_FORMAT)     # datetime.datetime(2018, 6, 17, 20, 45, 10)

    datetime.fromtimestamp(SECS)       # 类方法，返回本地datetime对象, datetime.datetime(2018, 6, 17, 20, 45, 10, 737000)
    datetime.utcfromtimestamp(SECS)    # 类方法， 返回UTC datetime对象

    DATE_TIME.ctime()                  # 返回日期字符串, 'Sun Jun 17 20:45:10 2018'

    DATE_TIME.isoformat(sep='T')       # 返回标准日期字符串, '2018-06-17T20:45:10'
    DATE_TIME.strftime(ISO_FORMAT)     # 返回指定格式的日期字符串, '2018-06-17 20:45:10'


    DATE_TIME - timedelta(days=1)      # 返回运算后的datetime对象, datetime.datetime(2018, 6, 16, 20, 45, 10)

    DATE_TIME.timetuple()              # 返回time对象的本地日期元组
    # time.struct_time(tm_year=2018,tm_mon=6,tm_mday=17,tm_hour=20,tm_min=45,tm_sec=10,tm_wday=6,tm_yday=168,tm_isdst=-1)
    timedelta.total_seconds()

    # Datetime对象减10分钟
    DATE_TIME = datetime.fromtimestamp((tm.mktime(DATE_TIME.timetuple())-600))  # datetime.datetime(2018, 6, 17, 20, 35, 10)

    # Datetime对象减10分钟
    ctup = tm.strptime(DATE_TIME.ctime(), C_FORMAT)
    DATE_TIME = datetime.fromtimestamp(tm.mktime(ctup)-600)        # datetime.datetime(2018, 6, 17, 20, 25, 10)


########################################################################
###  random
########################################################################
# 并非真正随机生成，系统可预测，os中的urandom类接近真正随机
def moduleRandom():
    import random
    seq = [1, 3, 7, 9, 8, 15]
    random.random()                    # 返回一个位于[0, 1]的随机数
    random.uniform(1, 10)              # 返回一个位于[1, 10]的随机数
    random.randrange(0,10,2)           # 返回一个位于range(start,stop,step)的随机数
    random.choice(seq)                 # 随机返回序列seq中的一个元素
    random.shuffle(seq)                # 就地打乱序列seq, <type 'list'>: [7, 3, 8, 9, 1, 15]
    random.sample(seq,5)               # 随机返回序列seq中5个不同位置的元素


########################################################################
###  numpy.array
########################################################################
def moduleNumpyArray():
    """
    ndarray, 多维同构数据

    arr =   0   1   2   3   4
            5   6   7   8   9
            ...
            90  91  92  93  94
            95  96  97  98  99
    """
    import numpy as np
    seq = np.arange(100)                # arange的生成性能优于range
    sep = np.arange(1,10,0.1)           # 指定步长 ，内置range函数步长不能为小数
    arr = seq.reshape(20, 5)            # 重构生成20*5数组（浅复制）
    arr = arr.copy()                    # 深复制

    arr1 = arr.T                        # 返回转置数组（浅复制）
    arr1 = arr[1:-1,1:3]                # 切片, 位于非首尾行、第2列和第3列的部分（浅复制）
    arr1 = arr[[1,3],:]                 # 选取多行（浅复制）
    arr1 = arr[[2,1,0],[1,2,0]]         # [11, 7, 0]选取(2, 1), (1, 2), (0, 0)处的元素(深复制)

    ele = arr[0][0]                     # 返回指定位置的副本
    ele = arr[0,0]                      # 同上, list类型该方式不可用

    arr1 = arr[arr>90]                  # 选取数组中所有大于90的元素, 返回一行数据-1*n型（深复制）
    arr1[arr1>0] = 1                    # 替换数组中大于0的元素为1
    arr1 = np.where(arr>90,100,0)       # 替换数组中元素大于90的为100、小于的为0（深复制）, 三元表达式
    arr1 = arr[(arr<10) | (arr>90)]     # 选取数组中大于10或小于90的所有元素, 1*n型(深复制)

    arr1 = np.delete(arr, range(18), axis=0)  # 返回arr去除前18行的副本
    arr1 = np.delete(arr, -1, axis=1)         # 返回arr去除最后一列的副本

    num = arr.size                       # 100, 元素数目
    num = arr.shape                      # (20, 5), 行列数元组
    num = arr.dtype                      # dtype('int32'), 元素数据类型
    num = arr.ndim                       # 2, 维度

    cmax = np.amax(arr, axis=0)         # 1*5, 列最大值(深复制)
    rmax = np.amax(arr, axis=1)         # 20*1, 行最大值(深复制)
    mean = np.mean(arr)                 # 计算所有元素均值
    cmean = np.mean(arr, axis=0)        # 列均值
    rmean = np.mean(arr, axis=1)        # 行均值
    sum = np.sum(arr)                   # 所有元素之和
    csum = np.sum(arr,0)                # 列和
                                        # 不同大小数组的运算称为广播
    sub = rmax - rmean                  # 两数组相同位置相减
    mul = rmax * rmean                  # 两数组相同位置相乘

    np.ones([2, 2])                     # [[1, 1],[1, 1]], 2*2全1array
    np.zeros([10, 10])                  # [[0, 0],[0, 0]], 2*2全0矩阵
    np.tile([1, 0], (3, 2))             # [[1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0]], 10*4, [1,0]行重复3次、列重复2次
    np.empty((2, 3))                    # 返回2行3列未初始化的垃圾数据
    np.unique([1, 1, 2, 3])             # [1, 2, 3]去重
    np.sort([[1, 2], [4, 2]],1)         # [[1, 2], [2, 4]], 仅对指定行排序(其它行不变), 返回副本

    np.random.rand(2, 2)                # 2*2的随机矩阵，随机值[0,1]
    np.random.randn(2,2)                # 2*2的正太分布矩阵, 均值为0, 方差为1
    np.random.uniform(0, 100)           # 生成指定范围内的一个数
    np.random.randint(0, 100)           # 生成指定范围内的一个整数
    np.random.normal(1, 0.1, (2, 3))    # 生成正态分布矩阵(给定均值、方差、维度)

    np.array([1,2,3]).astype('str')     # 转换数据类型为字符串型, 不能转换时溢出TypeError错误

    np.dot([1,2,3],[[1],[2],[3]])       # 矩阵运算shape(1,3) * shape(3,1) = shape(1)
    np.intersect1d(arr, [1,2,100])      # [1, 2]返回两数组中的公共元素, 1*n型列表
    np.union1d([[2],[1],[3]],[[1]])     # [1, 2, 3]返回两数组（元素类型相同）并集
    np.union1d([1,2,3],[1,4])           # [1, 2, 3, 4]
    np.in1d([[1,2],[3,4]],[1,2,4,5])    # [True, True, False, True]返回一个数组在另一个数组中是否存在的bool型列表

    np.vstack(([1,2],[3,4]))            # 垂直拼接(深复制)
    np.hstack(([1,2],[3,4]))            # 水平拼接(深复制)

    np.exp([1,2])                       # 每个元素求e的幂次方
    np.sqrt([2,4])                      # 每个元素开根号
    np.log([1,np.e])                    # 每个元素以e为底求对数, log2和10则分别以2和10为底

    from numpy.linalg import inv
    arrm = np.random.randn(5,5)
    arrm.T.dot(arrm)                    # 等价于a.T * a

    arrm = arrm.dot(inv(arrm))          # 矩阵*矩阵的逆, 并非得到单位矩阵, 可能以很小的值替代0元素
    arrm[arrm<1e-10] = 0                # 将较小的值置0


########################################################################
###  pandas.Series
########################################################################
def modulePandasSeries():
    import pandas as pd
    import numpy as np
    from pandas import Series

    cs = ['name', 'country', 'age']

    dataS = ['John', 'US', 26]
    dicS = dict(name='John', country='US', age=26)          # 生成Series类型时无序
    nonS = {'name':'John', 'country':'US', 'age':None}
    
    ds = Series(dicS)                  # 字典形式创建, 列序不定
    ds = Series(dataS,index=cs)        # 可自定义索引, 默认0开始递增

    dsIdx = ds.index                   # {Index}Index([u'name', u'country', u'age'], dtype='object')
    dsVal = ds.values                  # {ndarray}['John' 'US' 26] --浅复制
    dsVal[0] = 'new'                   # ds值改变
    ds['name'] = 'John'                # 字典形式为浅复制（原值改变）
    ds.name = 'Johe'                   # 成员方法为深复制（原值未改变）

    ds1 = ds[['name','country']]       # 两索引（深复制）
    ds1 = ds['country':'age']          # 两个索引（浅复制）

    ds1 = ds.drop('country')           # 返回删除指定索引的Series（深复制）
    
    ds1 = Series(nonS)
    ds2 = ds1[~pd.isnull(ds1)]          # 获取ds3无None的行
    ds2 = ds1.fillna('')                # 空白字符填充
    
    ds.sort_index()                     # index升序


def modulePandasDataFrame():
    """
    表格型结构, 面向行列操作平衡

    列为一个Series
    """
    import pandas as pd
    import numpy as np
    from pandas import DataFrame,Series

    cs = ['name', 'country', 'age']
    id = ['p1', 'p2', 'p3']
    dataF = [['John', 'US', 26],
             ['Jane', 'Japan', 24],
             ['Zhw', 'China', 26]]

    dicF = {'name':['John', 'Jane', 'ZhW'],
            'country':['US', 'Japan', 'China'],
            'age':[26, 24, 26]}

    df = DataFrame(dataF, index=id, columns=cs) # 多维列表初始化
    df = DataFrame(dicF, index=id)              # 字典初始化, 结果与上一致(列的顺序不定)

    dfIdx = df.index                            # Index([u'p1', u'p2', u'p3'], dtype='object')
                                                # index对象不可修改，使用到别处等价于继承
    dfCol = df.columns                          # Index([u'age', u'country', u'name'], dtype='object')
    dfVal = df.values                           # 返回全部元素值的array数组

    df_1 = df.T                                 # 返回转置，columns和index互换
    df_1 = df[df['age'] > 24]                   # age>24的所有行

    # loc、iloc、ix通过行标签、行号、行号或行标签索引
    df_1 = df.ix['p1']                          # 获取指定行(深复制)， Series
    df_1 = df.loc['p1']                         # 同上
    df_1 = df.ix[0]                             # 同上
    df_1 = df.iloc[0]                           # 同上

    df_1 = df.ix[['p1','p3'],:]                 # 获取索引为0和2的行（深复制），DataFrame
    df_1 = df.ix[[0,2],:]                       # 与上相同
    df_1 = df.ix[:,['name','age']]              # 获取指定列(深复制)
    df_1 = df[['name','age']]                   # 直接获取多列(深复制), DataFrame
    
    df_1 = df['name']                           # 获取指定列的引用（浅复制）, Series
    df_1[0] = 'Johe'                            # df被修改
    df.ix['p1','name'] = 'John'                 # df,df_1被修改
    names = df.name                             # 返回name列(浅复制), Series
    names[0] = 'name'                           # df被修改
    
    df_1 = df_1.reindex(['p1','p3','p2'])       # 重置行序
    df_1 = df_1.drop('p3')                      # 删除行索引为p3的行

    person = df[df['name'] == 'ZhW']            # 返回name符合条件的行(深复制), DataFrame
    age = df[df['name']=='ZhW']['age'].values[0]   # 26， Series的第一个值

    df['gender'] = ['M', 'M', 'F']              # 增加列
    del df['gender']                            # 删除列
    
    df1 = DataFrame([[1,2]],columns=['a','b'])
    df2 = DataFrame([[3,4]],columns=['c','a'])  
    
    # 行列同时匹配的元素进行运算
    df3 = df1 + df2         # values(5 NaN NaN), columns('a','b','c')
    df3 = df1 - df2         # values(-3 NaN NaN), columns('a','b','c')
    df3 = df1.reindex(columns=df2.columns, fill_value=0) # (0, 1) ('c', 'a')
    
    # 3*3, columns=[a,b,c], index=[0,1,2]
    df1 = DataFrame(np.arange(9).reshape(3,3),columns=list('abc'))
    f = lambda x:x.max() - x.min()
    df2 = df1.apply(f,axis=0)   # index=(a,b,c), value(6,6,6), 每列最大-最小
    df2 = df1.apply(f,axis=1)   # index=(0,1,2), value(2,2,2), 每行最大-最小
    f = lambda x:Series([x.min(), x.max()], index=['min', 'max'])
    df2 = df1.apply(f,axis=0)   # index=(min,max),columns=(a,b,c), 每列最大/小值
    df2 = df1.apply(f,axis=1)   # index=(0,1,2),columns=(min,max), 每行最大/小值
    
    df2 = df1.applymap(lambda x:x+10)   # 每个元素加10
    
    df1 = DataFrame(np.arange(9).reshape(3,3), \
                    index=list('012'), columns=list('bac'))
                    
    df1 = df1.reindex(['0','2','1'])                # 指定行序
    
    df2 = df1.sort_index(axis=0)                    # 按index(列)升序排列(深复制)
    df2 = df1.sort_index(axis=1, ascending=False)   # 按columns(行)逆序排列(深复制)
    
    df2 = df1.sort_index(by='b')                    # 按指定列升序排序(深复制)
    df2 = df1.sort_index(by=['a','b'])              # 多列排序
    
    df2.ix['0','a'] = 100 
