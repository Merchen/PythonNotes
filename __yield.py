# -*- coding: utf-8 -*-

import math

"""

next()和.next()与.send(None)等价8

第一次必须.send(None)，因为此时生成器未停留在yield表达式，表达式还不能接受参数
每次send数据后，yield表达式左值立即获得send参数，函数返回下个一yield值，并暂停在此处
"""


def isprime(number):
    """
    检查是否为素数
    :param number:
    :return:
    """
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

# -------------------------------------------------------------------------
f = get_priems()
f.send(None)        # 遇到第一个yield表达式时暂停，并返回yield的值
num = f.send(10)    # 将send参数(10)赋给yield表达式左值，返回第二个yield的值(11)
# -------------------------------------------------------------------------


msg1,msg2 = 0, 0

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