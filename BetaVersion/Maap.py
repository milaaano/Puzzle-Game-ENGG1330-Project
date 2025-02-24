from vector import *
from random import *
from Resources import *
from formatting import *
from Pace import *
import Gameplay

used_maps = set()
maps = {} #dictionary of maps, made in advance
map_names = {} # name of each map
map_starting_tokens = {} # starting tokens of each map

campaign_map_count = 0

def ReadMaps():
    f = list(i.strip('\n') for i in open('BetaVersion/maps.txt'))
    global campaign_map_count
    campaign_map_count = 0
    i, cur_map, num = 0, [], -1
    while i < len(f):
        try:
            fragments = f[i].split(' ')
            first_part = fragments[0]
            if first_part.isdigit():
                if num >= 0:
                    maps[num] = cur_map
                    cur_map = []
                
                num = int(first_part)
                if num == 0: # all campaign maps should have an index of 0.
                    campaign_map_count += 1
                    num = campaign_map_count
                
                map_starting_tokens[num] = int(fragments[1])
                map_names[num] = ' '.join(fragments[2:]) if len(fragments) > 1 else "unnamed"
            elif f[i][0:2] != '//':
                cur_map.append(list(first_part))
        except Exception:
            print(f"maps.txt: Error reading line {i}!")
            short_pause()
        i += 1
    if num >= 0:
        maps[num] = cur_map
        cur_map = []


def get_campaign_map_count():
    return campaign_map_count

def Remember(map_number):
    used_maps.add(map_number)

def NextMap():
    return choice(list(set(maps.keys()) - used_maps))

def Teleport(player, tunnels: list): # tunnels - list of all tunnels. User will be proposed to enter the number of exit tunnel
    cur_coords = player.coords
    print(', '.join(f"{i + 1}: {tunnels[i]}" for i in range(len(tunnels))))
    exit_tunnel = tunnels[int(input('Where are you going? ')) - 1]
    # dif_vector = Vector(exit_tunnel) - Vector(cur_coords)
    player.just_set_coords(Vector(exit_tunnel))

class MapObj:
    def Display(self):
        return APPEARANCES[self.__class__.__name__]

# class Meme:

#     def __init__(self, char):
#         self.char = char
#         self.accessibility = True

#     def Display(self):
#         return char

class Tunnel(MapObj):
    def __init__(self, price, coords):
        self.price = price
        self.coords = coords
        self.accessibility = True

class Wall(MapObj):
    def __init__(self):
        self.accessibility = False

class FreeSpace(MapObj):
    def __init__(self):
        self.accessibility = True

class Coin(MapObj):
    def __init__(self, value):
        self.accessibility = True
        self.value = value

class Button(MapObj):
    def __init__(self):
        self.accessibility = True

class Door(MapObj):
    def __init__(self, accessibility):
        self.accessibility = accessibility
    
    def Display(self):
        return APPEARANCES["DoorOpened" if self.accessibility else "DoorClosed"]

class StartPoint(MapObj):
    def __init__(self):
        self.accessibility = True

class EndPoint(MapObj):
    def __init__(self):
        self.accessibility = True

class Map:
    def __init__(self, map_number): # initialization.
        self.map_number = map_number # chosen map from maps.
        self.startpoint = None # player spawns here.
        self.endpoint   = None # player lands here, game ends.
        self.appearance = maps[map_number] # 2D string list. sketch of map.
        self.height     = len(self.appearance)
        self.width      = len(self.appearance[0])
        self.data       = [[0]*self.width for i in range(self.height)] # 2D list of all map objects.
        self.doors      = {} # key represents accessibility when button is up.

    def WriteData(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.appearance[i][j] == '.':
                    self.data[i][j] = FreeSpace()
                elif self.appearance[i][j] == '#':
                    self.data[i][j] = Wall()
                elif self.appearance[i][j] == '$':
                    self.data[i][j] = Coin(5)
                elif self.appearance[i][j] == 'X':
                    self.data[i][j] = Box(self, (j, i))
                elif self.appearance[i][j] == 'O':
                    self.data[i][j] = Button()
                elif self.appearance[i][j] == '%':
                    self.data[i][j] = Door(False)
                    self.doors[self.data[i][j]] = True
                elif self.appearance[i][j] == '@':
                    self.data[i][j] = Door(True)
                    self.doors[self.data[i][j]] = False
                elif self.appearance[i][j] == 'S':
                    self.data[i][j] = StartPoint()
                    self.startpoint = (j, i)
                elif self.appearance[i][j] == 'E':
                    self.data[i][j] = EndPoint()
                    self.endpoint = (j, i)
                elif self.appearance[i][j].isdigit():
                    self.data[i][j] = Tunnel(int(self.appearance[i][j]), (j, i))
                    # self.tunnels.append((j, i))
                else:
                    assert False, f"Map {map_names[self.map_number]}: Unidentified character at {(j, i)}!"
        assert self.startpoint, f"Map {map_names[self.map_number]} has no starting point!"
        assert self.endpoint, f"Map {map_names[self.map_number]} has no end point!"
    
    # prints the map, variable board is used instead of 'map' 
    def DisplayMap(self):
        for i in self.data:
            print(f"{back_green}{''.join(j.Display() for j in i)}")

    def CanAccess(self, destination: Vector): #Checks if it's possible to move to the particular point
        x = destination.x
        y = destination.y
        return 0 <= x <= len(self.data[0]) and 0 <= y <= len(self.data) and self.data[y][x].accessibility

    def control_doors(self, accessibility: bool):
        for door in self.doors:
            door.accessibility = self.doors[door] == accessibility

# entity.py stuff, put here cuz python can't deal w circular import >:(

class Entity(MapObj):

    def __init__(self, domain: Map, coords: tuple):
        self.domain = domain
        self._coords = Vector(coords)
        self.displaced = FreeSpace()
        self.accessibility = True

    # just set coords, don't check where coords is going
    def just_set_coords(self, value: Vector):
        if self._coords:
            self.domain.data[self._coords.y][self._coords.x] = self.displaced
            #print("left", type(self.displaced))
        self.displaced = self.domain.data[value.y][value.x]
        #print("landed on", type(self.displaced))
        self.domain.data[value.y][value.x] = self
        self._coords = value

class Box(Entity):
    
    # tries to move and returns a boolean based on if it succeeds.
    # if another block is in the way, tries to push it.
    def be_pushed(self, move_by: Vector):
        new_coords = self._coords + move_by
        if self.domain.CanAccess(new_coords):
            destination, can_move = self.domain.data[new_coords.y][new_coords.x], False
            if type(destination) == Box:
                if destination.be_pushed(move_by):
                    destination = self.domain.data[new_coords.y][new_coords.x] # now that the box has moved out of the way away, update destination.
            can_move = self.domain.CanAccess(new_coords)
            if can_move:
                #print("box moved!")
                if type(destination) == Button:
                    self.domain.control_doors(True) # button is down.
                    #print("button down!")
                elif type(self.displaced) == Button:
                    self.domain.control_doors(False) # button is up.
                    #print("button up!")
                self.just_set_coords(new_coords)
            return can_move

