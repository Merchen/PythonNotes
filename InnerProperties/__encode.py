import codecs
import os

# python3的str对象以unicode格式编码
# 从python3的str对象中获取字符(Unicode)等价于从python 2的Unicode对象中获取字符

# unicode万国码, 对所有字符使用2个字节; utf-8, 对英文使用一个字节

# Python默认使用UTF-8编码, utf_8, utf8, U8一致
# bytes经过适当转换可变成字符，如utf-8和gbk格式的bytes

# encode(指明字节序列编码方式)--码位转换成字节序列的过程
# unicode -> bytes    unicode(内存) -> utf-8(文件)
#
# decode(指明字节序列编码方式)--字节序列转换为码位的过程
# bytes -> unicode    utf-8(文件) -> unicode(内存)
#
# 以下两种写入效果一直, 打开文件均显示'你好'
# 打开文件时自动decode
# with open('t1.txt', 'wb') as f1, open('t2.txt', 'w', encoding='utf-8') as f2:
#     f1.write('你好'.encode())
#     f2.write('你好')

def fun1():
    len('12345'.encode('ASCII'))
    # 5
    len('12345'.encode('UTF-8'))
    # 5
    len('12345'.encode('UTF-32'))
    # 24

    string = '中国China'

    unicode = bytes(string, encoding='unicode_escape')
    # b'\\u4e2d\\u56fdChina'

    utf8 = bytes(string, encoding='utf-8')
    # b'\xe4\xb8\xad\xe5\x9b\xbdChina'

    utf8_arr = bytearray(utf8)
    # bytearray(b'\xe4\xb8\xad\xe5\x9b\xbdChina')

    # byte和bytearray对象的单个元素是整数(0-255)、切片是原始对象
    # byte[0] != byte[:1]

    s = utf8[0]
    # 228

    s = utf8[:1]
    # b'\xe4'

    string.encode('unicode_escape')
    # b'\\u4e2d\\u56fdChina', 字符串编码为bytes对象

    string.encode('utf-8')
    # b'\xe4\xb8\xad\xe5\x9b\xbdChina', 默认'utf-8', 与ASCII兼容

    unicode.decode()
    # '\\u4e2d\\u56fdChina'

    unicode.decode('unicode_escape')
    # '中国China'

    utf8.decode()
    # '中国China'

    utf8.decode('utf-8')
    # '中国China'

    strTest = 'Montréal'
    try:
        # 特定编码序列存在无法转换为文本的字节
        strTest.encode('iso8859_7')
    except UnicodeEncodeError:
        strTest.encode('cp1252')

    bytTest = b'Montr\xe9al'
    try:
        # 文本中存在目标编码未定义的字符
        bytTest.decode('utf-8')
    except UnicodeDecodeError:
        bytTest.decode('cp1252')

with open('__re1.py', encoding='utf-8') as f:
    contents = f.readlines()
    for line in contents:
        pass
        # s = repr(line.encode('utf-8')).lstrip('b').strip('\'').strip('\"').rstrip('\\n').replace('\\\\','\\').replace('\\t','\t')
        # print(eval("b'%s'"%s))

def toUnicode(filename):
    """文件转为Unicode格式"""
    with codecs.open(filename, mode='r', encoding='utf-8') as f:
        text = f.read().encode()
        new = 'unicode_' + str(os.path.basename(filename))
        with open(new, 'w') as f1:
            f1.write(str(text))


def fromUnicode(filename):
    """unicode转为utf-8"""
    with codecs.open(filename, mode='r') as f:
        text = eval(f.read()).decode('utf-8')
        print(text)
        new = 'utf8_' + str(os.path.basename(filename))
        with codecs.open(new, 'w', encoding='utf-8') as f1:
            f1.write(text)



