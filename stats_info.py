import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

file = 'total_orbs.npy'

total_orbs = np.load(file)
print("Select color output:")
print("[00] Red        [10] Red Any")
print("[01] Blue       [11] Blue Any")
print("[02] Green      [12] Green Any")
print("[03] Colorless  [13] Colorless Any")
print("[04] Other      [14] Other Any")
color_input = int(input(": "))

if color_input == 0:
    color = 'red'
elif color_input == 10:
    color = 'darkred'
elif color_input == 1:
    color = 'blue'
elif color_input == 11:
    color = 'darkblue'
elif color_input == 2:
    color = 'green'
elif color_input == 12:
    color = 'darkgreen'
elif color_input == 3:
    color = 'gray'
elif color_input == 13:
    color = '#555555'
elif color_input == 4:
    color = 'fuchsia'
elif color_input == 14:
    color = 'mediumslateblue'
else:
    print("Wrong input")
    quit()



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
percentile80 = 0
percentile90 = 0
percentile98 = 0
for i in range(1, cumulative_frequency.size):
    if cumulative_frequency[i] >= 50.0 and percentile50 == 0:
        percentile50 = i
    if cumulative_frequency[i] >= 80.0 and percentile80 == 0:
        percentile80 = i
    if cumulative_frequency[i] >= 90.0 and percentile90 == 0:
        percentile90 = i
    if cumulative_frequency[i] >= 98.0 and percentile98 == 0:
        percentile98 = i


print("")

if color_input == 0 or color_input == 10:
    print("Rojo:")
elif color_input == 1 or color_input == 11:
    print("Azul:")
elif color_input == 2 or color_input == 12:
    print("Verde:")
elif color_input == 3 or color_input == 13:
    print("Gris:")

print("Mediana:", end=" ")
print(percentile50)
print("Media:", end=" ")
print("%1.0f" % mu)
print("Percentil 80%:", end=" ")
print(percentile80)
print("Percentil 90%:", end=" ")
print(percentile90)
print("98th:", end=" ")
print(percentile98)
#print("Standard Deviation:", end=" ")
#print("%.2f" % sigma)


# Set X limits and tick size
print("")
print("x limit: [Default previous data]")
x_data = [0, 0]
x_data[0] = input(": ")
if x_data[0] == '':
    x_data = np.loadtxt('x_data.npy', dtype=int)
else:
    x_data[0] = int(x_data[0])
    print("x step:")
    x_data[1] = int(input(": "))
    np.savetxt('x_data.npy', x_data, fmt='% 4d')


# Plotting
sns.set_style("whitegrid", {
    'axes.edgecolor': '.8',
    'axes.grid': True,
    'font.family': ['nintendoP_Skip-D_003'],
    'grid.color': '.9',
    'grid.linestyle': '--',
    'xtick.color': '.2',
    'ytick.color': '.2',
})
sns.set_context("poster")

fig, ax = plt.subplots()

ax.plot(cumulative_frequency, color=color, linewidth=5)

ax.set_xlim(right=x_data[0], left=0)
ax.set_xticks(np.arange(0,x_data[0]+x_data[1],x_data[1]))

ax.set_yticks(np.arange(0,110,10))
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
#ax.set_xlabel("Orbs Spent", fontsize=30, labelpad=20)
#ax.set_ylabel("Chance of success (%)",fontsize=30, labelpad=20)

plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
fig.set_size_inches(11, 8, forward=True)

plt.savefig('fig/total_orbs_' + color + '.png')
plt.show()