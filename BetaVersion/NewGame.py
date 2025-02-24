55555rom entity import *
from Maap import *
from player_controller import *

def NewGame(screen):
    '''
        Purpose of this Game:
        To get as much as dollars as you can in restricted moving energies. Let's see how much * you can get!

        Your Movements:
        For Upward movement : press 'u'
        For Downward movement : press 'd'
        For Leftward movement : press 'l'
        For Rightward movement : press 'r'

    '''

    if Screen != type(screen):
        return "Wrong screen type"

    selection = "None" # to check what the player has chosen
    
    map
