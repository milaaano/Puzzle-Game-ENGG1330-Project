# functions that interface with the user.

# prompts user to enter a command of choice.
# please use lowercase keys!
from formatting import *

def prompt(proposals: dict):
    for key in proposals:
        print(f"\033[1m[{key.upper()}]\033[0m {proposals[key]}")
    inp = None

    print("Enter a character above.")

    while True:
        inp = input(">>>").lower()
        if inp in proposals:
            break
        print("What? Try again")
    
    return inp

_OPTIONS = {
    'p': "Pause game",
    'q': "Quit game",
    'r': "Restart level",
    'n': "Nevermind"
}

_OPTION_MAP = {
    'p': "Pause",
    'q': "Quit",
    'r': "Restart Level",
    'n': "None"
}

def options():
    fancy_bar("OPTIONS", start_from=5)
    return _OPTION_MAP[prompt(_OPTIONS)]

_YN = {
    'y': "Yes!",
    'n': "No!"
}

def yn():
    return prompt(_YN) == 'y'

def confirm(key, msg):
    proposal = {}
    proposal[key] = msg
    prompt(proposal)

def ok():
    confirm('k', "Ok.")

FANCY_BAR_PATTERN       = ('⫻', '/')
FANCY_BAR_PATTERN_SIZE  = len(FANCY_BAR_PATTERN)

def fancy_bar(text="", length=20, start_from=0):
    def bar(start, end):
        return "".join(FANCY_BAR_PATTERN[i%FANCY_BAR_PATTERN_SIZE] for i in range(start, end)) if start < end else ""
    if text != "":
        text = f" {text} "
    excess_space_len = start_from - length
    print(ansi_format(bar(0, min(start_from, length)) + (" " * excess_space_len if excess_space_len > 0 else "") + text + bar(start_from + len(text), length), Format.bold))
    
