# Object = A "bundle" of related attributes(variable) and method (function)
#          Ex. phone, cup, book
#          You need a "clase" to create many objects

# class = (blueprint) used to design the structure and layout of an object

# class Car:
#     def __init__(self, model, year, colour, for_sale):         #dunder (double underscore) method
#         self.model = model
#         self.year = year
#         self.colour = colour
#         self.for_sale = for_sale

from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Ferrari", 2025, "blue", True)
car3 = Car("charger", 2026, "yellow", True)

# print(car3.model)
# print(car3.year)
# print(car3.colour)
# print(car3.for_sale )


# Method are the action that are object can perform
# Method are function that belong to an object, they define what this object can do.

car2.drive()

car1.stop()

car1.describe()