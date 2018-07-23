# -*- coding: utf-8 -*-
from collections import Counter, deque, OrderedDict, defaultdict, \
    ChainMap, UserDict, namedtuple
import queue
from  warnings import warn


#=======================================================================
"""deque"""
# 高效处理频繁先进先出
# 执行1000万次pop和left，deque、list、Queue分别耗时1.8s、2.2s、44秒
# append和popleft为原子性操作，保证多线程安全访问
def _deque():
    dq = deque(range(5))
    # deque([0, 1, 2, 3, 4])
    dq.count(1)
    # 1

    dq.append(5)
    # deque([0, 1, 2, 3, 4, 5])
    dq.appendleft(-1)
    # deque([-1, 0, 1, 2, 3, 4, 5])
    dq.extend([6, 7])
    # deque([-1, 0, 1, 2, 3, 4, 5, 6, 7])
    dq.extend(deque([8, 9]))
    # deque([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    dq.extendleft(deque([-3, -2]))
    # deque([-2, -3, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    dq.index(1)
    # 4
    dq.insert(4, 1)
    # deque([-2, -3, -1, 0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    dq.pop()
    # 9, deque([-2, -3, -1, 0, 1, 1, 2, 3, 4, 5, 6, 7, 8])
    dq.popleft()
    # -2, deque([-3, -1, 0, 1, 1, 2, 3, 4, 5, 6, 7, 8])
    dq.remove(1)
    # deque([-3, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

    dq.reverse()
    # deque([8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -3])
    dq.rotate(3)
    # deque([0, -1, -3, 8, 7, 6, 5, 4, 3, 2, 1])

    dq1 = dq.copy()
    dq1.clear()


#=======================================================================
"""Queue"""
def _queue():
    que = queue.Queue(maxsize=5)
    try:
        for i in range(6):
            que.put(i, block=True, timeout=1)
    except queue.Full as err:
        warn('Full queue!')
    try:
        for i in range(6):
            que.get(block=False)
    except queue.Empty :
        warn('Empty queue!')


#=======================================================================
"""OrderedDict"""
# 有序字典，利用列表存储键名
# python3.6开始，dict默认有序
def _orderDict():
    items = ('a',1),('b',2),('c',3)

    odic = OrderedDict(items)
    # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

    odic['d'] = 4
    # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

    odic.keys()
    # odict_keys(['a', 'b', 'c', 'd'])

    odic.popitem()
    # ('d', 4)


#=======================================================================
"""defaultdict"""
# 访问不存在的键时，返回默认值
# dict.setdefault(key, default)
def _defaultdict():
    ddic = defaultdict(list)

    ddic.update(dict(a=1, b=2))
    # defaultdict(list, {'a': 1, 'b': 2})

    ddic['c'].append(3)
    # defaultdict(list, {'a': 1, 'b': 2, 'c': [3]})

    ddic = defaultdict(dict)

    ddic['first'].fromkeys(['a1', 'a2'], None)
    # {'a1': None, 'a2': None}

    ddic['second']['b1'] = 1
    # defaultdict(dict, {'first': {}, 'second': {'b1': 1}})


#=======================================================================
"""ChainMap"""
# ChainMap(dict1, dict2,...)
# 从前往后依次搜索键，直到搜索到为止
def _chainMap():
    cdic = ChainMap({'a':1, 'b':2}, {'a':2, 'c':3})
    value = cdic['a']
    # 1
    value = cdic['c']
    # 3


#=======================================================================
"""Counter"""
# ChainMap(dict1, dict2,...)
# 从前往后依次搜索键，直到搜索到为止
def _counter():
    counter = Counter('aabb')
    counter = Counter(dict(a=2, b=2))
    # Counter({'a': 2, 'b': 2})

    counter.update('abccababb')
    # Counter({'b': 6, 'a': 5, 'c': 2})

    counter.most_common(2)
    # [('b', 6), ('a', 5)]

    counter - Counter('aabbc')
    # Counter({'a': 3, 'b': 4, 'c': 1})

    iter = counter.elements()
    list(iter)
    # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c']


#=======================================================================
"""UserDict"""
# 使用c语言编写的内置数据类型list、set等作为超类，子类中的覆盖实现可能无效
# 使用dict作为超类，子类中可能需要重构许多方法，UserDict方便继承

class _userDict(UserDict):

    def __missing__(self, key):
        """__getitem__, KeyError时调用"""
        if isinstance(key, str):
            # 避免进入无限递归
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.keys()

    def __setitem__(self, key, value):
        self.data[str(key)] = value


#=======================================================================
"""namedtuple"""
# 元组中各字段支持字符串索引
def _namedtuple():

    # 构建
    TupClass = namedtuple('MytupleClass', ['name', 'age', 'job'])
    # TupClass = namedtuple('MytupleClass', 'name, age, job')
    # TupClass = namedtuple('MytupleClass', 'name age job'])

    obj = TupClass('Tom', 12, 'coder')

    # 解析
    name, age, job = obj
    # name='Tom', age='12', job='coder'

    print('%s is %d years old %s' % obj)
    # Tom is 12 years old coder

    print('%s is %d years old %s' % ('Tom', 12, 'coder'))
    # Tom is 12 years old coder

    print(obj.__doc__)
    # MytupleClass(name, age, job)

    Point = namedtuple('point', ['x', 'y'])
    point = Point(1, 2)

    print("x=%d, y=%d" % (point.x, point.y))
    # x = 1, y = 2

    # 转换为有序字典
    point._asdict()
    # OrderedDict([('x', 1), ('y', 2)])