from replit import clear
from art import logo

clear()
# add repeat function to introduce recursion, allows the while 
# loop to be broken and start the whole system over again
print(logo)
def repeat():
    def calculator(number_one, opperator, second_number):
        if opperator == "+":
            return number_one + number_two
        elif opperator == "-":
            return number_one - number_two
        elif opperator == "*":
            return number_one * number_two
        elif opperator == "/":
            return number_one / number_two

       
# new_calc = True
# while new_calc == True:
    # start the user input for the calculator function call
    number_one = float(input("what is your first number?: "))
    # flag to start the reuse result loop
    same_calc = True
    while same_calc == True:
        opperator = input("which opperator would you like to use? choose one: ( + - * / ): ")
        number_two = float(input("what is your next number?: "))

        result = calculator(number_one, opperator, number_two)
        print(f"{number_one} {opperator} {number_two} = {result}")
        # ask to go again or start over, if go again set the result equal to number one for the calculation
        if input(f'Type "Y" to keep calculating with {result} or "N" to start a new calculation: ').lower() == "y":
            number_one = result
        # if start again, break the while loop and call the start of the function
        else:
            clear()
            repeat()

# initially call the repeat function to start the calculator loop
repeat()