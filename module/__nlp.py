# -*- coding:utf-8 -*-
import random
from math import ceil, log2
from time import sleep

import numpy as np
from matplotlib import pyplot as plt


class Inherit:
    def __init__(self):
        self.delta = 0.0001
        self.max_iter = 500
        self.boundary = [[-1, 2]]
        self.generations = 30

        self.len_chromo = list(map(lambda x: ceil(log2((x[1] - x[0]) / self.delta)), self.boundary))

        # self.fitfun = lambda x: 21.5 + x[0] * np.sin(4 * np.pi * x[0]) + x[1] * np.sin(20 * np.pi * x[1])
        self.fitfun = lambda x: (x * np.sin(10 * np.pi * x) + 2)

    def decoded(self, chromosomes):
        """种群解码"""
        decoded = np.zeros((chromosomes.shape[0], len(self.len_chromo)))
        for i, pop in enumerate(chromosomes):
            start = 0
            for j, length in enumerate(self.len_chromo):
                num = sum(map(lambda x, y: 2 ** x * y, np.arange(length - 1, -1, -1), pop[start:start + length]))
                lower, upper = self.boundary[j][:2]
                decoded[i, j] = 1.* num * (upper - lower) / (2 ** length - 1) + lower
                start += length
        return decoded

    def select(self, chromosomes, fitness):
        """适应度选择"""
        m, n = chromosomes.shape
        new = np.zeros((m, n), dtype=np.uint8)
        fitness = fitness.T[0]
        for i in range(m):
            index = random.sample(range(m), 3)
            subfit = fitness[index]
            max_index = index[np.where(subfit == subfit.max())[0][0]]
            new[i] = chromosomes[max_index]
        return new
        # 随机产生m个概率值
        # cum = np.cumsum(fitness / sum(fitness))
        # randoms = np.random.rand(chromosomes.shape[0])
        # for i, randoma in enumerate(randoms):
        #     new[i] = chromosomes[np.where(cum > randoma)[0][0]]
        # return new

    def crossover(self, population, p=0.8):
        """种群交叉"""
        m, n = population.shape
        pairs = int(m * p)
        if pairs % 2 != 0:
            pairs += 1
        index = random.sample(range(m), pairs)
        new = np.ones((m, n), dtype=np.uint8)
        _ = [i not in index for i in range(m)]
        new[_] = population[_]
        for i in range(0, pairs, 2):
            a = index[i]
            b = index[i + 1]
            cp = random.choice(range(1, n))
            new[a] = np.hstack((population[a, :cp], population[b, cp:]))
            new[b] = np.hstack((population[b, :cp], population[a, cp:]))
        return new

    def mutation(self, population, pm=0.02):
        """染色体变异"""
        new = np.copy(population)
        m, n = population.shape
        # 随机突变num个基因
        num = np.uint8(m * n * pm) or 1
        index = random.sample(range(m * n), num)
        for gene in index:
            # 确定变异基因位于第几个染色体
            chromosome = gene // n
            # 确定变异基因位于当前染色体的第几个基因位
            pos = gene % n
            if new[chromosome, pos]:
                new[chromosome, pos] = 0
            else:
                new[chromosome, pos] = 1
        return new

    def run(self):
        # 每次迭代得到的最优解
        optimalValues = []
        optimalSolution = []
        plt.figure(1)
        x = np.arange(*self.boundary[0], 0.0001)
        y = list(map(self.fitfun, x))
        # 第一代
        chromosomes = np.random.randint(0, 2, [self.generations, sum(self.len_chromo)])
        for i in range(self.max_iter):
            decoded = self.decoded(chromosomes)
            # 染色体适应度
            fitness = np.array(list(map(self.fitfun, decoded)))
            # 自然选择
            select = self.select(chromosomes, fitness)
            # 基因重组
            crossover = self.crossover(select)
            # 基因突变
            mutation = self.mutation(crossover)
            chromosomes = mutation
            final_decoded = self.decoded(mutation)
            final_fitness = np.array(list(map(self.fitfun, final_decoded)))
            # 动态显示
            plt.cla()
            plt.plot(x, y, linewidth=1)
            plt.title('generations:%d' % i)
            plt.scatter(final_decoded, final_fitness, final_fitness, 'r', linewidths=3)
            plt.pause(0.1)
            # 存储最优结果
            max_value = final_fitness.max()
            optimalValues.append(max_value)
            max_index = np.where(final_fitness == max_value)[0][0]
            max_solution = final_decoded[max_index]
            optimalSolution.append(max_solution)
        opt_value = max(optimalValues)
        opt_index = optimalValues.index(opt_value)
        opt_solution = optimalSolution[opt_index]
        print(opt_value)
        print(opt_solution)

# Inherit().run()
