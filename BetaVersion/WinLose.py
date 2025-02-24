#AlphaVersion/WinLose.py

from Print import*

ps=[]
historyscore=[]

def Win(scores, playerName, cont=True, quit=True):

   col=26
   row=20

   screen = Screen(row,col)

   screen.defScreen(' ')
   div=5

   with open('BetaVersion/HighScore.txt', 'r') as file:
      lines = file.readlines()
      if lines[0] == 0:
         highscore = 0
      else:
         print(lines[0])
         highscore = lines[2][:-1]

   lst=['Well done!','Victory is yours!','Your Score: '+str(scores),'highscore: '+str(highscore)]
   Lrow=row//(div+1)
   Lcol=col//2


   choice = 'None'
# ensure a valid input
   while (quit and choice!= 'quit') or (cont and choice!= 'continue'):
      Lrow=row//(div+1)
      Lcol=col//2
      for i in lst:
        screen.writeText(Lrow,Lcol,i)
        Lrow+=row//(div+1)
   
      screen.writeText(row-2,Lcol,(('Continue(c) ' if cont else '') + ('Quit(q) ' if quit else '')))

      screen.printScreen()

      choice=input('Your Choice: ').lower()
      if choice=='quit' or choice == 'q':
         if cont:
            store(playerName,scores)
            historyscore.append(scores) 
         return 'Main Menu'
      elif choice=='continue' or choice == 'c':
         return 'Next Level'
    

def Lose(scores=None, playerName=None, showScores=False):
   col=26
   row=20

   screen = Screen(row,col)

   with open('BetaVersion/HighScore.txt', 'r') as file:
      lines = file.readlines()
      if lines[0] == 0:
         highscore = 0
      else:
         highscore = lines[2][:-1]


   lst=['GAME OVER!','Better luck next time!']
   if showScores:
      lst += ['Your Score: '+str(scores),'highscore: '+str(highscore)]
   div=5
   Lrow=row//(div+1)
   Lcol=col//2
   #print(Lcol, Lrow)
   choice='None'

   while choice != 'Quit' or choice!= 'Play again':
      screen.defScreen(" ")
      Lrow = col//2
      for i in lst:
          screen.writeText(Lrow,Lcol,i)
          #print(i)
          Lrow+=row//(div+1)
      screen.writeText(row-2,Lcol,'Play Again(p), Quit(q)')
   
      screen.printScreen()
      choice=input('Your Choice:')
      choice = choice.lower()

      if choice=='quit' or choice == 'q':
         store(playerName,scores)
         historyscore.append(scores)
         return 'Main Menu'
      elif choice=='play again' or choice == 'p':
         return 'Play Again'


def store(pname,scores):
    players = []


    with open('BetaVersion/HighScore.txt', 'r') as file:
      lines = file.readlines()
    
    for i in range(1, len(lines), 2):
        name = lines[i].strip()  # Read player name
        #print(lines[i+1])
        grade = int(lines[i + 1].strip())  # Read player grade
        players.append((name, grade))  # Append as a tuple (name, grade)

# Sort players by grade in descending order
    players.append((pname,scores))
    #print(players)
    sorted_players = sorted(players, key=lambda x: x[1], reverse=True)

# Write the sorted players back to the file
    with open('BetaVersion/HighScore.txt', 'w') as file:
      file.write(f"{len(sorted_players)}\n")
      for player in sorted_players:
   
         file.write(f"{player[0]}\n")  # Write name into file
         file.write(f"{player[1]}\n")  # Write score into file

#Win(12, 'A')


