# Input = A function that prompts the user to enter DeprecationWarning
#         Returms the entered data as a string 

 
name = input("What is your name?: ")
age = input("How old are you? : ")

age = int(age)
age = age + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY")
print(f"Your are {age} years old.")