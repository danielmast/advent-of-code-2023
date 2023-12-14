# Store all locs of rounded rocks
# Store all locs of cube-shaped rocks

# Iterate over the rounded rocks
# Iterate over the rows of its column, from the loc of the rounded rock, upwards, until you meet a 'O' or '#'
# Replace the rounded rock to under that obstacle
# Add the tilted rock to the new list

# Compute the load by iterating over the new rounded rocks and summing the rows (with some inversion, etc)

def main():
    rounded_rocks, cube_rocks, lines = read_file('input.txt')
    tilted_rounded_rocks = []

    # cube_rocks.sort(key=lambda c: c[0] * 100 + c[1])

    for line in lines:
        for c in line:
            if line == lines[2]:
                pass
            print(c, end='')
        print()
    print()

    for rounded_rock in rounded_rocks:
        c = rounded_rock[1]
        is_moved = False
        for i in range(rounded_rock[0] + 1):
            r = rounded_rock[0] - i

            if r == 0 or lines[r-1][c] in ('#', 'O'):


                if r != rounded_rock[0]:
                    # add rock to new position
                    lines[r] = lines[r][:c] + 'O' + lines[r][c+1:]

                    # remove rock from old position
                    lines[rounded_rock[0]] = lines[rounded_rock[0]][:c] + '.' + lines[rounded_rock[0]][c + 1:]

                tilted_rounded_rock = (r, c)
                tilted_rounded_rocks.append(tilted_rounded_rock)

                print('Moved', rounded_rock, 'to', tilted_rounded_rock)
                is_moved = True
                break

        if not is_moved:
            print('Not moved:', rounded_rock)
            tilted_rounded_rocks.append(rounded_rock)

        for line in lines:
            print(line)
        print()


    print('Lines:')
    for line in lines:
        print(line)
    print()

    sum = 0

    for tilted_rounded_rock in tilted_rounded_rocks:
        y = tilted_rounded_rock[0]
        sum += len(lines) - y

    answer = sum
    print(f'The answer: {answer}')

def print_rocks(cube_rocks, tilted_rounded_rocks, lines):
    R = len(lines)
    C = len(lines[0])

    for r in range(R):
        for c in range(C):
            cube_rock = None
            tilted_rounded_rock = None
            for cr in cube_rocks:
                if cr[0] == r and cr[1] == c:
                    cube_rock = cr
                    break

            for trr in tilted_rounded_rocks:
                if type(trr) is int:
                    print('debug')
                if trr[0] == r and trr[1] == c:
                    tilted_rounded_rock = trr
                    break

            if cube_rock is not None:
                print('#', end='')
            elif tilted_rounded_rock is not None:
                print('O', end='')
            else:
                print('.', end='')
        print()


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    rounded_rocks = []
    cube_rocks = []

    R = len(lines)
    C = len(lines[0].strip())

    for r in range(R):
        for c in range(C):
            if lines[r][c] == 'O':
                rounded_rocks.append((r, c))
            elif lines[r][c] == '#':
                cube_rocks.append((r, c))

    stripped = []
    for line in lines:
        stripped.append(line.strip())

    return rounded_rocks, cube_rocks, stripped


if __name__ == "__main__":
    main()
