# Get all data from file
data = [line.strip('\n') for line in open("input.txt", 'r').readlines()]

# Find the number of stacks to be sued by finding the last element in the 'key' line
index_of_key = data.index('')-1
element_count = [int(element.strip(' ')) for element in data[index_of_key].split(' ') if not element.strip('') == ''][-1]

# Reset the state to that defined in the input file, and reverse the lists for stack functionality
state = []
def reset_state():
    global state
    state = [list() for i in range(element_count)]

    for line_number in range(0, index_of_key):
        line = data[line_number]
        for i in range(0,len(line), 4):
            if not line[i+1] == ' ': state[i//4].append(line[i+1])
        
    [sublist.reverse() for sublist in state]

reset_state()

# Split command statements, then pop an item from the start stack and push it to dest stack quantity times
for line_number in range(index_of_key+2, len(data)):
    command = data[line_number].split(' ')
    quantity, start, destination = int(command[1]), int(command[3]), int(command[5])
    for i in range(quantity):
        state[destination-1].append(state[start-1].pop())

# Print last item from each stack as string      
print("Part1:", ''.join([stack[-1] for stack in state]))

reset_state()

# Same as above but pop to a chunk and reverse it to get in-order list, and add that to dest
for line_number in range(index_of_key+2, len(data)):
    command = data[line_number].split(' ')
    quantity, start, destination = int(command[1]), int(command[3]), int(command[5])

    chunk = []
    for i in range(quantity):
        chunk.append(state[start-1].pop())

    chunk.reverse()
    state[destination-1] += chunk

# Print last item as a string again for part 2
print("Part2:", ''.join([stack[-1] for stack in state]))