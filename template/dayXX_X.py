from collections import defaultdict
import re
from math import floor


def main():
    lines = read_file('input.txt')

    sum = 0

    for line in lines:
       pass

    answer = sum
    print(f'The answer: {answer}')

def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    return lines


if __name__ == "__main__":
    main()
