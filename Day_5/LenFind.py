# name = input("Enter the full name: ")

# result = len(name)
# result = name.find(" ")
# result = name.find("u")
# result = name.rfind("a")

# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# name = name.isdigit()
# name = name.isalpha()

# print(result)
# print(name)


# phone_number = input("Enter your phone number #: ")

# # result = phone_number.count("-")
# result = phone_number.replace("-", " ")
# # result = phone_number.replace("-", "")

# print(result)




# practise

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")



if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("your username can't contain number")
else:
    print(f"Welcome {username}")