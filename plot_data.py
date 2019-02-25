import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# PLOTTING
fig = plt.figure()
gs = gridspec.GridSpec(nrows=2, ncols=2, height_ratios=[4, 1])
plt.tight_layout()

# Number of sessions
d = np.diff(np.unique(total_pulls)).min()
left_of_first_bin = total_pulls.min() - float(d)/2
right_of_last_bin = total_pulls.max() + float(d)/2

ax0 = fig.add_subplot(gs[0, 0])
ax0.hist(total_pulls, np.arange(left_of_first_bin, right_of_last_bin + d, d), rwidth=1, density=True)
#ax0.xticks(np.arange(total_orbs.min(), total_orbs.max() + 1))
ax0.set_title("Number of sessions")

# Number of orbs
ax1 = fig.add_subplot(gs[0,1])
ax1.hist(total_orbs, bins='fd', density=True)
ax1.set_title("Number of orbs spent")

plt.show()