with open("day_1-input.txt") as file:
    count = 0
    nr_of_days = 3
    window_size = nr_of_days + 1
    window = [0 for _ in range(nr_of_days + 1)]
    for i, line in enumerate(file):
        current = int(line)

        window = [x if (i + 1) % window_size == j else x + current for j, x in enumerate(window)]

        if i >= 3:
            if window[(i + 1) % window_size] < window[(i + 2) % window_size]:
                count += 1

        window[(i + 1) % window_size] = 0

    print(count)
