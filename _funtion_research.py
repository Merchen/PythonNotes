# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
"""默认参数、参数顺序、函数引用"""
def hello(name, greeting='Hi'):
    """Function Help"""
    print('%s, %s!' % (greeting.title(), name.title()))

help(hello)                         # 打印函数开头的注释说明,与print(hello.__doc__)一致
print(callable(hello))              # 内建函数检查参数是否为可调用函数

fun = hello                         # 函数指针
fun('joe')                          # 'Hi, Joe!'
fun('joe', 'hello')                 # 'Hello, Joe!'
fun(greeting='Hi', name='joe')      # 指定参数名称时，参数顺序可变，'Hi, Joe!'


# -------------------------------------------------------------------------
"""动态参数"""
def get_userinfo(name, age=None, *userinfo, **kwds):
    """
    name: 必须通过实参给定
    age: 可使用默认参数
    *: 可接收任意数量实参的元组
    **: 可接受任意数量实参的字典
    """
    person = {'first': name[0], 'last': name[1]}
    if age:                         # age=''或 None时，条件均不成立
        person['age'] = age

    name[0] = 'newstr'              # 原列表被更改,形参使用复制传递则不会更改
    person['info'] = userinfo
    for key in kwds.keys():
        person[key] = kwds[key]
    return person

name = ['aa', 'bb']
person0 = get_userinfo(name[:], 23, 'chicago', 'engineer', fileld='physics')
print(name[0])          # aa, 列表以副本形式传递，函数内部不改变其值
                        # person = {'info':('chicago','engineer'),'fileld':'physics','age':23,'last':'bb','first':'aa'}
person1 = get_userinfo(name, 23, 'chicago', 'engineer', fileld='physics')
print(name[0])          # newstr,列表以引用形式传递，函数内部可改变其值


# -----------------------------------------------------------7--------------
"""元组解包"""
def add(x, y): return x + y

params = (1, 2)
res = add(*params)      # 元组加*表示分配参数，res=3


# -----------------------------------------------------------7--------------
"""递归，三元表达式"""
def factorial(n):
    """递归的可读性好，循环的效率高"""
    return 1 if n==0 else n*factorial(n-1)

print(factorial(3))     # 6


# -----------------------------------------------------------7--------------
"""递归，二分查找"""
def search(seq,num,lower=0,upper=None):
    """seq为有序序列，num为查找的数字"""
    if upper is None:
        upper = len(seq)-1

    if lower == upper:
        return upper

    mid = (lower + upper)/2
    if num > seq[mid]:
        return search(seq,num,mid+1,upper)
    else:
        return search(seq,num,lower,mid)

print(search([1,2,3,4,5,6],4))     # 3


# -----------------------------------------------------------7--------------
"""函数内部定义、函数作为参数、函数作为返回值"""
def func1(argf):
    print(1)
    def fun_in():   # 函数内部定义的函数仅在调用时执行
        argf()
    print(2)
    return fun_in

def func2(): print(3)

func1(func2)()      # 1 2 3, func1(func2)输出1,2，再执行函数运算()输出3