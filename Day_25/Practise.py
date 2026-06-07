# Q. Create Account class with 2 attributes - balance and account no. Create method for debit, credit and printing the balace.

class Account():
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} was debited")
        print(f"total balance = {self.get_balance()}")

    # credit method
    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} was credited")
        print(f"total balance = {self.get_balance()}")


    # final value
    def get_balance(self):
        return self.balance


acc1 = Account(1000, 12345)
# print(acc1.balance)
# print(acc1.account_no)

acc1.debit(1000)
acc1.credit(500)
acc1.credit(4000)
acc1.debit(2000)