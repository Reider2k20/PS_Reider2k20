import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore

a = float(25)
print(Fore.GREEN +"Hello user, this program is designed so that you do not strain your already busy brain so much.")
print("The program will do the calculations instead of you, first choose what exactly you need.")
print(Fore.LIGHTGREEN_EX +'After the solved example, you can write the received answer to the variable "a" and to use it later, just write "a" instead of the number in the example.')
print(Fore.GREEN +"You can always write 0 on any selection line to end the program."+ Fore.RESET)
print("")

while True:
    def converter():
        def counter(end):
            global a
            while end!=1 and end!=2 and end!=3:
                end = int(input(Fore.RED +'Please print 1, 2 or 3: '+ Fore.RESET))

            if end == 1:
                b = str(input(Fore.MAGENTA +'Print your amount of UAH: '+ Fore.RESET))
                if b == "a":
                    b = a
                elif b != "a":
                    b = float(b)
                print(Fore.GREEN + f'USD = {b / USD_in_UAH}$')
                print(f'EUR = {b / EUR_in_UAH}€'+ Fore.RESET)
                c = int(input(Fore.LIGHTGREEN_EX +"If you need write to variable USD, print '1', to write EUR, print '2': "+ Fore.RESET))
                if c == 1:
                    a = b / USD_in_UAH
                elif c == 2:
                    a = b / EUR_in_UAH
            elif end == 2:
                b = str(input(Fore.MAGENTA +'Print your amount of USD: '+ Fore.RESET))
                if b == "a":
                    b = a
                elif b != "a":
                    b = float(b)
                print(Fore.GREEN + f'UAH = {b * USD_in_UAH}₴')
                print(f'EUR = {b * USD_in_UAH / EUR_in_UAH}€'+ Fore.RESET)
                c = int(input(Fore.LIGHTGREEN_EX +"If you need write to variable UAH, print '1', to write EUR, print '2': "+ Fore.RESET))
                if c == 1:
                    a = b * USD_in_UAH
                elif c == 2:
                    a = b * USD_in_UAH / EUR_in_UAH
            elif end == 3:
                b = str(input(Fore.MAGENTA +'Print your amount of EUR: '+ Fore.RESET))
                if b == "a":
                    b = a
                elif b != "a":
                    b = float(b)
                print(Fore.GREEN + f'USD = {b*EUR_in_UAH / USD_in_UAH}$')
                print(f'UAH = {b*EUR_in_UAH}₴'+ Fore.RESET)
                c = int(input(Fore.LIGHTGREEN_EX +"If you need write to variable USD, print '1', to write UAH, print '2': "+ Fore.RESET))
                if c == 1:
                    a = b*EUR_in_UAH / USD_in_UAH
                elif c == 2:
                    a = b*EUR_in_UAH
            return a



        resp = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, features = "html.parser")
            soup_list = soup.find_all("td")
            res = str(soup_list[39]).split('<td data-label="Офіційний курс">')
            res = str(res[1]).split('</td>')
            USD_in_UAH = float(res[0].replace(',', '.'))

        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, features = "html.parser")
            soup_list = soup.find_all("td")
            res = str(soup_list[44]).split('<td data-label="Офіційний курс">')
            res = str(res[1]).split('</td>')
            EUR_in_UAH = float(res[0].replace(',', '.'))

        print(Fore.BLUE + f'USD in UAH = {USD_in_UAH}'+ Fore.RESET)
        print(Fore.BLUE + f'EUR in UAH = {EUR_in_UAH}'+ Fore.RESET)
        end = int(input(Fore.LIGHTGREEN_EX +"Choose convertor, if you neet from UAH to USD and EUR print 1, from USD to UAH and EUR print 2, from EUR to USD and UAH print 3: "+ Fore.RESET))
        if end == 0:
            sys.exit()
        counter(end)









    def calculator():
        def checker(example):
            def checker(*args, **kwargs):
                global a
                try:
                    result = example(*args, **kwargs)
                except Exception as exc:
                    print(Fore.LIGHTRED_EX +f"Sir we have problem with {exc}, please try to solve this problem"+ Fore.RESET)
                else:
                    if int(result) == result:
                        result = int(result)
                    else:
                        pass
                    print(Fore.BLUE +"Problems not found, "+ Fore.GREEN +f"Result = {result}"+ Fore.RESET)
                    c = str(input(Fore.LIGHTGREEN_EX +"If you need write to variable this result, print 'rem': "+ Fore.RESET))
                    if c == "rem":
                        a = result
            return checker

        def calculate(expression):
            return eval(expression)

        print(Fore.CYAN +"To get the root of a number you need to write this number (a), then write the exponentiation action (**), open parentheses and write 1/b in them, where b is the power of your root,")
        print("the result should be something like this "+ Fore.GREEN +"a ** ( 1 / b )"+ Fore.RESET)
        print(Fore.LIGHTMAGENTA_EX +"Example:")
        print(Fore.GREEN +"4 ** ( 1 / 2 ) = 2"+ Fore.RESET)
        print("")

        calculator = checker(calculate)
        test = str(input(Fore.LIGHTGREEN_EX +"Print your example: "+ Fore.RESET))
        if "a" in test:
            test = str(test.replace('a', f'{a}'))
        calculator(test)



    end = int(input(Fore.MAGENTA +"Write 1 if you need a currency converter, 2 for a simple calculator: "+ Fore.RESET))
    print("")
    if end == 0:
        sys.exit()
    if end == 1:
        converter()
    elif end == 2:
        calculator()