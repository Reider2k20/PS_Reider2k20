class Dad:
    height = 180
    eyes = "Brown"
    hair_color = "Black"
    peculiarities = "Big eyes"

class Mum:
    height = 160
    eyes = "Blue"
    hair_color = "Brown"
    ability = "flexibility"

class Son(Dad, Mum):
    pass

Dima = Son()

print(f"Height: {Dima.height}")
print(f"Eyes: {Dima.eyes}")
print(f"Hair_color: {Dima.hair_color}")
print(f"Peculiarities: {Dima.peculiarities}")
print(f"Ability: {Dima.ability}")