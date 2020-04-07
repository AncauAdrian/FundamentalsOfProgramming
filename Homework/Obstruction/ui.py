from Board import *
from Game import *


class UI:
    def start_game(self):
        try:
            rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))
        except ValueError:
            print("[ERROR] Try again")
            return None

        if rows < 3 or columns < 3:
            print("[ERROR] Try again")
            return None

        table = Board(rows, columns)
        game = Game(table)

        printtable = True

        while True:
            if printtable:
                print(game)
            else:
                printtable = True

            try:
                row = int(input("row >> "))
                column = int(input("column >> "))
            except ValueError:
                print("[ERROR] Invalid input!")
                printtable = False
                continue

            try:
                game.move(row, column)
            except ValueError as e:
                print(e)
                printtable = False
                continue

            if game.game_end():
                print("You WIN!")
                return

            game.move_computer()

            if game.game_end():
                print(game)
                print("Computer wins, you lose!")
                return


ui = UI()
ui.start_game()
