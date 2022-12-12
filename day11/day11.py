# Create list of objects in your backpack
# Create monkey objects
# For each iteration:
#   For every object:
#       Find its monkey
#       Follow monkey's rules using eval
#       Update object's monkey

import math

# Get info from file
data = [line.strip("\n") for line in open("input.txt", 'r').readlines()]

# Create monkey class containing all necessary info
class Monkey:
    def __init__(self, id, operation=None, test=None, true_path=None, false_path=None):
        self.id = id
        self.operation = operation
        self.test = test
        self.true_path = true_path
        self.false_path = false_path
        self.items : list[Item] = []
        self.inspections = 0

    # Setter for any required peice of info
    def set_attr(self, operation=None, test=None, true_path=None, false_path=None):
        if not operation == None:
            self.operation = operation
        if not test == None:
            self.test = test
        if not true_path == None:
            self.true_path = true_path
        if not false_path == None:
            self.false_path = false_path

    # Add an item to be processed by it
    def add_item(self, item):
        self.items.append(item)

    # Remove item when done
    def remove_item(self, item):
        self.items.remove(item)

    def __str__(self):
        return f"{self.id}: {self.items}"

# Create class item to track its info
class Item:
    def __init__(self, id, starting):
        self.id = id
        self.starting_monkey = starting
        self.current_monkey = starting

    # Unused reset method
    def reset(self):
        self.current_monkey = self.starting_monkey

    # Simulate this item for one round
    def simulate(self, monkeys, part2=False):
        monkey : Monkey = monkeys[self.current_monkey]

        # Set old variable used in eval statement. Part 1 requires intdiv by 3, part 2 requires
        # mitigations for very large numbers
        old = self.id
        self.id =   eval(monkey.operation) // 3 if not part2 else \
                    eval(monkey.operation) % math.lcm(*[monkey.test for monkey in monkeys])

        # Track inspections and reassign this item to its proper monkey
        monkey.inspections += 1
        if self.id % monkey.test == 0: self.current_monkey = monkey.true_path
        else: self.current_monkey = monkey.false_path
        monkey.remove_item(self)
        monkeys[self.current_monkey].add_item(self)

    def __str__(self):
        return f"Item {self.id}, current: {self.current_monkey}"

    def __repr__(self):
        return f"Item {self.id}, current: {self.current_monkey}"

monkeys : list[Monkey] = []

# Process input text and use it to create required monkeys, and assign them their items
def process_data():
    global monkeys
    monkeys = []
    current_monkey : Monkey = None
    for line in data:
        split_line = line.split(' ')
        if split_line[0] == 'Monkey' and ':' in split_line[1]:
            # Create monkey with number id
            current_monkey = Monkey(int(split_line[1].strip(':')))

        elif "Starting items:" in line:
            # Create items and assign them to their starter monkey
            for item in split_line:
                item = item.strip(',')
                if item.isnumeric():
                    current_monkey.add_item(Item(int(item), current_monkey.id))

        # Set all of the monkey's attributes
        elif "Operation:" in line:
            current_monkey.set_attr(operation=line.split('=')[1])
        elif "Test:" in line:
            current_monkey.set_attr(test=int(split_line[-1]))
        elif "If true:" in line:
            current_monkey.set_attr(true_path=int(split_line[-1]))
        elif "If false:" in line:
            current_monkey.set_attr(false_path=int(split_line[-1]))
            monkeys.append(current_monkey) # This is the last attribute, 'complete' monkey
        else:
            pass

# Simulate a single round for every item of every monkey
def simulate_round(part2=False):
    for monkey in monkeys:
        items = list(monkey.items)
        for item in items:
            item.simulate(monkeys, part2=part2)

# Get data, simulate 20 rounds, sort monkeys, and multiply top two's inspections for monkey business
process_data()
for i in range(20): simulate_round()
monkeys_sorted = sorted(monkeys, key=lambda monkey : monkey.inspections, reverse=True)[:2]
print("Part1:",monkeys_sorted[0].inspections*monkeys_sorted[1].inspections)

# Repeat 10000 times for part 2, with optional logging info
process_data()
rounds_to_log = [1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
for i in range(10000): 
    #if i in rounds_to_log: print(i,[monkey.inspections for monkey in monkeys])
    #if i % 100 == 0: print(f"{i/10000}%")
    simulate_round(part2=True)
monkeys_sorted = sorted(monkeys, key=lambda monkey : monkey.inspections, reverse=True)[:2]
print("Part2:",monkeys_sorted[0].inspections*monkeys_sorted[1].inspections)