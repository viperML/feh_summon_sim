import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import scipy

xlimit = 1200

total_sessions = np.loadtxt('total_sessions.txt.gz', dtype=int)
total_orbs = np.loadtxt('total_orbs.txt.gz', dtype=int)


sns.set_style('dark')
ax1 = sns.distplot(total_orbs, hist_kws=dict(cumulative=True, alpha=0.1), kde_kws=dict(cumulative=True))
ax1.set_xlim(right=xlimit, left=0)
ax1.set_xticks(np.arange(0,xlimit,50))

plt.show()