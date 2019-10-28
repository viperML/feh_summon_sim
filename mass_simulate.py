import feh_utils as feh
import numpy as np
import sys


simulations = 30000
full_circle = False

# TO DO visual input
pity_initial = np.load('pool_focus_pity.npy')
pity = np.empty_like(pity_initial)
pity_max = np.empty_like(pity_initial)

# Game pool info, containing focus banner heroes
pool = np.load('pool_permanent.npy')
# TO DO visual input
pool = np.append( pool, [np.load('pool_focus_heroes.npy')], axis=0)
total = [np.sum(pool[0]), np.sum(pool[1]), np.sum(pool[2])]



# SNIPE PLAN holds in each entry the color of the character, id and quantity (-1 if only one is wanted of any)
# Each row for each character to snipe for
# It is supposed to be correctly formatted TO DO visual input
snipe_plan = np.loadtxt('snipe_plan.txt', dtype=int, ndmin=2)
# Order to  snipe colors, IN CASE colors in snipe plan are not available. 
color_priority = [0, 1, 3, 2]
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
print("full_circle:", end=" ")
print(full_circle)
print("Initial rates:", end=" ")
print(pity_initial)

# SNIPE RESULTS is the same as snipe_plan, but holds quantity information of current simulations
snipe_results = np.empty_like(snipe_plan)


# Vectors with 'simulations' size
# Holds number of sessions for each simulation
total_sessions = np.empty((0,1), dtype=int)
# Holds number of orbs spent in each simulation
total_orbs  = np.empty((0,1), dtype=int)
total_pity_max = np.empty((0,1))

total_heroes = np.zeros( (pool[2].max()+2,4), dtype=int)

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
            # If using at_least_mode, the session will stop with the first 5*
            if any(c[0] == i for i in snipe_results[:,0]) and not (satisfied == True and full_circle == False):
                
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
                        if at_least_mode == True: satisfied = True
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
    sys.stdout.write('\r' + '[' + str(int(100*i/simulations))+ '%] ' +str(i+1)+'/'+str(simulations))
    sys.stdout.flush()


np.save( 'total_sessions.npy', total_sessions)
np.save( 'total_orbs.npy', total_orbs)
np.save( 'total_heroes.npy', total_heroes)
np.save( 'total_heroes.npy', total_heroes)
np.save( 'total_pity_max.npy', total_pity_max)