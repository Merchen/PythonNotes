# -*- coding: utf-8 -*-
import abc
import functools
import math
import operator
import reprlib
import collections
import itertools
import copy
import numbers


# __xxx__,系统专用标识,可在类外部使用instance.__xxx__形式调用
# __xxx，伪私有声明，不可在类外部使用instance.__xxx形式调用
# _xxx,伪保护声明，仅类实例和子类实例可以直接访问，不可通过import方式载入
#
# 对象实例的属性可映射到__dict__中的key
# 对象实例的属性查找顺序遵循--实例对象本身 --> 类 --> 类的父类
#
# Class0(Class1,Class2,....)多重继承
# Class0.__mro__元组中为所有继承类对象, (Class0, Class1, Class2, ...., object)
# Class0调用方法时遍历各个类，直到找到对应方法或发生异常

# 最好不要直接使用内置数据类型（C语言编写）作为基类, 子类可能无法覆盖基类的方法

# 鸭子类型（表征学）：忽略对象类型, 关注对象有没有实现特定协议（方法）
# 白鹅类型（支序系统学）：忽略对象单独特征，根据祖先特征分类

# collections.abc中模块UML图
#
# Iterable                      >>  Iterator
# Iterable + Container + Sized  >>  Sequence/Mapping/Set
# Sized                         >>  MappingView
#
# Sequence          >>  MutableSequence
# Mapping           >>  MutableMapping
# Set               >>  MutableSet
# Set + MappingView >>  ItemsView/KeysView
# MappingView       >> ValuesView

# 运算符重载: a + b
# 优先执行a.__add__(b), 返回不为NotImplemented时作为结果输出
# 否则执行b.__radd__(a), 返回不为NotImplemented时作为结果输出
# 否则溢出TypeError异常
# 即正向方法调用不成功的话，调用反向方法

# += 方法__iadd__未实现时, 自动调用__add__

# 实现__iter__或__getitem__后, 对象可迭代
# 执行iter()后返回迭代器


class _Vector2D:
    """
    限制属性, 不可新添加属性
    元组存储属性，节省内存
    """
    __slots__ = ('x', 'y')
    typecode = 'd'


class Vector():
    """内部属性"""

    typecode = 'd'
    shorcut_names = 'xyzt'

    def __init__(self, components):
        """
        constructor
        """
        self._components = components

        self.__pos = 0

    def __iter__(self):
        """
        iter()
        return self时，即是可迭代对象，又是自身的迭代器

        未实现该方法时试图迭代__getitem__方法, 从0开始索引
        可迭代需实现__iter___：isinstance(self, abc.Iterable) = True
        迭代器需实现__next__和__iter__: isinstance(self, abc.Iterator) = True

        可迭代对象一定不能是自身的迭代器, 即必须实现__iter__, 但不能实现__next__
        """
        # 返回生成器时, 迭代时不调用__next__方法
        # return self时(迭代器). 迭代时调用__next__方法
        return (i for i in self._components)

    def __next__(self):
        """
        for...in...、list(self.__iter__)、
        .next(self.__iter__)、next(self.__iter__)

        返回下一个可迭代对象, 捕获StopIteration异常后停止
        """
        pos = self.__pos
        if pos < len(self._components):
            value = self._components[self.__pos]
            self.__pos= pos + 1
            return value
        else:
            self.__pos = 0
            raise StopIteration

    def __contains__(self, item):
        """
        in self
        """
        return item in self._components

    def __len__(self):
        """
        len(self)
        """
        return len(self._components)

    def __getattr__(self, key):
        """"
        value = self.key, key不存在时
        影响hasattr(instance, name)
        """
        cls = type(self)
        if len(key) == 1:
            pos = cls.shorcut_names.find(key)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        raise AttributeError('{.__name__!r} objetc has no attribute {!r}'.format(cls, key))

    def __setattr__(self, key, value):
        """
        self.key = value

        对内部属性赋值均会调用该方法, 防止死循环
        self.__dict__方式赋值不调用__setattr__方法
        """
        cls = type(key)
        if len(key) == 1:
            if key in cls.shorcut_names:
                error = 'Read-only attribute {attr_name!r}'
            elif key.islower():
                error = "cann't set attributes 'a-z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=key)
                raise AttributeError(msg)
        # 更新self.__dict__
        # self.__dict__[key] = value
        super().__setattr__(key, value)

    def __getitem__(self, index):
        """
        value = self[key]

        实现该方法对象即可迭代
        index为数字, for循环中溢出IndexError时迭代结束
        """
        if isinstance(index, slice):
            return type(self)(self._components[index])
        elif isinstance(index, int):
            try:
                return self._components[index]
                # return self.__getattribute__('_components')[index]
            except(KeyError, AttributeError, IndexError) as err:
                raise err
        else:
            raise TypeError('Index must be integers!')

    def __setitem__(self, key, value):
        """
        self[key] = value
        """
        msg = "%s object does not support item assignment" \
              % type(self).__name__
        raise TypeError(msg)

    def __repr__(self):
        """
        repr(self)
        """
        components = reprlib.repr(self._components)
        components = components[components.find('['):]
        return 'Vector({})'.format(components)

    def __str__(self):
        """
        str(self)
        """
        return str(tuple(self))

    def __bytes__(self):
        """
        bytes(self)
        """
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        """
        self == other
        """
        if isinstance(other, type(self)):
            if len(self) != len(other):
                return False
            for a, b in zip(self, other):
                if a != b:
                    return False
            return True
        else:
            return NotImplemented

    def __hash__(self):
        """
        hash(self)

        可散列对象: 其生命周期内散列值不变、相同对象的散列值相等
        对于原子不可变数据类型str、bytes和数值类型都是hashable
        使用异或^混合各分量的散列值
        """
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __add__(self, other):
        """
        self + other

        # 溢出NotImplemented后, 执行other.__radd__(self)
        """
        # if self is other:
        #     other = copy.deepcopy(other)
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector([a + b for a, b  in pairs])
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        """
        other + self

        溢出NotImplemented后, 执行other.__add__(self)
        """
        return self + other

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector([i * scalar for i in self])
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar

    def __abs__(self):
        """
        abs(self)
        """
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        """
        bool(self)
        """
        return bool(abs(self))

    def __call__(self):
        """
        self()
        """
        pass

    @classmethod
    def frombytes(cls, octets):
        return cls(memoryview(octets[1:]).cast(chr(octets[0])))

    def _instance(self):
        print('Iterable: ', isinstance(self, collections.Iterable))
        # True, __iter__方法
        print('Iterator: ', isinstance(self, collections.Iterator))
        # True, __iter__和__next__方法
        print('Container: ', isinstance(self, collections.Container))
        # True, __container__方法
        print('Sized: ', isinstance(self, collections.Sized))
        # True, __len__方法

vec = Vector([1, 2, 3])

# vec._instance()
print(next(vec))


# class Car(metaclass=abc.ABCMeta):
class Car(abc.ABC):
    # python 2
    # __metaclass__ = abc.ABCMeta

    # 类级变量
    count = 0
    __count = 0

    def __init__(self, make, color):
        self.make, self.color = make, color
        self.__odometer = 0
        Car.count += 1
        Car.__count += 1

    @property
    def odometer(self):
        return self.__odometer

    @odometer.setter
    def odometer(self, mile):
        # 检查参数mile是否为int或float类型
        if isinstance(mile, int) or isinstance(mile, float):
            if self.__odometer > mile:
                raise ValueError('Odemeter cannot be reduced!')
            else:
                self.__odometer = mile
        else:
            raise TypeError('Odemeter should be a num!')

    # 与使用装饰器等价
    # odometer = property(getter, setter)

    @abc.abstractmethod
    def info(self):
        print('%s, %s' % (self.make, self.color))

    @classmethod
    def get_count(cls):
        return cls.__count


class Battery:
    __ModelInfo = {'A': 70, 'S': 100}

    def __init__(self, model='A'):
        self.model, self.__size = self.__init_model(model)

    def __init_model(self, model):
        try:
            size = self.__ModelInfo[model]
            return model, size
        except KeyError:
            return 'A', 70

    @property
    def size(self):
        return self.__size


class ElectricCar(Car):

    def __init__(self, make, color, model='a', **kwargs):
        # 初始化父类方法，未初始化将不能使用父类方法
        super(ElectricCar, self).__init__(make, color)

        self.battery = Battery(model)

        for key, value in kwargs.items():
            self.__dict__[key] = value

    def info(self):
        super(ElectricCar, self).info()
        print('%sKwh-battery' % self.battery.size)

# car = ElectricCar('Tesla', 'Balck')
# car.info()


class Dict2Object(object):
    """利用__dict__内置属性，将字典变量添加至类属性"""

    def __init__(self):
        self.__dict__.update(_MYDICT)


# ---------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    pass
    # mycar1 = ElectricCar('tesla', 'black', model='s', year=2016)
    # mycar2 = Car('bmw', 'grey')
    #
    # """使用类级成员"""
    # mycar1.more = 11  # mycar1对象中增加键值对
    # mycar1.count = 10  # 在mycar1对象中增加键值对,Car.count=2, mycar1.count=10, mycar2.count=2
    # Car.count = 2  # 修改类对象的键值对, 实例mycar2本身不存在键值对count，若外部引用其值，则自动寻找到父类Car
    # # Car.count = 20, mycar1.count = 10, mycar2.count = 20
    # n1 = mycar1.get_count1()  # 2, 通过实例对象调用类方法
    # n2 = Car.get_count2()  # 2, 直接通过类名调用类方法
    # n3 = Car.get_count3()  # 2, 直接通过类调用静态方法
    #
    # """字典转为对象"""
    # odict = Dict2Object()  # odict.a = 1
    #
    # """索引访问类属性"""
    # s1 = mycar1.make  # tesla
    # s2 = mycar1['make']  # tesla
    # # s2 = getattr(mycar1,'make')    #tesla
    #
    # """改变对象方法"""
    #
    #
    # def func():
    #     print('Instance method changed!')
    #
    #
    # mycar1.info = func
    # # mycar1.info()  # func1
    #
    # """查看所属类与继承关系"""
    # s3 = issubclass(ElectricCar, Car)  # True
    # s4 = ElectricCar.__bases__  # <type 'tuple'>: (<class 'Car'>,)
    # s5 = isinstance(mycar2, Car)  # True
    # s6 = isinstance(mycar1, Car)  # True,基类同样成立
    #
    # s7 = mycar2.__class__  # <class 'Car'>
    # s8 = s7('m', '3')  # 通过__class__获取类对象名，可新建类
    #
    # # mycar1.info = 'a','b'
    # for iter in mycar1:
    #     s9 = iter
    #
    # """__str__"""
    # print(mycar1)
    #
    # """__call__"""
    # print(mycar1())
    #
    # """类的引用"""
    # print(mycar1.__class__)
    # print(ElectricCar)
