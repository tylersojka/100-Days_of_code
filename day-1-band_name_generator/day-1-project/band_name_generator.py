#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

print("Welcome to Band Name Generator!")
city = input("Lets start with what was the city you grew up in?\n")
pet = input("Next, what was the name of your first pet?\n")
print("The name of your band should be The " + city + " " + pet + "s")