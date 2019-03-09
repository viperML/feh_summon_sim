import numpy as np
import matplotlib.pyplot as plt

from tkinter import filedialog
from tkinter import *
import os

# Set to same number when planning to overlay plots
xlim = 1200
xstep = 100

# Prompt user to choose file
root = Tk()
file = filedialog.askopenfilename(initialdir = "./",title = "Select simulation data",filetypes = ((".gz files","total_orbs*.gz"),("all files","*.*")))
fpath, fname = os.path.split(file)
print(fname)

# Automatic color detection
if 'red' in fname:
    if 'any' in fname:
        color = 'darkred'
        title = 'Red Any'
    else:
        color = 'red'
        title = 'Red Specific'
elif 'blue' in fname:
    if 'any' in fname:
        color = 'darkblue'
        title = 'Blue Any'
    else:
        color = 'blue'
        title = 'Blue Specific'
elif 'green' in fname:
    if 'any' in fname:
        color = 'darkgreen'
        title = 'Green Any'
    else:
        color = 'green'
        title = 'Green Especific'
elif 'colorless' in fname:
    if 'any' in fname:
        color = 'gray'
        title = 'Colorless Any'
    else:
        color = 'silver'
        title = 'Colorless Specific'
else:
    color = 'fuchsia'
    title = ' '

print(title)

total_orbs = np.loadtxt(file, dtype=int)


orbs_frequency = np.zeros(total_orbs.max()+1)
cumulative_frequency = np.zeros_like(orbs_frequency)

# Calculate frequencies
for o in total_orbs:
    orbs_frequency[o] += 1

for i in range(1, orbs_frequency.size):
    cumulative_frequency[i] = cumulative_frequency[i-1] + orbs_frequency[i]
cumulative_frequency /= cumulative_frequency.max()/100

# Calculate average, std deviation, median and 90th

mu = sum(total_orbs) / total_orbs.size

sigma = (total_orbs - mu)**2
sigma = np.sqrt( sum(sigma) / sigma.size )

percentile50 = 0
percentile90 = 0
for i in range(1, cumulative_frequency.size):
    if cumulative_frequency[i] >= 50.0 and percentile50 == 0:
        percentile50 = i
    if cumulative_frequency[i] >= 90.0 and percentile90 == 0:
        percentile90 = i

print("Average:", end=" ")
print("%1.0f" % mu)
print("Median:", end=" ")
print(percentile50)
print("90th:", end=" ")
print(percentile90)
#print("Standard Deviation:", end=" ")
#print("%.2f" % sigma)


# Plotting
fig, ax = plt.subplots()


ax.plot(cumulative_frequency, color=color)

ax.set_xticks(np.arange(0,xlim,xstep))
ax.set_xlim(right=xlim, left=0)
#ax.set_ylim(bottom=2, top=99.5)
ax.set_yticks([2,5,10,20,30,40,50,60,70,80,90,100])
ax.set_xlabel("Orbs Spent")
ax.set_ylabel("P(X<x)")

plt.grid()
plt.savefig('fig_' + fname.replace('.txt.gz', '.png'))
plt.show()