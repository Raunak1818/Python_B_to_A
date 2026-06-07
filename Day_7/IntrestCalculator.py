# Python compound intrest calculator

# A = P(1 + r/n)^t

# A = final amount 
# P = intial principal balance
# r = intrest rate
# t = number of time perids elapsed



# principle = 0
# rate = 0
# time = 0

# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Principle can't be less than or equal to zero")


# while rate <= 0:
#     rate = float(input("Enter the rate amount: "))
#     if rate <= 0:
#         print("rate can't be less than or equal to zero")

# while time <= 0:
#     time = int(input("Enter the time in years: "))
#     if time <= 0:
#         print("time can't be less than or equal to zero")

# print(principle)
# print(rate)
# print(time)

# total = principle * pow((1 + rate /100), time)

# print(f"Balance after {time} years: Rs {total:.2f}")







principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        print("rate can't be less than or equal to zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("time can't be less than or equal to zero")
    else:
        break
    
# print(principle)
# print(rate)
# print(time)

total = principle * pow((1 + rate /100), time)

print(f"Balance after {time} years: Rs {total:.2f}")


