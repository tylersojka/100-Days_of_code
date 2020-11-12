# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

#Write your code below this line 👇
meter = 39.3701

print("Welcome to the BMI calculator!")
weight = float(input("What is your weight?\nlbs"))
height = float(input("what is your height (ft)\n"))
inches = float(input("what is your height (in)\n"))

imperial_height = (height * 12) + inches
metric_height = imperial_height / meter
metric_weight = weight * 0.453592
# print(str(metric_height) + "meters")
# print(str(imperial_height) + "inches")
# print(str(metric_weight) + "kgs")
BMI = metric_weight / (metric_height**2)
print(f'Your BMI is {round(BMI)}')
if BMI < 18.5:
    print("You are underweight")
elif BMI < 25:
    print("You are a normal weight")
elif BMI < 30:
    print("you are slightly overweight")
elif BMI < 35:
    print("you are obese")
else:
    print("you are clinically obese, please contact my 600lb life")
