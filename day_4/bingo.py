class Bingo:
    bingo_size = 5

    def __init__(self, values):
        if len(values) != pow(Bingo.bingo_size, 2):
            raise ValueError("The passed values do not form a square matrix")
        self.matrix = [
            [[values[i + j * Bingo.bingo_size], False]
             for i in range(Bingo.bingo_size)]
            for j in range(Bingo.bingo_size)
        ]

    def get_value_at(self, x, y):
        return self.matrix[y][x]

    def set_value(self, value):
        for row in self.matrix:
            for cell in row:
                if cell[0] == value:
                    cell[1] = True
                    return

    def is_bingo(self):
        for i in range(Bingo.bingo_size):
            is_horizontal_bingo = True
            is_vertical_bingo = True
            for j in range(Bingo.bingo_size):
                if not self.get_value_at(i, j)[1]:
                    is_vertical_bingo = False
                if not self.get_value_at(j, i)[1]:
                    is_horizontal_bingo = False
            if is_horizontal_bingo or is_vertical_bingo:
                return True
        return False

    def unmarked_sum(self):
        return sum((value[0] for sub in self.matrix for value in sub if not value[1]))
