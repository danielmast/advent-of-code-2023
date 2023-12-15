def main():
    assert hash('HASH'), 52

    steps = read_file('input.txt')

    sum = 0

    for step in steps:
       sum += hash(step)

    answer = sum
    print(f'The answer: {answer}')

def hash(input):
    current = 0
    for c in input:
        ascii = ord(c)
        current += ascii
        current *= 17
        current %= 256
    return current

def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    steps_str = lines[0].strip().split(',')

    return steps_str


if __name__ == "__main__":
    main()
