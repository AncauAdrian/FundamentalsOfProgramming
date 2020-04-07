from random import randint
from Board import Board
from unittest import *


class Game:
    def __init__(self, board):
        self.table = board

    def game_end(self):
        """
        Checks if the game ended
        :return:
        """
        return self.table.game_end()

    def create_chunk(self, x, y):
        """
        Creates a square chunk of neighborhoods around the point
        :param x:
        :param y:
        :return:
        """
        startx = x - 1
        starty = y - 1
        stopx = x + 1
        stopy = y + 1

        if x == 0:
            startx += 1
        if x == self.table.height - 1:
            stopx -= 1
        if y == 0:
            starty += 1
        if y == self.table.length - 1:
            stopy -= 1

        for i in range(startx, stopx + 1):
            for j in range(starty, stopy + 1):
                self.table.adjust(i, j, 1)

    def move(self, x, y):
        """
        Makes a move on the point x, y
        :param x:
        :param y:
        :return:
        """
        try:
            self.validate_move(x, y)
        except ValueError as e:
            raise e

        self.create_chunk(x, y)
        self.table.adjust(x, y, 2)

    def can_win(self, moves):
        """
        Checks if there is a winning move and returns it
        :param moves:
        :return:
        """
        cache = self.table
        t = Board(self.table.height, self.table.length)
        self.table = t
        t.fill_except(moves)
        s = None

        for move in moves:
            self.create_chunk(move[0], move[1])
            if t.game_end():
                s = move
                break

        self.table = cache
        return s

    def move_computer(self):
        """
        Calculates a move for the computer. It checks if there is a winning move then makes it, and if there isn't
        then it makes a random move
        :return:
        """
        r = self.table.remaining_space()
        if len(r) <= 9:
            c = self.can_win(r)
            if c is not None:
                self.create_chunk(c[0], c[1])
                self.table.adjust(c[0], c[1], -2)
                return None

        x = randint(0, self.table.height - 1)
        y = randint(0, self.table.length - 1)

        while True:
            try:
                self.validate_move(x, y)
            except ValueError:
                x = randint(0, self.table.height - 1)
                y = randint(0, self.table.length - 1)
                continue

            break

        self.create_chunk(x, y)
        self.table.adjust(x, y, -2)
        return None

    def validate_move(self, x, y):
        """
        Checks if a move is valid and fits within the board
        :param x:
        :param y:
        :return:
        """
        try:
            int(x)
            int(y)
        except ValueError:
            raise ValueError("[ERROR] Coordinates must be integers!")

        if x < 0 or x > self.table.height - 1 or y < 0 or y > self.table.length - 1:
            raise ValueError("[ERROR] Invalid coordinates!")

        if self.table.get_value(x, y) != 0:
            raise ValueError("[ERROR] Invalid move!")

    def __str__(self):
        return str(self.table)


class GameTest(TestCase):
    def test_board(self):
        b = Board(6, 7)
        self.assertEqual(b.height, 6)
        self.assertEqual(b.length, 7)

        self.assertEqual(len(b.remaining_space()), 42)
        b.fill_except([[0, 0], [0, 1]])
        self.assertEqual(len(b.remaining_space()), 2)
        b.adjust(0, 0, 2)
        self.assertEqual(len(b.remaining_space()), 1)
        b.fill_except(b.remaining_space())
        self.assertTrue(b.game_end)

    def test_game(self):
        b = Board(6, 6)
        game = Game(b)

        game.move(1, 1)
        self.assertEqual(len(b.remaining_space()), 27)
        game.move_computer()
        self.assertLess(len(b.remaining_space()), 27)
        self.assertRaises(ValueError, game.validate_move, 1, 1)
        self.assertRaises(ValueError, game.validate_move, 0, 1)
        self.assertRaises(ValueError, game.validate_move, 1, 0)
        self.assertRaises(ValueError, game.validate_move, 0, 0)

        b = Board(3, 3)
        game = Game(b)
        self.assertTrue(game.can_win(b.remaining_space()))
        game.move_computer()
        self.assertTrue(game.game_end())
