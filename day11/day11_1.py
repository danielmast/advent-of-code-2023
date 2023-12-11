# First modify the input to add the row and column expansions

# Iterate over input to identify galaxy locations (x, y) and add to galaxies list
# Iterate over the galaxies with i and j (with i < j < len(galaxies)
# Else:
# Compute distances and store in distances

# Sum up distances
def main():
    lines = read_file('input.txt')

    expanded_lines_draft = []

    # Expand rows
    for line in lines:
        expanded_lines_draft.append(line.strip())
        if '#' not in line:
            expanded_lines_draft.append(line.strip())

    # Expand columns:
    # Iterate over every column to see if it contains no galaxies (#)
    # If it doesnt, insert a . add that location

    expanded_lines = []

    for r in range(len(expanded_lines_draft)):
        expanded_lines.append('')

    for c in range(len(expanded_lines_draft[0])):
        found_galaxy = False
        for r_i in range(len(expanded_lines_draft)):
            expanded_lines[r_i] += expanded_lines_draft[r_i][c]

            if expanded_lines_draft[r_i][c] == '#':
                found_galaxy = True

        if not found_galaxy:
            for r_i in range(len(expanded_lines)):
                expanded_lines[r_i] += '.'


    for line in expanded_lines:
        print(line)

    galaxies = get_galaxies(expanded_lines)
    distances = get_distances(galaxies)
    sum = get_sum(distances)

    answer = sum
    print(f'The answer: {answer}')

def get_galaxies(expanded_lines):
    galaxies = []
    for r_i in range(len(expanded_lines)):
        for c_i in range(len(expanded_lines[0])):
            if expanded_lines[r_i][c_i] == '#':
                galaxies.append((r_i, c_i))
    return galaxies

def get_distances(galaxies):
    distances = []
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            distance = get_distance(galaxies[i], galaxies[j])
            distances.append(distance)
    return distances

def get_distance(galaxy1, galaxy2):
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

def get_sum(distances):
    sum = 0
    for distance in distances:
        sum += distance
    return sum

def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    return lines


if __name__ == "__main__":
    main()
