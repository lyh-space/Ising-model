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

T_list = np.linspace(0.02, 2, 100)

m1_list = []
m2_list = []

for T in T_list:
    ep = 1
    m = 0.1
    while ep > 1e-3:
        m1 = np.tanh(m/T)
        ep = np.abs(m1 - m)
        m = m1
    m1_list.append(m)

for T in T_list:
    ep = 1
    m = -0.1
    while ep > 1e-3:
        m1 = np.tanh(m/T)
        ep = np.abs(m1 - m)
        m = m1
    m2_list.append(m)

fig, ax = plt.subplots(figsize=(1.9685, 1.4764), dpi=300, constrained_layout=True)

ax.plot(T_list, m1_list, linewidth=1.5, color='k')
ax.plot(T_list, m2_list, linewidth=1.5, color='k')

ax.scatter([1], [0], s=2, color='red')

ax.text(0.03, 1.35, r'$m$', color="k", fontsize=9.5)
ax.text(0.65, 0.95, r'$m_0$', color="k", fontsize=9.5)
ax.text(0.65, -1.05, r'$-m_0$', color="k", fontsize=9.5)
ax.text(2, -0.3, r'$T$', color="k", fontsize=9.5)

ax.text(0.5, -0.3, r'$T=T_c$', color="red", fontsize=9.5)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

ax.set_ylim(-1.5, 1.5)
ax.set_xticks([])
ax.set_yticks([])

plt.savefig('Phase diagram of order parameter m and temperature without external field.pdf', dpi=300)
plt.show()
