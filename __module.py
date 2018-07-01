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
def moduleNumpy():
    import numpy as np
    seq = np.arange(100)                # arange的生成性能优于range
    sep = np.arange(1,10,0.1)           # 指定步长 ，内置range函数步长不能为小数
    arr = seq.reshape(20, 5)            # 重构生成20*5数组（浅复制）
    are = arr.copy()                    # 深复制
    arr1 = arr[1:-1,1:3]                # 切片, 位于非首尾行、第2列和第3列的部分（浅复制）
    arr2 = arr[[1,3],:]                 # 选取多行
    arr3 = arr[[1,2],[1,2]]

    arr2 = arr[arr>90]                  # 选取数组中所有大于90的元素, 1*n型（深复制）
    arr2[arr2>0] = 1                    # 替换数组中大于0的元素为1
    arr3 = np.where(arr>90,100,0)       # 替换数组中元素大于90的为100、小于的为0（深复制）

    np.delete(arr3, range(18), axis=0)  # 删除前1行(深复制)
    np.delete(arr3, -1, axis=1)         # 删除最后一列（深复制）

    n1 = arr.size                       # 100, 元素数目
    n2 = arr.shape[0]                   # 20, 行数
    n3 = arr.shape[1]                   # 5, 列数
    n4 = arr.dtype                      # dtype('int32'), 元素数据类型
    n5 = arr.ndim                       # 2, 维度

    cmax = np.amax(arr, axis=0)         # 1*5, 列最大值(深复制)
    rmax = np.amax(arr, axis=1)         # 20*1, 行最大值(深复制)
    cmean = np.mean(arr, axis=0)        # 列均值
    rmean = np.mean(arr, axis=1)        # 行均值
    sub = rmax - rmean                  # 数组相减
    mul = rmax * rmean                  # 相同位置相乘

    np.ones([2, 2])                     # [[1, 1],[1, 1]], 2*2全1矩阵
    np.zeros([10, 10])                  # [[0, 0],[0, 0]], 2*2全0矩阵
    np.tile([1, 0], (3, 2))             # [[1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0]], 10*4, [1,0]行重复3次、列重复2次
    np.random.rand(2, 2)                # 10*10的随机矩阵，随机值[0,1]
    np.random.uniform(0, 100)           # 生成指定范围内的一个数
    np.random.randint(0, 100)           # 生成指定范围内的一个整数
    np.random.normal(1, 0.1, (2, 3))    # 生成正态分布矩阵(给定均值、方差、维度)

    np.dot([1,2,3],[[1],[2],[3]])       # 矩阵运算shape(1,3) * shape(3,1) = shape(1)

    np.vstack(([1,2],[3,4]))            # 垂直拼接(深复制)
    np.hstack(([1,2],[3,4]))            # 水平拼接(深复制)
