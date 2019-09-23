import numpy as np
import matplotlib.pyplot as plt

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
    color = 'silver'
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
percentile90 = 0
percentile98 = 0
for i in range(1, cumulative_frequency.size):
    if cumulative_frequency[i] >= 50.0 and percentile50 == 0:
        percentile50 = i
    if cumulative_frequency[i] >= 90.0 and percentile90 == 0:
        percentile90 = i
    if cumulative_frequency[i] >= 98.0 and percentile98 == 0:
        percentile98 = i
    
print("")
print("Average:", end=" ")
print("%1.0f" % mu)
print("Median:", end=" ")
print(percentile50)
print("90th:", end=" ")
print(percentile90)
print("98th:", end=" ")
print(percentile98)
#print("Standard Deviation:", end=" ")
#print("%.2f" % sigma)

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
color01 = '#212121'
fig, ax = plt.subplots()

ax.plot(cumulative_frequency, color=color, linewidth=2.5, alpha=0.8)

ax.set_xticks(np.arange(0,x_data[0],x_data[1]))
ax.set_xlim(right=x_data[0], left=0)
#ax.set_ylim(bottom=2, top=99.5)
ax.set_yticks([0,10,20,30,40,50,60,70,80,90,100])
ax.set_xlabel("Orbs Spent", color=color01, fontsize=15)
ax.set_ylabel("Chance of success (%)", color=color01, fontsize=15)

plt.grid()

plt.savefig('fig_total_orbs_' + color + '.png')
plt.show()