# Create function to compute (per line) sizes out of characters

# Use character line as input and recursively fill in the ?'s until all are filled in: then compute sizes
# If it matches the correct sizes, return total + 1

def main():
    lines = read_file('input.txt')

    assert get_sizes('#.#.###') == [1,1,3]
    assert get_sizes('.#.###.#.######') == [1, 3, 1, 6]
    assert get_sizes('#....######..#####.') == [1, 6, 5]

    assert replace('.??..??...?##.', 5, '.') == '.??...?...?##.'

    sum = 0
    for i, line in enumerate(lines):
        count = get_arrangements(line[0], line[1])
        sum += count
        print(i, line, 'count:', count)

    answer = sum
    print(f'The answer: {answer}')


def replace(input, index, char):
    return input[:index] + char + input[index + 1:]


def get_arrangements(chars, sizes):

    i = chars.find('?')

    if i == -1:
        if get_sizes(chars) == sizes:
            return 1
        return 0

    return get_arrangements(replace(chars, i, '#'), sizes) + get_arrangements(replace(chars, i, '.'), sizes)


def get_sizes(chars):
    if '?' in chars:
        assert False

    sizes = []

    in_contig = False

    for c in chars:
        if c == '#':
            if in_contig:
                sizes[-1] += 1
            else:
                in_contig = True
                sizes.append(1)
        else:
            in_contig = False

    return sizes


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    output = []

    for line in lines:
        line = line.strip()

        chars, sizes = line.split(' ')
        sizes = sizes.split(',')
        sizes = list(map(int, sizes))

        output.append((chars, sizes))

    return output


if __name__ == "__main__":
    main()
