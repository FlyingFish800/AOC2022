# Load data line by line
data = [line.strip('\n') for line in open("input.txt", 'r').readlines()]

# Make x a list if it isnt
to_list = lambda x : x if type(x) == list else [x]

# Compare two lists recursively and retrun true if theyre in right order
def compare(left, right, base_case = False):
    # If both are ints compare as ints. None means keep going
    if isinstance(left, int) and isinstance(right, int):
        if left == right: return None
        return  left < right

    # Make both sides lists
    left = to_list(left)
    right = to_list(right)

    # If left is emtpy, they are in right order
    if len(left) == 0: return True

    # For all positions in left list
    for i in range(len(left)):
        # If its out of scope of right list, they are not in the right order
        if i >= len(right): return False

        # If both are empty, keep checking
        if left[i] == [] and right[i] == []: continue

        # Compare recursively the items at this index. If its None, continue
        result = compare(left[i],right[i])
        if not result == None:
            return result
    
    # If all items were fine up until this point, they are in the right order if right list is longer,
    # or if weve reached the end
    return True if base_case or len(left) < len(right) else None

# List of indexes in the rifht order
in_right_order = []

# Use eval to parse each side, then compare them. Add to list if theyre in the right order. Sum for answer
for pair in range(0,len(data),3):
    left_side = eval(data[pair])
    right_side = eval(data[pair+1])
    if compare(left_side, right_side, base_case=True): in_right_order.append((pair/3)+1)
    
print("Part1:", int(sum(in_right_order)))
