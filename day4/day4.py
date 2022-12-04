# Split each line into a list containing the two intervals as a nested lsit, with their min and maxs as nested lists
pairs = [[line.split(',')[0].split('-'), line.split(',')[1].split('\n')[0].split('-')]for line in open("input.txt", 'r').readlines()]

# Check each pair is the mins and maxs are within eachother, increment tally and print
fully_cointained = 0
for pair in pairs:
    p1_min = min(int(pair[0][0]), int(pair[0][1]))
    p1_max = max(int(pair[0][0]), int(pair[0][1]))
    p2_min = min(int(pair[1][0]), int(pair[1][1]))
    p2_max = max(int(pair[1][0]), int(pair[1][1]))
    if ((p1_min >= p2_min and p1_max <= p2_max) or (p2_min >= p1_min and p2_max <= p1_max)): fully_cointained += 1


print("Part1:",fully_cointained)

# Check each pair to see if the hihgest minimum is greater than the lowest max, increment tally if so and print
contained = 0
for pair in pairs:
    p1_min = min(int(pair[0][0]), int(pair[0][1]))
    p1_max = max(int(pair[0][0]), int(pair[0][1]))
    p2_min = min(int(pair[1][0]), int(pair[1][1]))
    p2_max = max(int(pair[1][0]), int(pair[1][1]))
    lower_max = min(p1_max, p2_max)
    uper_min = max(p1_min, p2_min)
    if uper_min <= lower_max: contained += 1

print("Part2:",contained)