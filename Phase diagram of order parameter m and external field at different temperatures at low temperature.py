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

B1_list = np.linspace(-0.3, 0.3, 100)

m1_list = []
m2_list = []

for B in B1_list:
    ep = 1
    m = 0.1
    while ep > 1e-3:
        m1 = np.tanh(m/0.75 + B)
        ep = np.abs(m1 - m)
        m = m1
    m1_list.append(m)

for B in B1_list:
    ep = 1
    m = -0.1
    while ep > 1e-3:
        m1 = np.tanh(m/0.75 + B)
        ep = np.abs(m1 - m)
        m = m1
    m2_list.append(m)

m3_list = []
m4_list = []

for B in B1_list:
    ep = 1
    m = 0.1
    while ep > 1e-3:
        m1 = np.tanh(m/0.5 + B)
        ep = np.abs(m1 - m)
        m = m1
    m3_list.append(m)

for B in B1_list:
    ep = 1
    m = -0.1
    while ep > 1e-3:
        m1 = np.tanh(m/0.5 + B)
        ep = np.abs(m1 - m)
        m = m1
    m4_list.append(m)

m5_list = []
m6_list = []

for B in B1_list:
    ep = 1
    m = 0.1
    while ep > 1e-3:
        m1 = np.tanh(m/0.3 + B)
        ep = np.abs(m1 - m)
        m = m1
    m5_list.append(m)

for B in B1_list:
    ep = 1
    m = -0.1
    while ep > 1e-3:
        m1 = np.tanh(m/0.3 + B)
        ep = np.abs(m1 - m)
        m = m1
    m6_list.append(m)


fig, ax = plt.subplots(figsize=(1.9685, 1.4764), dpi=300, constrained_layout=True)

ax.plot(B1_list, m1_list, linewidth=1.5, color='r', zorder=3)
ax.plot(B1_list, m2_list, linewidth=1.5, color='r', zorder=3)

ax.plot(B1_list, m3_list, linewidth=1.5, color='b', zorder=2)
ax.plot(B1_list, m4_list, linewidth=1.5, color='b', zorder=2)

ax.plot(B1_list, m5_list, linewidth=1.5, color='k', zorder=1)
ax.plot(B1_list, m6_list, linewidth=1.5, color='k', zorder=1)

ax.text(0.01, 1.35, r'$m$', color="k", fontsize=9.5)
ax.text(0.3, -0.25, r'$B$', color="k", fontsize=9.5)

ax.text(-0.33, 1.2, r'$T_1 < T_2 < T_3 < T_c$', color="k", fontsize=9.5)
ax.text(-0.28, 0.6, r'$T_1$', color="k", fontsize=9.5)
ax.text(-0.15, 0.5, r'$T_2$', color="b", fontsize=9.5)
ax.text(-0.08, 0.4, r'$T_3$', color="r", fontsize=9.5)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

ax.set_ylim(-1.5, 1.5)
ax.set_xticks([])
ax.set_yticks([])

plt.savefig('Phase diagram of order parameter m and external field at different temperatures at low temperature.pdf', dpi=300)
plt.show()
