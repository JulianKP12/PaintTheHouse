# Libraries
from graphics import *


# Function to handle input from the user
def handleInput(key):
    try:
        if key == "Escape":
            return -1
        else:
            return {"W":1, "A":2, "S":3, "D":4, "w":1, "a":2, "s":3, "d":4}[key]
    except:
        return 0 # Set to value that calls the function again in the game loop


# Map initialisation
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
dir = 0
moves = 0
breaking = False


# Graphics setup

# Window
squareSize = 30
win = GraphWin("Paint the House", mapWidth*squareSize, mapHeight*squareSize, autoflush=False)
win.setBackground(color_rgb(41, 65, 104))

# Colors
wallColor = color_rgb(41, 65, 104)
paintColor = color_rgb(255, 16, 0)
floorColor = color_rgb(255, 255, 255)
playerColor = color_rgb(56, 239, 23)

# Rectangles used for blocks of the map
rects = []
for i in range(mapHeight):
    rects.append([])
    for j in range(mapWidth):
        rects[i].append(Rectangle(Point(j*squareSize, i*squareSize), Point(j*squareSize+squareSize, i*squareSize+squareSize)))
        rects[i][j].setWidth(0)



# Drawing the map
for i in range(mapHeight):
    for j in range(mapWidth):
        if map[i][j] == 0:
            rects[i][j].setFill(floorColor)
            rects[i][j].setOutline(floorColor)
            rects[i][j].draw(win)
        elif map[i][j] == 1:
            rects[i][j].setFill(paintColor)
            rects[i][j].setOutline(paintColor)
            rects[i][j].draw(win)
        elif map[i][j] == 2:
            rects[i][j].setFill(wallColor)
            rects[i][j].setOutline(wallColor)
            rects[i][j].draw(win)
        else:
            rects[i][j].setFill(playerColor)
            rects[i][j].setOutline(playerColor)
            rects[i][j].draw(win)
update(60)


# Main game loop
while True:

    # User input
    while dir == 0:
        dir = handleInput(win.getKey())
        if dir == -1:
            breaking = True
            break
    else:
        moves += 1

    # Handeling quitting
    if breaking:
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
    zeroes = False
    for i in range(mapHeight):
        for j in range(mapWidth):
            if map[i][j] == 0:
                zeroes = True
                rects[i][j].setFill(floorColor)
                rects[i][j].setOutline(floorColor)
            elif map[i][j] == 1:
                rects[i][j].setFill(paintColor)
                rects[i][j].setOutline(paintColor)
            elif map[i][j] == 2:
                rects[i][j].setFill(wallColor)
                rects[i][j].setOutline(wallColor)
            else:
                rects[i][j].setFill(playerColor)
                rects[i][j].setOutline(playerColor)
    update(60)


    # Checking win
    if zeroes == False:
        print(f"Congratulations!!! You\'ve won in just {moves} moves!")
        break
    else:
        dir = 0
