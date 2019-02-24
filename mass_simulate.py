import numpy as np
import feh_pull as feh
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

i = 1 # Generic counter


simulations = 2000

# Array with 'simulations' size
# Holds every result
N_results = np.empty((0,1), int)


while i < simulations+1:

    satisfied = False
    N = 0 # Number of pulls
    pity = 3 / 100

    # Full circle pulling
    while not satisfied:
        circle = feh.pull(pity)
        N += 1

        satisfied = any(five_star in circle[1] for five_star in (1, 2) )

        pity = pity + 0.25 / 100

    N_results = np.append( N_results, N)
    i += 1




# Plotting
d = np.diff(np.unique(N_results)).min()
left_of_first_bin = N_results.min() - float(d)/2
right_of_last_bin = N_results.max() + float(d)/2
plt.hist(N_results, np.arange(left_of_first_bin, right_of_last_bin + d, d), rwidth=0.95, density=True)
plt.xticks(np.arange(N_results.min(), N_results.max() + 1))

plt.show()