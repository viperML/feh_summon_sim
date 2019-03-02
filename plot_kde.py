import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os.path

xlimit = 600

sns.set_style('dark')

if os.path.isfile('total_orbs_0.txt.gz'):
    total_orbs_0 = np.loadtxt('total_orbs_0.txt.gz', dtype=int)
    ax1 = sns.kdeplot(total_orbs_0, cumulative=True, color='red')
if os.path.isfile('total_orbs_1.txt.gz'):
    total_orbs_1 = np.loadtxt('total_orbs_1.txt.gz', dtype=int)
    ax1 = sns.kdeplot(total_orbs_1, cumulative=True, color='blue')
if os.path.isfile('total_orbs_2.txt.gz'):
    total_orbs_2 = np.loadtxt('total_orbs_2.txt.gz', dtype=int)
    ax1 = sns.kdeplot(total_orbs_2, cumulative=True, color='green')
if os.path.isfile('total_orbs_3.txt.gz'):
    total_orbs_3 = np.loadtxt('total_orbs_3.txt.gz', dtype=int)
    ax1 = sns.kdeplot(total_orbs_3, cumulative=True, color='grey')

if os.path.isfile('total_orbs.txt.gz'):
    total_orbs = np.loadtxt('total_orbs.txt.gz', dtype=int)
    ax1 = sns.kdeplot(total_orbs, cumulative=True, color='fuchsia')


# ax1 = sns.distplot(total_orbs_0, hist_kws=dict(cumulative=True, alpha=0.1), kde_kws=dict(cumulative=True))

ax1.set_xlim(right=xlimit, left=0)
ax1.set_xticks(np.arange(0,xlimit,50))

ax1.set_xlabel('Orbs spent', fontsize=15)
ax1.set_ylabel('Accumulated probability', fontsize=15)

plt.show()