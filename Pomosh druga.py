import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 100
        self.progress = 0
        self.alive = True
        self.money = 100

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 2
        self.money -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 2

    def to_chill(self):
        print("Rest time")
        self.gladness += 4
        self.progress -= 0.1
        self.money -= 5

    def to_work(self):
        print("Time to work")
        self.progress -= 0.1
        self.gladness -= 2
        self.money += 15

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
        elif self.money < 1:
            print("Ran out of money")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress ={round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        self
        day = " Day " + str(day) + " of " + self.name + " life "
        print(f"{day:=^50}")
        if self.money <= 20:
            self.to_work()
            self.end_of_day()
            self.is_alive()

        elif self.progress <= 1:
            self.to_study()
            self.end_of_day()
            self.is_alive()

        else :
            live_cube = random.randint(1, 4)
            if live_cube == 1:
                self.to_study()
                self.end_of_day()
                self.is_alive()
            elif live_cube == 2:
                self.to_sleep()
                self.end_of_day()
                self.is_alive()
            elif live_cube == 3:
                self.to_chill()
                self.end_of_day()
                self.is_alive()
            elif live_cube == 4:
                self.to_work()
                self.end_of_day()
                self.is_alive()

nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)