from Domain.BoardException import *
from random import randint
from Domain.Board import Board
import unittest


class BoardController:
    def __init__(self, board):
        self._board = board

    def move(self, x, y, symbol):
        try:
            self.validate_move(x, y, symbol)
        except BoardException as e:
            raise e

        self._board.add_move(x, y, symbol)

    def is_won(self):
        return self._board.is_won()

    def prick_random(self):
        """
        This function picks a random sets of integers x, y and chooses a symbol at random between X and O
        :return: Returns x,y,symbol
        """
        x = randint(0, 5)
        y = randint(0, 5)
        symbol = randint(0, 1)
        if symbol == 0:
            symbol = 'X'
        else:
            symbol = 'O'

        return x, y, symbol

    def move_computer(self):
        """
        This function takes some random coordinates and a symbol, it checks whether it is a valid move and if it is
        it makes that move.
        """
        while True:
            try:
                x, y, symbol = self.prick_random()
                self.validate_move(x, y, symbol)
            except BoardException:
                continue

            break

        self._board.add_move(x, y, symbol)

    def validate_move(self, x, y, symbol):
        if x < 0 or x > 5 or y < 0 or y > 5:
            raise BoardException("[ERROR] The coordinates are not valid on a 6x6 board!")

        if symbol != 'O' and symbol != 'X':
            raise BoardException("[ERROR] Symbol must be either X or O")

        if self._board.is_occupied(x, y):
            raise BoardException("[ERROR] Position is already occupied!")

        return True


class ContTest(unittest.TestCase):
    def test_computer(self):
        b = Board()
        cont = BoardController(b)
        m = b.moves_left()
        print(m)
        cont.move_computer()
        self.assertTrue(b.moves_left() == m - 1)
