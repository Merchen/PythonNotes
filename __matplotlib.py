# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import cnames
import matplotlib.patches as mpatches
import random

fig, axes = plt.subplots(2, 2, facecolor='white', figsize=(16,9))
fig.suptitle('Figure Subtitle', fontsize=20, fontweight='bold')

# figure页边距
fig.subplots_adjust(top=0.9,bottom=0.06, left=0.06, right=0.96)

# 设置不同子图间距
# plt.subplots_adjust(wspace=0.2, hspace=0.2)

########################################################################
### subplot(220)
########################################################################
ax = axes[0, 0]
x = np.random.randn(100).cumsum()

# 最大、最小值
minVal, maxVal = min(x), max(x)
minIndex = list(x).index(minVal)
maxIndex = list(x).index(maxVal)
interval = np.abs(maxVal - minVal)

# 绘制曲线
# axes[0, 0].plot(x, 'k--', drawstyle='dashed',alpha=0.3)

# 绘制直线
ax.plot(x, 'k--', linewidth=1, alpha=0.6, label='one')
ax.plot(x, 'b-', linewidth=1.3, drawstyle='steps-post', alpha=0.9, label='one')

# 设置标签
ax.text(0.99, 0.01, 'Stages',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes, color='k', fontsize=12,
        bbox={'facecolor':'y', 'alpha':0.2, 'pad':1})
box = dict(facecolor='y', pad=1, alpha=0.2)
# ax.set_xlabel('Stages')
ax.set_ylabel('Values',bbox=box, rotation='vertical')

# sub标题
ax.set_title('Important dates in 2008-2009 financial crisis', size=16, color='k')

ax.grid()

# X标注
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xticklabels(labels=['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')

# xy轴长度
# ax.axis([xmin, xmax, ymin, ymax])
ax.set_ylim([minVal - 0.1*interval, maxVal + 0.3*interval])
ax.set_xlim([-2, 102])

ax.legend(['dush', 'step'], loc='upper left', fontsize='x-small', shadow=True, ncol=1, framealpha=0.7)

# 添加文字注解
annotateData = [(minIndex, 'Min Value'), (maxIndex, 'Max Value')]
for id, label in annotateData:
    ax.annotate(label,
                xy=(id, x[id] + 0.2),
                xytext=(id, x[id] + 0.2*interval),
                arrowprops=dict(facecolor='r', shrink=0.05),
                alpha=0.9, size=12, color='r')

########################################################################
### subplot(221)
########################################################################
ax = axes[0, 1]

data = [[0.30, 0.15, 0.37, 0.27], [0.75, 0.52, 0.69, 0.36],
        [0.38, 0.67, 0.47, 0.63], [0.94, 0.18, 0.71, 0.64],
        [0.84, 0.90, 0.01, 0.65], [0.06, 0.59, 0.81, 0.06]]
index = ['one', 'two', 'three', 'four', 'five', 'six']
columns = ['A', 'B', 'C', 'D']
colors = cnames.values()

len_x= 15                   # 坐标轴长度
len_space=0.5               # 坐标轴首尾空白长度
len_inter = 1.0             # 不同组间隔
num_gp = len(data)          # 数据组数
num_dt = len(data[0])       # 每组数据数

colors = random.sample(colors, num_dt)  # 不同的颜色
width = (len_x - 2. * len_space - (num_gp - 1) * len_inter) / (num_dt * num_gp)
fpos = len_space
record = []
for i in range(num_gp):
    x = np.arange(fpos, fpos + width * num_dt, width)[:num_dt]
    ax.bar(x, data[i], width=width, color=colors, alpha=0.5)
    record.append(x)
    fpos = x[-1] + len_inter

# X标注
ax.set_xticks(np.array(record).mean(axis=1))
ax.set_xticklabels(labels=index, rotation=30, fontsize='small')

# 添加legend
patches = [mpatches.Patch(color=colors[i], label=col) for i, col in enumerate(columns)]
ax.legend(handles=patches, loc='upper left', fontsize='x-small', shadow=True, ncol=2, framealpha=0.7, title="Genus")

# x = random.randn(500)
# axes[0, 1].hist(x, color='r', bins=100, alpha=0.4)        # 柱形图
# x = np.arange(50)
# y = x + 10*random.rand(50)
# axes[1, 0].scatter(x,y,alpha=0.8)                         # 散点图

plt.show()