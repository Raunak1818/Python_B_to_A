# default arguments = A default value for certain parameters
#                      default is used when that argument is omitted
#                      make your function more flexible, reduce # of arguments
#                      1. position, 2. DEFAULT, 3. keyboard, 4. arbitrary



# def net_price(list_price, discount, tax):
#     return list_price * (1 - discount) * (1 + tax)


# print(net_price(500,0,0.05))



# def net_price(list_price, discount=0, tax=0.05):    # set to be default value
#     return list_price * (1 - discount) * (1 + tax)


# # print(net_price(500))

# print(net_price(500,0.1,0))   #we can also adjust the default  value



# Q1 create a count up timer

# import time

# def count(start, end):
#     for x in range(start, end + 1):
#         print(x)
#         time.sleep(1)
#     print("Done")

# count(1,10)           



# import time

# def count(end, start = 0):      # for set default value
#     for x in range(start, end + 1):
#         print(x)
#         time.sleep(1)
#     print("Done")

# # count(10)

# count(30, 15)   # we can also adjust the default  value