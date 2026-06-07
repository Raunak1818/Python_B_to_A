# Class method = Allow operatio to the class itself
#                Take (cls) as the first parameter, which represent the class itself

# Best for class-level data or require access to the class itself 

class Student:

    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    # Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
student1 = Student("Spongebob", 3.5)
student2 = Student("Ron",2.1)
student3 = Student("Sandy", 4.0)

# print(Student.get_count())






class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa : {cls.total_gpa / cls.count:.2f}"
    
student1 = Student("Spongebob", 3.5)
student2 = Student("Ron",2.1)
student3 = Student("Sandy", 4.0)

print(Student.get_count())
print(Student.get_average_gpa())