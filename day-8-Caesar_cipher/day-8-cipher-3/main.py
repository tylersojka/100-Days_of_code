alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

keep_going = True

def caesar(text, shift, direction):
    message = []
    encoded_message = []

    if direction == "decode":
        shift *= -1
    for letter in text:
        message.append(alphabet.index(letter) + shift)
    for item in message:
        if item > int(len(alphabet)-1):
            item -= 26
        encoded_message.append(alphabet[item])
    print(f"Your {direction}d message is: {''.join(encoded_message)}")

while keep_going == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    keep_going = input("Would You Like To Go Again? (Y/N)\n").lower()
    if keep_going == "n":
        keep_going = False
    else:
        keep_going = True