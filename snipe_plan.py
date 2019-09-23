import numpy as np

snipe_plan = []
hero_input = [0 ,0, 0]

print("Do you want a certain number of copies of the characters or just 1 of any of all you want ('Any' mode)?")
print("[1] = Any mode // [0] = Input number of copies")
any_mode = int(input(": "))

continue_input = 1
while continue_input == 1:

    print("")
    print("Color:")
    print("[0] Red")
    print("[1] Blue")
    print("[2] Green")
    print("[3] Colorless")
    hero_input[0] = int(input(": "))

    if any_mode == 1:
        hero_input[2] = -1
    else:
        print("How many copies?")
        hero_input[2] = int(input(": "))

    if snipe_plan == []:
        snipe_plan = [hero_input[:]]
    else:
        snipe_plan = np.vstack(( snipe_plan, hero_input[:] ))

    print("")
    print("Snipe plan: ")
    for row in snipe_plan:
        if row[0] == 0:
            print("   Red", end='')
        elif row[0] == 1:
            print("   Blue", end='')
        elif row[0] == 2:
            print("   Green", end='')
        elif row[0] == 3:
            print("   Colorless", end='')
    
        if any_mode == 1:
            print(", any copies")
        else:
            print(",", row[2], "copies")

    print("")
    print("Do you want to add another hero?")
    continue_input = int(input("[1] Yes // [0] No : "))


id_counter = [2,2,2,2]
for row in snipe_plan:
    row[1] = id_counter[row[0]]
    id_counter[row[0]] += 1

np.savetxt('snipe_plan.txt', snipe_plan, fmt='% 3d')
