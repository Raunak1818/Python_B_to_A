# Encapsulation Questions:- 
# Q. Create a class Laptop with a private variable __price. Add methods to - set price, get price

class Laptop:
    def __init__(self):
        self._price = 0   #private variable

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price
    
laptop1= Laptop()

laptop1.set_price(50000)

# print(f"Laptop Price: {laptop1.get_price()}")





# Q. Create a class ATM where balance cannot be accessed directly.

class ATM:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount
        print(f"{amount} deposit successfully")

    def withdraw(self, amount):
        if self._balance > amount:
            self._balance -= amount
            print(f"{amount} withdraw succesfully")
        else:
            print("Insufficient amount")

    def check_balance(self):
        return self._balance
    
a1 = ATM()

# a1.deposit(50000)
# a1.withdraw(10000)
# print(f"Available balance: {a1.check_balance()}")





# Abstraction Questions
# Q. Create an abstract class Shape with abstract method area().

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2
    
Shapes = [Circle(5), Triangle(2,4)]

# for shape in Shapes:
#     print(f"{shape.area()}cm²")





# Create abstract class Payment with method pay().
# Implement: CreditCardPayment, UPIPayment

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class CredirtCardPayment(Payment):
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print(f"Paid {self.amount} using credit card") 


class UPIPayment(Payment):
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print(f"Paid {self.amount} using UPI Payment")


Payments = [CredirtCardPayment(5000), UPIPayment(2000)]

# for payment in Payments:
    # payment.pay()






# Build a Library Management System using classes.

class Book:
    def __init__(self, book_id, author, title):
        self.book_id = book_id
        self.author = author
        self.title = title
        self.is_issued = False

    def display_book(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"ID: {self.book_id} | Title : {self.title} | Author : {self.author} | Status : {status}")

# b1 = Book(1234, 'johnson','The new day')
# b1.display_book()

class Library:
    def __init__(self):
        self.books = []

    # Add book
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully")

    # Show all books
    def show_book(self):
        if not self.books:
            print("No books available")
        else:
            for book in self.books:
                book.display_book()

    # Issue book
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    print(f"Book '{book.title}' issued successfully")
                else:
                    print("Book already issued")
                return
        print("Book not found")

    # return book
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    print(f"Book {book.title} returned successfully")
                else:
                    print("Book was not issued")
                return
        print("Book not found")



# library = Library()

# b1 = Book(1, "Python Basic", "John")
# b2 = Book(2, "Data Structures", "Smith")
# b3 = Book(3, "Machine Learning", "David")

# library.add_book(b1)
# library.add_book(b2)
# library.add_book(b3)

# print("\nAll Books:")
# library.show_book()

# print("\n Issuing Book ID 2")
# library.issue_book(2)

# print("\n Book after Issue")
# library.show_book()

# print("\n Returning Book ID 2")
# library.return_book(2)

# print("\nFinal Book List:")
# library.show_book()










# Q. Create a class Student that stores marks of 5 subjects and calculates: total, average , grade

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)
    
    def average(self):
        return self.total() / len(self.marks)
    
    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "Fail"


    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Total Marks: {self.total()}")
        print(f"Average : {self.average()}")
        print(f"Grade: {self.grade()}")



s1 = Student("Ron",[85,45,39,78,92])
s1.display()