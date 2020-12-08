#Write your code below this line 👇
def prime_checker(number):
    prime_count = 0
    for x in range(1, number + 1):
        if number % x == 0: 
            prime_count += 1     
    if prime_count == 2:
        print(f"{number} is Prime!")    
    else:
        print(f"{number} is not prime")

# or 
# def prime_checker(number):
#     is_prime = True
#     for x in range(2, number):
#         if number % x == 0:
#             is_prime = False
#         print(x)
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

    
        


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


