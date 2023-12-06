def main():
    # real
    time = 53897698
    distance = 313109012141201

    # dummy
    #time = 71530
    #distance = 940200

    wins = 0
    print(time, distance)

    for t in range(0, time):
        dist = t * (time - t)
        print(dist)
        if dist > distance:
            wins += 1

    print('Answer:', wins)


if __name__ == "__main__":
    main()
