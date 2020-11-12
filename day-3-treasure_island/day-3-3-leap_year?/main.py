# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# if year % 400 == 0:
#     print(f'{year} is a leap year')
# else:
#     if year % 100 == 0:
#         print(f'{year} is not a leap year')
#     else:
#         if year % 4 == 0:
#             print(f'{year} is a leap year!')
#         else:
#             print(f'{year} is not a leap year!')

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap")
#         else:
#             print("not leap")
#     else:
#         print("leap")
# else:
#     print("not leap")

# if the year is divisible evenly by 4:
if year % 4 == 0:         
    # its a leap year
    print("leap")
# if not, is it divisible evenly by 100?
elif year % 100 == 0:
    #if so not a leap year
    print("not leap")
#if not is it divisible by 400?
elif year % 400 == 0:
    #if so, its a leap
    print("leap")
else:
    #if not its not a leap
    print("not leap")
