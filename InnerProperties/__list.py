
########################################################################
###  列表list
########################################################################

color = ['red', 'green', 'blue', 'orange']
len(color)
# 4


#=====================================================
"""排序"""
color = ['red', 'green', 'blue', 'orange']

sorted(color, reverse=False)
# ['blue', 'green', 'orange', 'red'], 非就地

max(color)
# 'red'

color.reverse()
# ['orange', 'blue', 'green', 'red']， 就地反转

color.sort()
# ['blue', 'green', 'orange', 'red']， 就地升序

color.sort(reverse=True)
# ['red', 'orange', 'green', 'blue']， 就地逆序


#=====================================================
"""修改"""
color = ['red', 'orange', 'green', 'blue']
color[0] = 'yellow'
# ['yellow', 'orange', 'green', 'blue']

color.append('red')
# ['yellow', 'orange', 'green', 'blue', 'red']

color.insert(0, 'pink')
# ['pink', 'yellow', 'orange', 'green', 'blue', 'red']

color.extend([1, 2])
# ['pink', 'yellow', 'orange', 'green', 'blue', 'red', 1, 2]


#=====================================================
"""查找/遍历/解析"""
color = ['red', 'orange', 'green', 'blue']
color.index('red')
# 5 元素首次出现位置
if 'red' in color:
    # 遍历查找
    pass

# 普通遍历
for co in color:
    pass

# 并行迭代
for idx, co in enumerate(color):
    print(idx, co)

# zip函数返回元组列表[(1,4),(2,5)]
zip([1, 2], [4, 5])

# 列表解析，生成列表速度优于循环append
arr = [i + 1 for i in range(3)]
# [1, 2, 3]


#=====================================================
"""切片"""
# 列表引用/别名, 通过co可修改color，列表、字典具有引用性质
# 切片方式获得的列表为深复制
c1 = color = ['pink', 'yellow', 'orange', 'green', 'blue', 'red']

c2 = color[-1]
# 'red'

c3 = color[:]
# ['pink', 'yellow', 'orange', 'green', 'blue', 'red']

c4 = color[1:3]
# ['yellow', 'orange']

c5 = color[1:5:2]
# ['yellow', 'green']

color[1:3] = [1, 2]
# ['pink', 1, 2, 'green', 'blue', 'red'], 切片形式赋值


#=====================================================
"""删除"""
color = ['pink', 'yellow', 'orange', 'green', 'blue', 'red']

del color[0]
# ['yellow', 'orange', 'green', 'blue', 'red']

color.remove('orange')
# ['yellow', 'green', 'blue', 'red']

color.pop(1)
# green, ['yellow', 'blue', 'red'], 随机pop（高效逐个删除）


#=====================================================
"""生成"""
arr1 = [1, 2, 3] + [2, 3, 4]  # 不支持减法, 效率低于extend
# [1, 2, 3, 2, 3, 4]

arr2 = [1, 2] * 2
# [1, 2, 1, 2]

arr3 = [None] * 3
# [None, None, None]

arr4 = [[]] * 3
# [[], [], []]

list(range(5))
# [0, 1, 2, 3, 4]

list('hello')
# ['h', 'e', 'l', 'l', 'o']


#=====================================================
"""运算"""
arr5 = [1, 2, 3]
# id(arr) = 345464219336
arr5 *= 2  # [1, 2, 3, 1, 2, 3]
# id(arr) = 345464219336