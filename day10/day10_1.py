import math

# Store all characters in a 2d list
# Start at S
# Look at all 4 surrounding chars, pick one that is connected
# Init the pipe: add S and 1 neighbour
# Then start iterating over the last element of each pipe
# Look at its unvisited (!) neighbours
# If an unvisited neighbour is connected with the pipe, add to the pipe
# Stop if no new unvisited neighbours are found, or when S is found

# When S is found, compute the length of the pipeline and divide by 2, round up

def main():
    lines = read_file('input.txt')

    S_loc = None

    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char == 'S':
                S_loc = (x, y)

    pipe = [S_loc]

    while True:
        current = pipe[-1]

        north = get_north(current)
        south = get_south(current)
        west = get_west(current)
        east = get_east(current)

        if can_go_north(current, lines) and (len(pipe) == 1 or north != pipe[-2]):
            pipe.append(north)
        elif can_go_south(current, lines) and (len(pipe) == 1 or south != pipe[-2]):
            pipe.append(south)
        elif can_go_west(current, lines) and (len(pipe) == 1 or west != pipe[-2]):
            pipe.append(west)
        elif can_go_east(current, lines) and (len(pipe) == 1 or east != pipe[-2]):
            pipe.append(east)
        elif pipe[0] in (north, south, west, east):
            break
        else:
            exit('unexpected')

    answer = math.ceil(len(pipe) / 2)
    print(f'The answer: {answer}')

def can_go_north(xy, lines):
    return get(xy, lines) in ('S', '|', 'J', 'L') and get(get_north(xy), lines) in ('|', '7', 'F')

def can_go_south(xy, lines):
    return get(xy, lines) in ('S', '|', 'F', '7') and get(get_south(xy), lines) in ('|', 'J', 'L')

def can_go_west(xy, lines):
    return get(xy, lines) in ('S', '-', '7', 'J') and get(get_west(xy), lines) in ('-', 'F', 'L')

def can_go_east(xy, lines):
    return get(xy, lines) in ('S', '-', 'F', 'L') and get(get_east(xy), lines) in ('-', 'J', '7')

def get(xy, lines):
    if xy[0] < 0 or xy[0] > len(lines[0]):
        return None
    if xy[1] < 0 or xy[1] > len(lines):
        return None
    return lines[xy[1]][xy[0]]

def get_east(xy):
    return xy[0] + 1, xy[1]

def get_west(xy):
    return xy[0] - 1, xy[1]

def get_north(xy):
    return xy[0], xy[1] - 1

def get_south(xy):
    return xy[0], xy[1] + 1


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    return lines

if __name__ == "__main__":
    main()
