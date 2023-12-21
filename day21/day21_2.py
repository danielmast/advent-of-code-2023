# Get locs of steps for < 500 steps

# cycle, steps, locs
# 1, 65, 3896
# 2, 196, 34617
# 3, 327, 95900
# 4, 458, 187745

# The diff of the diff between step x and step x + 131 is constant (where 131 is the width and length of the input)
# Wolfram alpha:
# InterpolatingPolynomial[{{65, 3896}, {196, 34617}, {327, 95900},{458,187745}}, x]
# Result = ( (15281(x-196)/17161 + 30721/131 )(x - 65) + 3896
# Use x = 26501365 as input
# Output = 625382480005896 = correct answer of day 21.2

def main():
    start, R, C, area = read_file('input.txt')

    prev_locs = set()
    prev_locs.add(start)

    for i in range(1, 500):
        if i % 10 == 0:
            print(i)

        locs = set()
        for loc in list(prev_locs):
            nbs = get_nbs(loc, area, R, C)

            for n in nbs:
                locs.add(n)

        # print_area(fill_area(area, locs, R, C))
        print('i:', i)
        # print(locs)
        print('len: ',len(locs))
        print()

        prev_locs = locs

    answer = len(prev_locs)
    print(f'The answer: {answer}')


def fill_area(area, locs, R, C):
    filled = []
    for r in range(R):
        line = ''
        for c in range(C):
            if (r, c) in locs:
                line += '0'
            else:
                if area[r][c] == '.':
                    line += ','
                else:
                    line += area[r][c]
        filled.append(line)
    return filled


def print_area(area):
    for line in area:
        print(line)
    print()


def get_nbs(loc, area, R, C):
    nbs = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx == 0 or dy == 0) and not (dx == 0 and dy == 0):
                n = (loc[0] + dy, loc[1] + dx)
                if area[n[0] % R][n[1] % C] != '#':
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
