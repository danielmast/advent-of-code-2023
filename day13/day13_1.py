# extract patterns separately

# per pattern, compute the 'summary'
# summary = columns left of reflection + 100 * rows above reflection

# columns left of reflection:
# scan each column until 2 adjacent ones are the same

# same for rows

def main():
    patterns = read_file('input.txt')

    sum = 0

    i = 0
    for pattern in patterns:
        summary = get_summary(pattern)
        sum += summary
        print(i, summary)
        i += 1

    answer = sum
    print(f'The answer: {answer}')

def get_summary(pattern):
    c = get_reflecting_columns(pattern)
    r = get_reflecting_rows(pattern)

    return c + 100 * r


def get_reflecting_columns(pattern):
    for c in range(len(pattern[0]) - 1):
        column1 = get_column(pattern, c)
        column2 = get_column(pattern, c+1)
        if column1 == column2:
            if check_other_columns(pattern, c):
                return c + 1
    return 0


def check_other_columns(pattern, c):
    for i in range(c+1):
        if c + 1 + i >= len(pattern[0]):
            return True

        if get_column(pattern, c - i) != get_column(pattern, c + 1 + i):
            return False
    return True


def get_column(pattern, i):
    c = []
    for r in pattern:
        c.append(r[i])
    return c


def get_reflecting_rows(pattern):
    for r in range(len(pattern) - 1):
        if pattern[r] == pattern[r+1]:
            if check_other_rows(pattern, r):
                return r+1
    return 0


def check_other_rows(pattern, r):
    for i in range(r+1):
        if r + 1 + i >= len(pattern):
            return True

        if pattern[r-i] != pattern[r+1+i]:
            return False
    return True


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    patterns = []

    pattern = []
    for line in lines:
        line = line.strip()
        if line == '':
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)

    patterns.append(pattern)

    return patterns


if __name__ == "__main__":
    main()
