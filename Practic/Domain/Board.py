from texttable import *
import unittest


class Board:
    def __init__(self):
        self._table = []

        self.fill_table(0)

    def save_board(self, path="save.txt"):
        f = open(path, "w")
        for i in self._table:
            for j in i:
                if j == 0:
                    f.write("0\n")
                else:
                    f.write(j + '\n')

        f.close()

    def load_board(self, path="save.txt"):
        try:
            f = open(path, "r")
        except IOError as e:
            print("[ERROR] Could not open the file!")
            return

        for i in range(6):
            for j in range(6):
                r = f.readline()
                if r[0] == "0":
                    self._table[i][j] = 0
                else:
                    self._table[i][j] = r[0]

        f.close()

    def moves_left(self):
        s = 0
        for i in self._table:
            for j in i:
                if j == 0:
                    s += 1

        return s

    def add_move(self, x, y, symbol):
        self._table[x][y] = symbol

    def is_occupied(self, x, y):
        if self._table[x][y] == 0:
            return False

        return True

    def row_sum(self, row, symbol):
        s = 0
        for i in range(0, 6):
            if self._table[row][i] == symbol:
                s += 1

        return s

    def col_sum(self, col, symbol):
        s = 0
        for i in range(0, 6):
            if self._table[i][col] == symbol:
                s += 1

        return s

    def first_diag_sum(self, symbol):
        s = 0
        for i in range(0, 6):
            if self._table[i][i] == symbol:
                s += 1

        return s

    def second_diag_sum(self, symbol):
        s = 0
        for i in range(0, 6):
            if self._table[i][5-i] == symbol:
                s += 1

        return s

    def is_won(self):
        for i in range(6):
            if self.row_sum(i, 'X') == 5:
                if self._table[i][0] != 'X' or self._table[i][5] != 'X':
                    return True

            if self.row_sum(i, 'O') == 5:
                if self._table[i][0] != 'O' or self._table[i][5] != 'O':
                    return True

            if self.col_sum(i, 'X') == 5:
                if self._table[0][i] != 'X' or self._table[5][i] != 'X':
                    return True

            if self.col_sum(i, 'O') == 5:
                if self._table[0][i] != 'O' or self._table[5][i] != 'O':
                    return True

        if self.first_diag_sum('X') == 5:
            if self._table[0][0] != 'X' or self._table[5][5] != 'X':
                return True

        if self.first_diag_sum('O') == 5:
            if self._table[0][0] != 'O' or self._table[5][5] != 'O':
                return True

        if self.second_diag_sum('X') == 5:
            if self._table[0][5] != 'X' or self._table[5][0] != 'X':
                return True

        if self.second_diag_sum('O') == 5:
            if self._table[0][5] != 'O' or self._table[5][0] != 'O':
                return True

        # diagonal above first
        s = self._table[0][1]
        i = 0
        if s != 0:
            while i < 5:
                if self._table[i][i+1] != s:
                    break
                i += 1
            if i == 5:
                return True

        # diagonal below first
        s = self._table[1][0]
        i = 0
        if s != 0:
            while i < 5:
                if self._table[i + 1][i] != s:
                    break
                i += 1
            if i == 5:
                return True

        # diagonal above second
        s = self._table[4][0]
        i = 0
        if s != 0:
            while i < 5:
                if self._table[4-i][i] != s:
                    break
                i += 1
            if i == 5:
                return True

        # diagonal below second
        s = self._table[5][1]
        i = 0
        if s != 0:
            while i < 5:
                if self._table[5 - i][i + 1] != s:
                    break
                i += 1
            if i == 5:
                return True

        return False

    def fill_table(self, symbol):
        for i in range(0, 6):
            new = []
            for j in range(0, 6):
                new.append(0)
            self._table.append(new)

    def __str__(self):
        cache = []
        for i in range(0, 6):
            row = []
            for j in range(0, 6):
                if self._table[i][j] == 0:
                    row.append(' ')
                elif self._table[i][j] == 'X':
                    row.append('X')
                elif self._table[i][j] == 'O':
                    row.append('O')
            cache.append(row)

        table = Texttable()
        table.add_rows(cache, header=False)

        s = table.draw()
        return s


class TestBoard(unittest.TestCase):
    def test_sums(self):
        b = Board()
        b.add_move(1, 5, 'O')
        b.add_move(2, 4, 'O')
        b.add_move(3, 3, 'O')
        self.assertFalse(b.is_won())
        b.add_move(4, 2, 'O')
        b.add_move(5, 1, 'O')
        self.assertTrue(b.is_won())
