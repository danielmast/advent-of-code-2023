from collections import defaultdict
import re

# per card
# - get the winning numbers
# - get your numbers
# - count the number of numbers from your numbers that occur in the winning numbers

# Iterate over the cards
# Count per card number how much you have won of it (in a dict)
# Iterate over the won_copies and sum

def main():
    lines = read_file('input.txt')

    copies_won = defaultdict(int)

    for line in lines:
        s = re.search('Card (.*):(.*)\|(.*)', line)
        game = int(s[1])
        copies_won[game] += 1
        winning_numbers = get_numbers_from_scratch_list(s[2])
        your_numbers = get_numbers_from_scratch_list(s[3])
        matches_count = get_matches_count(your_numbers, winning_numbers)

        print(game, matches_count, matches_count)

        for i in range(game + 1, game + 1 + matches_count):
            copies_won[i] += 1 * copies_won[game]

    sum = 0
    for game in copies_won:
        sum += copies_won[game]

    answer = sum
    print(f'The answer: {answer}')

def get_numbers_from_scratch_list(scratch_list):
    string_numbers = scratch_list.split(' ')
    new_string_numbers = []
    for sn in string_numbers:
        if sn.isdigit():
            new_string_numbers.append(int(sn))

    return new_string_numbers

def get_matches_count(your_numbers, winning_numbers):
    count = 0
    for your_number in your_numbers:
        if your_number in winning_numbers:
            count += 1

    return count


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    return lines


if __name__ == "__main__":
    main()
