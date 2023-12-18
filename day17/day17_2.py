import heapq

# Shortest path (Dijkstra)
# But also record the last direction and the repetitions of that last direction
# while traversing, check if the path is valid

def main():
    lines = read_file('input.txt')

    start = (0, 0)
    end = (len(lines) - 1, len(lines[0]) - 1)

    A = {}
    X = [(0, start, 'r', 0)]

    while len(X) > 0:
        x_loss, x_node, x_direction, x_dirreps = heapq.heappop(X)

        if (x_node, x_direction, x_dirreps) in A:
            continue

        A[(x_node, x_direction, x_dirreps)] = x_loss

        if len(A) % 10000 == 0:
            print('A (', len(A), ') append: node:', x_node, 'direction:', x_direction, 'dirreps:', x_dirreps)

        for z_node in get_neighbours(x_node, lines):
            z_direction = get_direction(x_node, z_node)

            if z_direction == x_direction:
                z_dirreps = x_dirreps + 1
            else:
                z_dirreps = 1

            if (z_node, z_direction, z_dirreps) in A:
                continue

            if not is_valid_path(z_node, end, x_direction, x_dirreps, z_direction, z_dirreps):
                continue

            local_loss = int(lines[z_node[0]][z_node[1]])
            heapq.heappush(X, (x_loss + local_loss, z_node, z_direction, z_dirreps))

    min_answer = 1000000000000
    for a in A:
        if a[0] == end:
            if A[a] < min_answer:
                min_answer = A[a]

    answer = min_answer

    print(f'The answer: {answer}')


def is_valid_path(last_node, end, prev_direction, prev_dirreps, direction, dirreps):
    if reverse_direction(prev_direction) == direction:
        return False

    if last_node == end and dirreps < 4:
        return False

    if prev_direction == direction:
        return dirreps <= 10
    else:
        return prev_dirreps >= 4


def reverse_direction(direction):
    if direction == 'l':
        return 'r'
    if direction == 'r':
        return 'l'
    if direction == 'u':
        return 'd'
    if direction == 'd':
        return 'u'
    assert False


def get_direction(node1, node2):
    dy = node1[0] - node2[0]
    dx = node1[1] - node2[1]
    if dy == -1:
        return 'd'
    if dy == 1:
        return 'u'
    if dx == -1:
        return 'r'
    if dx == 1:
        return 'l'

    assert False


def get_neighbours(node, lines):
    neighbours = []
    if node[0] - 1 >= 0:
        neighbours.append((node[0] - 1, node[1]))

    if node[0] + 1 < len(lines):
        neighbours.append((node[0] + 1, node[1]))

    if node[1] - 1 >= 0:
        neighbours.append((node[0], node[1] - 1))

    if node[1] + 1 < len(lines[0]):
        neighbours.append((node[0], node[1] + 1))

    return neighbours


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    stripped = []

    for line in lines:
        stripped.append(line.strip())

    return stripped


if __name__ == "__main__":
    main()
