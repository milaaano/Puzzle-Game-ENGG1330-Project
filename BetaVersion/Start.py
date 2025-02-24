# python BetaVersion/Start.py

from MainMenu import *
from Instructions import *
from HighScore import *
from Gameplay import *
from formatting import *

def draw(screen, divitions, text):
    screenRow, screenColumn = screen.getSize()

    row = screenRow // divitions
    column = screenColumn // 2

    for i in range(divitions - 1):

        r = row * (i +1)

        screen.writeText(r, column, text[i])

    row = screenRow -2
    screen.writeText(row, column, "Press Any Key to Start")


screen = Screen(20,35)

screen.defScreen(' ')

lst = ['Melon\'s Empire', 'The Unpaid Quest', 'Developed by', 'Daren Tat-yan Choi', 'Yuri Zheng Yu Hang', 'Milan Giliazetdinov', 'Mian Muneeb Ur Rehman', 'Ji Seong Yun']

draw(screen, 9, lst)
screen.printScreen()

input("Press Any key to Start the Game ")

current = MainMenu(screen)
while current != 'Quit':
    #['New Game', 'Continue', 'Instructions', 'High Score', 'Quit']
    match current:
        case 'Main Menu': current = MainMenu(screen)
        case 'New Game': current = run_game()
        case 'Continue': current = run_game()
        case 'Instructions': current = instructions(screen)
        case 'High Score': current = highScore(screen)
        case 'Make Map': current = makeMap()
        case 'Select Map to Play': current = run_single_level()
        case 'Quit': continue
        case _: print(current, "Error: the screen current is entered wrong")


        
