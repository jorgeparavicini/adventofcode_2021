def day_5(allow_diagonals):
    segments = []
    max_segment = [0, 0]
    with open("day_5-input.txt") as file:
        for i, line in enumerate(file):
            segments.append([[int(i) for i in component.split(",")] for component in line.split(" -> ")])
            max_segment[0] = max(segments[i][0][0], segments[i][1][0], max_segment[0])
            max_segment[1] = max(segments[i][0][1], segments[i][1][1], max_segment[1])

    matrix = [[0 for _ in range(max_segment[0] + 1)] for _ in range(max_segment[1] + 1)]
    for segment in segments:
        x_seg = (segment[0][0], segment[1][0])
        y_seg = (segment[0][1], segment[1][1])

        x_length = x_seg[1] - x_seg[0]
        y_length = y_seg[1] - y_seg[0]
        length = max(abs(x_length) + 1, abs(y_length) + 1)
        x_dir = 0 if x_length == 0 else x_length // abs(x_length)
        y_dir = 0 if y_length == 0 else y_length // abs(y_length)

        if not allow_diagonals and x_seg[0] != x_seg[1] and y_seg[0] != y_seg[1]:
            continue

        for i in range(length):
            matrix[y_seg[0] + y_dir * i][x_seg[0] + x_dir * i] += 1

    result = sum((1 for line in matrix for value in line if value >= 2))
    print(result)


if __name__ == '__main__':
    day_5(False)
    day_5(True)
