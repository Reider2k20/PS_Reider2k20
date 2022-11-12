result = 1
def raise_to_degrees(number):
    i = 0
    while True:
        result = number**i
        if result > 100**20:
            break
        i += 1



res = raise_to_degrees(5)
print(res)
for _ in res:
    print(_)
    print("---------")
