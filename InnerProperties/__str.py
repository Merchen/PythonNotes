# -*- coding: utf-8 -*-
"""
Python3.6之后方法，直接在字符串中使用变量
字符串元素的值不可改变,s[1]='r'非法
"""
import math
from math import pi as PI

#=====================================================
"""格式化/拼接"""
string = ' aBc def '

string.title()
# ' Abc Def '

string.upper()
# ' ABC DEF '

string.lower()
# ' abc def '

string.center(12, '*')
# '* aBc def **', 指定宽度，两边填充字符

buf = ["%s=%s" % (k, v) for k, v in dict(a=1, b=2).items()]
# ['a=1', 'b=2']
";".join(buf)
# 'a=1;b=2'， 多字符串(>10)连接时效率高

buf = 'ab ' + 'cd ' + 'ef '
# 'ab cd ef '， str为不可变对象，多字符串连接时效率低

eval('%s + %s' % ('12', '45'))
# 57

'{},{},and {}'.format(*'abc')
# 'a,b,and c'

'{0},{1} and {0}'.format(*('a','b'))
# 'a,b and a'

'{c1},{c0} and {c2}'.format(c0=1, c1=2, c2=3)
# '2,1 and 3'

'{c1},{c0} and {c2}'.format(**dict(c0=1,c1=2,c2=3))
# '2,1 and 3'

'{mod.__name__} module defines {mod.pi} for pi'.format(mod=math)
# 'math module defines 3.141592653589793 for pi'

f's={PI}'
# 's=3.141592653589793'

'{:f}'.format(10)
# '10.000000'

'{:3}'.format(10)
# ' 10'

'{:+<10.3f}'.format(10)
# '10.000++++', 左右中对齐<、>、^,使用$空白填充


#=====================================================
"""边界"""
string = ' aBc def '

string.startswith(' aB')
# True

string.rstrip()
# ' aBc def'

string.rstrip('f ')
# ' aBc de'

string.lstrip()
# 'aBc def '

string.strip()
# 'aBc def'

string.strip(' a')
# 'Bc def'


#=====================================================
"""查找/替换/分割"""
string = ' aBc def '

string.replace('Bc', 'aa')
# ' aaa def '

string.find('B')
# 2

string.count('a')
# 1

string.split()
# ['aBc', 'def']


#=====================================================
"""检测类型"""
'123'.isalnum()
# True
'abc'.isalpha()
# True
isinstance('ssd', str)
# True