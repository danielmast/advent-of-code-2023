def main():
    lines = read_file('input.txt')

    sum = 0

    for line in lines:
        first = None
        last = None
        for el in line:
            if el.isdigit():
                if first is None:
                    first = el
                    last = el
                else:
                    last = el

        d = int(first + last)
        sum += d
        print(d)

    answer = sum
    print(f'The answer: {answer}')


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    return lines


if __name__ == "__main__":
    main()
