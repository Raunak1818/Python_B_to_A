# Logical operators = Evaluate multiple condition (or, and, not)
#                     or = at least one condition must be True
#                     and = both conditions must be True      
#                     not = inverts the condition (not False, not True)


# temp = 30
# is_raining = False

# if temp > 35 or temp < 5 or is_raining:
#     print("The event is canceled")
# else:
#     print("The event is still scheduled")


temp = 35
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is Hot outside")
elif temp <= 0 and is_sunny:
    print("It is Cold outside")
elif 28 < temp > 0 and is_sunny:
    print("It is Warm outside")
else:
    print("We can go outside")
  