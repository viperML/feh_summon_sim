import matplotlib.pyplot as plt
import numpy as np

angl = -80

total_heroes = np.load('total_heroes.npy')

if total_heroes[:,0].size == 3:
    specific_colors = ['#ffcdd2', '#ef9a9a', '#f44336',
                       '#c5cae9', '#9fa8da', '#3f51b5',
                       '#c8e6c9', '#a5d6a7', '#4caf50',
                       '#f5f5f5', '#e0e0e0', '#9e9e9e']
    expsize = 0.2
    explode = [0,0,expsize,
               0,0,expsize,
               0,0,expsize,
               0,0,expsize]
elif total_heroes[:,0].size == 4:
    specific_colors = ['#ffcdd2', '#ef9a9a', '#f44336', '#e53935',
                       '#c5cae9', '#9fa8da', '#3f51b5', '#3949ab',
                       '#c8e6c9', '#a5d6a7', '#4caf50', '#43a047',
                       '#f5f5f5', '#e0e0e0', '#9e9e9e', '#757575']
    expsize = 0.2
    explode = [0,0,expsize,expsize,
               0,0,expsize,expsize,
               0,0,expsize,expsize,
               0,0,expsize,expsize]

relative = np.empty_like(total_heroes)
relative[:] = total_heroes[:]
relative = relative.transpose().astype(float)
for i in range(4):
    buffer = relative[i] / relative[i].sum()
    relative[i] = buffer * 100

relative_string = np.char.mod('%1.1f', relative.flatten())
for i in range(relative_string.size):
    relative_string[i] = relative_string[i] + '%'
    relative_string[i] = relative_string[i].replace('0.0%', ' ')

fig, ax = plt.subplots()

size = 0.25

general_colors = ['red', 'blue', 'green', 'silver']

ax.pie(total_heroes.transpose().flatten(), radius=1, colors=specific_colors, explode=explode, labels=relative_string, startangle=angl, labeldistance=1.05,
    wedgeprops=dict(width=size, edgecolor='w'),
    textprops=dict(size='small'))

ax.pie(total_heroes.sum(axis=0), radius=1-size, colors=general_colors, autopct='%1.2f%%',pctdistance=0.5,startangle=angl,
    wedgeprops=dict(width=1-size, edgecolor='w'),
    textprops=dict(color='white'))




ax.set(aspect="equal", title='Color distribution')
plt.savefig('fig_pie.png')
plt.show()