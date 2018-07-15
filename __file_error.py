# -*- coding: utf-8 -*-
import os
from warnings import warn

########################################################################
###  文件读取与异常捕捉
########################################################################
"""
open(name, mode=None, buffering=None)
    mode: 读取'r'、写入'w'、附加‘a’、读取并写入‘r+’、二进制'b'、文本't'、默认‘rt’
          w模式下，已经写入的字符被覆盖
    return: 返回文本对象迭代器，可使用list序列化全部行
    善于利用try-except相比if-else语句可提高程序效率
.read(n):
    读取n个字符数并移动游标, n缺省时读取全部, 无数据可读时返回空串''
.readline(n)
    读取一行数据，以\n作为行识别标志，最多读取n个字符，缺省时不限制字符
.readliens()
    返回列表，其将文件中的单行作为列表的一个元素
.writelines()
    将列表中元素作为一行写入文件
.seek(offset, whence)
    使用偏移量，移动文件游标
    offset: 相对参考点的偏移字符数
    whence: 定义offet的偏移参考点,默认文件开头(0), 2表示文件尾
    如.seek(0,0) 回到文件开头
.tell()
    返回游标所在位置
"""

FILE_NAME = r"C:\Users\MERLIN\Desktop\Python\mycsv.csv"


def absPath(filename):
    """获取文件绝对路径"""
    if filename:
        i = len(filename)
        while i and filename[i - 1] not in '/\\':
            i -= 1
        if i == 0:
            filename = os.path.join(os.path.dirname(__file__), filename)
    else:
        raise ("Error file path!")
    return filename


def writeFile(filename, data, method='a'):
    """向文件写入数据"""
    try:
        with open(filename, method) as f:
            f.write(data)
    except(IOError, TypeError) as err:
        if isinstance(err, IOError):
            raise ('Data Write Failure')
        else:
            warn('Data Type Error!')
    except Exception:
        raise


def readFile(filepath, separator=','):
    """文件内容读取成列表 """
    contents = ''
    try:
        file = absPath(filepath)
        if os.path.exists(file):
            with open(file, 'r') as f:
                # lines = []
                # for line in f:
                #     lines += line
                contents = f.read().strip()  # 从文件获取全部数据

                # 返回包含所有行的列表,每个元素为文件中的一行数据
                # 替换'\n'为','，然后将','作为字符串分隔符以获取包含所有元素的列表
                # csv中同行不同元素使用','分割,不同行使用‘\n’分割
                contents = contents.replace('\n', separator).split(separator)
    except Exception as err:
        print(err)
    else:
        pass
    finally:  # 无论是否异常均会执行，一般用于异常清理
        return contents


def rw_test():
    with open('open.dat', 'w') as f:
        f.write('first 1\nsecond 2\nthird 3')
        f.seek(0, 0)
        f.write('document-header')
    with open('open.dat') as f:
        for line in f:
            print(line)  # document-header 2
            # third 3
        print(f.readlines())  # 返回[]
        f.seek(19)
        print(f.read(), f.tell())  # third 3 26
        if f.read() == '':
            print(True)  # True


########################################################################
###  异常类
########################################################################
class NameError(Exception):
    """自定义异常类"""

    def __init__(self, value=None):
        super(NameError, self).__init__()
        self.value = value

    def __str__(self):
        """定义直接引用对象时的返回值"""
        return repr(self.value)


# raise NameError('Error string')


