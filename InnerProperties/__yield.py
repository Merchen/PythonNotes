# -*- coding: utf-8 -*-
import itertools
from collections import namedtuple
from math import sqrt

def _yield():
    for i in range(5):
        yield i


iterator1 = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
# for i in iterator1:
#     print(i)

# =======================================================================
"""生成素数"""
def prime():
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

    for i in ypriems(5):
        print(i)

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
"""协程"""
# 协程: 一个过程, 这个过程与调用方协作, 产出由调用方提供的值
#
# next()和.next()与.send(None)等价
# 仅当生成器在yield处暂停时才可发送非None值
# 初始时yield表达式不能接受参数, 必须.send(None)或使用next方法
#
# send执行后，yield表达式左值接收send参数，程序执行至下一个yield表达式暂停
# 并将此时的yield右值作为函数返回值

Result = namedtuple('Result', 'count average')


def averager():
    """生成器, 计算移动平均值"""
    count, total, average = 0, 0., 0
    while True:
        try:
            term = yield average
            if term is None:
                break
        except StopIteration:
            print('StopIteration')
        except GeneratorExit:
            print('GeneratorExit')

            # 抛出的异常不再被捕获
            raise StopIteration
        else:
            total += term
            count += 1
            average = total/count
    # python3.3之前不允许含返回值
    # 返回值赋给StopIteration
    return Result(count, average)


def _TestAverager():
    """生成器测试"""
    avg = averager()
    avg.send(None)
    print(avg.send(10))
    # 10.0
    print(avg.send(20))
    # 15.0

    # yield处抛出指定异常
    # 正常处理异常时, throw语句获得下一个yield表达式的值
    print(avg.throw(StopIteration))
    # StopIteration
    # 15.0

    # yield处抛出GeneratorExit异常
    # 未处理GeneratorExit或抛出StopIteration, 程序正常退出
    # 否则抛出RuntimeError异常
    try:
        avg.send(None)
    except StopIteration as exc:
        print(exc.value)
        # Result(count=2, average=15.0)


# yield from <iterable>(子生成器)
# yield from 打开双向通道, 连接最外层调用与最内层子生成器
# 不用通过中间协程即可处理异常、产出值
# 支持实现了__next__、send、close和throw的生成器
#
# 结构:  调用方 >> 委派生成器(管道) >> 子生成器(简单迭代器, 仅实现__next__方法)
# 委派生成器在yield from处暂停, 调用方将数据直接发送给子生成器, 子生成器把产出值发给调用方
#
def _TestYieldFrom():
    yield from 'AB'
    yield from range(3)


# print(list(_TestYieldFrom()))
# ['A', 'B', 0, 1, 2]


def main():
    """调用方"""

    def grouper(results, key):
        """
        委派生成器(等价于管道), 无法获取send的参数

        子生成器抛出StopIteration时, yield from恢复运行
        yield from的左值为StopIteration.value

        传入GeneratorExit异常或close方法, 将调用子生成器的close方法(无close则抛出GeneratorExit)
        若传入除GeneratorExit外的异常, 均throw给子生成器
        """
        while True:
            # 接收averager()的return值
            results[key] = yield from averager()

    data = {'girls': [10, 20, 30], 'boys': [40, 50, 60]}
    results = {}

    for key, values in data.items():
        # 获取生成器对象
        group = grouper(results, key)
        next(group)
        for value in values:
            # 接收averager()的yield值
            _ = group.send(value)
        group.send(None)
    print(results)
    # {'girls': Result(count=3, average=20.0), 'boys': Result(count=3, average=50.0)}

main()


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
        global msg1, msg2
        for sublist in nested:
            if isinstance(sublist, list):
                # flatten(sublist)             # 不可替代下方for循环，此句不重新建立变量存储空间，与continue效果一致
                for ele in flatten(sublist):   # r0
                    msg2 = yield ele           # r1,用于内层循环的yield，传值给外部
            else:
                msg1 = yield sublist           # r2,用于外层循环的yield，传值给外部或上一层递归调用

    a = ['aaaa',['bbbb','cccc'],'eeee']
    f = flatten(a)
    _ = f.send(None)   # 外层循环在r2暂停，函数返回'aaaa'
    _ = f.send(100)    # msg1=100，进入内层循环['bbbb','cccc']，内层在r2暂停并向外层r0返回'bbbb'，外层在r1暂停并返回'bbbb'
    _ = f.send(200)    # 外层r1获取send参数，msg2=200, 再次进入内层r2，msg1=None, 继续执行内层循环
                        # 内层在r2暂停并向外层r0返回'cccc'，外层在r1暂停返回'cccc'
    _ = f.send(300)    # 外层r1获取send参数，msg2=300, 再次进入内层r2行, msg1=None, 跳出内层循环，外层在r2暂停并返回'eeee'
