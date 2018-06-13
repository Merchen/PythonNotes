# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:49:32 2018

@author: MERLIN
"""

import re
import os
from datetime import datetime

#将字符串形式的正则表达式编译为Pattern对象
#re.compile(Pattern[, flag])

#匹配以pattern开始的string，匹配成功则返回匹配对象，失败返回None
#re.match(pattern,string,flags=0)

#匹配含有pattern的string，匹配成功则返回匹配对象，失败返回None
#re.search(pattern,string,flags=0)

#查找string中全部非重复pattern，成功返回匹配组列表，失败返回[]
#re.findall(pattern, string)

#搜索string,返回一个顺序访问每一个匹配结果的迭代器.相比findall更省内存
#使用.next()方法移动到下一个匹配对象
#re.finditer(pattern, string, flags=0)

#使用repl替换string中替换找到的正则项pattern,re.subn方法返回替换的总数
#re.sub(pattern, repl, string, count=0, flags=0)

#flags：re.I(忽略大小写)、M(多行模式)、S(点任意匹配模式)、等

#正则对象的一些方法
#.group([group1, …]):返回指定组匹配的字符串
#.groups():等价于.group(1,2,...,last),返回所有分组匹配的字符串
#.span([group]):返回指定组匹配字符串在源串中的起始位置


s = re.match('foo','fooffff')       #s.group()=foo
s = re.match('foo','dddfooff')      #s为None   

string = r'Hello World!'

pattern = re.compile('l[od]')       #将正则表达式编译成对象
s = pattern.match(string)           #s=None,仅可从头匹配字符串
s = pattern.search(string)          #s.group()='lo'、s.groups()=()、s.span(0)=(3, 5)
s = pattern.findall(string)         #s=['lo', 'ld']

pattern = re.compile(r'(\w+) (\w+)')
s = pattern.search(string)          #s.groups()=('Hello', 'World')、s.group(1)='Hello'

s = pattern.sub(r'\2 \1',string)    #s='World Hello!'
s = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{4}|\d{2})',r'\3/\2/\1','27/2/2016')    #格式化日期
s = re.search('(?<=\d){4}(?:-)(\d{2}).(\d{2})','2018-06-07')                #s.groups()=('06','07')





# 将根目录路径添加到环境变量中
#ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
#os.sys.path.append(ROOT_PATH)

def fun(argf):  
    print(1)
    def fun_in():  #函数内部定义的函数仅在调用时执行
        print(4)
        argf()
    print(2)
    return fun_in 
@fun    
def test():  
    print(3) 

if __name__ == '__main__':
    
#    fun1=fun(test)  
#    print(3)
#    fun1()  
    test()
    print(10)
    #输出结果1 2 3 4
