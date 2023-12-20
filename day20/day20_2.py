from collections import defaultdict, deque
from math import lcm

def main():
    modules, ffs, conjs = read_file('input.txt')

    ffs_to_conj = get_ffs_to_conj(ffs, conjs)

    i = 1
    while not is_done(ffs_to_conj):
        run(modules, ffs, conjs)

        # pure magic from here
        for ff in ffs_to_conj:
            if ffs_to_conj[ff][2] != 0:
                continue

            # if bit flipped
            if ffs[ff] == 1 - ffs_to_conj[ff][3]:
                # if subcycle was not yet set
                if ffs_to_conj[ff][0] == 0:
                    ffs_to_conj[ff][0] = i

                    if i == 1:
                        ffs_to_conj[ff][1] = 1
                else:
                    if ffs_to_conj[ff][0] == 1:
                        continue

                    m = i % ffs_to_conj[ff][0]
                    if m == 0:
                        ffs_to_conj[ff][1] += 1
                    else:
                        ffs_to_conj[ff][2] = m

                ffs_to_conj[ff][3] = 1 - ffs_to_conj[ff][3]

        i += 1

    cycles = set()
    for ff in ffs_to_conj:
        f = ffs_to_conj[ff]
        cycles.add(f[0] * f[1] + f[2])

    answer = lcm(*cycles)
    print(f'The answer: {answer}')


def is_done(ffs_to_conj):
    for ff in ffs_to_conj:
        if ffs_to_conj[ff][2] == 0 and ffs_to_conj[ff][0] != 1:
            return False
    return True


# Get all flip-flops that have a conjunction as output
def get_ffs_to_conj(ffs, conjs):
    ffs_to_conj = defaultdict(list)
    for c in conjs:
        conj = conjs[c]
        for s in conj:
            if s in ffs:
                ffs_to_conj[s] = [0, 1, 0, 0] # subcycle, reps, rest, prev
    return ffs_to_conj


def run(modules, ffs, conjs):
    q = deque()  # [(source_type, source, target, pulse)]

    source_type, source, targets = modules['broadcaster']
    for target in targets:
        pulse = 0
        q.append((source_type, source, target, pulse))

    while len(q) > 0:
        source_type, source, target, pulse = q.popleft()

        new_pulse = update_module(source, target, pulse, ffs, conjs)

        if new_pulse is None:
            continue

        new_source_type, new_source, new_targets = modules[target]
        for new_target in new_targets:
            q.append((new_source_type, new_source, new_target, new_pulse))


def update_module(source, target, pulse, ffs, conjs):
    # update the state of the target module based on the pulse
    # and return the output pulse
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
