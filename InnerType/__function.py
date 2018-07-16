# -*- coding: utf-8 -*-
""""""

#=======================================================================
"""默认参数、函数引用、注解"""
def fun1():
    def hello(name:str, greeting:str='Hi') -> bool:
        """Function Help"""
        print('%s, %s!' % (greeting.title(), name.title()))
        return True

    # 打印函数开头的注释说明,与print(hello.__doc__)一致
    help(hello)
    # Help on function hello in module __main__:
    # hello(name, greeting='Hi')
    #     Function Help
    print(hello.__doc__)
    # Function Help

    # 检查是否为可调用函数
    print('callable:', callable(hello))

    # 默认参数元组
    print('__defaults__:', hello.__defaults__)
    # class 'tuple'>: ('Hi',)

    # 函数注释
    print('__annotations__:', hello.__annotations__)
    # __annotations__: {'name': <class 'str'>,
    #                 'greeting': <class 'str'>,
    #                 'return': <class 'bool'>}

    from inspect import signature
    for nm, param in signature(hello).parameters.items():
        # signature: name name
        # signature: greeting greeting = 'Hi'
        print('signature:', nm, param)

    # 函数引用/指针
    fun = hello
    fun('joe')                          # 'Hi, Joe!'
    fun('joe', 'hello')                 # 'Hello, Joe!'
    fun(greeting='Hi', name='joe')       # 'Hi, Joe!', 指定参数名称时参数顺序可变


#=======================================================================
"""动态参数"""
def fun2():
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
    get_userinfo(name[:], 23, 'chicago', 'engineer', fileld='physics')
    # aa, 列表以副本形式传递，函数内部不改变其值
    print(name[0])

    # person = {'info':('chicago','engineer'),'fileld':'physics','age':23,'last':'bb','first':'aa'}
    get_userinfo(name, 23, 'chicago', 'engineer', fileld='physics')
    # newstr, 列表以引用形式传递，函数内部可改变其值
    print(name[0])


#=======================================================================
"""解包"""
def fun3():
    def add(x, y):
        return x + y

    params = (1, 2)
    # 3, 元组加*表示分配参数
    add(*params)

    params = {'x':1, 'y':2}
    # 3, 字典的全部元素作为参数，key与同名参数匹配
    add(**params)


#=======================================================================
"""递归，三元表达式、二分查找"""
def fun4():
    def factorial(n):
        """递归的可读性好，但效率底"""
        return 1 if n==0 else n*factorial(n-1)
    # 6
    print(factorial(3))


    def search(seq, num, lower=0, upper=None):
        """seq为有序序列，num为查找的数字"""
        if upper is None:
            upper = len(seq) - 1

        if lower == upper:
            return upper

        mid = (lower + upper) / 2
        if num > seq[mid]:
            return search(seq, num, mid + 1, upper)
        else:
            return search(seq, num, lower, mid)
    # 3
    print(search([1, 2, 3, 4, 5, 6], 4))


#=======================================================================
"""函数内部定义、函数作为参数、函数作为返回值"""
def fun5():
    def func1(argf):
        print(1)
        def fun_in():
            # 函数内部定义的函数仅在调用时执行
            argf()
        print(2)
        return fun_in

    def func2():
        print(3)

    # 1 2 3, func1(func2)输出1,2，再执行函数运算()输出3
    func1(func2)()


