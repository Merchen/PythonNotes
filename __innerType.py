# -*- coding: utf-8 -*-
import math
from math import pi as PI

########################################################################
###  列表
########################################################################
def fun1():

    color = ['red', 'green', 'blue', 'orange']
    len(color)
    # 4
    sorted(color, reverse=False)
    # ['blue', 'green', 'orange', 'red'], 非就地
    max(color)
    # 'red'
    color.reverse()
    # ['orange', 'blue', 'green', 'red']， 就地反转
    color.sort()
    # ['blue', 'green', 'orange', 'red']， 就地升序
    color.sort(reverse=True)
    # ['red', 'orange', 'green', 'blue']， 就地逆序

    color = ['red', 'orange', 'green', 'blue']
    color[0] = 'yellow'
    # ['yellow', 'orange', 'green', 'blue']
    color.append('red')
    # ['yellow', 'orange', 'green', 'blue', 'red']
    color.insert(0, 'pink')
    # ['pink', 'yellow', 'orange', 'green', 'blue', 'red']
    color.index('red')
    # 5 元素首次出现位置
    color.extend([1, 2])
    # ['pink', 'yellow', 'orange', 'green', 'blue', 'red', 1, 2]
    if 'red' in color:
        # 遍历查找
        pass

    # 列表引用/别名, 通过co可修改color，列表、字典具有引用性质
    # 切片方式获得的列表为深复制
    c = color = ['pink', 'yellow', 'orange', 'green', 'blue', 'red']
    c = color[-1]
    # 'red'
    c = color[:]
    # ['pink', 'yellow', 'orange', 'green', 'blue', 'red']
    c = color[1:3]
    # ['yellow', 'orange']
    c = color[1:5:2]
    # ['yellow', 'green']
    color[1:3] = [1, 2]
    # ['pink', 1, 2, 'green', 'blue', 'red'], 切片形式赋值

    # 删除
    color = ['pink', 'yellow', 'orange', 'green', 'blue', 'red']
    del color[0]
    # ['yellow', 'orange', 'green', 'blue', 'red']
    color.remove('orange')
    # ['yellow', 'green', 'blue', 'red']
    color.pop(1)
    # green, ['yellow', 'blue', 'red'], 随机pop（高效逐个删除）

    # 列表解析，生成列表速度优于循环append
    arr = [i+1 for i in range(3)]
    # [1, 2, 3]

    # 普通遍历
    for co in color:
        pass

    # 并行迭代
    for idx, co in enumerate(color):
        print(idx, co)

    # zip函数返回元组列表[(1,4),(2,5)]
    zip([1, 2], [4, 5])

    # 列表生成
    arr = [1, 2, 3] + [2, 3, 4]    # 不支持减法, 效率低于extend
    # [1, 2, 3, 2, 3, 4]
    arr = [1, 2] * 2
    # [1, 2, 1, 2]
    arr = [None] * 3
    # [None, None, None]
    arr = [[]]*3
    # [[], [], []]
    list(range(5))
    # [0, 1, 2, 3, 4]
    list('hello')
    # ['h', 'e', 'l', 'l', 'o']

    # 就地运算
    arr = [1, 2, 3]
    # id(arr) = 345464219336
    arr *= 2
    # [1, 2, 3, 1, 2, 3]
    # id(arr) = 345464219336


########################################################################
###  元组
########################################################################
# 元组内部元素不可修改，但元素变量可修改（变量可随意赋值）
# 元组内所有元素可散列时，元组才可散列
def fun2():
    dem = (200, 50)
    # (200, 50)

    a = dem[0]

    dem = (100, 100)
    # (100, 100)5

    dem = (200, 50) + (200,)
    # (200, 50, 200)
    dem = (200, 100) + (100, 50)
    # (200, 100, 100, 50)

    # 拆包
    a, b = (100, 200)
    # a = 100, b = 200
    a, b, *c = range(5)
    # 0, 1, [2, 3, 4]

    # 元祖中含可变对象
    tup = (1, 2, [3, 4])
    try:
        tup[2] += [4,5]
        # (1, 2, [3, 4, 4, 5])
    except TypeError:
        pass


########### #############################################################
###  集合
########################################################################
# 不支持索引且自动去重， 元素以hash表形式存储
# 最好不要在迭代集合或字典时添加值，考虑到存储字典元素的无序性（python3.6之后有序）
def fun3():

    set1 = set(range(5))
    # {0, 1, 2, 3, 4}
    set1 = {1, 4, 4, 3} # 构建集合速度最快
    # {1, 3, 4}
    set1.add(5)
    # {1, 3, 4, 5}
    set1.pop()
    # {3, 4, 5}
    set1.remove(5)
    # {3, 4}

    set1 = {1, 2}.union({2, 3})
    # {1, 2, 3}
    set1 = {1, 2}.union([2, 3])
    # {1, 2, 3}

    set1 = {1, 2} | {2 ,3}
    # {1, 2, 3}
    set1 = {1, 2} & {2, 3}
    # {2}
    set1 = {1, 2} ^ {2, 3}
    # {1, 3}
    set1 = {1, 2} - {2, 3}
    # {1}

    set1 = {i for i in range(3)}
    # {0, 1, 2}

    b = {1, 2, 3} > {1, 2}
    # True


########################################################################
###  字典
########################################################################
# 字典由键-值对构成，键值对也称为项
# 字典中不含相同的键，前者自动被覆盖
def fun4():

    dic = dict([('name', 'Gumby'), ('age', 35)])
    # {'name': 'Gumby', 'age': 35}
    dict.fromkeys(['a', '1'], None)
    # {'a': None, '1': None}
    dict(zip(('a', 'b'), (1, 2)))
    # {'a': 1, 'b': 2}
    dic = {name:code for name, code in [('a', 'b'), (1, 2)]}
    # {'a': 'b', 1: 2}

    # 字典引用/别名
    c = dic
    c = dic.copy()

    # 元素查找
    dic = {'a':1, 'b':2}
    value = dic['a']
    value = dic.get('a', None)

    # 迭代
    # .items()      获取字典所有项列表，元素为元祖
    # .iteritems()  返回字典项迭代器，使用.next()获取键值对元组
    # .iterkeys()   字典键值迭代器
    # .values()     值表（无序）
    # .keys()       值表（无序）

    dic = {'a':1, 'b':2}
    for key, value in dic.items():
        pass
    # 默认在keys中遍历
    for key in dic:
        pass
    # python3在视图中查找, python2在列表中查找
    for key in dic.keys():
        pass

    # 默认在keys中查找
    # python3中dic.keys()返回dict_keys对象，hash
    # python2中dic.keys()返回list对象，遍历
    if 'a' in dic:
        pass
    if 'a' in dic.keys():
        pass

    dic['a'] = 2
    # {'a': 2, 'b': 2}
    dic['c'] = 3
    # {'a': 2, 'b': 2, 'c': 3}

    dic.update({'a': 1, 'd': 4})
    # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    dic.pop('d')
    # 4, {'a': 1, 'b': 2, 'c': 3}
    dic.popitem()
    # ('c', 3)， {'a': 1, 'b': 2} 随机pop，高效逐个删除
    del dic['b']
    # {'a': 1}
    dic.clear()
    # {}
    dic.get('a', 1)
    # 1, {}
    dic.setdefault('a',1)
    # 1, {'a': 1}
    dic.setdefault('a', 2)
    # 1, {'a': 1}


#########################################################################
### 字符串
#########################################################################
# Python3.6之后方法，直接在字符串中使用变量
# 字符串元素的值不可改变,s[1]='r'非法
def fun5():
    string = ' aBc def '
    string.title()
    # ' Abc Def '
    string.upper()
    # ' ABC DEF '
    string.lower()
    # ' abc def '

    string.rstrip()
    # ' aBc def'
    string.lstrip()
    # 'aBc def '
    string.strip()
    # 'aBc def'
    string.rstrip('f ')
    # ' aBc de'
    string.strip(' a')
    # 'Bc def'

    string.replace('Bc', 'aa')
    # ' aaa def '

    string.find('B')
    # 2
    string.count('a')
    # 1

    string.split()
    # ['aBc', 'def']

    string.center(12, '*')
    # '* aBc def **', 指定宽度，两边填充字符

    eval('%s + %s' % ('12', '45'))
    # 57

    '{},{},and {}'.format(*'abc')
    # 'a,b,and c'
    '{0},{1} and {0}'.format(*('a','b'))
    # 'a,b and a'
    '{c1},{c0} and {c2}'.format(c0=1, c1=2, c2=3)
    # '2,1 and 3'
    '{c1},{c0} and {c2}'.format(**dict(c0=1,c1=2,c2=3))
    # '2,1 and 3'

    '{mod.__name__} module defines {mod.pi} for pi'.format(mod=math)
    # 'math module defines 3.141592653589793 for pi'

    f's={PI}'
    # 's=3.141592653589793'
    '{:f}'.format(10)
    # '10.000000'
    '{:3}'.format(10)
    # ' 10'
    '{:+<10.3f}'.format(10)
    # '10.000++++', 左右中对齐<、>、^,使用$空白填充

    buf = ["%s=%s" % (k, v) for k, v in dict(a=1, b=2).items()]
    # ['a=1', 'b=2']
    ";".join(buf)
    # 'a=1;b=2'

    '123'.isalnum()
    # True
    'abc'.isalpha()
    # True
    isinstance('ssd', str)
    # True


# ########################################################################
# ### 运算
# ########################################################################
# #-------------------------------------------------------------------------
#
# num = 1 / 2           #1
# num = 1. / 2          #0.5
#
# num = 12.35
# int(num)        #12
# float(num)      #12.35
# str(num)        #'12.35'
# math.ceil(num)  #13.0
# math.sqrt(9)    #3.0
#
# bool('')                  #False
# bool('0')                 #True
# bool(0)                   #False
# bool(23)                  #True
# bool(None)                #False
#
# a = 2 and 1               #and、or语句符合短路逻辑，即表示式值确定后终止判断
#
#
# ########################################################################
# ### is语句（同一元素符）
# ########################################################################
# num1 = num2 = 10          #整型对象，is语句与==语句一致
# num3 = 10
# print(num2 is num1)       #True
# print(num3 is num1)       #True
#
# lst1 = lst2 = [1,2,3]
# lst3 = [1,2,3]
# print(lst2 is lst1)       #True，引用对象
# print(lst2 == lst1)       #True
# print(lst3 is lst1)       #False,非引用对象
# print(lst3 == lst1)       #True
#
#
# ########################################################################
# ### in语句（成员资格）
# ########################################################################
# b = 's' in 'search'           #True
# b = 'ch' in 'search'          #True
#
#
# ########################################################################
# ### if语句
# ########################################################################
# a, b, c = 1, 5, 3          #序列解包，多元素使用元组赋值
# a, b = b, a                #交换
# if a >= b and a >= c:
#     max_num = a
# elif b >= a and b >= c:
#     max_num = b
# else:
#     max_num = c
# s = 'max[{},{},{}]={}'.format(a,b,c,max_num)
# print(s)    #max[1,5,3]=5
#
# a = True
# c = 2 if a else 0         #三元表达式，a为真返回2，否则返回0
#
#
# ########################################################################
# ### while语句
# ########################################################################
# #-------------------------------------------------------------------------
# while True:
#     city = r"Input your favorite city:"
#     if city == 'q':
#         break
#     else:
#         print("Input 'q' to exit!")
#
#
# ########################################################################
# ### assert语句
# ########################################################################
# #断言方法，语句不成立时终止程序
# age = 10
# assert 0 < age < 10


########################################################################
### 控制语句
########################################################################
#-------------------------------------------------------------------------
#break：#跳转出循环
#continue：直接进入下次循环
#return：返回上层函数
#pass:什么都不错
#del：删除对象，删除列表对象的引用不影响原列表
