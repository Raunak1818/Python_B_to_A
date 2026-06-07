import time 


# time.sleep(3)
# print("Time's up!")


my_time = int(input("Enter the time in second: "))

# for x in range(0 , my_time):
#     print(x)
#     time.sleep(2)

# print("TIME'S UP!")


# for x in reversed(range(1 , my_time)):
#     print(x)
#     time.sleep(1)

# print("TIME'S UP!")


# for x in range(my_time, 0, -1):
#     print(x)
#     time.sleep(1)

# print("TIME'S UP!")



for x in range(my_time, 0, -1):
    second = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"00:00:{second:02}")
    # print(f"00:{minutes:02}:{second:02}")    
    # print(f"{hours:02}:{minutes:02}:{second:02}")


    time.sleep(1)

print("TIME'S UP!")