from collections import Counter


def day_6(days):
    with open("day_6-input.txt") as file:
        data = Counter(int(x) for x in file.readline().split(","))
        data = [data.get(i, 0) for i in range(9)]

    for i in range(days):
        data[(i + 7) % 9] += data[i % 9]

    print(sum(data))


if __name__ == '__main__':
    day_6(80)
    day_6(256)
