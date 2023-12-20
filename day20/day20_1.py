from collections import defaultdict, deque


def main():
    modules, ffs, conjs = read_file('input.txt')

    total_high_count = 0
    total_low_count = 0

    for i in range(1000):
        high_count, low_count = run(modules, ffs, conjs)
        total_high_count += high_count
        total_low_count += low_count

    answer = total_high_count * total_low_count
    print(f'The answer: {answer}', ' = total_high_count * total_low_count = ', total_high_count, ' * ', total_low_count)


def run(modules, ffs, conjs):
    high_count = 0
    low_count = 0

    #print(f'button -{0}-> broadcaster')
    low_count += 1
    q = deque()  # [(source_type, source, target, pulse)]

    source_type, source, targets = modules['broadcaster']
    for target in targets:
        pulse = 0
        q.append((source_type, source, target, pulse))

    while len(q) > 0:
        source_type, source, target, pulse = q.popleft()
        #print(f'{source_type}{source} -{pulse}-> {target}')

        if pulse == 0:
            low_count += 1
        else:
            high_count += 1

        new_pulse = update_module(source, target, pulse, ffs, conjs)

        if new_pulse is None:
            continue

        new_source_type, new_source, new_targets = modules[target]
        for new_target in new_targets:
            q.append((new_source_type, new_source, new_target, new_pulse))

    return high_count, low_count


def update_module(source, target, pulse, ffs, conjs):
    # update the state of the target module based on the pulse
    if target in ffs:
        if pulse == 1:
            return None
        elif pulse == 0:
            old_state = ffs[target]
            ffs[target] = 1 - old_state
            return 1 - old_state
    elif target in conjs:
        conjs[target][source] = pulse

        for t in conjs[target]:
            if conjs[target][t] == 0:
                return 1
        return 0

    return None


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    modules = defaultdict(tuple)
    ffs = defaultdict(int)
    conjs = defaultdict(lambda: defaultdict(int))

    conj_names = []

    for line in lines:
        source_type, source, targets = get_parts(line)
        modules[source] = (source_type, source, targets)

        if source_type == '%':
            ffs[source] = 0
        elif source_type == '&':
            conj_names.append(source)

    for line in lines:
        source_type, source, targets = get_parts(line)

        for target in targets:
            if target in conj_names:
                conjs[target][source] = 0

    return modules, ffs, conjs


def get_parts(line):
    line = line.strip().replace(' ', '')
    source_str, targets_str = line.split('->')
    targets = targets_str.split(',')

    if source_str[0] == '%':
        source_type = '%'
        source = source_str[1:]
    elif source_str[0] == '&':
        source_type = '&'
        source = source_str[1:]
    else:
        source_type = 'broadcaster'
        source = source_str

    return source_type, source, targets


if __name__ == "__main__":
    main()
