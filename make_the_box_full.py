import random

def pathfind():

    path = [starty, startx]
    for i in range(15):
        excepts = []
        if path[1] == 4 or stage[path[0]][path[1]+1] == 'O': excepts.append(1)
        if path[0] == 4 or stage[path[0]+1][path[1]] == 'O': excepts.append(2) 
        if path[1] == 0 or stage[path[0]][path[1]-1] == 'O': excepts.append(3) 
        if path[0] == 0 or stage[path[0]-1][path[1]] == 'O': excepts.append(4) 
        if len(excepts) == 4:
            break
        direc = random.randint(1, 4)
        while direc in excepts:
            direc = random.randint(1, 4)
        stage[path[0]][path[1]] = "O"
        match direc:
            case 1:
                path[1] += 1
            case 2:
                path[0] += 1
            case 3:
                path[1] -= 1
            case 4:
                path[0] -= 1
        stage[path[0]][path[1]] = "O"

def printstage(stage):
    stage1 = ''
    for i in stage:
        for j in i:
            stage1 += j + ' '
        stage1 += '\n'
    print(stage1)

def startgame(stage):
    
    pathfind()

    stage[starty][startx] = 'H'
    
    printstage(stage)

    gameover = False
    victory = False
    path = [starty, startx]
    while gameover is False and victory is False:
        move = input("What is your next move? ")
        if move.lower() not in "wasd":
            print("This is not a valid move!")
            continue
        stage[path[0]][path[1]] = "I"
        match move.lower():
            case 'w':
                if path[0] == 0:
                    print("You are going outside the map! Try again!")
                    continue
                if stage[path[0]-1][path[1]] != 'O':
                    print("You are going in the forbidden zone! Try again!")
                    continue
                path[0] -= 1
            case 'd':
                if path[1] == 4:
                    print("You are going outside the map! Try again")
                    continue
                if stage[path[0]][path[1]+1] != 'O':
                    print("You are going in the forbidden zone! Try again!")
                    continue
                path[1] += 1
            case 's':
                if path[0] == 4:
                    print("You are going outside the map! Try again")
                    continue
                if stage[path[0]+1][path[1]] != 'O':
                    print("You are going in the forbidden zone! Try again!")
                    continue
                path[0] += 1
            case 'a':
                if path[1] == 0:
                    print("You are going outside the map! Try again")
                    continue
                if stage[path[0]][path[1]-1] != 'O':
                    print("You are going in the forbidden zone! Try again!")
                    continue
                path[1] -= 1
        stage[path[0]][path[1]] = "H"
        printstage(stage)
        if 'O' not in stage[0]+stage[1]+stage[2]+stage[3]+stage[4]:
            victory = True
            print("Congrats! You won the game!")
            break
        if (stage[path[0]][path[1]+1] != 'O' if path[1] < 4 else True) and (stage[path[0]][path[1]-1] != 'O' if path[1] > 0 else True) and (stage[path[0]+1][path[1]] != 'O' if path[0] < 4 else True) and (stage[path[0]-1][path[1]] != 'O' if path[0] > 0 else True): 
            gameover = True
            print("You lost, you cannot move anymore.")
            break

gamebegin = ''

print("Welcome to the MAKE THE BOX FULL game! Enter START if you are ready to play. Enter END if you are done with me :(.\nWhen in game, enter W for up, A for left, S for down, or D for right.")

while gamebegin.lower() != "end":

    gamebegin = input("What do you want to do: ")
    
    if gamebegin.lower() == "start":
        
        stage = [['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X']]

        startx = random.randint(0, 4)
        starty = random.randint(0, 4)

        startgame(stage)
    elif gamebegin.lower() != "end":
        print("Bruh, enter only START or END!")
print("Thanks for playing my game!")