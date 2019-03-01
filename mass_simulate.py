import feh_utils as feh
import numpy as np
import sys

# np.savetxt('pool.txt', pool, fmt='%2i')

simulations = 1

# Game pool info, containing focus banner heroes
# To do: update it from the wiki
pool = np.loadtxt('pool.txt', dtype=int)
total = [np.sum(pool[0]), np.sum(pool[1]), np.sum(pool[2])]


# Snipe plan holds in each entry the color of the character, quantity (-1 if only one is wanted of any) and id
# It is supposed to be correctly formatted
snipe_plan = np.loadtxt('snipe_plan.txt', dtype=int)
color_priority = np.loadtxt('color_priority.txt', dtype=int)
# Check for quantity column and set at_least_mode
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

snipe_results = np.empty_like(snipe_plan)
snipe_results[:] = snipe_plan[:]
snipe_results[:,2] = 0


# Arrays with 'simulations' size
# Holds number of sessions for each simulation
total_sessions = np.empty((0,1), dtype=int)
# Holds number of orbs spent in each simulation
total_orbs  = np.empty((0,1), dtype=int)
total_heroes = [[-3,-3]]


for i in range(simulations):

    satisfied = False
    sessions = 0 # Number of sessions
    orbs  = 0    # Number of orbs spent
    pity = 3 / 100
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
                total_heroes = np.append(total_heroes, [c], axis=0)

                summons += 1
                round_orbs += feh.spend_orbs(round_orbs)

                # If orb turns to be a 5 star, reset pity
                if c[1] > 0:
                    reset_pity = True
                else:
                    pity += 0.0005
                
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
                        total_heroes = np.append(total_heroes, [c], axis=0)
                        if c[1] > 0:
                            reset_pity = True
                        else:
                            pity += 0.0005
                


        if reset_pity:
            pity = 3/100

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

        # satisfied = sessions > 50

    # Satisfied confitions met:
    total_sessions = np.append( total_sessions, sessions)
    total_orbs  = np.append( total_orbs, orbs)

    

    # Keep track real time of the simulations performed
    sys.stdout.write('\r'+str(i+1))
    sys.stdout.flush()

total_heroes = np.delete(total_heroes, 0, 0)
#print(total_heroes)

np.savetxt( 'total_sessions.txt.gz', total_sessions, fmt='%2i' )
np.savetxt( 'total_orbs.txt.gz', total_orbs, fmt='%2i' )
np.savetxt( 'total_heroes.txt.gz', total_heroes, fmt='%1i')