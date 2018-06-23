# -*- coding: utf-8 -*-

########################################################################
###  环境变量
########################################################################
#
# sys.path包含编译系统环境变量，放置在site-packages内的文件任何用户均可加载（需管理员权限）
# 添加sys.path.append()添加自定义环境变量，此方法仅一次有效
#
# windows新建系统环境变量:
#     variable name: PYTHONPATH, 变量中添加路径即可，永久有效


########################################################################
###  模块与包
########################################################################
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


"""标准模板库(Standard Tamplate Library)"""
#
########################################################################
###  sys    os
########################################################################
# import os
# import sys

# sys.argv          包含向Python解释器传递的参数，包括脚本名
# sys.exit          退出主程序

# os.system()       执行程序，受限于空白(必须使用双引号包围)，os.system(r'C:\"Program Files"\"Internet Explorer"\iexplore.exe')
# os.startfile      执行程序，不受限空白,os.startfile(r'C:\Program Files\Internet Explorer\iexplore.exe')

# os.path.listdir('dir')        获取目录下的全部文件名称
# os.path.walk('dir')           递归获取目录下所有文件和目录名称，返回元组path,dirnames,filenames
# os.path.basename(__file__)    返回当前文件名称
# os.path.dirname(__file__)     返回当前文件所在目录（不含文件名）
# os.path.abspath(__file__)     返回当前文件绝地路径（含文件名）
# os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))    # 获取上级目录

########################################################################
###  heap
########################################################################
#
from heapq import *

import time

heap, data = [], [0, 4, 5, 6, 3, 2, 1, 7, 8, 9]

for n in data:                  # heapify(data)列表快速堆化
    heappush(heap,n)            # 压入堆, heap = [0, 3, 1, 6, 4, 5, 2, 7, 8, 9]

assert heapreplace(heap,6) == 0 # 弹出最小元素，并压入新元素

while len(heap):
    heappop(heap)               # 弹出堆,[1,2,3,4,5,6,6,7,8,9]


########################################################################
###  deque   OrderedDict    Counter
########################################################################
#
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