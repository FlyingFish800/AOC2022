# Get list of commands as (direction:str, steps:int) tuple
commands = [(line.split(' ')[0], int(line.split(' ')[1].strip('\n'))) for line in open("input.txt", 'r').readlines()]

# X, Y pairs for head, tail, and list of places been
head = [0,0]
tail = [0,0]
places_been = [(0,0)]

# Find if tail is too far away from head, >ropelen away in any direction
def too_far(head, tail, ropelen=1):
    if abs(head[0]-tail[0]) > ropelen or abs(head[1]-tail[1]) > ropelen: return True
    return False

# Do one move and calculate tail position, updating list of tail locations
def move(direction, length, ropelen=1):
    if direction == 'R':
        head[0] += length
        if too_far(head, tail, ropelen=ropelen):
            tail[1] = head[1]
            tail[0] = head[0]-ropelen
            tail_loc = (tail[0], tail[1])
            if not tail_loc in places_been: places_been.append(tail_loc)
    elif direction == 'L':
        head[0] -= length
        if too_far(head, tail, ropelen=ropelen):
            tail[1] = head[1]
            tail[0] = head[0]+ropelen
            tail_loc = (tail[0], tail[1])
            if not tail_loc in places_been: places_been.append(tail_loc)
    elif direction == 'U':
        head[1] += length
        if too_far(head, tail, ropelen=ropelen):
            tail[1] = head[1]-ropelen
            tail[0] = head[0]
            tail_loc = (tail[0], tail[1])
            if not tail_loc in places_been: places_been.append(tail_loc)
    elif direction == 'D':
        head[1] -= length
        if too_far(head, tail, ropelen=ropelen):
            tail[1] = head[1]+ropelen
            tail[0] = head[0]
            tail_loc = (tail[0], tail[1])
            if not tail_loc in places_been: places_been.append(tail_loc)

# Execute all moves and print how many places tail has been
for direction, length in commands:
    for _ in range(length):
        move(direction, 1)

print("Part1:", len(places_been))

# Execute all moves again with 10 ropes with length 1
places_been = [(0,0)]
knots = [[0,0] for i in range(10)]

# Do one move and calculate tail position, updating list of tail locations
def move_multiseg(knots, direction, length):
    multiseg_head = knots[0]

    if direction == 'R':
        multiseg_head[0] += length
    elif direction == 'L':
        multiseg_head[0] -= length
    elif direction == 'U':
        multiseg_head[1] += length
    elif direction == 'D':
        multiseg_head[1] -= length    

    # THEY MOVE IN THE SAME DIRECTION!!! All subsequent knots do the same as the first
    for i in range(1, len(knots)):
        seg_head = knots[i-1]
        seg_tail = knots[i]
        if too_far(seg_head, seg_tail):
            while (seg_head[0]-seg_tail[0]) > 1:
                seg_tail[0] += 1
            
            while (seg_head[0]-seg_tail[0]) < -1:
                seg_tail[0] -= 1

            while (seg_head[1]-seg_tail[1]) > 1:
                seg_tail[1] += 1
            
            while (seg_head[1]-seg_tail[1]) < -1:
                seg_tail[1] -= 1

        tail_loc = (seg_tail[0], seg_tail[1])

        if i == len(knots)-1 and not tail_loc in places_been: 
            print("A", i)
            places_been.append(tail_loc)
    

for direction, length in commands: 
    for _ in range(length):
        move_multiseg(knots, direction, 1)

print("Part2:", len(places_been))