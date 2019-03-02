import matplotlib.pyplot as plt
import numpy as np

colors1 = ['red', 'royalblue','lawngreen','silver']
colors2 = ['red', 'firebrick', 'royalblue', 'mediumblue', 'lawngreen', 'seagreen', 'silver', 'gray']
explode = [0,0.1,0,0.1,0,0.1,0,0.1]

total_heroes = np.loadtxt('total_heroes.txt', dtype=int)
data = np.append( sum(total_heroes[0:2]), total_heroes[2], axis=0).reshape((2,4)).transpose()

focus_percentages = data[:,1]/data.sum(1)

size= 0.8

fig1, ax1 = plt.subplots()
ax1.pie(data.sum(1), colors=colors1, autopct='%1.2f%%', pctdistance=0.4, wedgeprops=dict(width=size, edgecolor='w'))
ax1.pie(data.flatten(), colors=colors2, autopct='%1.2f%%', pctdistance=1.2, wedgeprops=dict(width=size/2, edgecolor='w'))


ax1.set(aspect="equal", title='Color distribution')

plt.show()