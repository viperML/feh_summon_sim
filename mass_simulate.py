import feh_utils as feh
import numpy as np
import sys

# np.savetxt('pool.txt', pool, fmt='%2i')

simulations = 7000

pity_initial = [0.08, 0.00]
pity = np.empty_like(pity_initial)
pity_max = np.empty_like(pity_initial)

# Game pool info, containing focus banner heroes
# To do: update it from the wiki
pool = np.loadtxt('pool.txt', dtype=int)
total = [np.sum(pool[0]), np.sum(pool[1]), np.sum(pool[2])]



# SNIPE PLAN holds in each entry the color of the character, id and quantity (-1 if only one is wanted of any)
# It is supposed to be correctly formatted
snipe_plan = np.loadtxt('snipe_plan.txt', dtype=int, ndmin=2)
# Order to  snipe colors, in case colors in snipe plan are not available. 
color_priority = np.loadtxt('color_priority.txt', dtype=int)
# Check at_least_mode
if all(j <= 0 for j in snipe_plan[:,2]):
    at_least_mode = True
    snipe_plan[:,2] = 1
elif all(j >= 0 for j in snipe_plan[:,2]):
    at_least_mode = False
else:
    print(snipe_plan)
    sys.exit("Mixed at_least_mode")

print("Snipe plan:")
print(snipe_plan)
print("at_least_mode:", end=" ")
print(at_least_mode)

# SNIPE RESULTS is the same as snipe_plan, but holds quantity information of current simulations
snipe_results = np.empty_like(snipe_plan)


# 1D Arrays with 'simulations' size
# Holds number of sessions for each simulation
total_sessions = np.empty((0,1), dtype=int)
# Holds number of orbs spent in each simulation
total_orbs  = np.empty((0,1), dtype=int)
total_pity_max = np.empty((0,1))

total_heroes = np.zeros( (snipe_plan[:,1].max()+1,4), dtype=int)

for i in range(simulations):

    snipe_results[:] = snipe_plan[:]
    snipe_results[:,2] = 0

    satisfied = False

    sessions = 0 # Number of sessions
    orbs  = 0    # Number of orbs spent

    pity[:] = pity_initial[:]
    pity_max = [0.0, 0.0]
    #print(snipe_plan)
    #print(snipe_results)

    # Keep pulling until a satisfied conditions are met
    while not satisfied:

        circle = feh.pull(pity, pool, total)
        sessions += 1
        round_orbs = 0
        summons = 0

        #print(sessions)
        #print(pity)
        #print(circle)

        reset_pity = False

        # Check if I want every orb
        for c in circle:
            # Orb is pulled if:
            # Color is in the snipe plan
            #       (When the quantity is reached, it is removed from the snipe plan)
            if any(c[0] == i for i in snipe_results[:,0]):
                
                #print(c, end=" ")
                #print("Color in snipe results, pulling")
                # total_heroes = np.append(total_heroes, [c], axis=0)

                summons += 1
                round_orbs += feh.spend_orbs(round_orbs)
                total_heroes[c[1], c[0]] += 1

                # If orb turns to be a 5 star, reset pity
                if c[1] > 0:
                    reset_pity = True
                else:
                    for p in range(2):
                        if pity[p] > 0.0:
                            pity[p] += 0.0005 

                
                # If 5 star, color and id matches, add to the results
                for j in range(snipe_results.shape[0]):
                    if c[0] == snipe_results[j,0] and c[1] == snipe_results[j,1]:
                        a = [0,0,1]
                        snipe_results[j] += a
                        #print("yeet")
                        #print(snipe_results)
        
        # No orbs pulled -> pull one orb following priority
        if round_orbs == 0:

            # Go through colors in priority order
            for j in range(4):
                for c in circle:
                    if round_orbs == 0 and color_priority[j] == c[0]:
                        #print("Pulling", end=" ")
                        #print(c)
                        summons += 1
                        round_orbs += feh.spend_orbs(round_orbs)
                        total_heroes[c[1], c[0]] += 1
                        # total_heroes = np.append(total_heroes, [c], axis=0)
                        if c[1] > 0:
                            reset_pity = True
                        else:
                            for p in range(2):
                                if pity[p] > 0.0:
                                    pity[p] += 0.0005         

        if pity[0] > pity_max[0]:
            pity_max[:] = pity[:]
        if reset_pity:
            pity[:] = pity_initial[:]

        # When quantity plan is reached, reset the component to -2
        for j in range(snipe_results.shape[0]):
            if snipe_results[j,2] >= snipe_plan[j,2]:
                #print("Resetting component")
                snipe_results[j] = [-2,-2,-2]
                #print(snipe_results)


        if sum(sum(snipe_results)) == snipe_results.shape[0]*(-6):
            satisfied = True
        elif at_least_mode and any(row[2] != 0 for row in snipe_results):
            satisfied = True

        orbs += round_orbs


    # Satisfied confitions met:
    total_sessions = np.append( total_sessions, sessions)
    total_orbs  = np.append( total_orbs, orbs)
    total_pity_max = np.append( total_pity_max, pity_max[0])
    #print(pity_max)
    

    # Keep track real time of the simulations performed
    sys.stdout.write('\r'+str(i+1))
    sys.stdout.flush()


np.savetxt( 'total_sessions.txt.gz', total_sessions, fmt='%3i' )
np.savetxt( 'total_orbs.txt.gz', total_orbs, fmt='%4i' )
np.savetxt( 'total_heroes.txt.gz', total_heroes, fmt='%1i')
np.savetxt( 'total_heroes.txt', total_heroes, fmt='%5i')
np.savetxt( 'total_pity_max.txt.gz', total_pity_max)