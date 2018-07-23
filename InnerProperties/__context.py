# -*- coding: utf-8 -*-
import sys
# 上下文协议需实现__enter__和__exit__方法

#=====================================================
"""else"""
# for...else/while...else
# 循环正常终止时else语句执行
# 使用break语句跳出循环不执行
for _ in range(5):
    pass
else:
    print(True)

i = 0
while i < 5:
    i += 1
else:
    print(True)


#=====================================================
"""with"""
# 简化try...finally语句
# as语句绑定目标变量, 应用__enter__方法
# with open('mirror.txt') as f:
#     src = f.read(60)

class LookingClass:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return '12345'

    def reverse_write(self, text):
        """逆序输出"""
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        """返回None或True之外的值, 产生异常时向上冒泡"""
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide zero!')
            return True

def _TestWith():
    with LookingClass() as what:
        print('abcd')
        # dcba
        print(what)
        # 54321

_TestWith()