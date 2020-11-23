import random
import hangman_words
import hangman_art


stages = hangman_art.stages
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

#lives variable
lives = 6
incorrect_guesses = [] 
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display. (to hold "_" for each letter of word)
display = []
for i in range(0,len(chosen_word)):
    display.append("_")

word_len = len(chosen_word)
#Join all the elements in the list and turn it into a String.
print(stages[lives])
print("Word: " + ' '.join(display) + "\n")

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

    # if letter is not in word decrease lives
    if guess not in chosen_word:
        lives -= 1
        incorrect_guesses.append(guess)
    #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word
       

    print("\n\n\nIncorrect Guesses: ") 
    print(" ".join(incorrect_guesses))
    print(stages[lives])
    print("Word: " + ' '.join(display) + "\n")

    if lives > 0:
        you_lose = False
    else:
        you_lose = True
        print("YOU LOSE")
        print("The Word Was: " + chosen_word)
    if "_" in display:
        you_win = False
    else:
        you_win = True
        print("YOU WIN")


