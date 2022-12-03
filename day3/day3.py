# Read file and parse into rucksacks by \n, divide in two equal sized compartments
rucksacks = [[rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:-1]] for rucksack in open("input.txt",'r').readlines()]

# Find which letters are the same in each compartment of a rucksack, and apply the get priority function, and sum it
same_items = [[itema for itema in rucksack[0] for itemb in rucksack[1] if itema == itemb][0] for rucksack in rucksacks]
get_priority = lambda char : ord(char)-ord('a')+1 if char.islower() else ord(char)-ord("A")+27
print("Part 1:", sum(list(map(get_priority, same_items))))

# Create groups in chunks of 3, check eevry item for every member to find a match, then sum their priorities
groups = [[rucksack.split('\n')[0] for rucksack in open("input.txt",'r').readlines()][i:i+3] for i in range(0,len(rucksacks),3)]
same_items_group = [[itema for itema in group[0] for itemb in group[1] for itemc in group[2] if itema == itemb == itemc][0] for group in groups]
print("Part 2:", sum(list(map(get_priority, same_items_group))))