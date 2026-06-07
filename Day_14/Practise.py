# Concession stand program


menu = {"pizza":50.5,
        "burger":15.5,
        "momo":30,
        "chowmin":40,
        "roll":35
        }

cart =[]

total = 0

print("-------MENU------------")
print("----------------------------")
for key, value in menu.items():
    print(f"{key:10} : ₹ {value:.2f}")
print("----------------------------")

# while True:
#     food = input("Select an item (q to quit): ").lower()
#     if food == "q":
#         break 
#     elif menu .get(food) is not None:
#         cart.append(food)

# # print(cart)

# print("-------------YOUR ORDER------------")
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")

# print()
# print(f"Total is: Rs {total:.2f}")




# Q2


# menu = {"pizza":50.5,
#         "burger":15.5,
#         "momo":30,
#         "chowmin":40,
#         "roll":35
#         }

# cart =[]

# total = 0

# print("-------MENU------------")
# print("----------------------------")
# for key, value in menu.items():
#     print(f"{key:10} : {value:.2f}")
# print("----------------------------")

# while True:
#     food = input("Enter food (q to quit): ")
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# print("-----------YOUR ORDER---------")
# print("---------------------")
# for food in cart:
#     total += menu.get(food)
#     print(food,end=" ")
# print()
# print(f"Total: {total}")


