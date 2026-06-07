# Abstraction = Hiding the implementation detail of a class and only showing the essential features to the user.
# Means - hide the unnecessary thing only show the necessary thing

class Car:
    def __init__(self):
        self.acceleator = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acceleator = True
        print("car started")

car1 = Car()
car1.start()