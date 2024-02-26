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

xx = np.linspace(-5, 5, 100)
y1 = xx**2 / 2 - np.log(2*np.cosh(xx/0.45))
y2 = xx**2 / 2 - np.log(2*np.cosh(xx))
y3 = xx**2 / 2 - np.log(2*np.cosh(xx/10))

s = 1
xxx = [s, s]
yyy1 = [0, s]

fig, ax = plt.subplots(figsize=(1.9685, 1.4764), dpi=300, constrained_layout=True)

ax.plot(xx, y1, linewidth=1.5, zorder=2, color="b")
ax.plot(xx, y2, linewidth=1.5, zorder=2, color="r")
ax.plot(xx, y3, linewidth=1.5, zorder=2, color="k")

ax.plot([2.25, 2.25], [0, -2.4], '--', linewidth=1.2, color='k', zorder=1)
ax.plot([-2.25, -2.25], [0, -2.4], '--', linewidth=1.2, color='k', zorder=1)
ax.scatter([2.25, -2.25], [-2.4, -2.4], s=5, color='black', zorder=6)

ax.text(-3.85, -0.9, r'$-m_0$', color="k", fontsize=10.5)
ax.text(2.35, -0.9, r'$m_0$', color="k", fontsize=10.5)

ax.text(0.2, 11, r'$F(m)$', color="k", fontsize=10.5)
ax.text(4.8, -1, r'$m$', color="k", fontsize=10.5)

ax.text(3.6, -2.6, r'$T<T_c$', color="b", fontsize=9, zorder=7)
ax.text(3.65, 1.9, r'$T=T_c$', color="r", fontsize=9, zorder=7)
ax.text(2, 7, r'$T>T_c$', color="k", fontsize=9, zorder=7)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

ax.set_xticks([])
ax.set_yticks([])

plt.savefig('Free energy landscape without external field at different temperatures.pdf', dpi=300)
plt.show()
