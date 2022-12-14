data = [line.strip('\n') for line in open("input.txt", 'r').readlines()]


screen = []

maxy = 0
def reset():
    global screen, maxy
    screen = [['.' for i in range(1000)] for i in range (200)]
    screen[0][500] = '+'

    for line in data:
        last = None
        points = [point.split(',') for point in line.split(' ') if not point == '->']
        for point in points:
            px = int(point[0])
            py = int(point[1])
            if py > maxy: maxy = py
            if last == None:
                last = (px,py)
                continue

            lx = last[0]
            ly = last[1]

            for x in range(min(lx,px), max(lx+1,px+1)):
                for y in range(min(ly,py),max(ly+1,py+1)):
                    screen[y][x] = '#'

            last = (px,py)

def print_screen():
    for y in range(0,200):
        for x in range(450,550):
            print(screen[y][x],end='')
        print()

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

def simulate_sand():
    x = 500
    y = 0
    move = can_move(x,y)
    while move > 0:
        y += 1
        if move == 2: x -= 1
        if move == 3: x += 1
        move = can_move(x,y)
        if move == None: return False
    screen[y][x] = 'o'
    return True

reset()
#print_screen()

sands = 0
while simulate_sand():
    #print_screen()
    sands += 1

print("Part1:", sands)

reset()
print(maxy)
for x in range(0,1000):
    screen[maxy][x] = '#'

sands = 0
while simulate_sand():
    #print_screen()
    sands += 1

print_screen()
print("Part2:", sands)
