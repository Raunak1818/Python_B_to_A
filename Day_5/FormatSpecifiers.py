# format specifiers = {:flags} format a value based on what 
#                             flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^  = centre align
# :+ = use a plus sign to indicate positive Value
# := = plae sign to leftmost position
# :  = insert a place before positive numbers
# :, = comma separator


# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34


# print(f"Price 1 is {price1:.3f}")
# print(f"Price 2 is {price2:.3f}")
# print(f"Price 3 is {price3:.3f}")



# print(f"Price 1 is {price1:08}")
# print(f"Price 2 is {price2:09}")
# print(f"Price 3 is {price3:07}")


# print(f"Price 1 is {price1:<8}")
# print(f"Price 2 is {price2:<9}")
# print(f"Price 3 is {price3:<7}")


# print(f"Price 1 is {price1:>8}")
# print(f"Price 2 is {price2:>9}")
# print(f"Price 3 is {price3:>7}")

# print(f"Price 1 is {price1:^8}")
# print(f"Price 2 is {price2:^9}")
# print(f"Price 3 is {price3:^7}")


# print(f"Price 1 is {price1:+}")
# print(f"Price 2 is {price2:+}")
# print(f"Price 3 is {price3:+}")


# print(f"Price 1 is {price1: }")
# print(f"Price 2 is {price2: }")
# print(f"Price 3 is {price3: }")


price1 = 30000.14159
price2 = -98700.65
price3 = 12000.34

# print(f"Price 1 is {price1:,}")
# print(f"Price 2 is {price2:,}")
# print(f"Price 3 is {price3:,}")


# print(f"Price 1 is {price1:,.2f}")
# print(f"Price 2 is {price2:,.2f}")
# print(f"Price 3 is {price3:,.2f}")


print(f"Price 1 is {price1:+,.2f}")
print(f"Price 2 is {price2:+,.2f}")
print(f"Price 3 is {price3:+,.2f}")