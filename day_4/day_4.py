from bingo import Bingo


def day4():
    with open("day_4-input.txt") as file:
        input_lines = [line.strip() for line in file if not line.isspace()]
        guesses = [int(guess) for guess in input_lines[0].split(",")]
        bingos = []

        offset = 1
        bingo_size = 5
        for i in range((len(input_lines) - offset) // bingo_size):
            values = []
            for x in range(Bingo.bingo_size):
                values += (int(value) for value in input_lines[offset + i * bingo_size + x].split())

            bingos.append(Bingo(values))

        successful_scores = []

        for guess in guesses:
            for bingo in bingos:
                bingo.set_value(guess)
                if bingo.is_bingo():
                    successful_scores.append(bingo.unmarked_sum() * guess)
            bingos = [bingo for bingo in bingos if not bingo.is_bingo()]

        print("Result part 1: " + str(successful_scores[0]))
        print("Result part 2: " + str(successful_scores[-1]))


if __name__ == '__main__':
    day4()
