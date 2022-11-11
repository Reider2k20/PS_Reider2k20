import colorama
from colorama import Fore
def checker(example):
    def checker(*args, **kwargs):
        try:
            result = example(*args, **kwargs)
        except Exception as exc:
            print(f"Sir we have problem with {exc}, please try to solve this problem")
        else:
            if int(result) == result:
                result = int(result)
            else:
                pass
            print("Problems not found, "+ Fore.GREEN +f"Result = {result}"+ Fore.RESET)
    return checker

def calculate(expression):
    return eval(expression)

print("To get the root of a number you need to write this number (a), then write the exponentiation action (**), open parentheses and write 1/b in them, where b is the power of your root,")
print("the result should be something like this " + Fore.GREEN +"a ** ( 1 / b )"+ Fore.RESET)
print("Example:")
print(Fore.GREEN +"4 ** ( 1 / 2 ) = 2"+ Fore.RESET)
print("")

calculator = checker(calculate)
calculator(str(input("Print your example: ")))