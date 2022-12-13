data = [line.strip('\n') for line in open("input.txt",'r').readlines()]

class node:
    def __init__(self, x, y, value, is_target=False):
        self.x = x
        self.y = y
        self.value = value
        if value == ord('S')-ord('a'): self.value = 0
        if value == ord('E')-ord('a'): self.value = 25
        self.is_target = is_target
        self.g_cost = None
        self.h_cost = None
        self.f_cost = None
        self.parent = None
        self.neighbors = []
        self.path = None

    def touching(self, node):
        neighbor_conditions = [(-1,0),(1,0),(0,-1),(0,1)]
        return (abs(self.x-node.x), abs(self.y-node.y)) in neighbor_conditions

    def find_neighbors(self, nodes):
        for node in nodes:
            if self.touching(node) and not self == node: self.neighbors.append(node)

    def calculate_f_cost(self,other,part2=False):
        tmp_g_cost = other.g_cost + 1 if not part2 or self.value == 0 else 0
        tmp_h_cost = abs(end.x-self.x)+abs(end.y-self.y)
        tmp_f_cost = tmp_g_cost + tmp_h_cost
        if self.f_cost == None or tmp_f_cost < self.f_cost:
            self.g_cost = tmp_g_cost
            self.h_cost = tmp_h_cost
            self.f_cost = tmp_f_cost

    def is_traversable(self, other): # Other is checcking if you are traversable
        if other == start: return self.value <= 1
        if self == end: return other.value == ord('z')-ord('a')
        return self.value <= other.value+1

    def __str__(self):
        return f"({self.value}:{self.x},{self.y})"

    def __repr__(self):
        return str(self)


start, end = None, None
nodes = []
open = []
closed = []

def setup():
    global start, end, nodes, open, closed
    start, end = None, None
    nodes = []

    for y in range(len(data)):
        for x, char in enumerate(data[y]):
            current_node = node(x, y, ord(data[y][x])-ord('a'))
            if char == 'S': start = current_node
            if char == 'E': end = current_node
            nodes.append(current_node)

    closed = []
    open = [start]

    start.g_cost = 0
    start.f_cost = 0
    start.h_cost = abs(end.x-start.x)+abs(end.y-start.y)

    [current_node.find_neighbors(nodes) for current_node in nodes]

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

def a_star():
    while True:
        current_node = find_lowest_cost()
        if len(open) == 0: return
        open.remove(current_node)
        closed.append(current_node)

        if current_node == end:
            return 

        for neighbor in current_node.neighbors:
            if not neighbor.is_traversable(current_node) or neighbor in closed:
                continue

            if  neighbor.path == None or current_node.path+1 < neighbor.path or not neighbor in open:
                neighbor.calculate_f_cost(current_node)
                neighbor.parent = current_node
                neighbor.path = 0 if current_node.path == None else current_node.path+1
                if not neighbor in open:
                    open.append(neighbor)

def print_path(node):
    if not node.parent == None: print_path(node.parent)
    print(node)

setup()
a_star()
print("Part1:",end.path+1)

def setup2(start_node):
    global start, end, nodes, open, closed
    start, end = None, None
    nodes = []

    for y in range(len(data)):
        for x, char in enumerate(data[y]):
            current_node = node(x, y, ord(data[y][x])-ord('a'))
            if start_node[0] == x and start_node[1] == y: 
                print("start!")
                start = current_node
            if char == 'E': end = current_node
            nodes.append(current_node)

    closed = []
    open = [start]

    start.g_cost = 0
    start.f_cost = 0
    start.h_cost = abs(end.x-start.x)+abs(end.y-start.y)

    [current_node.find_neighbors(nodes) for current_node in nodes]

def find_min_path():
    paths = []

    for y in range(len(data)):
        for x, char in enumerate(data[y]):
            if char in 'Sa': paths.append((x,y))

    min_path = None

    for path in paths:
        setup2(path)
        print(path)
        a_star()
        if not end.path == None and (min_path == None or min_path > end.path):
            min_path = end.path

    return  min_path

print("Part2:",find_min_path()+1)