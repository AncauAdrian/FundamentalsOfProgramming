from texttable import *


class Board:
    def __init__(self, height, length):
        self._length = length
        self._height = height

        self._board = list()
        for i in range(height):
            self._board.append((length * [0]))

    @property
    def length(self):
        return self._length

    @property
    def height(self):
        return self._height

    def get_value(self, x, y):
        return self._board[x][y]

    def adjust(self, x, y, s):
        self._board[x][y] = s

    def fill_except(self, omit):
        """
        Fills a board with empty moves except points that are in the omit list
        :param omit:
        :return:
        """
        for i in range(self._height):
            for j in range(self._length):
                pair = [i, j]
                if pair not in omit:
                    self._board[i][j] = 1
                else:
                    self._board[i][j] = 0

    def remaining_space(self):
        """
        Fetches a list of points which are empty (valid moves)
        :return:
        """
        cache = []
        for i in range(self._height):
            for j in range(self._length):
                if self._board[i][j] == 0:
                    cache.append([i, j])
        return cache

    def game_end(self):
        """
        Checks if the game has ended
        :return:
        """
        for i in self._board:
            for j in i:
                if j == 0:
                    return False

        return True

    def __str__(self):
        cache = []
        for i in range(self._height):
            row = []
            for j in range(self._length):
                if self._board[i][j] == 0:
                    row.append(' ')
                elif self._board[i][j] == 1:
                    row.append('-')
                elif self._board[i][j] == 2:
                    row.append('X')
                elif self._board[i][j] == -2:
                    row.append('O')

            cache.append(row)

        table = Texttable()
        table.add_rows(cache, header=False)

        return table.draw()