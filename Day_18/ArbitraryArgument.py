# Arbitrary(*args)   = allow you to pass multiple non - key arguments
# ** kwargs         = allow you to pass multiple keyboard -argument
#                      * unpacking operator


# def add(*args):
#     print(type(args))

# add(1,2,3)


# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total


# print(add(1,2,3))


# def display_name(*args):
#     for arg in args:
#         print(arg, end = " ")

# display_name("Dr.", "Spongebob","Harold", "Squarepants", "III")






# def print_address(**kwargs):
#     print(type(kwargs))


# print_address(Street ="123 Fake St.", 
#               city = "Detroit", 
#               State = "MI", 
#               Zip = "54321")




# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value)


# print_address(Street ="123 Fake St.", 
#               city = "Detroit", 
#               State = "MI", 
#               Zip = "54321")



# def print_address(**kwargs):
#     for key in kwargs.keys():
#         print(key)


# print_address(Street ="123 Fake St.", 
#               city = "Detroit", 
#               State = "MI", 
#               Zip = "54321")



# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")


# print_address(Street ="123 Fake St.", 
#               city = "Detroit", 
#               State = "MI", 
#               Zip = "54321")






# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     # for key , value in kwargs.items():
#         # print(f"{key} : {value}")
#     print(f"{kwargs.get('Street')}")
#     print(f"{kwargs.get('city')}, {kwargs.get('State')}, {kwargs.get('Zip')}")


# shipping_label("Dr.", "Spongebob","Harold", "Squarepants", "III",
#                Street ="123 Fake St.", 
#                city = "Detroit",
#                State = "MI",
#                Zip = "54321")





def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('Street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('Street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('State')}, {kwargs.get('Zip')}")


shipping_label("Dr.", "Spongebob","Harold", "Squarepants", "III",
               Street ="123 Fake St.", 
               city = "Detroit",
               State = "MI",
               Zip = "54321")
