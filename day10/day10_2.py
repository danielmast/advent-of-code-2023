# You can simply divide the clouds in 2 sets:
# left of the pipe, and right of the pipe
# one of them is inside, the other is outside

# How to construct the clouds:
# left_clouds = list of lists of tuples (locations) . initially empty
# right_clouds = list of lists of tuples (locations) . initially empty

# traverse along the pipeline
# for each pipe part, determine the 2 adjacent tiles that are not its pipe neighbours
# decide for each tile to add to left or right cloud

# After the pipe is traversed, complete the clouds with all the tiles that are not directly adjacent to the pipe
# Iterate over the first set of (adjacent) cloud tiles and recursively construct a set of non-adjacent cloud tiles

# try both cloud lengths as answer =)

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

    # Part 2 :

    # How to construct the clouds:
    # left_clouds = list of tuples (locations) . initially empty
    left_adj_cloud = []
    # right_clouds = list of tuples (locations) . initially empty
    right_adj_cloud = []

    # - | F J 7 L .

    # Current part type -> direction (relative to previous part type) -> cloud neighbour left or right
    lr = {
        '-': {'W': {'N': 'R', 'S': 'L'}, 'E': {'N': 'L', 'S': 'R'}},
        '|': {'N': {'W': 'L', 'E': 'R'}, 'S': {'W': 'R', 'E': 'L'}},
        'F': {'N': {'N': 'L', 'W': 'L'}, 'W': {'N': 'R', 'W': 'R'}},
        'J': {'S': {'S': 'L', 'E': 'L'}, 'E': {'S': 'R', 'E': 'R'}},
        '7': {'N': {'N': 'R', 'E': 'R'}, 'E': {'N': 'L', 'E': 'L'}},
        'L': {'S': {'S': 'R', 'W': 'R'}, 'W': {'S': 'L', 'W': 'L'}}
    }

    # traverse along the pipeline
    for i, pipe_part in enumerate(pipe):
        # for each pipe part, determine the 2 adjacent tiles that are not its pipe neighbours
        # decide for each tile to add to left or right cloud
        # By comparing the current and previous pipe part (to get the direction), and the pipe part type itself

        if i == 0:
            continue

        dir = get_dir(pipe[i-1], pipe_part)

        for cloud_dir in lr[get(pipe_part, lines)][dir]:
            value = lr[get(pipe_part, lines)][dir][cloud_dir]

            list_to_add_to = None
            if value == 'L':
                list_to_add_to = left_adj_cloud
            elif value == 'R':
                list_to_add_to = right_adj_cloud
            else:
                exit('unexpected')

            if cloud_dir == 'N' and get_north(pipe_part) not in pipe and get_north(pipe_part) not in list_to_add_to:
                list_to_add_to.append(get_north(pipe_part))
            elif cloud_dir == 'S' and get_south(pipe_part) not in pipe and get_south(pipe_part) not in list_to_add_to:
                list_to_add_to.append(get_south(pipe_part))
            elif cloud_dir == 'W' and get_west(pipe_part) not in pipe and get_west(pipe_part) not in list_to_add_to:
                list_to_add_to.append(get_west(pipe_part))
            elif cloud_dir == 'E' and get_east(pipe_part) not in pipe and get_east(pipe_part) not in list_to_add_to:
                list_to_add_to.append(get_east(pipe_part))


        print('i:', i)


    # After the pipe is traversed, complete the clouds with all the tiles that are not directly adjacent to the pipe
    # Iterate over the first set of (adjacent) cloud tiles and recursively construct a set of non-adjacent cloud tiles
    left_cloud = left_adj_cloud.copy()

    for adj_cloud_part in left_adj_cloud:
        add_neighbours_to_cloud(adj_cloud_part, pipe, left_cloud, 0, lines)

    print('left cloud length:', len(left_cloud))

    right_cloud = right_adj_cloud.copy()
    for adj_cloud_part in right_adj_cloud:
        add_neighbours_to_cloud(adj_cloud_part, pipe, right_cloud, 0, lines)

    print('right cloud length:', len(right_cloud))


def add_neighbours_to_cloud(current, pipe, cloud, depth, lines):
    #print('depth:', depth)

    if depth == 600:
        # this is a hack: expecting that other cloud parts will traverse all the other cloud parts
        # this is to prevent a stack overflow
        # it turned out to work
        return

    neighbours = [get_north(current), get_south(current), get_west(current), get_east(current)]
    for neighbour in neighbours:
        if get(neighbour, lines) is None:
            continue
        if neighbour not in pipe and neighbour not in cloud:
            cloud.append(neighbour)
            add_neighbours_to_cloud(neighbour, pipe, cloud, depth+1, lines)


def get_dir(prev_part, pipe_part):
    if get_east(prev_part) == pipe_part:
        return 'E'
    elif get_west(prev_part) == pipe_part:
        return 'W'
    elif get_north(prev_part) == pipe_part:
        return 'N'
    elif get_south(prev_part) == pipe_part:
        return 'S'

def can_go_north(xy, lines):
    return get(xy, lines) in ('S', '|', 'J', 'L') and get(get_north(xy), lines) in ('|', '7', 'F')

def can_go_south(xy, lines):
    return get(xy, lines) in ('S', '|', 'F', '7') and get(get_south(xy), lines) in ('|', 'J', 'L')

def can_go_west(xy, lines):
    return get(xy, lines) in ('S', '-', '7', 'J') and get(get_west(xy), lines) in ('-', 'F', 'L')

def can_go_east(xy, lines):
    return get(xy, lines) in ('S', '-', 'F', 'L') and get(get_east(xy), lines) in ('-', 'J', '7')

def get(xy, lines):
    if xy[0] < 0 or xy[0] >= len(lines[0]):
        return None
    if xy[1] < 0 or xy[1] >= len(lines):
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

    result = []

    for line in lines:
        result.append(line.strip())

    return result


if __name__ == "__main__":
    main()
