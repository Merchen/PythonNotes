# -*- coding: utf-8 -*-

import os
import re  # 正则搜索库
import sys

#当前所在目录绝对路径
#os.getcwd()
ROOT_PATH = os.path.dirname(__file__)
#上级绝对路径
FATHER_PATH = os.path.abspath(os.path.join(ROOT_PATH, ".."))

#文件内容查询条件
RE_QUERY = ''
#文件过滤条件
FILENAME_CONTAINS = None


def serch_file_contents(dirname = ROOT_PATH,
                        re_query = RE_QUERY,
                        fn_contains = FILENAME_CONTAINS):
    """
    递归查找包含指定内容的文件指定文件内容

    :param dirname: 查找路径
    :param re_query: 查找内容
    :param fn_contains: 文件名称条件
    :return: 包含指定内容的文件列表
    """
    pattern = re.compile(re_query)  #编译为正则对象
    result =  []                    #搜索结果列表

    #递归路径下的各目录
    for path,dirnames,filenames in os.walk(dirname):
        #遍历当前目录所有文件 
        for fname in filenames:
            #文件搜索过滤
            search = False
            if fn_contains:
                if fn_contains in fname:
                    search = True
            else:
                search = True
            #执行搜索
            if search:
                fpath = os.path.join(path,fname)    
                with open(fpath,'r') as f:          
                    if pattern.search(f.read()) is not None:
                        result.append(fpath)
    if len(result):
        print('The following files were found:')
        for res in result:
            print(res)
    else:
        print("Unfound file.")
            

def uniq_syspath():
    """编译系统环境变量去重"""
    sys.path = list(set(sys.path))
    # i = 0
    # while i < len(sys.path)-1:
    #     value = sys.path[i]
    #     j = i + 1
    #     while j <= len(sys.path)-1:
    #         if sys.path[j] == value:
    #             del sys.path[j]
    #         else:
    #                 j += 1
    #     i += 1


def append_syspath(path=ROOT_PATH):
    """编译系统添加环境变量"""
    if path not in sys.path:
        sys.path.append(path)


if __name__ == '__main__':
    pass

    serch_file_contents(r'C:\Users\MERLIN\Desktop\Python\vntrader','EVENT_CTA_LOG','py')
    # append_syspath()
#     # print(sys.path)