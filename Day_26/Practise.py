# Q. Create a class Student with name and marks. Add a method to display details.also Add a method to check if the student passed (marks ≥ 40)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):      # <-- method defined here
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

    def check_pass(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

student1 = Student("John", 87)
student2 = Student("Ron", 87)

# student1.display()
# student1.check_pass()
# student2.display()


# # Q. 2. Simple Calculator Class

class Calculator:
    def add(self,a, b):
        return a + b
    
    def substraction(self, a, b):
        return a - b
    
    def multiple(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a/b
    
calc = Calculator()
# print(calc.add(5,8))
# print(calc.substraction(8,4))
# print(calc.multiple(4,5))
# print(calc.divide(8,2))



# # Q. 3. Bank Account (Important Practice)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Balance: {self.balance}")

# acc = BankAccount(1234)
# acc.deposit(1000)
# acc.show_balance()





# Q

class Account:

    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance
        

    def credit(self, amount):
        self.balance += amount
        print(f"Your credit {amount}")
        print(f"Your total {self.show_balance()}")

    def debit(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"You debit {amount}")
            print(f"Your total balance is {self.show_balance()}")
        else:
            print(f"Insufficient balance")

    def show_balance(self):
        return self.balance

acc = Account(12345, 100000)
# print(f"Your account no. is {acc.balance}")
# print(f"Your balance is {acc.balance}")

# acc.credit(500)
# acc.debit(100000)




#Q. Create a class Rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Your length is {self.length}")
        print(f"Your breadth is {self.width}")
        print(f"Area of Rectangle: {self.length * self.width}")


rectangle = Rectangle(5,5)
# rectangle.area()




# Q. Employee Salary

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        increase_salary = self.salary * (percent / 100)
        self.salary += increase_salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

emp1 = Employee("John", 5000)

emp1.increase_salary(10)

# emp1.display()




# Q. Create a class called Rectangle. Add a method to calculate Area, Perimeter, display a detail.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def display(self):
        print(f"Your length is {self.length}")
        print(f"Your width is {self.width}")
        print(f"Area of Rectangle: {self.area()}")
        print(f"Area of perimeter: {self.perimeter()}")

r1 = Rectangle(5,5)
# r1.display()




# Q. Problem: Person → Student (Inheritance + Extra Method)
# Requirements:
# Create a base class Person:
# Attributes: name, age
# Method: display() → prints name and age
# Create a derived class Student (inherits from Person):
# Additional attribute: marks
# Method: display() → prints name, age, and marks
# Method: grade():
# marks ≥ 80 → "A"
# marks ≥ 50 → "B"
# else → "C"



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

    def grade(self):
        if self.marks >= 80:
            print(f"Your grade is A")
        elif self.marks >= 50:
            print(f"Your grade is B")
        else:
            print("Your is C" )

s1 = Student("Aman", 19, 72)
# s1.display()
# s1.grade()





# Q. Problem: Bank Account System (Inheritance)
# Requirements:
# Create a base class BankAccount:
# Attributes: account_number, balance
# Methods:
# deposit(amount) → add money
# withdraw(amount) → subtract money (if enough balance)
# display() → show account details
# Create a derived class SavingsAccount:
# Additional attribute: interest_rate
# Method:
# add_interest() → add interest to balance



class BankAccount():
    def __init__(self, account_no, balance):
        self.acc = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"Withdraw: {amount}")
        else:
            print(f"Insufficient balance")

    def display(self):
        print("Account detail are :-")
        print(f"Account Number: {self.acc}")
        print(f"Balance: {self.balance}")

class SavingAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate/100
        self.balance += interest
        print(f"Interest Added: {interest}")


acc1 = SavingAccount("12345", 50000, 5)
# acc1.deposit(5000)
# acc1.withdraw(300)
# acc1.add_interest()
# acc1.display()


# Q. Problem: Multiple Inheritance (Student + Sports)
# Requirements:
# Create class Student:
# Attributes: name, marks
# Method: display_student()
# Create class Sports:
# Attribute: sports_marks
# Method: display_sports()
# Create class Result (inherits from both Student and Sports):
# Method: total() → returns total marks
# Method: display_result() → shows all details + total


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_student(self):
        print(f"Name: {self.name}")
        print(f"marks: {self.marks}")

class Sports:
    def __init__(self, sport_marks):
        self.sport_marks = sport_marks

    def display_sports(self):
        print(f"Sport_marks: {self.sport_marks}")

class Result(Student, Sports):
    def __init__(self, name, marks, sport_marks):
        Student.__init__(self, name, marks)
        Sports.__init__(self, sport_marks)

    def total(self):
        return self.marks + self.sport_marks
    
    def display_result(self):
        self.display_student()
        self.display_sports()
        print(f"Total marks: {self.total()}")


r1 = Result("Ron",82, 16)
# r1.display_result()





# Q. Problem: Abstract Class (Shape)
# Requirements:
# Create an abstract class Shape:
# Method: area() (no implementation)
# Create two derived classes:
# Rectangle
# Circle
# Each class should:
# Take required inputs (length & width / radius)
# Implement the area() method

from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# Example usage
r = Rectangle(5, 3)
c = Circle(4)

print("Rectangle Area:", r.area())
print("Circle Area:", c.area())