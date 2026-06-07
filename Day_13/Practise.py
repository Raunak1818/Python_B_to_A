# Q1    Print a 2D list

# matrix = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]

# for row in matrix:
#     # print(row)
#     for num in row:
#         print(num, end=" ")
#     print()



# Q2    Print row sums


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# for row in matrix:
#     # print(row)
#     total = 0
#     for num in row:
#         # print(num)
#         total+= num
#     print(total)




# Q3    Count total numbers

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# total = 0

# for row in matrix:
#     # print(row)
#     for num in row:
#         # print(num, end=" ")
#         total += num
#     print(total)






# Q4


# questions = (
#     "What is the capital of India?: ",
#     "Which keyword is used to define a function in Python?: ",
#     "Which data type is used to store True/False?: ",
#     "Which symbol is used for comments in Python?: "
#     )

# options = (
#     ("A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"),
#     ("A. func", "B. define", "C. def", "D. function"),
#     ("A. int", "B. str", "C. bool", "D. float"),
#     ("A. //", "B. <!-- -->", "C. #", "D. **")
#     )

# answers = ("B", "C", "C", "C")

# guesses = []

# score = 0

# questions_num = 0


# for question in questions:
#     print("----------------------")
#     print(question)
#     for option in options[questions_num]:
#         print(option)
#     guess = input("Enter (A, B, C , D)?: ").upper()
#     guesses.append(guess)
#     if guess == answers[questions_num]:
#         score += 1
#         print("CORRECT")
#     else:
#         print("INCORRECT")
#         print(f"{answers[questions_num]} is correct")
#     questions_num += 1


# print("-------------------")
# print("     RESULT      ")
# print("-------------------")

# print("guesses: ", end="")
# for guess in guesses:
#     print(guess, end=" ")
# print()
# print("answers: ", end="")
# for answer in answers:
#     print(answer, end=" ")
# print()

# score_percentage = score / len(questions) * 100

# print(f"Your score is {score_percentage}%")





# Q5



questions = (
    "Who is known as the Missile Man of India?: ",
    "Which is the national animal of India?: ",
    "Who is the CEO of Google?: ",
    "Which planet is known as the Red Planet?: "
)

options = (
    ("A. Narendra Modi", "B. A. P. J. Abdul Kalam", "C. C. V. Raman", "D. Homi J. Bhabha"),
    ("A. Lion", "B. Elephant", "C. Tiger", "D. Leopard"),
    ("A. Elon Musk", "B. Sundar Pichai", "C. Bill Gates", "D. Mark Zuckerberg"),
    ("A. Earth", "B. Venus", "C. Jupiter", "D. Mars")
)

answers = ("B", "C", "B", "D")

guesses = []

score = 0

questions_num = 0


for question in questions:
    print("---------------")
    print(question)
    for option in options[questions_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    while guess not in ("A", "B", "C", "D"):
        print("Invalid input! Please enter A, B, C, or D.")
        guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[questions_num]} is correct")
    questions_num += 1


print("--------------------")
print("     ANSWER      ")
print("--------------------")

print("guesses: ",end="")
for guess in guesses:
    print(guess, end=" ")
print()
print("answer: ",end="")
for answer in answers:
    print(answer, end=" ")
print()

score = score / len(questions) * 100

print(f"Your score is {score}%")