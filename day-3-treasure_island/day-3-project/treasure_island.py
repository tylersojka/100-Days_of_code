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
choice_1 = input("After searching for days, you find an overgrown cave entrance. What do you do? Type 'Enter' to enter or 'Ignore' to keep wandering\n")
if choice_1.lower() == "enter":
    choice_2 = input("You enter the cave and notice a patch of delicious strawberries. if you don't eat soon you will surely die. What do you do? Type 'Eat' to eat some strawberries or 'Continue' to search for something else.\n")
    if choice_2.lower() == "eat":
        print("What you thought were strawberries were actually deathberries, and you die. GAME OVER")
    else:
        print("After searching the cave for hours, you get lost and starve to death. GAME OVER")
else:
    choice_3 = input("You continue walking, in no particular direction until you come across a raging river. the river is too deep to cross. What do you do? Type 'South' to follow the river South, or 'North' to follow the river North\n")
    if choice_3.lower() == "north":
        choice_4 = input("After walking for what seems to be hours, you realize you are being followed. What do you do? Type 'Turn' to turn around and look for your pursuer, or 'Ignore' to keep walking\n")
        if choice_4.lower() == "turn":
            print("You are shot in the face with an arrow and die. GAME OVER")
        else:
            print("You are shot in the back of the head with an arrow and die GAME OVER")
    else:
        choice_5 = input("You walk until you trip on a grassy mound. Type 'Kick' to kick the mound out of anger or 'continue' to keep walking.\n")
        if choice_5.lower() == 'kick':
            print("The mound you kick is a lot harder than you think, after further investigation you notice its actually a hastily buried treasure chest! YOU WIN")
        else:
            print("As you walk, your stubbed foot starts to ache. you take off your boot to rub your foot when suddenly you are attacked by a bear and die. GAME OVER")