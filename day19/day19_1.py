from collections import defaultdict

# Store all the parts, with its xmas values
# Store all workflows, with the label as key
# Per part, loop through the workflows, updating its xmas values
# If accepted, save in list

# Iterate over accepted and add values


def main():
    workflows, parts = read_file('input.txt')

    accepted = []
    for part in parts:
        if apply(part, workflows) == 'A':
            accepted.append(part)

    sum = 0
    for a in accepted:
        sum += a['x'] + a['m'] + a['a'] + a['s']

    answer = sum
    print(f'The answer: {answer}')


def apply(part, workflows):
    workflow_label = 'in'

    while workflow_label not in ('A', 'R'):
        workflow = workflows[workflow_label]
        for stage in workflow:
            if len(stage) == 4:
                variable, operator, value, target = stage
                if operator == '>' and part[variable] > value:
                    workflow_label = target
                    break
                elif operator == '<' and part[variable] < value:
                    workflow_label = target
                    break
            else:
                workflow_label = stage

    return workflow_label


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    workflows = defaultdict(list)
    parts = []

    newline_seen = False

    for line in lines:
        line = line.strip()

        if line == '':
            newline_seen = True
            continue

        # workflows
        if not newline_seen:
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

        # parts
        else:
            part = {}
            variables = line[1:-1].split(',')
            for variable_str in variables:
                variable, value = variable_str.split('=')
                part[variable] = int(value)
            parts.append(part)

    return workflows, parts


if __name__ == "__main__":
    main()
