from statistics import median, mean


def day_7():
    with open("day_7-input.txt") as file:
        data = [int(i) for i in file.readline().split(",")]

    '''Part 1'''
    m = round(median(data))
    result = sum(abs(m - i) for i in data)
    print(result)

    '''Part 2'''
    m = int(mean(data))
    result = sum(sum(range(abs(m - i) + 1)) for i in data)
    print(result)


if __name__ == '__main__':
    day_7()
