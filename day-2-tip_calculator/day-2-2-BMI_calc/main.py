meter = 39.3701
foot = 12
inch = 1

print("Welcome to the BMI calculator!")
weight = float(input("What is your weight?\nlbs"))
height = float(input("what is your height (ft)\n"))
inches = float(input("what is your height (in)\n"))

imperial_height = (height * 12) + inches
metric_height = imperial_height / meter
metric_weight = weight * 0.453592
print(str(metric_height) + "meters")
print(str(imperial_height) + "inches")
print(str(metric_weight) + "kgs")
BMI = metric_weight / (metric_height**2)
print(int(BMI))