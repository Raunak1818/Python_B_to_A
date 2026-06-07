# List comprehensive = A concise way to create lists in python
#                       compact and easier to read than traditional loops
#                       [expression for value in iterable if condition]



# double = []

# for x in range(1,11):
#     double.append(x*2)

# print(double)

# doubles = [expression for value in iterable if condition]
#           [x * 2 for x in range(1,11)]

# double = [x * 2 for x in range(1,11)]
# print(double)

# triple = [y * 3 for y in range(1,11)]
# print(triple)

# square = [z * z for z in range(1,11)]
# print(square)

# fruits = ["apple", "banana", "orange","coconut"]

# fruits = [fruit.upper() for fruit in fruits]
# fruits_charts = [fruit[0] for fruit in fruits]
# print(fruits)
# print(fruits_charts)




# fruits = [fruit.upper() for fruit in ["apple", "banana", "orange","coconut"]]
# print(fruits)




# numbers = [1,2,-2,-3,-4,-5,-6]
# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num <= 0]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 != 0]


# print(positive_nums)
# print(negative_nums)
# print(even_nums)
# print(odd_nums)


grades = [45,42,89,85,53,75,31]
passing_grades = [grade for grade in grades if grade >=60]

print(passing_grades)