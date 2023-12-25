from collections import defaultdict
import re
from math import floor


def main():
    hailstones = read_file('input.txt')

    answer = solve(hailstones)
    print(f'The answer: {answer}')

def solve(hailstones):
    sum = 0

    test_area = [200000000000000, 400000000000000]
    # test_area = [7, 27]

    # Iterate over all pairs of hailstones
    for h1 in range(len(hailstones)):
        for h2 in range(h1 + 1, len(hailstones)):
            hailstone1 = hailstones[h1]
            hailstone2 = hailstones[h2]
            intersection_point = get_intersection_point(hailstone1, hailstone2)

            if intersection_point is None:
                continue

            if hailstone1[0][0] == 20 and hailstone1[0][1] == 25 and hailstone2[0][0] == 20 and hailstone2[0][1] == 19:
                pass

            intersection_times = get_intersection_times(intersection_point, hailstone1, hailstone2)
            if min(intersection_times) >= 0 and is_in_test_area(intersection_point, test_area):
                sum += 1

    return sum

def is_in_test_area(intersection_point, test_area):
    for i in intersection_point:
        if not test_area[0] <= i <= test_area[1]:
            return False
    return True


def get_intersection_times(intersection_point, hailstone1, hailstone2):
    hailstones = [hailstone1, hailstone2]
    intersection_times = []

    for hailstone in hailstones:
        dx = intersection_point[0] - hailstone[0][0]
        t = dx / hailstone[1][0]

        intersection_times.append(t)

    return intersection_times

def get_intersection_point(hailstone1, hailstone2):
    h1a, h1b = get_formula(hailstone1)
    h2a, h2b = get_formula(hailstone2)

    if (h1a - h2a) == 0:
        return None

    x = (h2b - h1b) / (h1a - h2a)
    y = h1a * x + h1b
    return x, y


def get_formula(hailstone):
    px, py, pz = hailstone[0]
    vx, vy, vz = hailstone[1]

    a = vy / vx
    b = -1 * px * a + py

    return a, b


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    hailstones = []

    for line in lines:
        line = line.strip()
        line = line.replace(' ', '')
        p, v = line.split('@')
        px, py, pz = list(map(int, p.split(',')))
        vx, vy, vz = list(map(int, v.split(',')))
        hailstone = ((px, py, pz),(vx, vy, vz))
        hailstones.append(hailstone)

    return hailstones


if __name__ == "__main__":
    main()
