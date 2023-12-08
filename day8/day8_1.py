from collections import defaultdict
def main():
    directions, nodes = read_file('input.txt')

    current = 'AAA'
    finish = 'ZZZ'

    steps = 0
    reached_finish = False
    while not reached_finish:
        for direction in directions:
            if direction == 'L':
                current = nodes[current][0]
            else:
                current = nodes[current][1]

            steps += 1

            if current == finish:
                reached_finish = True
                break


    answer = steps
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
