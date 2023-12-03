from collections import defaultdict
import re

def main():
    lines = read_file('input.txt')

    sum = 0

    els = defaultdict(lambda: defaultdict(str))
    nums = defaultdict(str)

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

    nums_static = dict(nums)

    for coords in nums_static:
        y, x = coords.split(',')
        y = int(y)
        x = int(x)
        number = nums[coords]
        print(number, 'adjacent =', adjacent(coords, nums, els, lines))
        if adjacent(coords, nums, els, lines):

            sum += number

    answer = sum
    print(f'The answer: {answer}')


def adjacent(coords, nums, els, lines):
    y, x = coords.split(',')
    y = int(y)
    x = int(x)
    number = nums[coords]

    if number == 739:
        print('debug')

    for i in range(x - 1, x + len(str(number)) + 1):
        if els[y - 1][i] not in ('', '.', '\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print('adjacent', y - 1, i)
            return True

        if els[y + 1][i] not in ('', '.', '\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print('adjacent', y+1, i)
            return True

    if els[y][x - 1] not in ('', '.', '\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        print('adjacent', y, x-1)
        return True
    if els[y][x + len(str(number))] not in ('', '.', '\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        print('adjacent', y, x + len(str(number)) + 1)
        return True

    return False


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    return lines


if __name__ == "__main__":
    main()
