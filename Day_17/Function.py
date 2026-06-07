# function = A block of reusable code
#             place () after name to invoke it

# def happy_birthday():
#     print("Happy birthday to you!")
#     print("Your are old!")
#     print("Happy birthday to you!")
#     print()

# happy_birthday()
# happy_birthday()
# happy_birthday()



# Parameter does matter e.g What are inside parenthesis like name,age in below 

# def happy_birthday(name, age):                 
#     print(f"Happy birthday to {name}")
#     print(f"Your are {age} year old!")
#     print("Happy birthday to you!")
#     print()

# happy_birthday("Bro", 20)
# happy_birthday("Steve", 21)
# happy_birthday("John", 22)





def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of Rs {amount:.2f} is due: {due_date}")

display_invoice("Joe", 42.50, "01/04/2025")