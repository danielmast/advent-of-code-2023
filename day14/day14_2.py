# Create separate function to tilt the platform in a specific direction
# Create a loop that tilts a billion times, repeating the tilt function 4 times for each direction
# Store each platform state with its iteration
# Check after each cycle if the state was seen before
# If so, terminate the outer loop and compute what the eventual state will be

def main():
    platform = read_file('input.txt')
    prev_platforms = [platform]

    print_platform(platform)

    total_cycles = 1000000000

    for i in range(total_cycles):
        platform = tilt(platform, 'north')
        print_platform(platform)
        print('Total load:', get_total_load(platform))
        platform = tilt(platform, 'west')
        print_platform(platform)
        print('Total load:', get_total_load(platform))
        platform = tilt(platform, 'south')
        print_platform(platform)
        print('Total load:', get_total_load(platform))
        platform = tilt(platform, 'east')
        print_platform(platform)
        print('Total load:', get_total_load(platform))

        hsb = has_seen_before(prev_platforms, platform)
        if hsb is not None:
            print('Has seen before:', hsb)
            remaining_cycles = total_cycles - i
            cycles_until_repeat = i - hsb
            offset = remaining_cycles % cycles_until_repeat
            print('The answer:', get_total_load(prev_platforms[hsb + offset + 2]))
            break

        prev_platforms.append(platform)


def print_platform(platform):
    for r in platform:
        print(r)
    print()


def get_total_load(platform):
    total_load = 0
    rounded_rocks = get_rounded_rocks(platform)
    for rounded_rock in rounded_rocks:
        y = rounded_rock[0]
        total_load += len(platform) - y
    return total_load


def has_seen_before(prev_platforms, platform):
    for i, prev_platform in enumerate(prev_platforms):
        if equals(platform, prev_platform):
            return i

    return None


def equals(platform1, platform2):
    for r in range(len(platform1)):
        if platform1[r] != platform2[r]:
            return False
    return True


# Rotate platform 45 degrees to the right
def rotate_right(platform):
    rotated = []

    R = len(platform)
    C = len(platform[0])

    # Iterate over every column (left to right)
    for c in range(C):
        row_string = ''
        # Iterate over every row (bottom to top)
        for i in range(R):
            r = R - i - 1
            row_string += platform[r][c]

        rotated.append(row_string)

    return rotated


def tilt(platform, direction):
    platform = platform.copy()

    if direction == 'south':
        platform = rotate_right(platform)
        platform = rotate_right(platform)
    elif direction == 'west':
        platform = rotate_right(platform)
    elif direction == 'east':
        platform = rotate_right(platform)
        platform = rotate_right(platform)
        platform = rotate_right(platform)

    # the below algorithm was made for tilting to the north

    rounded_rocks = get_rounded_rocks(platform)

    for rounded_rock in rounded_rocks:
        c = rounded_rock[1]
        for i in range(rounded_rock[0] + 1):
            r = rounded_rock[0] - i

            if r == 0 or platform[r - 1][c] in ('#', 'O'):

                if r != rounded_rock[0]:
                    # add rock to new position
                    platform[r] = platform[r][:c] + 'O' + platform[r][c + 1:]

                    # remove rock from old position
                    platform[rounded_rock[0]] = platform[rounded_rock[0]][:c] + '.' + platform[rounded_rock[0]][c + 1:]

                break

    if direction == 'south':
        platform = rotate_right(platform)
        platform = rotate_right(platform)
    elif direction == 'west':
        platform = rotate_right(platform)
        platform = rotate_right(platform)
        platform = rotate_right(platform)
    elif direction == 'east':
        platform = rotate_right(platform)

    return platform


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    platform = []
    for line in lines:
        platform.append(line.strip())

    return platform


def get_rounded_rocks(platform):
    rounded_rocks = []

    R = len(platform)
    C = len(platform[0])

    for r in range(R):
        for c in range(C):
            if platform[r][c] == 'O':
                rounded_rocks.append((r, c))

    return rounded_rocks


if __name__ == "__main__":
    main()
