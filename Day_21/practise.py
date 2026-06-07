# Pyhon Banking Program
# 1.Show Balance
# 2. Deposit
# 3. Withdraw


# def show_balance(balance):
#     print("***********************************")
#     print(f"Your balance is ${balance:.2f}")
#     print("***********************************")


# def deposit():
#     print("***********************************")
#     amount = float(input("Enter an amount to be deposit: "))
#     print("***********************************")

#     if amount < 0:
#         print("***********************************")
#         print("That's not a valid amount")
#         print("***********************************")
#         return 0
#     else:
#         return amount


# def withdraw(balance):
#     print("***********************************")
#     amount = float(input("Enter an amount to be withdraw: "))
#     print("***********************************")


#     if amount > balance:
#         print("***********************************")
#         print("Insufficient funds")
#         print("***********************************")
#         return 0
#     elif amount < 0:
#         print("***********************************")
#         print("Amount must be greater than 0")
#         print("***********************************")
#         return 0
#     else:
#         return amount
    


# def main():
#     balance = 0
#     is_running = True


#     while is_running:
#         print("***********************************")
#         print("Banking Program")
#         print("***********************************")
#         print("1. Show Balance")
#         print("***********************************")
#         print("2. Deposit")
#         print("***********************************")
#         print("3. Withdraw")
#         print("***********************************")
#         print("4. Exit")
#         print("***********************************")

#         choice = input("Enter your choice (1 - 4): ")

#         if choice == "1":
#             show_balance(balance)
#         elif choice == "2":
#             balance += deposit()
#         elif choice == "3":
#             balance -= withdraw(balance)
#         elif choice == "4":
#             is_running = False
#         else:
#             print("***********************************")
#             print("That is not valid choice")
#             print("***********************************")

#     print("***********************************")
#     print("Thank you! have a nice day")
#     print("***********************************")


# if __name__ == "__main__":
#     main()





# Q. Python Slot MAchine

import random

def spin_row():
    symbols = ["🍒", "🍉", "🥭", "🔔", "⭐"]

    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🥭":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 10
    return 0
        


    

def main():
    balance = 100

    print("***********************")
    print("Welcome to python slots")
    print("***********************")
    print("Symbols: 🍒 🍉🥭 🔔 ⭐ ")
    print("***********************")


    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Please your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient fund")
            continue


        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet


        row = spin_row()
        # print(row)
        print("spinning...\n")
        print_row(row)


        payout = get_payout(row, bet)


        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout


        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != "Y":
            break

    print(f"Game over! Your final balance is ${balance}")    

if __name__  == "__main__":
    main()