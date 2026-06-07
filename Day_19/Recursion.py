# Recursion =   When a function calls itself repeatedly.

# def show(n):
#     if n == 0:
#         return
#     print(n)
#     show(n-1)

# show(5)




# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return factorial(n-1) * n

# print(factorial(2))





# Q 1. Write a ecursive function to calculate the sum of first n natural numbers.

def cal_sum(n):
    if n == 0:
        return 0
    return cal_sum(n-1) + n

print(cal_sum(5))




# Q 2. Write a recursive function to print all element in a list. Hint - use list & index as parameters.


def print_element(list,index=0):
    if(index == len(list)):
        return
    print(list[index])
    print_element(list,index+1)

cities = ["delhi", "noida", "gurgaon", "pune", "hajipur", "patna"]

print(print_element(cities))