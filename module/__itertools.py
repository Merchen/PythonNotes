# -*- coding: utf-8 -*-

import itertools
import operator

a = [0, 1, 2, 3, 4, 5]
b = [True, False, True, False, True, False]

fun = lambda x: x % 2 == 0
# 偶数为真
# fun(a) = [True, False, True, False, True, False]


# =======================================================================
"""compress"""
# 并行迭代两个可迭代对象, 返回b为True对应位置的a元素
list(itertools.compress(a, b))
# [0, 2, 4]


# =======================================================================
"""filterfalse"""
# 与filter函数作用相反, 返回fun(a)为False的a元素
list(itertools.filterfalse(fun, a))
# [1, 3, 5]
list(filter(fun, a))
# [0, 2, 4]


# =======================================================================
"""dropwhile"""
# 跳过fun(a)为True的a元素, 当遇到第一个False时产出剩下a元素（不再检查）
list(itertools.dropwhile(fun, a))
# [1, 2, 3, 4, 5]


# =======================================================================
"""takewhile"""
# 返回fun(a)为True的a元素, 遇到第一个False立即停止
list(itertools.takewhile(fun, a))
# [0]
list(itertools.takewhile(fun, [0, 2, 3, 4]))
# [0, 2]


# =======================================================================
"""islice"""
# 可迭代对象分片
list(itertools.islice(a, 3))
# [0, 1, 2]
list(itertools.islice(a, 1, 5, 2))
# [1, 3]


# =======================================================================
"""accumulate"""
# 首先将a前两个元素传给fun
# 然后将当前元素与上一个fun结果作为新的fun参数, 依次迭代
# 返回fun结果
list(itertools.accumulate(a, operator.add))
# [0, 1, 3, 6, 10, 15]
list(itertools.accumulate(a, min))
# [0, 0, 0, 0, 0, 0]


# =======================================================================
"""chain"""
# 拼接迭代器
list(itertools.chain([1, 2], [3, 4]))
# [1, 2, 3, 4]
list(itertools.chain.from_iterable([[1, 2], [3, 4, 5]]))
# [1, 2, 3, 4, 5]


# =======================================================================
"""product"""
# 返回迭代对象的笛卡尔积
list(itertools.product([1, 2], [4, 5]))
# [(1, 4), (1, 5), (2, 4), (2, 5)]


# =======================================================================
"""zip_longest"""
# zip的扩展版, 可处理不同长度的可迭代对象
list(itertools.zip_longest([1, 2, 3], [4, 5, 6]))
# [(1, 4), (2, 5), (3, 6)]
list(itertools.zip_longest([1, 2, 3], [4, 5], fillvalue=0))
# [(1, 4), (2, 5), (3, 0)]


# =======================================================================
"""combinations"""
# 组合可迭代对象产出值的为n维元组(不重复)
list(itertools.combinations('ABC', 2))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
list(itertools.combinations('ABC', 3))
# [('A', 'B', 'C')]


# =======================================================================
"""count"""
# 生成无穷等差数列
list(itertools.islice(itertools.count(1, 2), 5))
# [1, 3, 5, 7, 9]


# =======================================================================
"""groupby"""
# 返回可迭代对象的分组结果, 以[(key, value),...]形式返回
# value为迭代器
list(itertools.groupby(['aa','bb','ccc'], len))
# [(2, <itertools._grouper at 0x119cf9beb8>),
#  (3, <itertools._grouper at 0x119cf9bcc0>)]