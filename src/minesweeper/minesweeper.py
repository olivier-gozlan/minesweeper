""" This module implements the Minesweeper game. """
# minesweeper.py
import random

class Minesweeper:
    def __init__(self, rows:int, cols:int, num_mines:int):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [["" for _ in range(cols)] for _ in range(rows)]
        self.mines = set()
        self.revealed = set()
        self.place_mines()

    def place_mines(self)->None:
        while len(self.mines) < self.num_mines:
            r,c = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            if (r, c) not in self.mines:
                self.mines.add((r, c))
                self.board[r][c] =  '💣'

        for r, c in self.mines:
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if 0 <= i < self.rows and 0 <= j < self.cols and self.board[i][j] != '💣':
                        if self.board[i][j] == '':
                            self.board[i][j] = 1
                        else:
                            self.board[i][j] += 1

    def reveal(self, row:int, col:int) -> str:
        """ Reveal a cell on the board.
        Any adjacent cells with no mines are also revealed.
        Returns "Game Over" if a mine is revealed,"You win" is no more mine, "Continue" otherwise.
        """
        if(row,col) in self.revealed:
            return "Continue"

        self.revealed.add((row,col))
        if self.board[row][col]=='💣':
            return "Game Over"
        if self.board[row][col]=="":
            #case vide faut traiter case autour
            self._flood_fill(row,col)

        if self.is_winner():
            return "You win"

        return "Continue"


    def _flood_fill(self, row: int, col: int)->None:
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < self.rows and 0 <= j < self.cols and (i, j) not in self.revealed:
                    self.revealed.add((i, j))
                    if self.board[i][j] == "":
                        self._flood_fill(i, j)

    def get_board(self) -> list:
        """ Return the current state of the board. """
        visible_board=[]
        for r in range(self.rows):
            row_data=[]
            for c in range(self.cols):
                if (r,c) in self.revealed:
                    row_data.append(self.board[r][c]if self.board[r][c] != "" else " ")
                else:
                    row_data.append("■")
            visible_board.append(row_data)
        return visible_board


    def is_winner(self) -> bool:
        """ Check if the game has been won. """
        return len(self.revealed)==self.rows*self.cols-self.num_mines

    def restart(self) -> None:
        """ Restart the game with the same parameters. """
        self.__init__(self.rows, self.cols, self.num_mines)
