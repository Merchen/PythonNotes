# -*- coding: utf-8 -*-
"""
伪随机数生成器
系统可预测，os中的urandom类接近真正随机
"""
import random


# random(self):
# random() -> x in the interval [0, 1)
random.random()
# 0.06825043796651353


# randint(self, a, b):
# Return random integer in range [a, b], including both end points
random.randint(1, 10)
# 2


# uniform(self, a, b):
# Get a random number in the range [a, b) or [a, b] depending on rounding.
random.uniform(1, 10)
# 6.038140705159564


# choice(self, seq):
# Choose a random element from a non-empty sequence.
random.choice(range(5))
# 2


# sample(self, population, k):
# Chooses k unique random elements from a population sequence or set
# sample(self, population, k)
random.sample(range(5), 1)
# [1]
random.sample(range(5), 2)
# [0, 2]
random.sample(range(5), 5)
# [2, 4, 1, 0, 3]


# randrange(self, start, stop=None, step=1, _int=int):
# Choose a random item from range(start, stop[, step])
random.randrange(1, 10)
# 6


# shuffle(self, x, random=None):
# Shuffle list x in place, and return None.
_ = list(range(10))
random.shuffle(_)
# _ = [7, 1, 8, 6, 4, 2, 5, 0, 9, 3]


# choices(self, population, weights=None, *, cum_weights=None, k=1):
# Return a k sized list of population elements chosen with replacement.
random.choices(range(5), k=6)
# [1, 4, 1, 0, 2, 1]
prop = [0.1, 0.2, 0.2, 0.4, 0.1]
random.choices(range(5), weights=prop, k=5)
#  [3, 3, 2, 4, 1]


# seed(self, a=None, version=2)
# Initialize internal state from hashable object.
# seed执行后, 随机数按指定方式循环生成期望值集
random.seed(1)
random.random()
# 0.13436424411240122
random.randint(1, 10)
# 2


# 不可再生生成随机数
rm = random.SystemRandom(x=1)
rm.random()
# 0.0326057730051178