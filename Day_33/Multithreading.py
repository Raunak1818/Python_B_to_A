# multithreading = Used to perform multiple task concurrency(multitasking)
#                  Good for I/O bound like reading files or fetching data from API
#                  threading. Thread(target = my_function)

import threading
import time

def walk_dog():
    time.sleep(8)
    print("You finish walking the dog")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def  get_mail():
    time.sleep(4)
    print("You get the mail")

# walk_dog()
# take_out_trash()
# get_mail()

# chore1 = threading.Thread(target=walk_dog)
# chore1.start()

# chore2 = threading.Thread(target=take_out_trash)
# chore2.start()

# chore3 = threading.Thread(target=get_mail)
# chore3.start()





# ***********************************************************




import threading
import time

def walk_dog():
    time.sleep(8)
    print("You finish walking the dog")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def  get_mail():
    time.sleep(4)
    print("You get the mail")

# walk_dog()
# take_out_trash()
# get_mail()

# chore1 = threading.Thread(target=walk_dog)
# chore1.start()

# chore2 = threading.Thread(target=take_out_trash)
# chore2.start()

# chore3 = threading.Thread(target=get_mail)
# chore3.start()

# chore1.join()
# chore2.join()
# chore3.join()

# print("All Chores are complete")





# ***********************************************************


import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking the {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def  get_mail():
    time.sleep(4)
    print("You get the mail")

# walk_dog()
# take_out_trash()
# get_mail()

chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All Chores are complete")