#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("welcome to the tip calculator")
amount = float(input("what was the total cost of the bill?\n$"))
people = float(input("how many people will be splitting the bill?\n"))
percentage = float(input("what percent tip would you like to leave?\n%"))
per_person = (((amount + amount * (percentage / 100))/people))
print(round(per_person, 2))