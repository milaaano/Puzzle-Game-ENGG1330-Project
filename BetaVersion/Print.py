from Interface import *

''' 
screen class declation:

        printScreen: prints screen as it is
        defScreen: returns screen to default value
        writeText: writes screen to file based on the input of row and column
        writeTextL: writes screen to file with text left alligned to the column provided
        getSize: returns size of the size of the screen in form ( row, column)
        setSize: changes size of screen according to the input(row, column)
        
'''

class Screen:

    def __init__(self, height, width):
        self._screenRow = height
        self._screenColumn = width

        self._screen = [['*' for i in range(self._screenColumn)] for j in range(self._screenRow)]
        #print(self._screen)
    def printScreen(self):

        for i in range(self._screenRow):
            for j in range(self._screenColumn):
                print(self._screen[i][j], end = ' ')
                
            print('')

    def defScreen(self, symbol = ' '):

        for i in range(self._screenRow):
            for j in range(self._screenColumn):
                #print(i, j, self._screenRow, self._screenColumn)
                if (i == 0 or i == self._screenRow - 1 ):
                    
                    self._screen[i][j] = '='
                elif (j == 0 or j == self._screenColumn - 1 ):
                    self._screen[i][j] = '|'
                else:
                    self._screen[i][j] = symbol

    def writeTextL(self, row, column, text):


        if (row + 1 >= self._screenRow or column + len(text) >= self._screenColumn or row <= 0 or column <= 0):
            print("error: please increase the size of screen")
            return

        # error checking for text longer than the screen
        if (len(text) > self._screenColumn - 2):
            print("error:  please increase the size of screen")
            return

        # adding text to the location
        for char in text:
            #print(char, " ", row, ' ', column)
            self._screen[row][column] = char
            column += 1

    def writeText(self, row, column, text, form = None):


        if (row + 1 >= self._screenRow or column + len(text) // 2 >= self._screenColumn or row <= 0 or column - len(text) // 2 <= 0):
            print("error: please increase the size of screen")
            return

        # error checking for text longer than the screen
        if (len(text) > self._screenColumn - 2):
            print("error:  please increase the size of screen")
            return

        #checking row and columns for the writing
        column = column - len(text)//2

        # adding text to the location
        for char in text:
            #print(char, " ", row, ' ', column)
            self._screen[row][column] = char
            column += 1

    def getSize(self):
        return self._screenRow, self._screenColumn

    def newSize(self, row, col):
        del self._screen
        self._screen = [[' ' for i in range(col)] for j in range(row)]
        self._screenRow = row 
        self._screenColumn = col
        
