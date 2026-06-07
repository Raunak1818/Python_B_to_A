# Iterables =  An object/collection that can return its element one at a time,
#               allowing it to be iterated over in a loop

numbers = [1,2,3,4,5]

# for number in numbers:
#     print(number)

for number in reversed(numbers):
    print(number, end="-")
