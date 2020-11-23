import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

error = '''
  ___ _ __ _ __ ___  _ __ 
 / _ \ '__| '__/ _ \| '__|
|  __/ |  | | | (_) | |   
 \___|_|  |_|  \___/|_| 
 '''

# print("Welcome to Rock Paper Scissors!")
# user_throw = input("To throw, type 'Rock' 'Paper' or 'Scissors'\n").lower()

# computer_throw = random.randint(0,2)
# if computer_throw == 0:
#     computer_throw = 'r'
# elif computer_throw == 1:
#     computer_throw = "p"
# elif computer_throw == 2:
#      computer_throw = "s"

# if user_throw == "rock":
#     throw = 'r'
# elif user_throw == "paper":
#     throw = 'p'
# else:
#     throw = 's'


# if throw == 'r' and computer_throw == 'r':
#     print(f'you throw: {rock} \n computer throws: {rock} \n its a draw!')
# elif throw == 'r' and computer_throw == 'p':
#     print(f'you throw: {rock} \n computer throws: {paper} \n you LOSE!')
# elif throw == 'r' and computer_throw == 's':
#     print(f'you throw: {rock} \n computer throws: {scissors} \n you WIN!')

# if throw == 's' and computer_throw == 'r':
#     print(f'you throw: {scissors} \n computer throws: {rock} \n you LOSE!')
# elif throw == 's' and computer_throw == 'p':
#     print(f'you throw: {scissors} \n computer throws: {paper} \n you WIN!')
# elif throw == 's' and computer_throw == 's':
#     print(f'you throw: {scissors} \n computer throws: {scissors} \n its a draw!')

# if throw == 'p' and computer_throw == 'r':
#     print(f'you throw: {paper} \n computer throws: {rock} \n you WIN!')
# elif throw == 'p' and computer_throw == 'p':
#     print(f'you throw: {paper} \n computer throws: {paper} \n its a draw!')
# elif throw == 'p' and computer_throw == 's':
#     print(f'you throw: {paper} \n computer throws: {scissors} \n you LOSE!')

## way more elegant way 

game_images = [rock, paper, scissors, error]
print('Welcome to the exciting game of Rock Paper Scissors!')
user_choice = int(input("What would you like to throw? Type '0' for Rock, '1' for Paper or '2' for Scissors\n"))

if user_choice >=3 or user_choice < 0:
    print(game_images[3])
    print("You typed an invalid choice, idiot.")
else:
    print(f'You threw: {game_images[user_choice]}')

    computer_choice = random.randint(0,2)
    print(f'The computer throws: {game_images[computer_choice]}')

    if user_choice >= 3 or user_choice < 0:
        print ("You typed an invalid choice, YOU LOSE")
    elif user_choice == 0 and computer_choice == 2:
        print ("You WIN")
    elif computer_choice == 0 and user_choice == 2:
        print("You LOSE!")
    elif computer_choice > user_choice:
        print ('You LOSE')
    elif user_choice > computer_choice:
        print("You WIN")
    elif computer_choice == user_choice:
        print("It's a draw")
