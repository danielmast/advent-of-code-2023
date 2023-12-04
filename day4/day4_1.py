from collections import defaultdict
import re
from math import floor


# per card
# - get the winning numbers
# - get your numbers
# - count the number of numbers from your numbers that occur in the winning numbers
# - 2^count
# - sum up

def main():
    lines = read_file('input.txt')

    sum = 0

    for line in lines:
        s = re.search('Card (.*):(.*)\|(.*)', line)
        game = int(s[1])
        winning_numbers = get_numbers_from_scratch_list(s[2])
        your_numbers = get_numbers_from_scratch_list(s[3])
        matches_count = get_matches_count(your_numbers, winning_numbers)
        card_score = get_card_score(matches_count)
        print(game, matches_count, card_score)
        sum += card_score

    answer = sum
    print(f'The answer: {answer}')

def get_numbers_from_scratch_list(scratch_list):
    string_numbers = scratch_list.split(' ')
    new_string_numbers = []
    for sn in string_numbers:
        if sn.isdigit():
            new_string_numbers.append(int(sn))

    return new_string_numbers

def get_card_score(matches_count):
    if matches_count == 0:
        return 0

    return floor(2 ** matches_count / 2)

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
