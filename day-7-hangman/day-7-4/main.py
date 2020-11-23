stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Step 

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display. (to hold "_" for each letter of word)
display = []
for i in range(0,len(chosen_word)):
    display.append("_")

word_len = len(chosen_word)
#Join all the elements in the list and turn it into a String.
print(stages[lives])
print(" ".join(display))

# while loop to loop guesses till win or lose
you_win = False
you_lose = False
while you_win != True and you_lose != True:
    # user guess
    guess = input("Guess a letter: ").lower()

    # loop through the word and replace "_" with letter if correct
    # counter = 0
    # for letter in chosen_word:
    #     if letter == guess:
    #         display[counter] = letter
    #     counter += 1    
    for position in range(0, word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    if guess not in chosen_word:
        lives -= 1
    

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    # if letter not in chosen_word:
    #     lives -= 1
    # print(lives)
    
    print(stages[lives])
    print(" ".join(display))

    if lives > 0:
        you_lose = False
    else:
        you_lose = True
        print("YOU LOSE")
    if "_" in display:
        you_win = False
    else:
        you_win = True
        print("YOU WIN")


 #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.