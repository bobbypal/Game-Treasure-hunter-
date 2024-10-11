# Welcome to treasure hunter.
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choose1 = input("   Choose Left or Right : ").lower()
if choose1 == "right":
    print("Congrats!! You escaped from felling into hole ")
    print("Now you are on one side of the bank of amazon river")
    choose2 = input("Now Do you want to Swim or Wait for the boat to come ? ").lower()
    if choose2 == "wait":
        print(" Ohoo cool, good choice : this river is too danger full of Piranha's and crocodiles ")
        print(" You are just one step towards your treasure .......There are 3 door in front of you Blue, Yellow and Red. ")
        choose3 = input("Which door will you choose : ").lower()
        if choose3 == "blue":
            print("Eaten by beasts.")
            print('''
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"''')
            print("--GAME OVER--")
        elif choose3 == "yellow":
            print("Congratulation YOU WIN !")
        elif choose3 == "red":
            print('''
    .(
   /%/\
  (%(%))
 .-'..`-.
 `-'.'`-'dd''')
            print("Burned by fire.")
            print("--GAME OVER--")
        else:
            print("Invalid inputs")

    elif choose2 == "swim":
        print('''
          ,---,
  _    _,-'    `--,
 ( `-,'            `\
  \           ,    o \
  /   ,       ;       \
 (_,-' \       `, _  ""/
     pb `-,___ =='__,-'
              ````''')
        print("Attacked by Piranha's ")
        print("--GAME OVER--")
    else:
        print("Invalid inputs")

elif choose1 == "left":
    print('''
                                      +---+
                                      |\   \
  +-----------------------------+     | +---+
   \                      +-----------+ |   |
    \                      \            |   |
     \                 |/   +-----------+   |
      \                (c_      |   \ | |   |
       \                \       |    \| |   |
        \                       |     | |   |
         \                      |     + |   |
          \                     |      \| DM|
           \--------------------+       +---+
            \                    \        \
             \                    \        \
              +-----------------------------+
''')
    print(" You fell into the hole ")
    print("--GAME OVER--")
else:
    print("Invalid inputs")

