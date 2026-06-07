# import time

# num = int(input("Enter the number: "))

# for x in range(0, num + 1):
#     print(x)
#     time.sleep(1)


# import time

# num = int(input("Enter the number: "))

# i = 1

# while i < num:
#     print(i)
#     time.sleep(1)
#     i += 1

# print("over")




# import time

# num = int(input("Enter the number: "))

# for x in range(1 , num):
#     time.sleep(1)
#     if x == 12:
#         continue
#     else:
#         print(x)


# import time 


# num = int(input("Enter the number: "))

# i = 1

# while i < num:
#     if i % 2 != 0:
#         print(i, end=" ")
#         time.sleep(1)
#     i += 1
# print("above no. are odd")





# import time

# num = int(input("Enter the number: "))

# i = 1
# sum = 0

# while i < num:
#     # print(i)
#     sum += i
#     print(f"i: {i}, sum: {sum}")
#     time.sleep(1)
#     i += 1

# print(f"final sum: {sum}")



# import time

# num = int(input("Enter the number: "))

# for x in range(0 , num):
#     print(x)
#     time.sleep(1)




# import time

# num = int(input("Enter the number: "))

# for x in reversed(range(0 , num)):
#     print(x)
#     time.sleep(1)



# import time

# num = int(input("Enter the number: "))

# for x in range(num, 0, -1):
#     print(x)
#     time.sleep(1)




# import time

# num = int(input("Enter the number: "))

# for x in range(0 , num):
#     if x % 2 == 0:
#         print(x)
#         time.sleep(1)
    




# import time

# num = int(input("Enter the number: "))

# for x in range(0 , num):
#     if x % 2 != 0:
#         print(x)
#         time.sleep(1)
    



# import time

# num = int(input("Enter the number: "))

# print("---- Table of 5 ------")

# for x in range(1 , num):
#     print(f"5 x {x} = {5 * x}") 
#     time.sleep(1)






# import time 

# num = int(input("Enter the number "))

# sum = 0

# for x in range(1, num):
#      sum += x
#      time.sleep(1)
#      print(f"x: {x}, sum: {sum} ")

# print(f"total sum: {sum}")






# import time

# sum = 0

# num = int(input("Enter the number: "))

# for x in range(1, num):
#     if x % 2 == 0:
#         sum += x
#         time.sleep(1)
#         print(f"x: {x}, sum: {sum}")

# print(f"sum of even number: {sum}")





# import time

# num = int(input("Enter the number: "))

# sum = 0

# for x in range(1, num):
#     if x % 2 != 0:
#         sum += x
#         print(f"x: {x}, sum: {sum}")
#         time.sleep(1)

# print(f"sum of odd no.: {sum}")




# import time

# num = int(input("enter the number: "))

# for x in range(1, num):
#     if x % 3 == 0:
#         print(x)
#         time.sleep(1)
    
# print("above no. divisible by 3")






# import time

# num = int(input("Enter the number: "))

# count = 0

# for x in range(1, num):
#     if x % 5 == 0:
#         count += x
#         print(f"x: {x}, count: {count}")

# print(f"count total number are divisible by 5: {count}")





# num = int(input("Enter the number: "))

# for x in range (1,num):
#     print("*"*x)





num = int(input("Enter the number: "))

for x in range (1,num):
    for y in range(1, x+1):
        print(y,end="")
    print()