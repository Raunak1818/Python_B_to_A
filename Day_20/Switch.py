# Switch: An alternative to using many 'elif' statements
#         Execute some code if a value matches a 'case'
#         Benefitss: cleaner and syntax is more readable 

# Match case statement:

# def day_of_week(day):
#     if day == 1:
#         return "It is Sunday"
#     elif day == 2:
#         return "It is Monday"
#     elif day == 3:
#         return "It is Tuesday"
#     elif day == 4:
#         return "It is Wednesday"
#     elif day == 5:
#         return "It is Thrusday"
#     elif day == 6:
#         return "It is Friday"
#     elif day == 7:
#         return "It is Saturday"
#     else:
#         return "Enter the valid number"
    
# print(day_of_week(9))


# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is Sunday"
#         case 2:
#             return "It is Monday"
#         case 3:
#             return "It is Tuesday"
#         case 4:
#             return "It is Wednesday"
#         case 5:
#             return "It is Thrusday"
#         case 6:
#             return "It is Friday"
#         case 7:
#             return "It is Saturday"
#         case _:
#             return "Enter the valid number"
        
# print(day_of_week(4))




# def is_weekend(day):
#     match day:
#         case "Sunday":
#             return True
#         case "Monday":
#             return False 
#         case "Tuesday":
#             return False
#         case "Wednesday":
#             return False
#         case "Thrusday":
#             return False
#         case "Friday":
#             return False
#         case "Saturday":
#             return False
#         case _:
#             return False
        
# print(is_weekend("Monday"))




def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thrusday" | "Friday":
            return False 
        case _:
            return False
        
print(is_weekend("Monday"))