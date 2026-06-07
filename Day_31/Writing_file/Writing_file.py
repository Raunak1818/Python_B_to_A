# Python writing files (.txt, .json, .csv)



# **************************   .txt    ****************************************

# txt_data = "I like pizza!"

# file_path = "output.txt"                          # automatically goes onto the open file folder
# # file_path = "Day_31/Writing_file/output.txt"    # for custom path you have to put path location 

# with open(file_path, "w") as file:                # w is for write
#     file.write(txt_data)
#     print(f"txt file '{file_path}' was created ")


# ******************************************************************


txt_data = "I like pizza!"

file_path = "Day_31/Writing_file/output.txt"    # for custom path you have to put path location 

# try:
#     with open(file_path, "x") as file:                # x is for write
#         file.write(txt_data)
#         print(f"txt file '{file_path}' was created ")
# except FileExistsError:
#     print("That file already exist!")



# ******************************************************************


txt_data = "I like pizza!"

file_path = "Day_31/Writing_file/output.txt"    # for custom path you have to put path location 

# try:
#     with open(file_path, "a") as file:                # a is for append
#         file.write("\n" + txt_data)
#         print(f"txt file '{file_path}' was created ")
# except FileExistsError:
#     print("That file already exist!")





# ******************************************************************

employees = ["Raj", "Ron", "John", "ponge", "Max"]

file_path = "Day_31/Writing_file/output.txt"

# with open(file_path, "w") as file:
#     for employee in employees:
#         file.write(employee + " ")
#     print(f"employees txt file '{file_path}' was created")




# ***************************  .json   **************************


import json

employee = {
    "name" : "Ron",
    "age" : 30,
    "job": "cook"
}

file_path = "Day_31/Writing_file/output.json"

# with open(file_path,"w") as file:
#     json.dump(employee, file, indent= 4)
#     print(f"json file '{file_path}' was created")





# ********************** .csv ********************************

import json
import csv

employees = [["Name", "Age", "Job"],
            ["Ron", 30, "Cook"],
            ["Patrick", 25, "Unemployed"],
            ["sandy", 34, "Scientist"]]

file_path = "Day_31/Writing_file/output.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print(f"Csv file '{file_path} was created'")