
def find_distance(sequence, marker):
    count = 0
    distance = 0
    for ch in sequence:

        if ch == marker:
            count += 1
        if count == 1:
            distance += 1

    return distance-1


print(find_distance("---x------x", 'x'))