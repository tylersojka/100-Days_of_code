# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

death = 90
years_left = death - int(age)
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12
print(f"you have {days_left} days left to live\n"
      f"you have {weeks_left} weeks left to live\n"
      f"you have {months_left} months left to live\n"
      f"you have {years_left} years left to live")