# -*- coding: utf-8 -*-

from warnings import warn
"""
__xxx__,系统专用标识,可在类外部使用instance.__xxx__形式调用
__xxx，伪私有声明，不可在类外部使用instance.__xxx形式调用
_xxx,伪保护声明，仅类实例和子类实例可以直接访问，不可通过import方式载入

对象实例的属性可映射到__dict__中的key
对象实例的属性查找顺序遵循--实例对象本身 --> 类 --> 类的父类
"""


# 被保护类型，其他文件不同通过import方式载入
_MODEL_BATTERY = {"A": 70, "S": 100}
_MYDICT = {"a": 1, "b": 2, "c": 3}


class Car(object):
    """"""
    # 类变量，统计汽车总数,该变量可通过类直接引用
    count = 0
    __count = 0

    def __init__(self, make, color):
        """构造函数"""
        self.make = make.title()
        self.color = color.title()
        self.__odometer= 0
        # 更新类级变量
        Car.count += 1
        Car.__count += 1

    def __del__(self):
        """析构函数"""
        del self

    def __getitem__(self, key):
        """instance[key]方式访问时调用"""
        try:
            return self.__dict__[key]
        except:
            raise AttributeError("'%s' attribute not exist!" % key)

    def __setitem__(self, key, value):
        """instance[key]方式赋值时调用"""
        self.__dict__[key] = value

    def __getattr__(self, key):
        """instance.key方式访问不存在的属性时调用，影响hasattr(instance,name)的结果"""
        raise AttributeError("'%s' attribute not exist!" %key)

    def __setattr__(self, key, value):
        """instance.key方式赋值时，自动调用"""
        self.__dict__[key] = value
        if key not in self.__dict__:
            print('New attribute added.')


    @property
    def odometer(self):
        """
        使用property装饰器，将类方法转换为类属性（只读）

        value = instance.odometer形式引用，调用时执行property函数的getter方法
        若使用通过instance.read_odometer形式则报错
        """
        return self.__odometer

    @odometer.setter
    def odometer(self, mile):
        """
        使用装饰器的setter方法对类方法赋值

        instance.odometer = value形式调用，调用时执行property函数的setter方法
        """
        # 检查参数mile是否为int或float类型
        if isinstance(mile,int) or isinstance(mile,float):
            if self.__odometer > mile:
                raise ValueError('Odemeter cannot be reduced!')
            else:
                self.__odometer = mile
        else:
            raise TypeError('Odemeter should be a num!')

    def __get_baseinfo(self):
        """
        私有函数，作为baseinfo(property对象)的getter函数

        lambda self:'%s %s' %(self.make,self.color)与上等价
        经过property实例化后，通过value = instance.baseinfo调用该方法
        """
        return '%s %s' %(self.make,self.color)

    def __set_baseinfo(self,tuple_info):
        """
        私有函数，作为baseinfo(property对象)的setter函数

        经过property实例化后，通过instance.baseinfo = value调用该方法
        """
        self.make, self.color = map(lambda x:x.title(),tuple_info)

    baseinfo = property(__get_baseinfo, __set_baseinfo)

    def info(self):
        """调用__get_baseinfo方法，并返回"""
        return self.baseinfo

    def get_count1(cls):
        """返回属性__count的值"""
        return cls.__count

    # 声明方法为类方法，不属于特定实例，只能调用类级成员
    get_count1 = classmethod(get_count1)

    @classmethod
    def get_count2(cls):
        """
        类成员方法，含参数
        """
        return cls.__count

    @staticmethod
    def get_count3():
        """
        静态成员方法，不含参数，返回类级变量__count的值

        装饰器staticmethod声明方法为静态方法，即不属于特定实例
        """
        # return Car.__count
        return globals()['Car'].__count


class Battery(object):
    """"""
    def __init__(self, model):
        model = model.title()
        try:
            self.__battery_size = _MODEL_BATTERY[model]

        except KeyError:
            self.__battery_size = 0
            raise ("Error Model!")

        except Exception:
            raise

    def size(self):
        return '%sKwh' %self.__battery_size


class ElectricCar(Car):
    """
    电动车类，继承Car类

    Class0(Class1,Class2,....)为多重继承，应避免使用
    不同基类（无继承关系）之间方法可相互调用，这些方法在共同子类中有效，self对象的特性
    """
    def __init__(self, make, color, model='a', **args):
        # 初始化父类方法，未初始化将不能使用父类方法
        super(ElectricCar, self).__init__(make, color)
        self.battery = Battery(model)
        self._others = args

    def info(self):
        """父类方法重构"""
        # 执行父类方法
        strinfo = super(ElectricCar, self).info()
        for key, value in self._others.items():
            strinfo = "%s %s-%s " % (strinfo, key, value)

        return "%s %s " %(strinfo.title(), self.battery.size())


class Dict2Object(object):
    """利用__dict__内置属性，将字典变量添加至类属性"""
    def __init__(self):
        self.__dict__.update(_MYDICT)


if __name__ == '__main__':
    mycar1 = ElectricCar('tesla', 'black', model='s', year=2016)
    mycar2 = Car('bmw', 'grey')

    """使用类级成员"""
    mycar1.more = 11    # mycar1对象中增加键值对
    mycar1.count = 10   # 在mycar1对象中增加键值对,Car.count=2, mycar1.count=10, mycar2.count=2
    Car.count = 2       # 修改类对象的键值对, 实例mycar2本身不存在键值对count，若外部引用其值，则自动寻找到父类Car
                        # Car.count = 20, mycar1.count = 10, mycar2.count = 20
    n1 = mycar1.get_count1()    # 2, 通过实例对象调用类方法
    n2 = Car.get_count2()       # 2, 直接通过类名调用类方法
    n3 = Car.get_count3()       # 2, 直接通过类调用静态方法
    print(n1,n2,n3)

    """字典转为对象"""
    odict = Dict2Object()   # odict.a = 1

    """索引访问类属性"""
    s1 = mycar1.make                # tesla
    s2 = mycar1['make']             # tesla
    #s2 = getattr(mycar1,'make')    #tesla

    """改变对象方法"""
    def func(): print('Instance method changed!')

    mycar1.info = func
    #mycar1.info()  # func1

    """查看所属类与继承关系"""
    s3 = issubclass(ElectricCar, Car)   # True
    s4 = ElectricCar.__bases__          # <type 'tuple'>: (<class 'Car'>,)
    s5 = isinstance(mycar2, Car)        # True
    s6 = isinstance(mycar1, Car)        # True,基类同样成立

    s7 = mycar2.__class__               # <class 'Car'>
    s8 = s7('m', '3')                   # 通过__class__获取类对象名，可新建类
    #mycar1.info = 'a','b'
    print(mycar2.jkjkjk)


