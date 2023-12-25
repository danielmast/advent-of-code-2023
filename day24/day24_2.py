import numpy as np
from sympy import symbols, Eq, solve

# Apply sympy equation solver voodoo

def main():
    hailstones = read_file('input.txt')

    # See if the answer is correct for the first 3 hailstones (it is)
    answer = solve_puzzle(hailstones[:3])

    print(f'The answer: {answer}')


def solve_puzzle(hailstones):
    return sum(linear(hailstones))


def linear(hailstones):
    rvx, rvy, rvz, rpx, rpy, rpz = symbols('rvx rvy rvz rpx rpy rpz')
    syms = [rvx, rvy, rvz, rpx, rpy, rpz]

    eqs = []

    for h, hailstone in enumerate(hailstones):
        hvx, hvy, hvz = hailstone[1]
        hpx, hpy, hpz = hailstone[0]
        th = symbols(f't{h}')
        syms.append(th)
        eqx = Eq(hvx * th + hpx, rvx * th + rpx)
        eqy = Eq(hvy * th + hpy, rvy * th + rpy)
        eqz = Eq(hvz * th + hpz, rvz * th + rpz)
        eqs.extend([eqx, eqy, eqz])

    solution = solve(eqs, syms)
    rpx, rpy, rpz = list(solution[0])[3:6]
    return rpx, rpy, rpz


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
