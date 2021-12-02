with open("day_2-input.txt") as file:
    horizontal = 0
    depth = 0
    aim = 0

    for line in file:
        words = line.split(" ")
        amount = int(words[1])

        if words[0] == "forward":
            horizontal += amount
            depth += amount * aim
        if words[0] == "down":
            aim += amount
        if words[0] == "up":
            aim -= amount

    print(horizontal * depth)
