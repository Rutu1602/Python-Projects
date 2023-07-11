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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction = input("You are at a crossroad, where do you want to go? 'Left' or 'Right' ").lower()
# print(direction)

if direction == "left":
    make_a_choice = input("You came across a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim ").lower()
    # print(make_a_choice)

    if make_a_choice == "wait":
        select_door = input("You arrived at the island umharmed. There is a house with 3 doors. One red, one blue and one yellow. Which colour you will choose? ").lower()
        # print(select_door)

        if select_door == "red":
            print("Congratulation! You found the treasure.")
        elif select_door == "blue":
            print("You enter a room of beasts! Game over.")
        elif select_door == "yellow":
            print("You enter a room full of fire! Game over.")
        else:
            print("Invalid choice!")

    elif make_a_choice == "swim":
        print("You were eaten by a crocodile. Please try again!")
    else:
        print("Invalid choice!")
    
elif direction == "right":
    print("Game over!!! Please try again.")
else:
    print("Invalid choice!")


