class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []

    def addpassanger(self, human):
        self.passenger.append(human)

    def print_names_pasenger(self):
        if self.passenger != []:
            print(f"Names of {self.brand} passengers")
            for passenger in self.passenger:
                print(passenger.name)
        else:
            print(f"No passenger in {self.brand}")


hum1 = Human("Jack")
hum2 = Human("Lis")

auto1 = Auto("Mercedes")
auto2 = Auto("Tatra")

auto1.print_names_pasenger()
auto2.print_names_pasenger()

auto1.addpassanger(hum1)
auto2.addpassanger(hum2)

auto1.print_names_pasenger()
auto2.print_names_pasenger()