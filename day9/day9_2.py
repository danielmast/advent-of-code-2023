def main():
    lines = read_file('input.txt')

    sum = 0

    for line in lines:
        all_diffs = []
        history = list(map(int, line.split()))
        all_diffs.append(history)

        current = history

        all_zeroes = False
        while not all_zeroes:
            print('current', current)
            diffs = []
            for i in range(len(current) - 1):
                diffs.append(current[i+1] - current[i])
            print('diffs', diffs)

            all_diffs.append(diffs)

            all_zeroes = True
            for d in diffs:
                if d != 0:
                    all_zeroes = False

            current = diffs

        print(all_diffs)

        for i in range(len(all_diffs) - 1):
            i_rev = len(all_diffs) - i - 1
            left = all_diffs[i_rev][0]
            right = all_diffs[i_rev - 1][0]
            diff_of_firsts = right - left
            print('i_rev:', i_rev, 'left:', left, 'right:', right, 'sum_of_lasts:', diff_of_firsts)
            all_diffs[i_rev - 1].insert(0, diff_of_firsts)
        prediction = diff_of_firsts
        print('prediction', prediction)
        sum += prediction

    answer = sum
    print(f'The answer: {answer}')

def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    return lines


if __name__ == "__main__":
    main()
