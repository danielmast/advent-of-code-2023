# Start at the start
# Traverse through dots
# If new path start, add that to currents
# Find new unvisited neighbours
# For each current, keep track of length

def main():
    area = read_file('input.txt')

    R = len(area)
    C = len(area[0])

    start = (0, 1)
    end = (R - 1, C - 2)

    currents = [(start, None, 0)]

    while not is_all_end(currents, end):
        new_currents = []
        for current in currents:
            c, prev, l = current
            nbs = get_nbs(c, prev, area, R, C)

            for n in nbs:
                new_currents.append((n, c, l+1))

        currents = new_currents

    max_dist = 0
    for current in currents:
        max_dist = max(max_dist, current[2])

    answer = max_dist
    print(f'The answer: {answer}')


def is_all_end(currents, end):
    for c in currents:
        if c[0] != end:
            return False
    return True


def get_nbs(loc, prev, area, R, C):
    nbs = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx == 0 or dy == 0) and not (dx == 0 and dy == 0):
                n = (loc[0] + dy, loc[1] + dx)
                if 0 <= n[0] < R and 0 <= n[1] < C:
                    if n == prev:
                        continue

                    if area[n[0]][n[1]] == '.':
                        nbs.append(n)
                    elif area[n[0]][n[1]] == '>' and dx == 1:
                        nbs.append(n)
                    elif area[n[0]][n[1]] == '<' and dx == -1:
                        nbs.append(n)
                    elif area[n[0]][n[1]] == 'v' and dy == 1:
                        nbs.append(n)
                    elif area[n[0]][n[1]] == '^' and dy == -1:
                        nbs.append(n)
                    else:
                        pass
    return nbs


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    stripped = []
    for line in lines:
        stripped.append(line.strip())

    return stripped


if __name__ == "__main__":
    main()
