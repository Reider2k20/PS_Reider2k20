class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self, work):
        return f"i will help you with your {self.work}. After i will help you with {work}"


helper = Helper("homework")
print(helper("cleaning"))

