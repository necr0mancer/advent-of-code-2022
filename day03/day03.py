# --- Day 3: Rucksack Reorganization ---
from string import ascii_letters

# Getting the data
with open("data.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

#print(data)
# iterate through the data
totalSum = 0
for rucksack in data:
    # find half
    half = len(rucksack)//2
    
    left = set(rucksack[:half])
    right = set(rucksack[half:])
    
    #print(rucksack, left, right)
    for priority, char in enumerate(ascii_letters):
        if char in left and char in right:
            totalSum += priority + 1

print("Answer to part 1:" , totalSum)

# === part 2 ===

j = 3
totalSum = 0
for i in range(0, len(data), 3):
    rucksacks = data[i:j]
    j += 3
    
    #print(rucksacks)
    for priority, char in enumerate(ascii_letters):
        if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]:
            totalSum += priority + 1

print("Answer to part 2:" , totalSum)
