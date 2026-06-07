# Exception = An event that interrupts the flow of a program
#              (ZeroDivisionError, TypeError, ValueError)
#               1. try, 2.except, 3.finally

# 1/0 = ZeroDivisionError
# 1 +"1" = TypeError
# int("pizza") = ValueError

# try:
#     # Try some code
# except Exception:
#     # Handle an Exception
# finally:
#     # Do some clean up


# **********************************************************
try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by Zero IDIOT!")
except ValueError:
    print("Enter only numbers pls!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here!")