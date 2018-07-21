# -*- coding: utf-8 -*-
""""""

# =======================================================================
"""is/=="""
# is不能重载，执行速度优于None
# a==b ->a.__eq__(b)
a = None
print(a==None)
# True
print(a is None)
# True
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a==c, a==b)
# True True, 值比较
print(a is b, a is c)
# True False, id比较


# =======================================================================
"""in"""
a = 'ch' in 'search'
# True
b = 1 in [1, 2, 3]
# True


# =======================================================================
"""assert"""
# 断言方法，语句不成立时raise AssertionError
assert 0 < 8 < 10
assert 0 < 10 < 10


# =======================================================================
"""控制语句"""
# break: 跳转出for/while循环
# continue：直接进入下次for/while循环
# return: 程序返回至上层
# pass: 什么都不做
# del: 删除对象，删除列表对象的引用不影响原列表


# =======================================================================
"""if"""
#序列解包，多元素使用元组赋值
a1, a2, a3 = 1, 5, 3
#交换
a1, a2 = a2, a1

if a1 >= a2 and a1 >= a3:
    max_num = a1
elif a2 >= a3:
    max_num = a2
else:
    max_num = c

max_num = a1 if a2 <= a1 >= a3 else (a2 if a2 >= a3 else a3)

a = True
#三元表达式，a为真返回2，否则返回0
c = 2 if a else 0
# c = 2


# =======================================================================
"""while"""
i = 0
while True:
    print(i)
    i += 1
    if i == 5:
        break


# =======================================================================
"""类型转换/bool"""
import math
_ = 1 / 2
# 0.5, python2中为0
_ = 1. / 2
# 0.5

int(12.35)
# 12
float(12)
# 12.0
str(12.35)
# '12.35'
math.ceil(12.35)
# 13
math.sqrt(9)
# 3.0

bool('')
#False
bool('0')
#True
bool(0)
#False
bool(23)
#True
bool(None)
#False

#and、or语句符合短路逻辑，即表示式值确定后终止判断
_ = 2 and 1
