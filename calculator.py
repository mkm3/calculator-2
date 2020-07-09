"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


def get_input():
    """Prompts user for input in prefix notation"""

    input_string = input("Enter your equation: ") # "+ 1 2"

    tokens = tokenizer(input_string)

    return validate_input(tokens)



def validate_input(tokens):
    valid_operators = ['+', '-', '*', '/', 'square', 'cube', 'power', 'mod']

    while True:

        if tokens[0] == 'q':
            print("Thanks for playing!")
            return tokens

        if tokens[0] not in valid_operators:

            print("That's not a valid operator. Please try again.")
            input_string = input("Enter your equation: ")
            tokens = tokenizer(input_string)


        elif tokens[0] == 'square' or tokens[0] == 'cube':
        
            try:
                tokens[1] = int(tokens[1])
                break
            
            except:
                print("You must enter a valid integer.")
                input_string = input("Enter your equation again: ")
                tokens = tokenizer(input_string)


        else:

            try:
                tokens[1] = int(tokens[1])
                tokens[2] = int(tokens[2])
                break
                
            except:
                print("You must enter two valid integers.")
                input_string = input("Enter your equation again: ")
                tokens = tokenizer(input_string)


    return tokens



def tokenizer(str):

    tokens = []

    tokens = str.split(" ") # ['+', '1', '2']

    return tokens



def do_arithmetic(operator, num1, num2=None):
    """Call function to calculate equation"""

    if operator == "+":
        return add(num1, num2)

    elif operator == "-":
        return subtract(num1, num2)

    elif operator == "*":
        return multiply(num1, num2)

    elif operator == "/":
        return divide(num1, num2)

    elif operator == "square":
        return square(num1)

    elif operator == "cube":
        return cube(num1)

    elif operator == "power":
        return power(num1, num2)

    elif operator == "mod":
        return mod(num1, num2)

    else:
        print("Error")



def calculator():
    """Calculates equation from input"""
    
    while True:
    
        tokens = get_input()
        
        operator = tokens[0]

        if operator == 'q':
            break

        num1 = tokens[1]


        if len(tokens) == 3:
            num2 = tokens[2]


        if len(tokens) == 3:
            output = do_arithmetic(operator, num1, num2)
            print(output)

        else:
            output = do_arithmetic(operator, num1)
            print(output)

    

calculator()


