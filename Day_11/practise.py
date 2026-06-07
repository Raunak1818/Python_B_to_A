# shopping cart program

# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Enter the food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("----- YOUR CART-----")

# for food in foods:
#     print(food, end=" ")

# for price in prices:
#     total += price
# print()
# print(f"Your total is: ${total}")


# print("----- YOUR CART-----")

# for i in range(len(foods)):
#     print(f"{foods[i]} - ${prices[i]}")
#     total += prices[i]

# print(f"Your total is: ${total}")






# ********Q2 - Shopping List with Quantities*************

foods = []
prices = []
quantities = []
total = 0

while True:
    food = input("Enter the food (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        quantity = int(input("Enter the quantity: "))
        foods.append(food)
        prices.append(price)
        quantities.append(quantity)

print("****** YOUR CART********")

for i in range(len(foods)):
    item_total = quantities[i] * prices[i]
    print(f"{quantities[i]} X {foods[i]} = {item_total}")
    total += item_total

print(f"Your total is: {total}")