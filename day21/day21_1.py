# Loop 64 times:
# construct a new set everytime with the new locations
# Append the neighbours of the previous set

def main():
    start, R, C, area = read_file('input.txt')

    prev_locs = set()
    prev_locs.add(start)

    for i in range(64):
        locs = set()
        for loc in list(prev_locs):
            nbs = get_nbs(loc, area, R, C)
            for n in nbs:
                locs.add(n)

        #print(locs)
        prev_locs = locs

    answer = len(prev_locs)
    print(f'The answer: {answer}')

def get_nbs(loc, area, R, C):
    nbs = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx == 0 or dy == 0) and not (dx == 0 and dy == 0):
                n = (loc[0] + dy, loc[1] + dx)
                if 0 <= n[0] < R and 0 <= n[1] < C:
                    if area[n[0]][n[1]] != '#':
                        nbs.append(n)
    return nbs


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()
    start = None

    R = len(lines)
    C = len(lines[0].strip())

    stripped = []
    for r, line in enumerate(lines):
        line_str = line.strip()
        stripped.append(line_str)

        for c in range(C):
            if line_str[c] == 'S':
                start = (r, c)

    return start, R, C, stripped


if __name__ == "__main__":
    main()
