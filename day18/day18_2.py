from collections import defaultdict

def main():
    instructions = read_file('input.txt')

    position = (0, 0)

    min_x = 1000000000
    max_x = 0
    min_y = 1000000000
    max_y = 0

    trench = defaultdict(list)
    trench[position[0]].append(position[1])

    for instruction in instructions:
        direction, length = read_color(instruction)

        if direction == 'L':
            for dx in range(1, length+1):
                trench[position[0]].append(position[1] - dx)
        if direction == 'R':
            for dx in range(1, length+1):
                trench[position[0]].append(position[1] + dx)
        if direction == 'U':
            for dy in range(1, length+1):
                trench[position[0] - dy].append(position[1])
        if direction == 'D':
            for dy in range(1, length+1):
                trench[position[0] + dy].append(position[1])

        position = update_position(position, direction, length)

        min_x = min(min_x, position[1])
        max_x = max(max_x, position[1])
        min_y = min(min_y, position[0])
        max_y = max(max_y, position[0])

    sum = 0

    line_sums = defaultdict(int)
    for trench_y in trench:
        prev_sum = sum

        trench_xs = sorted(set(trench[trench_y]))
        sum += len(trench_xs)

        # Collect the horizontal edges. Determine for each if it's a peak
        # If so, do not invert the interior afterwards
        horizontal_edges = get_horizontal_edges(trench_xs)

        interior = True
        for i in range(len(trench_xs) - 1):
            adjacent_diff = trench_xs[i+1] - trench_xs[i]
            if adjacent_diff > 1:
                horizontal_edge = get_horizontal_edge(trench_xs[i], horizontal_edges)
                if horizontal_edge is not None and is_peak(trench_y, horizontal_edge, trench):
                    if not interior:
                        sum += adjacent_diff - 1
                else:
                    if interior:
                        sum += adjacent_diff - 1
                        interior = False
                    else:
                        interior = True

        line_sums[trench_y] = sum - prev_sum

    answer = sum
    print(f'The answer: {answer}')

def read_color(instruction):
    _, _, color = instruction
    color = color[2:-1]
    length = int(color[:-1], 16)

    dirs = {
        '0': 'R',
        '1': 'D',
        '2': 'L',
        '3': 'U'
    }

    direction = dirs[color[-1]]
    return direction, length

def is_peak(trench_y, horizontal_edge, trench):
    x_min = horizontal_edge[0]
    x_max = horizontal_edge[-1]

    if x_min in trench[trench_y - 1] and x_max in trench[trench_y - 1]:
        return True
    if x_min in trench[trench_y + 1] and x_max in trench[trench_y + 1]:
        return True
    return False


def get_horizontal_edge(x, horizontal_edges):
    for edge in horizontal_edges:
        if x in edge:
            return edge
    return None

def get_horizontal_edges(trench_xs):
    edges = []
    edge = []
    for i in range(len(trench_xs) - 1):
        if len(edge) == 0:
            edge.append(trench_xs[i])
        elif trench_xs[i] - edge[-1] == 1:
            edge.append(trench_xs[i])
        else:
            edges.append(edge)
            edge = [trench_xs[i]]

    if len(edge) > 0:
        edges.append(edge)

    cleaned = []
    for edge in edges:
        if len(edge) > 1:
            cleaned.append(edge)

    return cleaned

def update_position(position, direction, length):
    if direction == 'L':
        return (position[0], position[1] - length)
    if direction == 'R':
        return (position[0], position[1] + length)
    if direction == 'U':
        return (position[0] - length, position[1])
    if direction == 'D':
        return (position[0] + length, position[1])
    assert False
def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    instructions = []

    for line in lines:
        direction, length, color = line.strip().split()
        instructions.append((direction, int(length), color))

    return instructions


if __name__ == "__main__":
    main()
