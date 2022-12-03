# Alexander Symons | Dec 2 2022 | Advent of Code 2022 | day2.py

# Open file and read as 2d list of each half of a move, removing newlines
moves = open("input.txt","r").readlines()
moves = [move.split("\n")[0] for move in moves]

# Generate all possible move combos as "A X" formatted strings for string comparison later
possible_moves = [f"{play} {response}" for response in "XYZ" for play in "ABC"]

# Create a dict that returns just points for the play you made
points_per_response = {move: 3-(ord('Z')-ord(move.split(' ')[1])) for move in possible_moves}

# A/X:Rock   B/Y:paper   C/Z:scissors  NOTE: You win if you play the move to the 'right' of your opponent
# Create a dictionary that checks the relative position in the list above, wrapping around.
points_for_result = dict()
for move in possible_moves:
    # Normalize to check relatively to eachother
    play, response = move.split(' ')[0], move.split(' ')[1]
    play_normalized, response_normalized = (ord('C')-ord(play)), (ord('Z')-ord(response))

    if play_normalized == response_normalized: # Same play is 3 points
        points_for_result[move] = 3
    elif play_normalized == (response_normalized+1)%3:
        # You win when your response is to the 'right' in the above normalized list
        points_for_result[move] = 6
    else: points_for_result[move] = 0 # No points for loss

# Lookup points got in both categories per move, and sum for answer
print("Part 1:", sum([points_per_response[move] + points_for_result[move] for move in moves]))

# Change inputs for part 2
possible_responses = "XYZ"
updated_moves = []

for move in moves:
    play, response = move.split(' ')

    # Normalize your response to determine win state 'offset', to figure out if you are playing move to left, right,
    # or the same. Then add normalized play of other elf, and use as index into moveset
    updated_response = possible_responses[((ord(play)-ord('A'))+(ord(response)-ord('X')-1))%3]
    updated_moves.append(f"{play} {updated_response}")

print("Part 2:", sum([points_per_response[move] + points_for_result[move] for move in updated_moves]))