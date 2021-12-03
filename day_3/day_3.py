def day3():
    with open("day_3-input.txt") as file:
        most_common_bits = [0 for _ in range(12)]
        count = 0
        for line in file:
            for i, x in enumerate(line.rstrip()):
                most_common_bits[i] += int(x)

            count += 1

        most_common_bits = ''.join(("0" if x < count / 2 else "1" for x in most_common_bits))
        epsilon = ''.join(("1" if x == "0" else "0" for x in most_common_bits))
        gamma = int(most_common_bits, 2)
        epsilon = int(epsilon, 2)
        print(gamma * epsilon)


if __name__ == '__main__':
    day3()
