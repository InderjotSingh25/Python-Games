print(r'''
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
choice1 = input("you are at the crossroad. where do you want to go? (left or right)\n").lower()
if choice1 == "left":
    choice2 = input('you have come to a lake. '
                    'there is a island on the other side. '
                    'type "wait" to wait for the boat. '
                    'type "swim" to swim across the lake \n').lower()
    if choice2 == "wait":
        choice3 = input("you arrived at the island unharmed. "
          "there are three doors one red,"
          " one yellow and one blue. choose one door.\n").lower()
        if choice3 == "red":
            print("room was full of snakes...\nGAMEOVER!  ")
        elif choice3 == "yellow":
            print("you found the treasure. you won")
        elif choice3 == "blue":
            print("you were poisoned...\nGAMEOVER")
        else:
            print("ou choose the door that does not existed.game over")
    else:
        print("there were crocodiles in the lake...\nGAMEOVER!")
else:
    print("you fell into a hole. game over")
