from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx


def main():
    graph = read_file('input.txt')
    answer = solve(graph)
    print(f'The answer: {answer}')

def solve(graph):
    # Look at plot to decide which wires to cut
    draw_graph(graph)

    graph = cut_wires(graph, [('pmn', 'kdc'), ('jmn', 'zfk'), ('hvm', 'grd')])
    graph = get_full_graph(graph)
    sizes = get_graph_sizes(graph)

    return sizes[0] * sizes[1]


def get_graph_sizes(graph):
    sizes = [0, 0]
    nodes = ['smq', 'mvf']

    for i in [0, 1]:
        currents = [nodes[i]]
        seen = currents.copy()
        while len(currents) > 0:
            new_currents = []
            for current in currents:
                for right in graph[current]:
                    if right not in seen:
                        new_currents.append(right)
                        seen.append(right)
            currents = new_currents
        sizes[i] = len(seen)

    return sizes


def get_full_graph(graph):
    new_graph = defaultdict(list)

    for left in graph:
        rights = graph[left]
        for right in rights:
            new_graph[left].append(right)
            new_graph[right].append(left)

    return new_graph


def cut_wires(graph, wires):
    new_graph = defaultdict(list)

    for left in graph:
        rights = graph[left]
        for right in rights:
            should_add = True
            for (wleft, wright) in wires:
                if (left == wleft and right == wright) or (left == wright and right == wleft):
                    should_add = False
                    break
            if should_add:
                new_graph[left].append(right)

    return new_graph


def draw_graph(graph):
    g = nx.Graph()
    for node in graph:
        for neighbor in graph[node]:
            g.add_edge(node, neighbor)

    plt.figure(figsize=(30, 30))
    nx.draw(g, with_labels=True, node_color='skyblue', node_size=700, edge_color='black')
    plt.show()


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    graph = defaultdict(list)

    for line in lines:
        line = line.strip()
        left, rights_str = line.split(':')
        rights = rights_str.strip().split(' ')
        graph[left].extend(rights)

    return graph


if __name__ == "__main__":
    main()
