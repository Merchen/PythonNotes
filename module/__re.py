# -*- coding: utf-8 -*-
import re

# (…)	        封闭表达式
# […]	        匹配字符集中的任意字符，[]内特殊字符无意思，[\.]与[.]相同
# [^…]	        不匹配字符集中的任意字符
# [x-y]	        匹配x和y之间的任意字符
# {m, n}	    匹配表达式m至n次
# {m}	        匹配表达式m次
# {m,}	        匹配表达式至少m次
# .	            匹配除\n外的任意字符
# \	            转义字符， 若匹配'\'应使用'\\\\'，编译器将'\\\\'处理为'\\'匹配，正则对象中'\\'处理为'\',亦可直接使用r'\\'
# +	            至少匹配一次表达式
# ?	            至多匹配一次表达式
# *	            匹配表达式零次或多次
# *?	        非贪婪模式匹配
# $ 或 \Z	    字符串结尾位置，$多行模式匹配每一行
# ^ 或 \A	    字符串开始位置，^多行模式匹配每一行
# \d|\D	        等价于[0-9] [^0-9]
# \w|\W	        等价于[A-Za-z0-9_] [^A-Za-z0-9_]
# \s|\S	        等价于[\n\t\r\v\f [^\n\t\r\v\f]空白字符
# \b|\B	        匹配边界|不匹配边界
# |	            逻辑或，从左到右匹配，一旦匹配成功则跳过表达式
# (?P<name>…) 	分组，额外指定组别名name，(?P<id>abc){2}
# (?P=name)	    引用别名的name的分组内容，(?P<id>\d)abc(?P=id)
# (?:…)	        (…)的不分组版本，(?:abc){2}
# (?:iLmsux)	定义不同的匹配模式，(?i)abc
# (?=…)	        之后的字符串需匹配表达式才能匹配，a(?=\d)
# (?!...)	    之后的字符串不需匹配表达式才能匹配，a(?!\d)
# (?<=…)	    之前的字符串需匹配表达式才能匹配，(?<=\d)a
# (?<!...)	    之前的字符串不需匹配表达式才能匹配,，(?<=\d)a

# 正则对象的一些方法
# 'There (was a (copper))', 分组0:There was a copper、1:was a copper、2:copper
# .group()和.group(0), 返回匹配到的全部字符串包括各分组中的内容
# .group([group1, …]), 返回指定组匹配的字符串
# .groups():等价于.group(1,2,...,last), 返回所有分组匹配的字符串
# .span([group]), 返回指定组匹配字符串在源串中的起始位置
# flags：re.I(忽略大小写)、M(多行模式)、S(点任意匹配模式)、等

# 将字符串形式的正则表达式编译为Pattern对象
# 编译后的正则对象可多次使用
_ = re.compile('\d+')
_ = _.findall('1234.12')
# ['1234', '12']
_ = re.findall('\d+', '1234.12')
# ['1234', '12']

# 匹配以pattern开始的string
# 匹配成功则返回匹配对象，失败返回None
_ = re.match('fo(o)', 'fooffff')
# .group() = 'foo'; .group(0)=foo; .group(1)=o

# 匹配含有pattern的string
# 匹配成功则返回匹配对象，失败返回None
_ = re.search('\d+', '1234.12', flags=0)

# 查找string中全部非重复pattern
# 若含分组表达式, 成功返回匹配组列表，失败返回[]
# 不含分组表达式时, 返回匹配结果
_ = re.findall('\d+', '1234.12')
# ['1234', '12']
re.findall('(?:&nbsp;){2,}\d+', 'Windows&nbsp;&nbsp;2000')
# ['&nbsp;&nbsp;2000'], 不含分组时
re.findall('(&nbsp;){2,}\d+', 'Windows&nbsp;&nbsp;2000')
# ['&nbsp;'], 含一个分组时
re.findall('((?:&nbsp;){1,})(\d+)', 'Windows&nbsp;&nbsp;2000')
# [('&nbsp;&nbsp;', '2000')], 含多个分组时

# 搜索string,返回一个顺序访问每一个匹配结果的迭代器
# 相比findall更省内存，使用.next()方法移动到下一个匹配对象
_ = [i.group() for i in re.finditer('\d+', '1234.12')]
# 1234  12

# 使用repl替换string中替换找到的正则项pattern
# re.subn方法返回替换的总数
re.sub('(\d+)\.(\d+)', r'\2.\1', '1234.12', count=0, flags=0)
# '12.1234', r'\2.\1' == '\\2.\\1'


# =======================================================================
"""[]"""
# 匹配数字和字母
re.findall('[A-Za-z0-9]+', 'Aww.wqewq123.213')
# ['Aww', 'wqewq123', '213']
re.findall('[a-z\d]+', 'Aww.wqewq123.213', re.I)
# 'Aww', 'wqewq123', '213']
re.findall('[\w.]+@[\w.]+\.\w+',' ben@forta.com ben@urgent.forta.com')
# ['ben@forta.com', 'ben@urgent.forta.com']


# =======================================================================
"""{}"""
re.findall('(&nbsp;){2,}\d', 'Windows&nbsp;&nbsp;2000')


# =======================================================================
"""边界/多行"""
re.findall(r'\b(正则|对象)\b', u'正则 对象')
# ['正则', '对象']
re.findall(r'\B-\B', u'nine-dight')
# []

re.findall(r'^\s*\w+', 'aa\n bb\n cc')
# ['aa'], 单行模式
re.findall(r'^\s*\w+', 'aa\n bb\n cc', re.MULTILINE)
# ['aa', ' bb', ' cc'], 多行模式
re.findall(r'(?m)^\s*\w+', 'aa\n bb\n cc')
# ['aa', ' bb', ' cc'], 多行模式
re.findall(r'(?m)^\s*(\w+)', 'aa\n bb\n cc')
# ['aa', 'bb', 'cc'], 多行模式, 仅返回分组内容


# =======================================================================
"""回溯/分组"""
re.findall(r'(<H(\d)>.*?<H\2>)','<H1>Welcome to my Homepage<H1>\n<H2>Invalid<H3>')
# [('<H1>Welcome to my Homepage<H1>', '1')]

# 格式化日期
re.sub(r'(\d{1,2})/(\d{1,2})/(\d{4}|\d{2})', r'\3/\2/\1', '27/2/2016')
# '2016/2/27'

# 格式化HTML代码
re.sub(r'\*([^*]+)\*',r'<em>\1</em>','Hello **World!*')
# 'Hello *<em>World!</em>'
# 贪婪模式
re.sub(r'\*(.+)\*', r'<em>\1</em>', '*Hello* *World*!')
# '<em>Hello* *World</em>!'
# 非贪婪模式
re.sub(r'\*(.+?)\*', r'<em>\1</em>', '*Hello* *World*!')
# '<em>Hello</em> <em>World</em>!'

re.sub(r'(<H1>)(.*?)(</H1>)', r'\1\2\3','<H1>Welcome to my homepage</H1>')


_ = re.search('(?<=\d){4}(?:-)(\d{2}).(\d{2})', '2018-06-07')
# _.groups() = ('06', '07')

# 重命名分组
re.findall(r'(?P<name>John)((?P=name))(\d+)', 'JohnJohn2012')
# [('John', 'John', '2012')]
re.findall(r'(John)(\1)(\d+)', 'JohnJohn2012')
# [('John', 'John', '2012')]

# =======================================================================
"""前后查找"""
# (?=...) 向前查找, 不消耗字符
re.findall('.+(?=:)', 'http://www.forta.com')
# ['http']

# (?<=...) 向后查找, 不消耗字符
re.findall('(?<=//)\w*\.\w*\.\w+', 'http://www.forta.com')
# ['www.forta.com']

_ = re.search(r'(?<=<H(\d)>).*?(?=</H\1>)','<H1>Welcome to my homepage</H1>')
# _.group() = 'Welcome to my homepage'
# _.groups() = ('1',)

re.findall(r'(\d{3})(?(1))', '(123456-7890')


# =======================================================================
"""条件"""
# re.findall(r"(<A\s+[^>]+>\s*)?(<IMG\s+[^>]+>)(?(1)\s*</A>)",
#            '<A HREF="/home"><IMG SRG="/images/spacer.gif"></A>'
#            '<IMG SRG="/images/spacer.gif">')

# (?(1)\s*</A>)表示如果分组1匹配成功, 则继续匹配\s*</A>
re.search('(<A\s+[^>]+>\s*)?(<IMG\s+[^>]+>)((?(1)\s*</A>))',
          '<A HREF="/home"><IMG SRC=" /images/home.gif"></A>').group()
# '<A HREF="/home"><IMG SRC=" /images/home.gif"></A>'

# (?(1)\)|-)表示如果分组1匹配成功则匹配')', 否则匹配'-'
re.search('(\()?\d{3}(?(1)\)|-)\d{3}-\d{4}', '(123)456-7890').group()
# '(123)456-7890'
re.search('(\()?\d{3}(?(1)\)|-)\d{3}-\d{4}', '123-456-7890').group()
# '123-456-7890'
re.search('(\()?\d{3}(?(1)\)|-)\d{3}-\d{4}', '(123-456-7890').group()
# '123-456-7890', 默认不匹配'('？？？？？？
# 匹配')'不成功自动回退？？？

# '-'匹配成功继续匹配d{4}
re.search('\d{5}(-)?(?(1)\d{4})', '12345-4444').group()
# '12345-4444'


# =======================================================================
"""函数替换"""
dic = {}
def repl(match):
    code = match.group(1)
    try:
        # 在字典中查找对应键，并返回值
        return str(eval(code, dic))
    except SyntaxError:
        # 添加至字典并返回空串，被匹配的部分被替换为空串
        dic.update(eval('dict(%s)'%code))
        return ''
re.sub(r'\[(.+?)\]', repl, '[x = 3][y = 1] This sum of [x] and [y] is [x + y]')
# ' This sum of 3 and 1 is 4'

re.sub('\w+', lambda m:m.group().upper(), 'Welcome to my homepage.')
# 'WELCOME TO MY HOMEPAGE.'