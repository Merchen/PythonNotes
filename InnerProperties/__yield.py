# -*- coding: utf-8 -*-
import itertools
from math import sqrt
# itertools.count生成无穷等差数列
#
# next()和.next()与.send(None)等价
#
# 第一次必须.send(None)，因为此时生成器未停留在yield表达式，表达式还不能接受参数
# 每次send数据后，yield表达式左值立即获得send参数，函数返回下个一yield值，并暂停在此处


def _yield():
    for i in range(5):
        yield i


iterator1 = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
# for i in iterator1:
#     print(i)


# =======================================================================
"""生成素数"""
def fun1():
    def isprime(number):
        # if number > 1:
        #     if number == 2:
        #         return True
        #     if number % 2 == 0:
        #         return False
        #     for current in range(3, int(sqrt(number) + 1), 2):
        #         if number % current == 0:
        #             return False
        #     return True
        # return False
        return number > 1 and (number == 2 or not number % 2 == 0) and all(
            number % i for i in range(3, int(sqrt(number) + 1), 2))

    def ypriems(n):
        num = 2
        for i in range(n):
            while True:
                if isprime(num):
                    break
                num += 1
            yield num
            num += 1

    # for i in ypriems(5):
    #     print(i)

    def gpriems():
        msgnum = 2
        while True:
            if isprime(msgnum):
                # 函数获得yield后的值，yield表达式左值获得send参数值
                msgnum = yield msgnum
            else:
                msgnum += 1

    f = gpriems()
    # 遇到第一个yield表达式时暂停

    print(f.send(None))
    # 2
    # 第一次无法接受参数, 必须发送None
    # 返回2, 并停留在yield表达式

    print(f.send(100))
    # 101
    # 将100赋给yield表达式左值，遇到第二个yield返回右值(101)后暂停


# =======================================================================
"""拆分嵌套列表"""
def fun2():
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