import numpy as np

def pull(pity, pool, total):
    # Rarities
    # 0 -> 3* or 4*
    # 1 -> 5* Non-Focus
    # 2 -> 5* Focus
    rarity = [ 0, 1, 2]

    # Red=0  Blue=1 Green=2 Colorless=3
    color  = [0, 1, 2, 3]

    pull = np.empty([5,2], dtype=int)
    # ROLL RARITIES
    pull[:,1] = np.random.choice(rarity, 5, p=list([1-sum(pity), pity[1], pity[0]]) )

    # ROLL COLOR depending on rarity
    for i in range(5):
            pull[i,0] = np.random.choice(color, 1, p=list([
                pool[pull[i,1], 0] / total[pull[i,1]],
                pool[pull[i,1], 1] / total[pull[i,1]],
                pool[pull[i,1], 2] / total[pull[i,1]],
                pool[pull[i,1], 3] / total[pull[i,1]] ]))

            # If 5 star and there are more than 1 focus unit for the same color
            if pull[i,1] == 2 and pool[2, pull[i,0]] > 1:
                pull[i,1] = np.random.choice( np.arange(2, pool[2, pull[i,0]] + 2), 1)
                
    return pull

def spend_orbs(orbs):
    if orbs == 0:
        spend_orbs = 5
    elif orbs < 17:
        spend_orbs = 4
    else:
        spend_orbs = 3
    return spend_orbs