import random

brands_of_car = {
 "BMW":{"fuel": 100, "strength": 100, "consumption": 6},
 "Lada":{"fuel": 50, "strength": 40, "consumption": 10},
 "Volvo":{"fuel": 70, "strength": 150, "consumption": 8},
 "Ferrari":{"fuel": 80, "strength": 120, "consumption": 14},
 }


job_list = {
"Java developer": {"salary": 50, "gladness_less": 10 },
"Python developer": {"salary": 40, "gladness_less": 3 },
"C++ developer": {"salary": 45, "gladness_less": 25 },
"Rust developer": {"salary": 70, "gladness_less": 1 },
}

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, cat=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.cat = cat


    def get_cat(self):
        self.cat = Cat()

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def play_cat(self):
        self.gladness += 20
        self.home.mess += 5
        self.cat.cat_satiety -= 5

    def feed_cat(self):
        if self.home.cat_food <= 0:
            self.shopping("food")
        else:
            if self.cat.cat_satiety >= 100:
                self.cat.cat_satiety = 100
                return
            self.cat.cat_satiety += 20
            self.home.cat_food -= 20

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
            self.cat.cat_satiety -= 2

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
        self.cat.cat_satiety -= 6

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
            self.home.cat_food +=50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15
        self.cat.cat_satiety -= 4

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        self.cat.cat_satiety -= 2

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
        self.cat.cat_satiety -= 2

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
        self.cat.cat_satiety -= 2

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name} 's life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money = {self.money}")
        print(f"Satiety = {self.satiety}")
        print(f"Gladness = {self.gladness}")
        cat_indexes = self.cat.name + "'s indexes"
        print(f"{cat_indexes:^50}", "\n")
        print(f"Satiety = {self.cat.cat_satiety}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food = {self.home.food}")
        print(f"Food for cat = {self.home.cat_food}")
        print(f"Mess = {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel = {self.car.fuel}")
        print(f"Strength = {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False
        if self.cat.cat_satiety < 0:
            print("Cat dead, depression…")
            return False



    def live(self, day):
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.cat is None:
            self.get_cat()
            print(f"I get cat {self.cat.name}")
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job {self.job.job} with salary {self.job.salary}")
        if self.is_alive() == False:
            return False

        self.days_indexes(day)

        dice = random.randint(1, 5)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.cat.cat_satiety < 20:
            print("I'll go feed cat")
            self.feed_cat()
        elif self.gladness < 20:
            dice = random.randint(1,2)
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…\nSo I will clean the house ")
                self.clean_home()
            elif dice == 1:
                print("Let`s chill!")
                self.chill()
            elif dice == 2:
                print("Let`s play with cat")
                self.play_cat()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")
        elif dice == 5:
            print("Let`s play with cat")
            self.play_cat()







class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list (brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
        self.cat_food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job] ["salary"]
        self.gladness_less = job_list[self.job] ["gladness_less"]

class Cat:
    def __init__(self, name = "Cat"):
        self.name = name
        self.cat_satiety = 50






nick = Human(name = "Nick")
for day in range(1, 365):
    if nick.live(day) == False:
        break