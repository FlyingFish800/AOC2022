# Read instructions line by line
instructions = [line.strip('\n') for line in open("input.txt", 'r').readlines()]

# Set up cpu interals, and logger
x = 1
clock = 0
lines_to_log = [20,60,100,140,180,220]
x_log = []

# Execute every line, logging in necessary
for line in instructions:
    instruction = line.split(' ')
    if instruction[0] == "noop":
        clock += 1
        if clock in lines_to_log:
            x_log.append(x)
    if instruction[0] == "addx":
        clock += 1
        if clock in lines_to_log:
            x_log.append(x)
        clock += 1
        if clock in lines_to_log:
            x_log.append(x)
        x += int(instruction[1])

# Print sum of logging info multiplied
print("Part1:",sum([lines_to_log[i] * x_log[i] for i in range(len(lines_to_log))]))

# Set up cpu internals for part 2
clock = 0
x = 1
screen = [[0 for _ in range(40)] for _ in range(6)]
    
# Plot point to the screen if its within the 3 pixel window for that line
def render():
    global clock
    screen[clock//40][clock%40] = '#' if abs(x-(clock%40)) < 2 else '.'
    clock += 1

# Execute instructions
for line in instructions:
    instruction = line.split(' ')
    if instruction[0] == "noop":
        render()
    if instruction[0] == "addx":
        render()
        render()
        x += int(instruction[1])

# Print screen adding newlines after every row
print("Part2:", "".join(['\n'+"".join([str(screen[y][x]) for x in range(40)]) for y in range(6)]))