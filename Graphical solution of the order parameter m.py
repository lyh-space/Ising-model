# -- coding:utf-8 --
# Author: Yuhao Li
# date: 2023/12/21
# Python version: 3.11.4

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

config = {
    "font.family": 'serif',
    "font.size": 12,
    "mathtext.fontset": 'stix',
    "font.serif": ['Times New Roman'],
}
rcParams.update(config)
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

xx = np.linspace(-1.5, 1.5, 100)
y1 = xx
y2 = np.tanh(xx)
y3 = np.tanh(xx / 0.3)
y4 = np.tanh(xx / 2)

s = 1
xxx = [s, s]
yyy1 = [0, s]

fig, ax = plt.subplots(figsize=(1.9685, 1.4764), dpi=300, constrained_layout=True)

ax.plot(xx, y1, linewidth=1.5, color='black', zorder=2)
ax.plot(xx, y2, linewidth=1.5, color='red', zorder=5)
ax.plot(xx, y3, linewidth=1.5, color='blue', zorder=4)
ax.plot(xx, y4, linewidth=1.5, color='green', zorder=3)
ax.plot([1, 1], [0, 1], '--', linewidth=1.2, color='gray', zorder=1)
ax.plot([-1, -1], [0, -1], '--', linewidth=1.2, color='gray', zorder=1)
ax.scatter([1, -1], [1, -1], s=5, color='black', zorder=6)

ax.text(-1.5, 1.2, r'$y=m$', color="k", fontsize=9.5)
ax.text(-1.5, 0.8, r'$y=\tanh(\beta Jzm)$', color="k", fontsize=9.5)

ax.text(-1.2, 0.1, r'$-m_0$', color="k", fontsize=10.5)
ax.text(0.9, -0.25, r'$m_0$', color="k", fontsize=10.5)

ax.text(0.05, 1.44, r'$y$', color="k", fontsize=10.5)
ax.text(1.45, -0.25, r'$m$', color="k", fontsize=10.5)

ax.text(0.3, 1.1, r'$T<T_c$', color="b", fontsize=9, zorder=7)
ax.text(0, 0.55, r'$T=T_c$', color="r", fontsize=9, zorder=7)
ax.text(1.1, 0.2, r'$T>T_c$', color="g", fontsize=9, zorder=7)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

ax.set_xticks([])
ax.set_yticks([])

plt.savefig('Graphical solution of the order parameter m.pdf', dpi=300)
plt.show()
