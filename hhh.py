import simhash
import hashlib

def _hash_str(source):
    if source == "":
        return 0
    else:
        x = ord(source[0]) << 7
        m = 1000003
        mask = 2 ** 128 - 1
        for c in source:
            x = ((x * m) ^ ord(c)) & mask
        x ^= len(source)
        if x == -1:
            x = -2
        x = bin(x).replace('0b', '').zfill(64)[-64:]
        return x

import numpy as np

a = ['我是', '中国', '人', '你说非', '幅度', '幅度']
b = ['他是', '中国', '人', '你非', '幅度', '幅度']
wa = [1, 2, 3, 4, 5, 6]
wb = [1, 2, 3, 4, 5, 6]
def fun(a, wa):
    res = np.zeros((len(a), 64))
    for i, word, weight in zip(range(len(a)), a, wa):
        b = res[i]
        for j, char in enumerate(_hash_str(word)):
            if char == '0':
                b[j] = -weight
            else:
                b[j] = weight
    sum = res.sum(axis=0)
    return np.where(sum > 0, 1, 0)

import time
s1 = fun(a, wa)
s2 = fun(b, wb)
print(s1)
print(s2)
import time




