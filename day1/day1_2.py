def main():
    lines = read_file('input.txt')

    number_strings = {
        "one": [1, -1, -1],
        "two": [2, -1, -1],
        "three": [3, -1, -1],
        "four": [4, -1, -1],
        "five": [5, -1, -1],
        "six": [6, -1, -1],
        "seven": [7, -1, -1],
        "eight": [8, -1, -1],
        "nine": [9, -1, -1]
    }

    sum = 0

    for line in lines:
        first = None
        first_loc = 100000000000000000000
        last = None
        last_loc = -1

        i = 0
        for el in line:
            if el.isdigit():
                if first is None:
                    first = el
                    first_loc = i
                    last = el
                    last_loc = i
                else:
                    last = el
                    last_loc = i

            i += 1

        for s in number_strings:
            number_strings[s][1] = line.find(s)
            number_strings[s][2] = line.rfind(s)

            if number_strings[s][1] != -1:
                if first is None or number_strings[s][1] < first_loc:
                    first = number_strings[s][0]
                    first_loc = number_strings[s][1]

            if number_strings[s][2] != -1:
                if last is None or number_strings[s][2] > last_loc:
                    last = number_strings[s][0]
                    last_loc = number_strings[s][2]

        d = int(str(first) + str(last))
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
