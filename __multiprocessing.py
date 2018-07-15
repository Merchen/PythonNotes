# -*- coding: utf-8 -*-
# 进程之间内存空间独立，开辟进程时reload文件，所有函数从新加载
# main中已执行部分不重新执行
import multiprocessing
import Queue
import pandas as pd
import numpy as np
import os
from copy import  deepcopy
from  time import time, sleep
from functools import partial


########################################################################
### process 开辟单进程
########################################################################
def _fun1Process(n, lock, value, arr):
    """不请求锁定可能出错，若value为Manager类型可避免"""
    lock.acquire()
    value.value += n
    for j in range(len(arr)):
        arr[j] += n
    lock.release()


def _process1(count, lock, value, arr):
    """更改共享变量"""
    process = []
    for i in range(count):  # 创建进程
        pro = multiprocessing.Process(target=_fun1Process, args=(i, lock, value, arr))
        process.append(pro)
    [pro.start() for pro in process]                # 启动进程
    [x.join() for x in process if x.is_alive()]     # 等待所有进程结束
    # process[0].terminate()                        # 强行终止


def _fun2Process(n, lock, dframe, queue):
    length = len(dframe)
    for i in range(length):
        dframe.iloc[i] += n
    try:
        lock.acquire()                              # 请求锁定，未获得请求的线程等待
        queue.put(dframe, block=False)              # 不等待插入
        # queue.put(dframe, block=True, timeout=1)  # 不成功时，等待timeout秒后重试一次
        lock.release()                              # 释放锁
    except Queue.Full:
        pass


def _process2(count, lock, dframe, queue):
    """并行处理，并将结果插入队列"""
    process = []
    for i in range(count):  # 创建进程
        pro = multiprocessing.Process(target=_fun2Process, args=(i, lock, dframe, queue))
        process.append(pro)
    [pro.start() for pro in process]            # 启动进程
    [x.join() for x in process if x.is_alive()] # 等待所有进程结束


def _fun3Process(queue):
    while True:
        try:
            print(len(queue.get(block=False)))
        except Queue.Empty:
            sleep(1)


def _process3(queue):
    """处理队列数据"""
    pro = multiprocessing.Process(target=_fun3Process, args=(queue,))
    pro.start()
    return pro


########################################################################
### pool
########################################################################
# 进程池未满时，自动创建进程执行函数，否则等待
def _fun1Pool(n, dframe):
    for j in range(len(dframe)):
        dframe.iloc[j] *= (10**n)
    return dframe.iat[0, 0]


def _fun2Pool(ser):
    res = 0
    for i in ser:
        res += i
    return 1.*res/len(ser)


def _yield(dframe):
    length = len(dframe)
    for i in range(length):
        yield dframe.iloc[i]


def _dframe_tolist(dframe):
    """
    Dataframe(100000*10)转为行迭代对象
    若使用遍历方式转化，需根据行列数权衡遍历方向
    """

    print(time())

    # args = list(_yield(dframe))                         # 生成器构造DataFrame行列表--8s
    # print(time())
    #
    # args = [dframe.loc[id] for id in dframe.index]      # 解析式构造DataFrame行列表--10s
    # print(time())
    #
    # args = []                                           # 循环构造DataFrame行列表--8s
    # for i in dframe.index:
    #     args.append(dframe.iloc[i])
    # print(time())
    #
    # args = np.array(dframe).tolist()                    # 通过ndarray转换为行列表--0.3s
    # print(time())
    #
    # args = []                                           # 循环遍历--8s
    # for id in dframe.index:
    #     args.append(dframe.iloc[id])
    # print(time())

    # 数组在for循环中按行输出
    args = np.zeros(dframe.shape)                           # 使用数组赋值，DataFrame按列索引--0.001s
    for col in dframe:                                      # 默认按列遍历
        args[:, col] = dframe[col]
    args = list(args)
    print(time())

def _pool1(count, dframe):
    """async异步处理, 结果存入列表"""
    pool = multiprocessing.Pool(processes=count)
    res = []
    for i in range(count):
        res.append(pool.apply_async(_fun1Pool, args=(i, dframe)))       # 参数从新开辟内存空间
    pool.close()    # 阻止继续添加进程
    pool.join()     # 等待所有进程结束
    for x in res:
        print(x.get())


def _pool2(count, dframe):
    """map处理"""
    pool = multiprocessing.Pool(processes=count)
    # map多参数时若仅有一个参数为迭代量而其他参数为固定值，可使用partial方法固定其它参数
    res = pool.map(partial(_fun1Pool, dframe=dframe), range(count))
    pool.close()    # 阻止继续添加进程
    pool.join()     # 等待所有进程结束
    for x in res:
        print(x)


def _poo3(count, dframe):
    """map处理，多参下使用构造iterator"""
    pool = multiprocessing.Pool(processes=count)
    print(time())

    args = pool.map(_fun2Pool, args)                    # pool的map函数--0.8s
    print(time())

    args = map(_fun2Pool, args)                         # 内置map函数--0.1s
    print(time())


if __name__ == '__main__':

    dframe = pd.DataFrame(np.random.randn(1e6).reshape((1e5, 1e1)))
    cores = multiprocessing.cpu_count()         # 计算机核心数
    queue = multiprocessing.Queue()             # 多进程共享队列
    lock = multiprocessing.Lock()               # 线程锁对象
    value = multiprocessing.Value('d', 0.0)     # 共享内存，最好避免使用
    arr = multiprocessing.Array('i', range(3))

    _dframe_tolist(dframe)

    # Manager对象提供更高层次的封装，Manager对象控制一个server进程，保证多进程间数据通信安全
    # Manager启动较耗时，约1秒
    with multiprocessing.Manager() as man:
        lockManager = man.Lock()
        queueManager = man.Queue()
        valueManager = man.Value('d', 0.0)
        arrManager = man.Array('i', range(3))

        # _process1(cores, lock, value, arr)
        # print(value.value, arr[:])                  # (6.0, [6, 7, 8])
        # _process1(cores, lock, valueManager, arrManager)
        # print(valueManager.value, arr[:])           # (6.0, [6, 7, 8])


        # queue若非空则进程不终止，Manager对象可避免
        # pro = _process3(queue)                      # 处理队列数据
        # _process2(cores, lock, dframe, queue)       # 向队列插入数据
        # while not queue.empty():                    # 等待队列为空
        #     sleep(1)
        # pro.terminate()                             # 强制结束进程



        # _pool1(cores, dframe)                       # 所有变量重新分配内存空间


        # _pool2(cores, dframe)


        # _poo3(cores, dframe)





