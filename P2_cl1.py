class Student:
    print("Hi1")
    def __init__(self, height=160):
        self.height = height
        print("I am alive!")


first_ek = Student()
print(first_ek.height)

second_ek = Student(height = 190)
print(second_ek.height)