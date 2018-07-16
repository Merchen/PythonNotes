# -*- coding: utf-8 -*-

from functools import partial, update_wrapper

#=======================================================================
"""partial/update_wrapper"""
# 函数参数默认化/函数属性复制到指定函数
def fun1():
    def fun11(a, b):
        """Inner function"""
        print('a=%s, b=%s' % (a, b))

    mpatical = partial(fun11, b=2)
    mpatical(1)
    # a = 1, b = 2

    print(mpatical.__doc__)
    # partial(func, *args, **keywords) - new function with partial application
    # of the given arguments and keywords.

    update_wrapper(mpatical, fun11)
    print(mpatical.__doc__)
    # Inner function 5