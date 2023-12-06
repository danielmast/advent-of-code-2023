
def main():
    races = read_file('input.txt')
    #races = [(7, 9), (15, 40), (30, 200)] # dummy

    sum = 1

    for time, distance in races:
        wins = 0
        print(time, distance)

        for t in range(0, time):
            dist = t * (time - t)
            print(dist)
            if dist > distance:
                wins += 1

        sum *= wins

    print('Answer:', sum)

def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    races = [(53, 313), (89, 1090), (76, 1214), (98, 1201)]

    return races


if __name__ == "__main__":
    main()
