import os
from Day10_CalculatorArt import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2 if n2 > 0 else 0


operation_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator(first_num, second_num, operator):
    result = 0
    result = operation_dict[operator](first_num, second_num)
    # match operator:
    #     case "+":
    #         result = first_num + second_num
    #     case "-":
    #         result = operation_dict["-"](first_num,second_num)
    #     case "*":
    #         result = operation_dict["*"](first_num,second_num)
    #     case "/":
    #         if second_num > 0:
    #             result = first_num / second_num
    #         else:
    #             result = 0
    #     case "%":
    #         result = first_num % second_num
    #     case default:
    #         print("Choose from operator list")
    #         return 0

    return result


def main_menu():
    first_num = float(input("Enter the First Number: "))
    direction = True
    while direction:
        operation = input("+\n-\n*\n/\n\nPick an Operation: ")
        second_num = float(input("Enter the Next Number: "))
        answer = calculator(first_num, second_num, operation)
        print(f"{first_num} {operation} {second_num} = {answer}")
        go_ahead = input(
            f"Type 'y' to continue calculation with {answer}. Or type 'n' to start a new Calculator: ").lower()
        if go_ahead == "y":
            first_num = answer

        else:
            print('\n' * 100)
            main_menu()


print(logo)
main_menu()
