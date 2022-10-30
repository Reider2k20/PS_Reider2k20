class Human:
    height = 170

class Student(Human):
    pass

class Worker(Human):
    pass


Vasya = Student()
Dima = Worker()

print(Vasya.height)
print(Dima.height)