from collections import defaultdict


def main():
    bricks, max_x, max_y, max_low_end_z = read_file('input.txt')

    # Lowest (z) Point Possible for each x, y position
    lpp = defaultdict(int)

    for i in range(max_x + 1):
        for j in range(max_y + 1):
            lpp[(i, j)] = 1

    pass

    # The drop
    for z in range(1, max_low_end_z + 1):
        for brick in bricks:
            low_end, high_end = brick
            if low_end[2] == z:
                drop_dist = 1000000
                for i in range(low_end[0], high_end[0] + 1):
                    for j in range(low_end[1], high_end[1] + 1):
                        for k in range(low_end[2], high_end[2] + 1):
                            drop_dist = min(drop_dist, k - lpp[i, j])

                low_end[2] -= drop_dist
                high_end[2] -= drop_dist

                for i in range(low_end[0], high_end[0] + 1):
                    for j in range(low_end[1], high_end[1] + 1):
                        lpp[(i, j)] = high_end[2] + 1

    # Find supporters
    sup = defaultdict(set)
    # sup[3] = {4, 5} means: 3 is supported by 4 and 5

    for b1 in range(len(bricks) - 1):
        brick1 = bricks[b1]
        for b2 in range(b1 + 1, len(bricks)):
            brick2 = bricks[b2]

            b1le, b1he = brick1
            b2le, b2he = brick2

            for b1_x in range(b1le[0], b1he[0] + 1):
                for b1_y in range(b1le[1], b1he[1] + 1):
                    for b1_z in range(b1le[2], b1he[2] + 1):
                        for b2_x in range(b2le[0], b2he[0] + 1):
                            for b2_y in range(b2le[1], b2he[1] + 1):
                                for b2_z in range(b2le[2], b2he[2] + 1):
                                    if b1_x == b2_x and b1_y == b2_y:
                                        if b1_z - b2_z == 1:
                                            sup[b1].add(b2)
                                        elif b2_z - b1_z == 1:
                                            sup[b2].add(b1)

    # A brick can be disintegrated, if it is NOT listed in any other brick's supporters list as the only brick
    dis = []
    for b1 in range(len(bricks)):
        loose = True
        for b2 in range(len(bricks)):
            if sup[b2] == {b1}:
                assert b1 != b2
                loose = False
                break

        if loose:
            dis.append(b1)

    answer1 = len(dis)
    print('Answer part 1:', answer1)

    # Part 2
    sum = 0

    for b1 in range(len(bricks)):
        is_falling = {b1}
        more_has_fallen = True
        while more_has_fallen:
            more_has_fallen = False

            for b2 in range(len(bricks)):
                if b1 == b2:
                    continue
                # if b2 is supported only by the falling pieces, b2 is gonna fall
                if sup[b2] != set() and len(sup[b2] - is_falling) == 0 and b2 not in is_falling:
                    is_falling.add(b2)
                    more_has_fallen = True

        sum += len(is_falling) - 1

    answer2 = sum
    print(f'Answer part 2: {answer2}')


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    bricks = []
    max_x = -1
    max_y = -1
    max_low_end_z = 0

    for line in lines:
        line = line.strip()
        low_end, high_end = line.split('~')
        low_end = low_end.split(',')
        low_end = list(map(int, low_end))
        high_end = high_end.split(',')
        high_end = list(map(int, high_end))
        assert low_end[2] <= high_end[2]  # check if the left part is always at least as low as the right part
        bricks.append([low_end, high_end])

        max_x = max(max_x, low_end[0], high_end[0])
        max_y = max(max_y, low_end[1], high_end[1])
        max_low_end_z = max(max_low_end_z, low_end[2])

    return bricks, max_x, max_y, max_low_end_z


if __name__ == "__main__":
    main()
