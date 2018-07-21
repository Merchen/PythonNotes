""""""
"""此部分内容存储在__doc__

函数局部空间，记录函数参数和局部变量;
模块全局空间，记录函数、类、其他导入的模块及模块级变量;
内置空间，存放内置函数和异常;
Python查看变量顺序：函数局部空间-->模块全局空间-->内置空间

__file__    自身文件名，包含绝对路径
__doc__     存储文件开头注释、或函数开头注释，help(fanme)
__name__    当前文件执行时为'__main__'，被调用时为自身文件名
__bases__   查看继承
"""

# 全局变量，外部文件可引用
G_NUM = 10
G_STR = 'str'

locals()['G_NUM'] = 5
# G_NUM = 5, 全局变量被修改, 模块中可通过local()修改全局对象

globals()['G_NUM'] = 10
# G_NUM = 10, 全局变量被修改

# =======================================================================
"""函数参数/解包"""
def fun1():
    def hello(name: str='zhw', *args, **kwargs) -> bool:
        """Function Help"""
        print('Hi, %s!' % name.title())
        print('args: ' + ', '.join(str(arg) for arg in args))
        print('kwargs: %s' % kwargs)
        return True

    hello('mm')
    # Hi, Mm!
    # args:
    # kwargs: {}

    hello(a=1)
    # Hi, Zhw!
    # args:
    # kwargs: {'a': 1}

    hello('mm', 1, 2, a=3, b=4)
    # Hi, Mm!
    # args: 1, 2
    # kwargs: {'a': 3, 'b': 4}

    hello('mm', (1, 2))
    # Hi, Mm!
    # args: (1, 2)
    # kwargs: {}

    # 元组解包
    hello(*('mm', 2, 3))
    # Hi, Mm!
    # args: 2, 3
    # kwargs: {}

    # *列表/元组解包， *字典解包
    hello(*('mm', 2, 3), **{'a':1, 'b':2})
    # Hi, Mm!
    # args: 2, 3
    # kwargs: {'a': 1, 'b': 2}

    # 字典解包, 键参同名时自动配对
    hello(**{'name':'mm', 'a':1})
    # Hi, Mm!
    # args:
    # kwargs: {'a': 1}

    print(hello.__doc__)
    # 'Function Help'

    callable(hello)
    # True, 检查是否为可调用函数

    print(hello.__defaults__)
    # ('zhw',), 默认参数

    print(hello.__annotations__)
    # {'name': str, 'return': bool}, 注释


#=======================================================================
"""函数内部定义、函数作为参数、函数作为返回值"""
def fun2():
    def func1(f):
        print(1)
        def fun_in():
            # 函数内部定义的函数仅在调用时执行
            f()
        print(2)
        return fun_in

    def func2():
        print(3)

    # 1 2 3, func1(func2)输出1,2，再执行函数运算()输出3
    func1(func2)()


#=======================================================================
"""递归，三元表达式、二分查找"""
def fun3():
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


# =======================================================================
"""locals()/globals()"""
# 可通过globals()直接修改全局变量的值
# 函数内部的locals()函数，仅记录引用之前函数的局部变量
def fun4(arg=2):
    """Function Manual"""
    global G_NUM

    print(globals().get('arg', False))
    # False, 参数为局部对象

    print(locals())
    # {'arg': 2}, 局部空间

    print(globals())
    # G_NUM,G_STR,__name__,__doc__,等, 全局空间

    a = 1
    locals()['a'] = 10
    print(a)
    # a = 1, 副本形式，更改无效

    locals()['G_NUM'] = 1
    print(G_NUM)
    # G_NUM = 10, 副本形式，更改无效

    globals()['G_NUM'] = 1
    print(G_NUM)
    # G_NUM = 1, 引用形式，更改有效

    doc = fun1.__doc__
    # Function Manual, help(add)将显示更多信息


# =======================================================================
"""变量作用域/设计选择"""
def fun5():
    def fun21(a):
        print(a)
        print(b)

    b = 4; fun21(3)
    # 3, 4, 未在函数内部赋值的b，系统将逐层查找变量

    def fun22(a):
        print(a)
        print(b)
        b = 1

    b = 4; fun22(3)
    # 3, UnboundLocalError: local variable 'c' referenced before assignment
    #  变量b在函数内部中被赋值，默认为局部变量

    # b = 4
    # def fun23(a):
    #     global b
    #     print(a)
    #     print(b)
    #     b = 1
    #
    # b = 4; fun23(3)
    # global声明后，无论是否赋值均为全局变量（global在module根下查找）


# =======================================================================
"""装饰器"""
# 装饰器--运行时改变函数的行为
# 模块加载(import)时执行
def fun6():
    def _start(fun):
        print('running _start()')
        return fun

    @_start
    def start():
        print('runing start()')

    # 定义装饰器的等价形式
    start = _start(start)


# =======================================================================
"""闭包"""
# 闭包--延伸作用域的函数
# 引用定义体之外定义的非全局变量
# 自由变量，未在本地作用域绑定的变量
def fun7():
    def make_averager():
        series = []

        def averager(value):
            series.append(value)
            total = sum(series)
            return 1. * total / len(series)

        return averager

    print(make_averager.__code__.co_varnames)
    # ('averager',), make_averager的局部变量

    print(make_averager.__code__.co_freevars)
    # (), make_averager的自由变量

    avg = make_averager()
    print(avg.__code__.co_varnames)
    # ('value', 'total'), averager的局部变量
    print(avg.__code__.co_freevars)
    # ('series',), averager的自由变量

    print(avg.__closure__)
    # (<cell at 0x0000001B042AA1F8: list object at 0x0000001B0456CC08>,)
    # 自由对象的绑定对象

    avg(10), avg(11)
    print(avg.__closure__[0].cell_contents)
    # [10, 11], 自由对象的值
