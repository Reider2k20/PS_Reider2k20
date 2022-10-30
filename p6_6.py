import random


class NumbersError(Exception):
    def __str__(self):
        return f"first number bigger then second"


def check_numbers(num1, num2):
    if num1 <= num2:
        num = random.randint(num1, num2)
        print(num)
    else:
        raise NumbersError()

num1 = int(input("print number 1 "))
num2 = int(input("print number 2 "))

check_numbers(num1, num2)

