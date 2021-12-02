with open("day_2-input.txt") as file:
    horizontal = 0
    depth = 0

    for line in file:
        words = line.split(" ")
        amount = int(words[1])

        if words[0] == "forward":
            horizontal += amount
        if words[0] == "down":
            depth += amount
        if words[0] == "up":
            depth -= amount

    print(horizontal * depth)
