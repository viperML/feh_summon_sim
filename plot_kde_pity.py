import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os.path

xlimit = 0.1

sns.set_style('dark')

if os.path.isfile('total_pity_max_0.txt.gz'):
    total_pity_max_0 = np.loadtxt('total_pity_max_0.txt.gz')
    ax1 = sns.kdeplot(total_pity_max_0, cumulative=True, color='red')
if os.path.isfile('total_pity_max_1.txt.gz'):
    total_pity_max_1 = np.loadtxt('total_pity_max_1.txt.gz')
    ax1 = sns.kdeplot(total_pity_max_1, cumulative=True, color='blue')
if os.path.isfile('total_pity_max_2.txt.gz'):
    total_pity_max_2 = np.loadtxt('total_pity_max_2.txt.gz')
    ax1 = sns.kdeplot(total_pity_max_2, cumulative=True, color='green')
if os.path.isfile('total_pity_max_3.txt.gz'):
    total_pity_max_3 = np.loadtxt('total_pity_max_3.txt.gz')
    ax1 = sns.kdeplot(total_pity_max_3, cumulative=True, color='grey')

if os.path.isfile('total_pity_max.txt.gz'):
    total_pity_max = np.loadtxt('total_pity_max.txt.gz')
    ax1 = sns.kdeplot(total_pity_max, cumulative=True, color='fuchsia')


# ax1 = sns.distplot(total_pity_max_0, hist_kws=dict(cumulative=True, alpha=0.1), kde_kws=dict(cumulative=True))

ax1.set_xlim(right=xlimit)
#ax1.set_xticks(np.arange(0,xlimit,50))

ax1.set_xlabel('Pity Reached', fontsize=15)
ax1.set_ylabel('Accumulated probability', fontsize=15)

plt.show()