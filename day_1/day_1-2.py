def day1_2():
    with open("day_1-input.txt") as file:
        lines = [int(x) for x in file]
        buffer_size = 3
        count = 0
        previous_sum = 0

        for i in range(len(lines) - 2):
            current_sum = sum((lines[i + x] for x in range(buffer_size)))
            if current_sum > previous_sum != 0:
                count += 1
            previous_sum = current_sum

        print(count)


if __name__ == '__main__':
    day1_2()
