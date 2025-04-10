import math_utils


def calculate(x, y, operator):
    operations = {
        '+': math_utils.add,
        '-': math_utils.subtract,
        '*': math_utils.multiply,
        '/': math_utils.divide,
        '**': math_utils.power,
        '%': math_utils.mod
    }

    if operator in operations:
        return operations[operator](x, y)
    else:
        return "invalid operator"


if __name__ == "__main__":


    try:
        num1 = float(input("enter the first number: "))
        num2 = float(input("enter the second number: "))
        operator = input("enter the operator (+, -, *, /, **, %): ")

        result = calculate(num1, num2, operator)
        print(f"result: {result}")
    except Exception as e:
        print("Error: Please enter valid numbers.")

