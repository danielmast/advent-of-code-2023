from collections import defaultdict
import re

def main():
    lines = read_file('input.txt')

    sum = 0

    els = defaultdict(lambda: defaultdict(str))
    nums = defaultdict(str)
    stars = defaultdict(str)

    for i, line in enumerate(lines):
        isfirst = True

        for j, c in enumerate(line):
            els[i][j] = c

            if c.isdigit() and isfirst:
                number = int(re.findall(r'\d+', line[j:])[0])
                nums[str(i) + ',' + str(j)] = number
                isfirst = False
            elif not c.isdigit():
                isfirst = True

            if c == '*':
                stars[str(i) + ',' + str(j)] = '*'

    nums_static = dict(nums)

    for star_coords in stars:
        star_y, star_x = star_coords.split(',')
        star_y = int(star_y)
        star_x = int(star_x)

        adjacent_numbers = []

        for num_coords in nums_static:
            num_y, num_x = num_coords.split(',')
            num_y = int(num_y)
            num_x = int(num_x)
            number = nums[num_coords]

            if adjacent(star_y, star_x, num_y, num_x, number):
                adjacent_numbers.append(number)


        if len(adjacent_numbers) == 2:
            sum += adjacent_numbers[0] * adjacent_numbers[1]
        elif len(adjacent_numbers) > 2:
            print('debug')

    answer = sum
    print(f'The answer: {answer}')


def adjacent(star_y, star_x, num_y, num_x, number):
    if abs(star_y - num_y) <= 1:
        for i in range(num_x, num_x + len(str(number))):
            if abs(star_x - i) <= 1:
                return True

    return False


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    return lines


if __name__ == "__main__":
    main()
