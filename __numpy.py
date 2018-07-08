# -*- coding: utf-8 -*-

########################################################################
###  numpy.array
########################################################################
def moduleNumpyArray():
    """
    ndarray, 多维同构数据

    arr =   0   1   2   3   4
            5   6   7   8   9
            ...
            90  91  92  93  94
            95  96  97  98  99
    """
    import numpy as np
    seq = np.arange(100)  # arange的生成性能优于range
    sep = np.arange(1, 10, 0.1)  # 指定步长 ，内置range函数步长不能为小数
    arr = seq.reshape(20, 5)  # 重构生成20*5数组（浅复制）
    arr = arr.copy()  # 深复制

    arr1 = arr.T  # 返回转置数组（浅复制）
    arr1 = arr[1:-1, 1:3]  # 切片, 位于非首尾行、第2列和第3列的部分（浅复制）
    arr1 = arr[[1, 3], :]  # 选取多行（浅复制）
    arr1 = arr[[2, 1, 0], [1, 2, 0]]  # [11, 7, 0]选取(2, 1), (1, 2), (0, 0)处的元素(深复制)

    ele = arr[0][0]  # 返回指定位置的副本
    ele = arr[0, 0]  # 同上, list类型该方式不可用

    arr1 = arr[arr > 90]  # 选取数组中所有大于90的元素, 返回一行数据-1*n型（深复制）
    arr1[arr1 > 0] = 1  # 替换数组中大于0的元素为1
    arr1 = np.where(arr > 90, 100, 0)  # 替换数组中元素大于90的为100、小于的为0（深复制）, 三元表达式
    arr1 = arr[(arr < 10) | (arr > 90)]  # 选取数组中大于10或小于90的所有元素, 1*n型(深复制)

    arr1 = np.delete(arr, range(18), axis=0)  # 返回arr去除前18行的副本
    arr1 = np.delete(arr, -1, axis=1)  # 返回arr去除最后一列的副本

    num = arr.size  # 100, 元素数目
    num = arr.shape  # (20, 5), 行列数元组
    num = arr.dtype  # dtype('int32'), 元素数据类型
    num = arr.ndim  # 2, 维度

    cmax = np.amax(arr, axis=0)  # 1*5, 列最大值(深复制)
    rmax = np.amax(arr, axis=1)  # 20*1, 行最大值(深复制)
    mean = np.mean(arr)  # 计算所有元素均值
    cmean = np.mean(arr, axis=0)  # 列均值
    rmean = np.mean(arr, axis=1)  # 行均值
    sum = np.sum(arr)  # 所有元素之和
    csum = np.sum(arr, 0)  # 列和
    # 不同大小数组的运算称为广播
    sub = rmax - rmean  # 两数组相同位置相减
    mul = rmax * rmean  # 两数组相同位置相乘

    np.ones([2, 2])  # [[1, 1],[1, 1]], 2*2全1array
    np.zeros([10, 10])  # [[0, 0],[0, 0]], 2*2全0矩阵
    np.tile([1, 0], (3, 2))  # [[1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0]], 10*4, [1,0]行重复3次、列重复2次
    np.empty((2, 3))  # 返回2行3列未初始化的垃圾数据
    np.unique([1, 1, 2, 3])  # [1, 2, 3]去重
    np.sort([[1, 2], [4, 2]], 1)  # [[1, 2], [2, 4]], 仅对指定行排序(其它行不变), 返回副本

    np.random.rand(2, 2)  # 2*2的随机矩阵，随机值[0,1]
    np.random.randn(2, 2)  # 2*2的正太分布矩阵, 均值为0, 方差为1
    np.random.uniform(0, 100)  # 生成指定范围内的一个数
    np.random.randint(0, 100)  # 生成指定范围内的一个整数
    np.random.normal(1, 0.1, (2, 3))  # 生成正态分布矩阵(给定均值、方差、维度)

    np.array([1, 2, 3]).astype('str')  # 转换数据类型为字符串型, 不能转换时溢出TypeError错误

    np.dot([1, 2, 3], [[1], [2], [3]])  # 矩阵运算shape(1,3) * shape(3,1) = shape(1)
    np.intersect1d(arr, [1, 2, 100])  # [1, 2]返回两数组中的公共元素, 1*n型列表
    np.union1d([[2], [1], [3]], [[1]])  # [1, 2, 3]返回两数组（元素类型相同）并集
    np.union1d([1, 2, 3], [1, 4])  # [1, 2, 3, 4]
    np.in1d([[1, 2], [3, 4]], [1, 2, 4, 5])  # [True, True, False, True]返回一个数组在另一个数组中是否存在的bool型列表

    np.vstack(([1, 2], [3, 4]))  # 垂直拼接(深复制)
    np.hstack(([1, 2], [3, 4]))  # 水平拼接(深复制)

    np.exp([1, 2])  # 每个元素求e的幂次方
    np.sqrt([2, 4])  # 每个元素开根号
    np.log([1, np.e])  # 每个元素以e为底求对数, log2和10则分别以2和10为底

    from numpy.linalg import inv
    arrm = np.random.randn(5, 5)
    arrm.T.dot(arrm)  # 等价于a.T * a

    arrm = arrm.dot(inv(arrm))  # 矩阵*矩阵的逆, 并非得到单位矩阵, 可能以很小的值替代0元素
    arrm[arrm < 1e-10] = 0  # 将较小的值置0
