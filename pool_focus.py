import numpy as np

n = [0,0,0,0]

print("Please type nº of Focus Heroes")
n[0] = int(input("[Red]: "))
n[1] = int(input("[Blue]: "))
n[2] = int(input("[Green]: "))
n[3] = int(input("[Colorless]: "))
np.save('pool_focus_heroes.npy', n)

pity = [0.03, 0.03]

print("")
print("Please type initial pity for focus heroes ( 3% standard, 8% legendary)")
pity[0] = float(input("[0-100]: "))/100.0
print("Please type initial pity for permanent pool heroes ( 3% standard, 0% legendary)")
pity[1] = float(input("[0-100]: "))/100.0
np.save('pool_focus_pity.npy', pity)
