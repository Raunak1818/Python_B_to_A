# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set   ={} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = ()ordered and unchangeable. Duplicates OK. FASTER

# ***************  List ******************

# fruits = ["apple", "orange", "banana", "coconut"]

# print(fruits)
# print(fruits[3])
# print(fruits[0:3])
# print(fruits[::2])
# print(fruits[::-1])


# for x in fruits:
#     print(x)


# for fruit in fruits:
    # print(fruit)



# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))

# print("pineapple" in fruits)

# fruits[1] = "pineapple"

# for fruit in fruits:
#     print(fruit)


# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()

# print(fruits.index("apple"))
# print(fruits.count("banana"))


# for fruit in fruits:
#     print(fruit)


# print(fruits)






# ***************  Set ******************

# fruits = {"apple", "orange", "banana", "coconut"}

# print(fruits)

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()

# print(fruits)


# ****************** Tuple ********************

fruits = ("apple", "orange", "banana", "coconut",  "coconut")

# print(fruits)


# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
print("pineapple" in fruits)

print(fruits.index("apple"))
print(fruits.count("coconut"))

# print(fruits)

# for fruit in fruits:
#     print(fruit)