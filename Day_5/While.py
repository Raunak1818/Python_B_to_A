# While loop = execute some code WHILE some condition remain true 


# name = input("Enter your name: ")


# while name == "":
#     print("you did not enter your name")
#     name = input("Enter your name: ")


#     print(f"Hello {name}")



# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"Your are {age} years old.")



# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"you like {food}")
#     food = input("Enter a food you like (q to quit):")

# print("Bye")  


num = int(input("ENter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("ENter a # between 1 - 10: "))

print(f"Your number is {num}")