# -*- coding: utf-8 -*-
""""""
# 字典由键-值对构成，键值对也称为项
# 字典中不含相同的键，前者自动被覆盖


#=====================================================
"""生成"""
dict([('name', 'Gumby'), ('age', 35)])
# {'name': 'Gumby', 'age': 35}

dict.fromkeys(['a', '1'], None)
# {'a': None, '1': None}

dict(zip(('a', 'b'), (1, 2)))
# {'a': 1, 'b': 2}

dict({name:code for name, code in [('a', 'b'), (1, 2)]})
# {'a': 'b', 1: 2}


#=====================================================
"""引用/别名"""
c1 = dic = {'a':1, 'b':2}
c2 = dic.copy()

value1 = dic['a']

value2 = dic.get('a', None)


#=====================================================
"""迭代/查找"""
# .items()      获取字典所有项列表，元素为元祖
# .iteritems()  返回字典项迭代器，使用.next()获取键值对元组
# .iterkeys()   字典键值迭代器
# .values()     值表（无序）
# .keys()       值表（无序）

dic = {'a':1, 'b':2}

for key, value in dic.items():
    pass

# 默认在keys中遍历
for key in dic:
    pass

# python3在视图中查找, python2在列表中查找
for key in dic.keys():
    pass

# 默认在keys中查找
# python3中dic.keys()返回dict_keys对象，hash
# python2中dic.keys()返回list对象，遍历
if 'a' in dic:
    pass

if 'a' in dic.keys():
    pass


#=====================================================
"""修改/更新/删除"""
dic = {'a':1, 'b':2}

dic['a'] = 2
# {'a': 2, 'b': 2}

dic['c'] = 3
# {'a': 2, 'b': 2, 'c': 3}

dic.update({'a': 1, 'd': 4})
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

dic.pop('d')
# 4, {'a': 1, 'b': 2, 'c': 3}

# 随机pop，高效逐个删除
dic.popitem()
# ('c', 3)， {'a': 1, 'b': 2}

del dic['b']
# {'a': 1}

dic.clear()
# {}

dic.get('a', 1)
# 1, {}

dic.setdefault('a',1)
# 1, {'a': 1}

dic.setdefault('a', 2)
# 1, {'a': 1}