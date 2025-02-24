from Print import *
from formatting import *
from Interface import *
from Resources import *

def instructions(screen):

    """
    0    5        
  0 ######### 
    #p..XOT.# <<[x=1, You]<<[x=6, T:-3T]
    ###.###-# 
    #T#...#T# <<[x=1, T:-2T]<<[x=7, T:-2T]
    #####.#$# <<[x=7, $:+5T]
  5 #.XX..#$# <<[x=7, $:+5T]
    #$$X..#-# <<[x=1, $:+5T]<<[x=2, $:+5T]
    #$.....E# <<[x=1, $:+5T]
    ######### 

⫻ TURN 1 /
OPERATOR: Joseph R. Biden, the 46th President of the United States
SUBJECT <p> x=1, y=1
TOKENS: 10
⫻/⫻/⫻/⫻/⫻/"""

    instructions = [
        [
            "",
            "Welcome to INSTRUCTIONS!",
            "",
            "Here we will go over the UI",
            "",
            "and the basic mechanics of the game.",
            "",
            "Lets learn the mechanics one by one."
        ],
        [
            "Let's take a look at how a map is displayed.",
        ],
        [
            "Here is the UI.",
        ],
        [
            "Here are some of the symbols you will",
            "                         see on a map.",
            "",
            "<p> is the PLAYER.",
            "<S> is the START POINT.",
            "<E> is the END POINT.",
            "",
            "Once a level loads,",
            "PLAYER spawns at the START POINT.",
            "PLAYER wins when they reach END POINT.",
        ],
        [
            "<.> is a FREE SPACE,",
            "It is traversable.",
            "<#> is a WALL.",
            "It is not traversable.",
            "",
            "<$> is a COIN.",
            "Touching it increases your TOKEN(s).",
            "",
            "T is a TUNNEL.",
            "Pay TOKEN(s) to gain entry to TUNNELs."
        ],
        [
            "<X> is a BOX.",
            "It can be pushed by the PLAYER.",
            "Multiple BOXes that are lined up can be",
            "                        pushed together.",
            "<O> is a BUTTON.",
            "When a BOX is on a BUTTON, it activates ",
            "      some DOORs and deactivates others.",
            "Pushing a BOX away from the BUTTON does",
            "                           the opposite.",
            "<-> is a DOOR.",
            "This door is open.",
            "When opened, it appears as <#>(cyan).",
            "Opened DOORs are traversable; closed",
            "                       DOORs are not."
        ],
        [
            "TOKEN is the main currency of the game.",
            "Every move by the player consumes TOKENs.",
            "TOKENs can also be used to pay TUNNEL tolls.",
            "",
            "When you beat a level, your remaining",
            "          TOKENs determine your score,",
            "So try to preserve as much TOKENs as possible!"
        ],
        [
            "",
            "",
            "",
            "",
            "That's all! Good luck on your Unpaid Quest."
        ]
    ]
    
    for i, instruction in enumerate(instructions):
        true_col = 8 if i == 1 or i == 2 else 20
        screen = Screen(true_col, 52)
        row, col = screen.getSize()
        screen.defScreen(' ')
        screen.writeTextL(1, 5, "INSTRUCTIONS")
        for j, line in enumerate(instruction, 4):          
            screen.writeTextL(row // true_col * j, 3, line)
            #screen.writeText(row - 2, col //2, "Press Enter(e) to Continue, or Quit(q) to Exit")
        screen.printScreen()
        if i == 1:
            print(f"""
    0    5        
  0 ######### 
    #p..XO..# <<[x=1, You]   {embolden('<-- You are here')}
    ###.###-# 
    #T#...#.# <<[x=1, T:-2T] {embolden('<-- Pay 2 TOKENs to step on T')}
    #####.#T# <<[x=7, T:-2T]
  5 #.XX..#$# <<[x=7, $:+5T]
    #$$X..#-# <<[x=1, $:+5T]<<[x=2, $:+5T]
    #$.....E# <<[x=1, $:+5T] {embolden('<-- Gain 5 TOKENs by stepping on $')}
    ######### 
            """)
        elif i == 2:
            print(f"""
/ TURN 1 /          {embolden('<-- Current turn')}
OPERATOR: Jason     {embolden('<-- Your name')}
SUBJECT <p> x=1, y=1{embolden('<-- Your coordinates on the map')}
TOKENS: 10          {embolden('<-- No. of TOKENs in disposal')}
//////////
[W] Use command <UP>    --1 TOKEN(S)
[S] Use command <DOWN>  --1 TOKEN(S)
[A] Use command <LEFT>  --1 TOKEN(S)
[D] Use command <RIGHT> --1 TOKEN(S)
[O] Options...
{embolden('^^^ w, a, s, d keys to move; o key for options')}
            """)
        confirm('e', "Continue")

    return 'Main Menu' 


