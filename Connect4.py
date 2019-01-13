""" This is a class for Connect4 game.
Author - Aditya Goyal
"""
from __future__ import annotations
import sys


class Player:
    """ Stores the information of the player.

    ===Attributes===
    name: the name of the player
    color: the color the player has chosen
    """
    name: str
    color: str

    def __init__(self, name: str, color: str)-> None:
        """ Initializes the class.
        """
        self.name = name
        self.color = color


class Game:
    """ This class regulates the whole game and keeps track of the people and
    the chances they are having.
    === Attributes ===
    player1: the first player of the game.
    player2: the second player of the game.
    grid_1: The grid user in the game.

    """
    player1: Player
    player2: Player
    grid_1: Grid

    def __init__(self, p1: Player, p2: Player) -> None:
        """ Initializes the class Game.
        """
        self.player1 = p1
        self.player2 = p2
        self.grid_1 = Grid()

    def fill_grid(self, num: int, player_color: str) -> None:
        """ Fills the grid according to the number inputted by the user.
        """
        i = 5
        j = num
        while self.grid_1.grid[i][j] != 0:
            i -= 1
        self.grid_1.input_color(i, j, player_color)

    def play(self) -> None:
        """ Regulates and carries the game on.
        """
        while True:
            self.grid_1.output()
            p1_turn = input(f'{self.player1.name}, which row do '
                            f'you want to put the color in?')
            self.fill_grid(int(p1_turn), self.player1.color)
            if self.did_win(self.player1.color):
                print(f"{self.player1.name} won the game!")
                self.grid_1.output()
                sys.exit()
            p2_turn = input(f'{self.player2.name}, which row do you want to '
                            f'put'
                            f'the color in?')
            self.fill_grid(int(p2_turn), self.player2.color)
            if self.did_win(self.player2.color):
                print(f"{self.player2.name} Player 2 won the game!")
                self.grid_1.output()
                sys.exit()

    def did_win(self, col: str) -> bool:
        """ Returns if the person won the game.
        """
        return (self.grid_1.is_row(col) or self.grid_1.is_column(col) or
                self.grid_1.right_left_diagonal(col) or
                self.grid_1.left_right_diagonal(col))


class Grid:
    """ The grid of the game.

    ===Attributes===
    grid: the game grid.
    """
    grid: list

    def __init__(self)-> None:
        """ Initializes the class Grid.
        """
        self.grid = [[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

    def input_color(self, i: int, j: int, col: str) -> None:
        """ Inputs the value according to the grid.
        """
        self.grid[i][j] = col

    def output(self)-> None:
        """ Prints the grid.
        """
        for i in range(6):
            print(self.grid[i])

    def is_row(self, col: str) -> bool:
        """ Returns if the player has connected 4 colors in a row.
        """
        count = 0
        for i in range(6):
            for j in range(7):
                if self.grid[i][j] == col:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
        if count >= 4:
            return True
        else:
            return False

    def is_column(self, col: str) -> bool:
        """ Returns if the player has connected4 colors in a column.
        """
        count = 0
        for i in range(7):
            for j in range(6):
                if self.grid[j][i] == col:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
        if count >= 4:
            return True
        else:
            return False

    def left_right_diagonal(self, col: str) -> bool:
        """ Returns if the player has connected4 colors in the diagonal from
        left to right.
        """
        count = 0
        for a in range(3):
            for b in range(4):
                i = a
                j = b
                if a == 1 or a == 2:
                    j = 0
                while (i <= 5) and (j <= 6):
                    if self.grid[i][j] == col:
                        count += 1
                        if count >= 4:
                            return True
                    else:
                        count = 0
                    i += 1
                    j += 1
        if count >= 4:
            return True
        else:
            return False

    def right_left_diagonal(self, col:str) -> bool:
        """ Returns if the player has connected4 colors in the diagonals from
        right to left.
        """
        count = 0
        for a in range(3):
            for b in range(3, 7):
                i = a
                j = b
                if a == 1 or a == 2:
                    j = 6
                while (i <= 5) and (j >= 0):
                    if self.grid[i][j] == col:
                        count += 1
                        if count >= 4:
                            return True
                    else:
                        count = 0
                    i += 1
                    j -= 1
        if count >= 4:
            return True
        else:
            return False


if __name__ == '__main__':

    name_1 = input(" Player 1, What is your name?\n")
    color_1 = input(" Player 1, What is your color?\n")
    name_2 = input("PLayer 2, What is your name?\n")
    color_2 = input("Player 2, What is your color?\n")
    while color_1 == color_2:
        color_2 = input(" Player 2, this color has been selected!\n"
                        "Choose a different color.\n")
    p1 = Player(name_1, color_1)
    p2 = Player(name_2, color_2)
    g = Game(p1, p2)
    g.play()
