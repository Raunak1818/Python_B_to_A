# Inheritance = Allow a class to inheritance attribute and method from another class
#               Help with reusability and extensibility
#               Class Child(Parent)


class Animal():

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass


dog = Dog("Sheru")
cat = Cat("Garfield")
mouse = Mouse("Mice")


print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

# ********************


class Animal():

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def speak(self):
        print("Squeek!")


dog = Dog("Sheru")
cat = Cat("Garfield")
mouse = Mouse("Mice")


# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()


dog.speak()
cat.speak()