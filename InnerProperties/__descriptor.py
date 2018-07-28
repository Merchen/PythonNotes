# -*- coding: utf-8 -*-
"""
描述符是实现了特定协议的类, 协议包括__get__、__set__和__delete__方法
property/classmethod/staticmethod等装饰器使用了描述符功能

描述符基于协议实现，无需创建子类

实现__set__方法的描述符属于覆盖性描述符, 覆盖(接管)对描述属性的赋值操作
仅实现__get__方法的描述符属于非覆盖性描述符

仅实现__set__方法:
    obj.price   =>  无__get__方法且__dict__中无同名属性, 则返回描述符对象本身
    obj.__dict__['price'] = 10  # 遮盖描述符的读操作, 但写操作仍会被覆盖
    obj.price                   # 10， 调用set
    obj.price=7                 # 调用set覆盖， 但写入值不能通过obj.price获取
    obj.price                   # 10 

仅实现__get__方法:
    obj.price       # 调用get
    obj.price = 10  # 设置了同名的实例属性, 描述符被遮盖
    obj.price       # 10, 不调用get
    del obj.price   # obj.__dict__中删除'price'  
    obj.price       # 调用get
    
用户自定义的函数均含有__get__方法, 方法是描述符
因此对方法进行赋值, 方法将被覆盖

只读属性必须实现__get__和__set__方法, __set__抛出AttributeError异常即可

仅有__get__方法的描述符可实现高效缓存
赋值时同名属性覆盖描述符, 后续访问直接从__dict__中获取属性值, 不触发__get__, 达到缓存目的
"""


class Quantity:
    """描述符类"""

    __count = 0

    def __init__(self):
        cls = self.__class__
        # 存储属性名， 描述符无法获取托管属性的名称
        self.name = '_%s#%d' % (cls.__name__, cls.__count)
        cls.__count += 1

    def __get__(self, instance, owner):
        """
        托管属性引用时执行

        self描述符实例, 托管类的类属性
        <__main__.Quantity object at 0x000000B4D85D7F60>

        instance为托管实例
        <__main__.LineItem object at 0x000000F97B927FD0>

        owner托管类的引用, 用于获取托管类的类属性
        <class '__main__.LineItem'>
        """
        if instance is None:
            # 通过类访问托管属性时, 返回描述符实例
            return self
        else:
            # 托管属性名被构造成别名(存储属性名)，则可使用getattr获取属性值
            return getattr(instance, self.name)

    def __set__(self, instance, value):
        """
        托管属性赋值时执行
        """
        if value > 0:
            instance.__dict__[self.name] = value
        else:
            raise ValueError('Value must be > 0!')


def entity(self):
    """类装饰器, 更新托管属性名称"""
    for key, attr in self.__dict__.items():
        if isinstance(attr, Quantity):
            attr.name = '_{}#{}'.format(type(attr).__name__, key)
    return self


@entity
class LineItem:
    """托管类"""

    # 描述符实例（托管类的类属性）
    weight, price = Quantity(), Quantity()

    def __init__(self, weight, price):
        # 托管属性
        # weight属性名称在描述符类中重定义, 在self.__dict__中可能无法对应
        # 若'weight'被构造为'_Quantity#0', 则instance.weight实际执行getattr(instance, '_Quantity#0')
        # 属性被构造成别名, 难以维护, 通过类装饰器或元类可解决
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    # 托管实例
    instance = LineItem(10, 20)

    # 储存属性， 储存自己的值
    print(instance.price)

    # weight和price被构造成别名
    print(vars(instance))
    # {'_Quantity#0': 10, '_Quantity#1': 20}
    # {'_Quantity#weight': 10, '_Quantity#price': 20}


def _quantity(prop):
    """特性工厂函数"""

    def _getter(instance):
        # getattr(instance, prop)造成死循环
        return instance.__dict__[prop]

    def _setter(instance, value):
        if value > 0:
            instance.__dict__[prop] = value
        else:
            raise ValueError('Value must be > 0!')

    return property(_getter, _setter)


class _LineItem:
    """利用特性工厂函数添加描述符"""
    weight = _quantity('weight')
    price = _quantity('price')

    def __init__(self, weight, price):
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    instance = _LineItem(10, 20)
    print(instance.weight)
