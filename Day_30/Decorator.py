# Decorator = A function that extend the behavior of another function
#             w/o modifying the base function 
#             Pass the base function as an argument to the decorator

#               @add_sprinkles
#               get_ice_cream("Vanilla")
# Decorator is a function that take another function as argument and returns a function


# *****************************************************************

def decorator(func):
    def wrapper():
        print("Payment Iniated")
        func()
        print("Payment Completed")
    return wrapper

def hello():
    print("Executing all steps of Transaction.....")

h1 = decorator(hello)
# h1()

# *****************************************************************

def decorator(func):
    def wrapper():
        print("Payment Iniated")
        func()
        print("Payment Completed")
    return wrapper

@decorator
def hello():
    print("Executing all steps of Transaction.....")

# hello()



# *****************************************************************

def add_sprinkles(func):
    def wrapper():
        print("*You add sprinkles 🎊*")
        func()
    return wrapper

def add_fudge(func):
    def wrapper():
        print("You add fudge 🍫")
        func()
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream():
    print("Here is your ice cream 🍦")

# get_ice_cream()


# *****************************************************************


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🎊*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge 🍫")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")

# get_ice_cream("Vanilla")



