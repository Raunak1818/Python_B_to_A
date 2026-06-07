# Static Method = Method that don't use the self parameter (work at class level)

class Student:

    @staticmethod #decorator
    def hello():
        print("Hello")

s1 = Student()
s1.hello()

# Decorator allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanentaly modyfying it.
# It changing the behaviour of normal function