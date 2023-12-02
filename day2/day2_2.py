import re

def main():
    lines = read_file('input.txt')

    sum = 0

    for line in lines:
        # example line = 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'

        s = re.search('Game (.*):(.*)', line)
        game = int(s[1])
        max_red = 0
        max_green = 0
        max_blue = 0
        possible = True
        rest = s[2]
        splitted = rest.strip().split(';')
        #print(splitted)

        for set in splitted:
            splitted_again = set.split(', ')
            #print(splitted_again)

            for c in splitted_again:
                try:
                    blue = int(re.search('([0-9]*) blue', c)[1])

                    if (blue > max_blue):
                        max_blue = blue
                except TypeError:
                    blue = None

                #print('BLUE:', blue)

                try:
                    red = int(re.search('([0-9]*) red', c)[1])

                    if (red > max_red):
                        max_red = red
                except TypeError:
                    red = None

                #print('RED:', red)

                try:
                    green = int(re.search('([0-9]*) green', c)[1])

                    if (green > max_green):
                        max_green = green
                except TypeError:
                    green = None

                #print('GREEN:', green)


        if possible:
            power = max_blue * max_red * max_green
            print('Game', game, 'max blue:', max_blue,'max red:', max_red,'max green:', max_green, 'power:', power)
            sum += power

    answer = sum
    print(f'The answer: {answer}')


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    return lines


if __name__ == "__main__":
    main()
