# Load data as list of ints
data = [int(line) for line in open("input.txt", 'r').readlines()]

# Define mix function
def mix(decryption_key=1, mixes=1):
    # Create list of (index, value) pairs to get around duplicates
    original = [(i, x*decryption_key) for i, x in enumerate(data)]

    # Deep copy list for mixing
    mixed = list(original)
    for _ in range(mixes):
        for num in original:
            # For every number, add its current and original index, and move it tot he new index (with wrapping)
            index = mixed.index(num)
            mixed.pop(index)
            new_index = (index+num[1])%len(mixed)
            mixed.insert(new_index, num)

    # Return mixed list
    return mixed

# Mix list and find sum of values at indexes 1k, 2k, and 3k for part 1
mixed = mix()
zero_index = mixed.index((data.index(0),0))
print("Part1:",sum([mixed[(zero_index+num)%len(mixed)][1] for num in [1000, 2000, 3000]]))

# Repeat for part 2, apply decryption key and run 10 times
mixed = mix(decryption_key=811589153, mixes=10)
zero_index = mixed.index((data.index(0),0))
print("Part1:",sum([mixed[(zero_index+num)%len(mixed)][1] for num in [1000, 2000, 3000]]))