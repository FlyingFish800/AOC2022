# Load file so each set of points is on its own line
data = [line.strip('\n') for line in open("input.txt", 'r').readlines()]

screen = []
maxy = 0

# Reset screen, draw lines, set max y value
def reset():
    global screen, maxy
    # Screen is [200][1000] [y][x]
    screen = [['.' for i in range(1000)] for i in range (200)]
    screen[0][500] = '+'
    maxy = 0

    # Load in every shape. Line as in line of file
    for line in data:
        # Reset last point, and break all points int [(x1,y1), ...]
        last = None
        points = [point.split(',') for point in line.split(' ') if not point == '->']

        for point in points:
            px = int(point[0])
            py = int(point[1])

            # Update max y value if necessary, and set last if this is first point
            if py > maxy: maxy = py
            if last == None:
                last = (px,py)
                continue

            lx = last[0]
            ly = last[1]

            # Draw a line for all x,y points between the two points, set points to '#'
            for x in range(min(lx,px), max(lx+1,px+1)):
                for y in range(min(ly,py),max(ly+1,py+1)):
                    screen[y][x] = '#'

            last = (px,py)

# Print for debugging. Szie fits in terminal and shows important stuff
def print_screen():
    for y in range(0,200):
        for x in range(450,550):
            print(screen[y][x],end='')
        print()

# Determine move if one can be made. None: fallen off, 1: down, 2: down/left, 3: down/right in that priority order
def can_move(x,y):
    try:
        if screen[y+1][x] == '.':
            return 1
        if screen[y+1][x-1] == '.':
            return 2
        if screen[y+1][x+1] == '.':
            return 3
        return 0
    except IndexError:
        return None

# Simulate one grain of sand in the furrent enviroment. Returns wether or not another grain can be simulated
def simulate_sand():
    # Start at origin, and determine initial move
    x = 500
    y = 0
    move = can_move(x,y)

    # While move works
    while move > 0:
        y += 1 # All moves go down 1
        if move == 2: x -= 1 # Move horixontally as perscribed
        if move == 3: x += 1

        # Determine next move, return False to stop more sand if one fell into void (return False)
        move = can_move(x,y)
        if move == None: return False

    # If no moves were taken, return False to stop simulation and dont overwrite origin '+'
    if x == 500 and y == 0: return False

    # Set potition to have grain of sand and keep simulating more
    screen[y][x] = 'o'
    return True

# For part 1: Reset screen, simulate sand while they arent falling into void, and print tally
reset()
#print_screen()

sands = 0
while simulate_sand():
    #print_screen()
    sands += 1

print("Part1:", sands)

# For part 2: Reset and use max y to add floor, then run as before adding 1 for the origin
reset()
#print(maxy)

for x in range(0,1000):
    screen[maxy+2][x] = '#'

sands = 0
while simulate_sand():
    #print_screen()
    sands += 1

#print_screen()
print("Part2:", sands+1)
