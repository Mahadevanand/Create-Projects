import os

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

operations_dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

while True:
    number1 = float(input("Enter a number: "))

    print("Available operations:")
    for symbol in operations_dict:
        print(symbol)

    continue_calculation = True

    while continue_calculation:
        op_symbol = input("Choose an operation: ")

        if op_symbol not in operations_dict:
            print("Invalid operation! Please choose +, -, *, or /")
            continue

        number2 = float(input("Enter another number: "))

        if op_symbol == "/" and number2 == 0:
            print("Cannot divide by zero!")
            continue

        operation_function = operations_dict[op_symbol]
        output = operation_function(number1, number2)

        print(f"{number1} {op_symbol} {number2} = {output}")

        choice = input(
            f"Enter 'y' to continue with {output}, "
            f"'n' for a new calculation, or 'x' to exit: "
        ).lower()

        if choice == "y":
            number1 = output
        elif choice == "n":
            continue_calculation = False
            os.system("cls" if os.name == "nt" else "clear")
        elif choice == "x":
            print("Bye!")
            exit()
        else:
            print("Invalid choice. Starting a new calculation.")
            continue_calculation = False
