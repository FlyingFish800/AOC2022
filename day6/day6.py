# Read data as string
data = open("input.txt",'r').read()

# Find the index of a window of specified length
def find_window(length):
    window_end = 0
    for index in range(len(data)):
        # Try and get slice, reject invalid slices
        slice = data[index-length:index]
        if slice == '': continue

        # Sum occurences, chars that occur multiple times will have duplicate entries.
        # Check sum against window length and return the first one that is correct
        counts = sum([slice.count(char) for char in slice])
        if counts == length: 
            window_end = index
            break

    return window_end

# Part 1 is window size of 4, part 2 is size od 14
print("Part1:",find_window(4))

print("Part2:",find_window(14))
