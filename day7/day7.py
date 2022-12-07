import sys

# Get each line from input file without newlines
terminal_out = [line.strip('\n') for line in open("input.txt", 'r').readlines()]

# Create a node class for making trees
class node:

    # Each node has a name, and tracks if file or dir
    def __init__(self, name, is_file, size=0):
        self.children = []
        self.name = name
        self.is_file = is_file
        self.size = size
        self.parent = None

    # Add a child to the list, set its parent
    def add_child(self, child):
        self.children.append(child)
        child.set_parent(self)

    # Set the childs parent to this node
    def set_parent(self, parent):
        self.parent = parent

    # Getter for lsit of children
    def get_children(self):
        return self.children

    # String representation for debugging
    def __str__(self):
        return  f"{'/' if not self.is_file else ''}{self.name} {'[' if not self.is_file else ''}" + \
                f"{''.join([str(child) for child in self.children])}{']' if not self.is_file else ''}"

    # Find child by name, exit if not found
    def get_child(self, name):
        for child in self.children:
            if child.name == name: return child
        print(f"COULDN'T FIND {name}")
        sys.exit(1)
    
    # Return size, summing files if its a directory
    def get_size(self):
        if self.is_file: return self.size
        else: return sum(child.get_size() for child in self.children)

    # Return sum of self and all children if theyre less than amount
    def find_size(self, amount):
        my_size = self.get_size()
        total = my_size if my_size <= amount else 0
        total += sum([child.find_size(amount) for child in self.children if not child.is_file])
        return total

    # Return list of all directories larger than the size
    def find_to_delete(self, size):
        candidates = [child for child in self.children if child.get_size() >= size and not child.is_file]
        for child in self.children:
            if child.is_file: continue
            child_candidates = child.find_to_delete(size)
            candidates += child_candidates

        return candidates

# Create root node and track current node
root = node('/', False)
current = None

# Iterate over all the lines in the input file
for command in terminal_out:
    if '$' in command:
        if 'cd' in command:
            # If its a $ cd command, get the name
            name = command.split(' ')[2]
            if name == '/': 
                # Current dir is the root
                current = root
            elif name == '..':
                # Go up a directory
                current = current.parent
            else:
                # Change directories to directory named name
                current = current.get_child(name)
    else:
        # Add child, using size argument to see if its a file or directory, and add
        size, name = command.split(' ')
        if size == 'dir':
            current.add_child(node(name, False))
        else:
            current.add_child(node(name, True, size=int(size)))
            
# For part 1, find sum of all nodes <= 100k
print("Part1:", root.find_size(100000))

# Calculate space needed for update, and find minimum dir that is large enough to make space for it
space_needed = 30000000 - (70000000 - root.get_size())

print("Part2:", min([candidate.get_size() for candidate in root.find_to_delete(space_needed)]))