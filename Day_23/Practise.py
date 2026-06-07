# Q.  Write a recursive function to return the sum from 1 to n.

def sum(n):
    if n == 0:
        return 0
    return sum(n-1) + n

print(sum(5))



# Q. Reverse a string using recursion.

def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]
    
print(reverse_string("hello"))



# Q. Factorial Compute n!

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n-1) * n

print(factorial(5))



# Q. Check Palindrome

def is_palindrome(s):
    if len(s) <= 1:                 # 👉 If 1 or 0 letters → automatically palindrome
        return True
    if s[0] != s[-1]:               # 👉 First and last not same → NOT palindrome
        return False
    return is_palindrome(s[1:-1])   # 👉 Remove first and last, repeat again

print(is_palindrome("madam"))




# 

a = 1

def test():
    a = 2
    def inner():
        a = 3
        print(a)
    inner()
    print(a)

test()
print(a)