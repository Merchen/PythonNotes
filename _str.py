# -*- coding: utf-8 -*-

import math
from math import pi as PI


"""
字符串基本操作
"""
s = ' aBc def '     # 字符串元素的值不可改变,s[1]='r'非法
g = h = 'hi'        # 更改h的值，不影响g
s.title()           # 单词首位大写：' Abc Def '
s.upper()           # 全部大写：' ABC DEF
s.lower()           # 全部小写：' abc def '
s.rstrip()          # 去右边空格：' aBc def'
s.lstrip()          # 去左边空格：'aBc def '
s.strip()           # 去两边空格：'aBc def'
s.rstrip('f ')      # 去右边字符：' aBc de'
s.strip(' a')       # 去两边字符：'Bc def'
s.replace('Bc', 'aa')  # 替换字符：' aaa def '
s.find('B')         # 查找字符位置：2
s.count('a')        # 查找字符个数，1
s.split()           # 分割字符串，默认空格，['aBc', 'def']
s + g               # 合并字符：' aBc def hi'
str()

"""
字符串格式化
"""
s.center(12, '*')       # 指定宽度，两边填充字符，'* aBc def **'
path = r'c:\nowhere'    # 使用原始字符串
w = '%s + %s' % (s, g)  # 字符串格式化：'aBc def  + hi'

s = 'abc'
c = '{},{},and {}'.format(s[0], s[1], s[2])             # c='a,b and c'
c = '{0},{1} and {0}'.format(s[0], s[1])                # c='a,b and a'
c = '{c1},{} and {c2}'.format(s[0], c1=s[1], c2=s[2])   # c='b,a and c'
c = '{nm} is appro {v}'.format(v=PI, nm='pi')           # c='pi is appro 3.14159265359'

t = '{mod.__name__} module defines {mod.pi} for pi'
c = t.format(mod=math)      # 'math module defines 3.14159265359 for pi'

# c = f's={s}'              #python 3.6之后方法，直接在字符串中使用变量
'{:f}'.format(10)           # 转换输出浮点：'10.000000'
'{:3}'.format(10)           # 指定宽度输出：' 10'
'{:$<6.2f}'.format(10)      # 指定宽度和精度：'10.00$'，宽度为整数部分+小数点+小数部分位数和
# 左右中对齐<、>、^,使用$空白填充

# 字符串join[list]
dic = {"a": "1", "b": "2"}
buf = ["%s=%s" % (k, v) for k, v in dic.items()]  # buf=['a=1', 'b=2']
new = ";".join(buf) # new='a=1;b=2'


"""
更改字符串编码
"""
# 不同字符编码占用的空间不同
# -*- coding: utf-8 -*- #文件开头的编码声明
len('12345'.encode('ASCII'))    # 5
len('12345'.encode('UTF-8'))    # 5
len('12345'.encode('UTF-32'))   # 24


"""
判断字符串类型
"""
'123'.isalnum()         # 判断是否为数字，True
'abc'.isalpha()         # 判断是否为字母，True
isinstance('ssd',str)   # 判断是否是字符串
