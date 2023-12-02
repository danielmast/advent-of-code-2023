import re

def main():
    lines = read_file('input.txt')

    sum = 0

    max_red = 12
    max_green = 13
    max_blue = 14

    for line in lines:
        # example line = 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'

        s = re.search('Game (.*):(.*)', line)
        game = int(s[1])
        possible = True
        rest = s[2]
        splitted = rest.strip().split(';')
        print(splitted)

        for set in splitted:
            splitted_again = set.split(', ')
            print(splitted_again)

            for c in splitted_again:
                try:
                    blue = int(re.search('([0-9]*) blue', c)[1])

                    if (blue > max_blue):
                        possible = False
                except TypeError:
                    blue = None

                print('BLUE:', blue)

                try:
                    red = int(re.search('([0-9]*) red', c)[1])

                    if (red > max_red):
                        possible = False
                except TypeError:
                    red = None

                print('RED:', red)

                try:
                    green = int(re.search('([0-9]*) green', c)[1])

                    if (green > max_green):
                        possible = False
                except TypeError:
                    green = None

                print('GREEN:', green)


        if possible:
            print('Game', game, 'is possible')
            sum += game

    answer = sum
    print(f'The answer: {answer}')


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    return lines


if __name__ == "__main__":
    main()
