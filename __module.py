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
    os.startfile('')                #0 执行程序，不受限空白,os.startfile(r'C:\Program Files\Internet Explorer\iexplore.exe')

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
###  Operator
########################################################################
def fun1():
    from operator import itemgetter
    metro_data = [('Tokyo', 'JP', 36.933),
                  ('Mexico City', 'MX', 20.142),
                  ('Sao Paulo', 'BR', 19.649)]

    # 根据元组的某个字段排序
    cities = [city[:2] for city in sorted(metro_data, key=itemgetter(1))]
    # [('Sao Paulo', 'BR'), ('Tokyo', 'JP'), ('Mexico City', 'MX')]

    cities = [city[:2] for city in sorted(metro_data, key=lambda x:x[1])]
    # [('Sao Paulo', 'BR'), ('Tokyo', 'JP'), ('Mexico City', 'MX')]

    # 构建函数提取元组数值
    cities = [itemgetter(1, 0)(city) for city in metro_data]
    # [('JP', 'Tokyo'), ('MX', 'Mexico City'), ('BR', 'Sao Paulo')]

    cities = list(map(lambda x:(x[1], x[0]), metro_data))
    # [('JP', 'Tokyo'), ('MX', 'Mexico City'), ('BR', 'Sao Paulo')]


def fun2():
    from operator import attrgetter
    from collections import namedtuple

    metro_data = [('Tokyo', 'JP', (36.933, 139.671)),
                  ('Mexico City', 'MX', (20.142, 77.554)),
                  ('Sao Paulo', 'BR', (19.649, 45.254))]
    LatLong = namedtuple('latLong', 'lat long')
    Metro = namedtuple('metro', 'name cc coord')

    metro_areas = [Metro(name, cc, LatLong(lat, long)) for name, cc, (lat, long) in metro_data]

    print(metro_areas[1])
    # metro(name='Mexico City', cc='MX', coord=latLong(lat=20.142, long=77.554))

    cities = [city[:2] for city in sorted(metro_areas, key=attrgetter('coord.lat'))]
    # [('Sao Paulo', 'BR'), ('Mexico City', 'MX'), ('Tokyo', 'JP')]