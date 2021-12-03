def day1():
    with open("day_1-input.txt") as file:
        count = 0
        last = 0
        for line in file:
            current = int(line)
            if 0 < last < current:
                count += 1
            last = current

        print(count)


if __name__ == '__main__':
    day1()
