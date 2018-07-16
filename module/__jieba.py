import jieba
from functools import reduce
from operator import itemgetter, add

# 信息的冗余程度与每个符号出现的概率有关

# 不确定性函数关于概率单调递减、独立符号产生的不确定性等于各自不确定之和
# f(p1, p2)=,f(p1) + f(p2)
# f(p) = -log(p)满足: log(p1*p2) = log(p1) + log(p2)

# 信源的平均不确定性为信息熵，假定各符号相互独立可得：H(U) = ∑plogp
# 系统混乱则信息熵大(系统中各信号出现概率相同时信息熵最大)

def fun1():

    # 全模式
    list(jieba.cut('我来到北京大学', cut_all=True))

    # 精确模式，返回迭代对象
    list(jieba.cut('我来到北京大学', cut_all=False))
    # 精确模式，返回list
    jieba.lcut('他来到北京大学理科二号楼')

    # 搜索引擎模式
    list(jieba.cut_for_search('小明毕业与北京大学，后在美国哈弗大学深造'))

    text = '小明毕业与北京大学，后在美国哈弗大学深造。'*10000

    import time
    iterator = jieba.cut(text)

    # print(time.time())
    # iterator = jieba.cut(text)
    # for i in iterator:
    #     pass
    #
    # print(time.time())
    # lres = jieba.lcut(text)
    # for i in lres:
    #     pass
    # print(time.time()

phase = '你 中国 人 是 中国 人 哪 中国 人 里 中国 人 的 中国 '.split()

from operator import itemgetter
from collections import defaultdict, Counter
from math import log2


class FindNewWords(object):
    def __init__(self, engine=None):
        self.engine = engine
        self.wdict = dict()
        self.w2dict = dict()

        self.w_entropy = dict()
        self.w2_entropy = dict()

        self.new_words = dict()
        pass

    def create_edge_dict(self, phase):
        update_word_edge = self.update_word_edge

        # dict like:{'word':[0, [], []]}
        wdict, w2dict = self.wdict, self.w2dict

        length = len(phase)
        if length == 1:
            update_word_edge(wdict, phase[0], '', '')
        else:
            # update edge word in wdict
            update_word_edge(wdict, phase[0], '', phase[1])
            update_word_edge(wdict, phase[-1], phase[-2], '')

            # update edge word in w2dict
            try:
                right = phase[2]
                left = phase[-3]
            except IndexError:
                # only two words
                update_word_edge(w2dict, phase[0] + '+' + phase[1], '', '')
                return wdict, w2dict
            else:
                update_word_edge(w2dict, phase[0] + '+' + phase[1], '', right)
                update_word_edge(w2dict, phase[-2] + '+' + phase[-1], left, '')

            # update other word in wdict and w2dict
            for i in range(1, len(phase) - 2):
                # wdict
                update_word_edge(wdict, phase[i], phase[i - 1], phase[i + 1])
                # w2dict
                update_word_edge(w2dict, phase[i] + '+' + phase[i + 1], phase[i - 1], phase[i + 2])

            # update the penultimate word in wdict
            update_word_edge(wdict, phase[-2], phase[-3], phase[-1])
        return self.wdict, self.w2dict

    @staticmethod
    def update_word_edge(dic: dict, word: str, left: str = '', right: str = ''):
        try:
            value = dic[word]
            value[0] += 1
            value[1].append(left)
            value[2].append(right)
        except:
            dic[word] = [0, [left], [right]]

    @staticmethod
    def entropy(data: list):
        length = len(data)
        psum = 0
        for count in Counter(data).values():
            p = 1. * count / length
            psum += p * log2(p)
        return -psum

    def calculate_entropy(self, dic: dict):
        info = {}
        for key, val in dic.items():
            info[key] = self.entropy(val[1]) + self.entropy(val[2])
        return info

    def filter_words(self, wdict: dict, w2dict: dict):
        new_words = {}
        for key, value in w2dict.items():
            try:
                left, right = key.split('+')
            except ValueError:
                print("Error split '%s' to two words by '+'!" % key)
            else:
                if value > (wdict[left] + wdict[right])/2.:
                    new_words[key] = value
        return new_words


nw = FindNewWords()
wdict, w2dict = nw.create_edge_dict(phase)
print(wdict)
print(w2dict)
winfo = nw.calculate_entropy(wdict)
print(winfo)
w2info = nw.calculate_entropy(w2dict)
print(w2info)
new_word = nw.filter_words(winfo, w2info)

print(new_word)
# print(res[0])
# print(res[1].keys()

# def entropy(data):
#     length = len(data)
#     def fun(x):
#         p = 1. * x / length
#         return p * log2(p)
#     fun = lambda x:log2(1.*x/length)*x/length
#     return -reduce(add, map(fun, Counter(data).values()))

# print(timeit.timeit('entropy(range(1000000))', setup="from __main__ import entropy", number=1))
# print(timeit.timeit('entropy1(range(1000000))', setup="from __main__ import entropy1", number=1))

