# Membership Operators = used to test whether a value or variable is found in a sequence
#                         (string, list, set, or dictionary)
#                       1. in
#                       2. not in


# word = "APPLE"

# letter = input("Guess a letter in a the secret word: ").upper()

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")




# grades = {"Sandy": "A",
#           "Sumit": "B",
#           "Sue": "C",
#           "Saurav":"D"}

# student = input("Enter the student name: ").capitalize()

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} not found")



# email = "raunakjais@gmail.com"
email = input("Enter the email id: ")

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")