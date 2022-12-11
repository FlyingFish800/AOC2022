# Create list of objects in your backpack
# Create monkey objects
# For each iteration:
#   For every object:
#       Find its monkey
#       Follow monkey's rules using eval
#       Update object's monkey

data = [line.strip("\n") for line in open("input.txt", 'r').readlines()]

class Monkey:
    def __init__(self, id, operation, test, true_path, false_path):
        self.id = id
        self.operation = operation
        self.test = test
        self.true_path = true_path
        self.false_path = false_path

class Item:
    def __init__(self, id, starting):
        self.id = id
        self.starting_monkey = starting
