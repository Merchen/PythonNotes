# -*- coding: utf-8 -*-
import time

"""
issubclass(): 检查一个类是否是一个类的继承
isinstance(): 检查是否是特定类的实例

dir()       显示模块/对象的所有属性
help()      显示模块说明
"""

# 列表中包含from module import * 可直接导入的内容，用于变量过滤
__all__ = []


# =======================================================================
"""id"""
# Return the identity of an object.
a = [1, 2, 4]
b = a
id(a)
# 753407719176
id(b)
# 753407719176, 引用变量相同


# =======================================================================
"""dir"""
# 返回模块全部可用方法名称列表
dir(time)
# ['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__',
# '__spec__', 'altzone', 'asctime', 'clock', 'ctime', 'daylight',...]

# 返回int对象可用方法名称列表
dir(int)


# =======================================================================
"""format"""
# 对象格式化, 返回str格式
format(12.23, '.3f')
# 12.230
format(2/3, '.2%')
# '66.67%'
format(42, 'b')
# '101010'

# =======================================================================
"""eval/exec"""
#
scope = {'y': 3}

exec("scope['x'] = 2")
# {'y': 3, 'x': 2}

eval('x*y', scope)
# 6


# =======================================================================
"""map"""
# 对列表中的每个元素执行function功能，并返回列表
# map(function, sequence[, sequence, ...]) -> list
# 冒号前为参数（可以有多个），冒号右边为返回值，等价于返回一种函数指针
map(lambda x: x * x, [1, 2, 3, 4])
# [1, 4, 9， 16]

m3 = [x * x for x in [1, 2, 3, 4]]
# [1, 4, 9， 16]


# =======================================================================
"""reduce"""
# 使用函数返回值和列表中未迭代元素，执行函数（二元参数）功能
# reduce(function, sequence[, initial]) -> value
from functools import reduce
from operator import add

reduce(lambda x, y: x + y, [1, 2, 3, 4])
# 10
reduce(add, [1, 2, 3, 4])
# 10


# =======================================================================
"""filter"""
# 对各元素执行函数，返回结果为True的元素组成的列表等
# filter(function or None, sequence) -> list, tuple, or string
list(filter(lambda x: x > 2, [1, 2, 3, 4]))
# [x for x in [1, 2, 3, 4] if x > 2]


# =======================================================================
"""sorted"""
# 高阶函数，可将函数作为参数
fruits = ['apple', 'cherry', 'banana', 'strawberry']

sorted(fruits, key=len)
# ['apple', 'cherry', 'banana', 'strawb erry']

sorted(fruits, key=lambda x:x[::-1])
# ['banana', 'apple', 'strawberry', 'cherry'], 末尾字母排序


# =======================================================================
"""all/any"""
#
all([1, 2, 3])
# True, 全真则真

all([1, None, 3])
# False, 有假则假

any([1, None, 3])
# True, 有真则真
