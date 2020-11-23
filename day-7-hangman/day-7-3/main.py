#Step 

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display. (to hold "_" for each letter of word)
display = []
for i in range(0,len(chosen_word)):
    display.append("_")

print(display)
# step 3 #Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.TODO-1: -

while "_" in display:

    # user guess
    guess = input("Guess a letter: ").lower()

    # loop through the word and replace "_" with letter if correct
    counter = 0
    for letter in chosen_word:
        if letter == guess:
            display[counter] = letter
        counter += 1

    print(display)
print("YOU WIN!")