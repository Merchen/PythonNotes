# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import cnames
import matplotlib.patches as mpatches
import random
import networkx as nx

# =====================================================
"""subplot(220)"""


def fun1():
    fig, axes = plt.subplots(2, 2, facecolor='white', figsize=(16, 9))
    fig.suptitle('Figure Subtitle', fontsize=20, fontweight='bold')
    fig.subplots_adjust(top=0.9, bottom=0.06, left=0.06, right=0.96)

    ax1, ax2 = axes[0, :]
    ax1.grid()
    ax1.set_title('Important dates in 2008-2009 financial crisis', size=16, color='k')

    array = np.random.randn(100).cumsum()
    # 绘制直线
    ax1.plot(array, 'k--', linewidth=1, alpha=0.6, label='one')
    ax1.plot(array, 'b-', linewidth=1.3, drawstyle='steps-post', alpha=0.9, label='one')
    # 设置标签
    ax1.text(0.99, 0.01, 'Stages', verticalalignment='bottom', horizontalalignment='right', transform=ax1.transAxes,
             color='k', fontsize=12, bbox={'facecolor': 'y', 'alpha': 0.2, 'pad': 1})
    # X标注
    ax1.set_xticks([0, 25, 50, 75, 100])
    ax1.set_xticklabels(labels=['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
    # ax.set_xlabel('Stages')
    ax1.set_ylabel('Values', bbox=dict(facecolor='y', pad=1, alpha=0.2), rotation='vertical')
    # xy轴长度
    # ax.axis([xmin, xmax, ymin, ymax])
    ax1.set_ylim([array.min() - 0.1 * (array.max() - array.min()), array.max() + 0.3 * (array.max() - array.min())])
    ax1.set_xlim([-2, 102])
    # 图注
    ax1.legend(['dush', 'step'], loc='upper left', fontsize='x-small', shadow=True, ncol=1, framealpha=0.7)
    # 添加文字注解
    minX = np.where(array.min() == array)[0][0]
    maxX = np.where(array.max() == array)[0][0]
    annotateData = [(minX, 'Min Value'), (maxX, 'Max Value')]
    for id, label in annotateData:
        ax1.annotate(label, xy=(id, array[id] + 0.2), xytext=(id, array[id] + 0.2 * (array.max() - array.min())),
                     arrowprops=dict(facecolor='r', shrink=0.05), alpha=0.9, size=12, color='r')
    # subplot2
    data = [[0.30, 0.15, 0.37, 0.27], [0.75, 0.52, 0.69, 0.36], [0.38, 0.67, 0.47, 0.63], [0.94, 0.18, 0.71, 0.64],
            [0.84, 0.90, 0.01, 0.65], [0.06, 0.59, 0.81, 0.06]]
    index = ['one', 'two', 'three', 'four', 'five', 'six']
    columns = ['A', 'B', 'C', 'D']
    colors = cnames.values()
    len_x = 15  # 坐标轴长度
    len_space = 0.5  # 坐标轴首尾空白长度
    len_inter = 1.0  # 不同组间隔
    num_gp = len(data)  # 数据组数
    num_dt = len(data[0])  # 每组数据数
    colors = random.sample(list(colors), num_dt)  # 不同的颜色
    width = (len_x - 2. * len_space - (num_gp - 1) * len_inter) / (num_dt * num_gp)
    fpos = len_space
    record = []
    for i in range(num_gp):
        x = np.arange(fpos, fpos + width * num_dt, width)[:num_dt]
        ax2.bar(x, data[i], width=width, color=colors, alpha=0.5)
        record.append(x)
        fpos = x[-1] + len_inter
    # X标注
    ax2.set_xticks(np.array(record).mean(axis=1))
    ax2.set_xticklabels(labels=index, rotation=30, fontsize='small')
    # 添加legend
    patches = [mpatches.Patch(color=colors[i], label=col) for i, col in enumerate(columns)]
    ax2.legend(handles=patches, loc='upper left', fontsize='x-small', shadow=True, ncol=2, framealpha=0.7,
               title="Genus")
    # x = random.randn(500)
    # axes[0, 1].hist(x, color='r', bins=100, alpha=0.4)        # 柱形图
    # x = np.arange(50)
    # y = x + 10*random.rand(50)
    # axes[1, 0].scatter(x,y,alpha=0.8)                         # 散点图
    plt.show()


# fun1()


from nltk.corpus import wordnet

# def traverse(graph, start, node):
#      graph.depth[node.name] = node.shortest_path_distance(start)
#      for child in node.hyponyms():
#          graph.add_edge(node.name, child.name)
#          traverse(graph, start, child)


import matplotlib.pyplot as plt
import networkx as nx


