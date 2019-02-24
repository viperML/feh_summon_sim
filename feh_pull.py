import numpy as np

def pull(PITY):
    permanent_pool = np.array([
    #   R=0  B=1 G=2 C=3
        [41, 28, 21, 18],  # 5* Star
        [32, 29, 20, 28],  # 4* Star
        [28, 25, 18, 25]   # 3* Star
    ])

    focus_pool = np.array(
        [1,0,0,1]
    )

    # First, 5 hero rarities are chosen
    # 0 -> 3* or 4*
    # 1 -> 5* Non-Focus
    # 2 -> 5* Focus
    rarity = [ 0, 1, 2]

    # This would change in a Legendary Banner (To do)
    rarity_probabilities = [ 1-2*PITY, PITY, PITY]

    rarity_circle = np.random.choice(rarity, 5, p=list(rarity_probabilities) )
    # print(rarity_circle)


    # Color is chosen depending on the rarity

    # Red=0  Blue=1 Green=2 Colorless=3
    color = [0, 1, 2, 3]
    color_circle = np.empty([5], dtype=int)
    i = 0 
    while i < 5:

        if rarity_circle[i] == 2:
            total = np.sum(focus_pool)
            color_circle[i] = np.random.choice(color, 1, p=list(
                [ focus_pool[0]/total, focus_pool[1]/total, focus_pool[2]/total, focus_pool[3]/total] 
            ))

        elif rarity_circle[i] == 1:
            total = np.sum(permanent_pool[0])
            color_circle[i] = np.random.choice(color, 1, p=list(
                [ permanent_pool[0,0]/total, permanent_pool[0,1]/total, permanent_pool[0,2]/total, permanent_pool[0,3]/total]
            ))
        else:
            total = np.sum(permanent_pool[1]) + np.sum(permanent_pool[2])
            color_circle[i] = np.random.choice(color, 1, p=list(
              [ (permanent_pool[1,0] + permanent_pool[2,0])/total,
                (permanent_pool[1,1] + permanent_pool[2,1])/total,
                (permanent_pool[1,2] + permanent_pool[2,2])/total,
                (permanent_pool[1,3] + permanent_pool[2,3])/total ]
            ))

        i+=1

    pull = np.vstack([color_circle, rarity_circle])
    
    return pull