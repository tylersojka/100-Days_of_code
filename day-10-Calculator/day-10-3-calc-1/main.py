from replit import clear
clear()



def calculator(number_one, opperator, second_number):
    if opperator == "+":
        return number_one + number_two
    elif opperator == "-":
        return number_one - number_two
    elif opperator == "*":
        return number_one * number_two
    elif opperator == "/":
        return number_one / number_two

       
new_calc = True
while new_calc == True:
    number_one = int(input("what is your first number?: "))
    same_calc = True
    while same_calc == True:
        opperator = input("which opperator would you like to use? choose one: ( + - * / ): ")
        number_two = int(input("what is your next number?: "))

        result = calculator(number_one, opperator, number_two)
        print(f"{number_one} {opperator} {number_two} = {result}")



        new_same_calc = input(f'Type "Y" to keep calculating with {result} or "N" to start a new calculation: ').lower()
        if new_same_calc == "y":
            same_calc = True
            number_one = result
        elif new_same_calc == "n":
            same_calc = False
    
