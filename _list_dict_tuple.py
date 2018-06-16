# -*- coding: utf-8 -*-

#----------------------------------------------------------------------
"""
列表
"""
color=[]
color = ['red','green','blue','orange']
len(color)                  #获取列表长度
sorted(color)               #返回正序列表，不改变原始串
max(color)                  #返回最大元素，min返回最小

#操作顺序
color.reverse()             #列表反转
color.sort(reverse=True)    #逆序
color.sort()                #正序

#修改、插入
color[0] = 'yellow'         #指定位修改
color.append('white')       #附加
color.insert(0,'pink')      #指定位插入

#查找
color.index('red')          #查找元素首次出现位置
'red' in color              #成员查找：True

#引用、复制
co = color                  #列表引用/别名, 通过co可修改color
                            #列表、字典具有引用性质
co = color[-1]              #复制最后一个元素
co = color[:]               #列表复制全部
co = color[1:3]             #切片复制2个元素
co = color[1:5:2]           #步长为2，复制位于[1,3]的两个元素

#遍历
for co in color:                #普通遍历
    print(co)
for idx,co in enumerate(color): #并行迭代
    print(idx,co)
co = [c for c in color]         #列表解析
zip([1,2],[4,5])                #实现两个列表的并行迭代，zip函数返回元组列表[(1,4),(2,5)]

#删除
del color[0]                #指定位删除
color.remove('white')       #指定元素删除,删除第一个被找到的元素
color.pop(1)                #删除并引用

#列表生成
[1,2,3] + [2,3,4]           #列表相加：[1, 2, 3, 2, 3, 4],不支持减法
                            #效率低于.extend()方法
[1,2]*2                     #列表相乘：[1, 2, 1, 2]
[None]*3                    #列表相乘：[None, None, None]
list(range(5))              #range创建：[0, 1, 2, 3, 4]
list(range(1, 5))           #range创建：[1, 2, 3, 4]
list('hello')               #['h', 'e', 'l', 'l', 'o']

#----------------------------------------------------------------------
"""
元组
"""
#元组内部元素不可修改，但元素变量可修改（变量可随意赋值）
dem = (200,50)      #赋值
dem[0]              #引用
dem = (100,100)     #重新赋值

#----------------------------------------------------------------------
"""
集合
"""
#不支持索引且自动去重
a= {1,4,4,3}       #a={1,3,4}

#----------------------------------------------------------------------
"""
字典

字典由键-值对构成，键值对也称为项
字典中不含相同的键，前者自动被覆盖
"""

items = [('name','Gumby'),('age',35)]
d = dict(items)                     #通过字典函数把其他数据类型映射为字典，d={'age':35,'name':'Gumby'}
c = d                               #字典引用/别名，通过c可操作d
c = d.copy()                        #浅复制,可能与python3不同
c = dict.fromkeys(['a','1'],None)   #生成键值为空的字典，c={'age':None,'name':None}

value = d['name']                   #通过键访问字典值，键名不存在时报错
value = d.get('name',None)          #get方法获取键值，键名不存在时返回None


d.has_key('name')                   #检查是否存在键名，True

d.items()                           #获取字典所有项列表，列表元素为元组,[('age',35), ('name','Gumby')]
d.iteritems()                       #返回字典项迭代器，使用.next()获取键值对元组
d.iterkeys()                        #返回字典键值迭代器                
d.values()                          #获取键值列表，无序
d.keys()                            #获取键名列表，无序

    
for key,value in d.items():         #项遍历
    print(key,value)

for key in d.keys():                #值遍历
    print(key)

d['name'] = 'Gumbye'                #直接修改键值
d['add'] = 'Chicago'                #键名不存在时，添加新的键值对
d.update({'age':25,'gender':'male'})#更新存在键值对，添加不存在的键值对

v = d.pop('add')                    #删除并引用
v = d.popitem()                     #随机pop，高效的逐个删除
del d['age']                        #删除指定键值对
d.clear()                           #清空字典

