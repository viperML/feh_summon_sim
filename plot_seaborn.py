import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import scipy

xlimit = 600

total_orbs_0 = np.loadtxt('total_orbs_0.txt.gz', dtype=int)
total_orbs_1 = np.loadtxt('total_orbs_1.txt.gz', dtype=int)
total_orbs_2 = np.loadtxt('total_orbs_2.txt.gz', dtype=int)
total_orbs_3 = np.loadtxt('total_orbs_3.txt.gz', dtype=int)


sns.set_style('dark')

# ax1 = sns.distplot(total_orbs_0, hist_kws=dict(cumulative=True, alpha=0.1), kde_kws=dict(cumulative=True))
ax1 = sns.kdeplot(total_orbs_0, cumulative=True, color='red')
ax1 = sns.kdeplot(total_orbs_1, cumulative=True, color='blue')
ax1 = sns.kdeplot(total_orbs_2, cumulative=True, color='green')
ax1 = sns.kdeplot(total_orbs_3, cumulative=True, color='gray')

ax1.set_xlim(right=xlimit, left=0)
ax1.set_xticks(np.arange(0,xlimit,50))

ax1.set_xlabel('Orbs spent', fontsize=15)
ax1.set_ylabel('Accumulated probability', fontsize=15)

plt.show()