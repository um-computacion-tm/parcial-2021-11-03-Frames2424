import random

class Buscaminas():
    def __init__(self, rows=None, cols=None, bombs=None):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.board = [[" "] * rows] * cols
        for _ in range(bombs):
            self.board[random.randint(0, rows-1)][random.randint(0, rows-1)] = "B"
        print(self.board)

    def play(self):
        pass

    def show_board(self):
        pass

    def question(self):
        pass

    def win(self):
        return True

    def lose(self):
        pass