import feh_utils as feh
import numpy as np
import sys

i = 1 # Generic counter


simulations = 8000

# Colors to snipe. 4 colors will mean full circle summoning
# Red=0  Blue=1 Green=2 Colorless=3
snipe = [0,1,2,3]

# Whether to be satisfied with Non-Focus, Focus 5* or any combination
# 3* or 4* = 0, 5* Non-focus = 1, 5* Focus = 2
rarity_snipe = [1,2]

# Array with 'simulations' size
# Holds number of sessions for each simulation
total_sessions = np.empty((0,1), dtype=int)
# Holds number of orbs spent in each simulation
total_orbs  = np.empty((0,1), dtype=int)


for i in range(simulations):

    satisfied = False
    sessions = 0 # Number of sessions
    orbs  = 0 # Number of orbs spent
    pity = 3 / 100

    # Keep pulling until a satisfied conditions are met
    while (not satisfied):
        circle = feh.pull(pity)
        sessions += 1
        round_orbs = 0
        summons = 0

        # Check if I want every orb
        if circle[0,0] in snipe:
            summons += 1
            round_orbs += feh.spend_orbs(round_orbs)
            satisfied = (circle[1,0] in rarity_snipe)
        
        if circle[0,1] in snipe:
            summons += 1
            round_orbs += feh.spend_orbs(round_orbs)
            satisfied = (circle[1,1] in rarity_snipe)
        
        if circle[0,2] in snipe:
            summons += 1
            round_orbs += feh.spend_orbs(round_orbs)
            satisfied = (circle[1,2] in rarity_snipe)

        if circle[0,3] in snipe:
            summons += 1
            round_orbs += feh.spend_orbs(round_orbs)
            satisfied = (circle[1,3] in rarity_snipe)

        if circle[0,4] in snipe:
            summons += 1
            round_orbs += feh.spend_orbs(round_orbs)
            satisfied = (circle[1,4] in rarity_snipe)
        
        orbs += round_orbs 
        pity += 0.0025 * (5 - summons) / 5.0

    # Satisfied confitions met:
    total_sessions = np.append( total_sessions, sessions)
    total_orbs  = np.append( total_orbs, orbs)

    # Keep track real time of the simulations performed
    sys.stdout.write('\r'+str(i))
    sys.stdout.flush()

np.savetxt( 'total_sessions.gz', total_sessions, fmt='%2i' )
np.savetxt( 'total_orbs.gz', total_orbs, fmt='%2i' )