# Load data as 2d array[y][x] of values
data = [line.strip('\n') for line in open("input.txt",'r').readlines()]

# Create node for graph
class node:
    # Initialize with x,y, and a value. S is equivalent to a, and E to z 
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        if value == ord('S')-ord('a'): self.value = 0
        if value == ord('E')-ord('a'): self.value = 25

        # Set up values for A* algorithm
        self.g_cost = None
        self.h_cost = None
        self.f_cost = None
        self.parent = None
        self.neighbors = []
        self.path = None

    # Is this node neighboring another node?
    def touching(self, node):
        neighbor_conditions = [(-1,0),(1,0),(0,-1),(0,1)]
        return (abs(self.x-node.x), abs(self.y-node.y)) in neighbor_conditions

    # Find all neighboring nodes and populate self.neighbors
    def find_neighbors(self, nodes):
        for node in nodes:
            if self.touching(node) and not self == node: self.neighbors.append(node)

    # Calculate f cost, and all other costs
    def calculate_f_cost(self,other,part2=False):
        tmp_g_cost = other.g_cost + 1 if not part2 or self.value == 0 else 0
        tmp_h_cost = abs(end.x-self.x)+abs(end.y-self.y)
        tmp_f_cost = tmp_g_cost + tmp_h_cost
        if self.f_cost == None or tmp_f_cost < self.f_cost:
            self.g_cost = tmp_g_cost
            self.h_cost = tmp_h_cost
            self.f_cost = tmp_f_cost

    # Can be traversed from other->self
    def is_traversable(self, other): # Other is checcking if you are traversable
        if other == start: return self.value <= 1
        if self == end: return other.value == ord('z')-ord('a')
        return self.value <= other.value+1

    def __str__(self):
        return f"({self.value}:{self.x},{self.y})"

    def __repr__(self):
        return str(self)

# A* variables
start, end = None, None
nodes = []
open = []
closed = []

# Set up for A* from S->E
def setup():
    global start, end, nodes, open, closed
    start, end = None, None
    nodes = []

    # Populate nodes, remember start and end. Add start to be first node to search
    for y in range(len(data)):
        for x, char in enumerate(data[y]):
            current_node = node(x, y, ord(data[y][x])-ord('a'))
            if char == 'S': start = current_node
            if char == 'E': end = current_node
            nodes.append(current_node)

    closed = []
    open = [start]

    # Initialize nodes by setting up start manually, and finding all neighbors
    start.g_cost = 0
    start.f_cost = 0
    start.h_cost = abs(end.x-start.x)+abs(end.y-start.y)

    [current_node.find_neighbors(nodes) for current_node in nodes]

# Find node with lowest f cost (lowest h cost for tiebreaker) in list of searchable nodes
def find_lowest_cost():
    lowest_cost = 9999999999999999999
    lowest_node = None
    for current_node in open:
        if current_node.f_cost < lowest_cost:
            lowest_cost = current_node.f_cost
            lowest_node = current_node
        if current_node.f_cost == lowest_cost:
            if current_node.h_cost < lowest_node.h_cost:
                lowest_node = current_node

    return lowest_node

# Run A* algorithm
def a_star():
    while True:
        # Find current node and move it from searchable to searched
        current_node = find_lowest_cost()
        if len(open) == 0: return # Stop if dead end
        open.remove(current_node)
        closed.append(current_node)

        if current_node == end: # End found!
            return 

        # Update all neighbors
        for neighbor in current_node.neighbors:
            # If already processed or unwalkable, skip
            if not neighbor.is_traversable(current_node) or neighbor in closed:
                continue

            # If neighbor needs updating
            if neighbor.path == None or current_node.path+1 < neighbor.path or not neighbor in open:
                # Update path parent and f cost, and mark searchable if necessary
                neighbor.calculate_f_cost(current_node)
                neighbor.parent = current_node
                neighbor.path = 0 if current_node.path == None else current_node.path+1
                if not neighbor in open:
                    open.append(neighbor)

# Recursively print path to end for debugging
def print_path(node):
    if not node.parent == None: print_path(node.parent)
    print(node)

# Setup and run from S->E, add 1 for S path (length) being none (effectively -1)
setup()
a_star()
print("Part1:",end.path+1)

# Modified setup to start at a particular node
def setup2(start_node):
    # Reset values
    global start, end, nodes, open, closed
    start, end = None, None
    nodes = []

    # Reset nodes, set start to the node at start_node (an (x,y) tuple)
    for y in range(len(data)):
        for x, char in enumerate(data[y]):
            current_node = node(x, y, ord(data[y][x])-ord('a'))
            if start_node[0] == x and start_node[1] == y: 
                start = current_node
            if char == 'E': end = current_node
            nodes.append(current_node)

    # Reset A* tracking lists, manually set up start, and set neighbors 
    closed = []
    open = [start]

    start.g_cost = 0
    start.f_cost = 0
    start.h_cost = abs(end.x-start.x)+abs(end.y-start.y)

    [current_node.find_neighbors(nodes) for current_node in nodes]

# Fin minimum length path from start to 'E'
def find_min_path():
    # Paths to search
    paths = []

    # Find all locations at elevation 'a' and append them
    for y in range(len(data)):
        for x, char in enumerate(data[y]):
            if char in 'Sa': paths.append((x,y))

    # Track shortest path
    min_path = None

    # Try every path and if its shorter than the last shortest, update
    for path in paths:
        setup2(path)
        print(path)
        a_star()
        if not end.path == None and (min_path == None or min_path > end.path):
            min_path = end.path

    # Return shortest
    return  min_path

# Print shortest path for part 2, accounting for start.path = None as in part 1
print("Part2:",find_min_path()+1)
