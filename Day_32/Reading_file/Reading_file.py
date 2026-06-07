# Python reading file (.txt, .json, .csv)

# ************************** .txt   *****************************

file_path = "Day_32/Reading_file/input.txt"

with open(file_path, "r") as file:
    content = file.read()
    # print(content)



# *******************************************************

    
file_path = "Day_32/Reading_file/input"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")



# **********************. .json  *********************************

import json

file_path = "Day_32/Reading_file/input.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
        # print(content["name"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")



# **********************. .csv  *********************************

import csv

file_path = "Day_32/Reading_file/input.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
            # print(line[1])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")