# encoding: utf-8

def my_math(x,y):
    return x + y

import unittest

class ProductTestCase(unittest.TestCase):
    def test_math(self):
        for x in range(-10,10):
            for y in range(-10,10):
                p  =my_math(x,y)
                self.assertEqual(p,x+y,'Math function failed')

# def my_profile(x,y,z):
#     for i in range(x):
#         for j in range(y):
#             for z in range(z):
#                 pass

import cProfile,numpy,sys

my_array  = numpy.array([0,1,2,3,4,5,6,7,8,9])
my_list = [0,1,2,3,4,5,6,7,8,9]

def test_array():
    print('size:',sys.getsizeof(my_array))
    for i in range(10):
        for j in range(1000000):
            my_array[i] = 1

def test_list():
    print ('size:', sys.getsizeof(my_list))
    for i in range(10):
        for j in range(1000000):
            my_list[i] = i


if __name__ == '__main__':

    # 测试代码运行时间
    cProfile.run('test_array()')
    cProfile.run('test_list()')
    # 实例化所有TestCase子例，完成测试
    unittest.main()


