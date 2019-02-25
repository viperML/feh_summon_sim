import numpy as np

def pull(PITY, pool, total):
    # TO DO: Load this data from internet/Interface input

    # Rarities
    # 0 -> 3* or 4*
    # 1 -> 5* Non-Focus
    # 2 -> 5* Focus
    rarity = [ 0, 1, 2]

    # Red=0  Blue=1 Green=2 Colorless=3
    color  = [0, 1, 2, 3]


    # IN LENDARY BANNERS, P(1) = 0, TO DO
    rarity_probabilities = [ 1-2*PITY, PITY, PITY]

    # ROLL RARITIES
    rarity_circle = np.random.choice(rarity, 5, p=list(rarity_probabilities) )

    # ROLL COLOR depending on rarity
    color_circle = np.empty([5], dtype=int)
    for i in range(5):
        color_circle[i] = np.random.choice(color, 1, p=list([
            pool[rarity_circle[i], 0] / total[rarity_circle[i]],
            pool[rarity_circle[i], 1] / total[rarity_circle[i]],
            pool[rarity_circle[i], 2] / total[rarity_circle[i]],
            pool[rarity_circle[i], 3] / total[rarity_circle[i]]
        ]))
    return np.vstack([color_circle, rarity_circle])

def spend_orbs(orbs):
    if orbs == 0:
        spend_orbs = 5
    elif orbs < 17:
        spend_orbs = 4
    else:
        spend_orbs = 3
    return spend_orbs