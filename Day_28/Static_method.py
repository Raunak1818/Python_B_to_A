# Static method = A method that belong to a class rather than any object from the class(instance)
#                 Usually used for general utility functions

# Instance methods = Best for operation on instance of the class(object)
# Static methods = Best for utility function that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(Employee.is_valid_position("Cook"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())