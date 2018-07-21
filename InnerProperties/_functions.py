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
# True
all([1, None, 3])
# False
any([1, None, 3])
# True


# =======================================================================
"""yield"""
# next()和.next()与.send(None)等价
#
# 第一次必须.send(None)，因为此时生成器未停留在yield表达式，表达式还不能接受参数
# 每次send数据后，yield表达式左值立即获得send参数，函数返回下个一yield值，并暂停在此处
def fun9():
    import math

    # 解析构造生成器表达式
    express = (i for i in range(10))

    def isprime(number):
        """检查是否为素数"""
        if number > 1:
            if number == 2:
                return True
            if number % 2 == 0:
                return False
            for current in range(3, int(math.sqrt(number) + 1), 2):
                if number % current == 0:
                    return False
            return True
        return False


    def get_priems():
        """
        获取大于等于发送数字的素数
        :return:
        """
        msgnum = 0
        while True:
            if isprime(msgnum):
                # 函数获得yield后的值，yield表达式左值获得send参数值
                msgnum = yield msgnum
            else:
                msgnum += 1


    f = get_priems()
    f.send(None)        # 遇到第一个yield表达式时暂停，并返回yield的值
    num = f.send(10)    # 将send参数(10)赋给yield表达式左值，返回第二个yield的值(11)

    msg1, msg2 = 0, 0

    def flatten(nested):
        """
        递归拆分嵌套列表

        :param nested: 嵌套列表
        :return: 包含全部元素且不含列表嵌套的列表
        """
        global msg1,msg2
        for sublist in nested:
            if isinstance(sublist,list):
                # flatten(sublist)             # 不可替代下方for循环，此句不重新建立变量存储空间，与continue效果一致
                for ele in flatten(sublist):   # r0
                    msg2 = yield ele           # r1,用于内层循环的yield，传值给外部
            else:
                msg1 = yield sublist           # r2,用于外层循环的yield，传值给外部或上一层递归调用

    a = ['aaaa',['bbbb','cccc'],'eeee']
    f = flatten(a)
    n1 = f.send(None)   # 外层循环在r2暂停，函数返回'aaaa'
    n2 = f.send(100)    # msg1=100，进入内层循环['bbbb','cccc']，内层在r2暂停并向外层r0返回'bbbb'，外层在r1暂停并返回'bbbb'
    n3 = f.send(200)    # 外层r1获取send参数，msg2=200, 再次进入内层r2，msg1=None, 继续执行内层循环
                        # 内层在r2暂停并向外层r0返回'cccc'，外层在r1暂停返回'cccc'
    n4 = f.send(300)    # 外层r1获取send参数，msg2=300, 再次进入内层r2行, msg1=None, 跳出内层循环，外层在r2暂停并返回'eeee'