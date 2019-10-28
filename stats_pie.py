import matplotlib.pyplot as plt
import numpy as np
import sys # DEBUG

angl = -80

pool = np.load('pool_permanent.npy')
pool = np.append( pool, [np.load('pool_focus_heroes.npy')], axis=0)
total = [np.sum(pool[0]), np.sum(pool[1]), np.sum(pool[2])]
pity = np.load('pool_focus_pity.npy')


specific_colors = ['#ffcdd2', '#ef9a9a', '#ff3d4c',
                    '#c5cae9', '#9fa8da', '#4086ff',
                    '#c8e6c9', '#a5d6a7', '#9ff05e',
                   '#f5f5f5', '#e0e0e0', '#acacac']
expsize = 0.2
explode = [0,0,expsize,
            0,0,expsize,
            0,0,expsize,
            0,0,expsize]

#################################
# Rates calculation analitically
rates_colors = np.zeros(4)

for i in [0,1,2,3]:
    print(i)
    rates_colors[i] = pity[0]*pool[2, i]/total[2] + pity[1]*pool[1,i]/total[1] + (1-sum(pity))*pool[0,i]/total[0]

print(rates_colors*100)
# sys.exit("DEBUG")

rates = np.zeros(12)
rates_internal = np.zeros(12)

# cycle colors
for i in [0,1,2,3]:
        # 5* focus
    rates[i*3 + 2] = pity[0]*pool[2, i]/total[2] / rates_colors[i]
    rates_internal[i*3 + 2] = pity[0]*pool[2, i]/total[2]

        # 5* non focus
    rates[i*3 + 1] = pity[1]*pool[1,i]/total[1] / rates_colors[i]
    rates_internal[i*3 + 1] = pity[1]*pool[1,i]/total[1]

    # cycle rarities
        # 4-3 star
    rates[i*3] = 1 - rates[i*3 + 2] -rates[i*3 + 1]
    rates_internal[i*3] = (1-sum(pity))*pool[0,i]/total[0]

rates *= 100
print(rates[0:3])
print(rates[3:6])
print(rates[6:9])
print(rates[9:12])
#################################


rates_string = np.char.mod('%0.1f', rates)
rates_string_mod = np.empty(0, dtype='object')
print(rates_string)

for i in range(rates_string.size):
    #rates_string[i] = rates_string[i] + '%'
    rates_string_mod = np.append(rates_string_mod, rates_string[i] + '%')
    rates_string_mod[i] = rates_string_mod[i].replace('0.0%', ' ')

print(rates_string_mod)

fig, ax = plt.subplots()

size = 0.25

general_colors = ['red', 'blue', 'green', 'gray']

ax.pie(rates_internal, radius=1, colors=specific_colors, explode=explode, labels=rates_string_mod, startangle=angl, labeldistance=1.05, 
    wedgeprops=dict(width=size, edgecolor='w'),
    textprops=dict(fontsize=20, fontname='nintendoP_Skip-D_003', color='white'))
# 

ax.pie(rates_colors, radius=1-size, colors=general_colors, autopct='%1.0f%%',pctdistance=0.5,startangle=angl,
    wedgeprops=dict(width=1-size, edgecolor='w'),
    textprops=dict(color='white', fontname='nintendoP_Skip-D_003', fontsize=30))




ax.set(aspect="equal")
fig.set_size_inches(11, 11, forward=True)
plt.savefig('fig/pie.png', transparent=True)
plt.show()