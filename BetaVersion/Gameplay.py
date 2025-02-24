from Maap import *
from entity import *
from vector import *
from Resources import *
from Pace import *
from WinLose import *

ReadMaps()

def run_game():
    # add maps
    # board = Map(NextMap(), 21, 19)
    map_number = 1
    return run_level(map_number)

def run_level(map_number, p = None, do_next_level = True):
    board = Map(map_number)
    board.WriteData()

    # player initialization / update
    if p:
        p.new_level(board, map_starting_tokens[map_number])
    else:
        p = Player(board, map_starting_tokens[map_number])
        if do_next_level:
            p.name = get_player_name(p)
    
    p.turn = 1 # every level starts on turn 1

    # goofy level intro
    short_pause(3)
    print(f"LEVEL {map_number}: {map_names[map_number]}")
    short_pause(3)

    # gameplay loop
    selection = 'None'
    while selection != 'Quit':
        action = p.run_frame()
        if action == 'Quit':
            return 'Main Menu'
        elif action == 'Pause':
            x = 'a'
            while x != 'Pause':
                x = input("Enter 'Pause' to continue the game")
        elif action == "Restart Level":
            return run_level(map_number, p)
        elif action == 'Next Map':
            p.info()
            p.tally_score()
            scores = p.score
            if do_next_level:
                global levels_count
                if map_number >= get_campaign_map_count():
                    Win(scores, p.name, cont=True, quit=False)
                    play_ending(p)
                    store(p.name, scores)
                    return 'High Score'
                state = Win(scores, p.name)
                if state == 'Main Menu':
                    return state
                else:
                    return run_level(map_number + 1, p)
            else:
                Win(scores, p.name, False)
                return 'Main Menu'
        elif action == 'End Game':
            p.info()
            if do_next_level:
                scores = p.score
                state = Lose(scores, p.name)
            else:
                state = Lose(showScores=False)
            if state == 'Main Menu':
                return state
            elif state == 'Play Again':
                return run_level(map_number, p)

    return selection

def run_single_level():
    print("Available maps:")
    for num, name in tuple(zip(map_names.keys(), map_names.values())):
        print(f"{num}: {name}")
    map_number = ""
    while not (map_number.isnumeric() and int(map_number) in maps):
        map_number = input("Enter map number: ")
    feedback = run_level(int(map_number), do_next_level=False)
    return feedback

def get_player_name(player):
    
    # serious disclaimer
    short_pause(3)
    print("This is a work of fiction. Names, characters, businesses, places, events and incidents are either the products of the author's imagination or used in a fictitious manner. Any RESEMBLANCE to ACTUAL PERSONS, living or dead, or ACTUAL EVENTS is **PURELY COINCIDENTAL**.")
    short_pause(3)
    ok()
    print("To ascertain that you have thoroughly read the disclaimer above, please recite it below.")
    short_pause()
    skip_intro = input("Recitation: ") == "skip"
    print("(This game doesn't actually check if your recitation is correct.)")
    short_pause(3)

    playerName = None
    times_name_asked = 0
    print(f"{embolden('???')}:\tBefore we can start talking, I need to know your name.")
    short_pause()
    while True:
        if times_name_asked == 5:
            print("...")
            short_pause()
        elif times_name_asked > 5:
            print("\033[3m- You will regret this. -\033[0m")
            short_pause()
            ok()
            break
        playerName = input("What is your name? ")
        if times_name_asked < 3:
            print(f"Are you sure your name is {playerName}?{'?'*times_name_asked}")
        elif times_name_asked == 3:
            print(f"Are you sure your name is {playerName}!")
        elif times_name_asked == 4:
            print(f"YOU. NAME. {playerName.upper()}???")
        else:
            print(f"Last chance {playerName}.")
        if yn():
            break
        times_name_asked += 1
    
    player.name = playerName
    
    # goofy intro
    if not skip_intro:
        print(f"{embolden('???:')}\tSo uhh {playerName}, you will be handling a veeeery important task today.")
        short_pause()
        print(f"{embolden('???:')}\tYou see, I, {embolden('Melon Musk')}, will be holding a very serious robotics expo today.")
        short_pause()
        print(f"{embolden('Usk:')}\tIn this expo, we will be showcasing some of our (supposedly) fully autonomous robots!")
        short_pause()
        print(f"{embolden('Usk:')}\tUnfortunately, despite me constantly rushing my engineers to complete the thing,")
        short_pause()
        print(f"{embolden('Usk:')}\tThey still could't make the robots autonomous in time!")
        short_pause()
        print(f"{embolden('Usk:')}\tSo what I want you to do is to control these robots behind the scenes.")
        short_pause()
        print(f"{embolden('Usk:')}\tIf you are able to fool my guests, I'll pay you handsomely!")
        short_pause()
        print(f"{embolden('Usk:')}\tI'm a billionare after all.")
        short_pause()
        print(f"{embolden('Usk:')}\t(If you don't, I will erase your entire lineage.)")
        short_pause()
        print(f"{embolden('Usk:')}\tHave fun {playerName}!")
        short_pause()
        print("\033[3m- Voicemail ends -\033[0m")
        short_pause()
        confirm('w', "What did I just hear?")
        print("\033[3mAt the expo...\033[0m")
        short_pause(3)

    return playerName

def play_ending(player):
    playerName = player.name
    print(f"{embolden('Usk:')}\tHow's it going {playerName}?")
    short_pause()
    print(f"{embolden('Usk:')}\tYou did a great job today.")
    short_pause()
    print(f"{embolden('Usk:')}\tAll my guests thought that the robots in the expo were actually thinking by themselves!")
    short_pause()
    print(f"{embolden('Usk:')}\tAs promised, I'll pay you handsomely for all your efforts today.")
    short_pause()
    confirm('w', "What in the hell is this??")
    short_pause()
    print(f"{embolden('Usk:')}\tThis is a gun. My reward for you will be a bullet in the head.")
    short_pause()
    print(f"{embolden('Usk:')}\tYou didn't seriously think that you'd be able to be privy to the fact that I employ people to pretend to be AI...")
    short_pause()
    print(f"{embolden('Usk:')}\t...and leave here alive, right?")
    short_pause()
    confirm('y', "You can't do this, Melon. Murder is a crime, you know")
    short_pause()
    print(f"{embolden('Usk:')}\tI'm a billionare. I make my own laws.")
    short_pause(3)
    print("""
 _______  __   __  _______    _______  __    _  ______  
|       ||  | |  ||       |  |       ||  |  | ||      | 
|_     _||  |_|  ||    ___|  |    ___||   |_| ||  _    |
  |   |  |       ||   |___   |   |___ |       || | |   |
  |   |  |       ||    ___|  |    ___||  _    || |_|   |
  |   |  |   _   ||   |___   |   |___ | | |   ||       |
  |___|  |__| |__||_______|  |_______||_|  |__||______| 
    \\encore!/\\encore!/\\encore!/\\encore!/\\encore!/
(you are dead)""")
    short_pause(3)
    ok()

