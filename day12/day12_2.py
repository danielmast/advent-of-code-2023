from collections import defaultdict


def main():
    lines = read_file('input.txt')

    assert get_sizes('#.#.###') == [1,1,3]
    assert get_sizes('.#.###.#.######') == [1, 3, 1, 6]
    assert get_sizes('#....######..#####.') == [1, 6, 5]

    assert replace('.??..??...?##.', 5, '.') == '.??...?...?##.'

    assert unfold('.#', [1]) == ('.#?.#?.#?.#?.#', [1,1,1,1,1])

    assert get_start_of_right('#.#') == 2
    assert get_start_of_right('#.?') == 2
    assert get_start_of_right('#..#') == 3
    assert get_start_of_right('#..?') == 3
    assert get_start_of_right('#..') == 3

    assert occur_count('..?.?', '#') == 0
    assert occur_count('..?.#', '#') == 1
    assert occur_count('.#?#', '#') == 2

    assert get_arrangements('#.?', [1], defaultdict(lambda: -1)) == 1

    sum = 0
    for i, line in enumerate(lines):
        chars = line[0]
        sizes = line[1]
        unfolded = unfold(chars, sizes)
        memo = defaultdict(lambda: -1)
        count = get_arrangements(unfolded[0], unfolded[1], memo)
        sum += count
        print(i, unfolded, 'count:', count, len(memo))

    answer = sum
    print(f'The answer: {answer}')


def replace(input, index, char):
    return input[:index] + char + input[index + 1:]


def unfold(chars, sizes):
    unfolded_chars = ''
    for i in range(5):
        unfolded_chars += chars + '?'

    unfolded_chars = unfolded_chars[:-1]
    return unfolded_chars, sizes * 5


# Compute the number of options more efficiently (without traversing all of them)
# When a dot is found, you can separately compute the number of arrangements after the dot
# and multiply with the number of arrangements before the dot
def get_arrangements(chars, sizes, memo):
    if sizes == []:
        if '#' in chars:
            return 0
        return 1

    # No solution if: The string length is smaller than the minimal length of characters required to match the sizes
    if len(chars) < sum(sizes) + len(sizes) - 1:
        return 0

    # No solution if: The string contains more #'s than the sum of sizes
    if occur_count(chars, '#') > sum(sizes):
        return 0

    # No solution if: The string only contains dots, but sizes implied that it should contain #'s
    if occur_count(chars, '.') == len(chars) and sizes != []:
        return 0

    # Check if this combination of chars and sizes was computed before
    m = memo[get_key(chars, sizes)]
    if m != -1:
        return m

    dot_i = chars.find('.')

    # If a dot is found
    if dot_i != -1:
        product_sum = 0

        # For efficiency: If multiple dots are adjacent, only select the part on the right that starts with '#' or '?'
        start_of_right = get_start_of_right(chars)

        # Iterate over the different possible splits, left and right of the dot
        # Some splits won't be feasible, but those will quickly be terminated by one of the 'No solution if' checks above
        for s in range(len(sizes) + 1):
            res_left = get_arrangements(chars[:dot_i], sizes[:s], memo)
            res_right = get_arrangements(chars[start_of_right:], sizes[s:], memo)
            product_sum += res_left * res_right

        memo[get_key(chars, sizes)] = product_sum
        return product_sum

    # ... no dot is found

    i = chars.find('?')

    # If no question mark is found
    if i == -1:
        # Compute if the string matches with the sizes
        if get_sizes(chars) == sizes:
            return 1
        return 0  # this line is probably never reached


    # ... a question mark is found

    # Compute the counts for replacing the '?' with both possible values
    res_left = get_arrangements(replace(chars, i, '#'), sizes, memo)
    res_right = get_arrangements(replace(chars, i, '.'), sizes, memo)

    memo[get_key(chars, sizes)] = res_left + res_right

    return res_left + res_right


def get_key(chars, sizes):
    return chars + '|' + ','.join(list(map(str, sizes)))


def occur_count(chars, char):
    count = 0
    for c in chars:
        if c == char:
            count += 1
    return count


def get_start_of_right(chars):
    dot_i = chars.find('.')
    dash_i = chars[dot_i+1:].find('#')
    qm_i = chars[dot_i+1:].find('?')

    if dash_i == -1:
        if qm_i == -1:
            return len(chars)
        return qm_i + dot_i + 1
    elif qm_i == -1:
        return dash_i + dot_i + 1

    return min(dash_i + dot_i + 1, qm_i + dot_i + 1)


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
