# -*- coding: utf-8 -*-

""""""
"""
文件读取与异常捕捉

善于利用try-except相比if-else语句可提高程序效率
"""

# 两行数据['firstline,1,2,3\n', 'secondline,4,5,6\n']
# 路径中使用/和\效果一致
FILE_NAME = r"C:\Users\MERLIN\Desktop\Python\mycsv.csv"


def get_file_abspath(filename=FILE_NAME):
    """
    ：获取文件绝对路径

    :param filename:
    :return:
    """
    if filename:
        i = len(filename)
        while i and filename[i - 1] not in '/\\':
            i -= 1
        if i == 0:
            from os.path import abspath, dirname, join
            filename = join(abspath(dirname(__file__)), filename)
    else:
        raise ("Error file path!")
    return filename


def write_contents(filename=FILE_NAME,data=None,method='a'):
    """
    ：文件写入

    :param filename:
    :return:
    """
    try:
        with open(filename,method) as f:
            f.write(data)
    except(IOError,TypeError) as err:
        # IO读写错误时，打印出错信息
        if isinstance(err,IOError):

            raise('Error happened while writing data!')
        # 数据类型错误
        else:
            from  warnings import warn
            warn('Error Date Type!')
    except Exception:
        raise


def read_contents(filename=FILE_NAME,separator=','):
    """
    :文件内容读取成列表

    :param filename:文件绝对路径
    :return:
    """
    # 文件内容，执行状态字符串
    str_result, contents = '', ''
    # 文件元素列表
    content_list = []

    try:
        from os.path import exists
        filename = get_file_abspath(filename)
        if exists(filename):
            # open参数：读取'r'、写入'w'、附加‘a’、读取并写入‘r+’,默认‘r’
            with open(filename, 'r') as f:
                # 返回包含所有行的列表,每个元素为文件中的一行数据
                # lines = []
                # for line in f:
                #     lines +=

                # 返回文件文本字符串
                contents = f.read().strip()

                # 替换'\n'为','，然后将','作为字符串分隔符以获取包含所有元素的列表
                # csv中同行不同元素使用','分割,不同行使用‘\n’分割
                content_list = contents.replace('\n',separator).split(separator)

    # except FileNotFoundError as err: Python 3
    except Exception as err:
        str_result = 'Error:%s' %err

    # try执行成功后执行
    else:
        str_result = "Execute successfully"

    # 无论是否异常，均会执行，一般用于异常清理
    finally:
        return content_list if contents else str_result


# # 写入新行，含4个元素,换行符不可少
# ndata = 'thirdline,7,8,9\n'
# file_object.write(ndata)

