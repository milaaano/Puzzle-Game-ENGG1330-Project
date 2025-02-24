import os, time
from Print import *
from formatting import *

'''

Main Menu selections and navigation


'''

def drawMainMenu(screen, divitions, text, pointer):

    #screen.defScreen(" ")

    #game name to be decided later

    screenRow, screenColumn = screen.getSize()
    row = screenRow // divitions
    column = screenColumn // 2

    for i in range(divitions - 1):

        r = row * (i +1) + 2
        if i == 0:
            screen.writeText(r, column, text[i], Format.bold)
        else:
            screen.writeText(r, column, text[i])

        if pointer - 1 == i:
            c = column - len(text[i])//2 - 2
            #print(row, column)
            screen.writeText(r, c , '----')

    row = screenRow -2
    screen.writeText(row-1, column, "up(w), down(s), enter(e)", Format.bold)
    screen.writeText(row, column, "Quit Game(q)", Format.bold )

def MainMenu(screen):

    if Screen != type(screen):
        return "Wrong screen type"

    selection = "None" # to check what the player has chosen
    pointer = 2
    textSize = 6
    text = ['The Unpaid Quest', 'New Game', 'Select Map to Play', 'Instructions', 'High Score', 'Quit']
    divitions = textSize + 1


    #print("main menu")

    screen.defScreen(' ')
    while selection == "None":

        drawMainMenu(screen, divitions, text, pointer)
        #os.system('cls' if os.name == 'nt' else 'clear')
        #print("TRUE")
        screen.printScreen()
        inp = input().lower()
        #time.sleep(3)
        #move(pointer, divitions, text)

        screen.defScreen(' ')

        if (inp == 'up' or inp == 'w'):
            if pointer > 2 : pointer -= 1
        elif (inp == 'down' or inp == 's'):
            if pointer < textSize + 1 : pointer += 1
        elif (inp == 'enter' or inp == 'e'):
            selection = text[pointer - 1 ]
        elif (inp == 'quit' or inp == 'q'):
            selection = 'Quit'
        else:
            screen.writeText(1, screen.getSize()[1] // 2, 'Enter valid inputs')
        
        for sel in text[1:]:
            if inp == sel.lower():
                selection = sel
                #print (selection)

    return selection
