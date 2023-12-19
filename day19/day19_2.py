from collections import defaultdict


def main():
    workflows = read_file('input.txt')

    accepting_workflows = get_accepting_workflows(workflows)

    assert get_distinct_combinations(
        [{'x': [1000, 2000], 'm': [1, 4000], 'a': [3000, 3500], 's': [1, 4000]}]
    ) == 1001 * 4000 * 501 * 4000

    result_windows = []
    for workflow_label, a_i in accepting_workflows:
        window = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}

        prev_label = 'A'
        while True:
            workflow = workflows[workflow_label]
            update_window(window, workflow, prev_label, a_i)

            if workflow_label == 'in':
                result_windows.append(window)
                break

            prev_label = workflow_label
            workflow_label = get_workflow_referring_to(workflow_label, workflows)

    answer = get_distinct_combinations(result_windows)
    print(f'The answer: {answer}')


def get_distinct_combinations(windows):
    sum = 0
    for window in windows:
        sum += get_volume(window)
    return sum


def get_volume(window):
    volume = 1
    for v in window:
        volume *= window[v][1] - window[v][0] + 1
    return volume


def get_workflow_referring_to(referred_to_label, workflows):
    for workflow_label in workflows:
        workflow = workflows[workflow_label]
        for stage in workflow:
            if isinstance(stage, str) and stage == referred_to_label:
                return workflow_label
            if stage[-1] == referred_to_label:
                return workflow_label


# Very ugly function, but too lazy to deduplicate
def update_window(window, workflow, prev_label, a_i):
    if len(workflow) == 0:
        print('debug')

    last_stage = workflow[-1]

    if prev_label == 'A':
        stage = workflow[a_i]

        if stage != last_stage:
            # If the part did match one of the stages, iterate from right to left
            matched = False
            for i in range(0, a_i + 1):
                stage = workflow[a_i - i]

                if matched:
                    update_window_no_match(window, stage)
                elif stage[3] == prev_label:
                    matched = True
                    update_window_match(window, stage)

            return

    # If the part was rejected by this window, 'unmatch' all the stages
    if last_stage == prev_label:
        for stage in workflow[0:-1]:
            update_window_no_match(window, stage)
        return

    # If the part did match one of the stages, iterate from right to left
    matched = False
    for i in range(2, len(workflow) + 1):
        stage = workflow[len(workflow) - i]

        if matched:
            update_window_no_match(window, stage)
        elif stage[3] == prev_label:
            matched = True
            update_window_match(window, stage)


def update_window_match(window, stage):
    assert len(stage) == 4

    variable, operator, value, _ = stage

    if operator == '<':
        window[variable][1] = min(window[variable][1], value-1)

    elif operator == '>':
        window[variable][0] = max(window[variable][0], value+1)


def update_window_no_match(window, stage):
    assert len(stage) == 4

    variable, operator, value, _ = stage
    # s < 537
    # no match (so: s >= 537)
    # s: [537, 4000]
    if operator == '<':
        window[variable][0] = max(window[variable][0], value)

    # m > 1000
    # no match (so: m <= 1000)
    # m: [1, 1000]
    elif operator == '>':
        window[variable][1] = min(window[variable][1], value)


def get_accepting_workflows(workflows):
    accepting = []

    for workflow_label in workflows:
        workflow = workflows[workflow_label]
        for i, stage in enumerate(workflow):
            if stage[-1] == 'A':
                accepting.append((workflow_label, i))

    return accepting


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    workflows = defaultdict(list)

    for line in lines:
        line = line.strip()

        if line == '':
            break

        label = line[:line.index('{')]
        variables = line[line.index('{') + 1 : line.index('}')].split(',')

        for workflow_str in variables:
            if ':' in workflow_str:
                variable = workflow_str[0]
                operator = workflow_str[1]
                value = int(workflow_str.split(':')[0][2:])
                target = workflow_str.split(':')[1]
                workflows[label].append((variable, operator, value, target))
            else:
                workflows[label].append(workflow_str)

    return workflows


if __name__ == "__main__":
    main()
