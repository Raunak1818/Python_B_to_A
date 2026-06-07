# # Python number guessing game

# import random

# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True

# print("python number gurssing game")
# print(f"select a number between {lowest_num} and {highest_num}")


# while is_running:
#     guess = input("Enter your guess: ")

#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1

#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"please select a number between {lowest_num} and {highest_num}")
#         elif guess < answer:
#             print("Too low! Try again")
#         elif guess > answer:
#             print("Too high! Try again")
#         else:
#             print(f"Correct! The answer was  {answer}")
#             print(f"number of guesses: {guesses}")
#             is_running = False

#     else:
#         print("Invalid guess")
#         print(f"Please select a number between {lowest_num} and {highest_num}")






# # Q2

# import random

# lowest_number = 1
# highest_number = 100
# answer = random.randint(lowest_number,highest_number)
# guesses = 0
# is_running = True

# while is_running:
#     guess = input("Entert your guess: ")

#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1

#         if guess < lowest_number or guess > highest_number:
#             print("THe value is out of range:")
#             print(f"Pls Enter the value b/w {lowest_number} to {highest_number}")
#         elif guess < answer:
#             print("Too low! Pls Try again")
#         elif guess > answer:
#             print("Too high! Pls Try again")

#         else:
#             print(f"Correct! The answer was {answer}")
#             print(f"No. of guesses: {guesses}")
#             is_running = False


#     else:
#         print(f"Pls Enter the value b/w {lowest_number} to {highest_number}")




# Q3  

import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"computer: {computer}")


    if player == computer:
        print("Its a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!") 

    # if not input("Play again? (y/n): ") == "y":
    #     running = False


    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        running = False

print("Thanks for playing")