import numpy as np

pool = np.loadtxt(open("pool_permanent.csv", "rb"), delimiter=",", dtype=int)
pool = np.append( pool, [np.loadtxt(open("pool_focus.csv", "rb"), delimiter=",", dtype=int)], axis=0)

print(pool)