# -*- coding: utf-8 -*-

import math

#-------------------------------------------------------------------------
"""
运算

基本逻辑运算符：not and or in 
条件语句：if while for
"""

1 / 2           #1
1. / 2          #0.5

num = 12.35
int(num)        #12
float(num)      #12.35
str(num)        #'12.35'
math.ceil(num)  #13.0
math.sqrt(9)    #3.0


#-------------------------------------------------------------------------
"""
bool语句
"""
bool('')                  #False
bool('0')                 #True
bool(0)                   #False
bool(23)                  #True
bool(None)                #False

a = 2 and 1               #and、or语句符合短路逻辑，即表示式值确定后终止判断


#-------------------------------------------------------------------------
"""
is语句（同一元素符）
"""
num1 = num2 = 10          #整型对象，is语句与==语句一致
num3 = 10
print(num2 is num1)       #True
print(num3 is num1)       #True

lst1 = lst2 = [1,2,3]
lst3 = [1,2,3]
print(lst2 is lst1)       #True，引用对象
print(lst2 == lst1)       #True
print(lst3 is lst1)       #False,非引用对象
print(lst3 == lst1)       #True

#-------------------------------------------------------------------------
"""
in语句（成员资格）
"""
's' in 'search'           #True
'ch' in 'search'          #True


#-------------------------------------------------------------------------
"""
if语句
"""
a, b, c = 1, 5, 3          #序列解包，多元素使用元组赋值
a, b = b, a                #交换
if a >= b and a >= c:
	max_num = a
elif b >= a and b >= c:
	max_num = b
else:
	max_num = c
s = 'max[{},{},{}]={}'.format(a,b,c,max_num) 
print(s)    #max[1,5,3]=5

a = True
c = 2 if a else 0         #三元表达式，a为真返回2，否则返回0


#-------------------------------------------------------------------------
"""
while语句
"""
while True:
	city = raw_input("Input your favorite city:")
	if city == 'q':
		break
	else:
		print("Input 'q' to exit!")


#-------------------------------------------------------------------------
"""
assert语句
"""
#断言方法，语句不成立时终止程序
age = 10
assert 0 < age < 10

#-------------------------------------------------------------------------
"""
控制语句
"""
#break：#跳转出循环
#continue：直接进入下次循环
#return：返回上层函数
#pass:什么都不错
#del：删除对象，删除列表对象的引用不影响原列表
