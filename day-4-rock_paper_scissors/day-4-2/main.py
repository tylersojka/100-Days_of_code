import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# names = ['tyler', 'kayla', 'jimmy', 'dillon', 'evan']

x = len(names)
bullet = random.randint(0,x-1)
who_pays = names[bullet]

print(x)
print(bullet)
print(f'{who_pays} pays the bill')