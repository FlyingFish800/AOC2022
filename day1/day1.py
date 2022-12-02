# Alexander Symons | Dec 1 2022 | Advent of Code 2022 | day1.py

# Input data stored in input.txt
file = open("input.txt", "r")

elves_data = []

# Create list containing every elve's list of calories
tmp_data = []
for line in file:
    if line == '\n':
        elves_data.append(tmp_data)
        tmp_data = []
    else: tmp_data.append(int(line.split("\n")[0]))

# Sum and sort the lists in descending order
elves_data_tallied = sorted([sum(elf_data) for elf_data in elves_data], reverse=True)

print(f"Part 1: {elves_data_tallied[0]}")
print(f"Part 2: {sum(elves_data_tallied[0:3])}")