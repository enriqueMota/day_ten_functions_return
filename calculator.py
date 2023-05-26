# Calculator  on python


# Creating the basic
# arithmetic functions

# Adding
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Assigning the operations on they're symbols
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = int(input("What's the first number?: "))
    num2 = int(input("What's the second number?: "))
    for operation in operations:
        print(operation)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        first_result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {first_result}")

        if input(f"Type 'y' to continue calculating with {first_result} or type 'n' to exit.: ") == 'y':
            num1 = first_result
        else:
            should_continue = False
            calculator()


calculator()