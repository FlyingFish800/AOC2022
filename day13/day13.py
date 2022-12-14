data = [line.strip('\n') for line in open("input.txt", 'r').readlines()]

to_list = lambda x : x if type(x) == list else [x]

def compare(left, right, base_case = False):
    if isinstance(left, int) and isinstance(right, int):
        if left == right: return None
        return  left < right

    left = to_list(left)
    right = to_list(right)

    if len(left) == 0: return True
    for i in range(len(left)):
        if i >= len(right): return False
        if left[i] == [] and right[i] == []: continue

        result = compare(left[i],right[i])
        if not result == None:
            return result
    return True if base_case or len(left) < len(right) else None

in_right_order = []

for pair in range(0,len(data),3):
    left_side = eval(data[pair])
    right_side = eval(data[pair+1])
    if compare(left_side, right_side, base_case=True): in_right_order.append((pair/3)+1)
    
print("Part1:", int(sum(in_right_order)))
