# Q1.  Write a function to print the length of a list. (list is the parameter)


# cities = ["delhi", "noida", "gurgaon", "pune", "hajipur", "patna"]

# heroes = ["thor","ironman","shaktiman"]

# # def print_len(list):
# #     return len(list)
    
# # print(print_len(cities))


# def print_len(list):
#     print(len(list))

# print_len(cities)

# print_len(heroes)



# Q 2. WAF tp print the element of al list in a single line. (list is the parameter)

# cities = ["delhi", "noida", "gurgaon", "pune", "hajipur", "patna"]

# heroes = ["thor","ironman","shaktiman"]

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(heroes)
# print()
# print_list(cities)


# Q 3. WAF to find the factorial of n.n is the parameter)

# n = 5
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print(factorial)

# def cal_fact(n):
#     factorial = 1
#     for i in range(1, n+1):
#         factorial *= i
#     print(factorial)

# cal_fact(3)


# Q 4. WAF to convert USD to INR

# def converter(usd_val):
#     inr_val = usd_val * 94
#     print(f"{usd_val} USD = {inr_val} INR ")


# converter(56)


# Q5. WAF to check even or odd

# def check(number):
#     if number % 2 == 0:
#         print(f"{number} is EVEN")
#     else:
#         print(f"{number} is ODD")

# check(4)



# Q. Write a function say_hello() that prints "Hello, Python!"

def say_hello():
    print("HEllo, Python")

say_hello()



# Q. Write a function add(a, b) that returns the sum of two numbers.

def add_nums(a,b):
    c = a + b
    return c

print(add_nums(2,3))



# Q. Write a function find_max(a, b) that returns the larger of two numbers.

def max_nums(a,b):
    larger_num = max(a,b)
    return larger_num

print(max_nums(6,3))




# Q. Write a function factorial(n) that returns the factorial of a number.

def calc_num(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    print(factorial)

calc_num(5)




# Q. Write a function sum_list(numbers) that returns the sum of all elements in a list.

def sum_list(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    print(sum)

sum_list(3)


# Q. Write a function is_palindrome(word) that checks if a word is the same forwards and backwards.

def check_palindrome(word):
    if word == word[::-1]:
        print(f"{word} is Palindrome") 
    else:
        print(f"{word} is not Palindrome") 

check_palindrome("level")


# Q. Create a function calculator(a, b, operation) where operation can be "add", "sub", "mul", "div".

def calculator(a, b, operation):
    if operation == "sum":
        return a + b
    elif operation == "substraction":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return ("can not divided by Zero")
        return a/b
    else:
        return(f"{operation} not valid operation")

print(calculator(1,0,"divide"))




# Q. Write a function sum_all(*args) that returns the sum of all numbers passed.

def sum_all(*args):
    sum = 0
    for arg in args:
        sum += arg
    # print(sum)
    return sum

print(sum_all(1,2,3))





# Q. Write a function find_max(*args) that returns the largest number.

def find_max(*args):
    max_nums = max(args)
    return max_nums

print(find_max(12,3,4))




# Q. Write a function count_even(*args) that counts how many even numbers are passed.

def count_even(*args):
    count = 0
    for num in args:
        if num % 2 == 0:
            count += 1
    return count

print(count_even(1,2,3,4,5,6,7,8,9,10))



# Q. Write a function multiply_all(*args) that returns the product of all numbers.

def multiply_all(*args):
    multiply = 1
    for num in args:
        multiply *= num
    return multiply

print(multiply_all(2,3))



# Q. Write a function print_info(**kwargs) that prints all key-value pairs.

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}", end=" ")

print_info(Name = "Rohan", Age = "20" )