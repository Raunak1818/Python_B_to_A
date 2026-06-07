# Dice Art

import random

# print("\u25CF  \u250C  \u2500  \u2510  \u2502  \u2514  \u2518")

# ●  ┌  ─  ┐  │  └  ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"),
}


dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range (num_of_dice):
    # print(f"dice: {die}")
    # roll = random.randint(1,6)
    # dice.append(roll)
    dice.append(random.randint(1,6))
# print(dice)

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end="")
    print()


for die in dice:
    # print(f"die: {die}")
    total += die
print(f"total: {total}") 