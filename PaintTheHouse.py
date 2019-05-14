mapWidth = 10
mapHeight = 16
map = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
       [2, 4, 2, 0, 0, 0, 0, 0, 0, 2],
       [2, 0, 2, 0, 2, 2, 2, 2, 0, 2],
       [2, 0, 2, 0, 0, 0, 0, 0, 0, 2],
       [2, 0, 2, 2, 2, 2, 2, 2, 0, 2],
       [2, 0, 2, 0, 0, 0, 0, 2, 0, 2],
       [2, 0, 2, 0, 2, 0, 0, 0, 0, 2],
       [2, 0, 2, 0, 2, 2, 2, 0, 2, 2],
       [2, 0, 0, 0, 2, 0, 2, 0, 0, 2],
       [2, 2, 2, 0, 2, 0, 2, 0, 0, 2],
       [2, 0, 0, 0, 2, 0, 2, 0, 0, 2],
       [2, 0, 0, 0, 0, 0, 2, 0, 0, 2],
       [2, 0, 2, 2, 2, 0, 2, 0, 0, 2],
       [2, 0, 0, 2, 0, 0, 0, 0, 0, 2],
       [2, 0, 0, 2, 0, 0, 0, 0, 0, 2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]] # 0: Empty floor, 1: Painted floor, 2: Wall, 3: Player

posX = 1
posY = 1


# Drawing the map
for i in range(mapHeight):
    for j in range(mapWidth):
        if map[i][j] == 0:
            print(" ", end="")
        elif map[i][j] == 1:
            print(".", end="")
        elif map[i][j] == 2:
            print("#", end="")
        else:
            print("@", end="")
    print()


while True:

    # User input
    while True:
        key = str(input(">> What direction do you want to move? ( A, W, S or D)  "))
        try:
            dir = {"W":1, "A":2, "S":3, "D":4, "w":1, "a":2, "s":3, "d":4}[key]
            break
        except:
            print(f"{key} is not a valid input")

    # Handeling quitting
    if key == "q" or key == "Q":
        break

    # Applying movement
    map[posY][posX] = 0
    if dir == 1: # Up
        for i in reversed(range(0, posY+1)):
            if map[i][posX] == 2:
                if i == posY:
                    map[posY][posX] = 3
                    break
                else:
                    posY = i+1
                    map[posY][posX] = 3
                    break
            else: # Should check if set to 1 or 0 for perfomance but this is a tiny game so that isn't too big of a deal
                map[i][posX] = 1

    elif dir == 2: # Left
        for i in reversed(range(0, posX+1)):
            if map[posY][i] == 2:
                if i == posX:
                    map[posY][posX] = 3
                    break
                else:
                    posX = i+1
                    map[posY][posX] = 3
                    break
            else: # Should check if set to 1 or 0 for perfomance but this is a tiny game so that isn't too big of a deal
                map[posY][i] = 1

    elif dir == 3: # Down
        for i in range(posY, mapHeight):
            if map[i][posX] == 2:
                if i == posY:
                    map[posY][posX] = 3
                    break
                else:
                    posY = i-1
                    map[posY][posX] = 3
                    break
            else: # Should check if set to 1 or 0 for perfomance but this is a tiny game so that isn't too big of a deal
                map[i][posX] = 1

    elif dir == 4: # Right
        for i in range(posX, mapWidth):
            if map[posY][i] == 2:
                if i == posX:
                    map[posY][posX] = 3
                    break
                else:
                    posX = i-1
                    map[posY][posX] = 3
                    break
            else: # Should check if set to 1 or 0 for perfomance but this is a tiny game so that isn't too big of a deal
                map[posY][i] = 1


    # Drawing the map
    print("\n"*13)
    zeroes = False
    for i in range(mapHeight):
        for j in range(mapWidth):
            if map[i][j] == 0:
                print(" ", end="")
                zeroes = True
            elif map[i][j] == 1:
                print(".", end="")
            elif map[i][j] == 2:
                print("#", end="")
            else:
                print("@", end="")
        print()


    # Checking win
    if zeroes == False:
        print("Congratulations!!! You\'ve won!")
        break
