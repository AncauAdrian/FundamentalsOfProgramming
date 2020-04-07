from Domain.Board import Board
from Controller.BoardController import *


class UI:
    def __init__(self):
        pass

    def main(self):
        board = Board()
        boardCont = BoardController(board)

        try:
            a = input("Continue? (c)    or    New game? (any key other than c)")
            if a == "c":
                board.load_board()
        except IOError as e:
            print(e + "Starting new game since save file couldn't be found")

        while True:
            print(board)
            try:
                x = int(input("X      >> "))
                y = int(input("Y      >> "))
                symbol = input("Symbol >> ")
                symbol = symbol.upper()
            except ValueError as e:
                print("[ERROR] X and Y must be integers!")
                continue

            try:
                boardCont.move(x, y, symbol)
            except BoardException as e:
                print(e)
                continue

            if boardCont.is_won():
                print(board)
                print("Order wins!")
                return

            boardCont.move_computer()

            if boardCont.is_won():
                print(board)
                print("Order wins!")
                return

            if board.moves_left() == 0:
                print(board)
                print("Chaos wins!")

            board.save_board()


