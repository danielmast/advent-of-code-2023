from collections import defaultdict
import re

def main():
    seed_ranges, maps = read_file('input.txt')
    print()

    # init layers dict
    layers = []
    layers.append(('seed-to-soil', dict(seed_ranges)))
    for layer_name in ['soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location', 'locations']:
        layers.append((layer_name, dict()))

    for l, layer in enumerate(layers[:-1]):
        print('Layer:', l)
        layer_name = layer[0]

        map = dict(maps[layer_name])

        layer_segment_chunks_todo = []
        layer_segment_chunks_done = []
        for layer_segment_key in layer[1]:
            layer_segment = (layer_segment_key, layer[1][layer_segment_key])
            layer_segment_chunks_todo.append(layer_segment)

        new_todos = layer_segment_chunks_todo
        while len(new_todos) > 0:
            todos = []
            skip = []
            for new_todo in new_todos:
                todos.append(new_todo)
                skip.append(False)
            new_todos = []
            for i, layer_segment_chunk in enumerate(todos):
                if skip[i]:
                    continue

                for map_key in map:
                    map_segment = (map_key, map[map_key][1])
                    map_segment_destination = map[map_key][0]

                    print('layer_segment_chunk:', layer_segment_chunk)
                    print('map_segment:', map_segment)

                    # decide the overlap and rest
                    overlap, layer_segment_chunk_rest = get_overlap(layer_segment_chunk, map_segment)
                    print('overlap:', overlap)

                    if overlap:
                        new_chunk = (overlap[0] - map_key + map_segment_destination, overlap[1])

                        layer_segment_chunks_done.append(new_chunk)

                        if len(layer_segment_chunk_rest) > 0:
                            new_todos.extend(layer_segment_chunk_rest)
                        skip[i] = True

            for i, todo in enumerate(todos):
                if not skip[i]:
                    layer_segment_chunks_done.append(todo)

        for d in layer_segment_chunks_done:
            layers[l+1][1][d[0]] = d[1]

    min_location = 1000000000000000000000

    for loc in layers[7][1]:
        min_location = min(min_location, loc)

    answer = min_location
    print(f'The answer: {answer}')


def get_overlap(layer_segment, map_segment):
    l_start = layer_segment[0]
    l_range = layer_segment[1]
    l_end = l_start + l_range
    m_start = map_segment[0]
    m_range = map_segment[1]
    m_end = m_start + m_range

    overlap = None
    layer_segment_rest = [layer_segment]

    if (l_start <= m_start <= l_end <= m_end): # case 1: layer is shifted left of map
        overlap = (m_start, l_end - m_start)
        layer_segment_rest = [(l_start, m_start - l_start)]
    elif (m_start <= l_start <= m_end <= l_end): # case 2: layer is shifted right of map
        overlap = (l_start, m_end - l_start)
        layer_segment_rest = [(m_end, l_end - m_end)]
    elif (m_start <= l_start <= l_end <= m_end):  # case 3: layer is fully within map
        overlap = (l_start, l_range)
        layer_segment_rest = []
    elif (l_start <= m_start <= m_end <= l_end):  # case 4: map is fully within layer
        overlap = (m_start, m_range)
        layer_segment_rest = [(l_start, m_start - l_start), (m_end, l_end - m_end)]

    if overlap is not None and overlap[1] == 0:
        overlap = None

    lsr_clean = []
    for lsr in layer_segment_rest:
        if lsr[1] != 0:
            lsr_clean.append(lsr)

    return overlap, lsr_clean

def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    seeds_input = list(map(int, re.search('seeds: (.*)', lines[0])[1].split()))

    seed_ranges = defaultdict(int)

    for i in range(0, len(seeds_input), 2):
        start = seeds_input[i]
        _range = seeds_input[i+1]
        seed_ranges[start] = _range

    maps = defaultdict(lambda: defaultdict(tuple))

    for line in lines[2:]:
        try:
            s = re.search('(.*) map:', line)
            current_map_description = s[1]
            print(current_map_description)
            continue
        except TypeError:
            pass

        if line == '\n':
            continue

        nums = list(map(int, line.split(' ')))
        if len(nums) == 3:
            print(nums)
            maps[current_map_description][nums[1]] = (nums[0], nums[2])


    return seed_ranges, maps


if __name__ == "__main__":
    main()
