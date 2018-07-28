# -*- coding: utf-8 -*-

MyClass = type('MyClass', (object, ), dict(a=2, b=lambda self:self.a * 2))

myclass = MyClass()
print(myclass.b())