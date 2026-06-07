# Python file detection

import os

# file_path = "test.txt"
file_path = "Day_30/File_Detection/test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
    else:
        print("That location doesn't exist")

else:
    print(f"That location doesn't exist")