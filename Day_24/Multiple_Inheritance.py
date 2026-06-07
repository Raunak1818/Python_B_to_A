# Multiple Inheritance = Inherit from more than one parent class
#                          C(A, B)

# Multilevel inhritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

# e.g.- Animal -> grandparents, Prey & Predator -> parents, Rabbit, Hawk, Fish -> child

class Animal:

    def __init__(self, name):
        self.name = name


    def eat(self):
        print(f" {self.name} is eating")

    def sleep(self):
        print(f" {self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f" {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f" {self.name} is hunting")


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")


# rabbit.flee()
# hawk.hunt()
# fish.flee()

# rabbit.sleep()
# rabbit.eat()


rabbit.eat()
hawk.hunt()
fish.sleep()