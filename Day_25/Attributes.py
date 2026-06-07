# Attributes
# Class & Instance Attributes

# class.attr
# obj.attr

# class Student:

#     college_name = "ABC Public School"
#     name = "anonymous"  # class attr

#     def __init__(self, name, mark):
#         self.name = name        # object attr
#         self.mark = mark
#         print("adding new student in database..")

# s1 = Student("karan", 98)
# print(s1.name)
# print(s1.college_name)

# object attr > class attr




# Method


class Student:

    college_name = "ABC Public School"

    def __init__(self, name, mark):
        self.name = name     
        self.mark = mark
    
    def welcome(self):
        print(f"Welcome students, {self.name}")

    def get_marks(self):
        return self.mark

s1 = Student("karan", 98)
s1.welcome()
print(s1.get_marks())




# Creates student class that takes names and marks of 3 subjects as argument in constructor. Then create a method to print the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total = 0
        for value in self.marks:
            total += value
        avg = total/len(self.marks)
        print(f"Hi {self.name}, Your avg mark is {avg}")

s1 = Student("Tony Stark", [76,80,90])
s1.get_avg()


s1.name = "Ironman"
s1.get_avg()