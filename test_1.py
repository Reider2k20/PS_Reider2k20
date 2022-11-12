import inspect

a = int
b = str
c = float

d = tuple([1, 2, 5])

a1 = inspect.ClassFoundException(a)
print(a1)

print(inspect.ClassFoundException(a))
print(inspect.ClassFoundException(b))
print(inspect.ClassFoundException(c))

print(len(d))