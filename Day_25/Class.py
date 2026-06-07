# Oops (object oriented programming )
# To map with real world scenarios we started using object in code this is call oops
# Procedural – sequence me kaam hona mtlb ek ke baad ek kaam hona
# Function – redundancy decrese karne ke liya aur reusability increase karne ke liye
# Oops – 
# (Object – anything is an object like pen, mouse), (class- class is basically a blueprint for creating object)
# Object banana se pahle hm class bnate h

# Four pillars of OOPS
# 1.Abstraction 2. Encapsulation    3. Inheritance  4. Polymosphism


# 	Inner box(Blue box) is object 
# 	Outer box is class


# __init__ Function
# Constructor – all class have function called __init__(), which is always executed when the object is being initiated. (ye object creation ke time invoke(execute) hota hai.







# class Student:

#     name = "karan"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)


# class Car:
#     colour = "blue"
#     brand = "mercedece"

# car = Car()
# print(car.colour)
# print(car.brand)



class Student:

    # Default constructor
    def __init__(self):
        pass

    # Parameterized constructor
    def __init__(self, name):   #Write inside the def is known as constructor
        self.name = name

s1 = Student("karan")
print(s1.name)

# The self parameter is a reference to the current instance of the class, and is used to acces variable that belong to the class.
# e.g self = s1 (we only give name to object(s1) )

s2 = Student("Arjun")
print(s2.name)


# "Self" ke help se (dwara) hm different different variable/ data store karte hai
# Jo v data hm object ke liya store karte h, jaise s1.name (s1 ke liya "name" store kiye) ya sabhi ke lye "name" store kiye use hm "attributes" kahte hai
# (The data/variable store inside the class or object is known as "attributes")