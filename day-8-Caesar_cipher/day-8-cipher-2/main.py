alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
text = "abcxyz"
shift = 3



message = []
encoded_message = []
def encrypt(text, shift):
    for letter in text:
        message.append(alphabet.index(letter) + shift)
    for item in message:
        if item > int(len(alphabet)-1):
            item -= 26
        encoded_message.append(alphabet[item])
    print("Your Encrypted Message is: " + "".join(encoded_message))
        

decoded_message = []
def decrypt(text, shift):
    for letter in text:
        message.append(alphabet.index(letter) - shift)
    for item in message:
        if item > int(len(alphabet)-1):
            item -= 26
        encoded_message.append(alphabet[item])
    print("Your Decrypted Message is: " + "".join(encoded_message))
        

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)





# or and adding a second set of a-z in the alphabet
# def encrypt(text, shift):
#   cipher_text = ""
#   for letter in text:
#     position = alphabet.index(letter)
#     new_position = position + shift
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The encoded text is {cipher_text}"