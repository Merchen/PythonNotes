# encoding: UTF-8

import numpy as np

"""numpy"""
########################################################################
###  numpy.array
########################################################################
#
# arr.copy()      返回深复制数组

seq = np.arange(100)                # arange的生成性能优于range
arr = seq.reshape(20, 5)            # 重构生成20*5数组（浅复制）
are = arr.copy()                    # 深复制
arr1 = arr[1:-1,1:3]                # 切片, 位于非首尾行、第2列和第3列的部分（浅复制）
arr2 = arr[[1,3],:]                 # 选取多行
arr3 = arr[[1,2],[1,2]]             

arr2 = arr[arr>90]                  # 选取数组中所有大于90的元素, 1*n型（深复制）
arr2[arr2>0] = 1                    # 替换数组中大于0的元素为1
arr3 = np.where(arr>90,100,0)       # 替换数组中元素大于90的为100、小于的为0（深复制）

np.delete(arr3, range(18), axis=0)  # 删除前1行(深复制)
np.delete(arr3, -1, axis=1)         # 删除最后一列（深复制）

n1 = arr.size                       # 100, 元素数目
n2 = arr.shape[0]                   # 20, 行数
n3 = arr.shape[1]                   # 5, 列数
n4 = arr.dtype                      # dtype('int32'), 元素数据类型
n5 = arr.ndim                       # 2, 维度

cmax = np.amax(arr, axis=0)         # 1*5, 列最大值(深复制)
rmax = np.amax(arr, axis=1)         # 20*1, 行最大值(深复制)
cmean = np.mean(arr, axis=0)        # 列均值
rmean = np.mean(arr, axis=1)        # 行均值
sub = rmax - rmean                  # 数组相减
mul = rmax * rmean                  # 相同位置相乘

np.ones([2, 2])                     # [[1, 1],[1, 1]], 2*2全1矩阵
np.zeros([10, 10])                  # [[0, 0],[0, 0]], 2*2全0矩阵
np.tile([1, 0], (3, 2))             # [[1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0]], 10*4, [1,0]行重复3次、列重复2次
np.random.rand(2, 2)                # 10*10的随机矩阵，随机值[0,1]
np.random.uniform(0, 100)           # 生成指定范围内的一个数
np.random.randint(0, 100)           # 生成指定范围内的一个整数
np.random.normal(1, 0.1, (2, 3))    # 生成正态分布矩阵(给定均值、方差、维度)

np.dot([1,2,3],[[1],[2],[3]])       # 矩阵运算shape(1,3) * shape(3,1) = shape(1)

np.vstack(([1,2],[3,4]))            # 垂直拼接(深复制)
np.hstack(([1,2],[3,4]))            # 水平拼接(深复制)


