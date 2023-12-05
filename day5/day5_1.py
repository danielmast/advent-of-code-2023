from collections import defaultdict
import re

def main():
    seeds, maps = read_file('input.txt')
    print()

    min_location = 10000000000000000000000000

    for seed in seeds:
        print('Seed: ', seed)
        current = seed
        for map in maps:
            found = False

            for source in maps[map]:
                destination = maps[map][source][0]
                range = maps[map][source][1]

                if source <= current <= source + range:
                    current = destination + (current - source)
                    found = True
                    break

            if not found:
                pass

        location = current
        print('location: ', location)
        min_location = min(min_location, location)

    answer = min_location
    print(f'The answer: {answer}')

def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    seeds = list(map(int, re.search('seeds: (.*)', lines[0])[1].split()))
    maps = defaultdict(lambda: defaultdict(tuple))

    for line in lines[2:]:
        try:
            s = re.search('(.*) map:', line)
            current_map_description = s[1]
            print(current_map_description)
            continue
        except TypeError:
            pass

        if line == '\n':
            continue

        nums = list(map(int, line.split(' ')))
        if len(nums) == 3:
            print(nums)
            maps[current_map_description][nums[1]] = (nums[0], nums[2])


    return seeds, maps


if __name__ == "__main__":
    main()
