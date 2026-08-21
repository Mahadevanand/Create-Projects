import os

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def sub(a, b):
    return a - b

# Function to multiply two numbers
def mul(a, b):
    return a * b

# Function to divide two numbers
def div(a, b):
    return a / b


# Dictionary that stores operation symbols and their functions
operations_dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


# Main calculator loop
while True:

    # Get the first number from the user
    number1 = float(input("Enter a number: "))

    # Display the available operations
    print("Available operations:")

    # Print each operation symbol
    for symbol in operations_dict:
        print(symbol)

    # Variable to control continuous calculation
    continue_calculation = True

    # Continue calculating until the user chooses a new calculation
    while continue_calculation:

        # Ask the user to choose an operation
        op_symbol = input("Choose an operation: ")

        # Check whether the entered operation is valid
        if op_symbol not in operations_dict:
            print("Invalid operation! Please choose +, -, *, or /")
            continue

        # Get the second number from the user
        number2 = float(input("Enter another number: "))

        # Check for division by zero
        if op_symbol == "/" and number2 == 0:
            print("Cannot divide by zero!")
            continue

        # Get the function corresponding to the operation symbol
        operation_function = operations_dict[op_symbol]

        # Perform the selected operation
        output = operation_function(number1, number2)

        # Display the calculation result
        print(f"{number1} {op_symbol} {number2} = {output}")

        # Ask the user what they want to do next
        choice = input(
            f"Enter 'y' to continue with {output}, "
            f"'n' for a new calculation, or 'x' to exit: "
        ).lower()

        # If user enters y, use the previous result as the first number
        if choice == "y":
            number1 = output

        # If user enters n, start a new calculation
        elif choice == "n":
            continue_calculation = False

            # Clear the screen
            # "cls" is used for Windows
            # "clear" is used for Linux/Mac
            os.system("cls" if os.name == "nt" else "clear")

        # If user enters x, exit the calculator
        elif choice == "x":
            print("Bye!")
            exit()

        # Handle an invalid choice
        else:
            print("Invalid choice. Starting a new calculation.")
            continue_calculation = False
