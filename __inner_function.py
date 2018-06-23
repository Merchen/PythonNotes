# -*- coding: utf-8 -*-
""""""
# -------------------------------------------------------------------------
"""此部分内容存储在__doc__

函数局部空间，记录函数参数和局部变量;
模块全局空间，记录函数、类、其他导入的模块及模块级变量;
内置空间，存放内置函数和异常;
Python查看变量顺序：函数局部空间-->模块全局空间-->内置空间

__file__    自身文件名，包含绝对路径
__doc__     存储文件开头注释、或函数开头注释，help(fanme)
__name__    当前文件执行时为'__main__'，被调用时为自身文件名
__bases__   查看继承

issubclass(): 检查一个类是否是一个类的继承
isinstance(): 检查是否是特定类的实例

dir()       显示模块/对象的所有属性
help()      显示模块说明
"""
__all__ = []  # 列表中包含from module import * 可直接导入的内容，用于变量过滤

# ----------------------------------------from module import * 可直接导入的内容，用于变量过滤---------------------------------
"""全局变量，外部文件可引用"""

G_NUM = 10
G_STR = 'str'


# -------------------------------------------------------------------------
"""locals() globals()"""
# 可通过globals()直接修改全局变量的值
# 函数内部的locals()函数，仅记录引用之前函数的局部变量

def add(arg=2):
    """Function Manual"""
    global G_NUM  # 声明引用全局变量，否则为局部变量
    print(globals().has_key('arg')) # False, 不存在局部变量a

    print(globals(),locals())       # 显示全局空间，G_NUM,G_STR,__name__,__doc__,等
                                    # 显示局部空间，{'a':1, 'arg':2}
    locals()['G_NUM'] = 1           # 副本形式，更改无效,G_NUM = 10
    globals()['G_NUM'] = 1          # 引用形式，更改有效,G_NUM = 1

locals()['G_NUM'] = 5       # 模块内调用local(),可修改全局变量
globals()['G_NUM'] = 10     # G_NUM = 20

add_doc = add.__doc__       # Function Manual,help(add)将显示更多信息

# -------------------------------------------------------------------------
"""dir"""
# dir(module)   返回模块全部可用方法名称列表
# dir(int)      返回int对象可用方法名称列表

# -------------------------------------------------------------------------
"""exec与eval"""

scope = {'y': 3}
exec 'x=2' in scope     # 执行一条字符串语句,scope['x']=2
eval('x*y', scope)      # 计算字符串表达式，并返回结果值,6


# -------------------------------------------------------------------------
"""map"""
# map(function, sequence, *sequence_1)
# map(function, sequence[, sequence, ...]) -> list  对列表中的每个元素执行function功能，并返回列表
# lambda parameters:express 冒号前为参数（可以有多个），冒号右边为返回值，等价于返回一种函数指针

def func1(x): return x * x              # lambda x:x*x
m1 = map(func1,[1, 2, 3 ,4])            # [1, 4, 9， 16]

m2 = map(lambda x:x*x, [1, 2, 3 ,4])    # [1, 4, 9， 16]
m3 = [x*x for x in [1, 2, 3 ,4]]        # [1, 4, 9， 16]


# -------------------------------------------------------------------------
"""reduce"""
# reduce(function, sequence, initial=None)
# reduce(function, sequence[, initial]) -> value    使用函数返回值和列表中未迭代元素，执行函数（二元参数）功能

def func2(x, y): return x + y       # lambda x,y:x+y
m4 = reduce(func2,[1, 2, 3 ,4])     # 10


# -------------------------------------------------------------------------
"""filter"""
# filter(function_or_none, sequence)
# filter(function or None, sequence) -> list, tuple, or string      对各元素执行函数，返回结果为True的元素组成的列表等

def func3(x):  return x > 2                 # lambda x:x>2
print(filter(func3,[1, 2, 3 ,4]))           # [3, 4]
print([x for x in [1, 2, 3 ,4] if x > 2])   # [3, 4]
