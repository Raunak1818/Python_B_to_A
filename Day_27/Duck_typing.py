# Duck typing = ANother way to achieve polymorphismbeside Inheritance
#               Object must have the minimum attributes/methods
#               "If it look like a duck and quacks like a duck, it must be a duck"


class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car:

    alive = False
    
    def speak(self):
        print("HONK")


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print((animal.alive))