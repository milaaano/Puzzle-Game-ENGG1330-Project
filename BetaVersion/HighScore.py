from Print import *

def drawHS(screen, divitions, text):
    screenRow, screenColumn = screen.getSize()

    row = screenRow // divitions
    column = screenColumn // 2

    for i in range(divitions - 1):

        r = row * (i +1)

        screen.writeText(r, column, text[i])

    row = screenRow -2
    screen.writeText(row, column, "exit(e), play(p)")


def highScore(screen):

    if Screen != type(screen):
        return "Wrong screen type"

    screen.defScreen(' ')
    row, col = screen.getSize()

    scores = open("BetaVersion/HighScore.txt", 'rt')

    selection = "None" # to check what the player has chosen

    count = int(scores.readline())
    text = ['High Scores']

    if count == 0:
        text += ['No Scores yet!', 'Play to set your score now']
    else:
        count = count if count < 5 else 5
        for i in range(count):
            name = scores.readline()[:-1]
            if len(name) > 15:
                name = name[:15] + "..."
            t = name + ": " + scores.readline()[:-1]
            #print(t)
            text.append(t)

    """
    if len(score) == 0:
        text.append('Set your Score now')
    elif len(score) <= 5:
        for i in score):
            text.append(score)
    else:
        for i in range(5):
            text.append(score[i])"""

    textSize = count + 1
    divitions = textSize + 1

    screen.defScreen(' ')

    while(selection == "None"):
        
        drawHS(screen, divitions, text)
        screen.printScreen()
        screen.defScreen(' ')
        inp = input().lower()

        if inp == 'exit' or inp == 'main menu' or inp == 'e':
            selection = "Main Menu"
        elif inp == 'play' or inp == 'new game' or inp == 'p':
            selection = "New Game"
        elif inp == 'instructions':
            selection = 'Instructions'
        # elif inp == 'quit':
        #     selection = 'Quit'
        else:
            screen.writeText(1, screen.getSize()[1] // 2, "Enter valid input")
            
    return selection
        
