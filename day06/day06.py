with open('06data.txt') as datafile:
    input = datafile.read()

# === part 1 ===
for i in range(4, len(input)):
    sequence = set(input[(i-4):i])
    if len(sequence) == 4:
        print("answer: ", i)
        break


# === part 2 ===
for i in range(14, len(input)):
    sequence = set(input[(i-14):i])
    if len(sequence) == 14:
        print("anser:" , i)
        break