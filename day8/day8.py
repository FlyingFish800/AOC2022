# Load data. nested list of rows contaning numbers. Indexed [y][x]
trees = [[int(tree) for tree in line if not tree == '\n'] for line in open("input.txt", 'r').readlines()]

# Check visibility by getting max value on all sides and seeing if tree is taller from any side
def is_visible(x,y):
    if x == 0 or y == 0 or x == len(trees)-1 or y == len(trees)-1: return True
    value = trees[y][x]
    row = trees[y]
    column = [row[x] for row in trees]
    
    if max(row[:x]) < value: return True
    if max(row[x+1:]) < value: return True
    if max(column[:y]) < value: return True
    if max(column[y+1:]) < value: return True
    return False

# Tally visible trees and print result
tally = 0
for x in range(len(trees)):
    for y in range(len(trees)):
        if is_visible(x,y): tally += 1

print("Part1:", tally)

# Get scenic score for a tree by incrementing side scores until taller tree found, then multiply all side scores
def scenic_score(x,y):
    row = trees[y]
    column = [row[x] for row in trees]
    value = trees[y][x]
    
    left_score = 0
    for tree in row[x-1::-1]:
        left_score += 1
        if tree >= value: break
    
    right_score = 0
    for tree in row[x+1:]:
        right_score += 1
        if tree >= value: break
    
    up_score = 0
    for tree in column[y-1::-1]:
        up_score += 1
        if tree >= value: break
    
    down_score = 0
    for tree in column[y+1:]:
        down_score += 1
        if tree >= value: break
    
    return left_score * right_score * up_score * down_score

# Find max value of all trees scenic scores
print("Part2:", max([scenic_score(x,y) for x in range(len(trees)) for y in range(len(trees))]))