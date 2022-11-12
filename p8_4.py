def addef(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs:
        result