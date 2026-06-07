# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrot", "potatoes"]
# meats = ["chicken", "mutton", "fish"]


# groceries = [fruits, vegetables, meats]

# print(groceries[1][1])





# groceries = [["apple", "orange", "banana", "coconut"],
#              ["celery", "carrot", "potatoes"],
#              ["chicken", "mutton", "fish"]]

# # print(groceries[1][1])

# for collection in groceries:
#     # print(collection)
#     for food in collection:
#         print(food, end=" ")
#     print()




    # ******** 2 D keypad ***************

num_pad = ((1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
             ("*", 0, "#"))
    
for row in num_pad:
    # print(row)
    for num in row:
        print(num, end=" ")
    print()