# -*- coding: utf-8 -*-

import re

"""
正则表达式--匹配文本片段的模式

(…)	    封闭表达式                                 
[…]	    匹配字符集中的任意字符                      
[^…]	不匹配字符集中的任意字符                    
[x-y]	匹配x和y之间的任意字符                      
{m, n}	匹配表达式m至n次                           
{m}	    匹配表达式m次                             
{m,}	匹配表达式至少m次                           
.	    匹配除\n外的任意字符                         
\	    转义字符
+	    至少匹配一次表达式
?	    至多匹配一次表达式
*	    匹配表达式零次或多次
*?	    非贪婪模式匹配
$ 或 \Z	字符串结尾位置，$多行模式匹配每一行
^ 或 \A	字符串开始位置，^多行模式匹配每一行
\d	等价于[0-9]，与\D相反
\w	等价于[A-Za-z0-9]，与\W相反
\s	等价于[\n\t\r\v\f]，空格字符
|	逻辑或，从左到右匹配，一旦匹配成功则跳过表达式

(?P<name>…)	分组，额外指定组别名name，(?P<id>abc){2}
(?P=name)	引用别名的name的分组内容，(?P<id>\d)abc(?P=id)
(?:…)	(…)的不分组版本，(?:abc){2}
(?:iLmsux)	定义不同的匹配模式，(?i)abc
(?=…)	之后的字符串需匹配表达式才能匹配，a(?=\d)
(?!...)	之后的字符串不需匹配表达式才能匹配，a(?!\d)
(?<=…)	之前的字符串需匹配表达式才能匹配，(?<=\d)a
(?<!...)	之前的字符串不需匹配表达式才能匹配,，(?<=\d)a
"""
#
# 匹配'\'应使用'\\\\'：编译器将'\\\\'处理为'\\'匹配，正则对象中'\\'处理为'\',亦可直接使用r'\\'
# []内转义字符不需要，[\.]与[.]相同

# 将字符串形式的正则表达式编译为Pattern对象
# re.compile(Pattern[, flag])

# 匹配以pattern开始的string，匹配成功则返回匹配对象，失败返回None
# re.match(pattern,string,flags=0)

# 匹配含有pattern的string，匹配成功则返回匹配对象，失败返回None
# re.search(pattern,string,flags=0)

# 查找string中全部非重复pattern，成功返回匹配组列表，失败返回[]
# re.findall(pattern, string)

# 搜索string,返回一个顺序访问每一个匹配结果的迭代器.相比findall更省内存
# 使用.next()方法移动到下一个匹配对象
# re.finditer(pattern, string, flags=0)

# 使用repl替换string中替换找到的正则项pattern,re.subn方法返回替换的总数
# re.sub(pattern, repl, string, count=0, flags=0)

# flags：re.I(忽略大小写)、M(多行模式)、S(点任意匹配模式)、等

# 正则对象的一些方法
# 'There (was a (copper))', 分组0:There was a copper、1:was a copper、2:copper
# .group()和.group(0), 返回全部分组
# .group([group1, …]), 返回指定组匹配的字符串
# .groups():等价于.group(1,2,...,last), 返回所有分组匹配的字符串
# .span([group]), 返回指定组匹配字符串在源串中的起始位置

# s.group()=s.group(0)=foo, s.group(1)=o
s = re.match('fo(o)', 'fooffff')
# s为None
s = re.match('foo', 'dddfooff')

string = r'Hello World!'

# 将正则表达式编译成对象
pattern = re.compile('l[od]')

# s=None,仅可从头匹配字符串
s = pattern.match(string)

# s.group()='lo'、s.groups()=()、s.span(0)=(3, 5)
s = pattern.search(string)

# s=['lo', 'ld']
s = pattern.findall(string)

# s.groups()=('Hello', 'World')、s.group(1)='Hello'
pattern = re.compile(r'(\w+) (\w+)')
s = pattern.search(string)

# s='World Hello!'
s = pattern.sub(r'\2 \1', string)

# 格式化日期
re.sub(r'(\d{1,2})/(\d{1,2})/(\d{4}|\d{2})', r'\3/\2/\1', '27/2/2016')
# 格式化HTML代码, 'Hello *<em>World!</em>'
re.sub(r'\*([^\*]+)\*',r'<em>\1</em>','Hello **World!*')

# 贪婪模式, '<em>Hello* *World</em>!'
re.sub(r'\*(.+)\*', r'<em>\1</em>', '*Hello* *World*!')
# 非贪婪模式, 'Hello '<em>Hello</em> <em>World</em>!'
re.sub(r'\*(.+?)\*', r'<em>\1</em>', '*Hello* *World*!')

# s.groups()=('06','07')
s = re.search('(?<=\d){4}(?:-)(\d{2}).(\d{2})', '2018-06-07')


def templates():
    pattern = re.compile(r'\[(.+?)\]')
    scope = {}
    def replacement(match):
        code = match.group(1)
        try:
            # 在字典中查找对应键，并返回值
            return str(eval(code,scope))
        except SyntaxError:
            # 添加至字典并返回空串，被匹配的部分被替换为空串
            exec code in scope
            return ''
    text = '[x = 3][y = 1]' \
           'this sum of [x] and [y] is [x + y]'
    print(pattern.sub(replacement,text))


if __name__ == '__main__':
    # templates()
    # res = re.search(r'(\\)(d)',r's\dd\d')
    # print(res.group(0))

    pass