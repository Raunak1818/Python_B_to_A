# dictionary    =   a collection of {key:value}pairs
#                   ordered and changeable. No duplicates




capitals = {"USA": "Washington D.c",
            "India" : "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"
            }

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))

# print(capitals.get("India"))


# if capitals.get("Japan"):
#     print("That capital exist")
# else:
#     print("That capital doesn't exit")


# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Detroit"})

# capitals.pop("China")

# capitals.popitem()

# capitals.clear()


# print(capitals)


# keys = capitals.keys()

# # print(keys)

# for key in capitals.keys():
#     print(key)


# values = capitals.values()

# for value in capitals.values():
#     print(value)


# items = capitals.items()

# print(items)

for key, value in capitals.items():
    print(f"{key} : {value}")