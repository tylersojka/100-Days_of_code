#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# nr_letters = 4
# nr_symbols = 4
# nr_numbers = 4



#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# # nr_letters amount of random letters
# letters_list = []
# for letter in range(1, nr_letters + 1):
#     letter = random.randint(0, 50)
#     letters_list.append(letter)
# print(letters_list)

# # nr_numbers amount of random numbers
# num_list = []
# for num in range(1, nr_numbers + 1):
#     num = random.randint(0,9)
#     num_list.append(num)
# print(num_list)

# # nr_symbols amount of random symbols
# symbol_list = []
# for symbol in range(1, nr_symbols + 1):
#     symbol = random.randint(0, 8)
#     symbol_list.append(symbol)
# print(symbol_list)



# password = []
# for letter in letters_list:
#     password.append(letters[letter])
# for symbol in symbol_list:
#     password.append(symbols[symbol])
# for number in num_list:
#     password.append(numbers[number])
# print(str(password))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# random_pw = []
# for character in password:
#     position = random.randint(0, len(password))
#     random_pw.insert(position, character)

# print("".join(random_pw))


# # more elegant
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

# random_pw = []
# for character in password:
#     position = random.randint(0, len(password))
#     random_pw.insert(position, character)

# print("".join(random_pw))

#even more elegant

password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))


print(password_list)
random.shuffle(password_list)
print("".join(password_list))