from collections import defaultdict


def main():
    area = read_file('input.txt')

    R = len(area)
    C = len(area[0])

    start = (0, 1)
    end = (R - 1, C - 2)

    graph = create_graph(start, end, area)
    answer = longest_path(graph, start, end)
    print(f'The answer: {answer}')


def create_graph(start, end, area):
    R = len(area)
    C = len(area[0])

    currents = [(start, None, [], 0, 0)]

    graph = defaultdict(set)
    seen = set()

    while currents:
        new_currents = []

        for current in currents:
            c, prev, path, l, sl = current

            if c == end:
                graph[path[-1]].add((c, sl))

            nbs = get_nbs(c, prev, area, R, C)

            assert len(nbs) in [0, 1, 2, 3]

            if len(nbs) >= 2:
                if len(graph.keys()) == 0:
                    graph[start].add((c, sl))
                else:
                    graph[path[-1]].add((c, sl))
                    graph[c].add((path[-1], sl))

                    if c not in seen:
                        seen.add(c)
                    else:
                        continue

                path = path + [c]
                sl = 0

            for n in nbs:
                new_currents.append((n, c, path, l + 1, sl + 1))

        currents = new_currents

    return graph


def longest_path(graph, start, end):
    max_so_far = [0]
    seen = defaultdict(lambda: False)
    dfs2(start, end, 0, seen, graph, 0, max_so_far)
    return max_so_far[0]


def dfs2(v, end, length, SEEN, G, d, max_so_far):
    if SEEN[v]:
        return

    SEEN[v] = True

    if v == end:
        if length > max_so_far[0]:
            max_so_far[0] = length
            print(f'Max so far = {length}, d = {d}')

    for t, d in G[v]:
        dfs2(t, end, length + d, SEEN, G, d+1, max_so_far)

    SEEN[v] = False


def get_nbs(loc, prev, area, R, C):
    nbs = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx == 0 or dy == 0) and not (dx == 0 and dy == 0):
                n = (loc[0] + dy, loc[1] + dx)
                if 0 <= n[0] < R and 0 <= n[1] < C:
                    if n == prev:
                        continue

                    if area[n[0]][n[1]] in ['.', '>', '<', '^', 'v']:
                        nbs.append(n)
    return nbs


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    stripped = []
    for line in lines:
        stripped.append(line.strip())

    return stripped


if __name__ == "__main__":
    main()
