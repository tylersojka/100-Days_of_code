# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# name1 = "Tyler sojka"
# name2 = "Kayla hams"

# change names to lowercase
name1 = name1.lower()
name2 = name2.lower()
# combine the two names
combo_name = name1 + name2
# count occurances of the letters 
# true = combo_name.count("t")+combo_name.count("r")+combo_name.count("u")+combo_name.count("e")
# love = combo_name.count("l")+combo_name.count("o")+combo_name.count("v")+combo_name.count("e")
true = sum(map(combo_name.count, ["l","o","v","e"]))
love = sum(map(combo_name.count, ["t","r","u","e"]))


# convert to strings so we can add the digits ("5"+"3" = 53 instead of 8)
love_score = str(true) + str(love)
#convert back to int so we can use opperands on the numbers
love_score = int(love_score)

if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif love_score >= 40 and love_score <=50:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')
