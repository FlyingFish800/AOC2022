# Read data in line by line
data = [line.strip('\n') for line in open("input.txt", 'r').readlines()]

# Global variables for screen size, and function to set them
screen_y0, screen_y1, screen_x0, screen_x1 = 0,0,0,0
def find_screen_size():
    global screen_x0, screen_y0, screen_x1, screen_y1

    # Track all coords
    x_coords = []
    y_coords = []

    # For every line of the input file
    for line in data:
        # Split to get each number
        chunks = line.split('=')
        sensor_x = int(chunks[1].split(',')[0])
        sensor_y = int(chunks[2].split(':')[0])
        beacon_x = int(chunks[3].split(',')[0])
        beacon_y = int(chunks[4])

        # Calculate manhattan distance and add all coordinate values that will be covered
        distance = abs(sensor_x-beacon_x)+abs(sensor_y-beacon_y)
        x_coords.append(sensor_x+distance)
        x_coords.append(sensor_x-distance)
        x_coords.append(beacon_x)
        y_coords.append(sensor_y+distance)
        y_coords.append(sensor_y-distance)
        y_coords.append(beacon_y)

    # Find the extremes and save them
    screen_x0 = min(*x_coords)
    screen_x1 = max(*x_coords)
    screen_y0 = min(*y_coords)
    screen_y1 = max(*y_coords)

# Print the screen for debugging
def print_screen():
    for y in range(screen_y0, screen_y1+1):
        print(f"{y:>3}",end=':')
        for x in range(screen_x0, screen_x1+1):
            print("#" if in_range(x,y) else '.', end='')
        print()

# Lists of sensors and beacons to track their position and distance
sensors = []
beacons = []

# Populate above arrays with coords and distances
def find_distances():
    for line in data:
        chunks = line.split('=')
        sensor_x = int(chunks[1].split(',')[0])
        sensor_y = int(chunks[2].split(':')[0])
        beacon_x = int(chunks[3].split(',')[0])
        beacon_y = int(chunks[4])   
        distance = abs(sensor_x-beacon_x)+abs(sensor_y-beacon_y)
        sensors.append((sensor_x, sensor_y, distance))
        # No duplicates!
        if not (beacon_x, beacon_y) in beacons: beacons.append((beacon_x, beacon_y))

find_distances()

# Find if coord is in range of a senssor
def in_range(x, y):
    for sensor in sensors:
        sx, sy, sd = sensor
        distance = abs(sx-x)+abs(sy-y)
        if sd >= distance: return True
    return False

# Find number of beacons in a row of given y coordinate
def beacons_in_row(y):
    beacons_found = 0
    for beacon in beacons:
        bx, by = beacon
        if by == y: beacons_found += 1
    return beacons_found

# Tally number of spots covered by sensors and subtract the covered beacons
def tally_row(y):
    tally = 0
    for x in range(screen_x0, screen_x1+1):
        if in_range(x,y): tally += 1
    tally -= beacons_in_row(y)
    return tally

# Tally the row for part 1
find_screen_size()
#print_screen()          
print("Part1:",tally_row(2000000))

# Find open spaces in the range
def find_open(x0,x1,y0,y1):
    # For all the perimeter points of each sensor
    for sx, sy, sd in sensors:
        for length in range(sd+1):
            for px, py in ( (sx+sd+1-length,sy-length),
                            (sx-sd-1+length,sy+length),
                            (sx+sd+1-length,sy-length),
                            (sx-sd-1+length,sy+length)):
                # If it matches the area were searching and is out of range of all sensors, hash and print
                if (x0 <= px <= x1) and (y0 <= py <= y1) and all(abs(px-sx2)+abs(py-sy2) > sd2 for sx2,sy2,sd2 in sensors):
                    print("Part2:", px*4000000+py)
                    return

# Call for part 2
find_open(0,4000000,0,4000000)