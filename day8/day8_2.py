import math
from collections import defaultdict

def main():
    directions, nodes = read_file('input.txt')

    print(directions)

    currents = []
    cycles = []
    for node in nodes:
        if node.endswith('A'):
            currents.append(node)
            cycles.append(-1)

    print(currents)

    steps = 0
    reached_finish = False
    while not reached_finish:
        for direction in directions:
            steps += 1
            for i, current in enumerate(currents):
                if direction == 'L':
                    currents[i] = nodes[current][0]
                else:
                    currents[i] = nodes[current][1]

                if currents[i].endswith('Z'):
                    cycles[i] = steps / len(directions)
                    if -1 not in cycles:
                        reached_finish = True

    answer = int(math.prod(cycles) * len(directions))
    print(f'The answer: {answer}')

def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    nodes = defaultdict()

    directions = lines[0].strip()

    for line in lines[2:]:
        node, to = line.split('=')
        node = node.strip()
        left = to[2:5]
        right = to[7:10]
        nodes[node] = (left, right)

    return directions, nodes


if __name__ == "__main__":
    main()
