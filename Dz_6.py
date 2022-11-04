result = []


def divider(a, b):
    if type(a) != int:
        if len(a) == 0:
            a = int(0)
        else:
            a = int(a)
    if type(b) != int:
        if len(b) == 0:
            b = int(0)
        else:
            b = int(b)

    if a < b:
        print(a, "<", b, "ValueError")
    if a > 100:
        print(a, "IndexError")
    if b > 100:
        print(b, "IndexError")

    print("")

    if b == 0:
        return str("∅")
    else:
        return int(a / b)

data = {10: 2, 2: 5, "123": 4, 18: 0, tuple([]): 15, 8 : 4}


for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)