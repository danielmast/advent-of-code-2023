# Init a list of currents
# Add the top left to the currents
# current = [(0,0, 'right')]
# Determine the next location, based on the current location and the direction
# If split, add a current
# Add locations to seen
# seen = [][] (with same length and width as area, init with dots

# Iterate over seen to count the #'s

delta = {
        '.': {
            'l': [((0, -1), 'l')],
            'r': [((0, 1), 'r')],
            'u': [((-1, 0), 'u')],
            'd': [((1, 0), 'd')]
        },
        '-': {
            'l': [((0, -1), 'l')],
            'r': [((0, 1), 'r')],
            'u': [((0, -1), 'l'), ((0, 1), 'r')],
            'd': [((0, -1), 'l'), ((0, 1), 'r')]
        },
        '|': {
            'l': [((-1, 0), 'u'), ((1, 0), 'd')],
            'r': [((-1, 0), 'u'), ((1, 0), 'd')],
            'u': [((-1, 0), 'u')],
            'd': [((1, 0), 'd')]
        },
        '/': {
            'l': [((1, 0), 'd')],
            'r': [((-1, 0), 'u')],
            'u': [((0, 1), 'r')],
            'd': [((0, -1), 'l')]
        },
        '\\': {
            'l': [((-1, 0), 'u')],
            'r': [((1, 0), 'd')],
            'u': [((0, -1), 'l')],
            'd': [((0, 1), 'r')]
        }
    }

def main():
    area = read_file('input.txt')
    seen = init_seen(area)
    seen_currents = []

    currents = [((0,0), 'r')]

    while len(currents) > 0:
        current = currents.pop(0)
        current_location = current[0]

        if current in seen_currents:
            continue
        else:
            seen_currents.append(current)


        line = seen[current_location[0]]
        seen[current_location[0]] = line[:current_location[1]] + '#' + line[current_location[1] + 1:]

        next_locations = get_next_locations(current, area)
        currents.extend(next_locations)

        for line in seen:
            print(line)
        print()

    sum = 0

    for line in seen:
        for char in line:
            if char == '#':
                sum += 1

    answer = sum
    print(f'The answer: {answer}')

def init_seen(area):
    seen = []

    for line in area:
        seen.append('.' * len(line))

    return seen

def get_next_locations(current, area):
    current_location = current[0]
    direction = current[1]

    current_char = area[current_location[0]][current_location[1]]
    deltas = delta[current_char][direction]

    next_locations = []

    for d in deltas:
        next_location = (current_location[0] + d[0][0], current_location[1] + d[0][1])
        next_direction = d[1]

        if 0 <= next_location[0] < len(area) and 0 <= next_location[1] < len(area[0]):
            next_locations.append((next_location, next_direction))

    return next_locations


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    stripped = []

    for line in lines:
        stripped.append(line.strip())

    return stripped


if __name__ == "__main__":
    main()
