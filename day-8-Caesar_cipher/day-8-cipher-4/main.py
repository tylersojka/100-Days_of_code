import art
import random
allascii = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


shuffled_ascii = [' ', 'X', 'c', 'h', '+', '2', 'i', 'e', 'l', '-', '%', 'D', '?', 'U', 'u', 'Z', '<', 'Y', '&', 'w', '!', 'f', '6', '1', ')', 'F', 'p', ']', 'W', 'T', 'G', 'v', 'C', 'B', 'P', 's', 'd', 'S', 'a', 'K', '$', '0', 'n', 'q', 'R', 'b', '8', '5', ',', 'A', '.', 'm', 'g', 'j', 'Q', 'O', '9', ';', '[', 'I', '#', 'k', '_', '3', '4', '>', '/', 'J', 'V', '(', 'o', 'N', '=', 'r', '7', '@', '\\', 'x', '"', '`', 'y', "'", 't', 'z', ':', 'M', 'E', 'L', '*', 'H', '^']


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#start the while loop
keep_going = True
# function body
def caesar(text, shift, direction):
    # to hold the shifted index list
    message = []
    # to hold the shifted list
    encoded_message = []
    # takes care of changing the shift direction for encode/decode
    if direction == "decode":
        shift *= -1
    # grab and append the ascii list index of the letter in the input
    for letter in text:
        message.append(shuffled_ascii.index(letter) + shift)
    
    for item in message:
        if item == " ":
            item += 1
        if item > int(len(shuffled_ascii)-1):
            item -= int(len(shuffled_ascii))
        encoded_message.append(shuffled_ascii[item])
    print(f"Your {direction}d message is: {''.join(encoded_message)}")

# print(art.logo)
 
while keep_going == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    shift = shift % 90
    caesar(text, shift, direction)


    keep_going = input("Would You Like To Go Again? (Y/N)\n").lower()
    if keep_going == "n":
        keep_going = False
    else:
        keep_going = True




# old function
# def caesar(text, shift, direction):
#     message = []
#     encoded_message = []

#     if direction == "decode":
#         shift *= -1
#     for letter in text:
#         if letter in alphabet:
#             message.append(alphabet.index(letter) + shift)
#         else:
#             message.append(letter)
#     for item in message:
#         if type(item) == str:
#             encoded_message.append(item)
#         else:
#             if item > int(len(alphabet)-1):
#                 item -= 26
#             encoded_message.append(alphabet[item])
#     print(f"Your {direction}d message is: {''.join(encoded_message)}")