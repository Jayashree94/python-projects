import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b  
def multiply(a,b):
    return a*b  
def divide(a,b):
    return a/b

operation_dictionary = {
    "+": add,   
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculate():

    number1 = float(input("Enter the first number: "))
    for symbol in operation_dictionary:
        print(symbol)

    continue_calculation = True
    while continue_calculation:

        operation_symbol = input("Pick an operation from the line above: ")
        number2 = float(input("Enter the second number: "))

        result =operation_dictionary[operation_symbol](number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {result}")

        continue_calculation = input(f"Enter 'y' to continue calculating with {result}, or enter 'n' to start a new calculation or 'x' toexit: ").lower()
        if continue_calculation == 'y':
            number1 = result
        elif continue_calculation == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue_calculation = False
            calculate()
        elif continue_calculation == 'x':
            continue_calculation = False
            print("Thank you for using the calculator. Goodbye!")
calculate()
    
