
# per history (line):
# set current = history
# diffs = create a list of the differences in the current list
# store a list of list diffs
# check if all zeroes, if not continue
# at the end, add the last number of every diff layer to the right last number in the history lines
#
# and then sum all history extra numbers

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
            left = all_diffs[i_rev][-1]
            right = all_diffs[i_rev - 1][-1]
            sum_of_lasts = left + right
            print('i_rev:', i_rev, 'left:', left, 'right:', right, 'sum_of_lasts:', sum_of_lasts)
            all_diffs[i_rev - 1].append(sum_of_lasts)
        prediction = sum_of_lasts
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
