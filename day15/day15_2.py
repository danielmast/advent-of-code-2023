from collections import defaultdict


def main():
    assert hash('HASH'), 52

    steps = read_file('input.txt')

    boxes = defaultdict(list)

    for step in steps:
        label = step[0]
        label_hash = hash(label)
        box = boxes[label_hash]
        if len(step) == 2:
            removed = []
            for lens in box:
                if lens[0] != step[0]:
                    removed.append(lens)
            boxes[label_hash] = removed

        else:
            lens = (step[0], int(step[2]))
            if len(box) == 0:
                box.append(lens)
            else:
                is_replaced = False
                for l in range(len(box)):
                    if box[l][0] == lens[0]:
                        box[l] = lens
                        is_replaced = True
                        break
                if not is_replaced:
                    box.append(lens)

    total_focusing_power = 0

    for b in list(boxes):
        box = boxes[b]
        for l in range(len(box)):
            lens = box[l]
            focusing_power = (b+1) * (l+1) * lens[1]
            total_focusing_power += focusing_power

    answer = total_focusing_power
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

    steps = []
    for step_str in steps_str:
        if step_str.endswith('-'):
            step = (step_str[:-1], '-')
        else:
            key, value = step_str.split('=')
            step = (key, '=', value)

        steps.append(step)

    return steps


if __name__ == "__main__":
    main()
